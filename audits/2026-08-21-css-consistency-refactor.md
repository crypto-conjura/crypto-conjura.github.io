# CSS consistency refactor, 21 August 2026

Behaviour-preserving refactor per the brief in this session. Phase 1 (audit)
and Phase 2 (apply) both completed; scope was narrowed twice by explicit
user decision during Phase 1 (see "Deferred", below).

## What changed

Every substitution below replaces a literal with a Sass variable holding
the exact same value. None of them changes what a browser paints -- see
"Verification".

| Old value | New value | Affected selectors | File(s) |
|---|---|---|---|
| `#f8ecd4` (literal, 4 sites) | `$cj-fill-strong` | `.callout-important` header/body, `.cj-mission`, `.cj-explore-card:hover`, `.cj-interface-head` | theme-light.scss |
| `#fbf6ea` (literal, 3 sites) | `$cj-fill-soft` | `.callout-note` header/body, `.cj-explore-card`, `.cj-interface` | theme-light.scss |
| `#e0c9a8` (literal, 2 sites) | `$cj-tan-border` | `.cj-interface` border, `.cj-interface-head` border-bottom | theme-light.scss |
| `#332a1a` (literal, 4 sites) | `$cj-fill-strong` | same selectors as above, dark palette | theme-dark.scss |
| `#282019` (literal, 3 sites) | `$cj-fill-soft` | same selectors as above, dark palette | theme-dark.scss |
| `#4a3f2c` (literal, 2 sites) | `$cj-tan-border` | same selectors as above, dark palette | theme-dark.scss |
| `#f5f4ef` (literal, 2 unrelated sites) | `$cj-ink-light` | `::selection` color, `.cj-glyph` fill | theme-dark.scss |
| `#e89b7f` (hardcoded literal) | `$link-color` | `code` | theme-dark.scss |
| sans-serif stack (literal, identical in both files) | `$font-family-glyph` | `.cj-glyph` | both |
| `padding: 1.25em 1.5em` (2 sites/file) | `$cj-box-padding` | `.cj-mission`, `.cj-explore-card` | both |
| `border-radius: 1em` (2 sites/file) | `$cj-pill-radius` | `.cj-tag`, `.cj-io` | both |
| `font-size: 0.85em` (2 sites/file) | `$cj-caption-size` | `.cj-status-summary`, `.nav-footer` | both |
| `margin-left: 0.5em` (2 sites/file) | `$cj-inline-gap` | `.cj-io`, `.cj-comment` | both |
| `margin: 1.2em 0` (2 sites/file) | `$cj-loose-margin` | `.cj-listing-empty`, `.cj-tag-cloud` | both |

20 substitution sites total across the two files; 9 new shared variables
in `theme-light.scss`, 10 in `theme-dark.scss` (the extra one is
`$cj-ink-light`, which has no light-mode equivalent cluster -- see the
Phase 1 audit). The `code { color: #e89b7f }` fix in dark mode is the one
genuine authoring inconsistency found: light's equivalent rule already
referenced `$link-color`; dark hardcoded the literal that happened to
equal it.

Nothing else was touched. No selector, class name, HTML structure, or
non-duplicate literal was changed. `_quarto.yml`, all `.qmd`/`.md`
sources, and every file outside the two theme stylesheets are untouched.

## Verification

- Baseline: 80 Playwright screenshots (7 representative pages that between
  them exercise every touched selector, x 4 viewports, x 2 colour modes,
  plus hover/focus-visible/tabset/mobile-sidebar states), captured against
  `main` @ `97d27dc` before any edit, committed in
  `tests/visual/specs/theme.spec.js-snapshots/`.
- Site re-rendered in full (`quarto render`, 334 files, exit 0) so every
  page's compiled-CSS link hash reflects the edited SCSS.
- Comparison run: **80/80 passed at `maxDiffPixelRatio: 0`** (the brief's
  own budget is 0.002; this pass used the stricter exact-zero threshold to
  confirm "byte-for-byte identical," not merely "within tolerance"). Zero
  snapshot files were touched by the comparison run -- `git status` after
  the full apply-and-reverify cycle shows only the two theme files and one
  config comment changed.
- Contrast: unaffected by construction -- every substitution preserves the
  exact computed colour, so no text/background pair anywhere on the site
  changed contrast ratio.

## Deferred

Carried over from the Phase 1 audit, with the scope decisions made during
that phase:

1. **`surveys/uc-for-gamers/html/` + `scripts/build_uc_html.sh`** -- a
   second, independent CSS surface (tex4ht output, 69 tracked files) that
   hand-copies the site's SCSS palette with no drift detection, and is
   also where the two worst known contrast failures live (link colour
   2.22:1, interface-box header text 3.52:1, both below the 4.5:1 floor;
   see `audits/2026-08-17-site-audit.md`). **Explicitly left out of scope
   by user decision** -- the `.sh` script and its generated output aren't
   in the brief's editable file types, and no partial fix was requested.
2. **Site footer contrast**, `#959592` on `#faf9f5` = 2.85:1 (same prior
   audit). This literal does not appear in either theme SCSS file --
   it's most likely a Bootstrap-computed muted/secondary colour rather
   than an authored one. Not touched: its true source was never
   confirmed, and guessing at a fix wasn't part of this pass's scope.
3. **`0.95rem` vs `0.95em`** on `.cj-explore-card p` vs `.cj-listing-empty`
   -- same number, different unit, likely harmless in their current
   unnested contexts. Left as-is by user decision.
4. **`.cj-mission` border-radius 4px vs `.cj-explore-card` border-radius
   6px** -- same visual family, 2px apart, which exceeds the invariant's
   ≤1px spacing tolerance in either direction. Left open/unresolved by
   user decision; out of budget to correct even if it turns out to be
   accidental drift.
5. **`cj-game-table`, `cj-functionality-table`, `cj-definition`,
   `cj-sortkey`** -- hand-authored class names with no matching CSS rule
   in either theme file, rendering off Bootstrap's bare `.table` default.
   Treated as intentional by user decision, not a gap.
6. **`$nav-tabs-link-active-color`/`$nav-tabs-link-active-bg`, dark-theme
   only** -- plausible explanation (Bootstrap's un-overridden active-tab
   default likely already reads fine against the light theme's near-white
   background, but would clash against dark's near-black one), still
   unconfirmed. This pass's tabset screenshot check (`statement @ 1280px
   [mode] second tab open`) verified that *this refactor's own edits*
   don't disturb tab styling -- it did not investigate the asymmetry
   itself, since neither `$nav-tabs-link-active-*` variable was touched.
   Still open.
7. Every other finding in `audits/2026-08-17-site-audit.md` (missing
   accessible names on nav/sidebar controls, duplicate `id`s, missing
   `og:image`, etc.) is pre-existing, unrelated to CSS consistency, and
   out of scope for this pass. Not touched, not newly introduced.
