# Working LaTeX drafts (local only)

This folder holds in-progress LaTeX documents — papers and conjectures — that
aren't ready for the site yet. It's excluded from git (`/latex/` in
`.gitignore`), so nothing here ever reaches GitHub or the published site.

```
latex/papers/         working paper drafts
latex/conjectures/    working conjecture drafts
latex/uc/             working UC functionality drafts (see latex/uc/README.md)
```

Drop `.tex` files (and any `.bib`/figures) directly in the relevant subfolder,
organized however is convenient while drafting — except `latex/uc/`, which
already has one pre-made folder + skeleton `main.tex` per UC functionality,
mirroring the site's `uc/layer-N-.../<slug>/` structure exactly; write into
those rather than creating new ones.

## Starting a new conjecture with the Conjura house style

`latex/conjectures/_template/` holds two small LaTeX classes
(`conjura-conjecture.cls`, `conjura-solution.cls`) plus a matching empty
`statement.tex` and `solution.tex`, giving the Conjura look (Baskervald X,
orange accent, boxed definitions/conjectures, running heads) without
re-deriving the preamble each time. Copy the whole `_template/` folder to
`latex/conjectures/<new-slug>/` to start:

- `statement.tex` — the conjecture only: kicker/title/subtitle, a
  `Status`/`Category` line, an `informalconjecture` box, then the usual
  Setting → Conjectures → Bibliography sections. Narrow "screen" page —
  keep it short and curated.
- `solution.tex` — a proof or attempted proof for that statement, kept as
  its *own* document. Unbounded in length, no required structure beyond
  `\cjresolves{...}` at the top naming which conjecture it addresses.
  Wider, book-trim page to leave room for long derivations.

Both classes stay with the `.tex` files they came with — since class
resolution is directory-relative, copy the whole folder rather than the
`.tex` files alone.

## Publishing a draft

When a draft is ready to go live, ask Claude to generate its site page from
this folder's contents. That means:

- For a conjecture: create `open-problems/<topic>/<slug>/`, following the
  template in `open-problems/lattices/example-conjecture/` — the `.tex`
  source and compiled PDF move into that folder's `latex/` and `pdf/`
  subfolders (which *are* tracked on GitHub), and the statement gets
  transcribed into `index.qmd`.
- For a paper: same, but under `papers/<paper-slug>/`, following
  `papers/example-paper/`.
- For a UC functionality: regenerate `uc/layer-N-.../<slug>/index.qmd`
  from the matching `latex/uc/layer-N-.../<slug>/main.tex`.

The draft's `.tex` file can stay here afterwards or be deleted — it's no
longer the source of truth once it's copied into the tracked per-page
`latex/` folder (conjectures/papers) or transcribed into the site page
(UC functionalities, which don't currently have their own tracked `latex/`
subfolder on the site).
