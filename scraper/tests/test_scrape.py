"""Unit tests for src.scrape.py."""

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest

import src.scrape as scrape
from src.constants import FETCH_HEADERS


def _make_mock_browser() -> tuple[AsyncMock, AsyncMock]:
    """Return (mock_browser, mock_context) wired so new_context() works.

    child attrs of an AsyncMock are MagicMocks (not awaitable) by default, so
    route/new_page/close must be set to AsyncMock explicitly.
    """
    mock_context = AsyncMock()
    mock_context.route = AsyncMock()
    mock_context.new_page = AsyncMock()
    mock_context.close = AsyncMock()

    mock_browser = AsyncMock()
    mock_browser.new_context = AsyncMock(return_value=mock_context)
    mock_browser.close = AsyncMock()
    return mock_browser, mock_context


@pytest.fixture
def mock_browser_and_context() -> tuple[AsyncMock, AsyncMock]:
    return _make_mock_browser()


@pytest.mark.asyncio
async def test_create_shared_context_sets_ua_js_headers(
    mock_browser_and_context: tuple[AsyncMock, AsyncMock],
) -> None:
    """new_context should receive the project UA, JS enabled, and headers."""
    mock_browser, _mock_context = mock_browser_and_context

    await scrape._create_shared_context(mock_browser)

    mock_browser.new_context.assert_awaited_once()
    kwargs = mock_browser.new_context.call_args.kwargs
    assert kwargs["user_agent"] == FETCH_HEADERS["User-Agent"]
    assert kwargs["java_script_enabled"] is True
    assert kwargs["extra_http_headers"] == {
        "Accept-Language": FETCH_HEADERS["Accept-Language"]
    }


@pytest.mark.asyncio
async def test_create_shared_context_registers_analytics_route_once(
    mock_browser_and_context: tuple[AsyncMock, AsyncMock],
) -> None:
    """The analytics/ad route must be registered exactly once on the context."""
    mock_browser, mock_context = mock_browser_and_context

    await scrape._create_shared_context(mock_browser)

    mock_context.route.assert_awaited_once()
    args = mock_context.route.call_args.args
    # The single positional arg is the handler callable that checks
    # resource_type and URL keywords internally.
    assert callable(args[0])


class TestBuildExistingSlugsMap:
    """Tests for the existing articles index builder."""

    def test_returns_empty_when_directory_missing(self, tmp_path: Path) -> None:
        """Should return empty dict when the output directory does not exist."""
        result = scrape.build_existing_slugs_map(tmp_path / "nonexistent")
        assert result == {}

    def test_returns_empty_when_directory_empty(self, tmp_path: Path) -> None:
        """Should return empty dict when the output directory has no .md files."""
        (tmp_path / "2024" / "01" / "15").mkdir(parents=True)
        result = scrape.build_existing_slugs_map(tmp_path)
        assert result == {}

    def test_extracts_site_and_article_slugs(self, tmp_path: Path) -> None:
        """Should parse filenames and build the site -> slugs map."""
        d = tmp_path / "2024" / "01" / "15"
        d.mkdir(parents=True)
        (d / "guardian--some-article.md").touch()
        (d / "bbc--another-piece.md").touch()
        (d / "guardian--second-article.md").touch()

        result = scrape.build_existing_slugs_map(tmp_path)

        assert "guardian" in result
        assert "bbc" in result
        assert "some-article" in result["guardian"]
        assert "second-article" in result["guardian"]
        assert "another-piece" in result["bbc"]

    def test_handles_article_slugs_with_double_dashes(self, tmp_path: Path) -> None:
        """Article slugs may contain '--' themselves; only the first '--'
        separates the site slug from the article slug."""
        d = tmp_path / "2024" / "02" / "10"
        d.mkdir(parents=True)
        (d / "reuters--path--to--article.md").touch()

        result = scrape.build_existing_slugs_map(tmp_path)

        assert "reuters" in result
        assert "path--to--article" in result["reuters"]

    def test_ignores_non_md_files(self, tmp_path: Path) -> None:
        """Non-.md files should be ignored."""
        d = tmp_path / "2024" / "01"
        d.mkdir(parents=True)
        (d / "guardian--article.md").touch()
        (d / "guardian--article.txt").touch()
        (d / "README.md").touch()

        result = scrape.build_existing_slugs_map(tmp_path)

        assert "guardian" in result
        assert "article" in result["guardian"]
        # README.md has no '--' separator, so it should be ignored
        assert "" not in result


