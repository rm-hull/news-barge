---
name: scrape-analyzer
description: >
  A disciplined methodology for identifying the correct configuration for new sites added to the `sites.yaml` configuration. Use this skill whenever the user asks to 
  analyse, check, or report on a particular URL that looks like it might be a news website. Trigger
  on phrases like "analyse this URL", "check site https://news.bbc.co.uk", 
---

# Scrape Analyzer Skill

This skill provides a disciplined methodology for identifying the correct configuration (RSS feed or CSS selectors) for new sites added to the `sites.yaml` configuration.

## Goal
Determine if an RSS feed is available; if not, find the most precise CSS class or URL pattern that captures actual news articles while excluding navigation, footer, sponsored content, and guides. Additionally, identify **article-page exclusions** — HTML elements (modals, overlays, subscribe/paywall prompts, author bios, comment widgets, "follow on Google News" call-to-actions, cookie banners, etc.) that leak into the extracted prose and should be stripped with `exclusions` *before* trafilatura runs. Exclusions apply to the resolved article page, so they are relevant whether the article was discovered via RSS or via HTML-listing scraping.

## Process

### 1. Initial Inspection
- Search for an RSS feed (check for `<link rel="alternate" type="application/rss+xml">` or common paths like `/rss`, `/feed`).
- If an RSS feed is found, fetch the first few items to verify it contains actual news articles and not just category lists or empty entries.
- If a valid RSS feed is verified, skip to **Step 4 — Exclusion Detection** (article-page exclusions still apply to feed-sourced articles).
- If no RSS feed is found, fetch the `listing_urls` using `curl` or `playwright` (if JS-heavy).
- Search for `<a>` tags to identify the general structure of article links.
- Identify the container that holds the list of articles (e.g., `div.listingResult`, `article.news-item`).
### 2. Candidate Identification
- **Pattern Search**: Look for common URL segments in article links (e.g., `/news/`, `/article/`, `/story/`). Note: When adding these to `sites.yaml`, they MUST be enclosed in double quotes to ensure the regex is parsed correctly.
- **Class Search**: Look for repeating classes in the wrapping elements of article links.
- **Noise Analysis**: On the *listing* page, identify links to "Best Picks", "Reviews", "Sponsored", or "Promoted" content, and attributes like `data-sponsored="true"` or classes containing `ad-` or `promo-`. Where possible, prefer a `listing_link_pattern` that naturally skips these (e.g. a URL segment only real articles share). Article-page chrome (modals, overlays, footer CTAs) is handled separately in **Step 4 — Exclusion Detection**.

### 3. Verification
- Use `grep` or a small Python script (stored in the system temporary folder) to count how many links match the candidate class/pattern.
- Verify a few sample links to ensure they lead to actual articles and not category pages.
- Check if the links are relative or absolute to determine if `resolve_relative_to_root` is needed.
- Check if the page uses infinite scroll or dynamic loading; if so, recommend `force_playwright: true`.
- **Categorization**: Review the site's content and propose at least one relevant category (e.g., Local, Tech, World, Government) based on the project's existing categories.

### 4. Exclusion Detection
Not all unwanted content lives on the listing page — some of it is injected into the **article page** itself and survives trafilatura's extraction, polluting the Markdown body and frontmatter. This step identifies such elements so they can be removed with `exclusions` *before* extraction runs.

- Applies to both RSS-discovered and HTML-listing-discovered articles (exclusions run on the resolved article page, not the listing). Skip only if the target article pages are known to be clean of chrome.
- Fetch a representative article page (from a feed item or a listing link) using `curl`, or `playwright` when the site is JS-heavy (see Heuristics). Inspect the **rendered** HTML — use the browser's inspector to see overlays/modals that only appear after load.
- Scan the article HTML for elements that are *not* part of the article body but would otherwise be captured by trafilatura. Common offenders:
  - **Membership / paywall / subscribe overlays** — e.g. `role="dialog"`, `data-modal="paywall"`, `//div[contains(@class, 'paywall')]`, `//div[@id='subscribe']`.
  - **Cookie / privacy banners** — e.g. `//div[contains(@class, 'cookie')]` or `//div[@id='cookie']`.
  - **Author bios / byline blocks** that trafilatura treats as body text (typically near the end of the article) — e.g. `//div[contains(@class, 'author-bio')]`.
  - **Comment widgets** — e.g. `//div[contains(@class, 'comments')]`, `//div[contains(@class, 'viafoura')]`.
  - **Inline call-to-actions** — "Follow on Google News" badges (often a `<figure>` wrapping an image whose `src` lives on `news.google.com`), share prompts, "recommended reading", etc.
  - **Footer chrome** repeated at the end of the article.
