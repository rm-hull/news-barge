"""
News-barge scraper.

Reads sites.yaml, fetches articles (via feed or explicit URL list),
extracts the main content with trafilatura, converts to Markdown,
and writes dated .md files with YAML frontmatter.
"""

from __future__ import annotations

import argparse
import asyncio
import calendar
import hashlib
import os
import random
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock
from typing import Any, cast
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse

import aiohttp
import feedparser
import trafilatura
import yaml
from lxml import html as lxml_html
from markdownify import markdownify as to_markdown
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Route,
    async_playwright,
)
from taxotag import Gist
from tqdm.asyncio import tqdm

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
SITES_FILE = REPO_ROOT / "sites.yaml"
CONTENT_DIR = REPO_ROOT / "content"

TRAFILATURA_CONFIG = trafilatura.settings.use_config()
TRAFILATURA_CONFIG.set("DEFAULT", "EXTRACTION_TIMEOUT", "30")

FETCH_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

DEFAULT_CONCURRENCY = 10
DEFAULT_BROWSER_CONCURRENCY = 2
TAXOTAG_TOP_K = 3
taxotag: Gist = Gist()
taxotag_lock: Lock = Lock()


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
    def __init__(self, site_name: str, site_slug: str) -> None:
        self.site_name = site_name
        self.site_slug = site_slug
        self.logs: list[str] = []

    def log(self, message: str) -> None:
        self.logs.append(message)

    def error(self, message: str) -> None:
        if os.environ.get("GITHUB_ACTIONS") == "true":
            self.logs.append(f"::error::{message}")
        else:
            RED_BOLD = "\033[1;31m"
            RESET = "\033[0m"
            self.logs.append(f"{RED_BOLD}ERROR:{RESET} {message}")

    def info(self, message: str) -> None:
        self.log(message)


def report_error(message: str, logger: SiteLogger | None = None) -> None:
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


def url_to_slug(url: str, exclude_query_params: bool = False) -> str:
    parsed = urlparse(url)

    path = parsed.path.strip("/").replace("/", "--")

    # When the site requests it, skip query params entirely in the slug.
    # This avoids noisy or collision-prone suffixes from tracking / campaign
    # params that aren't useful for identifying the article.
    if not exclude_query_params:
        # Filter out utm_* query params
        query_params = parse_qsl(parsed.query)
        filtered_query_params = [
            (k, v) for k, v in query_params if not k.startswith("utm_")
        ]

        # Rebuild URL components without utm_*
        # We only need the path and filtered query for the slug
        filtered_query = urlencode(filtered_query_params)

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
    text = re.sub(r"(\*\*|\*)[ \t]+([^*\n]+?)[ \t]*\1", r"\1\2\1", text)
    # Matches: (** or *) + (content) + horizontal-space + (** or *)
    text = re.sub(r"(\*\*|\*)([^*\n]+?)[ \t]+\1", r"\1\2\1", text)

    # 2. Ensure a space follows closing tags if followed by alphanumeric
    # Target: **Header:**Hard -> **Header:** Hard
    # Use a negative lookahead to avoid matching across newlines
    text = re.sub(r"(\*\*|\*)([^\*\n]+?)\1([a-zA-Z0-9])", r"\1\2\1 \3", text)

    # 3. Remove empty bold tags
    text = re.sub(r"\*\*\s*\*\*", "", text)

    return text.strip()


def normalize_inline_spacing(extracted_html: str) -> str:
    """Move boundary whitespace outside inline formatting elements."""
    tree = lxml_html.fromstring(extracted_html)
    inline_elements = tree.xpath(".//em | .//strong | .//b | .//i")

    for element in inline_elements:
        if not element.text:
            continue

        leading = re.match(r"[ \t]+", element.text)
        if leading:
            whitespace = leading.group(0)
            element.text = element.text[len(whitespace) :]
            previous = element.getprevious()
            if previous is not None:
                previous.tail = (previous.tail or "") + whitespace
            else:
                parent = element.getparent()
                parent.text = (parent.text or "") + whitespace

        trailing = re.search(r"[ \t]+$", element.text)
        if trailing:
            whitespace = trailing.group(0)
            element.text = element.text[: -len(whitespace)]
            element.tail = whitespace + (element.tail or "")

    return cast(str, lxml_html.tostring(tree, encoding="unicode"))


