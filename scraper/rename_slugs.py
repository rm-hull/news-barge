"""
rename_slugs.py — Recompute article slugs for sites that use
``exclude_query_params: true`` in sites.yaml.

For every content file belonging to such a site, the slug is re-derived from
the ``source_url`` stored in the file's YAML frontmatter using the *new*
``url_to_slug`` logic (which omits query params entirely).  The file is then
renamed so the permalink changes from, e.g.::

    bbc - -news - articles - crk3xd8j3k5o - at - mediumrssat - campaignrss.md

to::

    bbc - -news - articles - crk3xd8j3k5o.md

Only the *filename* changes; the frontmatter ``source_url`` is already correct
and is left untouched.
"""

import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, urlencode, parse_qsl

import yaml

# ---------------------------------------------------------------------------
# Reuse the same slug / url-to-slug logic as the scraper so results match.
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = REPO_ROOT / "content"
SITES_FILE = REPO_ROOT / "sites.yaml"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def url_to_slug(url: str, exclude_query_params: bool = False) -> str:
    parsed = urlparse(url)

    path = parsed.path.strip("/").replace("/", "--")

    if not exclude_query_params:
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


def load_sites() -> dict[str, dict]:
    """Return a dict mapping site slug -> site config dict."""
    with open(SITES_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {s["slug"]: s for s in data.get("sites", [])}


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Split a Markdown file into (frontmatter_dict, body)."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_yaml, body = match.groups()
    fm = yaml.safe_load(fm_yaml) or {}
    return fm, body


def main() -> None:
    sites = load_sites()
    # Only process files for sites that have exclude_query_params: true
    target_slugs = {
        slug for slug, cfg in sites.items() if cfg.get("exclude_query_params", False)
    }

    if not target_slugs:
        print("No sites with exclude_query_params: true found — nothing to do.")
        return

    print(f"Sites with exclude_query_params: {sorted(target_slugs)}")

    renamed = 0
    skipped = 0
    collisions = 0

    for md_file in CONTENT_DIR.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        frontmatter, _body = extract_frontmatter(text)

        source_slug = frontmatter.get("source_slug")
        source_url = frontmatter.get("source_url")
        if not source_slug or not source_url:
            continue

        if source_slug not in target_slugs:
            continue

        new_article_slug = url_to_slug(source_url, exclude_query_params=True)
        new_filename = f"{source_slug}--{new_article_slug}.md"
        old_path = md_file
        new_path = old_path.with_name(new_filename)

        if old_path.name == new_filename:
            skipped += 1
            continue

        # Check for collisions — if the target already exists and is a different file,
        # we need to be careful. We'll report it but not overwrite.
        if new_path.exists() and new_path != old_path:
            collisions += 1
            print(
                f"  ⚠ COLLISION: {old_path.name} -> {new_filename} "
                f"(target already exists, skipping)"
            )
            continue

        old_path.rename(new_path)
        rel_old = old_path.relative_to(REPO_ROOT)
        rel_new = new_path.relative_to(REPO_ROOT)
        print(f"  ✓ {rel_old.name}  →  {rel_new.name}")
        renamed += 1

    print(
        f"\nDone. Renamed: {renamed}, Already correct: {skipped}, "
        f"Collisions: {collisions}"
    )


if __name__ == "__main__":
    main()
