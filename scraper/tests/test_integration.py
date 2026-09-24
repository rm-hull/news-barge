"""
Integration smoke tests: end-to-end scrape from a local HTTP server.

These tests exercise the full pipeline:
  1. An in-process aiohttp server serves a dummy RSS feed, listing page,
     and article HTML pages.
  2. The scraper's main_async() discovers URLs, fetches each article,
     extracts content with trafilatura, categorises with taxotag,
     converts to Markdown, and writes YAML-frontmatter files.
  3. We assert that the expected files are produced and that the Markdown
     body faithfully reflects the source article text.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from unittest.mock import AsyncMock

import pytest
import yaml

import src.scrape as scrape

# ─── Full feed-based scrape ─────────────────────────────────────────────────


async def test_full_scrape_produces_markdown_files(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Run the full pipeline and verify output files are created."""
    await scrape.main_async(scraper_args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    assert len(md_files) == 2, f"Expected 2 articles, got {len(md_files)}"


async def test_article_content_matches_source(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Verify that extracted Markdown body contains the original article text."""
    await scrape.main_async(scraper_args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    article_one = next(f for f in md_files if "test-article-one" in f.name)
    content = article_one.read_text(encoding="utf-8")

    # The Markdown body (after frontmatter) should contain key phrases
    # from the original HTML article.
    assert "technology and science" in content
    assert "quick brown fox" in content


async def test_article_two_content(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Verify the second article's content was extracted correctly."""
    await scrape.main_async(scraper_args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    article_two = next(f for f in md_files if "test-article-two" in f.name)
    content = article_two.read_text(encoding="utf-8")

    assert "cooking recipes" in content
    assert "home cooks" in content


async def test_frontmatter_is_valid_yaml(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Every output file must have parseable YAML frontmatter."""
    await scrape.main_async(scraper_args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    assert len(md_files) >= 2

    for f in md_files:
        text = f.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        assert match, f"Missing YAML frontmatter in {f.name}"

        meta = yaml.safe_load(match.group(1))
        assert isinstance(meta, dict)

        # Required fields
        assert "title" in meta
        assert "source_url" in meta
        assert "source_slug" in meta
        assert meta["source_slug"] == "test-site"
        assert "scraped_at" in meta
        assert "published" in meta
        assert "categories" in meta
        assert "description" in meta
        assert "image" in meta

        assert meta["title"] is not None


async def test_source_urls_are_correct(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Each article's source_url should point to its original article page."""
    await scrape.main_async(scraper_args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    source_urls = set()

    for f in md_files:
        text = f.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        assert match
        meta = yaml.safe_load(match.group(1))
        source_urls.add(meta["source_url"])

    assert any("test-article-one.html" in u for u in source_urls)
    assert any("test-article-two.html" in u for u in source_urls)


# ─── Dry-run ───────────────────────────────────────────────────────────────


async def test_dry_run_writes_no_files(
    test_server: str,
    tmp_sites_file: Path,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """--dry-run should discover articles but write nothing."""
    test_yaml = f"""
sites:
  - name: Test Site
    slug: test-site
    categories: [News & Politics]
    feed: {test_server}/feed
    limit: 5
"""
    tmp_sites_file.write_text(test_yaml)

    args = argparse.Namespace(
        config=tmp_sites_file,
        site=None,
        dry_run=True,
        force=True,
        retention_months=0,
        concurrency=2,
        browser_concurrency=1,
        output_dir=tmp_output_dir,
    )

    await scrape.main_async(args)

    md_files = list(tmp_output_dir.rglob("*.md"))
    assert len(md_files) == 0, "Dry-run should not create any files"


# ─── Listing URL discovery ──────────────────────────────────────────────────


async def test_listing_url_discovery(
    test_server: str,
    tmp_sites_file: Path,
    tmp_output_dir: Path,
    listing_sites_yaml: str,
    mock_playwright: AsyncMock,
) -> None:
    """Scrape using listing_url instead of feed — exercises urls_from_listing."""
    tmp_sites_file.write_text(listing_sites_yaml)

    args = argparse.Namespace(
        config=tmp_sites_file,
        site=None,
        dry_run=False,
        force=True,
        retention_months=0,
        concurrency=2,
        browser_concurrency=1,
        output_dir=tmp_output_dir,
    )

    await scrape.main_async(args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    assert len(md_files) == 2


# ─── Exclusion elements ────────────────────────────────────────────────────


async def test_exclusions_strip_site_chrome(
    test_server: str,
    tmp_sites_file: Path,
    tmp_output_dir: Path,
    exclusion_sites_yaml: str,
    mock_playwright: AsyncMock,
) -> None:
    """Exclusion rules should remove modals/overlays before extraction."""
    tmp_sites_file.write_text(exclusion_sites_yaml)

    args = argparse.Namespace(
        config=tmp_sites_file,
        site=None,
        dry_run=False,
        force=True,
        retention_months=0,
        concurrency=2,
        browser_concurrency=1,
        output_dir=tmp_output_dir,
    )

    await scrape.main_async(args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    assert len(md_files) == 2

    # The subscribe modal / paywall text should NOT appear in any article
    for f in md_files:
        content = f.read_text(encoding="utf-8")
        assert "Subscribe to our newsletter" not in content
        assert "Please subscribe to read more" not in content


# ─── Retention filter ──────────────────────────────────────────────────────


async def test_retention_filter_skips_old_articles(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Articles older than the retention window should be skipped."""
    # The test articles are dated Jan 1-2, 2024 — well over 1 month ago.
    scraper_args.retention_months = 1

    await scrape.main_async(scraper_args)

    md_files = list(tmp_output_dir.rglob("*.md"))
    assert len(md_files) == 0, "Articles older than retention window should be skipped"


# ─── Already-exists skip (no force) ────────────────────────────────────────


async def test_already_exists_without_force_skips(
    scraper_args: argparse.Namespace,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
) -> None:
    """Re-running without --force should skip already-existing files."""
    # First run writes the files
    await scrape.main_async(scraper_args)
    assert len(list(tmp_output_dir.rglob("*.md"))) == 2

    # Second run without --force should skip them
    scraper_args.force = False
    scraper_args.retention_months = 0
    await scrape.main_async(scraper_args)

    md_files = sorted(tmp_output_dir.rglob("*.md"))
    assert len(md_files) == 2


# ─── main() entry point ────────────────────────────────────────────────────


def test_main_entry_point(
    tmp_path: Path,
    mock_playwright: AsyncMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """main() should parse argv and run the full pipeline."""
    sites_file = tmp_path / "sites.yaml"
    sites_file.write_text(
        """
sites:
  - name: Test Site
    slug: test-site
    feed: http://localhost:1/nonexistent
    limit: 1
"""
    )
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    monkeypatch.setattr(
        "sys.argv",
        [
            "scrape.py",
            "--config",
            str(sites_file),
            "--output-dir",
            str(output_dir),
            "--dry-run",
            "--retention-months",
            "0",
        ],
    )

    # main() calls asyncio.run() — with no real server, the feed fetch will
    # fail gracefully (feedparser returns no entries) and the run completes.
    scrape.main()

    # Dry-run should not create any files
    md_files = list(output_dir.rglob("*.md"))
    assert len(md_files) == 0


# ─── Site not found ─────────────────────────────────────────────────────────


async def test_site_not_found_exits(
    test_server: str,
    tmp_sites_file: Path,
    tmp_output_dir: Path,
    mock_playwright: AsyncMock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """--site with a non-existent slug should exit with code 1."""
    tmp_sites_file.write_text(
        f"""
sites:
  - name: Test Site
    slug: test-site
    feed: {test_server}/feed
    limit: 5
"""
    )

    args = argparse.Namespace(
        config=tmp_sites_file,
        site="nonexistent",
        dry_run=False,
        force=True,
        retention_months=0,
        concurrency=2,
        browser_concurrency=1,
        output_dir=tmp_output_dir,
    )

    with pytest.raises(SystemExit) as exc_info:
        await scrape.main_async(args)

    assert exc_info.value.code == 1
