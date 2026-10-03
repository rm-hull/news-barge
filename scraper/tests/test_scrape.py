"""Unit tests for the shared Playwright context created in src/scrape.py."""

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
    assert "analytics" in args[0] or "doubleclick" in args[0]
    # second positional arg is the abort-route handler callable
    assert callable(args[1])
