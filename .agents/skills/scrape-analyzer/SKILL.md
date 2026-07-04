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
Determine if an RSS feed is available; if not, find the most precise CSS class or URL pattern that captures actual news articles while excluding navigation, footer, sponsored content, and guides.

## Process

### 1. Initial Inspection
- Search for an RSS feed (check for `<link rel="alternate" type="application/rss+xml">` or common paths like `/rss`, `/feed`).
- If an RSS feed is found, fetch the first few items to verify it contains actual news articles and not just category lists or empty entries.
- If a valid RSS feed is verified, skip to **Configuration Output**.
- If no RSS feed is found, fetch the `listing_url` using `curl` or `playwright` (if JS-heavy).
- Search for `<a>` tags to identify the general structure of article links.
- Identify the container that holds the list of articles (e.g., `div.listingResult`, `article.news-item`).
### 2. Candidate Identification
- **Pattern Search**: Look for common URL segments in article links (e.g., `/news/`, `/article/`, `/story/`). Note: When adding these to `sites.yaml`, they MUST be enclosed in double quotes to ensure the regex is parsed correctly.
- **Class Search**: Look for repeating classes in the wrapping elements of article links.
- **Noise Analysis**: Identify common classes/patterns used for "Best Picks", "Reviews", "Sponsored", or "Promoted" content. Look for attributes like `data-sponsored="true"` or classes containing `ad-` or `promo-` that should be excluded.

### 3. Verification
- Use `grep` or a small Python script (stored in the system temporary folder) to count how many links match the candidate class/pattern.
- Verify a few sample links to ensure they lead to actual articles and not category pages.
- Check if the links are relative or absolute to determine if `resolve_relative_to_root` is needed.
- Check if the page uses infinite scroll or dynamic loading; if so, recommend `force_playwright: true`.

### 4. Configuration Output
Provide the finalized configuration in the following format. Before suggesting, verify that the `slug` does not conflict with any existing entries in `sites.yaml`. Explicitly ask the user if they would like you to add this configuration to `sites.yaml`. Do not add it automatically.
```yaml
  - name: [Site Name]
    slug: [site-slug]
    listing_url: [HTML_URL] # Only for HTML scraping
    feed: [RSS_URL] # Only for RSS feeds
    # Use listing_class/listing_link_pattern ONLY if feed is not used
    listing_class: "[class_name]" # Optional
    listing_link_pattern: "[pattern]" # Optional
    resolve_relative_to_root: [true/false] # Optional
    limit: [number]
```

## Heuristics
- **Prefer RSS over Scraping**: RSS feeds are more stable and efficient than HTML scraping. Always check for them first and verify their content.
- **Check for Soft 404s**: If relative links resolve to the home page but return 200 OK, `resolve_relative_to_root: true` is required.
- **JS Detection**: If the HTML returned by `curl` is mostly empty or contains "JavaScript required", recommend `force_playwright: true`.
- **Prefer Classes over Patterns**: If scraping is necessary, `listing_class` is usually more robust than `listing_link_pattern`.
- **Infinite Scroll/SPA**: If the initial HTML is missing content that appears in the browser, `force_playwright: true` is mandatory.
