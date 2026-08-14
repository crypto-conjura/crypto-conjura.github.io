# Conjura

An open archive of unresolved conjectures in cryptography, precise write-ups that don't necessarily resolve a conjecture (clarifications of existing ideas, or corrections to gaps in existing papers), and reusable prompts/tooling for automating research in theoretical cryptography with AI assistance.

The site is built with [Quarto](https://quarto.org) and published to GitHub Pages via GitHub Actions on every push to `main`.

## Repository layout

```
open-problems/<topic>/<conjecture-slug>/   conjecture pages: statement, status, source, sessions
papers/<paper-slug>/                       write-ups that don't resolve a conjecture
prompts/                                   reusable prompts for research, proof-checking, writing
blog/posts/                                informal write-ups (and eventually podcasts/videos) for resolved conjectures
resources/                                 pdfs/books used as reference material, not rendered on the site
```

Each conjecture or paper folder follows the same template:

- `index.qmd` — the rendered page
- `latex/` — original `.tex` source, `.bib`, figures, if imported from an existing paper
- `pdf/` — compiled PDF
- `sessions/` — dumps of prompt/agent research sessions, kept for provenance, excluded from the site

Copy `open-problems/lattices/example-conjecture/` or `papers/example-paper/` as a starting template.

## Contributing

- **New conjecture, paper, or prompt** — open a pull request adding the relevant files, and add the new page to `_quarto.yml`'s sidebar.
- **Gap in a proof, or discussion of a conjecture** — open an issue.

## Local development

```
quarto preview
```

requires the [Quarto CLI](https://quarto.org/docs/get-started/) installed locally.
