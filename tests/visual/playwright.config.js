// @ts-check
const path = require('path');
const { defineConfig } = require('@playwright/test');

// Dev-only harness for the CSS consistency refactor (see /audits or the
// conversation that produced this). Serves the pre-rendered _site/ as
// static files -- it never invokes `quarto render` itself, so it never
// becomes a build dependency of the site.
const SITE_DIR = path.resolve(__dirname, '../../_site');

module.exports = defineConfig({
  testDir: './specs',
  fullyParallel: true,
  retries: 0,
  reporter: [['list'], ['json', { outputFile: 'results.json' }]],
  expect: {
    toHaveScreenshot: {
      // Invariant budget from the refactor brief.
      maxDiffPixelRatio: 0.002,
      animations: 'disabled',
    },
  },
  use: {
    baseURL: 'http://127.0.0.1:4173',
    ignoreHTTPSErrors: true,
  },
  webServer: {
    command: 'python3 -m http.server 4173',
    cwd: SITE_DIR,
    url: 'http://127.0.0.1:4173/index.html',
    reuseExistingServer: true,
    timeout: 20_000,
  },
  projects: [{ name: 'chromium', use: { browserName: 'chromium' } }],
});
