import * as yaml from 'js-yaml';
import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

function byDescendingPublishedDate(a, b) {
  const order = new Date(b.data.published) - new Date(a.data.published);
  if (order !== 0) {
    return order;
  }
  return new Date(b.data.scraped_at || b.date) - new Date(a.data.scraped_at || a.date);
}

export default function (eleventyConfig) {
  // ── Template Formats ─────────────────────────────────────────────────────
  // Process markdown as template (for article metadata)
  eleventyConfig.addTemplateFormats('md');

  // ── Content ──────────────────────────────────────────────────────────────
  // Pull markdown articles from ./content into the build
  eleventyConfig.addWatchTarget('./content');

  // ── Data ─────────────────────────────────────────────────────────────────
  // Make sites.yaml available as {{ sites }} in templates
  eleventyConfig.addGlobalData('sites', () => {
    const raw = readFileSync(join(__dirname, '../sites.yaml'), 'utf-8');
    return yaml.load(raw).sites;
  });

  // ── Collections ──────────────────────────────────────────────────────────
  eleventyConfig.addCollection('articles', (collectionApi) => {
    return collectionApi.getFilteredByGlob('content/**/*.md').sort(byDescendingPublishedDate);
  });

  // Articles grouped by source site slug
  eleventyConfig.addCollection('articlesBySite', (collectionApi) => {
    const all = collectionApi.getFilteredByGlob('content/**/*.md').sort(byDescendingPublishedDate);
    const grouped = {};
    for (const art of all) {
      const slug = art.data.source_slug || 'unknown';
      grouped[slug] = grouped[slug] || [];
      grouped[slug].push(art);
    }
    return grouped;
  });

  // Articles grouped by site, split into pages (30 per page)
  eleventyConfig.addCollection('articlesBySitePages', (collectionApi) => {
    const all = collectionApi.getFilteredByGlob('content/**/*.md').sort(byDescendingPublishedDate);

    const grouped = {};
    for (const art of all) {
      const slug = art.data.source_slug || 'unknown';
      grouped[slug] = grouped[slug] || [];
      grouped[slug].push(art);
    }

    const PAGE_SIZE = 30;
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
  });

  // ── Filters ───────────────────────────────────────────────────────────────
  eleventyConfig.addFilter('readableDate', (dateObj) => {
    if (!dateObj) return '';
    return new Date(dateObj).toLocaleDateString('en-GB', {
      day: 'numeric',
      month: 'short',
      year: 'numeric',
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

  eleventyConfig.addFilter('slice', (array, start, end) => {
    if (!array) return [];
    return array.slice(start, end);
  });

  // ── Passthrough ───────────────────────────────────────────────────────────
  eleventyConfig.addPassthroughCopy({ 'public/css': 'css' });
  eleventyConfig.addPassthroughCopy({ 'public/js': 'js' });

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
