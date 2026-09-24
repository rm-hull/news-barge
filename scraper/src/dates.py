"""Date and time utilities."""

from __future__ import annotations

import calendar
from datetime import UTC, datetime


def months_ago(months: int = 1) -> datetime:
    """UTC cutoff `months` calendar-months ago, with the day clamped to the
    target month length (e.g. Aug 31 -> Jul 31, Mar 31 -> Feb 28).

    Mirrors GNU ``date -d "N months ago"`` so the scraper and the archive
    workflow agree on what "older than N months" means.
    """
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
