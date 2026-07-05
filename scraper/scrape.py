"""
news-barge/scraper/scrape.py

Reads sites.yaml, fetches articles (via feed or explicit URL list),
extracts the main content with trafilatura, converts to Markdown,
and writes dated .md files with YAML frontmatter.
"""

import argparse
import asyncio
import hashlib
import os
import re
import sys
import random
from tqdm.asyncio import tqdm
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urljoin, urlunparse, urlencode, parse_qsl

import aiohttp
import feedparser
import trafilatura
from lxml import html as lxml_html
import yaml
from playwright.async_api import async_playwright

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
SITES_FILE = REPO_ROOT / "sites.yaml"
CONTENT_DIR = REPO_ROOT / "content"

TRAFILATURA_CONFIG = trafilatura.settings.use_config()
TRAFILATURA_CONFIG.set("DEFAULT", "EXTRACTION_TIMEOUT", "30")

FETCH_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

DEFAULT_CONCURRENCY = 10
DEFAULT_BROWSER_CONCURRENCY = 2


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


class SiteLogger:
    def __init__(self, site_name: str, site_slug: str):
        self.site_name = site_name
        self.site_slug = site_slug
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)

    def error(self, message: str):
        if os.environ.get("GITHUB_ACTIONS") == "true":
            self.logs.append(f"::error::{message}")
        else:
            RED_BOLD = "\033[1;31m"
            RESET = "\033[0m"
            self.logs.append(f"{RED_BOLD}ERROR:{RESET} {message}")

    def info(self, message: str):
        self.log(message)


def report_error(message: str, logger: SiteLogger = None) -> None:
    """Prints an error message to stderr with colors and GitHub Actions support."""
    if logger:
        logger.error(message)
    elif os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::error::{message}", file=sys.stderr)
    else:
        # ANSI codes: Bold Red
        RED_BOLD = "\033[1;31m"
        RESET = "\033[0m"

        formatted_msg = f"{RED_BOLD}ERROR:{RESET} {message}"
        print(formatted_msg, file=sys.stderr)


def report_group_start(name: str) -> None:
    """Starts a GitHub Actions log group."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::group::{name}")


def report_group_end() -> None:
    """Ends a GitHub Actions log group."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("::endgroup::")


def url_to_slug(url: str) -> str:
    parsed = urlparse(url)

    # Filter out utm_* query params
    query_params = parse_qsl(parsed.query)
    filtered_query_params = [
        (k, v) for k, v in query_params if not k.startswith("utm_")
    ]

    # Rebuild URL components without utm_*
    # We only need the path and filtered query for the slug
    filtered_query = urlencode(filtered_query_params)

    path = parsed.path.strip("/").replace("/", "--")

    # Handle URLs where the identity is in the query string (e.g., ?id=123)
    if filtered_query:
        # Use the filtered query string as part of the slug to avoid collisions
        # when the path is identical for all articles.
        query_slug = slugify(filtered_query).replace("=", "--").replace("&", "--")
        path = f"{path}--{query_slug}"

    short = slugify(path) or hashlib.sha1(url.encode()).hexdigest()[:10]
    return short


def clean_markdown_formatting(text: str) -> str:
    """
    Fixes markdown formatting issues to improve compatibility with Eleventy.
    """
    if not text:
        return ""

    # Remove extraction cruft
    text = re.sub(
        r"^\s*[\*\-]\s*Published\s*\n", "\n", text, flags=re.MULTILINE | re.IGNORECASE
    )
    text = re.sub(
        r"\*\*Recommended reading:\*\*", "\n", text, flags=re.MULTILINE | re.IGNORECASE
    )

    # 1. Normalize internal spacing (strip spaces inside tags, NO NEWLINES)
    # Matches: (** or *) + horizontal-space + (content) + horizontal-space + (** or *)
    text = re.sub(r"(\*\*|\*)[ \t]+(.+?)[ \t]*\1", r"\1\2\1", text)
    # Matches: (** or *) + (content) + horizontal-space + (** or *)
    text = re.sub(r"(\*\*|\*)(.+?)[ \t]+\1", r"\1\2\1", text)

    # 2. Ensure a space follows closing tags if followed by alphanumeric
    # Target: **Header:**Hard -> **Header:** Hard
    # Use a negative lookahead to avoid matching across newlines
    text = re.sub(r"(\*\*|\*)([^\*\n]+?)\1([a-zA-Z0-9])", r"\1\2\1 \3", text)

    # 3. Remove empty bold tags
    text = re.sub(r"\*\*\s*\*\*", "", text)

    return text.strip()


