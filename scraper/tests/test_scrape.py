"""Unit tests for the shared Playwright context created in src.scrape.py."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock

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
    # First positional arg is the URL-matcher predicate (a callable, not a
    # string glob), so that keywords are matched in the full URL — including
    # the hostname (e.g. cdn.taboola.com, not just /analytics/ in the path).
    assert callable(args[0])
    # Second positional arg is the abort-route handler callable.
    assert callable(args[1])


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

    def test_handles_article_slugs_with_double_dashes(
        self, tmp_path: Path
    ) -> None:
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
