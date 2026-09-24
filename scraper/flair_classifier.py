import argparse
from pathlib import Path

from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter

import yaml
from tqdm import tqdm


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = REPO_ROOT / "content"


def parse_article(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    frontmatter = yaml.safe_load(text[4:end]) or {}
    body = text[end + len("\n---\n") :]
    if not isinstance(frontmatter, dict):
        raise ValueError("frontmatter is not a mapping")
    return frontmatter, body


def render_article(frontmatter: dict, body: str) -> str:
    rendered = yaml.dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return "---\n" + rendered + "---\n" + body


def filter_duplicate_names(names):
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


if __name__ == "__main__":
    tagger = Classifier.load("ner-fast")
    splitter = SegtokSentenceSplitter()

    parser = argparse.ArgumentParser(
        description="Backfill spacy entities in article Markdown"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="write changes; without this flag, only report them",
    )
    args = parser.parse_args()

    changed = 0
    skipped = 0

    result = ""
    for path in tqdm(sorted(CONTENT_DIR.rglob("*.md"))):
        try:
            frontmatter, body = parse_article(path)
            if (
                "locations" in frontmatter
                or "people" in frontmatter
                or "orgs" in frontmatter
            ):
                skipped += 1
                # print(f"SKIP {path.relative_to(REPO_ROOT)}: already processed")
                continue

            cleaned_lines = [line.strip() for line in body.split("\n") if line.strip()]
            cleaned_text = " ".join(cleaned_lines)

            sentences = splitter.split(cleaned_text)
            tagger.predict(sentences)

        except (OSError, ValueError, KeyError, TypeError) as error:
            skipped += 1
            print(f"SKIP {path.relative_to(REPO_ROOT)}: {error}\n{result}")
            continue

        orgs = []
        locations = []
        people = []

        for sentence in sentences:
            for label in sentence.get_labels():
                if label.value == "LOC" and label.data_point.text not in locations:
                    locations.append(label.data_point.text)
                if label.value == "PER" and label.data_point.text not in people:
                    people.append(label.data_point.text)
                if label.value == "ORG" and label.data_point.text not in orgs:
                    orgs.append(label.data_point.text)

        frontmatter["locations"] = sorted(filter_duplicate_names(locations))
        frontmatter["people"] = sorted(filter_duplicate_names(people))
        frontmatter["organisations"] = sorted(filter_duplicate_names(orgs))

        changed += 1
        # action = "WRITE" if args.write else "WOULD WRITE"
        # print(f"{action} {path.relative_to(REPO_ROOT)}: locations={locations} people={people} orgs={orgs}")
        if args.write:
            path.write_text(render_article(frontmatter, body), encoding="utf-8")

    mode = "updated" if args.write else "would update"
    print(f"Done: {mode} {changed} article(s); skipped {skipped}.")
