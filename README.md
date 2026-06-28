# News Barge

A clean mirror of news feeds designed to eliminate insidious tracking and adtech.
Pulls articles from RSS feeds or HTML lists, strips the noise, converts to Markdown,
and serves them as a static site without the baggage of the modern web.

Contributions are welcome! If there's a feed you'd like to see added, please [create a new issue](https://github.com/rm-hull/news-barge/issues/new) or use the [scrape-analyzer skill](.agents/skills/scrape-analyzer/SKILL.md) to submit a pull request.

## Repository layout

```
sites.yaml               ← Edit this to add/remove sites
scraper/
scraper/
  scrape.py              ← Python scraper (uv-managed, no separate requirements.txt)

content/                 ← Generated markdown (committed by the Action)
  2025/06/27/
    guardian--article-slug.md
site/                    ← 11ty site
  eleventy.config.js
  index.njk              ← Latest articles
  search.njk             ← Pagefind search
  sites.njk              ← Site index
  public/css/style.css
.github/workflows/
  scrape.yml             ← Cron job + Pages deploy
```

## Setup

### 1. Enable GitHub Pages

In your repo → **Settings → Pages**:
- Source: **GitHub Actions**

### 2. Give the Action write access

**Settings → Actions → General → Workflow permissions**: set to
**Read and write permissions**.

### 3. Add your sites

Edit `sites.yaml`. Each entry can have a `feed` (RSS/Atom URL) or a `listing_url` (HTML page to scrape):

```yaml
sites:
  - name: The Guardian
    slug: guardian
    feed: https://www.theguardian.com/world/rss
    listing_limit: 5

  - name: Some HTML-only site
    slug: example
    listing_url: https://example.com/news
    listing_class: ".article-link"
    listing_limit: 10
    force_playwright: true   # use a real browser for JS-heavy sites
```

### 4. Commit and push

The Action runs every day at 07:00 UTC. You can also trigger it manually
from the **Actions** tab, optionally targeting a single site slug.

## Running locally

Ensure [uv](https://github.com/astral-sh/uv) is installed.

```bash
# Scrape
cd scraper
uv run scrape.py --dry-run        # preview only
uv run scrape.py                  # write to ../content/

# Ensure playwright browser is installed
uv run playwright install chromium

# Build and preview the site
cd ../site
npm install
npm start    # http://localhost:8080
```
```bash
# Scrape
cd scraper
pip install -r requirements.txt
python -m playwright install chromium
python scrape.py --dry-run        # preview only
python scrape.py                  # write to ../content/

# Build and preview the site
cd ../site
npm install
npm start    # http://localhost:8080
```

### Adding a custom extraction rule

For sites where Readability struggles, add a `custom_selector` field in
`sites.yaml` (not implemented yet — see scrape.py for the hook point) or
pre-process the HTML before passing it to trafilatura.

### Search

Pagefind runs automatically as part of `npm run build`. It indexes all
rendered HTML and ships a WASM bundle. No external service needed.

## Privacy

This site uses anonymous [Umami analytics](https://umami.is/) to understand usage patterns without compromising visitor privacy. No personal data is collected.
