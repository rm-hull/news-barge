"""
Logging utilities for the scraper.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Generator
from contextlib import contextmanager


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
            RED_BOLD = "\033[1;31m"
            RESET = "\033[0m"
            self.logs.append(f"{RED_BOLD}ERROR:{RESET} {message}")

    def info(self, message: str) -> None:
        self.log(message)


def report_error(message: str, logger: SiteLogger | None = None) -> None:
    """Prints an error message to stderr with colors and GitHub Actions support."""
    if logger:
        logger.error(message)
    elif os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::error::{message}", file=sys.stderr)
    else:
        RED_BOLD = "\033[1;31m"
        RESET = "\033[0m"
        formatted_msg = f"{RED_BOLD}ERROR:{RESET} {message}"
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
