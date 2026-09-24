"""
News-barge scraper.

Reads sites.yaml, fetches articles (via feed or explicit URL list),
extracts the main content with trafilatura, converts to Markdown,
and writes dated .md files with YAML frontmatter.
"""

from __future__ import annotations

__all__ = [
    "main",
    "main_async",
]

import argparse
import asyncio
import os
import random
import re
import sys
from pathlib import Path
from typing import Any, cast

import aiohttp
import feedparser
import yaml
from lxml import html as lxml_html
from playwright.async_api import Browser, async_playwright
from tqdm.asyncio import tqdm

from .constants import (
    CONTENT_DIR,
    DEFAULT_BROWSER_CONCURRENCY,
    DEFAULT_CONCURRENCY,
    REPO_ROOT,
    SITES_FILE,
    TAXOTAG_TOP_K,
    taxotag,
    taxotag_lock,
)
from .fetchers import (
    fetch_html_aiohttp,
    fetch_html_playwright,
)
from .log_helper import (
    SiteLogger,
    report_error,
    report_group,
)
from .pipeline import process_article

# ---------------------------------------------------------------------------
# Feed handlers
# ---------------------------------------------------------------------------


async def urls_from_feed(
    feed_url: str,
    limit: int,
    session: aiohttp.ClientSession,
    logger: SiteLogger | None = None,
    site: dict[str, Any] | None = None,
) -> list[str]:
    """Fetch URLs from an RSS/Atom feed."""
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
    """Discover article URLs from a listing page."""
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
        links = tree.xpath(
            f"//*[contains(concat(' ', normalize-space(@class)"
            f", ' '), ' {listing_class} ')]//a[@href]"
        )
    else:
        links = tree.xpath("//a[@href]")

    from urllib.parse import urljoin, urlparse

    parsed_base = urlparse(listing_url)
    root_url = f"{parsed_base.scheme}://{parsed_base.netloc}/"

    urls: list[str] = []
    for link in links:
        href = link.get("href")
        if href is None:
            continue

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


def classify_article(title: str, description: str) -> list[str]:
    """Classify an article using taxotag."""
    text = "\n\n".join(part.strip() for part in (title, description) if part.strip())
    if not text:
        return []
    with taxotag_lock:
        topics = taxotag.classify(text, top_k=TAXOTAG_TOP_K)
    return [topic.name for topic in topics]


def write_markdown(
    path: Path, frontmatter: dict[str, Any], body: str, logger: SiteLogger
) -> None:
    """Write a markdown file with YAML frontmatter."""
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
                tqdm_kwargs["mininterval"] = 10
                tqdm_kwargs["bar_format"] = (
                    "{desc}: {percentage:3.0f}%|{elapsed}<{remaining}, "
                    "{n_fmt}/{total_fmt} [{elapsed}]"
                )

            for future in tqdm(asyncio.as_completed(article_tasks), **tqdm_kwargs):
                if await future:
                    total_new += 1

            await browser.close()

    # Print stashed logs grouped by site
    for site_slug in sorted(site_loggers.keys()):
        logger = site_loggers[site_slug]
        if not logger.logs:
            continue

        with report_group(f"Site: {logger.site_name} ({logger.site_slug})"):
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
