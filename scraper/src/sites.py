"""Site configuration model for the scraper."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

import yaml

from .constants import SITES_FILE

# ─── Placeholder expansion ──────────────────────────────────────────────────


def expand_placeholders(value: str | None) -> str | None:
    """Replace template placeholders in *value* with runtime values.

    Currently supports ``{yyyy}`` - the current four-digit year (e.g.
    ``2024``).  This lets a ``sites.yaml`` entry stay current without
    manual edits each year - for instance, a university news archive whose
    listing URL contains the current year.
    """
    if value is None:
        return None
    current_year = datetime.now(UTC).strftime("%Y")
    return value.replace("{yyyy}", current_year)


@dataclass
class SiteConfig:
    """Configuration for a single news site, loaded from ``sites.yaml``.

    Required fields are ``name`` and ``slug``. Every other field is optional
    and defaults to a sensible value, so a minimal two-line entry is all you
    need to get started.
    """

    name: str
    slug: str

    # ── Source configuration ──────────────────────────────────────────────
    # A site may provide one or more of: a feed URL, a listing page URL,
    # or a static list of article URLs.
    feed: str | None = None
    listing_url: str | None = None
    urls: list[str] = field(default_factory=list)

    # ── Limits ────────────────────────────────────────────────────────────
    # ``limit`` is the top-level cap shared by feed and listing discovery.
    # If unset, the source-specific ``feed_limit`` / ``listing_limit`` is
    # tried, falling back to 10.
    limit: int | None = None
    feed_limit: int | None = None
    listing_limit: int | None = None

    # ── Fetching behaviour ───────────────────────────────────────────────
    force_playwright: bool = False
    trust_insecure_certs: bool = False
    exclude_query_params: bool = False

    # ── Listing / article processing ───────────────────────────────────────
    listing_link_pattern: str | None = None
    listing_class: str | None = None
    resolve_relative_to_root: bool = False
    exclusions: list[str] = field(default_factory=list)
    remove_suffix: str | None = None

    # ── Metadata ───────────────────────────────────────────────────────────
    categories: list[str] = field(default_factory=list)
    notes: str | None = None

    @property
    def feed_limit_or_default(self) -> int:
        """Effective limit for feed discovery."""
        return self.limit or self.feed_limit or 10

    @property
    def listing_limit_or_default(self) -> int:
        """Effective limit for listing discovery."""
        return self.limit or self.listing_limit or 10

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SiteConfig:
        """Build a :class:`SiteConfig` from a raw mapping (e.g. parsed YAML).

        Any ``{yyyy}`` placeholders in the ``feed``, ``listing_url`` and
        ``urls`` fields are expanded to the current year at load time.
        """
        return cls(
            name=data["name"],
            slug=data["slug"],
            feed=expand_placeholders(data.get("feed")),
            listing_url=expand_placeholders(data.get("listing_url")),
            urls=[expand_placeholders(u) for u in (data.get("urls") or [])],
            categories=data.get("categories") or [],
            limit=data.get("limit"),
            feed_limit=data.get("feed_limit"),
            listing_limit=data.get("listing_limit"),
            force_playwright=data.get("force_playwright", False),
            trust_insecure_certs=data.get("trust_insecure_certs", False),
            exclude_query_params=data.get("exclude_query_params", False),
            exclusions=data.get("exclusions") or [],
            listing_link_pattern=data.get("listing_link_pattern"),
            listing_class=data.get("listing_class"),
            resolve_relative_to_root=data.get("resolve_relative_to_root", False),
            remove_suffix=data.get("remove_suffix"),
            notes=data.get("notes"),
        )

    @classmethod
    def load_sites(cls, path: Path = SITES_FILE) -> list[SiteConfig]:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        raw_sites = cast(list[dict[str, Any]], data.get("sites", []))
        return [cls.from_dict(s) for s in raw_sites]
