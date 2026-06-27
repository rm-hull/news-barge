"""
news-barge/scraper/scrape.py

Reads sites.yaml, fetches articles (via feed or explicit URL list),
extracts the main content with trafilatura, converts to Markdown,
and writes dated .md files with YAML frontmatter.
"""

import argparse
import hashlib
import os
import re
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import feedparser
import trafilatura
import yaml
from playwright.sync_api import sync_playwright

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


def fetch_html_requests(url: str) -> str | None:
    """Lightweight fetch using trafilatura's built-in downloader."""
    try:
        return trafilatura.fetch_url(url)
    except Exception as e:
        print(f"  ✗ requests fetch failed for {url}: {e}", file=sys.stderr)
        return None


def fetch_html_playwright(url: str) -> str | None:
    """Full browser fetch for JS-heavy or anti-bot sites."""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            ctx = browser.new_context(
                user_agent=FETCH_HEADERS["User-Agent"],
                java_script_enabled=True,
                # Block analytics, ads, tracking beacons
                extra_http_headers={
                    "Accept-Language": FETCH_HEADERS["Accept-Language"]
                },
            )
            page = ctx.new_page()
            # Block common tracking/ad domains at network level
            page.route(
                "**/{analytics,doubleclick,googlesyndication,adservice,tracking}**",
                lambda route: route.abort(),
            )
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            html = page.content()
            browser.close()
            return html
    except Exception as e:
        print(f"  ✗ playwright fetch failed for {url}: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------


def extract(html: str, url: str) -> dict | None:
    """
    Use trafilatura to pull the main article body + metadata.
    Returns a dict with title, text, date, description or None on failure.
    """
    result = trafilatura.bare_extraction(
        html,
        url=url,
        include_comments=False,
        include_tables=True,
        favor_precision=True,
        config=TRAFILATURA_CONFIG,
    )
    if not result or not result.get("text"):
        return None
    return result


def to_markdown(extracted: dict) -> str:
    """
    Build a clean Markdown body from trafilatura's extraction result.
    trafilatura can output markdown directly; we use that then clean up.
    """
    html = trafilatura.bare_extraction.__module__  # just a ref check
    # Re-extract as markdown
    # We call extract_metadata separately to avoid double work in callers,
    # but trafilatura's output_format='markdown' does the heavy lifting.
    return extracted.get("text", "")


# ---------------------------------------------------------------------------
# Feed handling
# ---------------------------------------------------------------------------


def urls_from_feed(feed_url: str, limit: int) -> list[str]:
    parsed = feedparser.parse(feed_url)
    entries = parsed.entries[:limit]
    urls = []
    for entry in entries:
        link = entry.get("link") or entry.get("id")
        if link:
            urls.append(link)
    return urls


# ---------------------------------------------------------------------------
# Per-article pipeline
# ---------------------------------------------------------------------------


def process_article(url: str, site: dict, dry_run: bool = False) -> bool:
    slug = url_to_slug(url)
    site_slug = site["slug"]
    use_playwright = site.get("force_playwright", False)

    print(f"  → {url}")

    html = fetch_html_playwright(url) if use_playwright else fetch_html_requests(url)
    if not html:
        return False

    # Re-extract as markdown using trafilatura
    md_body = trafilatura.extract(
        html,
        url=url,
        output_format="markdown",
        include_comments=False,
        include_tables=True,
        favor_precision=True,
        config=TRAFILATURA_CONFIG,
    )
    meta = trafilatura.extract_metadata(html, default_url=url)

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
    }

    path = output_path(site_slug, slug, file_date)

    if path.exists():
        print(f"  · already exists, skipping: {path.name}")
        return False

    if dry_run:
        print(f"  [dry-run] would write {path.relative_to(REPO_ROOT)}")
        return True

    write_markdown(path, frontmatter, md_body)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def load_sites() -> list[dict]:
    with open(SITES_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("sites", [])


def main():
    parser = argparse.ArgumentParser(description="Scrape sites → Markdown")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--site", help="Only process this slug")
    args = parser.parse_args()

    sites = load_sites()
    if args.site:
        sites = [s for s in sites if s["slug"] == args.site]
        if not sites:
            print(f"No site with slug '{args.site}' found.", file=sys.stderr)
            sys.exit(1)

    total_new = 0

    for site in sites:
        print(f"\n{'─'*50}")
        print(f"Site: {site['name']} ({site['slug']})")

        urls = list(site.get("urls") or [])

        if "feed" in site:
            limit = site.get("feed_limit", 10)
            print(f"  Fetching feed ({limit} items): {site['feed']}")
            feed_urls = urls_from_feed(site["feed"], limit)
            print(f"  Found {len(feed_urls)} URLs in feed")
            urls = feed_urls + urls

        if not urls:
            print("  No URLs configured, skipping.")
            continue

        for url in urls:
            ok = process_article(url, site, dry_run=args.dry_run)
            if ok:
                total_new += 1

    print(f"\n{'─'*50}")
    print(f"Done. {total_new} new article(s) written.")


if __name__ == "__main__":
    main()