# A bare ``attr="value"`` selector, e.g. ``role="dialog"``. The first group is
# the attribute name, the second its value (single- or double-quoted).
_EXCLUSION_ATTR_PATTERN: re.Pattern[str] = re.compile(
    r'^\s*([\w:-]+)\s*=\s*["\']([^"\']+)["\']\s*$'
)


def normalize_exclusion(expr: str) -> str:
    """Translate an ``exclusions`` entry into an XPath expression.

    Two forms are accepted:

    * A full XPath expression, used verbatim — e.g.
      ``//div[contains(@class, 'bookmark-experience')]`` or
      ``//script | //style``.
    * A bare attribute matcher — e.g. ``role="dialog"`` — which is expanded to
      ``//*[@role='dialog']`` for convenience.

    Anything that isn't a full XPath and doesn't look like an attribute
    matcher is returned unchanged so lxml can surface a clear error.
    """
    expr = expr.strip()
    # Already a full XPath expression (absolute path, relative path, or a
    # node-set operation / function call).
    if expr.startswith(("/", "//", "(", ".", "descendant")):
        return expr
    match = _EXCLUSION_ATTR_PATTERN.match(expr)
    if match:
        attr, value = match.group(1), match.group(2)
        return f"//*[@{attr}='{value}']"
    return expr


def remove_excluded_elements(
    html: str, exclusions: list[str], logger: SiteLogger | None = None
) -> str:
    """Detach every element matched by ``exclusions`` from ``html``.

    Each entry is either an XPath expression or a bare ``attr="value"``
    matcher (see :func:`normalize_exclusion`). Matching elements and their
    subtrees are removed *before* the HTML reaches trafilatura, so site
    chrome — paywall modals, bookmark prompts, subscribe overlays, etc. —
    never contaminates the extracted article.

    Returns the cleaned HTML string, or the original string untouched when
    ``exclusions`` is empty.
    """
    if not exclusions:
        return html

    tree = lxml_html.fromstring(html)
    # lxml_html.fromstring can return a list of elements when the input has
    # multiple top-level nodes (e.g. a fragment). Wrap those in a single root
    # so xpath + serialization stay consistent for the rest of the pipeline.
    if isinstance(tree, list):
        tree = lxml_html.fragment_fromstring(
            lxml_html.tostring(tree, encoding="unicode"),
            create_parent="div",
        )

    removed = 0
    for expr in exclusions:
        xpath = normalize_exclusion(expr)
        for element in tree.xpath(xpath):
            parent = element.getparent()
            if parent is not None:
                parent.remove(element)
                removed += 1

    if logger and removed:
        logger.log(
            f"  · excluded {removed} element(s) via {len(exclusions)} exclusion rule(s)"
        )

    return cast(str, lxml_html.tostring(tree, encoding="unicode"))


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

    def replace(match: re.Match[str]) -> str:
        img, link, url, email = match.groups()
        if img:
            # Check if it's a placeholder image (case-insensitive)
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


def classify_article(title: str, description: str) -> list[str]:
    text = "\n\n".join(part.strip() for part in (title, description) if part.strip())
    if not text:
        return []
    with taxotag_lock:
        topics = taxotag.classify(text, top_k=TAXOTAG_TOP_K)
    return [topic.name for topic in topics]


def months_ago(months: int = 1) -> datetime:
    """UTC cutoff `months` calendar-months ago, with the day clamped to the
    target month length (e.g. Aug 31 -> Jul 31, Mar 31 -> Feb 28).

    Mirrors GNU ``date -d "N months ago"`` so the scraper and the archive
    workflow agree on what "older than N months" means.
    """
    now = datetime.now(UTC)
    year, month = now.year, now.month - months
    while month <= 0:
        month += 12
        year -= 1
    while month > 12:
        month -= 12
        year += 1
    day = min(now.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day, tzinfo=UTC)


def output_path(
    site_slug: str,
    article_slug: str,
    date: datetime,
    output_dir: Path = CONTENT_DIR,
) -> Path:
    date_path = date.strftime("%Y/%m/%d")
    filename = f"{site_slug}--{article_slug}.md"
    return output_dir / date_path / filename


