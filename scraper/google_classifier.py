import json
import os
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from google import genai
from google.genai import types

REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = REPO_ROOT / "content"
PROMPT = """
Give me a JSON list of locations, people, organisations that are mentioned in the article. Example:

{"locations":[...],"people":[...],"organisations":[...]}
"""


class Categories(BaseModel):
    locations: List[str]
    people: List[str]
    organisations: List[str]


class Classifier:

    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model

        self.client = genai.Client(api_key=api_key)

    def analyze(self, text: str) -> Categories | None:
        response = self.client.interactions.create(
            model=self.model,
            input=PROMPT + "\n\n" + text,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": Categories.model_json_schema(),
            },
        )

        print(response.output_text)
        return Categories.model_validate_json(response.output_text.replace("`", ""))


if __name__ == "__main__":

    with open(
        CONTENT_DIR
        / "2026/09/21/bbc--news-articles-cx4gqv239043o-at-mediumrssat-campaignrss.md"
    ) as f:
        article = f.read()

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY", "")
    # model = "gemma-4-26b-a4b-it"
    model = "gemini-3.5-flash-lite"
    classifier = Classifier(api_key, model)
    result = classifier.analyze(article)

    print(result)
