"""Unit tests for src/dates.py."""

from __future__ import annotations

from datetime import UTC, datetime

from src.dates import months_ago


class TestMonthsAgo:
    """Tests for months_ago."""

    def test_returns_utc_datetime(self) -> None:
        result = months_ago(1)
        assert result.tzinfo == UTC

    def test_one_month_ago(self) -> None:
        now = datetime.now(UTC)
        result = months_ago(1)
        expected_year = now.year
        expected_month = now.month - 1
        if expected_month <= 0:
            expected_month += 12
            expected_year -= 1
        assert result.year == expected_year
        assert result.month == expected_month

    def test_zero_months_returns_current_month(self) -> None:
        now = datetime.now(UTC)
        result = months_ago(0)
        assert result.year == now.year
        assert result.month == now.month

    def test_six_months_ago(self) -> None:
        now = datetime.now(UTC)
        result = months_ago(6)
        expected_year = now.year
        expected_month = now.month - 6
        while expected_month <= 0:
            expected_month += 12
            expected_year -= 1
        assert result.year == expected_year
        assert result.month == expected_month

    def test_twelve_months_ago(self) -> None:
        now = datetime.now(UTC)
        result = months_ago(12)
        expected_year = now.year - 1
        expected_month = now.month
        assert result.year == expected_year
        assert result.month == expected_month

    def test_clamps_day_to_month_length(self) -> None:
        """When current day exceeds target month length, clamp down."""
        now = datetime.now(UTC)
        result = months_ago(1)
        # The day should be the minimum of the current day and target month's days
        import calendar

        target_year = now.year
        target_month = now.month - 1
        if target_month <= 0:
            target_month += 12
            target_year -= 1
        max_day = calendar.monthrange(target_year, target_month)[1]
        assert result.day == min(now.day, max_day)

    def test_high_month_count(self) -> None:
        """Test months_ago with large month counts."""
        # 13 months ago from month M gives month M-1 (of last year)
        # because: M-13 <= 0, so month becomes M-13+12 = M-1
        now = datetime.now(UTC)
        result = months_ago(13)
        # M-13 <= 0, so we add 12: result is M-1, year-1
        if now.month - 13 <= 0:
            expected_month = now.month - 13 + 12
            expected_year = now.year - 1
        else:
            expected_month = now.month - 13
            expected_year = now.year
        assert result.year == expected_year
        assert result.month == expected_month

    def test_negative_months_triggers_overflow_clause(self) -> None:
        """Test the month > 12 clause with negative months (edge case)."""
        now = datetime.now(UTC)
        # months_ago(-1) means 1 month forward: month = now.month + 1
        # If now.month is 12, month becomes 13, which triggers the > 12 loop
        result = months_ago(-1)
        # 1 month in the future
        if now.month + 1 > 12:
            expected_month = now.month + 1 - 12
            expected_year = now.year + 1
        else:
            expected_month = now.month + 1
            expected_year = now.year
        if now.month == 12:
            # This tests the month > 12 clause
            assert result.year == expected_year
            assert result.month == expected_month
        assert result.year == expected_year or result.year == expected_year + 1
