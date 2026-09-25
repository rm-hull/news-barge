"""Article classification and categorization utilities."""

from __future__ import annotations

import re
from dataclasses import dataclass
from threading import Lock
from typing import cast

from flair.data import Sentence
from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter
from taxotag import Gist

from .constants import TAXOTAG_TOP_K

# ---------------------------------------------------------------------------
# Taxotag
# ---------------------------------------------------------------------------

# `Gist` and the Flair `Classifier` both eagerly load heavyweight models
# (TensorFlow Lite / PyTorch) inside their constructors. Constructing them at
# import time makes importing this module - and therefore spinning up the whole
# test suite - slow, so both are instantiated/loaded lazily on first use and
# cached as module-level singletons. Double-checked locking keeps the
# `Lock` only on the very first construction.

_gist: Gist | None = None
_gist_lock: Lock = Lock()


def _get_gist() -> Gist:
    """Return the cached taxotag Gist, constructing it on first call."""
    global _gist
    if _gist is None:  # fast path - already constructed
        with _gist_lock:
            if _gist is None:  # double-checked locking
                _gist = Gist()
    return _gist


_tagger: Classifier[Sentence] | None = None
_tagger_lock: Lock = Lock()
_splitter = SegtokSentenceSplitter()


def _get_tagger() -> Classifier[Sentence]:
    """Return the cached NER classifier, loading it on first call."""
    global _tagger
    if _tagger is None:  # fast path - already loaded
        with _tagger_lock:
            if _tagger is None:  # double-checked locking
                _tagger = Classifier.load("ner-fast")
    return _tagger


@dataclass
class NamedEntities:
    people: set[str]
    locations: set[str]
    organisations: set[str]


def article_categories(title: str, description: str) -> list[str]:
    """Classify an article using taxotag.

    Combines title and description for classification.
    """
    text = "\n\n".join(part.strip() for part in (title, description) if part.strip())
    if not text:
        return []

    # Resolve the Gist *before* locking: _get_gist() takes _gist_lock on first
    # construction, and `Lock` is not reentrant, so it must not be called
    # while we already hold it (would deadlock).
    gist = _get_gist()
    with _gist_lock:
        topics = gist.classify(text, top_k=TAXOTAG_TOP_K)
    return cast(list[str], [topic.name for topic in topics])


def strip_non_alnum(s: str) -> str:
    return re.sub(r"^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$", "", s)


def named_entities(text: str) -> NamedEntities:
    cleaned_lines = [line.strip() for line in text.split("\n") if line.strip()]
    cleaned_text = " ".join(cleaned_lines)

    sentences = _splitter.split(cleaned_text)
    _get_tagger().predict(sentences)

    entities = NamedEntities(set(), set(), set())

    for sentence in sentences:
        for label in sentence.get_labels():
            entity = strip_non_alnum(label.data_point.text)
            if label.value == "LOC":
                entities.locations.add(entity)
            if label.value == "PER":
                entities.people.add(entity)
            if label.value == "ORG":
                entities.organisations.add(entity)

    return entities