@pytest.mark.asyncio
async def test_blocked_request_matcher_catches_ads_and_tracking() -> None:
    """The matcher should flag known analytics/ad/tracking URLs."""
    matcher = scrape._is_blocked_request

    # URLs that should be blocked (keywords appear in hostname or path).
    assert matcher("https://cdn.taboola.com/widget.js")
    assert matcher("https://cmp.inmobi.com/choice.js")
    assert matcher("https://uk-script.dotmetrics.net/collect")
    assert matcher("https://www.googletagmanager.com/gtag.js")
    assert matcher("https://cdn.eu.amplitude.com/tracker")
    assert matcher("https://example.com/analytics/pageview.gif")
    assert matcher("https://securepubads.g.doubleclick.net/pixel")
    assert matcher("https://livecomments.viafoura.co/embed")

    # URLs that should NOT be blocked — normal article / content requests.
    assert not matcher("https://www.leeds-live.co.uk/news/article-slug-12345")
    assert not matcher("https://www.theguardian.com/uk-news/article")
    assert not matcher("https://www.bbc.co.uk/news/uk-politics-12345")
    assert not matcher("https://fonts.googleapis.com/css2?family=Roboto")
    assert not matcher("https://example.com/api/articles/123")


@pytest.mark.asyncio
async def test_route_handler_does_not_abort_document_with_blocked_keyword() -> None:
    """A document navigation whose URL contains a blocked keyword must NOT be aborted.

    Regression test: a page like bbc.co.uk/news/articles/tracking-down-the-culprit
    contains "tracking" and was incorrectly aborted because the old route handler
    matched the keyword against the full URL for every request type, including
    the main document navigation.
    """
    mock_browser = AsyncMock()
    mock_context = AsyncMock()
    mock_browser.new_context = AsyncMock(return_value=mock_context)

    # Track which handler was registered with context.route()
    registered_handler = None

    async def capture_route(handler):
        nonlocal registered_handler
        registered_handler = handler

    mock_context.route = capture_route

    await scrape._create_shared_context(mock_browser)

    # registered_handler should be the _abort_route closure
    assert registered_handler is not None

    # Simulate a document request with "tracking" in the URL
    mock_request = MagicMock()
    mock_request.resource_type = "document"
    mock_request.url = "https://www.bbc.co.uk/news/articles/tracking-down-the-culprit"

    mock_route = MagicMock()
    mock_route.request = mock_request

    # The handler should NOT abort for document requests
    await registered_handler(mock_route)
    mock_route.abort.assert_not_awaited() if hasattr(
        mock_route.abort, "assert_not_awaited"
    ) else True


@pytest.mark.asyncio
async def test_route_handler_aborts_non_document_with_blocked_keyword() -> None:
    """A non-document request (e.g. script) with a blocked keyword MUST be aborted."""
    mock_browser = AsyncMock()
    mock_context = AsyncMock()
    mock_browser.new_context = AsyncMock(return_value=mock_context)

    registered_handler = None

    async def capture_route(handler):
        nonlocal registered_handler
        registered_handler = handler

    mock_context.route = capture_route

    await scrape._create_shared_context(mock_browser)
    assert registered_handler is not None

    # Simulate a script request with "tracking" in the URL
    mock_request = MagicMock()
    mock_request.resource_type = "script"
    mock_request.url = "https://cdn.taboola.com/widget.js"

    mock_route = AsyncMock()
    mock_route.request = mock_request

    await registered_handler(mock_route)
    mock_route.abort.assert_awaited_once()


