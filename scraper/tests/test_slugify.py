"""Unit tests for helper functions."""

from __future__ import annotations

from src.helpers import url_to_slug


def test_url_to_slug_basic() -> None:
    """url_to_slug should produce a filesystem-safe slug."""
    slug = url_to_slug("https://example.com/path/to/article?id=123")
    assert "path" in slug
    assert "/" not in slug


def test_url_to_slug_query_params_removed() -> None:
    """url_to_slug should remove query parameters and fragments."""
    slug = url_to_slug("https://example.com/article?foo=bar#section")
    assert "?" not in slug
    assert "#" not in slug


def test_url_to_slug_simple_path() -> None:
    """url_to_slug should handle simple paths."""
    slug = url_to_slug("https://example.com/simple")
    assert slug == "simple"


def test_url_to_slug_nested_path() -> None:
    """url_to_slug should handle nested paths with hyphens."""
    slug = url_to_slug("https://example.com/path/to/my-article")
    assert "path" in slug
    assert "to" in slug or "my-article" in slug


def test_url_to_slug_replaces_special_chars() -> None:
    """url_to_slug should replace special characters."""
    slug = url_to_slug("https://example.com/test article")
    assert " " not in slug  # spaces should be replaced
