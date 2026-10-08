"""Unit tests for src/text_extraction.py."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.text_extraction import (
    clean_markdown_formatting,
    ensure_image_extension,
    extract_first_image_from_markdown,
    html_to_markdown,
    linkify_text,
    normalize_exclusion,
    normalize_inline_spacing,
    parse_srcset,
    pick_largest_srcset_url,
    remove_excluded_elements,
    resolve_srcset_images,
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

    def test_removes_figure_containing_specific_image(self) -> None:
        """Mimics the TechRadar Google News badge exclusion: a <figure>
        wrapping a targeted image is removed while other figures survive."""
        html = """\
<div>
  <p>Real article content that should survive.</p>
  <a href="https://news.google.com/publications/xyz" target="_blank">
    <figure class="van-image-figure pull-right inline-layout">
      <div class="image-full-width-wrapper">
        <div class="image-widthsetter" style="max-width:676px;">
          <p class="vanilla-image-block">
            <picture>
              <img src="https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg"
                   alt="Click to follow TechRadar">
            </picture>
          </p>
        </div>
      </div>
    </figure>
  </a>
  <figure class="van-image-figure">
    <p>
      <picture>
        <img src="https://cdn.mos.cms.futurecdn.net/legit-article-image.jpg"
             alt="A real photo">
      </picture>
    </p>
  </figure>