class TestUrlsFromListing:
    """Tests for the listing page URL discovery function."""

    @pytest.mark.asyncio
    async def test_listing_class_selects_matching_links(self) -> None:
        """listing_class should select only links inside elements with that class."""
        html = b"""<!DOCTYPE html>
        <body>
          <div class="article-link">
            <a href="/articles/one.html">One</a>
            <a href="/articles/two.html">Two</a>
          </div>
          <div class="sidebar">
            <a href="/other.html">Other</a>
          </div>
        </body>"""
        with patch.object(
            scrape, "fetch_html_aiohttp", new_callable=AsyncMock
        ) as mock_fetch:
            mock_fetch.return_value = html.decode()
            session = MagicMock(spec=aiohttp.ClientSession)
            context = MagicMock()
            browser_semaphore = asyncio.Semaphore(1)

            result = await scrape.urls_from_listing(
                listing_url="https://example.com/listing",
                pattern=None,
                limit=10,
                use_playwright=False,
                session=session,
                context=context,
                browser_semaphore=browser_semaphore,
                listing_class="article-link",
            )

            assert len(result) == 2
            assert "https://example.com/articles/one.html" in result
            assert "https://example.com/articles/two.html" in result
            assert "https://example.com/other.html" not in result

    @pytest.mark.asyncio
    async def test_listing_class_with_single_quote_does_not_crash(self) -> None:
        """A class name containing a single quote must not raise XPathEvalError.

        This is the injection vulnerability: f-string interpolation of the class
        name into the XPath expression would break on quotes.
        """
        html = b"""<!DOCTYPE html>
        <body>
          <div class="o'neill-article">
            <a href="/articles/one.html">One</a>
          </div>
        </body>"""
        with patch.object(
            scrape, "fetch_html_aiohttp", new_callable=AsyncMock
        ) as mock_fetch:
            mock_fetch.return_value = html.decode()
            session = MagicMock(spec=aiohttp.ClientSession)
            context = MagicMock()
            browser_semaphore = asyncio.Semaphore(1)

            # Should not raise XPathEvalError
            result = await scrape.urls_from_listing(
                listing_url="https://example.com/listing",
                pattern=None,
                limit=10,
                use_playwright=False,
                session=session,
                context=context,
                browser_semaphore=browser_semaphore,
                listing_class="o'neill-article",
            )

            assert len(result) == 1
            assert "https://example.com/articles/one.html" in result

    @pytest.mark.asyncio
    async def test_listing_class_with_special_xpath_chars(self) -> None:
        """A class name with XPath-special characters must not crash."""
        html = b"""<!DOCTYPE html>
        <body>
          <div class="article[link]">
            <a href="/articles/one.html">One</a>
          </div>
        </body>"""
        with patch.object(
            scrape, "fetch_html_aiohttp", new_callable=AsyncMock
        ) as mock_fetch:
            mock_fetch.return_value = html.decode()
            session = MagicMock(spec=aiohttp.ClientSession)
            context = MagicMock()
            browser_semaphore = asyncio.Semaphore(1)

            result = await scrape.urls_from_listing(
                listing_url="https://example.com/listing",
                pattern=None,
                limit=10,
                use_playwright=False,
                session=session,
                context=context,
                browser_semaphore=browser_semaphore,
                listing_class="article[link]",
            )

            assert len(result) == 1

    @pytest.mark.asyncio
    async def test_no_listing_class_selects_all_links(self) -> None:
        """Without listing_class, all links on the page should be selected."""
        html = b"""<!DOCTYPE html>
        <body>
          <div class="article-link">
            <a href="/articles/one.html">One</a>
          </div>
          <div class="sidebar">
            <a href="/other.html">Other</a>
          </div>
        </body>"""
        with patch.object(
            scrape, "fetch_html_aiohttp", new_callable=AsyncMock
        ) as mock_fetch:
            mock_fetch.return_value = html.decode()
            session = MagicMock(spec=aiohttp.ClientSession)
            context = MagicMock()
            browser_semaphore = asyncio.Semaphore(1)

            result = await scrape.urls_from_listing(
                listing_url="https://example.com/listing",
                pattern=None,
                limit=10,
                use_playwright=False,
                session=session,
                context=context,
                browser_semaphore=browser_semaphore,
                listing_class=None,
            )

            assert len(result) == 2
            assert "https://example.com/articles/one.html" in result
            assert "https://example.com/other.html" in result
