"""Unit tests for src/text_extraction.py."""

from __future__ import annotations

import asyncio
from unittest.mock import MagicMock

import pytest

from src.text_extraction import (
    _find_next_page_url,
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
    restore_trailing_dot_images,
    resolve_srcset_images,
    unfurl_multipage_article,
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

    def test_adds_jpg_to_trailing_dot_path(self) -> None:
        """CDNs like The Independent serve images with trailing dots (e.g. '123..').
        ensure_image_extension appends .jpg so trafilatura accepts the URL."""
        url = "https://static.independent.co.uk/2026/10/30/12/2279298894.."
        result = ensure_image_extension(url)
        assert result == "https://static.independent.co.uk/2026/10/30/12/2279298894...jpg"

    def test_adds_jpg_to_trailing_dot_path_with_query(self) -> None:
        """Trailing dot paths with query strings should also get .jpg appended."""
        url = "https://static.independent.co.uk/2026/10/30/12/2279298894..?quality=75&width=640&auto=webp"
        result = ensure_image_extension(url)
        assert result == "https://static.independent.co.uk/2026/10/30/12/2279298894...jpg?quality=75&width=640&auto=webp"


class TestRestoreTrailingDotImages:
    """Tests for restore_trailing_dot_images."""

    def test_restores_trailing_dot_in_img_src(self) -> None:
        html = '<img src="https://cdn.com/2279298894...jpg?quality=75&width=640">'
        result = restore_trailing_dot_images(html)
        assert 'src="https://cdn.com/2279298894..?quality=75&width=640"' in result

    def test_restores_trailing_dot_in_markdown_image(self) -> None:
        md = '![alt](https://cdn.com/2279298894...jpg?quality=75&width=640)'
        result = restore_trailing_dot_images(md)
        assert '](https://cdn.com/2279298894..?quality=75&width=640)' in result

    def test_does_not_touch_normal_jpg(self) -> None:
        html = '<img src="https://cdn.com/photo.jpg">'
        result = restore_trailing_dot_images(html)
        assert result == html

    def test_does_not_touch_jpeg(self) -> None:
        html = '<img src="https://cdn.com/photo.jpeg?w=640">'
        result = restore_trailing_dot_images(html)
        assert result == html

    def test_restores_multiple_images(self) -> None:
        html = (
            '<img src="https://cdn.com/123...jpg?w=320">'
            '<img src="https://cdn.com/456...jpg?w=640">'
        )
        result = restore_trailing_dot_images(html)
        assert "123..?w=320" in result
        assert "456..?w=640" in result

    def test_handles_empty_string(self) -> None:
        assert restore_trailing_dot_images("") == ""

    def test_no_change_when_no_trailing_dot_pattern(self) -> None:
        html = "<p>No images here</p>"
        result = restore_trailing_dot_images(html)
        assert result == html

    def test_restores_independent_cdn_url(self) -> None:
        """Real-world example from The Independent CDN."""
        html = '<img src="https://static.independent.co.uk/2026/10/30/12/2279298894...jpg?quality=75&width=640&auto=webp">'
        result = restore_trailing_dot_images(html)
        assert 'src="https://static.independent.co.uk/2026/10/30/12/2279298894..?quality=75&width=640&auto=webp"' in result


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


class TestFindNextPageUrl:
    """Tests for _find_next_page_url."""

    def test_rel_next_link_tag(self) -> None:
        html = """<html><head>
        <link rel="next" href="https://example.com/article/2" />
        </head><body><p>Page 1</p></body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_next_page_class(self) -> None:
        html = """<html><body>
        <p>Page 1</p>
        <a class="next-page" href="/article/2">Next</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_next_link_text(self) -> None:
        html = """<html><body>
        <p>Page 1</p>
        <a href="/article/2">Next page</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_next_link_text_uppercase(self) -> None:
        html = """<html><body>
        <p>Page 1</p>
        <a href="/article/2">NEXT</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_arrow_link_text(self) -> None:
        html = """<html><body>
        <p>Page 1</p>
        <a href="/article/2">›</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_page_number_link_text(self) -> None:
        html = """<html><body>
        <p>Page 1</p>
        <a href="/article/3">Page 3</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/3"

    def test_no_pagination_returns_none(self) -> None:
        html = """<html><body><p>Single page article</p></body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result is None

    def test_relative_url_resolved(self) -> None:
        html = """<html><body>
        <a class="next-page" href="/article/2">Next</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_aria_label_next(self) -> None:
        html = """<html><body>
        <a aria-label="Next page" href="/article/2">›</a>
        </body></html>"""
        result = _find_next_page_url(html, "https://example.com/article/1")
        assert result == "https://example.com/article/2"

    def test_invalid_html_returns_none(self) -> None:
        result = _find_next_page_url("not html at all", "https://example.com/page")
        assert result is None


class TestUnfurlMultipageArticle:
    """Tests for unfurl_multipage_article."""

    @pytest.mark.asyncio
    async def test_returns_original_when_no_pagination(self) -> None:
        html = "<html><body><p>Single page</p></body></html>"
        base_url = "https://example.com/article/1"

        async def fetcher(url: str) -> str | None:
            return "<html><body><p>Should not be called</p></body></html>"

        result = await unfurl_multipage_article(html, base_url, fetcher)
        # When no pagination, the function extracts the body and wraps it
        # in a minimal HTML document — content should be preserved
        assert "<p>Single page</p>" in result
        assert "unfurled-page" not in result

    @pytest.mark.asyncio
    async def test_merges_two_pages(self) -> None:
        page1 = """<html><body>
        <p>Page 1 content</p>
        <a class="next-page" href="/article/2">Next</a>
        </body></html>"""
        page2 = """<html><body>
        <h2>Continued</h2>
        <p>Page 2 content</p>
        </body></html>"""

        call_count = 0

        async def fetcher(url: str) -> str | None:
            nonlocal call_count
            call_count += 1
            return page2

        result = await unfurl_multipage_article(
            page1, "https://example.com/article/1", fetcher
        )
        assert call_count == 1
        assert "Page 1 content" in result
        assert "unfurled-page" in result

    @pytest.mark.asyncio
    async def test_stops_when_fetch_fails(self) -> None:
        page1 = """<html><body>
        <p>Page 1</p>
        <a class="next-page" href="/article/2">Next</a>
        </body></html>"""

        async def fetcher(url: str) -> str | None:
            return None  # Simulate fetch failure

        logger = MagicMock()
        result = await unfurl_multipage_article(
            page1, "https://example.com/article/1", fetcher, logger=logger
        )
        # Should return original HTML when fetch fails
        assert "Page 1" in result
        logger.log.assert_called()
        assert "failed to fetch" in logger.log.call_args[0][0]

    @pytest.mark.asyncio
    async def test_respects_max_pages(self) -> None:
        """Should not fetch more than max_pages."""
        html = """<html><body>
        <p>Content</p>
        <a class="next-page" href="/article/2">Next</a>
        </body></html>"""

        call_count = 0

        async def fetcher(url: str) -> str | None:
            nonlocal call_count
            call_count += 1
            # Return HTML with another "Next" link to test max_pages limit
            return """<html><body>
            <p>More content</p>
            <a class="next-page" href="/article/3">Next</a>
            </body></html>"""

        result = await unfurl_multipage_article(
            html, "https://example.com/article/1", fetcher, max_pages=3
        )
        # Should have fetched 2 additional pages (max_pages=3, page 1 already fetched)
        assert call_count <= 2

    @pytest.mark.asyncio
    async def test_avoids_infinite_loop(self) -> None:
        """If next URL equals current URL, stop."""
        html = """<html><body>
        <p>Content</p>
        <a class="next-page" href="/article/1">Next</a>
        </body></html>"""

        async def fetcher(url: str) -> str | None:
            raise AssertionError("Should not fetch when next URL equals current")

        result = await unfurl_multipage_article(
            html, "https://example.com/article/1", fetcher
        )
        # Content should be preserved; fetcher should not be called
        assert "Content" in result
        assert "unfurled-page" not in result
