import argparse
import json
import os
from pathlib import Path
from typing import List, Optional
import litert_lm
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from google import genai
from google.genai import types
from regex import T
import yaml
from tqdm import tqdm


class Categories(BaseModel):
    locations: Optional[List[str]]
    people: Optional[List[str]]
    organisations: Optional[List[str]]


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = REPO_ROOT / "content"

PROMPT = """
Extract geographical locations (include city, state, country), people, and organisations mentioned in the article.
Respond with ONLY raw JSON (no markdown, no code fences, no commentary) matching this example: {"locations":["UK","London"],"people":["Ben Smith"],"organisations":["Microsoft"]}
"""


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
    litert_lm.set_min_log_severity(litert_lm.LogSeverity.ERROR)  # Hide log for TUI app

    parser = argparse.ArgumentParser(
        description="Backfill piitag entities in article Markdown"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="write changes; without this flag, only report them",
    )
    args = parser.parse_args()

    # model = "/Users/rhu/.litert-lm/cache/huggingface/litert-community/gemma-4-E4B-it-litert-lm/gemma-4-E4B-it.litertlm"
    model = "/Users/rhu/.litert-lm/cache/huggingface/litert-community/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm"
    # model = "/Users/rhu/.litert-lm/cache/huggingface/litert-community/Qwen3-0.6B/Qwen3-0.6B.litertlm"

    with litert_lm.Engine(
        model,
        backend=litert_lm.Backend.GPU(),
        enable_speculative_decoding=True,
    ) as engine:
        changed = 0
        skipped = 0

        messages = [litert_lm.Message.system(PROMPT)]
        thinking_config = litert_lm.ThinkingConfig(
            enable_thinking=False, thinking_token_budget=0
        )

        result = ""
        for path in tqdm(sorted(CONTENT_DIR.rglob("*.md"))):
            try:
                frontmatter, body = parse_article(path)

                with engine.create_conversation(
                    messages=messages, thinking_config=thinking_config
                ) as conversation:
                    response = conversation.send_message(body)
                    result = response["content"][0]["text"]
                    categories = Categories.model_validate_json(result)

            except (OSError, ValueError, KeyError, TypeError) as error:
                skipped += 1
                print(f"SKIP {path.relative_to(REPO_ROOT)}: {error}\n{result}")
                continue

            frontmatter["locations"] = categories.locations
            frontmatter["people"] = categories.people
            frontmatter["organisations"] = categories.organisations

            changed += 1
            # action = "WRITE" if args.write else "WOULD WRITE"
            # print(f"{action} {path.relative_to(REPO_ROOT)}: {categories}")
            if args.write:
                path.write_text(render_article(frontmatter, body), encoding="utf-8")

            if changed > 50:
                break

        mode = "updated" if args.write else "would update"
        print(f"Done: {mode} {changed} article(s); skipped {skipped}.")
