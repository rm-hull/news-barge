import yaml from "js-yaml";
import { readFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));

export default function (eleventyConfig) {
  // ── Template Formats ─────────────────────────────────────────────────────
  // Process markdown as template (for article metadata)
  eleventyConfig.addTemplateFormats("md");

  // ── Content ──────────────────────────────────────────────────────────────
  // Pull markdown articles from ./content into the build
  eleventyConfig.addWatchTarget("./content");

  // ── Data ─────────────────────────────────────────────────────────────────
  // Make sites.yaml available as {{ sites }} in templates
  eleventyConfig.addGlobalData("sites", () => {
    const raw = readFileSync(join(__dirname, "../sites.yaml"), "utf-8");
    return yaml.load(raw).sites;
  });

  // ── Collections ──────────────────────────────────────────────────────────
  eleventyConfig.addCollection("articles", (collectionApi) => {
    return collectionApi
      .getFilteredByGlob("content/**/*.md")
      .sort(
        (a, b) =>
          new Date(b.data.published || b.date) -
          new Date(a.data.published || a.date),
      );
  });

  // Articles grouped by source site slug
  eleventyConfig.addCollection("articlesBySite", (collectionApi) => {
    const all = collectionApi
      .getFilteredByGlob("content/**/*.md")
      .sort(
        (a, b) =>
          new Date(b.data.published || b.date) -
          new Date(a.data.published || a.date),
      );
    const grouped = {};
    for (const art of all) {
      const slug = art.data.source_slug || "unknown";
      grouped[slug] = grouped[slug] || [];
      grouped[slug].push(art);
    }
    return grouped;
  });

  // ── Filters ───────────────────────────────────────────────────────────────
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    if (!dateObj) return "";
    return new Date(dateObj).toLocaleDateString("en-GB", {
      day: "numeric",
      month: "short",
      year: "numeric",
    });
  });

  eleventyConfig.addFilter("absoluteUrl", (url, base) => {
    try {
      return new URL(url, base).toString();
    } catch {
      return url;
    }
  });

  // ── Passthrough ───────────────────────────────────────────────────────────
  eleventyConfig.addPassthroughCopy({ public: "public" });
  eleventyConfig.addPassthroughCopy({ "public/css": "css" });

  // ── Config ────────────────────────────────────────────────────────────────
  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts",
      data: "_data",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["njk", "md"],
  };
}
