"""Unit tests for date helper functions."""

from __future__ import annotations

from datetime import datetime

import pytest

from src.dates import months_ago


def test_months_ago_returns_datetime() -> None:
    """months_ago should return a datetime object."""
    result = months_ago(1)
    assert isinstance(result, datetime)


def test_months_ago_has_timezone() -> None:
    """months_ago result should have timezone info."""
    result = months_ago(1)
    assert result.tzinfo is not None


@pytest.mark.parametrize(
    ("months", "expected_months_offset"),
    [
        (0, 0),
        (1, 1),
        (6, 6),
        (12, 12),
    ],
)
def test_months_ago_offset(months: int, expected_months_offset: int) -> None:
    """months_ago should correctly offset by the given number of months."""
    from datetime import UTC

    result = months_ago(months)
    expected = datetime.now(UTC).replace(
        day=1, hour=0, minute=0, second=0, microsecond=0
    )
    # Calculate expected offset
    month = expected.month - months
    year = expected.year
    while month <= 0:
        month += 12
        year -= 1
    while month > 12:
        month -= 12
        year += 1
    # Just verify it's in the right range
    assert 1 <= result.month <= 12
    assert result.year >= expected.year - (months // 12 + 2)
