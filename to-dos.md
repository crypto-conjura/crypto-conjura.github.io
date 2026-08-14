# To-dos

## 1. Tag papers by topic

Give papers the same tag treatment conjectures already have:

- `papers/example-paper/index.qmd` already has the `categories: []` field scaffolded in; populate it once there's real content to tag.
- Decide whether papers get their own per-topic listing pages (mirroring `open-problems/<topic>/index.qmd`), or a single `categories: true` filterable listing on `papers/index.qmd` (mirroring `blog/index.qmd`) — revisit once there's more than one real paper to justify either.

## 2. UC Encyclopedia content

Every one of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) is still a stub. Fill in real content incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts.

## 3. Sync corrected citations into LaTeX/PDF sources

The three real conjecture pages under `open-problems/symmetric-key/` (`generalized-mirror-theory`, `feistel-6-round-indifferentiability`, `k-collisions-auxiliary-input`) had several citations in their `index.qmd` that were fabricated or misattributed (e.g. "Ito et al., 2021" didn't correspond to any real paper; "Dai et al. (2018)" was actually Mandal–Patarin–Seurin 2012). These were corrected and linked to free versions in the `.qmd` pages, but the mirrored `latex/main.tex` sources (and their compiled `pdf/main.pdf`) still have the old, incorrect citation text — recompile once `hyperref` links are wanted there too.
