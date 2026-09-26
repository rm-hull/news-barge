# News Barge

A clean mirror of news feeds designed to eliminate insidious tracking and adtech.
Pulls articles from RSS feeds or HTML lists, strips the noise, converts to Markdown,
and serves them as a static site without the baggage of the modern web.

Contributions are welcome! If there's a feed you'd like to see added, please [create a new issue](https://github.com/rm-hull/news-barge/issues/new) or use the [scrape-analyzer skill](.agents/skills/scrape-analyzer/SKILL.md) to submit a pull request.

## Repository layout

```
sites.yaml               ← Edit this to add/remove sites
scraper/                 ← Python scraper package (uv-managed)
  pyproject.toml         ← Project config, entry point, deps
  uv.lock
  pyrightconfig.json
  .python-version
  .editorconfig
  .env                    ← Local-only secrets (gitignored)
  src/
    __init__.py
    scrape.py            ← Main CLI entry point (console script: scrape)
    pipeline.py          ← Per-article processing pipeline
    classifiers.py       ← Article categorisation & NER (taxotag + flair)
    constants.py         ← Paths, headers, defaults
    dates.py             ← Date / retention-window helpers
    fetchers.py          ← aiohttp + Playwright HTML fetchers
    log_helper.py        ← Colour + GitHub Actions logging
    output.py            ← Output file-path computation
    slugs.py             ← URL → filesystem-safe slug helpers
    text_extraction.py   ← HTML cleaning, markdown conversion, exclusions
  tests/                 ← pytest suite (unit + integration)
  backfill_entities.py   ← Backfill NER entities on existing articles
  flair_classifier.py    ← Flair NER backfill script
  litert_classifier.py   ← LiteRT classifier backfill script
  google_classifier.py   ← Google GenAI classifier backfill script
  spacy_classifier.py    ← spaCy classifier backfill script
  rename_slugs.py        ← Recompute / rename article slugs

content/                 ← Generated markdown (committed by the Action)
  YYYY/MM/DD/
    <site-slug>--<article-slug>.md
site/                    ← 11ty static site
  eleventy.config.js
  index.njk              ← Latest articles
  archive.njk            ← Archive index
  search.njk             ← Pagefind search
  sites.njk              ← Site index
  categories.njk
  _data/site.json
  _includes/
  _layouts/
  _site/                  ← Built output
  public/css/style.css    ← Styles
  public/js/
  package.json
.github/workflows/
  scrape.yml             ← Cron job: scrape, commit, Pages deploy
  build.yml              ← CI: lint, type-check, test on PRs/pushes
  archive.yml            ← Cron job: prune articles older than retention window
```

## Setup

### 1. Enable GitHub Pages

In your repo → **Settings → Pages**:
- Source: **GitHub Actions**

### 2. Give the Action write access

**Settings → Actions → General → Workflow permissions**: set to
**Read and write permissions**.

### 3. Add your sites

Edit `sites.yaml`. Each entry can have a `feed` (RSS/Atom URL) or `listing_urls` (one or more HTML pages to scrape):

```yaml
sites:
  - name: The Guardian
    slug: guardian
    feed: https://www.theguardian.com/world/rss
    limit: 5

  - name: Some HTML-only site
    slug: example
    listing_urls:
      - https://example.com/news
    listing_class: article-link
    limit: 10
    force_playwright: true   # use a real browser for JS-heavy sites
```

#### Adding a custom extraction rule for noisy sites

Some sites inject modals, paywalled overlays, or author bios into the article
HTML that trafilatura can mistake for body content. Add an `exclusions` list
to the site's entry in `sites.yaml` — each entry is either a bare
`attr="value"` matcher or a full XPath expression. Matched elements are
detached from the HTML **before** trafilatura runs:

```yaml
sites:
  - name: Some News Site
    slug: example
    feed: https://example.com/rss
    exclusions:
      - role="dialog"                        # bare attr form
      - //div[contains(@class, "paywall")]   # full XPath
      - //p[contains(., "Follow on Google")] # text-based XPath
```

### 4. Commit and push

The Action runs every 4 hours. You can also trigger it manually
from the **Actions** tab, optionally targeting a single site slug.

## Running locally

Ensure [uv](https://github.com/astral-sh/uv) is installed.

```bash
# Scrape
cd scraper
uv sync
# Ensure playwright browser is installed/updated
uv run playwright install chromium

uv run scrape --dry-run       # preview only
uv run scrape                  # write to ../content/

# Build and preview the site
cd ../site
npm install
npm start    # http://localhost:8080
```

### Type checking, linting, and testing

The scraper is fully typed and linted using
[`mypy`](https://mypy.readthedocs.io/) and [`ruff`](https://docs.astral.sh/ruff/).
Tests are written with [`pytest`](https://docs.pytest.org/). Install dev
dependencies and run:

```bash
uv sync --group dev
uv run ruff check src/ tests/            # lint
uv run ruff format --check src/ tests/   # format check
uv run mypy src/ tests/                  # type check
uv run pytest tests/                     # run tests with coverage
```

The CI workflow (`.github/workflows/build.yml`) runs all checks on every
push and pull request affecting files under `scraper/`.

### Search

Pagefind runs automatically as part of `npm run build`. It indexes all
rendered HTML and ships a WASM bundle. No external service needed.

## Privacy

This site uses anonymous [Umami analytics](https://umami.is/) to understand usage patterns without compromising visitor privacy. No personal data is collected.
