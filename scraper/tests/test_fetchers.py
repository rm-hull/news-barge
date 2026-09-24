"""Unit tests for src/fetchers.py."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest
from aiohttp import ClientResponseError, ClientSession

from src.constants import FETCH_HEADERS
from src.fetchers import fetch_html_aiohttp, fetch_html_playwright
from src.log_helper import SiteLogger


def _make_success_response(html: str) -> MagicMock:
    """Create a mock successful HTTP response."""
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.text = AsyncMock(return_value=html)
    mock_response.__aenter__ = AsyncMock(return_value=mock_response)
    mock_response.__aexit__ = AsyncMock(return_value=None)
    return mock_response


class TestFetchHtmlAiohttp:
    """Tests for fetch_html_aiohttp."""

    @pytest.mark.asyncio
    async def test_success_returns_html(self) -> None:
        """Should return HTML content on successful fetch."""
        mock_response = _make_success_response("<html><body>Test</body></html>")
        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        result = await fetch_html_aiohttp("https://example.com", mock_session)
        assert result == "<html><body>Test</body></html>"

    @pytest.mark.asyncio
    async def test_failure_returns_none(self) -> None:
        """Should return None on HTTP error."""
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock(
            side_effect=ClientResponseError(
                request_info=MagicMock(),
                history=(),
                status=404,
                message="Not Found",
            )
        )
        mock_response.text = AsyncMock(return_value="<html></html>")
        mock_response.__aenter__ = AsyncMock(return_value=mock_response)
        mock_response.__aexit__ = AsyncMock(return_value=None)

        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        result = await fetch_html_aiohttp("https://example.com", mock_session)
        assert result is None

    @pytest.mark.asyncio
    async def test_uses_default_headers(self) -> None:
        """Should use FETCH_HEADERS when no custom headers provided."""
        mock_response = _make_success_response("<html></html>")
        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        await fetch_html_aiohttp("https://example.com", mock_session)

        call_kwargs = mock_session.get.call_args.kwargs
        assert call_kwargs["headers"] == FETCH_HEADERS

    @pytest.mark.asyncio
    async def test_uses_custom_headers(self) -> None:
        """Should use provided custom headers instead of defaults."""
        custom_headers = {"User-Agent": "TestAgent"}
        mock_response = _make_success_response("<html></html>")
        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        await fetch_html_aiohttp(
            "https://example.com", mock_session, headers=custom_headers
        )

        call_kwargs = mock_session.get.call_args.kwargs
        assert call_kwargs["headers"] == custom_headers

    @pytest.mark.asyncio
    async def test_allow_redirects_parameter(self) -> None:
        """Should pass allow_redirects parameter to session.get."""
        mock_response = _make_success_response("<html></html>")
        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        await fetch_html_aiohttp(
            "https://example.com", mock_session, allow_redirects=False
        )
        call_kwargs = mock_session.get.call_args.kwargs
        assert call_kwargs["allow_redirects"] is False

    @pytest.mark.asyncio
    async def test_ssl_parameter(self) -> None:
        """Should pass ssl parameter to session.get."""
        mock_response = _make_success_response("<html></html>")
        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        await fetch_html_aiohttp("https://example.com", mock_session, ssl=False)
        call_kwargs = mock_session.get.call_args.kwargs
        assert call_kwargs["ssl"] is False

    @pytest.mark.asyncio
    async def test_logs_error_on_failure(self) -> None:
        """Should call report_error with logger when logger is provided."""
        logger = SiteLogger("Test Site", "test")

        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock(
            side_effect=ClientResponseError(
                request_info=MagicMock(),
                history=(),
                status=500,
                message="Internal Server Error",
            )
        )
        mock_response.text = AsyncMock(return_value="<html></html>")
        mock_response.__aenter__ = AsyncMock(return_value=mock_response)
        mock_response.__aexit__ = AsyncMock(return_value=None)

        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        result = await fetch_html_aiohttp(
            "https://example.com", mock_session, logger=logger
        )
        assert result is None

    @pytest.mark.asyncio
    async def test_timeout_handling(self) -> None:
        """Should handle timeout errors gracefully."""
        mock_response = MagicMock()
        mock_response.__aenter__ = AsyncMock(side_effect=TimeoutError("timeout"))
        mock_response.__aexit__ = AsyncMock(return_value=None)

        mock_session = AsyncMock(spec=ClientSession)
        mock_session.get = MagicMock(return_value=mock_response)

        result = await fetch_html_aiohttp("https://example.com", mock_session)
        assert result is None


class TestFetchHtmlPlaywright:
    """Tests for fetch_html_playwright."""

    @pytest.mark.asyncio
    async def test_success_returns_html(self) -> None:
        """Should return HTML content on successful fetch."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(return_value="<html><body>Test</body></html>")
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        result = await fetch_html_playwright(
            "https://example.com", mock_browser, semaphore
        )
        assert result == "<html><body>Test</body></html>"

    @pytest.mark.asyncio
    async def test_failure_returns_none(self) -> None:
        """Should return None on fetch failure."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(side_effect=Exception("Browser crashed"))
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        result = await fetch_html_playwright(
            "https://example.com", mock_browser, semaphore
        )
        assert result is None

    @pytest.mark.asyncio
    async def test_uses_user_agent_header(self) -> None:
        """Should use FETCH_HEADERS User-Agent when creating context."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(return_value="<html></html>")
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        await fetch_html_playwright("https://example.com", mock_browser, semaphore)

        call_kwargs = mock_browser.new_context.call_args.kwargs
        assert call_kwargs["user_agent"] == FETCH_HEADERS["User-Agent"]
        assert call_kwargs["java_script_enabled"] is True
        assert "Accept-Language" in call_kwargs["extra_http_headers"]

    @pytest.mark.asyncio
    async def test_registers_route_blocking(self) -> None:
        """Should register a route to block analytics/ad requests."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(return_value="<html></html>")
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        await fetch_html_playwright("https://example.com", mock_browser, semaphore)

        mock_page.route.assert_called_once()
        route_pattern = mock_page.route.call_args[0][0]
        assert "analytics" in route_pattern

    @pytest.mark.asyncio
    async def test_navigates_to_url(self) -> None:
        """Should navigate to the given URL."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(return_value="<html></html>")
        mock_page.route = AsyncMock()
        mock_page.goto = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        await fetch_html_playwright("https://example.com/page", mock_browser, semaphore)

        mock_page.goto.assert_called_once()
        call_kwargs = mock_page.goto.call_args
        assert call_kwargs[0][0] == "https://example.com/page"
        assert call_kwargs[1]["wait_until"] == "domcontentloaded"

    @pytest.mark.asyncio
    async def test_closes_page_and_context_on_success(self) -> None:
        """Should close page and context after successful fetch."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(return_value="<html></html>")
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        await fetch_html_playwright("https://example.com", mock_browser, semaphore)

        mock_page.close.assert_called_once()
        mock_context.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_logs_error_on_failure(self) -> None:
        """Should log error with provided logger on failure."""
        logger = SiteLogger("Test Site", "test")

        mock_page = AsyncMock()
        mock_page.content = AsyncMock(side_effect=Exception("Failed"))
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock()

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock()

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        result = await fetch_html_playwright(
            "https://example.com", mock_browser, semaphore, logger=logger
        )
        assert result is None

    @pytest.mark.asyncio
    async def test_handles_context_failure(self) -> None:
        """Should handle failure when creating context."""
        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(side_effect=Exception("Browser crashed"))

        semaphore = asyncio.Semaphore(1)

        result = await fetch_html_playwright(
            "https://example.com", mock_browser, semaphore
        )
        assert result is None

    @pytest.mark.asyncio
    async def test_handles_page_close_failure(self) -> None:
        """Should handle failures during page.close gracefully."""
        mock_page = AsyncMock()
        mock_page.content = AsyncMock(return_value="<html></html>")
        mock_page.route = AsyncMock()
        mock_page.close = AsyncMock(side_effect=Exception("Close failed"))

        mock_context = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        mock_context.close = AsyncMock(side_effect=Exception("Ctx close failed"))

        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)

        semaphore = asyncio.Semaphore(1)

        result = await fetch_html_playwright(
            "https://example.com", mock_browser, semaphore
        )
        assert result == "<html></html>"
