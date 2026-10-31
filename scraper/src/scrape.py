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
import tempfile
from pathlib import Path
from typing import Any

import aiohttp

# Pre-import dateparser to avoid lazy-import deadlocks under high
# concurrency (GitHub issue #32, run 38850341610).
import dateparser  # noqa: F401
import feedparser
import yaml
from lxml import html as lxml_html
from playwright.async_api import Browser, BrowserContext, Route, async_playwright
from tqdm.asyncio import tqdm

from .constants import (
    BLOCKED_REQUEST_KEYWORDS,
    CONTENT_DIR,
    DEFAULT_BROWSER_CONCURRENCY,
    DEFAULT_CONCURRENCY,
    FETCH_HEADERS,
    REPO_ROOT,
    SITES_FILE,
)
from .fetchers import (
    fetch_html_aiohttp,
    fetch_html_playwright,
)
from .log_helper import (
    SiteLogger,
    report_error,
    report_group,
    report_notice,
    write_step_summary,
)
from .pipeline import extract_article_from_html, process_article
from .profiling import format_profile_stats
from .sites import SiteConfig
from .slugs import url_to_slug
from .text_extraction import (
    remove_excluded_elements,
    resolve_srcset_images,
)

# ---------------------------------------------------------------------------
# Existing articles index
# ---------------------------------------------------------------------------


def build_existing_slugs_map(
    output_dir: Path = CONTENT_DIR,
) -> dict[str, set[str]]:
    """Walk the content directory and build a map of site_slug -> set of article slugs.

    Scans all .md files under ``output_dir`` (structured as
    ``YYYY/MM/DD/site--article.md``) and extracts the site slug and article
    slug from each filename.  Returns a dict mapping each site slug to the set
    of article slugs that already have a file on disk.
    """
    existing: dict[str, set[str]] = {}
    if not output_dir.is_dir():
        return existing

    for md_path in output_dir.rglob("*.md"):
        stem = md_path.stem  # e.g. "guardian--some-article-slug"
        parts = stem.split("--", 1)
        if len(parts) == 2:
            site_slug, article_slug = parts
            existing.setdefault(site_slug, set()).add(article_slug)

    return existing


# ---------------------------------------------------------------------------
# Feed handlers
# ---------------------------------------------------------------------------


