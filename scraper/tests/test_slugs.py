"""Unit tests for src/slugs.py."""

from __future__ import annotations

from src.slugs import slugify, url_to_slug


class TestSlugify:
    """Tests for slugify."""

    def test_lowercases_text(self) -> None:
        assert slugify("Hello World") == "hello-world"

    def test_strips_surrounding_whitespace(self) -> None:
        assert slugify("  hello  ") == "hello"

    def test_replaces_spaces_with_hyphens(self) -> None:
        assert slugify("hello world foo") == "hello-world-foo"

    def test_replaces_underscores_with_hyphens(self) -> None:
        assert slugify("hello_world_foo") == "hello-world-foo"

    def test_collapses_multiple_hyphens(self) -> None:
        assert slugify("hello---world") == "hello-world"

    def test_removes_special_chars(self) -> None:
        assert slugify("hello!@world#$") == "helloworld"

    def test_truncates_to_80_chars(self) -> None:
        text = "a" * 100
        result = slugify(text)
        assert len(result) == 80

    def test_empty_string_returns_empty(self) -> None:
        assert slugify("") == ""

    def test_only_special_chars_returns_empty(self) -> None:
        assert slugify("!@#$%^&*()") == ""


class TestUrlToSlug:
    """Tests for url_to_slug."""

    def test_basic_url(self) -> None:
        result = url_to_slug("https://example.com/path/to/page")
        assert "path" in result
        assert "to" in result
        assert "page" in result

    def test_strips_leading_slash(self) -> None:
        result = url_to_slug("https://example.com//article")
        assert not result.startswith("/")
        assert "article" in result

    def test_handles_empty_path(self) -> None:
        result = url_to_slug("https://example.com")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_exclude_query_params_ignores_query(self) -> None:
        url1 = "https://example.com/article?utm_source=rss&utm_medium=feed"
        url2 = "https://example.com/article?foo=bar&baz=qux"
        result1 = url_to_slug(url1, exclude_query_params=True)
        result2 = url_to_slug(url2, exclude_query_params=True)
        # With exclude_query_params=True, both should only contain path
        assert "utm" not in result1.lower()
        assert "foo" not in result2.lower()

    def test_includes_filtered_query_params(self) -> None:
        url = "https://example.com/article?utm_source=rss&id=123"
        result = url_to_slug(url, exclude_query_params=False)
        assert "utm" not in result.lower()
        assert "id" in result

    def test_removes_utm_params_from_query(self) -> None:
        url = "https://example.com/path?utm_source=rss&utm_campaign=test&id=456"
        result = url_to_slug(url, exclude_query_params=False)
        assert "utm_source" not in result
        assert "utm_campaign" not in result
        assert "id" in result

    def test_preserves_multiple_non_utm_params(self) -> None:
        url = "https://example.com/path?id=123&page=2"
        result = url_to_slug(url, exclude_query_params=False)
        assert "id" in result
        assert "page" in result

    def test_empty_query_returns_path_slug(self) -> None:
        url = "https://example.com/some/article"
        result = url_to_slug(url)
        assert "some" in result
        assert "article" in result

    def test_falls_back_to_hash_for_empty_slug(self) -> None:
        """When slug is empty after processing, should use SHA1 hash."""
        url = "https://example.com/"
        result = url_to_slug(url, exclude_query_params=True)
        # The result should be a hash since path is just /
        assert len(result) == 10
        assert result.isalnum()

    def test_nested_path(self) -> None:
        result = url_to_slug("https://example.com/a/b/c/d")
        assert "a--b--c--d" in result or ("a" in result and "b" in result)
