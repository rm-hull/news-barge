"""Unit tests for the shared Playwright context created in src.scrape.py."""

from __future__ import annotations

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
