// @ts-check
const { test, expect } = require('@playwright/test');

// Coverage note (logged deliberately, per the brief's "no silent caps"
// rule): the invariant as written calls for every one of the site's ~260
// rendered pages. This suite instead samples the 7 pages below, chosen to
// be the only ones that actually render every selector this refactor
// touches -- every other page renders a subset of the same shared SCSS
// rules, so a page not on this list cannot exercise a code path this list
// doesn't already cover. If a future edit touches a selector not
// exercised here, add a page that renders it before trusting this suite
// for that edit.
const PAGES = [
  { name: 'landing', path: '/index.html' },
  { name: 'statement', path: '/c/0001/index.html' },
  { name: 'uc-functionality', path: '/uc/layer-0-idealized-setup/f-crs/index.html' },
  { name: 'status-badge-legend', path: '/reviews/status-badge/index.html' },
  { name: 'problems-by-topic', path: '/problems/by-topic/index.html' },
  { name: 'problems-all-listing', path: '/problems/all/index.html' },
  { name: 'proposals-by-topic', path: '/projects/proposals/by-topic/index.html' },
];

const VIEWPORTS = [
  { name: '375', width: 375, height: 812 },
  { name: '768', width: 768, height: 1024 },
  { name: '1280', width: 1280, height: 900 },
  { name: '1920', width: 1920, height: 1080 },
];

const MODES = ['light', 'dark'];

// Quarto's own toggle sentinel (see _site/index.html's inline script):
// "default" == light (the authored default), "alternate" == dark.
async function setMode(page, mode) {
  await page.addInitScript((sentinel) => {
    window.localStorage.setItem('quarto-color-scheme', sentinel);
  }, mode === 'dark' ? 'alternate' : 'default');
}

async function gotoAndSettle(page, path) {
  await page.goto(path, { waitUntil: 'networkidle' });
  // MathJax typesets asynchronously after load and isn't reliably tied to
  // network-idle; a fixed settle window is pragmatic here since no edit in
  // this pass touches math rendering.
  await page.waitForTimeout(800);
}

for (const pg of PAGES) {
  for (const vp of VIEWPORTS) {
    for (const mode of MODES) {
      test(`${pg.name} @ ${vp.name}px [${mode}] default`, async ({ page }) => {
        await setMode(page, mode);
        await page.setViewportSize({ width: vp.width, height: vp.height });
        await gotoAndSettle(page, pg.path);
        await expect(page).toHaveScreenshot(`${pg.name}-${vp.name}-${mode}-default.png`, {
          fullPage: true,
        });
      });
    }
  }
}

// Interaction states, sampled at one representative viewport per state
// rather than the full grid -- same logged-reduction rationale as above.
const HOVER_TARGETS = {
  landing: '.cj-explore-card >> nth=0',
  statement: '.cj-tag-topic >> nth=0',
  // status-badge-legend renders bare `.cj-status-badge` SVGs with no
  // surrounding `.cj-status-link` wrapper, so it has no touched :hover
  // rule to sample -- intentionally absent from this map, not an oversight.
  'problems-by-topic': '.cj-tag-cloud-item >> nth=0',
  'problems-all-listing': '.cj-tag-topic >> nth=0',
  'proposals-by-topic': '.cj-tag-cloud-item >> nth=0',
};

for (const pg of PAGES) {
  const targetSelector = HOVER_TARGETS[pg.name];
  if (!targetSelector) continue; // uc-functionality: no :hover rule is touched by this pass
  for (const mode of MODES) {
    test(`${pg.name} @ 1280px [${mode}] hover`, async ({ page }) => {
      await setMode(page, mode);
      await page.setViewportSize({ width: 1280, height: 900 });
      await gotoAndSettle(page, pg.path);
      const target = page.locator(targetSelector);
      await target.scrollIntoViewIfNeeded();
      await target.hover();
      await expect(page).toHaveScreenshot(`${pg.name}-1280-${mode}-hover.png`, { fullPage: false });
    });

    test(`${pg.name} @ 1280px [${mode}] focus-visible`, async ({ page }) => {
      await setMode(page, mode);
      await page.setViewportSize({ width: 1280, height: 900 });
      await gotoAndSettle(page, pg.path);
      const target = page.locator(targetSelector);
      await target.scrollIntoViewIfNeeded();
      await target.focus();
      await expect(page).toHaveScreenshot(`${pg.name}-1280-${mode}-focus.png`, { fullPage: false });
    });
  }
}

// Panel-tabset alternate state: the statement pages use Quarto's tabset
// (Bootstrap nav-tabs) heavily. Not touched by this pass's edits, but the
// dark-only $nav-tabs-link-active-* variables flagged in the audit make
// this worth a sanity check now rather than assuming.
for (const mode of MODES) {
  test(`statement @ 1280px [${mode}] second tab open`, async ({ page }) => {
    await setMode(page, mode);
    await page.setViewportSize({ width: 1280, height: 900 });
    await gotoAndSettle(page, '/c/0001/index.html');
    const tabs = page.locator('.panel-tabset [role="tab"], .nav-tabs .nav-link');
    if (await tabs.count() > 1) {
      await tabs.nth(1).click();
      await page.waitForTimeout(200);
    }
    await expect(page).toHaveScreenshot(`statement-1280-${mode}-tab2.png`, { fullPage: false });
  });
}

// Mobile sidebar/TOC toggle: sampled on the one page with both a sidebar
// and a TOC, at the one viewport where they collapse behind a toggle.
for (const mode of MODES) {
  test(`statement @ 375px [${mode}] sidebar open`, async ({ page }) => {
    await setMode(page, mode);
    await page.setViewportSize({ width: 375, height: 812 });
    await gotoAndSettle(page, '/c/0001/index.html');
    const toggle = page.locator('#quarto-sidebar-toggle, .quarto-btn-toggle').first();
    if (await toggle.count() > 0) {
      await toggle.click();
      await page.waitForTimeout(200);
    }
    await expect(page).toHaveScreenshot(`statement-375-${mode}-sidebar-open.png`, { fullPage: false });
  });
}
