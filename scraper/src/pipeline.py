"""
Per-article processing pipeline: fetch, extract, classify, write.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from aiohttp import ClientSession
from markdownify import markdownify as to_markdown
from playwright.async_api import BrowserContext

from .classifiers import article_categories, named_entities
from .constants import (
    REPO_ROOT,
)
from .dates import months_ago
from .fetchers import fetch_html_aiohttp, fetch_html_playwright
from .log_helper import SiteLogger, report_error
from .output import output_path
from .sites import SiteConfig
from .slugs import url_to_slug
from .text_extraction import (
    clean_markdown_formatting,
    extract_article_html,
    extract_article_metadata,
    extract_first_image_from_markdown,
    filter_duplicate_names,
    linkify_text,
    normalize_inline_spacing,
    remove_excluded_elements,
    resolve_srcset_images,
    restore_trailing_dot_images,
    unfurl_multipage_article,
)


@dataclass
class ExtractionResult:
    """Result of extracting an article from raw HTML."""

    frontmatter: dict[str, Any]
    markdown_body: str


# ---------------------------------------------------------------------------


def extract_article_from_html(
    html: str,
    url: str,
    site: SiteConfig,
    logger: SiteLogger | None = None,
    title_fallback: str | None = None,
    meta: Any = None,
) -> ExtractionResult | None:
    """Extract frontmatter and markdown body from preprocessed article HTML.

    This is the shared core used by both the main pipeline and debug mode.
    Callers should pass HTML that has already had exclusions removed and
    srcset images resolved.

    Args:
        html: Preprocessed HTML of the article page (exclusions removed,
            srcset images resolved).
        url: The article URL (used for relative URL resolution).
        site: Site configuration for exclusions and title suffix.
        logger: Optional logger for progress reporting.
        title_fallback: Fallback title when metadata is missing. Defaults to
            the URL if not provided.
        meta: Pre-extracted metadata (trafilatura Document). If provided,
            this is used instead of extracting from HTML. This is important
            for multi-page articles where the merged HTML has no <head>.

    Returns:
        ExtractionResult with frontmatter dict and markdown body, or None
        if extraction failed.
    """
    if logger is None:
        logger = SiteLogger("", "")

    if meta is None:
        meta = extract_article_metadata(html, url=url)
    extracted_html = extract_article_html(html, url=url)

    if not extracted_html:
        report_error(f"extraction returned nothing for {url}", logger=logger)
        return None

    # Restore CDN trailing-dot image URLs that were given fake .jpg extensions
    # so that trafilatura would accept them
    extracted_html = restore_trailing_dot_images(extracted_html)
    extracted_html = normalize_inline_spacing(extracted_html)
    md_body = to_markdown(extracted_html, heading_style="ATX")

    # Clean markdown inline
    md_body = clean_markdown_formatting(md_body)
    md_body = linkify_text(md_body)

    # Fallback to first image in markdown if metadata image is missing
    image: str | None = None
    if meta and meta.image:
        image = meta.image
    else:
        image = extract_first_image_from_markdown(md_body)

    title = (meta.title if meta else None) or title_fallback or url
    if title:
        suffix = site.remove_suffix
        if suffix and title.endswith(suffix):
            title = title[: -len(suffix)].strip()
        if "|" in title:
            title = title.split("|")[0].strip()
    description = (meta.description if meta else None) or ""

    frontmatter: dict[str, Any] = {
        "title": title,
        "source_url": url,
        "source_site": site.name,
        "source_slug": site.slug,
        "description": description,
        "image": image,
    }
    if meta and meta.date:
        frontmatter["published"] = meta.date

    return ExtractionResult(frontmatter=frontmatter, markdown_body=md_body)


async def process_article(
    url: str,
    site: SiteConfig,
    dry_run: bool,
    force: bool,
    session: ClientSession,
    context: BrowserContext,
    browser_semaphore: asyncio.Semaphore,
    fetch_semaphore: asyncio.Semaphore,
    logger: SiteLogger,
    retention_months: int = 1,
    output_dir: Path = REPO_ROOT / "content",
) -> bool:
    """Process a single article: fetch, extract, classify, write.

    Args:
        url: The article URL to process.
        site: Site configuration (SiteConfig).
        dry_run: If True, only report what would be done.
        force: Force regeneration of existing files.
        session: aiohttp ClientSession for HTTP requests.
        context: Shared Playwright BrowserContext for JS-heavy pages.
        browser_semaphore: Semaphore for concurrent browser usage.
        fetch_semaphore: Semaphore for concurrent HTTP fetches.
        logger: Logger for progress reporting.
        retention_months: Minimum age of article to write (0 = all).
        output_dir: Directory to write output files.

    Returns:
        True if article was processed successfully.
    """
    exclude_query_params = site.exclude_query_params
    article_slug = url_to_slug(url, exclude_query_params)

    logger.log(f"  → {url}")

    async with fetch_semaphore:
        ssl = not site.trust_insecure_certs
        if site.force_playwright:
            async with browser_semaphore:
                html = await fetch_html_playwright(
                    url,
                    context,
                    logger=logger,
                    wait_until=site.playwright_wait_until,
                )
        else:
            html = await fetch_html_aiohttp(url, session, logger=logger, ssl=ssl)

    if not html:
        return False

    # Unfurl multi-page articles (fetch subsequent pages and merge).
    # This also extracts metadata from the original first-page HTML before
    # the document is rebuilt (which drops <head>), so title, date, and
    # og:image are not lost.
    unfurled_meta: Any = None
    if site.unfurl_multipage:
        # Build a fetcher that matches the site's fetch method
        async def _page_fetcher(page_url: str) -> str | None:
            async with fetch_semaphore:
                ssl = not site.trust_insecure_certs
                if site.force_playwright:
                    async with browser_semaphore:
                        return await fetch_html_playwright(
                            page_url,
                            context,
                            logger=logger,
                            wait_until=site.playwright_wait_until,
                        )
                else:
                    return await fetch_html_aiohttp(
                        page_url, session, logger=logger, ssl=ssl
                    )

        html, unfurled_meta = await unfurl_multipage_article(
            html, url, _page_fetcher, logger=logger
        )

    # Extract metadata early for date-based retention checks.
    # If the article was unfurled, use the metadata captured from the
    # original first-page HTML (before <head> was dropped).
    if site.exclusions:
        preprocessed_html = remove_excluded_elements(
            html, site.exclusions, logger=logger
        )
    else:
        preprocessed_html = html
    preprocessed_html = resolve_srcset_images(
        preprocessed_html, base_url=url, logger=logger
    )

    if unfurled_meta is not None:
        meta = unfurled_meta
    else:
        meta = await asyncio.to_thread(
            extract_article_metadata, preprocessed_html, url=url
        )

    now = datetime.now(UTC)
    pub_date: datetime | None = None
    if meta and meta.date:
        try:
            pub_date = datetime.fromisoformat(meta.date.replace("Z", "+00:00"))
        except ValueError:
            pass
    file_date = pub_date or now

    path = output_path(site.slug, article_slug, file_date, output_dir=output_dir)

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

    # Use shared extraction logic, passing pre-extracted metadata for
    # unfurled articles so title/date/image are not lost.
    result = await asyncio.to_thread(
        extract_article_from_html,
        preprocessed_html,
        url,
        site,
        logger,
        article_slug,
        meta,
    )
    if result is None:
        return False

    md_body = result.markdown_body
    frontmatter = dict(result.frontmatter)

    if dry_run:
        display_path = (
            path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        )
        logger.log(f"  [dry-run] would write {display_path}")
        return True

    # Augment frontmatter with classification data
    title = frontmatter.get("title", "")
    description = frontmatter.get("description", "")
    derived_categories = await asyncio.to_thread(article_categories, title, description)
    categories = list(dict.fromkeys(site.categories + derived_categories))
    entities = await asyncio.to_thread(named_entities, md_body)

    frontmatter["scraped_at"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    frontmatter["published"] = file_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    frontmatter["categories"] = categories
    frontmatter["people"] = sorted(filter_duplicate_names(entities.people))
    frontmatter["locations"] = sorted(filter_duplicate_names(entities.locations))
    frontmatter["organisations"] = sorted(
        filter_duplicate_names(entities.organisations)
    )

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
