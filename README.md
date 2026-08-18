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
problems/               generated facet listings (areas/model/form/assumption_class) + status legend
prompts/                     reusable prompts (research, proof-checking, writing), one Markdown file each
resources/                   reusable supporting material; books/ and papers/ hold local reference PDFs
schema/                      the frontmatter contract, for humans and agents
about/                       the site's position: where it's headed, and the reasoning underneath
latex/                       working drafts, staged here before they become a site page
scripts/                     the four CI gates: badges, facet index, relation graph, UC boxes
_templates/                  copy-paste skeletons for a new statement or problem
_listing-templates/          the table template the statement listings render through
_generated/, conjura.json    build_index.py output; gitignored, rebuilt by CI before every render
.githooks/, .github/         the pre-commit hook, and the publish and checks workflows
```

`blog/` holds one post and is hidden from the navbar and the sidebar as of 2026-08-16. The pages are still built and still resolve, so any link already pointing at one keeps working; they are only unadvertised. Both lists get a `Blog` entry back when it is wanted again.

Topic (`areas`) is a tag a statement carries, never a home directory -- see `/schema/` for the full frontmatter contract and `CONTRIBUTING.md` for how to add a statement or a problem.

Each statement or paper folder follows the same convention:

- `index.qmd` -- the rendered page
- `latex/` -- original `.tex` source, `.bib`, figures, if imported from an existing paper
- `pdf/` -- compiled PDF
- `lean/` -- the Lean artifact, when the statement has one
- `sessions/` -- dumps of prompt/agent research sessions, kept for provenance, excluded from the site

Copy `_templates/statement.qmd` (or `_templates/problem.qmd`, or `_templates/paper.qmd`) as a starting template.

## Licensing

Two licenses, split by what the file is:

- [`LICENSE-CODE`](LICENSE-CODE) (MIT) covers the tooling: `scripts/`,
  `.githooks/`, `.github/workflows/`, `_listing-templates/`, `_templates/`,
  the `.scss` themes, and the LaTeX document classes under
  `latex/conjectures/_template/`.
- [`LICENSE-CONTENT`](LICENSE-CONTENT) (CC BY 4.0) covers the writing:
  statement and problem pages under `c/` and `p/`, papers under `papers/`,
  surveys under `surveys/`, the UC encyclopedia under `uc/`, the prompts
  under `prompts/`, and the `schema/`, `about/` and `resources/` pages.

Lean artifacts under `c/<id>/lean/` are code, so MIT.

**Imported material is carved out.** Some `.tex` sources and PDFs under
`c/<id>/latex/`, `c/<id>/pdf/`, `papers/<slug>/latex/`, `papers/<slug>/pdf/`,
`surveys/<slug>/latex/`, `surveys/<slug>/pdf/` and `latex/` came from work with
co-authors or from published papers, and may carry third-party rights the
Conjura contributors cannot grant. Where that is so, the imported file's own
terms govern and `LICENSE-CONTENT` does not apply to it. See the final section
of that file. If you want to reuse something under one of those paths and it
is not obvious who holds the rights, ask first.

## Contributing

See `CONTRIBUTING.md` for the full workflow (identifier allocation, the same-id-vs-new-id revision rule, adding a statement or a problem). In short:

- **New statement, problem, paper, or prompt**: open a pull request adding the relevant files, after running the local checks below.
- **Gap in a proof, or discussion of a conjecture** -- open an issue.
- **A result that breaks something deployed** -- do not open either. See
  [`SECURITY.md`](SECURITY.md) and use private vulnerability reporting. Nearly
  nothing here is in that category, and the file says where the line is.

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
