"""Unit tests for src/pipeline.py."""

from __future__ import annotations

import asyncio
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.log_helper import SiteLogger
from src.pipeline import process_article
from src.output import output_path
from src.slugs import url_to_slug


def make_site(**overrides: object) -> dict[str, object]:
    """Create a minimal site config dict."""
    return {
        "slug": "test-site",
        "name": "Test Site",
        "categories": ["News"],
        **overrides,
    }


@pytest.fixture
def mock_logger() -> SiteLogger:
    return SiteLogger("Test Site", "test-site")


@pytest.fixture
def mock_session() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def mock_browser() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def mock_page() -> AsyncMock:
    page = AsyncMock()
    page.content = AsyncMock(
        return_value="<html><body>Test article content here.</body></html>"
    )
    page.route = AsyncMock()
    page.goto = AsyncMock()
    page.close = AsyncMock()
    return page


@pytest.fixture
def mock_context(mock_page: AsyncMock) -> AsyncMock:
    ctx = AsyncMock()
    ctx.new_page = AsyncMock(return_value=mock_page)
    ctx.close = AsyncMock()
    return ctx


@pytest.fixture
def mock_browser_with_context(mock_context: AsyncMock) -> AsyncMock:
    browser = AsyncMock()
    browser.new_context = AsyncMock(return_value=mock_context)
    return browser


