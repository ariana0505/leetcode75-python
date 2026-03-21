import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://ariana0505.github.io',
  base: '/leetcode75',
  build: {
    format: 'directory'
  },
  markdown: {
    shikiConfig: {
      theme: 'github-dark'
    }
  }
});
