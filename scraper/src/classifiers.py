"""Article classification and categorization utilities."""

from __future__ import annotations

from threading import Lock
from typing import cast

from taxotag import Gist

from .constants import TAXOTAG_TOP_K

# ---------------------------------------------------------------------------
# Taxotag
# ---------------------------------------------------------------------------

_gist: Gist = Gist()
_lock: Lock = Lock()


def article_categories(title: str, description: str) -> list[str]:
    """Classify an article using taxotag.

    Combines title and description for classification.
    """
    text = "\n\n".join(part.strip() for part in (title, description) if part.strip())
    if not text:
        return []

    with _lock:
        topics = _gist.classify(text, top_k=TAXOTAG_TOP_K)
    return cast(list[str], [topic.name for topic in topics])
