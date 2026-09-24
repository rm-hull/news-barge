"""
Per-article processing pipeline: fetch, extract, classify, write.
"""

from __future__ import annotations

import asyncio
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import trafilatura
from aiohttp import ClientSession
from markdownify import markdownify as to_markdown
from playwright.async_api import Browser
import yaml

from .classifiers import article_categories, named_entities
from .constants import (
    REPO_ROOT,
    TRAFILATURA_CONFIG,
)
from .dates import months_ago
from .fetchers import fetch_html_aiohttp, fetch_html_playwright
from .log_helper import SiteLogger, report_error
from .output import output_path
from .slugs import url_to_slug
from .text_extraction import (
    clean_markdown_formatting,
    extract_first_image_from_markdown,
    linkify_text,
    normalize_inline_spacing,
    remove_excluded_elements,
)

# ---------------------------------------------------------------------------


async def process_article(
    url: str,
    site: dict[str, Any],
    dry_run: bool,
    force: bool,
    session: ClientSession,
    browser: Browser,
    browser_semaphore: asyncio.Semaphore,
    fetch_semaphore: asyncio.Semaphore,
    logger: SiteLogger,
    retention_months: int = 1,
    output_dir: Path = REPO_ROOT / "content",
) -> bool:
    """Process a single article: fetch, extract, classify, write.

    Args:
        url: The article URL to process.
        site: Site configuration dictionary.
        dry_run: If True, only report what would be done.
        force: Force regeneration of existing files.
        session: aiohttp ClientSession for HTTP requests.
        browser: Playwright Browser for JS-heavy pages.
        browser_semaphore: Semaphore for concurrent browser usage.
        fetch_semaphore: Semaphore for concurrent HTTP fetches.
        logger: Logger for progress reporting.
        retention_months: Minimum age of article to write (0 = all).
        output_dir: Directory to write output files.

    Returns:
        True if article was processed successfully.
    """
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

    # Strip site-level chrome before trafilatura sees it
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

    # Clean markdown inline
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
    generated_categories = await asyncio.to_thread(
        article_categories, title, description
    )
    categories = list(
        dict.fromkeys((site.get("categories") or []) + generated_categories)
    )

    entities = named_entities(description)

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
        "people": entities.people,
        "locations": entities.locations,
        "organisations": entities.organisations,
    }

    path = output_path(site_slug, slug, file_date, output_dir=output_dir)

    # Don't create articles older than the retention window
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

    path.parent.mkdir(parents=True, exist_ok=True)
    fm_yaml = yaml.dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    path.write_text(
        "---\n" + fm_yaml + "---\n\n" + md_body.strip() + "\n", encoding="utf-8"
    )
    display_path = (
        path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
    )
    logger.log(f"  ✓ {display_path}")
    return True
