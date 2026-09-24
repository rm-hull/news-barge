"""
HTTP fetchers: aiohttp and Playwright-based HTML retrieval.
"""

from __future__ import annotations

import asyncio
from typing import Any

import aiohttp
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Route,
)

from constants import FETCH_HEADERS
from log_helper import report_error

# Type alias for fetch results
FetchResult = str | None


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


async def fetch_html_playwright(
    url: str,
    browser: Browser,
    browser_semaphore: asyncio.Semaphore,
    logger: Any = None,
) -> FetchResult:
    """Full browser fetch for JS-heavy or anti-bot sites.

    Args:
        url: The URL to fetch.
        browser: Playwright Browser instance.
        browser_semaphore: Semaphore to limit concurrent browser instances.
        logger: Optional logger for error reporting.

    Returns:
        The HTML content as a string, or None on failure.
    """
    async with browser_semaphore:
        ctx: BrowserContext | None = None
        page: Page | None = None
        try:
            ctx = await browser.new_context(
                user_agent=FETCH_HEADERS["User-Agent"],
                java_script_enabled=True,
                extra_http_headers={
                    "Accept-Language": FETCH_HEADERS["Accept-Language"]
                },
            )
            page = await ctx.new_page()

            async def abort_route(route: Route) -> None:
                await route.abort()

            await page.route(
                "**/{analytics,doubleclick,googlesyndication,adservice,tracking}**",
                abort_route,
            )
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
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
            if ctx is not None:
                try:
                    await ctx.close()
                except Exception:
                    pass
