---
name: scrape-analyzer
description: >
  A disciplined methodology for identifying the correct `listing_class` and `listing_link_pattern` 
  for new sites added to the `sites.yaml` configuration. Use this skill whenever the user asks to 
  analyse, check, or report on a particular URL that looks like it might be a news website. Trigger
  on phrases like "analyse this URL", "check site https://news.bbc.co.uk", 
---

# Scrape Analyzer Skill

This skill provides a disciplined methodology for identifying the correct `listing_class` and `listing_link_pattern` for new sites added to the `sites.yaml` configuration.

## Goal
Determine the most precise CSS class or URL pattern that captures actual news articles while excluding navigation, footer, sponsored content, and guides.

## Process

### 1. Initial Inspection
- Fetch the `listing_url` using `curl` or `playwright` (if JS-heavy).
- Search for `<a>` tags to identify the general structure of article links.
- Identify the container that holds the list of articles (e.g., `div.listingResult`, `article.news-item`).

### 2. Candidate Identification
- **Pattern Search**: Look for common URL segments in article links (e.g., `/news/`, `/article/`, `/story/`).
- **Class Search**: Look for repeating classes in the wrapping elements of article links.
- **Noise Analysis**: Identify common classes/patterns used for "Best Picks", "Reviews", or "Sponsored" content that should be excluded.

### 3. Verification
- Use `grep` or a small Python script to count how many links match the candidate class/pattern.
- Verify a few sample links to ensure they lead to actual articles and not category pages.
- Check if the links are relative or absolute to determine if `resolve_relative_to_root` is needed.

### 4. Configuration Output
Provide the finalized configuration in the following format:
```yaml
  - name: [Site Name]
    slug: [site-slug]
    listing_url: [URL]
    listing_class: "[class_name]" # Optional
    listing_link_pattern: "[pattern]" # Optional
    resolve_relative_to_root: [true/false] # Optional
    listing_limit: [number]
```

## Heuristics
- **Prefer Classes over Patterns**: `listing_class` is usually more robust than `listing_link_pattern` because URL structures can change or overlap with category pages.
- **Check for Soft 404s**: If relative links resolve to the home page but return 200 OK, `resolve_relative_to_root: true` is required.
- **JS Detection**: If the HTML returned by `curl` is mostly empty or contains "JavaScript required", recommend `force_playwright: true`.
