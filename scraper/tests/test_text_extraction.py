"""Unit tests for src/text_extraction.py."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.text_extraction import (
    clean_markdown_formatting,
    extract_first_image_from_markdown,
    html_to_markdown,
    linkify_text,
    normalize_exclusion,
    normalize_inline_spacing,
    remove_excluded_elements,
)


class TestCleanMarkdownFormatting:
    """Tests for clean_markdown_formatting."""

    def test_empty_string_returns_empty(self) -> None:
        assert clean_markdown_formatting("") == ""

    def test_removes_published_bullet(self) -> None:
        # Pattern matches "* Published" or "- Published" as a list item
        text = "Some intro\n* Published\nSome content"
        result = clean_markdown_formatting(text)
        assert "Published" not in result
        assert "Some content" in result

    def test_removes_recommended_reading(self) -> None:
        text = "Content before\n**Recommended reading:**\nContent after"
        result = clean_markdown_formatting(text)
        assert "Recommended reading" not in result

    def test_strips_surrounding_whitespace(self) -> None:
        text = "  some content  "
        result = clean_markdown_formatting(text)
        assert result == "some content"


class TestLinkifyText:
    """Tests for linkify_text."""

    def test_empty_string_returns_empty(self) -> None:
        assert linkify_text("") == ""

    def test_linkifies_bare_url(self) -> None:
        text = "Check this out: https://example.com/page"
        result = linkify_text(text)
        assert "[https://example.com/page](https://example.com/page)" in result

    def test_preserves_existing_markdown_links(self) -> None:
        text = "[example](https://example.com)"
        result = linkify_text(text)
        assert result == text

    def test_links_emails(self) -> None:
        text = "Contact us at test@example.com for info"
        result = linkify_text(text)
        assert "[test@example.com](mailto:test@example.com)" in result

    def test_removes_excluded_images(self) -> None:
        text = "![placeholder image](https://example.com/img.jpg)"
        result = linkify_text(text)
        assert result == ""

    def test_keeps_non_excluded_images(self) -> None:
        text = "![alt text](https://example.com/img.jpg)"
        result = linkify_text(text)
        assert "![alt text](https://example.com/img.jpg)" in result


class TestExtractFirstImageFromMarkdown:
    """Tests for extract_first_image_from_markdown."""

    def test_returns_first_image_url(self) -> None:
        md = "Some text\n![alt](https://example.com/img.jpg)\nMore text"
        assert extract_first_image_from_markdown(md) == "https://example.com/img.jpg"

    def test_returns_none_when_no_image(self) -> None:
        md = "Just text, no images here"
        assert extract_first_image_from_markdown(md) is None

    def test_handles_multiple_images(self) -> None:
        md = "![first](https://a.com/1.jpg)\n![second](https://b.com/2.jpg)"
        result = extract_first_image_from_markdown(md)
        assert result == "https://a.com/1.jpg"


class TestHtmlToMarkdown:
    """Tests for html_to_markdown."""

    def test_converts_html_to_markdown(self) -> None:
        html = "<p>Hello <strong>world</strong></p>"
        result = html_to_markdown(html)
        assert "Hello" in result
        assert "world" in result

    def test_handles_empty_html(self) -> None:
        result = html_to_markdown("")
        assert result.strip() == ""


class TestNormalizeInlineSpacing:
    """Tests for normalize_inline_spacing."""

    def test_moves_leading_whitespace_outside(self) -> None:
        html = "<div>Hello <em> world</em></div>"
        result = normalize_inline_spacing(html)
        assert "<em>world" in result
        assert result.index(" ") < result.index("<em>")

    def test_moves_trailing_whitespace_outside(self) -> None:
        html = "<div>Hello <strong>world </strong>after</div>"
        result = normalize_inline_spacing(html)
        assert "world </strong>" not in result


class TestNormalizeExclusion:
    """Tests for normalize_exclusion."""

    def test_returns_xpath_unchanged(self) -> None:
        expr = "//div[@class='test']"
        assert normalize_exclusion(expr) == expr

    def test_returns_root_xpath_unchanged(self) -> None:
        expr = "/html/body"
        assert normalize_exclusion(expr) == expr

    def test_returns_dot_xpath_unchanged(self) -> None:
        expr = ".//div"
        assert normalize_exclusion(expr) == expr

    def test_returns_descendant_xpath_unchanged(self) -> None:
        expr = "descendant::div"
        assert normalize_exclusion(expr) == expr

    def test_translates_attr_selector(self) -> None:
        expr = "role='dialog'"
        result = normalize_exclusion(expr)
        assert result == "//*[@role='dialog']"

    def test_translates_attr_selector_double_quotes(self) -> None:
        expr = 'role="dialog"'
        result = normalize_exclusion(expr)
        assert result == "//*[@role='dialog']"

    def test_returns_plain_class_as_xpath(self) -> None:
        expr = ".some-class"
        result = normalize_exclusion(expr)
        assert result == expr


class TestRemoveExcludedElements:
    """Tests for remove_excluded_elements."""

    def test_returns_html_unchanged_when_no_exclusions(self) -> None:
        html = "<div><p>Hello</p></div>"
        result = remove_excluded_elements(html, [])
        assert result == html

    def test_removes_elements_by_attr_selector(self) -> None:
        html = '<div><p class="keep">Keep me</p><p role="dialog">Remove me</p></div>'
        result = remove_excluded_elements(html, ["role='dialog'"])
        assert "Remove me" not in result
        assert "Keep me" in result

    def test_removes_elements_by_xpath(self) -> None:
        html = '<div><aside class="paywall">Paywall</aside><p>Keep</p></div>'
        result = remove_excluded_elements(html, ["//aside"])
        assert "Paywall" not in result
        assert "Keep" in result

    def test_logs_removal_count(self) -> None:
        html = '<div><p role="dialog">A</p><p role="dialog">B</p></div>'
        logger = MagicMock()
        remove_excluded_elements(html, ["role='dialog'"], logger=logger)
        logger.log.assert_called_once()
        log_msg = logger.log.call_args[0][0]
        assert "excluded 2" in log_msg

    def test_handles_list_tree_fromstring(self) -> None:
        html = '<div><p role="dialog">Remove</p><p>Keep</p></div>'
        result = remove_excluded_elements(html, ["role='dialog'"])
        assert "Remove" not in result
        assert "Keep" in result
