import * as yaml from 'js-yaml';
import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const PAGE_SIZE = 50;
const MIN_ARTICLES_FOR_PEOPLE = 10;
const MIN_ARTICLES_FOR_LOCATIONS = 50;
const __dirname = dirname(fileURLToPath(import.meta.url));

const fmt = new Intl.DateTimeFormat('en-GB', { dateStyle: 'long', timeZone: 'UTC' });
const dateCache = new Map();

// Simple LRU cache for compiled NER regex patterns.
// With ~25k articles, an unbounded cache exhausts the JS heap because each
// cached entry holds a compiled V8 regex (native code).  Capping it at 500
// entries keeps the most common term combinations while staying well within
// memory limits.
const NER_CACHE_MAX = 500;
const nerCache = new Map();

function nerCacheSet(key, value) {
  // If already present, move to end (most recently used).
  if (nerCache.has(key)) {
    nerCache.delete(key);
  } else if (nerCache.size >= NER_CACHE_MAX) {
    // Evict the oldest entry.
    const oldest = nerCache.keys().next().value;
    nerCache.delete(oldest);
  }
  nerCache.set(key, value);
}

function byDescendingPublishedDate(a, b) {
  const order = new Date(b.data.published) - new Date(a.data.published);
  if (order !== 0) {
    return order;
  }
  return new Date(b.data.scraped_at || b.date) - new Date(a.data.scraped_at || a.date);
}

function categoriesForArticle(article, siteMap) {
  const articleCategories = article.data.categories;
  if (Array.isArray(articleCategories) && articleCategories.length > 0) {
    return articleCategories;
  }
  return siteMap.get(article.data.source_slug) || ['Uncategorized'];
}

