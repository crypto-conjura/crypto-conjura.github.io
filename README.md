# Conjura

[![Publish site](https://github.com/crypto-conjura/crypto-conjura.github.io/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/crypto-conjura/crypto-conjura.github.io/actions/workflows/publish.yml)

An open archive of unresolved conjectures in cryptography, precise write-ups that don't necessarily resolve a conjecture (clarifications of existing ideas, or corrections to gaps in existing papers), and reusable prompts/tooling for automating research in theoretical cryptography with AI assistance.

The site is built with [Quarto](https://quarto.org) and published to GitHub Pages via GitHub Actions on every push to `main`.

## Repository layout

```
c/<id>/                      statement leaves: one precise proposition, one Lean declaration
p/<slug>/                    problem hubs: one informal question, provenance, parameter lattice
papers/<paper-slug>/         write-ups that don't resolve a conjecture
surveys/<survey-slug>/       book-length expository work, with its own latex/ and pdf/
uc/layer-N-<slug>/<id>/      UC encyclopedia: one page per ideal functionality
open-problems/               generated facet listings (areas/model/form/assumption_class) + status legend
prompts/                     reusable prompts (research, proof-checking, writing), one Markdown file each
resources/                   reusable supporting material; books/ and papers/ hold local reference PDFs
schema/                      the frontmatter contract, for humans and agents
vision/                      why Conjura exists and where it's headed
philosophy/                  the reasoning under the site's choices, plus audio/ readings of it
latex/                       working drafts, staged here before they become a site page
scripts/                     the four CI gates: badges, facet index, relation graph, UC boxes
_templates/                  copy-paste skeletons for a new statement or problem
_listing-templates/          the table template the statement listings render through
_generated/, conjura.json    build_index.py output; gitignored, rebuilt by CI before every render
.githooks/, .github/         the pre-commit hook, and the publish and checks workflows
```

There is no `blog/` yet. It was dropped from the navbar and the sidebar on 2026-08-16 because no posts existed, and it returns to both once there is real content to put in it.

Topic (`areas`) is a tag a statement carries, never a home directory -- see `/schema/` for the full frontmatter contract and `CONTRIBUTING.md` for how to add a statement or a problem.

Each statement or paper folder follows the same convention:

- `index.qmd` -- the rendered page
- `latex/` -- original `.tex` source, `.bib`, figures, if imported from an existing paper
- `pdf/` -- compiled PDF
- `lean/` -- the Lean artifact, when the statement has one
- `sessions/` -- dumps of prompt/agent research sessions, kept for provenance, excluded from the site

Copy `_templates/statement.qmd` (or `_templates/problem.qmd`, or `papers/example-paper/`) as a starting template.

## Contributing

See `CONTRIBUTING.md` for the full workflow (identifier allocation, the same-id-vs-new-id revision rule, adding a statement or a problem). In short:

- **New statement, problem, paper, or prompt**: open a pull request adding the relevant files, after running the local checks below.
- **Gap in a proof, or discussion of a conjecture** -- open an issue.

## Local development

```
pip install -r requirements.txt
git config core.hooksPath .githooks  # once per clone: run the checks below pre-commit
python3 scripts/status_badge.py     # regenerate badges + statement_sha
python3 scripts/build_index.py      # validate schema, emit _generated/ + conjura.json
python3 scripts/check_relations.py  # validate the relation graph
python3 scripts/gen_interface.py    # regenerate the UC functionality boxes
quarto preview                      # facet listings need build_index.py to have run first
```

The `core.hooksPath` line enables `.githooks/pre-commit`, which runs the same
four checks the publish workflow gates on. It matters because those checks run
*before* `quarto render` in CI: a stale `statement_sha` fails the whole job, so
one unregenerated edit blocks the site deploy on every push after it, not just
its own. Editing prose inside a `## Statement` block is enough to cause this --
the block is hashed. Bypass a single commit with `git commit --no-verify`.

requires the [Quarto CLI](https://quarto.org/docs/get-started/) installed locally.
