"""
news-barge/scraper/scrape.py

Reads sites.yaml, fetches articles (via feed or explicit URL list),
extracts the main content with trafilatura, converts to Markdown,
and writes dated .md files with YAML frontmatter.
"""

import argparse
import asyncio
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urljoin

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
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
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


def url_to_slug(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "--")
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
    # We want to identify them so we don't linkify the URL inside.
    # We'll use a substitution function to handle images vs URLs.
    pattern = r"(!\[.*?\]\(https?://[^\s\)]+\))|(https?://[^\s\)]+)|([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    excluded_imgs = ["placeholder image", "google preferred source"]

    def replace(match):
        img, url, email = match.groups()
        if img:
            # Check if it's a placeholder image (case-insensitive check for 'placeholder')
            for excluded in excluded_imgs:
                if excluded.lower() in img.lower():
                    return ""
            return img
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


def write_markdown(path: Path, frontmatter: dict, body: str) -> None:
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
    print(f"  ✓ {path.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------


async def fetch_html_aiohttp(url: str, session: aiohttp.ClientSession) -> str | None:
    """Lightweight fetch using aiohttp."""
    try:
        timeout = aiohttp.ClientTimeout(total=30)
        async with session.get(url, headers=FETCH_HEADERS, timeout=timeout) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        print(f"  ✗ HTTP fetch failed for {url}: {e}", file=sys.stderr)
        return None


async def fetch_html_playwright(
    url: str,
    browser,
    browser_semaphore: asyncio.Semaphore,
) -> str | None:
    """Full browser fetch for JS-heavy or anti-bot sites."""
    async with browser_semaphore:
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
            await page.close()
            await ctx.close()
            return html
        except Exception as e:
            print(f"  ✗ playwright fetch failed for {url}: {e}", file=sys.stderr)
            return None


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
    feed_url: str, limit: int, session: aiohttp.ClientSession
) -> list[str]:
    body = await fetch_html_aiohttp(feed_url, session)
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
):
    html = (
        await fetch_html_playwright(listing_url, browser, browser_semaphore)
        if use_playwright
        else await fetch_html_aiohttp(listing_url, session)
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
) -> bool:
    slug = url_to_slug(url)
    site_slug = site["slug"]
    use_playwright = site.get("force_playwright", False)

    print(f"  → {url}")

    async with fetch_semaphore:
        html = (
            await fetch_html_playwright(url, browser, browser_semaphore)
            if use_playwright
            else await fetch_html_aiohttp(url, session)
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
    md_body = clean_markdown_formatting(md_body)
    md_body = linkify_text(md_body)
    meta = await asyncio.to_thread(trafilatura.extract_metadata, html, default_url=url)

    # Fallback to first image in markdown if metadata image is missing
    image = None
    if meta and meta.image:
        image = meta.image
    else:
        image = extract_first_image_from_markdown(md_body)

    if not md_body:
        print(f"  ✗ extraction returned nothing for {url}", file=sys.stderr)
        return False

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
        print(f"  · already exists, skipping: {path.name}")
        return False

    if dry_run:
        print(f"  [dry-run] would write {path.relative_to(REPO_ROOT)}")
        return True

    await asyncio.to_thread(write_markdown, path, frontmatter, md_body)
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
            print(f"No site with slug '{args.site}' found.", file=sys.stderr)
            sys.exit(1)

    total_new = 0
    concurrency = args.concurrency or DEFAULT_CONCURRENCY
    browser_concurrency = args.browser_concurrency or DEFAULT_BROWSER_CONCURRENCY
    fetch_semaphore = asyncio.Semaphore(concurrency)
    browser_semaphore = asyncio.Semaphore(browser_concurrency)

    async with aiohttp.ClientSession() as session:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)

            for site in sites:
                print(f"\n{'─'*50}")
                print(f"Site: {site['name']} ({site['slug']})")

                urls = list(site.get("urls") or [])

                if "feed" in site:
                    limit = site.get("limit", site.get("feed_limit", 10))
                    print(f"  Fetching feed ({limit} items): {site['feed']}")
                    feed_urls = await urls_from_feed(site["feed"], limit, session)
                    print(f"  Found {len(feed_urls)} URLs in feed")
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
                    )
                    urls = listing_urls + urls

                if not urls:
                    print("  No URLs configured, skipping.")
                    continue

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
                    )
                    for url in urls
                ]

                for future in asyncio.as_completed(article_tasks):
                    if await future:
                        total_new += 1

            await browser.close()

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
