"""
Configuration and constants for the scraper.
"""

from __future__ import annotations

from pathlib import Path

import trafilatura

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
SITES_FILE = REPO_ROOT / "sites.yaml"
CONTENT_DIR = REPO_ROOT / "content"

# ---------------------------------------------------------------------------
# Trafilatura config
# ---------------------------------------------------------------------------

TRAFILATURA_CONFIG = trafilatura.settings.use_config()  # pyright: ignore
TRAFILATURA_CONFIG.set("DEFAULT", "EXTRACTION_TIMEOUT", "30")

# ---------------------------------------------------------------------------
# HTTP headers
# ---------------------------------------------------------------------------

FETCH_HEADERS: dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_CONCURRENCY = 10
DEFAULT_BROWSER_CONCURRENCY = 2
TAXOTAG_TOP_K = 3

# Maximum time (in ms) to wait for page.goto() to complete.
# Pages that cannot load core content within this window are abandoned —
# ad-heavy sites (e.g. Leeds Live) with continuous background requests
# would otherwise always hit the timeout, wasting ~30s per article.
PLAYWRIGHT_TIMEOUT = 5000
