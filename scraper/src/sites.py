"""Site configuration model for the scraper."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal, cast

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


# Pattern for ${VAR_NAME} environment variable placeholders
_ENV_VAR_RE = re.compile(r"\$\{([^}]+)\}")


def resolve_env_vars(value: str | None) -> str | None:
    """Replace ``${VAR_NAME}`` placeholders in *value* with environment variable values.

    If the environment variable is not set, the placeholder is left unchanged
    so the user gets a clear signal that something is misconfigured.

    Returns ``None`` unchanged, otherwise returns the resolved string.
    """
    if value is None:
        return None

    def _replacer(match: re.Match[str]) -> str:
        env_name = match.group(1)
        env_value = os.environ.get(env_name)
        if env_value is not None:
            return env_value
        # Leave the placeholder intact if the env var is not set
        return match.group(0)

    return _ENV_VAR_RE.sub(_replacer, value)


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
    # A site may provide one or more of: a feed URL, a list of listing
    # page URLs, or a static list of article URLs.
    feed: str | None = None
    listing_urls: list[str] = field(default_factory=list)
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
    playwright_wait_until: (
        Literal["commit", "domcontentloaded", "load", "networkidle"] | None
    ) = None  # "domcontentloaded" (default),
    # "load", "networkidle", etc.

    # ── Proxy configuration ──────────────────────────────────────────────
    # Per-site HTTPS proxy. Supports ${VAR_NAME} for environment variable
    # substitution, or a literal URL.
    proxy_server: str | None = None
    # Proxy authentication in "user:password" format. Supports ${VAR_NAME}
    # for environment variable substitution, or a literal value.
    proxy_user_pass: str | None = None

    # ── Listing / article processing ───────────────────────────────────────
    listing_link_pattern: str | None = None
    listing_class: str | None = None
    resolve_relative_to_root: bool = False
    exclusions: list[str] = field(default_factory=list)
    remove_suffix: str | None = None
    # If True, attempt to unfurl multi-page articles (detect "Next page"
    # links, fetch subsequent pages, and merge into a single article).
    unfurl_multipage: bool = False

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

        Any ``{yyyy}`` placeholders in the ``feed``, ``listing_urls`` and
        ``urls`` fields are expanded to the current year at load time.

        For backward compatibility, ``listing_urls`` also accepts the legacy
        ``listing_url`` key (a single string) — it is coerced to a
        one-element list.
        """
        # Support both `listing_urls` (new, array) and `listing_url` (legacy, string)
        listing_urls_raw = data.get("listing_urls")
        if listing_urls_raw is None:
            legacy_listing_url = data.get("listing_url")
            listing_urls_raw = [legacy_listing_url] if legacy_listing_url else []
        elif isinstance(listing_urls_raw, str):
            listing_urls_raw = [listing_urls_raw]

        return cls(
            name=data["name"],
            slug=data["slug"],
            feed=expand_placeholders(data.get("feed")),
            listing_urls=[
                u
                for u in (expand_placeholders(u) for u in listing_urls_raw)
                if u is not None
            ],
            urls=[
                u
                for u in (expand_placeholders(u) for u in (data.get("urls") or []))
                if u is not None
            ],
            categories=data.get("categories") or [],
            limit=data.get("limit"),
            feed_limit=data.get("feed_limit"),
            listing_limit=data.get("listing_limit"),
            force_playwright=data.get("force_playwright", False),
            trust_insecure_certs=data.get("trust_insecure_certs", False),
            exclude_query_params=data.get("exclude_query_params", False),
            playwright_wait_until=data.get("playwright_wait_until"),
            proxy_server=resolve_env_vars(data.get("proxy_server")),
            proxy_user_pass=resolve_env_vars(data.get("proxy_user_pass")),
            exclusions=data.get("exclusions") or [],
            listing_link_pattern=data.get("listing_link_pattern"),
            listing_class=data.get("listing_class"),
            resolve_relative_to_root=data.get("resolve_relative_to_root", False),
            remove_suffix=data.get("remove_suffix"),
            unfurl_multipage=data.get("unfurl_multipage", False),
            notes=data.get("notes"),
        )

    @classmethod
    def load_sites(cls, path: Path = SITES_FILE) -> list[SiteConfig]:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        raw_sites = cast(list[dict[str, Any]], data.get("sites", []))
        return [cls.from_dict(s) for s in raw_sites]