def write_markdown(
    path: Path, frontmatter: dict[str, Any], body: str, logger: SiteLogger
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
    display_path = (
        path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
    )
    logger.log(f"  ✓ {display_path}")


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------


async def fetch_html_aiohttp(
    url: str,
    session: aiohttp.ClientSession,
    logger: SiteLogger | None = None,
    headers: dict[str, str] | None = None,
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
    browser: Browser,
    browser_semaphore: asyncio.Semaphore,
    logger: SiteLogger | None = None,
) -> str | None:
    """Full browser fetch for JS-heavy or anti-bot sites."""
    async with browser_semaphore:
        ctx: BrowserContext | None = None
        page: Page | None = None
        try:
            ctx = await browser.new_context(
                user_agent=FETCH_HEADERS["User-Agent"],
                java_script_enabled=True,
                extra_http_headers={
                    "Accept-Language": FETCH_HEADERS["Accept-Language"]
                },
            )
            page = await ctx.new_page()

            async def abort_route(route: Route) -> None:
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
    logger: SiteLogger | None = None,
    site: dict[str, Any] | None = None,
) -> list[str]:
    # Use neutral headers for feeds to avoid being served HTML instead of XML
    feed_headers: dict[str, str] = {
        "User-Agent": "curl/7.81.0",
        "Accept": (
            "application/rss+xml,application/xml,text/xml,"
            "application/xhtml+xml,text/html;q=0.9,*/*;q=0.8"
        ),
    }
    ssl = not site.get("trust_insecure_certs", False) if site else True
    body = await fetch_html_aiohttp(
        feed_url,
        session,
        logger=logger,
        headers=feed_headers,
        allow_redirects=True,
        ssl=ssl,
    )
    if not body:
        return []

    parsed = feedparser.parse(body)
    entries = parsed.entries[:limit]
    urls: list[str] = []
    for entry in entries:
        link = entry.get("link") or entry.get("id")
        if link:
            urls.append(link)
    return urls


async def urls_from_listing(
    listing_url: str,
    pattern: str | None,
    limit: int,
    use_playwright: bool,
    session: aiohttp.ClientSession,
    browser: Browser,
    browser_semaphore: asyncio.Semaphore,
    listing_class: str | None = None,
    resolve_relative_to_root: bool = False,
    logger: SiteLogger | None = None,
    site: dict[str, Any] | None = None,
) -> list[str]:
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
        # Find all elements with the specified class, then find all <a> tags
        links = tree.xpath(
            f"//*[contains(concat(' ', normalize-space(@class)"
            f", ' '), ' {listing_class} ')]//a[@href]"
        )
    else:
        links = tree.xpath("//a[@href]")

    parsed_base = urlparse(listing_url)
    root_url = f"{parsed_base.scheme}://{parsed_base.netloc}/"

    urls: list[str] = []
    for link in links:
        href = link.get("href")
        if href is None:
            continue

        # If resolve_relative_to_root is True and link is relative, resolve from root
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
    seen: set[str] = set()
    unique_urls: list[str] = []
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
    site: dict[str, Any],
    dry_run: bool,
    force: bool,
    session: aiohttp.ClientSession,
    browser: Browser,
    browser_semaphore: asyncio.Semaphore,
    fetch_semaphore: asyncio.Semaphore,
    logger: SiteLogger,
    retention_months: int = 1,
    output_dir: Path = CONTENT_DIR,
) -> bool:
    slug = url_to_slug(url, site.get("exclude_query_params", False))
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

    # Strip site-level chrome (modals, bookmark prompts, paywall overlays,
    # etc.) from the *raw page* before trafilatura sees it. Doing it here —
    # rather than on trafilatura's output — means the unwanted elements are
    # gone before content heuristics run, so their text never merges into the
    # extracted article prose.
    exclusions = site.get("exclusions") or []
    if exclusions:
        html = remove_excluded_elements(html, exclusions, logger=logger)

    extracted_html = await asyncio.to_thread(
        trafilatura.extract,
        html,
        url=url,
        output_format="html",
        include_comments=False,
        include_formatting=True,
        include_images=True,
        include_tables=True,
        favor_precision=True,
        config=TRAFILATURA_CONFIG,
    )

    if not extracted_html:
        report_error(f"extraction returned nothing for {url}", logger=logger)
        return False

    extracted_html = normalize_inline_spacing(extracted_html)
    md_body = to_markdown(extracted_html, heading_style="ATX")
    md_body = clean_markdown_formatting(md_body)
    md_body = linkify_text(md_body)
    meta = await asyncio.to_thread(trafilatura.extract_metadata, html, default_url=url)

    # Fallback to first image in markdown if metadata image is missing
    image: str | None = None
    if meta and meta.image:
        image = meta.image
    else:
        image = extract_first_image_from_markdown(md_body)

    now = datetime.now(UTC)
    pub_date: datetime | None = None
    if meta and meta.date:
        try:
            pub_date = datetime.fromisoformat(meta.date.replace("Z", "+00:00"))
        except ValueError:
            pass
    file_date = pub_date or now

    title = (meta.title if meta else None) or slug
    if title:
        suffix = site.get("remove_suffix")
        if suffix and title.endswith(suffix):
            title = title[: -len(suffix)].strip()
        if "|" in title:
            title = title.split("|")[0].strip()
    description = (meta.description if meta else None) or ""
    generated_categories = await asyncio.to_thread(classify_article, title, description)
    categories = list(
        dict.fromkeys((site.get("categories") or []) + generated_categories)
    )

    frontmatter: dict[str, Any] = {
        "title": title,
        "source_url": url,
        "source_site": site["name"],
        "source_slug": site_slug,
        "scraped_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "published": file_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "description": description,
        "categories": categories,
        "image": image,
    }

    path = output_path(site_slug, slug, file_date, output_dir=output_dir)

    # Don't create articles older than the retention window. The archive job
    # deletes them anyway, so writing them only creates churn — and an archive
    # dry-run preview is meant to show exactly the articles that survive here.
    if retention_months > 0:
        cutoff = months_ago(retention_months)
        if file_date.date() < cutoff.date():
            logger.log(
                f"  · older than {retention_months} month(s) "
                f"(published {file_date.date()} < {cutoff.date()}), skipping"
            )
            return False

    if path.exists() and not force:
        logger.log(f"  · already exists, skipping: {path.name}")
        return False

    if dry_run:
        display_path = (
            path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        )
        logger.log(f"  [dry-run] would write {display_path}")
        return True

    await asyncio.to_thread(write_markdown, path, frontmatter, md_body, logger)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def load_sites(path: Path = SITES_FILE) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return cast(list[dict[str, Any]], data.get("sites", []))


