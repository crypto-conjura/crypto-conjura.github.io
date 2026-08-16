# Site audit, 17 August 2026

Run against `CHECKS.md`. Scope: the whole built site, 259 HTML pages, rendered
from `main` at `8a85dac` and cross-checked against production.

Method follows the taxonomy's three layers. Layer 1 and 2 (grep, static crawl of
`_site`) produced hypotheses; layer 3 (headless Chromium, post-typeset DOM,
axe-core 4.13, console and network logs, layout metrics at 320 and 375 px)
settled them. **Every count below that is called a finding survived layer 3 or a
direct inspection of the markup.** Where a layer-2 signal turned out to be an
artefact of the detector, it is recorded as cleared rather than dropped, because
the false positives are informative about the detector.

Sampled in the browser: home, Philosophy, `c/0001`, Open Problems, the
uber-groups-rsr paper, a UC edition chapter, the blog listing, the UC
encyclopedia index.

---

## Clean

These were checked and found sound. They are the load-bearing ones for an
archive, so they are listed first.

| ID | Result |
|---|---|
| LNK-01 | 0 broken internal links across 259 pages |
| LNK-02 | 0 dead fragments; every `#anchor` resolves against its target's id set |
| LNK-10 | 0 missing PDF/LaTeX/Lean assets |
| MTH-01 | 0 MathJax error nodes, on pages carrying 42, 62 and 425 formulas |
| MTH-03 | 0 stray `$` outside math |
| MTH-09 | MathJax is self-hosted; a UC chapter contacts no external host at all |
| REF-01/02 | 0 unresolved cross-references, 0 unresolved citations |
| JSC-01 | 0 uncaught JavaScript exceptions on any sampled page |
| JSC-02 | 0 failed or non-2xx subresource requests |
| JSC-05 | Theme toggle changes theme and persists across reload |
| BLD-01 | `site_libs/` assets serve 200 in production; the Actions deploy does not run Jekyll, so `.nojekyll` is not required |
| BLD-05 | Clean render, 0 warnings or errors in the log |
| MET-07 | `robots.txt` present, points at the sitemap, disallows nothing |
| MET-08 | No stray `noindex` |
| SEC-02 | No mixed-content subresources |
| RSP-01 | No horizontal overflow at 320 or 375 px, except the one page below |

## S2 — accessibility

Ordered by how much they cost a real user.

**A11Y-02 (colour contrast), 55 failing nodes on all 8 sampled pages.** Confirmed
by axe with computed values:

- Site footer, every page: `#959592` on `#faf9f5` = **2.85:1**, against a 4.5:1
  floor. This is the "This site is AI-generated and has not been independently
  reviewed" line and its link — the site's own provenance disclaimer is the least
  readable text on the page.
- UC edition, 41 of the 55: an accent link at `#e89b7f` on the `#ffffff`
  tcolorbox fill = **2.22:1**, and interface-box header text at `#7a4a0c` on
  `#e0a85c` = **3.52:1**.

The UC edition failures are a direct consequence of a decision recorded in
`scripts/build_uc_html.sh` step 7: the site palette was applied to text and links
while the book's own `tcolorbox` fills were deliberately left alone, because each
generated rule sets a text colour beside its background. That reasoning was
sound for the box interiors and wrong at the seam, where a themed link colour
lands on an unthemed white fill. It needs revisiting, not just recolouring.

**A11Y-04 / LNK-09 (controls with no accessible name), 7 nodes per page,
site-wide.** Three distinct controls, all from Quarto's own navbar and sidebar:

- The dark-mode toggle is an `<a>` with an empty `href` and no text. This is
  verbatim the example in `CHECKS.md`'s A11Y section.
- The GitHub navbar link contains only `<i class="bi bi-github" role="img">`
  with no `aria-label` — fails `link-name` and `role-img-alt` together.
- Four sidebar collapse toggles, empty `href`, no name.
- The sidebar's "Philosophy" section header renders as an anchor with no `href`,
  which is the inert-`section:`-entry behaviour this repo has hit before.

**A11Y-01 / A11Y-12 (status badge), 2 nodes.** The `cj-status-badge` SVG carries
`role="img"` but no `<title>` child, so axe fails it on `svg-img-alt`. The
accessible name lives on the wrapping `<a>`'s `aria-label`, so the badge is not
silent to a screen reader — but the SVG itself is unlabelled, and the badge is
the site's central trust signal. Worth fixing properly given `CHECKS.md` singles
out A11Y-12: the shape/glyph inside the badge does distinguish states, so it is
not colour-alone, but that should be asserted deliberately rather than by luck.

