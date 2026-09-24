"""
Shared pytest fixtures for scraper integration tests.
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
from collections.abc import AsyncGenerator, Generator
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from aiohttp import web

import src.scrape as scrape

# ─── Dummy content served by the test HTTP server ──────────────────────────

FEED_XML_TEMPLATE = """\
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Test News Feed</title>
    <item>
      <title>Test Article One</title>
      <link>__BASE__/__ARTICLE_1__</link>
      <guid>__BASE__/__ARTICLE_1__</guid>
      <description>A test article about technology and science.</description>
      <pubDate>Mon, 01 Jan 2024 12:00:00 GMT</pubDate>
    </item>
    <item>
      <title>Test Article Two</title>
      <link>__BASE__/__ARTICLE_2__</link>
      <guid>__BASE__/__ARTICLE_2__</guid>
      <description>A second test article about cooking recipes.</description>
      <pubDate>Tue, 02 Jan 2024 12:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>"""

ARTICLE_ONE_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="date" content="2024-01-01T12:00:00Z">
  <title>Test Article One</title>
</head>
<body>
  <div class="subscribe-modal" role="dialog">
    <p>Subscribe to our newsletter!</p>
  </div>
  <header><h1>Test Article One</h1></header>
  <article>
    <p>This is the first test article. It contains meaningful content
    about technology and science.</p>
    <p>The quick brown fox jumps over the lazy dog. This sentence provides
    additional content to verify proper text extraction by trafilatura.</p>
  </article>
  <aside><p>Related: <a href="/other">other stuff</a></p></aside>
</body>
</html>"""

ARTICLE_TWO_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="date" content="2024-01-02T12:00:00Z">
  <title>Test Article Two</title>
</head>
<body>
  <div class="paywall-overlay">
    <p>Please subscribe to read more.</p>
  </div>
  <header><h1>Test Article Two</h1></header>
  <article>
    <p>This is the second test article. It discusses cooking recipes and
    kitchen tips for home cooks.</p>
    <p>Learning to cook at home is rewarding and saves money. Start with
    simple ingredients and build confidence in the kitchen.</p>
  </article>
</body>
</html>"""

LISTING_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Listing Page</title></head>
<body>
  <div class="story-list">
    <h2>Recent Articles</h2>
    <a href="__BASE__/articles/test-article-one.html">Article One</a>
    <a href="__BASE__/articles/test-article-two.html">Article Two</a>
    <a href="__BASE__/other-page.html">Other Page</a>
  </div>
</body>
</html>"""

ARTICLE_1 = "articles/test-article-one.html"
ARTICLE_2 = "articles/test-article-two.html"


# ─── Fixtures ───────────────────────────────────────────────────────────────


@pytest.fixture
def mock_playwright() -> Generator[AsyncMock]:
    """Mock Playwright so tests don't need a real browser binary."""

    mock_browser = AsyncMock()
    mock_browser.close = AsyncMock()

    mock_pw_instance = MagicMock()
    mock_pw_instance.chromium = MagicMock()
    mock_pw_instance.chromium.launch = AsyncMock(return_value=mock_browser)
    mock_pw_instance.stop = AsyncMock()

    mock_ctx_manager = AsyncMock()
    mock_ctx_manager.__aenter__ = AsyncMock(return_value=mock_pw_instance)
    mock_ctx_manager.__aexit__ = AsyncMock(return_value=None)

    with patch.object(scrape, "async_playwright", return_value=mock_ctx_manager):
        yield mock_browser


@pytest.fixture
def tmp_output_dir() -> Generator[Path]:
    """Create a temporary directory for article output."""
    path = Path(tempfile.mkdtemp(prefix="news-barge-test-"))
    yield path
    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture
def tmp_sites_file(tmp_output_dir: Path) -> Path:
    """Path for a temporary sites.yaml file."""
    return tmp_output_dir / "sites.yaml"


@pytest.fixture
async def test_server() -> AsyncGenerator[str]:
    """Start an in-process aiohttp server serving a dummy RSS feed and articles."""

    app = web.Application()

    async def feed_handler(request: web.Request) -> web.Response:
        xml = FEED_XML_TEMPLATE.replace("__BASE__", str(request.url.origin()))
        xml = xml.replace("__ARTICLE_1__", ARTICLE_1)
        xml = xml.replace("__ARTICLE_2__", ARTICLE_2)
        return web.Response(text=xml, content_type="application/xml")

    async def article_one(request: web.Request) -> web.Response:
        return web.Response(text=ARTICLE_ONE_HTML, content_type="text/html")

    async def article_two(request: web.Request) -> web.Response:
        return web.Response(text=ARTICLE_TWO_HTML, content_type="text/html")

    async def listing_handler(request: web.Request) -> web.Response:
        html = LISTING_HTML_TEMPLATE.replace("__BASE__", str(request.url.origin()))
        return web.Response(text=html, content_type="text/html")

    app.router.add_get("/feed", feed_handler)
    app.router.add_get(f"/{ARTICLE_1}", article_one)
    app.router.add_get(f"/{ARTICLE_2}", article_two)
    app.router.add_get("/listing", listing_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 0)
    await site.start()

    # Determine the actual port assigned by the OS
    port = site._server.sockets[0].getsockname()[1]  # type: ignore[union-attr]
    base_url = f"http://localhost:{port}"

    yield base_url

    await runner.cleanup()


@pytest.fixture
def test_sites_yaml(test_server: str) -> str:
    """Generate a minimal sites.yaml pointing at the test server (feed-based)."""
    return f"""
sites:
  - name: Test Site
    slug: test-site
    categories: [News & Politics]
    feed: {test_server}/feed
    limit: 5
"""


@pytest.fixture
def listing_sites_yaml(test_server: str) -> str:
    """Generate a sites.yaml using listing_url discovery."""
    return f"""
sites:
  - name: Test Listing Site
    slug: test-site
    categories: [News & Politics]
    listing_url: {test_server}/listing
    listing_link_pattern: "articles/test-article"
    limit: 5
"""


@pytest.fixture
def exclusion_sites_yaml(test_server: str) -> str:
    """Generate a sites.yaml with exclusion rules for site chrome."""
    return f"""
sites:
  - name: Test Site
    slug: test-site
    categories: [News & Politics]
    feed: {test_server}/feed
    limit: 5
    exclusions:
      - role="dialog"
      - //div[contains(@class, "paywall-overlay")]
"""


@pytest.fixture
def scraper_args(
    tmp_sites_file: Path,
    tmp_output_dir: Path,
    test_sites_yaml: str,
) -> argparse.Namespace:
    """Build an argparse.Namespace matching main_async() expectations."""
    tmp_sites_file.write_text(test_sites_yaml)
    return argparse.Namespace(
        config=tmp_sites_file,
        site=None,
        dry_run=False,
        force=True,
        retention_months=0,
        concurrency=2,
        browser_concurrency=1,
        output_dir=tmp_output_dir,
    )
