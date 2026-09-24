"""
Configuration and constants for the scraper.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from threading import Lock

import trafilatura
from taxotag import Gist

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

# ---------------------------------------------------------------------------
# Taxotag
# ---------------------------------------------------------------------------

taxotag: Gist = Gist()
taxotag_lock: Lock = Lock()

# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def months_ago(months: int = 1) -> datetime:
    """UTC cutoff `months` calendar-months ago, with the day clamped to the
    target month length (e.g. Aug 31 -> Jul 31, Mar 31 -> Feb 28).

    Mirrors GNU ``date -d "N months ago"`` so the scraper and the archive
    workflow agree on what "older than N months" means.
    """
    import calendar

    now = datetime.now(UTC)
    year, month = now.year, now.month - months
    while month <= 0:
        month += 12
        year -= 1
    while month > 12:
        month -= 12
        year += 1
    day = min(now.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day, tzinfo=UTC)
