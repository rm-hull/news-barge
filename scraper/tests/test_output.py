"""Unit tests for src/output.py."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from src.output import output_path


class TestOutputPath:
    """Tests for output_path."""

    def test_generates_correct_path(self) -> None:
        path = output_path(
            "bbc",
            "article-slug",
            datetime(2024, 1, 15, 10, 30, 0, tzinfo=UTC),
        )
        assert "bbc" in str(path)
        assert "article-slug" in str(path)
        assert "2024" in str(path)
        assert "01" in str(path)
        assert "15" in str(path)
        # Filename format: {site_slug}--{article_slug}.md
        assert path.name == "bbc--article-slug.md"

    def test_includes_year_month_day_dirs(self) -> None:
        path = output_path(
            "cnn",
            "breaking-news",
            datetime(2023, 12, 25, 12, 0, 0, tzinfo=UTC),
        )
        # Path should include year/month/day
        assert path.parts[-4] == "2023"
        assert path.parts[-3] == "12"
        assert path.parts[-2] == "25"
        assert path.parts[-1] == "cnn--breaking-news.md"

    def test_custom_output_dir(self, tmp_path: Path) -> None:
        custom_dir = tmp_path / "output"
        path = output_path(
            "site",
            "my-article",
            datetime(2024, 6, 1, tzinfo=UTC),
            output_dir=custom_dir,
        )
        assert path.parent == custom_dir / "2024" / "06" / "01"
