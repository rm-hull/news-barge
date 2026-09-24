"""
Logging utilities for the scraper.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Generator
from contextlib import contextmanager

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
