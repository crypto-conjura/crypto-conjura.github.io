# To-dos

## 1. Three-tab conjecture pages

Restructure every conjecture page (`open-problems/<topic>/<slug>/index.qmd`) so its content is presented as three tabs, using Quarto's tabset syntax (`::: {.panel-tabset}` with a `## Tab Title` heading per tab):

1. **Statement** — the conjecture statement exactly as the page reads today (the existing rendered Markdown/math body), plus download links for the *statement's* `.tex` source and compiled PDF (already present under each conjecture's `latex/` and `pdf/` folders, e.g. `latex/main.tex` / `pdf/main.pdf`).
2. **Proof** — a written overview of the proof (or best-known proof attempt/sketch), plus download links for a `.tex` source and compiled PDF *of the proof*. This is new, separate content from the statement's tex/pdf, so each conjecture folder needs a second tex/pdf pair (e.g. `latex/proof.tex` / `pdf/proof.pdf`).
3. **Formal Artifact** — a link to a machine-checked Lean proof. Each conjecture already links to a Lean *statement* (`lean/Statement.lean`, done), sitting as a plain link alongside the PDF/LaTeX links; what's left here is moving that link into its own tab, and adding a "no proof yet" placeholder state for the (eventual, separate) proof artifact, since none of these conjectures are resolved yet.

Update the template (`open-problems/lattices/example-conjecture/`) first, then the three real write-ups (`open-problems/symmetric-key/k-collisions-auxiliary-input/`, `feistel-6-round-indifferentiability/`, `generalized-mirror-theory/`) to match, including any `_metadata.yml`/frontmatter changes needed to support the new folder layout.

## 2. Tag papers by topic

Conjectures are already tagged this way — done: each conjecture carries a `categories: [...]` frontmatter field naming one or more of the 19 preselected topics, and each topic's `index.qmd` is a Quarto `listing` auto-filtered by category, decoupled from which folder the conjecture physically lives in.

Papers don't have this yet (deliberately deferred — there's only one, a template, so far):

- `papers/example-paper/index.qmd` already has the `categories: []` field scaffolded in; populate it the same way conjectures do once there's real content to tag.
- Decide whether papers get their own per-topic listing pages (mirroring `open-problems/<topic>/index.qmd`), or a single `categories: true` filterable listing on `papers/index.qmd` (mirroring how `blog/index.qmd` already does it) — revisit once there's more than one real paper to justify either.
