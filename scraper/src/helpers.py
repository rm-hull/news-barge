"""
Utility functions for the scraper.
"""

from __future__ import annotations

import hashlib
import re
from datetime import datetime
from pathlib import Path
from typing import Any, cast
from urllib.parse import parse_qsl, urlencode, urlparse

from lxml import html as lxml_html
from markdownify import markdownify as to_markdown

from .constants import REPO_ROOT

# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def url_to_slug(url: str, exclude_query_params: bool = False) -> str:
    """Convert a URL to a filesystem-safe slug."""
    parsed = urlparse(url)

    path = parsed.path.strip("/").replace("/", "--")

    # When the site requests it, skip query params entirely in the slug.
    if exclude_query_params:
        short = slugify(path) or hashlib.sha1(url.encode()).hexdigest()[:10]
        return short

    # Filter out utm_* query params
    query_params = parse_qsl(parsed.query)
    filtered_query_params = [
        (k, v) for k, v in query_params if not k.startswith("utm_")
    ]
    filtered_query = urlencode(filtered_query_params)

    if filtered_query:
        query_slug = slugify(filtered_query).replace("=", "--").replace("&", "--")
        path = f"{path}--{query_slug}"

    short = slugify(path) or hashlib.sha1(url.encode()).hexdigest()[:10]
    return short


# ---------------------------------------------------------------------------
# Image extraction
# ---------------------------------------------------------------------------


def extract_first_image_from_markdown(md: str) -> str | None:
    """Finds the first image in Markdown text: ![alt](url)."""
    match = re.search(r"!\[.*?\]\((https?://[^\s\)]+)\)", md)
    if match:
        return match.group(1)
    return None


# ---------------------------------------------------------------------------
# Markdown formatting
# ---------------------------------------------------------------------------


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


def html_to_markdown(extracted_html: str) -> str:
    """Convert extracted HTML to clean markdown."""
    md_body = to_markdown(extracted_html, heading_style="ATX")
    md_body = clean_markdown_formatting(md_body)
    md_body = linkify_text(md_body)
    return md_body


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


# ---------------------------------------------------------------------------
# Output path
# ---------------------------------------------------------------------------


def output_path(
    site_slug: str,
    article_slug: str,
    date: datetime,
    output_dir: Path = REPO_ROOT / "content",
) -> Path:
    """Compute the output file path for an article."""
    date_path = date.strftime("%Y/%m/%d")
    filename = f"{site_slug}--{article_slug}.md"
    return output_dir / date_path / filename
