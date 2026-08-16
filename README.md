# Conjura

An open archive of unresolved conjectures in cryptography, precise write-ups that don't necessarily resolve a conjecture (clarifications of existing ideas, or corrections to gaps in existing papers), and reusable prompts/tooling for automating research in theoretical cryptography with AI assistance.

The site is built with [Quarto](https://quarto.org) and published to GitHub Pages via GitHub Actions on every push to `main`.

## Repository layout

```
c/<id>/                     statement leaves: one precise proposition, one Lean declaration
p/<slug>/                   problem hubs: one informal question, provenance, parameter lattice
open-problems/               generated facet listings (areas/model/form/assumption_class) + status legend
schema/                      the frontmatter contract, for humans and agents
_templates/                  copy-paste skeletons for a new statement or problem
papers/<paper-slug>/         write-ups that don't resolve a conjecture
prompts/                     reusable prompts (research, proof-checking, writing), one Markdown file each
blog/posts/                  informal write-ups (and eventually podcasts/videos) for resolved conjectures
resources/                   pdfs/books used as reference material, not rendered on the site
```

Topic (`areas`) is a tag a statement carries, never a home directory -- see `/schema/` for the full frontmatter contract and `CONTRIBUTING.md` for how to add a statement or a problem.

Each statement or paper folder follows the same convention:

- `index.qmd` — the rendered page
- `latex/` — original `.tex` source, `.bib`, figures, if imported from an existing paper
- `pdf/` — compiled PDF
- `sessions/` — dumps of prompt/agent research sessions, kept for provenance, excluded from the site

Copy `_templates/statement.qmd` (or `_templates/problem.qmd`, or `papers/example-paper/`) as a starting template.

## Contributing

See `CONTRIBUTING.md` for the full workflow (identifier allocation, the same-id-vs-new-id revision rule, adding a statement or a problem). In short:

- **New statement, problem, paper, or prompt**: open a pull request adding the relevant files, after running the local checks below.
- **Gap in a proof, or discussion of a conjecture** — open an issue.

## Local development

```
pip install -r requirements.txt
python3 scripts/status_badge.py     # regenerate badges + statement_sha
python3 scripts/build_index.py      # validate schema, emit _generated/ + conjura.json
python3 scripts/check_relations.py  # validate the relation graph
quarto preview                      # facet listings need build_index.py to have run first
```

requires the [Quarto CLI](https://quarto.org/docs/get-started/) installed locally.