**SEM-02 / heading-order, 10 pages.** Confirmed in the browser on 3 of them, e.g.
an `<h3>Abstract</h3>` with no intervening `<h2>`.

**SEM-01 (duplicate ids), 513 instances.** `id="quarto-text-highlighting-styles"`
appears three times per page. Quarto's output, not authored content, but it is a
genuine violation and breaks id-based assistive-technology references.

**SEM-03, 258 pages.** Two `<h1>` per page: Quarto emits a
`quarto-secondary-nav-title` for narrow viewports and a `title d-none d-lg-block`
for wide. Only one is visible at a time, so this is a DOM-level rather than a
perceived defect.

**UC edition landmarks: `region` 255 nodes, `landmark-one-main`,
`page-has-heading-one`.** The tex4ht pages have no `<main>`, no landmarks and no
`<h1>`, so all content sits outside any landmark. Cheap to fix in the generator.

**SEM-06, 3 pages.** Tables without `<th>`, including the status-legend table,
which is exactly the table a non-visual reader most needs.

## S3 — discoverability and metadata

- **MET-05**, all 259 pages: no `og:image` anywhere. Every share renders bare.
- **MET-02**, 258 pages: no `<meta name="description">`. Partially mitigated —
  `og:description` and `twitter:description` are present.
- **MET-03/04**, 86 pages: no canonical and no Open Graph. 27 are Quarto redirect
  stubs (which also lack `lang` and `charset`, **SEM-07/08**); the other 59 are
  the UC edition's tex4ht pages, which are real published pages and carry none of
  this metadata.
- **MET-06**: `sitemap.xml` lists 173 URLs against 259 pages. The 59 UC edition
  pages and the 27 redirect stubs are absent, so the book is invisible to a
  crawler that trusts the sitemap.
- **MTH-07**, 8 pages: raw TeX in `og:title`, e.g. `Tight Time-Space Tradeoffs
  for \(k\)-Collisions`. Social cards will show the backslashes.
- **LNK-05**, 49 links: absolute `https://crypto-conjura.github.io` self-links,
  mostly from generated status badges. These break local preview and any future
  domain change.
- **LNK-07**, 4 links: outbound `http://`.
- **RSP-01**, 1 page: the uber-groups-rsr paper overflows horizontally by 23 px
  at 320 px. Every other sampled page is clean at both 320 and 375.

## S3/S4 — operational

- **OPS-01**: no custom `404.html`. Production returns GitHub's default.
- **OPS-02**: no favicon; none referenced, none served.
- **OPS-05**: no `CITATION.cff`, on a site whose purpose is to be cited.
- **MET-01**: 27 pages share the title `Redirect`.

## Not established

- **JSC-03 (search)**: `search.json` and the search UI are both present in the
  build, but the automated interaction did not locate the input, so this is
  **indeterminate**, not a failure. It needs a hand check.
- **LNK-03/04 (external link rot)**: 139 distinct external URLs were inventoried
  but not fetched. Per the taxonomy, 401/403/429/999 must be treated as
  indeterminate rather than broken, so this needs the rate-limited checker.
- **CNT-01/09 (badge vs Lean artifact)**: no Lean artifacts are currently linked,
  so there was nothing to contradict. This check becomes live the moment one is.
- **REF-05/06 (citation resolution)**: not run here. The repo's own convention
  already requires verifying every citation at the source, and the encyclopedia
  work is generating new ones continuously; this wants the DOI/ePrint resolver
  rather than a spot check.
- **PRF-\***, **A11Y-05/06/09/13**, **SEC-05/08**: not covered in this pass.

## Detector notes

Three layer-2 signals were artefacts, all of them mine, and worth recording
because each would have been reported as a defect by a less sceptical pass:

- The crawler parsed only double-quoted attributes, so every single-quoted
  attribute in the tex4ht output looked like an empty `href` or a missing `alt`.
  That alone accounted for ~5,000 phantom findings including 9 phantom
  missing-`alt` images.
- Reachability compared resolved absolute paths against relative ones, so all 258
  non-index pages looked orphaned (CNT-04).
- Mixed content was tested against `href` as well as `src`, turning 4 ordinary
  outbound `http://` links into phantom SEC-02 failures.