def linkify_text(text: str) -> str:
    if not text:
        return ""

    # Regex for Markdown images: ![alt](url)
    # Regex for Markdown links: [text](url)
    # We want to identify them so we don't linkify the URL inside either.
    pattern = (
        r"(!\[.*?\]\(https?://[^\s\)]+\))"  # 1: image
        r"|(\[.*?\]\(https?://[^\s\)]+\))"  # 2: existing link
        r"|(https?://[^\s\)]+)"  # 3: bare url
        r"|([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"  # 4: email
    )
    excluded_imgs = ["placeholder image", "google preferred source"]

    def replace(match):
        img, link, url, email = match.groups()
        if img:
            # Check if it's a placeholder image (case-insensitive check for 'placeholder')
            for excluded in excluded_imgs:
                if excluded.lower() in img.lower():
                    return ""
            return img
        if link:
            # Already a proper markdown link — leave it alone.
            return link
        if url:
            return f"[{url}]({url})"
        if email:
            return f"[{email}](mailto:{email})"
        return match.group(0)

    return re.sub(pattern, replace, text)


def output_path(site_slug: str, article_slug: str, date: datetime) -> Path:
    date_path = date.strftime("%Y/%m/%d")
    filename = f"{site_slug}--{article_slug}.md"
    return CONTENT_DIR / date_path / filename