class TestProcessArticle:
    """Unit tests for process_article."""

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_no_html_returns_false(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should return False when fetch returns no HTML."""
        mock_fetch.return_value = None
        mock_extract.return_value = None
        mock_meta.return_value = None

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=False,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is False

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_extraction_returns_none_returns_false(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should return False when trafilatura extraction returns nothing."""
        mock_fetch.return_value = "<html><body>Nothing extractable</body></html>"
        mock_extract.return_value = None
        mock_meta.return_value = None

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=False,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is False

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_playwright_fetch_success(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_browser: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should use fetch_html_playwright when force_playwright is True."""
        mock_classify.return_value = ["tech"]
        mock_meta.return_value = None
        mock_extract.return_value = "<p>Test extracted content</p>"

        with patch(
            "src.pipeline.fetch_html_playwright", new_callable=AsyncMock
        ) as mock_pw_fetch:
            mock_pw_fetch.return_value = "<html><body>Test content</body></html>"

            result = await process_article(
                url="https://example.com/article",
                site=make_site(force_playwright=True),
                dry_run=True,
                force=True,
                session=AsyncMock(),
                browser=mock_browser,
                browser_semaphore=asyncio.Semaphore(1),
                fetch_semaphore=asyncio.Semaphore(1),
                logger=mock_logger,
                retention_months=0,
                output_dir=tmp_path,
            )

        assert result is True
        mock_pw_fetch.assert_called_once()

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_retention_filter_skips_old_articles(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should skip articles older than retention window."""
        mock_fetch.return_value = "<html><body>Old article</body></html>"
        mock_extract.return_value = "<p>Old content</p>"

        # Create a meta with an old date
        meta = MagicMock()
        old_date = datetime(2020, 1, 1, tzinfo=UTC)
        meta.date = old_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        meta.title = "Old Article"
        meta.description = "Old"
        meta.image = None
        mock_meta.return_value = meta
        mock_classify.return_value = ["old"]

        result = await process_article(
            url="https://example.com/old-article",
            site=make_site(),
            dry_run=False,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=1,
            output_dir=tmp_path,
        )
        assert result is False

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_existing_file_without_force_skips(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should skip existing files when force is False."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = ["news"]

        meta = MagicMock()
        meta.date = None
        meta.title = "Test Article"
        meta.description = "Test description"
        meta.image = None
        mock_meta.return_value = meta

        slug = url_to_slug("https://example.com/article", False)
        file_date = datetime.now(UTC)
        path = output_path("test-site", slug, file_date, output_dir=tmp_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\ntitle: existing\n---\ncontent", encoding="utf-8")

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=False,
            force=False,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is False

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_dry_run_returns_true(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Dry-run should return True without writing files."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = ["news"]

        meta = MagicMock()
        meta.date = None
        meta.title = "Test Article"
        meta.description = "Test"
        meta.image = None
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

        # No files should be written
        md_files = list(tmp_path.rglob("*.md"))
        assert len(md_files) == 0

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_success_writes_markdown_file(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should write a markdown file on successful processing."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Article content</p>"
        mock_classify.return_value = ["tech", "science"]

        meta = MagicMock()
        meta.date = None
        meta.title = "Test Article Title"
        meta.description = "A test description"
        meta.image = "https://example.com/image.jpg"
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=False,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

        md_files = list(tmp_path.rglob("*.md"))
        assert len(md_files) == 1

        content = md_files[0].read_text(encoding="utf-8")
        assert content.startswith("---")
        assert "title" in content

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_exclusions_strip_site_chrome(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should strip excluded elements before extraction."""
        html = '<div><p role="dialog">Subscribe!</p><article>Content</article></div>'
        mock_fetch.return_value = html
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = ["news"]

        meta = MagicMock()
        meta.date = None
        meta.title = "Test Article"
        meta.description = "Test"
        meta.image = None
        mock_meta.return_value = meta

        await process_article(
            url="https://example.com/article",
            site=make_site(exclusions=["role='dialog'"]),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )

        # Verify fetch_html_aiohttp was called
        mock_fetch.assert_called_once()

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_title_from_metadata(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should use metadata title over URL slug."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = []

        meta = MagicMock()
        meta.date = None
        meta.title = "Custom Metadata Title | SiteName"
        meta.description = "Desc"
        meta.image = "https://img.example.com/photo.jpg"
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/some-article-slug",
            site=make_site(),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_remove_suffix_from_title(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should strip suffix from title when configured."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = []

        meta = MagicMock()
        meta.date = None
        meta.title = "Article Title | SiteName"
        meta.description = "Desc"
        meta.image = None
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/article",
            site=make_site(remove_suffix=" | SiteName"),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_invalid_date_string_falls_back_to_now(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should fall back to current time when date parsing fails."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = []

        meta = MagicMock()
        meta.date = "invalid-date-string"
        meta.title = "Test Article"
        meta.description = "Desc"
        meta.image = None
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_image_fallback_to_markdown_extraction(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should fall back to extracting image from markdown."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        markdown_with_img = (
            "<p>Content with ![alt](https://example.com/fallback.jpg)</p>"
        )
        mock_extract.return_value = markdown_with_img
        mock_classify.return_value = []

        meta = MagicMock()
        meta.date = None
        meta.title = "Test Article"
        meta.description = "Desc"
        meta.image = None  # No image in metadata
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/article",
            site=make_site(),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_title_falls_back_to_slug(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should use URL slug as title when metadata title is missing."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = []

        meta = MagicMock()
        meta.date = None
        meta.title = None  # No title in metadata
        meta.description = None
        meta.image = None
        mock_meta.return_value = meta

        result = await process_article(
            url="https://example.com/some-article-slug/123",
            site=make_site(),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )
        assert result is True

    @pytest.mark.asyncio
    @patch("src.pipeline.fetch_html_aiohttp")
    @patch("src.pipeline.trafilatura.extract")
    @patch("src.pipeline.trafilatura.extract_metadata")
    @patch("src.pipeline.article_categories")
    async def test_categories_merge_with_site_categories(
        self,
        mock_classify: MagicMock,
        mock_meta: MagicMock,
        mock_extract: MagicMock,
        mock_fetch: AsyncMock,
        mock_session: AsyncMock,
        mock_browser_with_context: AsyncMock,
        mock_logger: SiteLogger,
        tmp_path: Path,
    ) -> None:
        """Should merge generated categories with site's configured categories."""
        mock_fetch.return_value = "<html><body>Article</body></html>"
        mock_extract.return_value = "<p>Content</p>"
        mock_classify.return_value = ["AI", "Science"]

        meta = MagicMock()
        meta.date = None
        meta.title = "Test Article"
        meta.description = "Desc"
        meta.image = None
        mock_meta.return_value = meta

        await process_article(
            url="https://example.com/article",
            site=make_site(categories=["News", "Politics"]),
            dry_run=True,
            force=True,
            session=mock_session,
            browser=mock_browser_with_context,
            browser_semaphore=asyncio.Semaphore(1),
            fetch_semaphore=asyncio.Semaphore(1),
            logger=mock_logger,
            retention_months=0,
            output_dir=tmp_path,
        )

        # Verify article_categories was called with title and description
        mock_classify.assert_called_once_with("Test Article", "Desc")
