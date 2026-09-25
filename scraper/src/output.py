"""Output file path utilities."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .constants import REPO_ROOT


def output_path(
    site_slug: str,
    article_slug: str,
    date: datetime,
    output_dir: Path = REPO_ROOT / "content",
) -> Path:
    """Compute the output file path for an article."""
    date_path = date.strftime("%Y/%m/%d")
    filename = f"{site_slug}--{article_slug}.md"
    return output_dir / date_path / filename
