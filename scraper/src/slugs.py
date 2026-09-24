"""URL and slug utilities."""

from __future__ import annotations

import hashlib
import re
from urllib.parse import parse_qsl, urlencode, urlparse


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
