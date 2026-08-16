// Layer-3 audit: the authoritative layer. Post-typeset DOM, console, network,
// axe-core, layout metrics. Maps findings onto CHECKS.md ids.
const { chromium } = require('playwright');
const fs = require('fs');
const axeSource = require('fs').readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');

const BASE = process.argv[2];
const PAGES = [
  ['/index.html', 'home'],
  ['/about/index.html', 'philosophy'],
  ['/c/0001/index.html', 'conjecture leaf'],
  ['/open-problems/index.html', 'open problems'],
  ['/papers/uber-groups-rsr/index.html', 'paper'],
  ['/surveys/uc-for-gamers/html/mainch5.html', 'UC edition chapter'],
  ['/blog/index.html', 'blog listing'],
  ['/uc/index.html', 'uc encyclopedia'],
];

const out = { axe: {}, pages: {} };

(async () => {
  const b = await chromium.launch();
  for (const [path, label] of PAGES) {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
    const p = await ctx.newPage();
    const errors = [], failed = [], warns = [], hosts = new Set();
    p.on('pageerror', e => errors.push(String(e).slice(0, 140)));
    p.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text().slice(0, 140));
                           if (m.type() === 'warning') warns.push(m.text().slice(0, 100)); });
    p.on('requestfailed', r => failed.push(r.url().slice(0, 100)));
    p.on('response', r => { const s = r.status(); if (s >= 400) failed.push(`${s} ${r.url().slice(0, 90)}`); });
    p.on('request', r => { try { const h = new URL(r.url()).host; if (!h.startsWith('localhost')) hosts.add(h); } catch {} });

    let rec = { label, path };
    try {
      await p.goto(BASE + path, { waitUntil: 'networkidle', timeout: 45000 });
      await p.waitForTimeout(1200);

      // MTH-01: MathJax error nodes after typeset
      rec.mathErrors = await p.evaluate(() => document.querySelectorAll('mjx-merror, .katex-error').length);
      rec.formulas = await p.evaluate(() => document.querySelectorAll('mjx-container').length);
      // MTH-03: stray $ outside math
      rec.strayDollar = await p.evaluate(() => {
        const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let n, c = 0;
        while ((n = w.nextNode())) {
          if (n.parentElement.closest('mjx-container, script, style, code, pre')) continue;
          const m = n.textContent.match(/\$/g); if (m) c += m.length;
        }
        return c;
      });
      // REF-01
      rec.unresolvedXref = await p.evaluate(() => (document.body.innerText.match(/\?@[\w-]+/g) || []).length);

      // RSP-01 / A11Y-10: overflow at 320 and 375
      rec.overflow = {};
      for (const w of [320, 375]) {
        await p.setViewportSize({ width: w, height: 800 });
        await p.waitForTimeout(350);
        rec.overflow[w] = await p.evaluate(() =>
          document.documentElement.scrollWidth - document.documentElement.clientWidth);
      }
      await p.setViewportSize({ width: 1280, height: 900 });
      await p.waitForTimeout(250);

      // axe-core (A11Y-*)
      await p.addScriptTag({ content: axeSource });
      const res = await p.evaluate(async () =>
        await window.axe.run(document, { resultTypes: ['violations'] }));
      rec.violations = res.violations.map(v => ({ id: v.id, impact: v.impact, n: v.nodes.length,
                                                  help: v.help.slice(0, 80) }));
      for (const v of res.violations) {
        out.axe[v.id] = out.axe[v.id] || { impact: v.impact, help: v.help, pages: [], nodes: 0 };
        out.axe[v.id].pages.push(label);
        out.axe[v.id].nodes += v.nodes.length;
      }
    } catch (e) {
      rec.fatal = String(e).slice(0, 160);
    }
    rec.errors = errors; rec.failed = failed; rec.hosts = [...hosts]; rec.warnCount = warns.length;
    out.pages[label] = rec;
    await ctx.close();
    console.log(`  ${label.padEnd(20)} math:${rec.formulas ?? '-'}/${rec.mathErrors ?? '-'}err ` +
                `ovf320:${rec.overflow?.[320] ?? '-'} ovf375:${rec.overflow?.[375] ?? '-'} ` +
                `js:${errors.length} net:${failed.length} axe:${(rec.violations||[]).length}` +
                (rec.fatal ? ` FATAL ${rec.fatal}` : ''));
  }
  await b.close();
  fs.writeFileSync('/tmp/audit_browser.json', JSON.stringify(out, null, 1));
  console.log('\n=== axe violations across sampled pages ===');
  for (const [id, v] of Object.entries(out.axe).sort((a, b) => b[1].nodes - a[1].nodes))
    console.log(`  ${(v.impact||'?').padEnd(8)} ${id.padEnd(28)} ${String(v.nodes).padStart(4)} nodes  ${v.pages.length} pages  ${v.help.slice(0,60)}`);
})();
