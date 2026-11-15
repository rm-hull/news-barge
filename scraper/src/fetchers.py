"""
HTTP fetchers: curl_cffi and Playwright-based HTML retrieval.
"""

from __future__ import annotations

import asyncio
import re
import time
from typing import Any, Literal

from curl_cffi.requests import AsyncSession
from playwright.async_api import Browser, BrowserContext, Page

from .constants import PLAYWRIGHT_TIMEOUT
from .log_helper import report_error
from .profiling import profiled

# Type alias for fetch results
FetchResult = str | None


# ─── Proxy helpers ──────────────────────────────────────────────────────────


def _build_proxy_url(server: str | None, user_pass: str | None) -> str | None:
    """Build a proxy URL from server and optional user:pass credentials.

    If *server* is ``None`` or empty, returns ``None``.
    If *user_pass* is provided, it is prepended to the host (before the ``://``).
    """
    if not server:
        return None
    if user_pass:
        return re.sub(r"^(https?)://", r"\1://" + user_pass + "@", server, count=1)
    return server


# Cloudflare challenge page markers — these are specific to the challenge
# interstitial, not present on normal pages that merely load Cloudflare CDN
# resources (e.g. cdnjs.cloudflare.com).
_CF_CHALLENGE_TITLE = re.compile(
    r"<title>\s*Just a moment\.\.\.\s*</title>", re.IGNORECASE
)
_CF_CHALLENGE_RUNNING = re.compile(
    r"""id\s*=\s*['"]challenge-running['"]""", re.IGNORECASE
)
_CF_CHALLENGE_WIDGET = re.compile(
    r"""class\s*=\s*['"].*?challenge-widget.*?['"]""", re.IGNORECASE
)
_CF_CHALLENGE_NOSCRIPT = re.compile(
    r"""class\s*=\s*['"].*?noscript-warning.*?['"]""", re.IGNORECASE
)
_CF_CHALLENGE_SCRIPT = re.compile(r"challenges\.cloudflare\.com", re.IGNORECASE)


def _is_cloudflare_challenge(html: str) -> bool:
    """Return True if the HTML looks like a Cloudflare challenge interstitial.

    Checks for specific markers that only appear on the challenge page itself,
    avoiding false positives from pages that merely reference Cloudflare CDN
    domains (e.g. cdnjs.cloudflare.com).
    """
    hits = 0
    if _CF_CHALLENGE_TITLE.search(html):
        hits += 1
    if _CF_CHALLENGE_RUNNING.search(html):
        hits += 1
    if _CF_CHALLENGE_WIDGET.search(html):
        hits += 1
    if _CF_CHALLENGE_NOSCRIPT.search(html):
        hits += 1
    if _CF_CHALLENGE_SCRIPT.search(html):
        hits += 1
    # Require at least one strong signal to avoid false positives.
    # The title match alone is the most reliable single indicator.
    return hits >= 1


@profiled
async def fetch_html_curl(
    url: str,
    session: AsyncSession,
    logger: Any = None,
    headers: dict[str, str] | None = None,
    allow_redirects: bool = True,
    verify: bool = True,
    proxy: str | None = None,
) -> FetchResult:
    """Lightweight fetch using curl_cffi with Chrome impersonation.

    Uses ``impersonate="chrome"`` so headers, TLS handshake, and HTTP/2
    settings are all set consistently for a Chrome browser — no need to
    set a custom User-Agent or other browser headers manually.

    Args:
        url: The URL to fetch.
        session: curl_cffi AsyncSession to use.
        logger: Optional logger for error reporting.
        headers: Optional extra HTTP headers (merged on top of impersonated ones).
        allow_redirects: Whether to follow redirects.
        verify: Whether to verify SSL certificates.
        proxy: Optional proxy URL (e.g. ``http://user:pass@proxy:8080``).

    Returns:
        The HTML content as a string, or None on failure.
    """
    try:
        response = await session.get(
            url,
            headers=headers,
            allow_redirects=allow_redirects,
            verify=verify,
            proxy=proxy,
            timeout=30,
        )
        response.raise_for_status()  # type: ignore[no-untyped-call]
        return response.text
    except Exception as e:
        report_error(f"HTTP fetch failed ({e!r}) for: {url}", logger=logger)
        return None


@profiled
async def fetch_html_playwright(
    url: str,
    context: BrowserContext,
    logger: Any = None,
    wait_until: Literal["commit", "domcontentloaded", "load", "networkidle"]
    | None = None,
    proxy: str | None = None,
    browser: Browser | None = None,
) -> FetchResult:
    """Full browser render for JS-heavy or anti-bot pages.

    Uses a *shared* ``BrowserContext`` (created once per scrape in
    ``scrape._create_shared_context``) rather than creating one per fetch.
    Opening a ``Page`` within that context is cheap, so the per-article ~2.8s
    ``browser.new_context()`` cost is paid just once per run instead of once
    per article (see issue #49).

    The analytics/ad route is registered once on the context (not per page),
    so every page inherits the blocking rule automatically.

    If *proxy* is set, a new context is created with that proxy instead of
    using the shared context. The *browser* argument must be provided in that
    case so the new context can be created.

    .. note::
       Callers must acquire ``browser_semaphore`` **before** calling this
       function.  The semaphore is deliberately *not* part of this function
       so that ``@profiled`` measures only the actual fetch time — not queue
       wait.  With ``DEFAULT_BROWSER_CONCURRENCY = 5`` and 200+ URLs, semaphore
       wait can easily dominate the profile if it were measured here.

    Args:
        url: The URL to fetch.
        context: Shared Playwright BrowserContext to open pages from.
        logger: Optional logger for error reporting.
        wait_until: Playwright wait_until mode (default: "domcontentloaded").
        proxy: Optional proxy URL (e.g. ``http://user:pass@proxy:8080``).
        browser: Playwright Browser instance (required when *proxy* is set).

    Returns:
        The HTML content as a string, or None on failure.
    """
    page: Page | None = None
    temp_context: BrowserContext | None = None
    start = time.perf_counter()
    try:
        # If a proxy is configured, create a new context with that proxy
        # because Playwright sets proxy at the context level, not per-request.
        use_context = context
        if proxy:
            if browser is None:
                report_error(
                    "Playwright proxy requires browser instance", logger=logger
                )
                return None
            use_context = await browser.new_context(
                proxy={"server": proxy},
                java_script_enabled=True,
            )
            temp_context = use_context

        page = await use_context.new_page()
        await page.goto(
            url,
            wait_until=wait_until or "domcontentloaded",
            timeout=PLAYWRIGHT_TIMEOUT,
        )
        html = await page.content()
        # Wait for Cloudflare/anti-bot challenge to resolve if present
        if _is_cloudflare_challenge(html):
            for _ in range(30):
                await asyncio.sleep(1)
                html = await page.content()
                if not _is_cloudflare_challenge(html):
                    break
        _elapsed = time.perf_counter() - start
        if _elapsed > PLAYWRIGHT_TIMEOUT / 1000:
            report_error(
                f"Playwright fetch slow (took {_elapsed:.1f}s, "
                f"timeout={PLAYWRIGHT_TIMEOUT / 1000:.0f}s) for: {url}",
                logger=logger,
            )
        return html
    except Exception as e:
        report_error(f"Playwright fetch failed ({e!r}) for: {url}", logger=logger)
        return None
    finally:
        if page is not None:
            try:
                await page.close()
            except Exception:
                pass
        if temp_context is not None:
            try:
                await temp_context.close()
            except Exception:
                pass
