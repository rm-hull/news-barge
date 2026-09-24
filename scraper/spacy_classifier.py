import argparse
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from regex import T
import spacy
import en_core_web_trf
import yaml
from tqdm import tqdm


class Categories(BaseModel):
    locations: Optional[List[str]]
    people: Optional[List[str]]
    organisations: Optional[List[str]]


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


if __name__ == "__main__":

    # nlp = spacy.load("en_core_web_lg")

    nlp = spacy.load("en_core_web_trf")
    nlp = en_core_web_trf.load()

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
    for path in tqdm(sorted(CONTENT_DIR.rglob("harrogate*.md"))):
        try:
            frontmatter, body = parse_article(path)

            doc = nlp(body)

            locations, people, orgs = [], [], []
            for ent in doc.ents:
                if ent.label_ in ("GPE", "LOC"):
                    locations.append(ent.text)
                elif ent.label_ == "PERSON":
                    people.append(ent.text)
                elif ent.label_ == "ORG":
                    orgs.append(ent.text)


        except (OSError, ValueError, KeyError, TypeError) as error:
            skipped += 1
            print(f"SKIP {path.relative_to(REPO_ROOT)}: {error}\n{result}")
            continue

        frontmatter["locations"] = list(set(locations))
        frontmatter["people"] = list(set(people))
        frontmatter["organisations"] = list(set(orgs))

        changed += 1
        # action = "WRITE" if args.write else "WOULD WRITE"
        # print(f"{action} {path.relative_to(REPO_ROOT)}: locations={locations} people={people} orgs={orgs}")
        if args.write:
            path.write_text(render_article(frontmatter, body), encoding="utf-8")

    mode = "updated" if args.write else "would update"
    print(f"Done: {mode} {changed} article(s); skipped {skipped}.")
