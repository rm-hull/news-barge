"""Backfill article categories using the scraper's classification logic."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml

from .classifiers import article_categories
from .constants import CONTENT_DIR, SITES_FILE
from .log_helper import report_error


def parse_article(path: Path) -> tuple[dict[str, Any], str]:
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


def render_article(frontmatter: dict[str, Any], body: str) -> str:
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

    sites = yaml.safe_load(SITES_FILE.read_text(encoding="utf-8")).get("sites", [])
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
            generated_categories = article_categories(title, description)
            categories = list(
                dict.fromkeys(
                    site_categories.get(source_slug, []) + generated_categories
                )
            )
        except (OSError, ValueError, KeyError, TypeError) as error:
            skipped += 1
            report_error(f"SKIP {path.relative_to(CONTENT_DIR.parent.parent)}: {error}")
            continue

        if frontmatter.get("categories") == categories:
            continue

        frontmatter["categories"] = categories
        changed += 1
        action = "WRITE" if args.write else "WOULD WRITE"
        print(f"{action} {path.relative_to(CONTENT_DIR.parent.parent)}: {categories}")
        if args.write:
            path.write_text(render_article(frontmatter, body), encoding="utf-8")

    mode = "updated" if args.write else "would update"
    print(f"Done: {mode} {changed} article(s); skipped {skipped}.")


if __name__ == "__main__":
    main()
