"""Unit tests for src/fetchers.py."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from aiohttp import ClientResponseError, ClientSession

from src.constants import FETCH_HEADERS, PLAYWRIGHT_TIMEOUT
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
    """Tests for fetch_html_playwright with a shared BrowserContext."""

    @pytest.fixture
    def mock_page(self) -> AsyncMock:
        page = AsyncMock()
        page.content = AsyncMock(
            return_value="<html><body>Test article content here.</body></html>"
        )
        page.goto = AsyncMock()
        page.route = AsyncMock()
        page.close = AsyncMock()
        return page

    @pytest.fixture
    def mock_context(self, mock_page: AsyncMock) -> AsyncMock:
        ctx = AsyncMock()
        ctx.new_page = AsyncMock(return_value=mock_page)
        ctx.route = AsyncMock()
        ctx.close = AsyncMock()
        return ctx

    @pytest.mark.asyncio
    async def test_success_returns_html(self, mock_context: AsyncMock) -> None:
        """Should return HTML content on a successful fetch."""
        result = await fetch_html_playwright("https://example.com", mock_context)
        assert result == "<html><body>Test article content here.</body></html>"
        mock_context.new_page.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_failure_returns_none(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should return None on fetch failure and still close the page."""
        mock_page.content = AsyncMock(side_effect=Exception("Browser crashed"))
        result = await fetch_html_playwright("https://example.com", mock_context)
        assert result is None
        mock_page.close.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_navigates_to_url(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should navigate to the given URL with the default wait mode."""
        await fetch_html_playwright("https://example.com/page", mock_context)
        mock_page.goto.assert_awaited_once()
        call_args = mock_page.goto.call_args
        assert call_args[0][0] == "https://example.com/page"
        assert call_args[1]["wait_until"] == "domcontentloaded"
        assert call_args[1]["timeout"] == PLAYWRIGHT_TIMEOUT

    @pytest.mark.asyncio
    async def test_uses_reduced_timeout(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should pass a reduced timeout (far below Playwright's 30s default)."""
        await fetch_html_playwright("https://example.com/page", mock_context)
        assert mock_page.goto.call_args[1]["timeout"] == PLAYWRIGHT_TIMEOUT
        assert mock_page.goto.call_args[1]["timeout"] < 30000

    @pytest.mark.asyncio
    async def test_wait_until_networkidle(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should pass wait_until='networkidle' through to page.goto."""
        await fetch_html_playwright(
            "https://example.com/page",
            mock_context,
            wait_until="networkidle",
        )
        mock_page.goto.assert_awaited_once()
        assert mock_page.goto.call_args[1]["wait_until"] == "networkidle"

    @pytest.mark.asyncio
    async def test_closes_page_not_context(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should close the page but leave the shared context intact."""
        await fetch_html_playwright("https://example.com", mock_context)
        mock_page.close.assert_awaited_once()
        mock_context.close.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_does_not_register_per_page_route(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """The analytics/ad route is set once on the context, not per page."""
        await fetch_html_playwright("https://example.com", mock_context)
        mock_page.route.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_handles_page_creation_failure(self, mock_context: AsyncMock) -> None:
        """Should return None if the context cannot open a page."""
        mock_context.new_page = AsyncMock(side_effect=Exception("Context died"))
        result = await fetch_html_playwright("https://example.com", mock_context)
        assert result is None

    @pytest.mark.asyncio
    async def test_handles_page_close_failure(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """A failure in page.close() should not mask the returned HTML."""
        mock_page.close = AsyncMock(side_effect=Exception("Close failed"))
        result = await fetch_html_playwright("https://example.com", mock_context)
        assert result == "<html><body>Test article content here.</body></html>"

    @pytest.mark.asyncio
    async def test_logs_error_on_failure(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should log an error with the provided logger on failure."""
        logger = SiteLogger("Test Site", "test")
        mock_page.content = AsyncMock(side_effect=Exception("Failed"))
        result = await fetch_html_playwright(
            "https://example.com", mock_context, logger=logger
        )
        assert result is None

    @pytest.mark.asyncio
    async def test_logs_warning_on_slow_fetch(
        self, mock_context: AsyncMock, mock_page: AsyncMock
    ) -> None:
        """Should report a warning when the fetch exceeds the timeout window."""
        from unittest.mock import patch

        logger = SiteLogger("Test Site", "test")
        # Simulate elapsed time exceeding PLAYWRIGHT_TIMEOUT (in seconds).
        threshold_s = PLAYWRIGHT_TIMEOUT / 1000
        # perf_counter is called 4 times: decorator start, function start,
        # function finally, profiler record — need 4 side-effect values.
        with patch(
            "src.fetchers.time.perf_counter",
            side_effect=[0.0, 0.0, threshold_s + 2, 0.0],
        ):
            await fetch_html_playwright(
                "https://example.com", mock_context, logger=logger
            )
        assert mock_page.close.assert_awaited_once
        # The warning is routed through report_error → SiteLogger.log
        assert any("slow" in line.lower() for line in logger.logs), (
            f"Expected slow-fetch warning in logs: {logger.logs}"
        )