function normalizePersonName(person) {
  // Strip stray markdown characters and annotations
  let name = person
    .trim()
    .replace(/^[‘’']+/, '')
    .replace(/[‘’']+$/, '');
  // Remove markdown heading/list artifacts that sometimes leak in (##, etc.)
  name = name
    .replace(/^#+\s*/, '')
    .replace(/[……]+$/, '')
    .trim();
  if (!name) return null;
  // Normalize: strip trailing punctuation (periods, commas, etc.)
  name = name.replace(/[.,;:!?]+$/, '');
  // Only include names with at least 2 parts (first name + last name)
  if (name.split(/\s+/).length < 2) return null;
  return name;
}

function normalizeLocationName(location) {
  // Strip stray markdown characters and annotations
  let name = location
    .trim()
    .replace(/^[‘’']+/, '')
    .replace(/[‘’']+$/, '');
  // Remove markdown heading/list artifacts that sometimes leak in (##, etc.)
  name = name
    .replace(/^#+\s*/, '')
    .replace(/[……]+$/, '')
    .trim();
  if (!name) return null;
  // Normalize: strip trailing punctuation (periods, commas, etc.)
  name = name.replace(/[.,;:!?]+$/, '');
  return name;
}

function groupPeopleByArticle(allArticles, eleventyConfig) {
  const grouped = {};
  for (const art of allArticles) {
    const people = art.data.people;
    if (!Array.isArray(people) || people.length === 0) continue;
    for (const person of people) {
      if (!person || typeof person !== 'string') continue;
      const name = normalizePersonName(person);
      if (!name) continue;
      const slug = eleventyConfig.getFilter('slug')(name);
      if (!grouped[slug]) {
        grouped[slug] = { name, slug, count: 0, articles: [] };
      }
      grouped[slug].count++;
      grouped[slug].articles.push(art);
    }
  }

  const filtered = Object.values(grouped).filter((p) => p.count >= MIN_ARTICLES_FOR_PEOPLE);
  filtered.sort((a, b) => b.count - a.count);
  return filtered;
}

function groupLocationsByArticle(allArticles, eleventyConfig, minArticles) {
  const grouped = {};
  for (const art of allArticles) {
    const locations = art.data.locations;
    if (!Array.isArray(locations) || locations.length === 0) continue;
    for (const location of locations) {
      if (!location || typeof location !== 'string') continue;
      const name = normalizeLocationName(location);
      if (!name) continue;
      const slug = eleventyConfig.getFilter('slug')(name);
      if (!grouped[slug]) {
        grouped[slug] = { name, slug, count: 0, articles: [] };
      }
      grouped[slug].count++;
      grouped[slug].articles.push(art);
    }
  }

  const filtered = Object.values(grouped).filter((p) => p.count >= minArticles);
  filtered.sort((a, b) => b.count - a.count);
  return filtered;
}

export default function (eleventyConfig) {
  // ── Template Formats ─────────────────────────────────────────────────────
  // Process markdown as template (for article metadata)
  eleventyConfig.addTemplateFormats('md');

  // ── Markdown ─────────────────────────────────────────────────────────────
  // Prevent markdown-it from consuming backslashes before [ ] ( ).
  // Those sequences are MathJax delimiters (\[ … \] and \( … \)), not
  // markdown escapes.  We replace the built-in "escape" inline rule with
  // a version that preserves the backslash for these four characters.
  eleventyConfig.amendLibrary('md', (md) => {
    // Build the same ESCAPED lookup table as markdown-it, but without [ ] ( )
    const ESCAPED = new Uint8Array(256);
    '\\!"#$%&\'()*+,./:;<=>?@[]^_`{|}~-'
      .split('').forEach((ch) => { ESCAPED[ch.charCodeAt(0)] = 1 });
    // Remove MathJax delimiters from the escapable set
    ESCAPED[0x5B] = 0; // [
    ESCAPED[0x5D] = 0; // ]
    ESCAPED[0x28] = 0; // (
    ESCAPED[0x29] = 0; // )

    md.inline.ruler.disable('escape');
    md.inline.ruler.push('escape', (state, silent) => {
      const src = state.src;
      const max = state.posMax;
      let pos = state.pos;

      if (pos >= max || src.charCodeAt(pos) !== 0x5C) return false;
      pos++;

      if (pos >= max) return false;

      const ch1 = src.charCodeAt(pos);

      // Hard break: \ at end of line
      if (ch1 === 0x0A) {
        if (!silent) {
          state.push('hardbreak', 'br', 0);
        }
        pos++;
        while (pos < max) {
          const c = src.charCodeAt(pos);
          if (c !== 0x20 && c !== 0x09) break;
          pos++;
        }
        state.pos = pos;
        return true;
      }

      // \ before space is a literal backslash
      if (ch1 === 0x20) {
        if (!silent) {
          const token = state.push('text_special', '', 0);
          token.content = '\\';
          token.markup = '\\';
          token.info = 'escape';
        }
        state.pos = pos;
        return true;
      }

      let escapedStr = src[pos];
      if (ch1 >= 0xD800 && ch1 <= 0xDBFF && pos + 1 < max) {
        const ch2 = src.charCodeAt(pos + 1);
        if (ch2 >= 0xDC00 && ch2 <= 0xDFFF) {
          escapedStr += src[pos + 1];
          pos++;
        }
      }

      const origStr = '\\' + escapedStr;

      if (!silent) {
        const token = state.push('text_special', '', 0);
        // Only consume backslash for characters in the ESCAPED set
        token.content = ch1 < 256 && ESCAPED[ch1] ? escapedStr : origStr;
        token.markup = origStr;
        token.info = 'escape';
      }

      state.pos = pos + 1;
      return true;
    });
  });

  // ── Content ──────────────────────────────────────────────────────────────
  // Pull markdown articles from ./content into the build
  eleventyConfig.addWatchTarget('./content');

  // ── Data ─────────────────────────────────────────────────────────────────
  // Make sites.yaml available as {{ sites }} in templates
  eleventyConfig.addGlobalData('sites', () => {
    const raw = readFileSync(join(__dirname, '../sites.yaml'), 'utf-8');
    const sites = yaml.load(raw).sites;
    sites.forEach((site) => {
      site.sortName = site.name.replace(/^The\s+/i, '').toLowerCase();
    });
    return sites;
  });

  // ── Shared data cache ────────────────────────────────────────────────────
  // Avoid scanning 25k files repeatedly: cache the article list and derived
  // data so every collection reuses the same results.
  let cachedArticles = null;
  let cachedArticlesSorted = null;
  let cachedPeople = null;
  let cachedLocations = null;
  let cachedSiteMap = null;

  function getArticles(collectionApi) {
    if (!cachedArticles) {
      cachedArticles = collectionApi.getFilteredByGlob('content/**/*.md');
    }
    return cachedArticles;
  }

  function getArticlesSorted(collectionApi) {
    if (!cachedArticlesSorted) {
      cachedArticlesSorted = getArticles(collectionApi).slice().sort(byDescendingPublishedDate);
    }
    return cachedArticlesSorted;
  }

  function getPeople(collectionApi, eleventyCfg) {
    if (!cachedPeople) {
      cachedPeople = groupPeopleByArticle(getArticlesSorted(collectionApi), eleventyCfg);
    }
    return cachedPeople;
  }

  function getLocations(collectionApi, eleventyCfg) {
    if (!cachedLocations) {
      cachedLocations = groupLocationsByArticle(
        getArticlesSorted(collectionApi),
        eleventyCfg,
        MIN_ARTICLES_FOR_LOCATIONS
      );
    }
    return cachedLocations;
  }

  function getSiteMap() {
    if (!cachedSiteMap) {
      const sites = yaml.load(readFileSync(join(__dirname, '../sites.yaml'), 'utf-8')).sites;
      cachedSiteMap = new Map(sites.map((s) => [s.slug, s.categories || []]));
    }
    return cachedSiteMap;
  }

  // ── Collections ──────────────────────────────────────────────────────────
  eleventyConfig.addCollection('articles', (collectionApi) => {
    return getArticlesSorted(collectionApi);
  });

  // Articles grouped by source site slug
  eleventyConfig.addCollection('articlesBySite', (collectionApi) => {
    const all = getArticlesSorted(collectionApi);
    const grouped = {};
    for (const art of all) {
      const slug = art.data.source_slug || 'unknown';
      grouped[slug] = grouped[slug] || [];
      grouped[slug].push(art);
    }
    return grouped;
  });

  // Articles grouped by category
  eleventyConfig.addCollection('articlesByCategory', (collectionApi) => {
    const all = getArticles(collectionApi);
    const siteMap = getSiteMap();

    const grouped = {};
    for (const art of all) {
      const categories = categoriesForArticle(art, siteMap);

      for (const cat of categories) {
        grouped[cat] = grouped[cat] || [];
        grouped[cat].push(art);
      }
    }

    // Sort each category's articles
    for (const cat in grouped) {
      grouped[cat].sort(byDescendingPublishedDate);
    }

    return grouped;
  });

  // Locations grouped by name with article count and articles
  eleventyConfig.addCollection('locationsByArticleCount', (collectionApi) => {
    return getLocations(collectionApi, eleventyConfig);
  });

  // Locations listing pages (pagination of the locations index)
  eleventyConfig.addCollection('locationsByArticleCountPages', (collectionApi) => {
    const locations = getLocations(collectionApi, eleventyConfig);
    const pages = [];
    const totalPages = Math.ceil(locations.length / PAGE_SIZE);

    for (let i = 0; i < totalPages; i++) {
      pages.push({
        pageNumber: i,
        locations: locations.slice(i * PAGE_SIZE, (i + 1) * PAGE_SIZE),
        previousHref: i > 0 ? (i === 1 ? '/locations/' : `/locations/page/${i}/`) : null,
        nextHref: i < totalPages - 1 ? `/locations/page/${i + 2}/` : null,
      });
    }

    return pages;
  });

  // Articles grouped by location name, split into pages
  eleventyConfig.addCollection('articlesByLocationPages', (collectionApi) => {
    const locations = getLocations(collectionApi, eleventyConfig);

    const pages = [];
    for (const location of locations) {
      const totalPages = Math.ceil(location.articles.length / PAGE_SIZE);
      const base = `/locations/${location.slug}/`;

      for (let i = 0; i < totalPages; i++) {
        pages.push({
          location: location.name,
          slug: location.slug,
          count: location.count,
          pageNumber: i,
          articles: location.articles.slice(i * PAGE_SIZE, (i + 1) * PAGE_SIZE),
          previousHref: i > 0 ? (i === 1 ? base : `${base}page/${i}/`) : null,
          nextHref: i < totalPages - 1 ? `${base}page/${i + 2}/` : null,
        });
      }
    }

    return pages;
  });
  // People grouped by name with article count and articles
  // (filtered to people mentioned in at least MIN_ARTICLES_FOR_PEOPLE articles)
  eleventyConfig.addCollection('peopleByArticleCount', (collectionApi) => {
    return getPeople(collectionApi, eleventyConfig);
  });

  // People listing pages (pagination of the people index)
  eleventyConfig.addCollection('peopleByArticleCountPages', (collectionApi) => {
    const people = getPeople(collectionApi, eleventyConfig);
    const pages = [];
    const totalPages = Math.ceil(people.length / PAGE_SIZE);

    for (let i = 0; i < totalPages; i++) {
      pages.push({
        pageNumber: i,
        people: people.slice(i * PAGE_SIZE, (i + 1) * PAGE_SIZE),
        previousHref: i > 0 ? (i === 1 ? '/people/' : `/people/page/${i}/`) : null,
        nextHref: i < totalPages - 1 ? `/people/page/${i + 2}/` : null,
      });
    }

    return pages;
  });

  // Articles grouped by person name, split into pages
  eleventyConfig.addCollection('articlesByPersonPages', (collectionApi) => {
    const people = getPeople(collectionApi, eleventyConfig);

    const pages = [];
    for (const person of people) {
      const totalPages = Math.ceil(person.articles.length / PAGE_SIZE);
      const slug = eleventyConfig.getFilter('slug')(person.name);
      const base = `/people/${slug}/`;

      for (let i = 0; i < totalPages; i++) {
        pages.push({
          person: person.name,
          slug,
          count: person.count,
          pageNumber: i,
          articles: person.articles.slice(i * PAGE_SIZE, (i + 1) * PAGE_SIZE),
          previousHref: i > 0 ? (i === 1 ? base : `${base}page/${i}/`) : null,
          nextHref: i < totalPages - 1 ? `${base}page/${i + 2}/` : null,
        });
      }
    }

    return pages;
  });

  // Articles grouped by site, split into pages (30 per page)
  eleventyConfig.addCollection('articlesBySitePages', (collectionApi) => {
    const all = getArticlesSorted(collectionApi);

    const grouped = {};
    for (const art of all) {
      const slug = art.data.source_slug || 'unknown';
      grouped[slug] = grouped[slug] || [];
      grouped[slug].push(art);
    }

    const pages = [];

    for (const [slug, articles] of Object.entries(grouped)) {
      const siteName = articles[0].data.source_site;
      const totalPages = Math.ceil(articles.length / PAGE_SIZE);
      const base = `/sites/${slug}/`;

      for (let i = 0; i < totalPages; i++) {
        pages.push({
          slug,
          siteName,
          pageNumber: i,
          articles: articles.slice(i * PAGE_SIZE, (i + 1) * PAGE_SIZE),
          previousHref: i > 0 ? (i === 1 ? base : `${base}page/${i}/`) : null,
          nextHref: i < totalPages - 1 ? `${base}page/${i + 2}/` : null,
        });
      }
    }

    return pages;
  });

  // Articles grouped by category, split into pages (30 per page)
  eleventyConfig.addCollection('articlesByCategoryPages', (collectionApi) => {
    const all = getArticlesSorted(collectionApi);
    const siteMap = getSiteMap();

    const grouped = {};
    for (const art of all) {
      const categories = categoriesForArticle(art, siteMap);

      for (const cat of categories) {
        grouped[cat] = grouped[cat] || [];
        grouped[cat].push(art);
      }
    }

    const pages = [];

    for (const [category, articles] of Object.entries(grouped)) {
      const totalPages = Math.ceil(articles.length / PAGE_SIZE);
      const base = `/categories/${eleventyConfig.getFilter('slugify')(category)}/`;

      for (let i = 0; i < totalPages; i++) {
        pages.push({
          category,
          pageNumber: i,
          articles: articles.slice(i * PAGE_SIZE, (i + 1) * PAGE_SIZE),
          previousHref: i > 0 ? (i === 1 ? base : `${base}page/${i}/`) : null,
          nextHref: i < totalPages - 1 ? `${base}page/${i + 2}/` : null,
        });
      }
    }

    return pages;
  });

  // ── Computed Data ──────────────────────────────────────────────────────────
  eleventyConfig.addGlobalData('eleventyComputed', {
    permalink: function (data) {
      const inputPath = data.page?.inputPath || data.inputPath;

      if (inputPath && inputPath.includes('content/')) {
        const normalizedPath = inputPath.replace(/\\/g, '/');
        const parts = normalizedPath.split('/');

        const contentIndex = parts.indexOf('content');
        if (contentIndex !== -1 && parts.length > contentIndex + 4) {
          const year = parts[contentIndex + 1];
          const month = parts[contentIndex + 2];
          const day = parts[contentIndex + 3];
          const filename = parts[contentIndex + 4].replace('.md', '');

          // Force uniqueness using date and filename
          return `/articles/${year}/${month}/${day}/${filename}/`;
        }
      }
      return data.permalink;
    },
    title: function (data) {
      if (data.title && typeof data.title === 'string' && data.title.includes(' | ')) {
        return data.title.split(' | ')[0].trim();
      }
      return data.title;
    },
  });

  // Add last updated time
  eleventyConfig.addGlobalData('lastUpdated', () => new Date().toISOString());

  // Array of site slugs that have had articles scraped within the last 6 hours
  // (computed via a collection so it has access to all article frontmatter)
  eleventyConfig.addCollection('sitesWithRecentArticles', (collectionApi) => {
    const SIX_HOURS_MS = 6 * 60 * 60 * 1000;
    const now = Date.now();
    const slugs = new Set();
    const all = getArticles(collectionApi);
    for (const art of all) {
      const scrapedAt = art.data.scraped_at;
      if (scrapedAt) {
        const age = now - new Date(scrapedAt).getTime();
        if (age < SIX_HOURS_MS && art.data.source_slug) {
          slugs.add(art.data.source_slug);
        }
      }
    }
    return [...slugs];
  });

  // ── Filters ───────────────────────────────────────────────────────────────
  // Take the first N items of an array (Nunjucks' built-in `slice` filter
  // divides an array into N chunks, it does NOT perform array sub-slicing).
  eleventyConfig.addFilter('limit', (arr, n) => {
    if (!Array.isArray(arr)) return arr;
    return arr.slice(0, n);
  });

  eleventyConfig.addFilter('isoDate', (dateObj) => {
    if (!dateObj) return '';
    const date = new Date(dateObj);
    return date.toISOString().split('T')[0];
  });

  eleventyConfig.addFilter('readableDate', (d) => {
    if (!d) return '';
    const date = d instanceof Date ? d : new Date(d);
    if (Number.isNaN(date.getTime())) return '';
    const key = d instanceof Date ? d.getTime() : d;
    let out = dateCache.get(key);
    if (out === undefined) {
      out = fmt.format(date);
      dateCache.set(key, out);
    }
    return out;
  });

  eleventyConfig.addFilter('readableDateTime', (dateObj) => {
    if (!dateObj) return '';
    return new Date(dateObj).toLocaleString('en-GB', {
      day: 'numeric',
      month: 'short',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      timeZone: 'Europe/London',
    });
  });

  eleventyConfig.addFilter('absoluteUrl', (url, base) => {
    try {
      return new URL(url, base).toString();
    } catch {
      return url;
    }
  });

  eleventyConfig.addFilter('basename', (path) => {
    if (!path) return '';
    return path.split('/').pop();
  });

  eleventyConfig.addFilter('stripQueryParams', (url) => {
    if (!url) return '';
    return url.split('?')[0];
  });

  eleventyConfig.addFilter('stripImageSize', (url) => {
    if (!url) return '';
    return url.replace(/-(\d+)-(\d+)(?=\.[a-z]+$)/i, '');
  });

  function escapeRegExp(str) {
    return String(str).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Precompiled regex for the uppercase check in wrapSearchable.
  const hasUpperCase = /[A-Z]/;

  // Hoisted replacement handler — avoids creating a closure on every call.
  function wrapSearchable(match) {
    // Entities are proper nouns: avoid matching all-lowercase words
    // that merely share a case-insensitive form (the pronoun "us"
    // vs. the acronym "US").
    if (hasUpperCase.test(match)) {
      return `<a href="/search/?q=${encodeURIComponent('"' + match + '"')}" class="searchable">${match}</a>`;
    }
    return match;
  }

  eleventyConfig.addFilter('nerSearch', (html, ...termArrays) => {
    if (!html) return html;
    const input = typeof html === 'string' ? html : String(html);

    // Fast path: if there are no term arrays at all, skip everything.
    if (termArrays.length === 0) return input;

    const seen = new Set();
    const terms = [];
    for (const arr of termArrays) {
      if (!Array.isArray(arr)) continue;
      for (const raw of arr) {
        if (raw == null) continue;
        // Strip trailing sentence punctuation that sometimes leaks into
        // extracted names ("Falkland Islands." -> "Falkland Islands").
        const term = String(raw)
          .trim()
          .replace(/[.,;:!?]+$/, '');
        if (!term) continue;
        const key = term.toLowerCase();
        if (seen.has(key)) continue;
        seen.add(key);
        terms.push(term);
      }
    }
    if (terms.length === 0) return input;

    // Build a cache key from the sorted, lowercased terms so articles sharing
    // the same set of terms reuse the compiled regex.
    const cacheKey = terms
      .map((t) => t.toLowerCase())
      .sort()
      .join('\x00');
    let cached = nerCache.get(cacheKey);
    if (!cached) {
      // Escape for use in a regex alternation, longest first so multi-word
      // phrases win over their shorter sub-strings.
      const alternation = terms
        .map(escapeRegExp)
        .sort((a, b) => b.length - a.length)
        .join('|');
      cached = new RegExp('\\b(?:' + alternation + ')\\b', 'gi');
      nerCacheSet(cacheKey, cached);
    }

    // String.prototype.replace() resets lastIndex on /g regexes before each
    // call, so the cached instance can be reused directly without copying.
    const termPattern = cached;

    // Split input by LaTeX math delimiters so we don't mangle terms inside
    // math expressions.  Display math: \[ … \], inline math: \( … \).
    // We split on the delimiters and process only the non-math segments.
    const mathSplit = input.split(/(\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))/);

    let out = '';
    for (let i = 0; i < mathSplit.length; i++) {
      const segment = mathSplit[i];
      // Odd indices are math blocks (captured by the alternation) — skip them
      if (i % 2 === 1) {
        out += segment;
        continue;
      }

      // Even indices are non-math text — apply term replacement
      // Fast path: if the segment has no HTML tags, replace directly.
      if (segment.indexOf('<') === -1) {
        out += segment.replace(termPattern, wrapSearchable);
        continue;
      }

      // Only rewrite text that lives outside of HTML tags so attribute
      // values (hrefs, alt text, ...) are left untouched.
      const parts = segment.split(/(<[^>]*>)/);
      // split() with capturing group produces: [text, tag, text, tag, ...]
      // Odd indices are tags, even indices are text.
      let segOut = parts[0].replace(termPattern, wrapSearchable);
      for (let j = 1; j < parts.length; j += 2) {
        segOut += parts[j] + parts[j + 1].replace(termPattern, wrapSearchable);
      }
      out += segOut;
    }
    return out;
  });

  eleventyConfig.addFilter('altOverlay', (html) => {
    if (!html) return html;
    const input = typeof html === 'string' ? html : String(html);

    const imgRe = /(<p>\s*)?(<img\b[^>]*?\salt\s*=\s*(?:"([^"]+)"|'([^']+)')[^>]*>)(\s*<\/p>)?/gi;

    return input.replace(imgRe, (match, pOpen, imgTag, dqAlt, sqAlt, pClose) => {
      const altText = dqAlt || sqAlt || '';
      if (!altText.trim()) return match;

      const safeAlt = altText
        .replace(/&(?!(?:[a-z][a-z0-9]*|#\d+|#x[0-9a-f]+);)/gi, '&amp;') // leave existing entities alone
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');

      const wrapper =
        `<span class="img-alt-overlay">${imgTag}` +
        `<span class="img-alt-text" aria-hidden="true">${safeAlt}</span></span>`;

      // Image alone in its <p>: drop the <p> tags. Otherwise preserve whatever was captured.
      if (pOpen && pClose) return wrapper;
      return (pOpen || '') + wrapper + (pClose || '');
    });
  });

  eleventyConfig.addFilter('monthName', (monthIndex) => {
    const months = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ];
    return months[parseInt(monthIndex) - 1];
  });

  // ── Passthrough ───────────────────────────────────────────────────────────
  eleventyConfig.addPassthroughCopy({ 'public/css': 'css' });
  eleventyConfig.addPassthroughCopy({ 'public/js': 'js' });
  eleventyConfig.addPassthroughCopy({
    'public/favicon.svg': 'favicon.svg',
    'public/favicon.ico': 'favicon.ico',
    'public/apple-touch-icon.png': 'apple-touch-icon.png',
    'public/icon-192.png': 'icon-192.png',
    'public/icon-512.png': 'icon-512.png',
    'public/site.webmanifest': 'site.webmanifest',
  });

  // ── Config ────────────────────────────────────────────────────────────────
  return {
    dir: {
      input: '.',
      output: '_site',
      includes: '_includes',
      layouts: '_layouts',
      data: '_data',
    },
    markdownTemplateEngine: 'njk',
    htmlTemplateEngine: 'njk',
    templateFormats: ['njk', 'md'],
  };
}
