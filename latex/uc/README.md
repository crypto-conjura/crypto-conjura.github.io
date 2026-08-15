# UC Encyclopedia drafts (local only)

One folder per UC ideal functionality, mirroring the site's structure at
`uc/layer-N-.../<functionality-slug>/` exactly:

```
latex/uc/layer-0-idealized-setup/f-crs/main.tex
latex/uc/layer-0-idealized-setup/f-acrs/main.tex
...
latex/uc/layer-8-time-application/f-vote/main.tex
```

All 100 already exist with a skeleton `main.tex` (title filled in,
Abstract/Functionality/Known Realizations/Properties/Formal Artifacts
sections stubbed out with comments) — write the real content directly
into the matching file rather than creating new ones, so the folder
layout stays in exact 1:1 correspondence with the site's `uc/` tree.

Each skeleton compiles as-is (`pdflatex main.tex`) — verified for the
whole batch before committing.

## Publishing a draft

When a functionality's write-up is ready, ask Claude to regenerate its
site page (`uc/layer-N-.../<slug>/index.qmd`) from this file's content —
same process as publishing a conjecture or paper draft (see the parent
`latex/README.md`), just for a UC functionality instead.