- For each candidate, write the most **precise** exclusion expression possible:
  - Use a **bare attribute matcher** (`role="dialog"`, `data-sponsored="true"`, `x-show="showConfirmDisplayNamePrompt"`) for simple, robust selectors — these expand to `//*[@attr='value']`.
  - Use a **full XPath** when precision matters, e.g. `//figure[.//img[contains(@src, '...')]]` to target a specific leaky image, or `//p[contains(., 'Follow TechRadar on Google News')]` for a precise text snippet. Avoid broad tag selectors like `//div` that could remove real content.
- **Verify** each exclusion by re-running extraction with and without the rule and confirming that (a) the unwanted element is gone and (b) no legitimate article content is removed. When in doubt, tighten the selector rather than broadening it.

### 5. Configuration Output
Provide the finalized configuration in the following format. Before suggesting, verify that the `slug` does not conflict with any existing entries in `sites.yaml`. Explicitly ask the user if they would like you to add this configuration to `sites.yaml`. Do not add it automatically.
```yaml
  - name: [Site Name]
    slug: [site-slug]
    listing_urls:
      - [HTML_URL] # Only for HTML scraping
    feed: [RSS_URL] # Only for RSS feeds
    # Use listing_class/listing_link_pattern ONLY if feed is not used
    listing_class: "[class_name]" # Optional
    listing_link_pattern: "[pattern]" # Optional
    resolve_relative_to_root: [true/false] # Optional
    limit: [number]
    categories: [[Category1, Category2]] # Required
    # Optional — XPath expressions (or bare attr="value" matchers) for
    # article-page elements to strip BEFORE trafilatura extraction. These
    # run on every resolved article page, so they apply to feed- and
    # listing-sourced articles alike. See the sites.yaml header comment
    # for worked examples.
    exclusions:
      - role="dialog"                              # bare attr form
      - //figure[.//img[contains(@src, "...")]]    # full XPath
    notes: [optional] # Rationale for tricky exclusions, e.g. "strips Google News follow CTA that leaks into body"
```

## Heuristics
- **Prefer RSS over Scraping**: RSS feeds are more stable and efficient than HTML scraping. Always check for them first and verify their content.
- **Check for Soft 404s**: If relative links resolve to the home page but return 200 OK, `resolve_relative_to_root: true` is required.
- **JS Detection**: If the HTML returned by `curl` is mostly empty or contains "JavaScript required", recommend `force_playwright: true`.
- **Prefer Classes over Patterns**: If scraping is necessary, `listing_class` is usually more robust than `listing_link_pattern`.
- **Infinite Scroll/SPA**: If the initial HTML is missing content that appears in the browser, `force_playwright: true` is mandatory.
- **Strip Before Extract**: `exclusions` run *before* trafilatura, so a leaky modal never silently merges into the article body. Prefer exclusions over post-hoc Markdown cleanup — once text is in the body, it's hard to separate without a re-scrape.
- **Precise Over Broad**: Target the specific leaking element (a `<figure>` wrapping a known image `src`, a `data-modal` attribute, a precise text snippet) rather than broad class substrings or tag names, which risk removing real article content.
- **Attribute Match When Possible**: Bare `attr="value"` matchers (e.g. `role="dialog"`, `data-sponsored="true"`) are robust to class-name churn; use them unless you need the precision of a full XPath.
- **Safe When Unused**: A broad or no-match `exclusions` entry is a no-op, so it's cheap to include a rule you're unsure about — but always verify with a real extraction that it removes the offender and nothing more (see Step 4).
