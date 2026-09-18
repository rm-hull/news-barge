"""Backfill article categories using the scraper's category logic."""

import argparse
from pathlib import Path
from threading import Lock

import yaml
from taxotag import Gist

REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = REPO_ROOT / "content"
SITES_FILE = REPO_ROOT / "sites.yaml"
TAXOTAG_TOP_K = 3

taxotag = Gist()
taxotag_lock = Lock()


def classify_article(title: str, description: str) -> list[str]:
    text = "\n\n".join(
        part.strip()
        for part in (title, description)
        if isinstance(part, str) and part.strip()
    )
    if not text:
        return []

    with taxotag_lock:
        topics = taxotag.classify(text, top_k=TAXOTAG_TOP_K)
    return [topic.name for topic in topics]


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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Backfill taxotag categories in article Markdown"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="write changes; without this flag, only report them",
    )
    args = parser.parse_args()

    with SITES_FILE.open(encoding="utf-8") as file:
        sites = yaml.safe_load(file).get("sites", [])
    site_categories = {
        site["slug"]: site.get("categories") or [] for site in sites if site.get("slug")
    }

    changed = 0
    skipped = 0
    for path in sorted(CONTENT_DIR.rglob("*.md")):
        try:
            frontmatter, body = parse_article(path)
            source_slug = frontmatter.get("source_slug")
            title = frontmatter.get("title") or ""
            description = frontmatter.get("description") or ""
            generated_categories = classify_article(title, description)
            categories = list(
                dict.fromkeys(
                    site_categories.get(source_slug, []) + generated_categories
                )
            )
        except (OSError, ValueError, KeyError, TypeError) as error:
            skipped += 1
            print(f"SKIP {path.relative_to(REPO_ROOT)}: {error}")
            continue

        if frontmatter.get("categories") == categories:
            continue

        frontmatter["categories"] = categories
        changed += 1
        action = "WRITE" if args.write else "WOULD WRITE"
        print(f"{action} {path.relative_to(REPO_ROOT)}: {categories}")
        if args.write:
            path.write_text(render_article(frontmatter, body), encoding="utf-8")

    mode = "updated" if args.write else "would update"
    print(f"Done: {mode} {changed} article(s); skipped {skipped}.")


if __name__ == "__main__":
    main()
