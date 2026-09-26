"""Unit tests for src/sites.py - config loading & {yyyy} placeholder expansion."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
import yaml

from src.sites import SiteConfig, expand_placeholders

# ─── expand_placeholders unit tests ────────────────────────────────────────


def test_expand_placeholders_expands_token() -> None:
    """The {yyyy} literal token should be expanded to the current year."""
    current_year = datetime.now(UTC).strftime("%Y")
    result = expand_placeholders("https://example.com/news/{yyyy}/")
    assert result == f"https://example.com/news/{current_year}/"
    assert "{yyyy}" not in result


def test_expand_placeholders_none_returns_none() -> None:
    """A None input should return None (not crash)."""
    assert expand_placeholders(None) is None


def test_expand_placeholders_no_placeholder_unchanged() -> None:
    """A string without any placeholder should be returned as-is."""
    url = "https://example.com/news/latest"
    assert expand_placeholders(url) == url


def test_expand_placeholders_multiple_occurrences() -> None:
    """Every occurrence of {yyyy} in the same string should be replaced."""
    current_year = datetime.now(UTC).strftime("%Y")
    url = f"https://example.com/{current_year}/path/{current_year}/"
    assert expand_placeholders("https://example.com/{yyyy}/path/{yyyy}/") == url


def test_expand_placeholders_in_url_with_query() -> None:
    """{yyyy} inside a query string should also be expanded."""
    current_year = datetime.now(UTC).strftime("%Y")
    result = expand_placeholders(
        f"https://example.com/search?year={{yyyy}}&q={current_year}"
    )
    assert result == f"https://example.com/search?year={current_year}&q={current_year}"


# ─── SiteConfig.from_dict tests ────────────────────────────────────────────


def test_from_dict_expands_yyyy_in_listing_url() -> None:
    """from_dict should expand {yyyy} in listing_url."""
    current_year = datetime.now(UTC).strftime("%Y")
    site = SiteConfig.from_dict(
        {
            "name": "Test Site",
            "slug": "test",
            "listing_url": "https://example.com/news/{yyyy}/",
        }
    )
    assert site.listing_url == f"https://example.com/news/{current_year}/"


def test_from_dict_expands_yyyy_in_feed() -> None:
    """from_dict should expand {yyyy} in feed URL."""
    current_year = datetime.now(UTC).strftime("%Y")
    site = SiteConfig.from_dict(
        {
            "name": "Test Site",
            "slug": "test",
            "feed": "https://example.com/rss/{yyyy}.xml",
        }
    )
    assert site.feed == f"https://example.com/rss/{current_year}.xml"


def test_from_dict_expands_yyyy_in_urls() -> None:
    """from_dict should expand {yyyy} in each entry of the urls list."""
    current_year = datetime.now(UTC).strftime("%Y")
    site = SiteConfig.from_dict(
        {
            "name": "Test Site",
            "slug": "test",
            "urls": [
                "https://example.com/news/{yyyy}/article-1",
                "https://example.com/news/{yyyy}/article-2",
            ],
        }
    )
    assert site.urls == [
        f"https://example.com/news/{current_year}/article-1",
        f"https://example.com/news/{current_year}/article-2",
    ]


def test_from_dict_no_placeholder_unchanged() -> None:
    """from_dict should leave URLs without placeholders untouched."""
    site = SiteConfig.from_dict(
        {
            "name": "Test Site",
            "slug": "test",
            "feed": "https://example.com/rss/latest",
            "listing_url": "https://example.com/news/latest",
            "urls": ["https://example.com/article-1"],
        }
    )
    assert site.feed == "https://example.com/rss/latest"
    assert site.listing_url == "https://example.com/news/latest"
    assert site.urls == ["https://example.com/article-1"]


def test_from_dict_none_urls_when_missing() -> None:
    """from_dict should default urls to an empty list when absent."""
    site = SiteConfig.from_dict({"name": "Test Site", "slug": "test"})
    assert site.urls == []
    assert site.feed is None
    assert site.listing_url is None


# ─── Real sites.yaml integration test ──────────────────────────────────────


def test_sites_yaml_york_uses_yyyy_placeholder() -> None:
    """The University of York entry in sites.yaml should use {yyyy}.

    After loading, the listing_url must contain the current year, not the
    literal ``{yyyy}`` token.
    """
    sites_yaml = Path(__file__).resolve().parents[2] / "sites.yaml"
    with open(sites_yaml, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    york_entry = next(s for s in data["sites"] if s["slug"] == "york-university")
    # The raw YAML should contain the placeholder token
    assert "{yyyy}" in york_entry["listing_url"]

    # After from_dict expansion it should be replaced with the current year
    config = SiteConfig.from_dict(york_entry)
    current_year = datetime.now(UTC).strftime("%Y")
    assert f"/{current_year}/" in config.listing_url
    assert "{yyyy}" not in config.listing_url


def test_sites_yaml_all_urls_expand_yyyy() -> None:
    """Every {yyyy} in the real sites.yaml must expand after loading.

    This guards against accidentally introducing a literal ``{yyyy}`` that
    a future run would try to fetch.
    """
    sites_yaml = Path(__file__).resolve().parents[2] / "sites.yaml"
    configs = SiteConfig.load_sites(sites_yaml)

    for config in configs:
        if config.feed and "{yyyy}" in config.feed:
            pytest.fail(f"feed not expanded in {config.slug}: {config.feed}")
        if config.listing_url and "{yyyy}" in config.listing_url:
            pytest.fail(
                f"listing_url not expanded in {config.slug}: {config.listing_url}"
            )
        for url in config.urls:
            if "{yyyy}" in url:
                pytest.fail(f"url not expanded in {config.slug}: {url}")
