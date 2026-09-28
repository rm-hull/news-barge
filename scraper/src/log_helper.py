"""
Logging utilities for the scraper.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path

from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
# strip=False forces colors even when not writing to a TTY
init(strip=False)


class SiteLogger:
    """Logger that collects messages for grouped GitHub Actions output."""

    def __init__(self, site_name: str, site_slug: str) -> None:
        self.site_name = site_name
        self.site_slug = site_slug
        self.logs: list[str] = []

    def log(self, message: str) -> None:
        self.logs.append(message)

    def error(self, message: str) -> None:
        if os.environ.get("GITHUB_ACTIONS") == "true":
            self.logs.append(f"::error::{message}")
        else:
            self.logs.append(
                f"{Style.BRIGHT + Fore.RED}ERROR:{Style.RESET_ALL} {message}"
            )

    def info(self, message: str) -> None:
        self.log(message)


def report_error(message: str, logger: SiteLogger | None = None) -> None:
    """Prints an error message to stderr with colors and GitHub Actions support."""
    if logger:
        logger.error(message)
    elif os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::error::{message}", file=sys.stderr)
    else:
        formatted_msg = f"{Style.BRIGHT + Fore.RED}ERROR:{Style.RESET_ALL} {message}"
        print(formatted_msg, file=sys.stderr)


def report_notice(message: str, *, title: str | None = None) -> None:
    """Emit ``message`` as a GitHub Actions ``::notice`` annotation in CI.

    Outside of GitHub Actions this is a no-op, so callers should emit their
    own human-readable ``print`` for local runs. Workflow-command special
    characters (``%``, ``\r``, ``\n``) are escaped per GitHub's spec.
    """
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return
    escaped_msg = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    if title:
        escaped_title = (
            title.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        )
        print(f"::notice title={escaped_title}::{escaped_msg}")
    else:
        print(f"::notice::{escaped_msg}")


def write_step_summary(markdown: str) -> bool:
    """Append a markdown block to the GitHub Actions step summary file.

    No-ops (and returns False) when the ``GITHUB_STEP_SUMMARY`` environment
    variable is unset — i.e. not running inside a GitHub Actions step.
    Returns True if the block was appended successfully.
    """
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return False
    try:
        path = Path(summary_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(markdown)
            if not markdown.endswith("\n"):
                fh.write("\n")
    except OSError:
        return False
    return True


@contextmanager
def report_group(name: str) -> Generator[None]:
    """Context manager for GitHub Actions log groups."""
    in_github_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    if in_github_actions:
        print(f"::group::{name}")
    try:
        yield
    finally:
        if in_github_actions:
            print("::endgroup::")
