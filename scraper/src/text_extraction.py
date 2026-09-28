"""Content extraction and text processing utilities."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Any, cast
from urllib.parse import urljoin, urlparse, urlunparse

from lxml import html as lxml_html
from markdownify import markdownify as to_markdown


def clean_markdown_formatting(text: str) -> str:
    """Fixes markdown formatting issues to improve compatibility with Eleventy."""
    if not text:
        return ""

    text = re.sub(
        r"^\s*[\*\-]\s*Published\s*\n", "\n", text, flags=re.MULTILINE | re.IGNORECASE
    )
    text = re.sub(
        r"\*\*Recommended reading:\*\*", "\n", text, flags=re.MULTILINE | re.IGNORECASE
    )

    text = re.sub(r"(\*\*|\*)[ \t]+([^*\n]+?)[ \t]*\1", r"\1\2\1", text)
    text = re.sub(r"(\*\*|\*)([^*\n]+?)[ \t]+\1", r"\1\2\1", text)
    text = re.sub(r"(\*\*|\*)([^\*\n]+?)\1([a-zA-Z0-9])", r"\1\2\1 \3", text)
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
    """Linkify bare URLs and emails in text, preserving existing markdown."""
    if not text:
        return ""

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
            return f"[{url}]({url})"
        if email:
            return f"[{email}](mailto:{email})"
        return match.group(0)

    return re.sub(pattern, replace, text)


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

    >>> parse_srcset(
    ...     "https://example.com/large.jpg 1400w, https://example.com/small.jpg 575w"
    ... )
    [('https://example.com/large.jpg', 1400), ('https://example.com/small.jpg', 575)]
    >>> parse_srcset(
    ...     "https://example.com/img.jpg 2x, https://example.com/img.jpg"
    ... )
    [('https://example.com/img.jpg', None), ('https://example.com/img.jpg', None)]
    """
    entries: list[tuple[str, int | None]] = []
    for part in srcset.split(","):
        part = part.strip()
        if not part:
            continue
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
            # Pixel-density descriptors (e.g. "2x") are not widths - skip.
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

    >>> ensure_image_extension("https://ex.com/img/123/?type=large")
    'https://ex.com/img/123.jpg?type=large'
    >>> ensure_image_extension("https://ex.com/img/photo.jpg")
    'https://ex.com/img/photo.jpg'
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


def resolve_srcset_images(
    html: str, base_url: str = "", logger: Any = None
) -> str:
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
