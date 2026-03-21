import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://ariana0505.github.io',
  base: '/leetcode75-python',
  build: {
    format: 'directory'
  },
  markdown: {
    shikiConfig: {
      theme: 'github-dark'
    }
  }
});