</div>"""
        xpath = "//figure[.//img[contains(@src, 'diM9tpwF2Lz85R8q85CT78')]]"
        result = remove_excluded_elements(html, [xpath])
        assert "diM9tpwF2Lz85R8q85CT78" not in result
        assert "Click to follow TechRadar" not in result
        assert "Real article content" in result
        assert "legit-article-image" in result


class TestParseSrcset:
    """Tests for parse_srcset."""

    def test_parses_width_descriptors(self) -> None:
        srcset = (
            "https://example.com/large.jpg 1400w, https://example.com/small.jpg 575w"
        )
        result = parse_srcset(srcset)
        assert result == [
            ("https://example.com/large.jpg", 1400),
            ("https://example.com/small.jpg", 575),
        ]

    def test_parses_multi_line_srcset(self) -> None:
        srcset = (
            "https://example.com/img.jpg 575w,\n"
            "        https://example.com/img.jpg 962w,\n"
            "        https://example.com/img.jpg 1400w"
        )
        result = parse_srcset(srcset)
        assert len(result) == 3
        assert result[0] == ("https://example.com/img.jpg", 575)
        assert result[2] == ("https://example.com/img.jpg", 1400)

    def test_parses_pixel_density_descriptors(self) -> None:
        srcset = "https://example.com/img.jpg 2x, https://example.com/img.jpg"
        result = parse_srcset(srcset)
        assert result == [
            ("https://example.com/img.jpg", None),
            ("https://example.com/img.jpg", None),
        ]

    def test_parses_urls_without_descriptors(self) -> None:
        srcset = "https://example.com/a.jpg, https://example.com/b.jpg"
        result = parse_srcset(srcset)
        assert result == [
            ("https://example.com/a.jpg", None),
            ("https://example.com/b.jpg", None),
        ]

    def test_handles_comma_in_query_parameter_crop(self) -> None:
        """URLs with commas in query params (crop=3:2,smart) should not be split."""
        srcset = (
            "https://www.harrogateadvertiser.co.uk/webimg/"
            "b25lY21zOjA2MWI1NTVkLWMxODAtNDNiNC04MmM0LWI4Mzc0YTFlYzkzMQ.jpg"
            "?crop=3:2,smart&trim=&width=320&quality=65 320w,"
            " https://www.harrogateadvertiser.co.uk/webimg/"
            "b25lY21zOjA2MWI1NTVkLWMxODAtNDNiNC04MmM0LWI4Mzc0YTFlYzkzMQ.jpg"
            "?crop=3:2,smart&trim=&width=626&quality=65 626w"
        )
        result = parse_srcset(srcset)
        assert len(result) == 2
        assert result[0][1] == 320
        assert result[1][1] == 626
        assert "crop=3:2,smart&trim=&width=320" in result[0][0]
        assert "crop=3:2,smart&trim=&width=626" in result[1][0]

    def test_handles_comma_in_query_parameter_trim(self) -> None:
        """URLs with commas in trim param (trim=0,0,0,0) should not be split."""
        srcset = (
            "https://www.harrogateadvertiser.co.uk/jpim-static/image/2026/10/07/"
            "11/31/Artistic-impression.jpeg?trim=0,0,0,0&width=320&quality=65 320w,"
            " https://www.harrogateadvertiser.co.uk/jpim-static/image/2026/10/07/"
            "11/31/Artistic-impression.jpeg?trim=0,0,0,0&width=640&quality=65 640w"
        )
        result = parse_srcset(srcset)
        assert len(result) == 2
        assert result[0][1] == 320
        assert result[1][1] == 640
        assert "trim=0,0,0,0" in result[0][0]
        assert "trim=0,0,0,0" in result[1][0]

    def test_handles_empty_srcset(self) -> None:
        assert parse_srcset("") == []
        assert parse_srcset("  ") == []


class TestPickLargestSrcsetUrl:
    """Tests for pick_largest_srcset_url."""

    def test_picks_highest_width(self) -> None:
        srcset = "a.jpg 575w, b.jpg 1400w, c.jpg 962w"
        assert pick_largest_srcset_url(srcset) == "b.jpg"

    def test_picks_last_when_same_width(self) -> None:
        srcset = "a.jpg 500w, b.jpg 500w"
        assert pick_largest_srcset_url(srcset) == "b.jpg"

    def test_falls_back_to_first_when_no_width(self) -> None:
        srcset = "a.jpg 2x, b.jpg"
        assert pick_largest_srcset_url(srcset) == "a.jpg"

    def test_handles_single_entry(self) -> None:
        srcset = "https://example.com/large.jpg 1400w"
        assert pick_largest_srcset_url(srcset) == "https://example.com/large.jpg"

    def test_returns_none_for_empty_srcset(self) -> None:
        assert pick_largest_srcset_url("") is None

    def test_handles_mixed_descriptors(self) -> None:
        srcset = "small.jpg 575w, medium.jpg 2x, large.jpg 1400w"
        # Should pick large.jpg since it has the highest width descriptor
        assert pick_largest_srcset_url(srcset) == "large.jpg"


class TestEnsureImageExtension:
    """Tests for ensure_image_extension."""

    def test_adds_jpg_to_url_with_query_string(self) -> None:
        url = "https://example.com/img/123/?type=large"
        result = ensure_image_extension(url)
        assert result == "https://example.com/img/123.jpg?type=large"

    def test_adds_jpg_to_url_without_query_string(self) -> None:
        url = "https://example.com/img/123"
        result = ensure_image_extension(url)
        assert result == "https://example.com/img/123.jpg"

    def test_preserves_existing_jpg_extension(self) -> None:
        url = "https://example.com/img/photo.jpg"
        assert ensure_image_extension(url) == url

    def test_preserves_existing_png_extension(self) -> None:
        url = "https://example.com/img/photo.png"
        assert ensure_image_extension(url) == url

    def test_preserves_extension_with_query_string(self) -> None:
        url = "https://example.com/img/photo.jpg?type=large"
        assert ensure_image_extension(url) == url

    def test_preserves_webp_extension(self) -> None:
        url = "https://example.com/img/photo.webp"
        assert ensure_image_extension(url) == url

    def test_handles_uppercase_extension(self) -> None:
        url = "https://example.com/img/photo.JPG"
        assert ensure_image_extension(url) == url

    def test_adds_jpg_to_relative_url(self) -> None:
        url = "/resources/images/21500997/?type=mds-article-620"
        result = ensure_image_extension(url)
        assert result == "/resources/images/21500997.jpg?type=mds-article-620"


class TestResolveSrcsetImages:
    """Tests for resolve_srcset_images."""

    def test_converts_srcset_to_src_largest(self) -> None:
        html = '<img srcset="small.jpg 575w, large.jpg 1400w" alt="test">'
        result = resolve_srcset_images(html)
        assert 'src="large.jpg"' in result
        assert "srcset" not in result
        assert "sizes" not in result

    def test_resolves_relative_urls_with_base_url(self) -> None:
        html = '<img srcset="/img/small.jpg 575w, /img/large.jpg 1400w" alt="test">'
        result = resolve_srcset_images(html, base_url="https://example.com")
        assert 'src="https://example.com/img/large.jpg"' in result

    def test_adds_image_extension_to_srcset_url(self) -> None:
        html = (
            '<img srcset="https://example.com/img/123/?type=575 575w, '
            'https://example.com/img/123/?type=620 1400w" alt="test">'
        )
        result = resolve_srcset_images(html)
        assert 'src="https://example.com/img/123.jpg?type=620"' in result

    def test_preserves_existing_src_when_no_srcset(self) -> None:
        html = '<img src="https://example.com/img.jpg" alt="test">'
        result = resolve_srcset_images(html)
        assert 'src="https://example.com/img.jpg"' in result

    def test_overrides_existing_src_with_largest_from_srcset(self) -> None:
        html = (
            '<img src="https://example.com/small.jpg" '
            'srcset="https://example.com/small.jpg 575w, '
            'https://example.com/large.jpg 1400w" alt="test">'
        )
        result = resolve_srcset_images(html)
        assert 'src="https://example.com/large.jpg"' in result

    def test_handles_multiple_srcset_images(self) -> None:
        html = (
            "<html><body>"
            '<img srcset="a.jpg 575w, b.jpg 1400w" alt="img1">'
            '<img srcset="c.jpg 320w, d.jpg 768w, e.jpg 1920w" alt="img2">'
            "</body></html>"
        )
        result = resolve_srcset_images(html)
        assert 'src="b.jpg"' in result
        assert 'src="e.jpg"' in result

    def test_removes_sizes_attribute(self) -> None:
        html = '<img srcset="a.jpg 1400w" sizes="(max-width: 992px) 962px" alt="test">'
        result = resolve_srcset_images(html)
        assert "sizes" not in result

    def test_handles_multi_line_srcset(self) -> None:
        html = (
            '<img srcset="/img/a.jpg 575w,\n'
            "        /img/b.jpg 962w,\n"
            '        /img/c.jpg 1400w" alt="test">'
        )
        result = resolve_srcset_images(html, base_url="https://example.com")
        assert 'src="https://example.com/img/c.jpg"' in result

    def test_handles_srcset_without_width_descriptors(self) -> None:
        html = '<img srcset="a.jpg 2x, b.jpg" alt="test">'
        result = resolve_srcset_images(html)
        assert 'src="a.jpg"' in result

    def test_handles_empty_html(self) -> None:
        assert resolve_srcset_images("") == ""

    def test_no_changes_when_no_srcset_images(self) -> None:
        html = "<html><body><p>No images here</p></body></html>"
        result = resolve_srcset_images(html)
        assert "<img" not in result

    def test_logs_processed_count(self) -> None:
        html = (
            "<html><body>"
            '<img srcset="a.jpg 575w, b.jpg 1400w" alt="img1">'
            '<img srcset="c.jpg 320w, d.jpg 768w" alt="img2">'
            "</body></html>"
        )
        logger = MagicMock()
        resolve_srcset_images(html, logger=logger)
        logger.log.assert_called_once()
        log_msg = logger.log.call_args[0][0]
        assert "2" in log_msg

    def test_does_not_log_when_no_srcset(self) -> None:
        html = '<html><body><img src="a.jpg" alt="test"></body></html>'
        logger = MagicMock()
        resolve_srcset_images(html, logger=logger)
        logger.log.assert_not_called()

    def test_works_with_realistic_york_press_html(self) -> None:
        """Mimics the structure from the York Press article."""
        html = (
            "<article>"
            '<p><img srcset="https://www.yorkpress.co.uk/resources/images/'
            "21500997/?type=mds-article-575 575w, "
            "https://www.yorkpress.co.uk/resources/images/"
            '21500997/?type=mds-article-620 1401w"'
            ' sizes="(max-width: 575px) 575px" width="100%">'
            '<span class="inline-image-caption">Caption text</span></p>'
            "</article>"
        )
        result = resolve_srcset_images(html)
        # The extensionless URL should get .jpg added
        assert (
            'src="https://www.yorkpress.co.uk/resources/images/21500997.jpg'
            '?type=mds-article-620"'
        ) in result
        assert "srcset" not in result
        assert "sizes" not in result
