# Agents

This repository includes specialized agent skills to help maintain and extend the News Barge configuration.

## Available Skills

### Scrape Analyzer
Located at: `.agents/skills/scrape-analyzer/SKILL.md`

This skill provides a disciplined methodology for adding new news sites to `sites.yaml`. It automates the process of:
- **RSS Discovery**: Searching for and verifying valid RSS/Atom feeds (preferred).
- **HTML Analysis**: If no feed is available, it identifies the most precise CSS classes (`listing_class`) or URL patterns (`listing_link_pattern`) to capture article links.
- **Noise Reduction**: Identifying and excluding sponsored or promoted content, and detecting article-page elements (modals, overlays, paywall prompts, author bios, comment widgets) that leak into the extracted prose and need `exclusions`.
- **Validation**: Verifying that links lead to actual articles and checking for JS-heavy pages that require Playwright.
- **Configuration**: Generating the correct YAML snippet for `sites.yaml` and verifying slug uniqueness.

## Development Guidelines for Agents

When creating or updating scripts for the agent to use:

### Python Execution
**All Python scripts must be executed using `uv`.** Do not use `pip` or `python` directly to avoid environment drift and ensure reproducible dependencies.

**Example:**
```bash
uv run scraper/scrape.py --dry-run
```

### Configuration Changes
Agents should never modify `sites.yaml` automatically. They should:
1. Perform the analysis.
2. Propose the configuration snippet.
3. Explicitly ask the user for permission to apply the change.

### Filesystem Search
**Never run `find /` against the whole filesystem.** The Poolside Laguna LLM has a recurring tendency to reach for `find /` when searching, which is slow, noisy, and sweeps up virtual filesystems and caches. Always prefer **ripgrep (`rg`)** instead — it's fast, respects `.gitignore`/`ignore` files, and is the right tool for content and path searches. For example, use `rg -l "pattern" path` to find files by content, or `rg --files path` to list files.