def write_markdown(
    path: Path, frontmatter: dict, body: str, logger: SiteLogger
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_yaml = yaml.dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    path.write_text(
        "---\n" + fm_yaml + "---\n\n" + body.strip() + "\n", encoding="utf-8"
    )
    logger.log(f"  ✓ {path.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------


async def fetch_html_aiohttp(
    url: str,
    session: aiohttp.ClientSession,
    logger: SiteLogger = None,
    headers: dict | None = None,
    allow_redirects: bool = True,
    ssl: bool = True,
) -> str | None:
    """Lightweight fetch using aiohttp."""
    try:
        timeout = aiohttp.ClientTimeout(total=30)
        request_headers = headers if headers is not None else FETCH_HEADERS
        async with session.get(
            url,
            headers=request_headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
        ) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        report_error(f"HTTP fetch failed for {url}: {e}", logger=logger)
        return None


async def fetch_html_playwright(
    url: str,
    browser,
    browser_semaphore: asyncio.Semaphore,
    logger: SiteLogger = None,
) -> str | None:
    """Full browser fetch for JS-heavy or anti-bot sites."""
    async with browser_semaphore:
        ctx = None
        page = None
        try:
            ctx = await browser.new_context(
                user_agent=FETCH_HEADERS["User-Agent"],
                java_script_enabled=True,
                extra_http_headers={
                    "Accept-Language": FETCH_HEADERS["Accept-Language"]
                },
            )
            page = await ctx.new_page()

            async def abort_route(route):
                await route.abort()

            await page.route(
                "**/{analytics,doubleclick,googlesyndication,adservice,tracking}**",
                abort_route,
            )
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            html = await page.content()
            return html
        except Exception as e:
            report_error(f"playwright fetch failed for {url}: {e}", logger=logger)
            return None
        finally:
            # Always release page/context resources, even on failure, to
            # avoid leaking browser contexts over a long-running batch.
            if page is not None:
                try:
                    await page.close()
                except Exception:
                    pass
            if ctx is not None:
                try:
                    await ctx.close()
                except Exception:
                    pass


def extract_first_image_from_markdown(md: str) -> str | None:
    """Finds the first image in Markdown text: ![alt](url)."""
    # Regex for ![alt](url)
    match = re.search(r"!\[.*?\]\((https?://[^\s\)]+)\)", md)
    if match:
        return match.group(1)
    return None


# ---------------------------------------------------------------------------
# Feed handling
# ---------------------------------------------------------------------------


async def urls_from_feed(
    feed_url: str,
    limit: int,
    session: aiohttp.ClientSession,
    logger: SiteLogger = None,
    site: dict = None,
) -> list[str]:
    # Use neutral headers for feeds to avoid being served HTML instead of XML
    feed_headers = {
        "User-Agent": "curl/7.81.0",
        "Accept": "application/rss+xml,application/xml,text/xml,application/xhtml+xml,text/html;q=0.9,*/*;q=0.8",
    }
    ssl = not site.get("trust_insecure_certs", False) if site else True
    body = await fetch_html_aiohttp(
        feed_url,
        session,
        logger=logger,
        headers=feed_headers,
        allow_redirects=False,
        ssl=ssl,
    )
    if not body:
        return []

    parsed = feedparser.parse(body)
    entries = parsed.entries[:limit]
    urls = []
    for entry in entries:
        link = entry.get("link") or entry.get("id")
        if link:
            urls.append(link)
    return urls


async def urls_from_listing(
    listing_url,
    pattern,
    limit,
    use_playwright,
    session: aiohttp.ClientSession,
    browser,
    browser_semaphore: asyncio.Semaphore,
    listing_class=None,
    resolve_relative_to_root=False,
    logger: SiteLogger = None,
    site: dict = None,
):
    ssl = not site.get("trust_insecure_certs", False) if site else True
    html = (
        await fetch_html_playwright(
            listing_url, browser, browser_semaphore, logger=logger
        )
        if use_playwright
        else await fetch_html_aiohttp(listing_url, session, logger=logger, ssl=ssl)
    )
    if not html:
        return []

    tree = lxml_html.fromstring(html)

    if listing_class:
        # Find all elements with the specified class, then find all <a> tags within them
        links = tree.xpath(
            f"//*[contains(concat(' ', normalize-space(@class), ' '), ' {listing_class} ')]//a[@href]"
        )
    else:
        links = tree.xpath("//a[@href]")

    parsed_base = urlparse(listing_url)
    root_url = f"{parsed_base.scheme}://{parsed_base.netloc}/"

    urls = []
    for link in links:
        href = link.get("href")

        # If resolve_relative_to_root is True and the link is relative (no leading slash, no scheme)
        if (
            resolve_relative_to_root
            and href
            and not href.startswith(("/", "http", "mailto", "tel"))
        ):
            full_url = urljoin(root_url, href)
        else:
            full_url = urljoin(listing_url, href)

        if pattern:
            if re.search(pattern, full_url):
                urls.append(full_url)
            else:
                continue
        else:
            urls.append(full_url)

    # Deduplicate while preserving order
    seen = set()
    unique_urls = []
    for u in urls:
        if u not in seen:
            unique_urls.append(u)
            seen.add(u)

    return unique_urls[:limit]


# ---------------------------------------------------------------------------
# Per-article pipeline
# ---------------------------------------------------------------------------


async def process_article(
    url: str,
    site: dict,
    dry_run: bool,
    force: bool,
    session: aiohttp.ClientSession,
    browser,
    browser_semaphore: asyncio.Semaphore,
    fetch_semaphore: asyncio.Semaphore,
    logger: SiteLogger,
) -> bool:
    slug = url_to_slug(url)
    site_slug = site["slug"]
    use_playwright = site.get("force_playwright", False)

    logger.log(f"  → {url}")

    async with fetch_semaphore:
        ssl = not site.get("trust_insecure_certs", False)
        html = (
            await fetch_html_playwright(url, browser, browser_semaphore, logger=logger)
            if use_playwright
            else await fetch_html_aiohttp(url, session, logger=logger, ssl=ssl)
        )

    if not html:
        return False

    md_body = await asyncio.to_thread(
        trafilatura.extract,
        html,
        url=url,
        output_format="markdown",
        include_comments=False,
        include_images=True,
        include_tables=True,
        favor_precision=True,
        config=TRAFILATURA_CONFIG,
    )

    if not md_body:
        report_error(f"extraction returned nothing for {url}", logger=logger)
        return False

    md_body = clean_markdown_formatting(md_body)
    md_body = linkify_text(md_body)
    meta = await asyncio.to_thread(trafilatura.extract_metadata, html, default_url=url)

    # Fallback to first image in markdown if metadata image is missing
    image = None
    if meta and meta.image:
        image = meta.image
    else:
        image = extract_first_image_from_markdown(md_body)

    now = datetime.now(timezone.utc)
    pub_date = None
    if meta and meta.date:
        try:
            pub_date = datetime.fromisoformat(meta.date.replace("Z", "+00:00"))
        except ValueError:
            pass
    file_date = pub_date or now

    title = (meta.title if meta else None) or slug
    description = (meta.description if meta else None) or ""

    frontmatter = {
        "title": title,
        "source_url": url,
        "source_site": site["name"],
        "source_slug": site_slug,
        "scraped_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "published": file_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "description": description,
        "image": image,
    }

    path = output_path(site_slug, slug, file_date)

    if path.exists() and not force:
        logger.log(f"  · already exists, skipping: {path.name}")
        return False

    if dry_run:
        logger.log(f"  [dry-run] would write {path.relative_to(REPO_ROOT)}")
        return True

    await asyncio.to_thread(write_markdown, path, frontmatter, md_body, logger)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def load_sites() -> list[dict]:
    with open(SITES_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("sites", [])


async def main_async(args):
    sites = load_sites()
    if args.site:
        sites = [s for s in sites if s["slug"] == args.site]
        if not sites:
            report_error(f"No site with slug '{args.site}' found.")
            sys.exit(1)

    total_new = 0
    concurrency = args.concurrency or DEFAULT_CONCURRENCY
    browser_concurrency = args.browser_concurrency or DEFAULT_BROWSER_CONCURRENCY
    fetch_semaphore = asyncio.Semaphore(concurrency)
    browser_semaphore = asyncio.Semaphore(browser_concurrency)

    site_loggers = {}
    all_tasks = []

    async with aiohttp.ClientSession() as session:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)

            # Phase 1 & 2: Discovery
            for site in sites:
                site_slug = site["slug"]
                logger = SiteLogger(site["name"], site_slug)
                site_loggers[site_slug] = logger

                print(f"Discovery: {site['name']} ({site['slug']})", end="", flush=True)

                urls = list(site.get("urls") or [])
                initial_count = len(urls)

                if "feed" in site:
                    limit = site.get("limit", site.get("feed_limit", 10))
                    feed_urls = await urls_from_feed(
                        site["feed"], limit, session, logger=logger, site=site
                    )
                    print(
                        f" | Feed {site['feed']}: found {len(feed_urls)} URLs",
                        end="",
                        flush=True,
                    )
                    urls = feed_urls + urls

                if "listing_url" in site:
                    use_playwright = site.get("force_playwright", False)
                    limit = site.get("limit", site.get("listing_limit", 10))
                    pattern = site.get("listing_link_pattern", "")
                    listing_class = site.get("listing_class")
                    resolve_relative_to_root = site.get(
                        "resolve_relative_to_root", False
                    )
                    listing_urls = await urls_from_listing(
                        site["listing_url"],
                        pattern,
                        limit,
                        use_playwright,
                        session,
                        browser,
                        browser_semaphore,
                        listing_class,
                        resolve_relative_to_root,
                        logger=logger,
                        site=site,
                    )
                    print(
                        f" | Listing {site['listing_url']}: found {len(listing_urls)} URLs",
                        end="",
                        flush=True,
                    )
                    urls = listing_urls + urls

                print()  # Newline after all sources for this site are printed

                if not urls:
                    logger.log("  No URLs configured, skipping.")
                    continue

                # Deduplicate URLs discovered across feed / listing / static
                # sources for this site, preserving order.
                seen_urls = set()
                deduped_urls = []
                for u in urls:
                    if u not in seen_urls:
                        deduped_urls.append(u)
                        seen_urls.add(u)
                urls = deduped_urls

                # Log discovery to the stashed logger for the final grouped report
                logger.log(f"\n{'─'*50}")
                logger.log(f"Site: {site['name']} ({site['slug']})")
                if "feed" in site:
                    logger.log(f"  Fetching feed: {site['feed']}")
                if "listing_url" in site:
                    logger.log(f"  Fetching listing: {site['listing_url']}")
                logger.log(f"  Total URLs discovered: {len(urls)}")

                for url in urls:
                    all_tasks.append((url, site, logger))

            # Phase 3: Shuffle
            random.shuffle(all_tasks)

            # Phase 4: Processing
            article_tasks = [
                process_article(
                    url,
                    site,
                    dry_run=args.dry_run,
                    force=args.force,
                    session=session,
                    browser=browser,
                    browser_semaphore=browser_semaphore,
                    fetch_semaphore=fetch_semaphore,
                    logger=logger,
                )
                for url, site, logger in all_tasks
            ]

            is_gh = os.environ.get("GITHUB_ACTIONS") == "true"
            tqdm_kwargs = {
                "total": len(article_tasks),
                "desc": "Processing articles",
            }
            if is_gh:
                # In GH Actions, update less frequently and use a simpler format without the bar
                tqdm_kwargs["mininterval"] = 10  # Update every 10 seconds
                tqdm_kwargs["bar_format"] = (
                    "{desc}: {percentage:3.0f}%|{elapsed}<{remaining}, {n_fmt}/{total_fmt} [{elapsed}]"
                )
            else:
                # Keep the nice default progress bar for the console
                pass

            for future in tqdm(asyncio.as_completed(article_tasks), **tqdm_kwargs):
                if await future:
                    total_new += 1

            await browser.close()

    # Print stashed logs grouped by site
    for site_slug in sorted(site_loggers.keys()):
        logger = site_loggers[site_slug]
        if not logger.logs:
            continue

        if os.environ.get("GITHUB_ACTIONS") == "true":
            report_group_start(f"Site: {logger.site_name} ({logger.site_slug})")
            for line in logger.logs:
                print(line)
            report_group_end()
        else:
            # Mimic the layout: newline and separator are already in logger.logs[0]
            # but we need to make sure we print them.
            for line in logger.logs:
                print(line)

    print(f"\n{'─'*50}")
    print(f"Done. {total_new} new article(s) written.")


def main():
    parser = argparse.ArgumentParser(description="Scrape sites → Markdown")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--site", help="Only process this slug")
    parser.add_argument(
        "--force", action="store_true", help="Force regeneration of existing files"
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help="Number of concurrent fetches to run",
    )
    parser.add_argument(
        "--browser-concurrency",
        type=int,
        default=DEFAULT_BROWSER_CONCURRENCY,
        help="Number of concurrent Playwright browser fetches",
    )
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
