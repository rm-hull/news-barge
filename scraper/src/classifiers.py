"""Article classification and categorization utilities."""

from __future__ import annotations

import re
from dataclasses import dataclass
from threading import Lock
from typing import cast

from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter
from taxotag import Gist

from .constants import TAXOTAG_TOP_K

# ---------------------------------------------------------------------------
# Taxotag
# ---------------------------------------------------------------------------

_gist: Gist = Gist()
_lock: Lock = Lock()

_tagger = Classifier.load("ner-fast")
_splitter = SegtokSentenceSplitter()


@dataclass
class NamedEntities:
    people: list[str]
    locations: list[str]
    organisations: list[str]


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


def strip_non_alnum(s: str) -> str:
    return re.sub(r"^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$", "", s)


def named_entities(text: str) -> NamedEntities:
    cleaned_lines = [line.strip() for line in text.split("\n") if line.strip()]
    cleaned_text = " ".join(cleaned_lines)

    sentences = _splitter.split(cleaned_text)
    _tagger.predict(sentences)

    entities = NamedEntities([], [], [])

    for sentence in sentences:
        for label in sentence.get_labels():
            if label.value == "LOC" and label.data_point.text not in entities.locations:
                entities.locations.append(strip_non_alnum(label.data_point.text))
            if label.value == "PER" and label.data_point.text not in entities.people:
                entities.people.append(strip_non_alnum(label.data_point.text))
            if (
                label.value == "ORG"
                and label.data_point.text not in entities.organisations
            ):
                entities.organisations.append(strip_non_alnum(label.data_point.text))

    return entities
