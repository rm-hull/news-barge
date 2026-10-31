"""Content extraction and text processing utilities."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import urljoin, urlparse, urlunparse

from lxml import html as lxml_html
from markdownify import markdownify as to_markdown
from trafilatura import extract, extract_metadata

from .constants import TRAFILATURA_CONFIG
from .profiling import profiled

if TYPE_CHECKING:
    from trafilatura.settings import Document


# ---------------------------------------------------------------------------
# Multi-page article unfurling
#
# Some news sites split long articles across multiple pages (e.g. ReachLocal
# sites like Harrogate Advertiser).  These pages are linked via "Next page"
# buttons/links, typically using URL patterns like:
#   /article-name-12345/2  (page 2)
#   /article-name-12345/3  (page 3)
# or via ``rel="next"`` link tags in the <head>.
#
# The unfurling logic detects these links, fetches all subsequent pages,
# extracts their article body content, and merges them into a single HTML
# document before trafilatura extraction.
# ---------------------------------------------------------------------------

# XPath selectors for "Next page" navigation links
_NEXT_PAGE_SELECTORS = [
    # Generic pagination patterns
    "//a[@rel='next']",
    "//a[contains(@class, 'next-page')]",
    "//a[contains(@class, 'next')]",
    "//a[contains(@class, 'pagination-next')]",
    "//a[contains(@class, 'page-next')]",
    "//a[@aria-label='Next']",
    "//a[@aria-label='Next page']",
    # ReachLocal / local news patterns
    "//a[contains(@class, 'article-next')]",
    "//a[contains(@class, 'next-article')]",
    "//div[contains(@class, 'next')]/a",
    "//span[contains(@class, 'next')]/a",
    "//li[contains(@class, 'next')]/a",
]

# Link text patterns that indicate a "Next page" link
_NEXT_PAGE_TEXTS = re.compile(
    r"^(next|next\s+page|page\s+\d+|→|\u203a|»|\s*>\s*)$", re.IGNORECASE
)


def _find_next_page_url(html: str, base_url: str) -> str | None:
    """Find the URL of the next page in a multi-page article.

    Searches for next-page links using multiple strategies:
    1. ``rel="next"`` link tags in <head>
    2. XPath selectors for common pagination patterns
    3. Link text matching "Next", "Next page", page numbers, etc.

    Args:
        html: The raw HTML of the current page.
        base_url: The URL of the current page (for resolving relative URLs).

    Returns:
        The absolute URL of the next page, or ``None`` if not found.
    """
    try:
        tree = lxml_html.fromstring(html)
    except lxml_html.ParserError:
        return None

    next_url: str | None = None

    # Strategy 1: rel="next" in <head> <link> tags
    for link in tree.xpath("//head//link[@rel='next']"):
        href = link.get("href")
        if href:
            next_url = urljoin(base_url, href)
            break

    # Strategy 2: XPath selectors for common pagination patterns
    if next_url is None:
        for selector in _NEXT_PAGE_SELECTORS:
            try:
                elements = tree.xpath(selector)
                if elements:
                    for el in elements:
                        href = el.get("href")
                        if href:
                            next_url = urljoin(base_url, href)
                            break
                    if next_url:
                        break
            except Exception:
                continue

    # Strategy 3: Link text matching
    if next_url is None:
        for anchor in tree.xpath("//a[@href]"):
            href = anchor.get("href")
            if not href:
                continue
            text = (anchor.text_content() or "").strip()
            if _NEXT_PAGE_TEXTS.match(text):
                next_url = urljoin(base_url, href)
                break

    return next_url


async def unfurl_multipage_article(
    html: str,
    base_url: str,
    fetcher: Any,
    *,
    max_pages: int = 20,
    logger: Any = None,
) -> str:
    """Unfurl a multi-page article into a single HTML document.

    Detects "Next page" links in the HTML, fetches subsequent pages,
    extracts their article body content, and appends it to the first page's
    body. Returns the merged HTML where the <body> contains the first page's
    extracted body followed by each subsequent page's extracted body.

    Args:
        html: The raw HTML of the first page.
        base_url: The URL of the first page.
        fetcher: An async callable that fetches HTML for a URL.
            Signature: ``async def fetcher(url) -> str | None``.
        max_pages: Maximum number of pages to fetch (safety limit).
        logger: Optional logger for progress reporting.

    Returns:
        The merged HTML of all pages, or the original HTML if no pagination
        was detected.
    """
    pages_fetched = 1
    current_url = base_url
    # Keep the raw HTML of the last fetched page so we can find the
    # next-page link in it — not in the merged document where old
    # pagination links from earlier pages would confuse detection.
    last_raw_html = html

    # Extract the first page's body so we can concatenate subsequent
    # page bodies with it — trafilatura will re-extract from the final
    # HTML, so we need the bodies in the <body> tag as plain children.
    first_body = extract(
        html,
        url=base_url,
        output_format="html",
        include_comments=False,
        include_formatting=True,
        include_images=True,
        include_tables=True,
        favor_precision=True,
        config=TRAFILATURA_CONFIG,
    )

    # Build a minimal HTML document with just the first page's body
    if first_body:
        merged_html = f"<html><body>{first_body}</body></html>"
    else:
        merged_html = html

    while pages_fetched < max_pages:
        next_url = _find_next_page_url(last_raw_html, current_url)
        if next_url is None:
            break

        # Avoid infinite loops: don't re-fetch the same URL.
        # Normalize by stripping hash fragments so "?page=5" and
        # "?page=5#" are treated as identical.
        next_clean = next_url.split("#", 1)[0]
        current_clean = current_url.split("#", 1)[0]
        if next_clean == current_clean:
            break

        if logger:
            logger.log(f"  · unfurling page {pages_fetched + 1}: {next_url}")

        # Fetch the next page
        next_html = await fetcher(next_url)

        if not next_html:
            if logger:
                logger.log(f"  · failed to fetch page {pages_fetched + 1}, stopping")
            break

        # Extract the article body from the next page using trafilatura
        # to avoid duplicating header/footer/navigation content
        next_body = extract(
            next_html,
            url=next_url,
            output_format="html",
            include_comments=False,
            include_formatting=True,
            include_images=True,
            include_tables=True,
            favor_precision=True,
            config=TRAFILATURA_CONFIG,
        )

        if next_body:
            # Append the next page's body to the merged document
            try:
                tree = lxml_html.fromstring(merged_html)
                body = tree.xpath("//body")
                if body:
                    body_el = body[0]
                    wrapper = (
                        f'<div class="unfurled-page" '
                        f'data-page="{pages_fetched + 1}">{next_body}</div>'
                    )
                    fragment = lxml_html.fromstring(wrapper)
                    if isinstance(fragment, list):
                        for child in fragment:
                            body_el.append(child)
                    else:
                        body_el.append(fragment)
                merged_html = cast(str, lxml_html.tostring(tree, encoding="unicode"))
            except lxml_html.ParserError:
                # If parsing fails, just concatenate
                wrapper = (
                    f'<div class="unfurled-page" '
                    f'data-page="{pages_fetched + 1}">{next_body}</div></body>'
                )
                merged_html = merged_html.replace("</body>", wrapper)

        pages_fetched += 1
        current_url = next_url
        last_raw_html = next_html

    if pages_fetched > 1 and logger:
        logger.log(f"  · unfurled {pages_fetched} page(s) into single article")

    return merged_html


def clean_markdown_formatting(text: str) -> str:
    """Fixes markdown formatting issues to improve compatibility with Eleventy.

    Removes boilerplate bullets ("* Published", "**Recommended reading:**")
    and cleans up empty bold markers.  Spacing fixes around emphasis delimiters
    apply *only* when the delimiter is word-adjacent (real markdown emphasis),
    not when surrounded by spaces on both sides (e.g. "2 * 3 * 4").
    """
    if not text:
        return ""

    text = re.sub(
        r"^\s*[\*\-]\s*Published\s*\n", "\n", text, flags=re.MULTILINE | re.IGNORECASE
    )
    text = re.sub(
        r"\*\*Recommended reading:\*\*", "\n", text, flags=re.MULTILINE | re.IGNORECASE
    )

    # Fix spacing inside emphasis delimiters, but only when the opening *
    # is preceded by a non-space (or start of line) — this avoids touching
    # prose like "2 * 3 * 4" where the * is surrounded by spaces.
    #
    # Process ** (bold) and * (italic) separately to avoid the closing **
    # bleeding into the next match.  A negative lookbehind for * ensures we
    # don't start a new emphasis match right after a * that belongs to a
    # closing delimiter.

    def _fix_emphasis(m: re.Match[str]) -> str:
        delim = m.group(1)
        inner = m.group(2).strip()
        return f"{delim}{inner}{delim}"

    # --- Bold (** ... **) ---
    # Double-asterisk is unlikely in prose, so no lookbehind needed.
    # ** word **  =>  **word**   (leading space)
    text = re.sub(r"(?<!\*)(\*\*)\s+([^\*\n]+?)\s*\1", _fix_emphasis, text)
    # **word **   =>  **word**   (trailing space)
    text = re.sub(r"(?<!\*)(\*\*)([^\*\n]+?)\s+\1", _fix_emphasis, text)

    # **word**X   =>  **word** X (missing space after closing)
    def _add_space_after_bold(m: re.Match[str]) -> str:
        inner = m.group(1)
        trailing = m.group(2)
        return f"**{inner}** {trailing}"

    text = re.sub(
        r"(?<!\*)\*\*([^\*\n]+?)\*\*([a-zA-Z0-9])", _add_space_after_bold, text
    )

    # --- Italic (* ... *) ---
    # * word *  =>  *word*   (leading space)
    text = re.sub(r"(?<!\*)(?<=\S)(\*)\s+([^\*\n]+?)\s*\1", _fix_emphasis, text)
    # *word *   =>  *word*   (trailing space)
    text = re.sub(r"(?<!\*)(?<=\S)(\*)([^\*\n]+?)\s+\1", _fix_emphasis, text)

    # *word*X   =>  *word* X (missing space after closing)
    def _add_space_after_italic(m: re.Match[str]) -> str:
        inner = m.group(1)
        trailing = m.group(2)
        return f"*{inner}* {trailing}"

    text = re.sub(
        r"(?<!\*)(?<=\S)\*([^\*\n]+?)\*([a-zA-Z0-9])", _add_space_after_italic, text
    )

    text = re.sub(r"\*\*\s*\*\*", "", text)

    return text.strip()


def normalize_inline_spacing(extracted_html: str) -> str:
    """Move boundary whitespace outside inline formatting elements."""
    tree = lxml_html.fromstring(extracted_html)
    inline_elements = tree.xpath(".//em | .//strong | .//b | .//i")

    for element in inline_elements:
        if not element.text:
            continue

        leading = re.match(r"[ \t]+", element.text)
        if leading:
            whitespace = leading.group(0)
            element.text = element.text[len(whitespace) :]
            previous = element.getprevious()
            if previous is not None:
                previous.tail = (previous.tail or "") + whitespace
            else:
                parent = element.getparent()
                parent.text = (parent.text or "") + whitespace

        trailing = re.search(r"[ \t]+$", element.text)
        if trailing:
            whitespace = trailing.group(0)
            element.text = element.text[: -len(whitespace)]
            element.tail = whitespace + (element.tail or "")

    return cast(str, lxml_html.tostring(tree, encoding="unicode"))


def linkify_text(text: str) -> str:
    """Linkify bare URLs and emails in text, preserving existing markdown.

    Skips URLs inside inline code spans (backticks) and strips trailing
    punctuation (.,;:!?) from captured URLs so that prose like
    "see https://example.com/a." doesn't swallow the full stop.
    """
    if not text:
        return ""

    # First, protect inline code spans by replacing them with placeholders.
    _CODE_PLACEHOLDER_PREFIX = "\x00CODE\x00"
    code_spans: list[str] = []

    def _save_code_span(m: re.Match[str]) -> str:
        code_spans.append(m.group(0))
        return f"{_CODE_PLACEHOLDER_PREFIX}{len(code_spans) - 1}\x00"

    text = re.sub(r"`+[^`]+`+", _save_code_span, text)

    pattern = (
        r"(!\[.*?\]\(https?://[^\s\)]+\))"
        r"|(\[.*?\]\(https?://[^\s\)]+\))"
        r"|(https?://[^\s\)]+)"
        r"|([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    )
    excluded_imgs = ["placeholder image", "google preferred source"]

    def replace(match: re.Match[str]) -> str:
        img, link, url, email = match.groups()
        if img:
            for excluded in excluded_imgs:
                if excluded.lower() in img.lower():
                    return ""
            return img
        if link:
            return link
        if url:
            # Strip trailing punctuation that's likely prose, not part of URL,
            # but preserve it after the link.  Note: '?' is excluded because
            # it usually starts a query string, not ends prose.
            trailing = url[len(url.rstrip(".,;:!")) :]
            url = url[: len(url) - len(trailing)]
            return f"[{url}]({url}){trailing}"
        if email:
            return f"[{email}](mailto:{email})"
        return match.group(0)

    text = re.sub(pattern, replace, text)

    # Restore code spans
    for i, span in enumerate(code_spans):
        text = text.replace(f"{_CODE_PLACEHOLDER_PREFIX}{i}\x00", span)

    return text


def extract_first_image_from_markdown(md: str) -> str | None:
    """Finds the first image in Markdown text: ![alt](url)."""
    match = re.search(r"!\[.*?\]\((https?://[^\s\)]+)\)", md)
    if match:
        return match.group(1)
    return None


def html_to_markdown(extracted_html: str) -> str:
    """Convert extracted HTML to clean markdown."""
    md_body = to_markdown(extracted_html, heading_style="ATX")
    md_body = clean_markdown_formatting(md_body)
    md_body = linkify_text(md_body)
    return md_body


# ---------------------------------------------------------------------------
# Srcset resolution
# ---------------------------------------------------------------------------

_SRCSET_DELIMITER_PATTERN = re.compile(r"\s+")


def parse_srcset(srcset: str) -> list[tuple[str, int | None]]:
    """Parse a ``srcset`` attribute value into ``(url, width)`` pairs.

    Each entry may be ``"url"``, ``"url 575w"`` (width descriptor), or
    ``"url 2x"`` (pixel-density descriptor).  Only width descriptors are
    returned as ``int``; ``None`` means the entry had no width descriptor.

    Handles URLs that contain commas in query parameters (e.g.
    ``?crop=3:2,smart`` or ``?trim=0,0,0,0``) by tokenizing on commas that
    are followed by whitespace (indicating an entry boundary), rather than
    naively splitting on every comma.

    >>> parse_srcset(
    ...     "https://example.com/large.jpg 1400w, https://example.com/small.jpg 575w"
    ... )
    [('https://example.com/large.jpg', 1400), ('https://example.com/small.jpg', 575)]
    >>> parse_srcset("https://example.com/img.jpg 2x, https://example.com/img.jpg")
    [('https://example.com/img.jpg', None), ('https://example.com/img.jpg', None)]
    >>> parse_srcset("https://example.com/a.jpg, https://example.com/b.jpg")
    [('https://example.com/a.jpg', None), ('https://example.com/b.jpg', None)]
    >>> parse_srcset("https://ex.com/i.jpg?c=a,b 320w, https://ex.com/i.jpg?c=a,b 640w")
    [('https://ex.com/i.jpg?c=a,b', 320), ('https://ex.com/i.jpg?c=a,b', 640)]
    >>> parse_srcset(
    ...     "https://ex.com/i.jpeg?t=0,0,0,0 320w, https://ex.com/i.jpeg?t=0,0,0,0 640w"
    ... )
    [('https://ex.com/i.jpeg?t=0,0,0,0', 320), ('https://ex.com/i.jpeg?t=0,0,0,0', 640)]
    """
    # Tokenize: split on commas followed by whitespace (entry boundary),
    # rather than naively splitting on every comma. This correctly handles
    # URLs that contain commas in query parameters (e.g. ``?crop=3:2,smart``
    # or ``?trim=0,0,0,0``) because those commas are not followed by
    # whitespace, while actual srcset entry separators always have
    # whitespace after the comma.
    parts = re.split(r",\s+", srcset.strip())

    entries: list[tuple[str, int | None]] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Try to find a trailing descriptor (width "w" or density "x")
        # The descriptor is preceded by whitespace and is at the end.
        tokens = _SRCSET_DELIMITER_PATTERN.split(part)
        url = tokens[0]
        width: int | None = None
        for token in tokens[1:]:
            if token.endswith("w"):
                try:
                    width = int(token[:-1])
                    break
                except ValueError:
                    continue
        entries.append((url, width))
    return entries


def pick_largest_srcset_url(srcset: str) -> str | None:
    """Return the URL of the largest image described by *srcset*.

    Selection prefers entries with a ``w`` (width) descriptor and picks the
    one with the highest width.  Falls back to the first URL entry when no
    width descriptors are present.

    >>> pick_largest_srcset_url("a.jpg 575w, b.jpg 1400w, c.jpg 962w")
    'b.jpg'
    >>> pick_largest_srcset_url("a.jpg 2x, b.jpg")
    'a.jpg'
    """
    entries = parse_srcset(srcset)
    if not entries:
        return None

    best_url: str | None = None
    best_width = -1
    for url, width in entries:
        if width is not None and width >= best_width:
            best_width = width
            best_url = url
    if best_url is None:
        best_url = entries[0][0]
    return best_url


# Matches a path ending in a recognised image file extension
_IMAGE_EXT_PATTERN: re.Pattern[str] = re.compile(
    r"\.(avif|bmp|gif|hei[cf]|jpe?g|png|svg|webp|tiff?)$", re.IGNORECASE
)


def ensure_image_extension(url: str) -> str:
    """Ensure *url* has a recognisable image file extension.

    Trafilatura's ``is_image_file`` rejects URLs whose path does not end in
    an image extension (``.jpg``, ``.png``, …).  Some sites serve images
    via query-parameter URLs such as ``/img/123/?type=large`` which lack an
    extension and are silently dropped.  This helper inserts a ``.jpg``
    extension into the path when none is present.

    For CDN URLs with trailing dots (e.g. ``/img/123..``), this appends
    ``.jpg`` producing ``/img/123...jpg`` so that trafilatura accepts the
    URL.  Use :func:`restore_trailing_dot_images` after extraction to
    restore the original URLs.

    >>> ensure_image_extension("https://ex.com/img/123/?type=large")
    'https://ex.com/img/123.jpg?type=large'
    >>> ensure_image_extension("https://ex.com/img/photo.jpg")
    'https://ex.com/img/photo.jpg'
    >>> ensure_image_extension("https://ex.com/img/123..")
    'https://ex.com/img/123...jpg'
    """
    parsed = urlparse(url)
    path = parsed.path
    if _IMAGE_EXT_PATTERN.search(path):
        return url
    if path.endswith("/"):
        path = path[:-1] + ".jpg"
    else:
        path = path + ".jpg"
    return urlunparse(parsed._replace(path=path))


# Pattern to detect fake .jpg appended to trailing-dot CDN paths
# e.g. "2279298894...jpg" → should be "2279298894.."
_TRAILING_DOT_FAKE_JPG_PATTERN: re.Pattern[str] = re.compile(r"\.\.\.jpg")


def restore_trailing_dot_images(html: str) -> str:
    """Restore CDN image URLs where ``ensure_image_extension`` added fake ``.jpg``.

    Some CDNs (e.g. The Independent) serve images with trailing-dot paths
    like ``2279298894..``.  The :func:`ensure_image_extension` helper appends
    ``.jpg`` to these so that trafilatura accepts them, producing URLs like
    ``2279298894...jpg``.  This function reverses that transformation after
    trafilatura extraction, restoring the original CDN URLs.

    >>> restore_trailing_dot_images('<img src="https://cdn.com/123...jpg?w=640">')
    '<img src="https://cdn.com/123..?w=640">'
    >>> restore_trailing_dot_images('<img src="https://cdn.com/photo.jpg">')
    '<img src="https://cdn.com/photo.jpg">'
    """
    return _TRAILING_DOT_FAKE_JPG_PATTERN.sub("..", html)


def resolve_srcset_images(html: str, base_url: str = "", logger: Any = None) -> str:
    """Convert ``<img>`` tags that use ``srcset`` into a plain ``src``.

    Trafilatura strips ``srcset`` attributes, leaving behind empty ``<img>``
    tags with no source.  This preprocessing step picks the largest image
    from each ``srcset`` (by width descriptor) and promotes it to the
    ``src`` attribute so that trafilatura retains the image in its output.

    Relative URLs are resolved against *base_url* when provided.

    Args:
        html: The raw HTML string to preprocess.
        base_url: Base URL for resolving relative ``src`` values.
        logger: Optional logger for progress reporting.

    Returns:
        The preprocessed HTML string.
    """
    if not html or not html.strip():
        return html

    tree = lxml_html.fromstring(html)
    if isinstance(tree, list):
        tree = lxml_html.fragment_fromstring(
            lxml_html.tostring(tree, encoding="unicode"),
            create_parent="div",  # pyright: ignore[reportArgumentType,reportUnknownArgumentType]
        )

    processed = 0
    for img in tree.xpath("//img"):
        srcset = img.get("srcset")
        if not srcset:
            continue

        best_url = pick_largest_srcset_url(srcset)
        if best_url is None:
            continue

        if base_url:
            best_url = urljoin(base_url, best_url)

        best_url = ensure_image_extension(best_url)

        img.set("src", best_url)
        img.attrib.pop("srcset", None)
        img.attrib.pop("sizes", None)
        processed += 1

    if logger and processed:
        logger.log(f"  · resolved {processed} srcset image(s) to src")

    return cast(str, lxml_html.tostring(tree, encoding="unicode"))


# ---------------------------------------------------------------------------
# Exclusion handling
# ---------------------------------------------------------------------------

_EXCLUSION_ATTR_PATTERN: re.Pattern[str] = re.compile(
    r'^\s*([\w:-]+)\s*=\s*["\']([^"\']+)["\']\s*$'
)


def normalize_exclusion(expr: str) -> str:
    """Translate an ``exclusions`` entry into an XPath expression."""
    expr = expr.strip()
    if expr.startswith(("/", "//", "(", ".", "descendant")):
        return expr
    match = _EXCLUSION_ATTR_PATTERN.match(expr)
    if match:
        attr, value = match.group(1), match.group(2)
        return f"//*[@{attr}='{value}']"
    return expr


def remove_excluded_elements(
    html: str, exclusions: list[str], logger: Any = None
) -> str:
    """Detach every element matched by ``exclusions`` from ``html``."""
    if not exclusions:
        return html

    tree = lxml_html.fromstring(html)
    if isinstance(tree, list):
        tree = lxml_html.fragment_fromstring(
            lxml_html.tostring(tree, encoding="unicode"),
            create_parent="div",  # pyright: ignore[reportArgumentType,reportUnknownArgumentType]
        )

    removed = 0
    for expr in exclusions:
        xpath = normalize_exclusion(expr)
        for element in tree.xpath(xpath):
            parent = element.getparent()
            if parent is not None:
                parent.remove(element)
                removed += 1

    if logger and removed:
        logger.log(
            f"  · excluded {removed} element(s) via {len(exclusions)} exclusion rule(s)"
        )

    return cast(str, lxml_html.tostring(tree, encoding="unicode"))


def filter_duplicate_names(names: Iterable[str]) -> list[str]:
    """
    Remove single-word names (forename or surname fragments) that are
    already covered by a fuller (multi-word) name in the list.

    A single-word entry is dropped if it exactly matches one of the
    whitespace-separated parts of some other multi-word entry.
    Multi-word entries (including hyphenated ones like 'Stokes-McCullum',
    since they don't split on whitespace) are always kept.
    """
    full_names = [n for n in names if len(n.split()) > 1]
    fragment_pool = set()
    for full in full_names:
        fragment_pool.update(full.split())

    result = []
    for name in names:
        if len(name.split()) > 1:
            result.append(name)  # always keep full names
        elif name in fragment_pool:
            continue  # drop fragment covered by a fuller name
        else:
            result.append(name)  # keep standalone single-word names

    return result


# ---------------------------------------------------------------------------
# Trafilatura wrappers
#
# Trafilura's extractor/metadata calls are synchronous and CPU-bound, so the
# pipeline offloads them via ``asyncio.to_thread`` (see ``pipeline.py``). To
# make their cost visible in the ``@profiled`` exit-time report, we wrap them
# here in thin delegating functions and decorate those. The wrappers preserve
# the exact arguments/options previously passed at the call sites.
# ---------------------------------------------------------------------------


@profiled
def extract_article_html(
    html: str,
    *,
    url: str | None = None,
) -> str | None:
    """Profiled wrapper around :func:`trafilatura.extract`.

    Returns the extracted article HTML, or ``None`` if nothing was extracted.
    """
    return extract(
        html,
        url=url,
        output_format="html",
        include_comments=False,
        include_formatting=True,
        include_images=True,
        include_tables=True,
        favor_precision=True,
        config=TRAFILATURA_CONFIG,
    )


@profiled
def extract_article_metadata(
    html: str,
    *,
    url: str | None = None,
) -> Document | None:
    """Profiled wrapper around :func:`trafilatura.extract_metadata`."""
    return extract_metadata(html, default_url=url)