async def urls_from_feed(
    feed_url: str,
    limit: int,
    session: aiohttp.ClientSession,
    logger: SiteLogger | None = None,
    site: SiteConfig | None = None,
) -> list[str]:
    """Fetch URLs from an RSS/Atom feed."""
    feed_headers: dict[str, str] = {
        "User-Agent": "curl/7.81.0",
        "Accept": (
            "application/rss+xml,application/xml,text/xml,"
            "application/xhtml+xml,text/html;q=0.9,*/*;q=0.8"
        ),
    }
    ssl = not site.trust_insecure_certs if site else True
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
    context: BrowserContext,
    browser_semaphore: asyncio.Semaphore,
    listing_class: str | None = None,
    resolve_relative_to_root: bool = False,
    logger: SiteLogger | None = None,
    site: SiteConfig | None = None,
) -> list[str]:
    """Discover article URLs from a listing page."""
    ssl = not site.trust_insecure_certs if site else True
    if use_playwright:
        async with browser_semaphore:
            html = await fetch_html_playwright(listing_url, context, logger=logger)
    else:
        html = await fetch_html_aiohttp(listing_url, session, logger=logger, ssl=ssl)
    if not html:
        return []

    tree = lxml_html.fromstring(html)

    if listing_class:
        links = tree.xpath(
            "//*[contains(concat(' ', normalize-space(@class), ' '), $cls)]//a[@href]",
            cls=f" {listing_class} ",
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


# Analytics/ad URL matcher.  Instead of a glob pattern (which only catches
# keywords in the URL *path*), this predicate checks the full URL — including
# the hostname — so domains like cdn.taboola.com or cmp.inmobi.com are blocked
# even when the keyword appears outside the path.  Registered once on the
# shared context so every page inherits the blocking rule.
def _is_blocked_request(url: str) -> bool:
    """Return True if *url* matches any analytics/ad/tracking keyword."""
    url_lower = url.lower()
    return any(kw in url_lower for kw in BLOCKED_REQUEST_KEYWORDS)


async def _create_shared_context(browser: Browser) -> BrowserContext:
    """Create the single reusable Playwright context for a scrape run.

    Opens one ``BrowserContext`` off ``browser`` with the project User-Agent,
    JS enabled, and an Accept-Language header, then registers the analytics/ad
    route on it so *all* pages opened from it inherit the blocking rule (rather
    than registering it per-page inside ``fetch_html_playwright``).

    Args:
        browser: A launched Playwright ``Browser``.

    Returns:
        The shared ``BrowserContext`` (closed once in ``main_async``).
    """
    context = await browser.new_context(
        user_agent=FETCH_HEADERS["User-Agent"],
        java_script_enabled=True,
        extra_http_headers={"Accept-Language": FETCH_HEADERS["Accept-Language"]},
    )

    async def _route(route: Route) -> None:
        # Never abort the main document navigation — a legitimate article
        # URL may contain a blocked keyword (e.g. "tracking" in the path).
        if route.request.resource_type == "document":
            return
        if route.request.resource_type in {
            "image",
            "media",
            "font",
        } or _is_blocked_request(route.request.url):
            try:
                await route.abort()
            except Exception:
                # Page/context already closed; nothing to do.
                pass
        else:
            await route.continue_()

    await context.route("*", _route)
    return context


# ---------------------------------------------------------------------------
# Debug mode
# ---------------------------------------------------------------------------


async def _debug_url(args: argparse.Namespace) -> None:
    """Debug mode: fetch a single URL, process it, and print the result.

    Saves the raw HTML to a temp file for inspection, then runs the full
    extraction pipeline (exclusions, srcset resolution, trafilatura, markdown
    conversion) and prints the resulting markdown to stdout.
    """
    if not args.site:
        report_error("--debug-url requires --site to specify the site slug.")
        sys.exit(1)

    sites = SiteConfig.load_sites(args.config)
    site = next((s for s in sites if s.slug == args.site), None)
    if site is None:
        report_error(f"No site with slug '{args.site}' found.")
        sys.exit(1)

    url = args.debug_url
    logger = SiteLogger(site.name, site.slug)
    print(f"Debug mode: processing {url} with site '{site.slug}'")

    async with aiohttp.ClientSession() as session:
        ssl = not site.trust_insecure_certs
        if site.force_playwright:
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch(headless=True)
                context = await _create_shared_context(browser)
                html = await fetch_html_playwright(
                    url,
                    context,
                    logger=logger,
                    wait_until=site.playwright_wait_until,
                )
                await context.close()
                await browser.close()
        else:
            html = await fetch_html_aiohttp(url, session, logger=logger, ssl=ssl)

    if not html:
        report_error(f"Failed to fetch HTML from {url}")
        sys.exit(1)

    # Save raw HTML to a temp file for inspection
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    )
    tmp.write(html)
    tmp.close()
    tmp_path = Path(tmp.name)
    print(f"Raw HTML saved to: {tmp_path}")

    # Preprocess HTML before extraction (same as pipeline)
    if site.exclusions:
        html = remove_excluded_elements(html, site.exclusions, logger=logger)
    html = resolve_srcset_images(html, base_url=url, logger=logger)

    # Use shared extraction logic
    result = extract_article_from_html(html, url, site, logger)
    if result is None:
        report_error(f"Extraction returned nothing for {url}")
        print(f"\n--- Raw HTML available at: {tmp_path} ---", file=sys.stderr)
        sys.exit(1)

    # Print result
    fm_yaml = yaml.dump(
        result.frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    print("---")
    print(fm_yaml, end="")
    print("---")
    print()
    print(result.markdown_body.strip())
    print()
    print(f"--- Raw HTML available at: {tmp_path} ---", file=sys.stderr)

    # Print any log messages
    for log_line in logger.logs:
        print(log_line, file=sys.stderr)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _deduplicate_urls(urls: list[str]) -> list[str]:
    """Deduplicate URLs while preserving order."""
    seen: set[str] = set()
    deduped: list[str] = []
    for u in urls:
        if u not in seen:
            deduped.append(u)
            seen.add(u)
    return deduped


async def _discover_urls(
    sites: list[SiteConfig],
    session: aiohttp.ClientSession,
    shared_context: BrowserContext,
    browser_semaphore: asyncio.Semaphore,
) -> tuple[list[tuple[str, SiteConfig, SiteLogger]], dict[str, SiteLogger]]:
    """Discover article URLs for each site from feeds, listings, and static config.

    Returns a tuple of (task_list, site_loggers) where task_list contains
    `(url, site, logger)` triples for every discovered URL.
    """
    site_loggers: dict[str, SiteLogger] = {}
    all_tasks: list[tuple[str, SiteConfig, SiteLogger]] = []

    for site in sites:
        site_logger = SiteLogger(site.name, site.slug)
        site_loggers[site.slug] = site_logger

        print(f"Discovery: {site.name} ({site.slug})", end="", flush=True)

        urls = list(site.urls)

        if site.feed:
            feed_urls = await urls_from_feed(
                site.feed,
                site.feed_limit_or_default,
                session,
                logger=site_logger,
                site=site,
            )
            print(
                f" | Feed {site.feed} -> found {len(feed_urls)} URLs",
                end="",
                flush=True,
            )
            urls = feed_urls + urls

        for listing_url in site.listing_urls:
            discovered = await urls_from_listing(
                listing_url,
                site.listing_link_pattern,
                site.listing_limit_or_default,
                site.force_playwright,
                session,
                shared_context,
                browser_semaphore,
                site.listing_class,
                site.resolve_relative_to_root,
                logger=site_logger,
                site=site,
            )
            print(
                f" | Listing {listing_url} -> found {len(discovered)} URLs",
                end="",
                flush=True,
            )
            urls = discovered + urls

        print()  # Newline after all sources for this site are printed

        if not urls:
            site_logger.log("  No URLs configured, skipping.")
            continue

        urls = _deduplicate_urls(urls)

        # Log discovery to the stashed logger for the final grouped report
        site_logger.log(f"\n{'─' * 50}")
        site_logger.log(f"Site: {site.name} ({site.slug})")
        if site.feed:
            site_logger.log(f"  Fetching feed: {site.feed}")
        for listing_url in site.listing_urls:
            site_logger.log(f"  Fetching listing: {listing_url}")
        site_logger.log(f"  Total URLs discovered: {len(urls)}")

        for url in urls:
            all_tasks.append((url, site, site_logger))

    return all_tasks, site_loggers


def _filter_existing(
    tasks: list[tuple[str, SiteConfig, SiteLogger]],
    force: bool,
    output_dir: Path,
) -> list[tuple[str, SiteConfig, SiteLogger]]:
    """Remove tasks for articles that already exist on disk.

    Returns the filtered task list with existing articles skipped.
    """
    if force:
        return tasks

    existing_slugs = build_existing_slugs_map(output_dir)
    filtered: list[tuple[str, SiteConfig, SiteLogger]] = []
    for url, site_cfg, site_logger in tasks:
        article_slug = url_to_slug(url, site_cfg.exclude_query_params)
        site_existing = existing_slugs.get(site_cfg.slug)
        if site_existing is not None and article_slug in site_existing:
            site_logger.log(f"  · already exists (skipping fetch): {article_slug}")
            continue
        filtered.append((url, site_cfg, site_logger))

    skipped = len(tasks) - len(filtered)
    if skipped:
        print(
            f"\nSkipping {skipped} article(s) that already exist "
            f"on disk ({len(filtered)} remaining to fetch)."
        )

    return filtered


async def _process_articles(
    tasks: list[tuple[str, SiteConfig, SiteLogger]],
    *,
    dry_run: bool,
    force: bool,
    session: aiohttp.ClientSession,
    shared_context: BrowserContext,
    browser_semaphore: asyncio.Semaphore,
    fetch_semaphore: asyncio.Semaphore,
    retention_months: int,
    output_dir: Path,
) -> tuple[int, dict[str, int]]:
    """Process all article tasks concurrently.

    Returns (total_new, site_new_counts).
    """

    process_kwargs: dict[str, Any] = {
        "dry_run": dry_run,
        "force": force,
        "session": session,
        "context": shared_context,
        "browser_semaphore": browser_semaphore,
        "fetch_semaphore": fetch_semaphore,
        "retention_months": retention_months,
        "output_dir": output_dir,
    }

    async def _tagged_process(
        url: str, site_cfg: SiteConfig, site_logger: SiteLogger
    ) -> tuple[SiteConfig, bool]:
        was_new = await process_article(
            url, site_cfg, logger=site_logger, **process_kwargs
        )
        return site_cfg, was_new

    article_tasks = [
        _tagged_process(url, site_cfg, site_logger)
        for url, site_cfg, site_logger in tasks
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

    total_new = 0
    site_new_counts: dict[str, int] = {}
    for future in tqdm(asyncio.as_completed(article_tasks), **tqdm_kwargs):
        site_cfg, was_new = await future
        if was_new:
            total_new += 1
            site_new_counts[site_cfg.slug] = site_new_counts.get(site_cfg.slug, 0) + 1

    return total_new, site_new_counts


def _print_summary(
    site_loggers: dict[str, SiteLogger],
    site_new_counts: dict[str, int],
    total_new: int,
) -> None:
    """Print the final summary report and GitHub Actions step summary."""
    # Print stashed logs grouped by site
    for site_slug in sorted(site_loggers.keys()):
        site_logger = site_loggers[site_slug]
        if not site_logger.logs:
            continue

        with report_group(f"Site: {site_logger.site_name} ({site_logger.site_slug})"):
            for line in site_logger.logs:
                print(line)

    print(f"\n{'─' * 50}")
    done_msg = f"Done. {total_new} new article(s) written."
    print(done_msg)
    report_notice(done_msg)

    # Append a per-site markdown summary to the GitHub Actions step summary,
    # if running inside a step that supports it (GITHUB_STEP_SUMMARY is set).
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        summary_lines = [
            "### News barge scrape summary",
            "",
            "| Site | New articles |",
            "| --- | --- |",
        ]
        for slug in sorted(site_loggers, key=lambda s: site_loggers[s].site_name):
            name = site_loggers[slug].site_name
            summary_lines.append(f"| {name} | {site_new_counts.get(slug, 0)} |")
        summary_lines.append(f"| **Total** | **{total_new}** |")
        summary_lines.append("")

        # Surface the @profiled timing table in the step summary so it's
        # always visible in CI (a trailing stderr atexit dump is easy to miss
        # or lost entirely if the job is killed by the timeout).
        profile_table = format_profile_stats()
        if profile_table:
            summary_lines.append("### Profiling statistics")
            summary_lines.append("```")
            summary_lines.append(profile_table)
            summary_lines.append("```")
        write_step_summary("\n".join(summary_lines))


async def main_async(args: argparse.Namespace) -> None:
    # Handle --debug-url mode: single URL, fast feedback, no file write
    if args.debug_url:
        await _debug_url(args)
        return

    sites = SiteConfig.load_sites(args.config)
    if args.site:
        sites = [s for s in sites if s.slug == args.site]
        if not sites:
            report_error(f"No site with slug '{args.site}' found.")
            sys.exit(1)

    concurrency = args.concurrency or DEFAULT_CONCURRENCY
    browser_concurrency = args.browser_concurrency or DEFAULT_BROWSER_CONCURRENCY
    fetch_semaphore = asyncio.Semaphore(concurrency)
    browser_semaphore = asyncio.Semaphore(browser_concurrency)

    async with aiohttp.ClientSession() as session:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)

            # One shared browsing context for ALL Playwright fetches (listings
            # and articles). A context is expensive to create (~2.8s on CI);
            # reusing it instead of opening one per fetch is the biggest
            # Playwright win (issue #49). Pages (cheap) are opened/closed
            # inside it by fetch_html_playwright.
            shared_context = await _create_shared_context(browser)

            # Phase 1: Discovery
            tasks, site_loggers = await _discover_urls(
                sites, session, shared_context, browser_semaphore
            )

            # Phase 2: Filter existing
            tasks = _filter_existing(tasks, args.force, args.output_dir)

            # Phase 3: Shuffle
            random.shuffle(tasks)

            # Phase 4: Process
            total_new, site_new_counts = await _process_articles(
                tasks,
                dry_run=args.dry_run,
                force=args.force,
                session=session,
                shared_context=shared_context,
                browser_semaphore=browser_semaphore,
                fetch_semaphore=fetch_semaphore,
                retention_months=args.retention_months,
                output_dir=args.output_dir,
            )

            await shared_context.close()
            await browser.close()

    _print_summary(site_loggers, site_new_counts, total_new)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape sites → Markdown")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--site", help="Only process this slug")
    parser.add_argument(
        "--debug-url",
        help="Debug mode: fetch and process a single URL, print markdown to stdout, "
        "and save raw HTML to a temp file (requires --site)",
    )
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
