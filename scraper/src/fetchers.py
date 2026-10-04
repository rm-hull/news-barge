"""
HTTP fetchers: aiohttp and Playwright-based HTML retrieval.
"""

from __future__ import annotations

import asyncio
from typing import Any, Literal

import aiohttp
from playwright.async_api import BrowserContext, Page

from .constants import FETCH_HEADERS, PLAYWRIGHT_TIMEOUT
from .log_helper import report_error
from .profiling import profiled

# Type alias for fetch results
FetchResult = str | None


@profiled
async def fetch_html_aiohttp(
    url: str,
    session: aiohttp.ClientSession,
    logger: Any = None,
    headers: dict[str, str] | None = None,
    allow_redirects: bool = True,
    ssl: bool = True,
) -> FetchResult:
    """Lightweight fetch using aiohttp.

    Args:
        url: The URL to fetch.
        session: aiohttp ClientSession to use.
        logger: Optional logger for error reporting.
        headers: Optional HTTP headers to use instead of defaults.
        allow_redirects: Whether to follow redirects.
        ssl: Whether to verify SSL certificates.

    Returns:
        The HTML content as a string, or None on failure.
    """
    try:
        timeout = aiohttp.ClientTimeout(total=30)
        request_headers = headers if headers is not None else FETCH_HEADERS
        async with session.get(
            url,
            headers=request_headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            ssl=ssl,
        ) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        report_error(f"HTTP fetch failed for {url}: {e}", logger=logger)
        return None


@profiled
async def fetch_html_playwright(
    url: str,
    context: BrowserContext,
    browser_semaphore: asyncio.Semaphore,
    logger: Any = None,
    wait_until: Literal["commit", "domcontentloaded", "load", "networkidle"]
    | None = None,
) -> FetchResult:
    """Full browser render for JS-heavy or anti-bot pages.

    Uses a *shared* ``BrowserContext`` (created once per scrape in
    ``scrape._create_shared_context``) rather than creating one per fetch.
    Opening a ``Page`` within that context is cheap, so the per-article ~2.8s
    ``browser.new_context()`` cost is paid just once per run instead of once
    per article (see issue #49).

    The analytics/ad route is registered once on the context (not per page),
    so every page inherits the blocking rule automatically.

    Args:
        url: The URL to fetch.
        context: Shared Playwright BrowserContext to open pages from.
        browser_semaphore: Semaphore to limit concurrent browser pages.
        logger: Optional logger for error reporting.
        wait_until: Playwright wait_until mode (default: "domcontentloaded").

    Returns:
        The HTML content as a string, or None on failure.
    """
    async with browser_semaphore:
        page: Page | None = None
        try:
            page = await context.new_page()
            await page.goto(
                url,
                wait_until=wait_until or "domcontentloaded",
                timeout=PLAYWRIGHT_TIMEOUT,
            )
            html = await page.content()
            return html
        except Exception as e:
            report_error(f"playwright fetch failed for {url}: {e}", logger=logger)
            return None
        finally:
            if page is not None:
                try:
                    await page.close()
                except Exception:
                    pass
