import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

// English-only at launch. When a second locale ships, re-introduce
// `i18n: { defaultLocale, locales, routing }` here and pass matching
// `i18n` config to the sitemap integration.
export default defineConfig({
  site: "https://brazlatch.com",
  integrations: [tailwind(), sitemap()],
  build: {
    format: "directory",
  },
});
