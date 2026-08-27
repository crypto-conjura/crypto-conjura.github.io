# Provenance: The Online Threshold for Contracting Hypergrid Vectors

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Adaptive Robustness of Hypergrid Johnson-Lindenstrauss**
- Authors: Andrej Bogdanov, Alon Rosen, Neekon Vafa, Vinod Vaikuntanathan
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/666
- Bibliographic detail: inferred
- File: `2025-666.pdf` (37 pages)
- sha256: `91774104adbdec2004bac7a6bbcdbd7634f50e566c2dd6312c65109032d6ba64`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Conjecture 1 of the source, its 'online threshold conjecture'. The source gives an online algorithm achieving kappa = O(sqrt(alpha)/B) and an overlap-gap argument against stable algorithms; the conjecture pins the constant sqrt(pi/8) as the exact place where online algorithms stop.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 16 | 16 | exact (100%) | For every δ and B there exists a sufficiently small α |
| informal | 6 | 6 | exact (100%) | In general, we conjecture p √ that no online algorithm can succeed when κ is at most |
| caveat | 6 | 6 | exact (100%) | We believe that some assumption of this type is necessary for an OGP-based argument to ensure stability. |
| neighbour | 7 | 7 | exact (100%) | We leave it as a fascinating open question as to whether this lower bound can be improved to match that of Theorem 3 or similar. |
| constant | 16 | 16 | exact (100%) | The drift pushes U towards the fixed point |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 1 is verbatim on page 16 and is transcribed as printed. One correction is recorded in the statement rather than applied: immediately before stating it the source notes its OGP argument assumes the algorithm is committed to the approximate norm of x before seeing A, and says some such assumption is likely necessary -- but Conjecture 1 as printed quantifies over 'every online algorithm' without repeating that condition. The statement flags the discrepancy and asks a resolution to say which reading it settles, rather than silently narrowing the source's wording.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