async def main_async(args: argparse.Namespace) -> None:
    sites = load_sites(args.config)
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

    site_loggers: dict[str, SiteLogger] = {}
    all_tasks: list[tuple[str, dict[str, Any], SiteLogger]] = []

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
                        f" | Listing {site['listing_url']} -> "
                        f"found {len(listing_urls)} URLs",
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
                seen_urls: set[str] = set()
                deduped_urls: list[str] = []
                for u in urls:
                    if u not in seen_urls:
                        deduped_urls.append(u)
                        seen_urls.add(u)
                urls = deduped_urls

                # Log discovery to the stashed logger for the final grouped report
                logger.log(f"\n{'─' * 50}")
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
                    retention_months=args.retention_months,
                    output_dir=args.output_dir,
                )
                for url, site, logger in all_tasks
            ]

            is_gh = os.environ.get("GITHUB_ACTIONS") == "true"
            tqdm_kwargs: dict[str, Any] = {
                "total": len(article_tasks),
                "desc": "Processing articles",
            }
            if is_gh:
                # In GH Actions, update less frequently (simpler format)
                tqdm_kwargs["mininterval"] = 10  # Update every 10 seconds
                tqdm_kwargs["bar_format"] = (
                    "{desc}: {percentage:3.0f}%|{elapsed}<{remaining}, "
                    "{n_fmt}/{total_fmt} [{elapsed}]"
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

    print(f"\n{'─' * 50}")
    print(f"Done. {total_new} new article(s) written.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape sites → Markdown")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--site", help="Only process this slug")
    parser.add_argument(
        "--config",
        type=Path,
        default=SITES_FILE,
        help="Path to sites.yaml (default: repo root sites.yaml)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=CONTENT_DIR,
        help="Directory to write article Markdown files (default: repo root content/)",
    )
    parser.add_argument(
        "--force", action="store_true", help="Force regeneration of existing files"
    )
    parser.add_argument(
        "--retention-months",
        type=int,
        default=1,
        help="Don't write articles older than this many months (default: 1)",
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
