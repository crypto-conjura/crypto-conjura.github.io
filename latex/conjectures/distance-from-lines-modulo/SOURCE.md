# Provenance: Distance from Lines Is Resilient to Reduction Modulo a Random Prime

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **From OT to OLE with Subquadratic Communication**
- Authors: Jack Doerner, Iftach Haitner, Yuval Ishai, Nikolaos Makriyannis
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/1722
- Bibliographic detail: inferred
- File: `2025-1722.pdf` (81 pages)
- sha256: `573a449ccbee1abcbc4f780952fafc44e2921dd2207dc668b5e853928979fd4c`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Numbered Conjecture 5.37 of the source, described there as a natural but apparently new number-theoretic conjecture whose study may be of independent interest. Nothing is proved about it. The source notes a deterministic variant might be easier to prove and is still useful.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 42 | 42 | exact (100%) | Namely, α measures how far f is, in expectation, from being a linear function over S, where α bκ measures how far it is from being a linear function modulo a un... |
| openness | 6 | 6 | exact (100%) | The security of this variant reduces to a natural but apparently new number-theoretic conjecture (see Conjecture 5.37) whose study may be of independent interes... |
| openness | 42 | 42 | exact (100%) | We note that the deterministic variant of Conjecture 5.37, where the max in the definition of δκ,ℓ is only taken over deterministic f , which might be easier to... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is numbered and verbatim, and the paper is explicit that it is unproved. The one substantive defect is in the source itself: the difference in Definition 5.36 is printed in the order that makes the quantity non-positive, so the statement is typeset in the direction the rest of the paper requires and the discrepancy is documented in a remark rather than passed on silently.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 42 | Conjecture 5.37 and Definition 5.36 are printed on PDF page 42 (paper page 39) and were re-read off the rendered page, not the text layer. |
| openness | pass | 42 | Stays open: no proof, no partial result, and the deterministic variant is offered as possibly easier rather than as proved. |
| strength | fail | 42 | Definition 5.36 as printed takes max{alpha_hat - alpha}. For any fixed prime p and any fixed (a,b), agreement over Z implies agreement mod p, so the mod-p Hamming distance is pointwise at most the integer one; minimising over (a,b) after seeing p only lowers it further, hence alpha_hat <= alpha always and the printed quantity is non-positive. The conjecture as literally printed is therefore vacuous. Corrected to alpha - alpha_hat, the direction the conjecture's title, the source's own gloss and its Theorem 5.39 all require, with the discrepancy stated in a remark rather than silently fixed. |
| quantifiers-and-parameters | pass | 42 | Quantifiers reproduced exactly: minimum over a,b in N outside the expectation over r for alpha; expectation over p outside the minimum for alpha_hat; maximum over S and f last; the conjecture's 'for all kappa and all n <= 2^{c_n kappa}'. |
| attribution | pass | 42 | Conjecture 5.37 is the harvested paper's own and is described there as apparently new. |
| definitions | fail | 10 | The source writes the second subscript as ell in Definition 5.36 and as n in Conjecture 5.37 and Theorem 5.39. Recorded: the index is the domain parameter, written n throughout. Also: (n) = {0,...,n} is the source's own Section 3.1 notation and is stated rather than assumed, and Ham is defined in the source for bit vectors but applied to vectors over (n), which the draft notes. |
| fabrication | pass | - | No fabrication. The draft does not claim any partial result, and it attributes the deterministic-variant observation to Remark 5.40. |
| self-containment | pass | - | Self-contained once (n), P_kappa and Ham are given, which the draft does. |

### Corrections the checker asked for

- **definitions_latex** — The printed order of the difference in Definition 5.36 makes delta_{kappa,n} non-positive and the conjecture vacuous.
  - suggested: Define delta_{kappa,n} := max_{S,f}(alpha - alpha_hat_kappa) and add a remark giving the one-line proof that the printed order is non-positive, together with the three reasons (title, gloss, Theorem 5.39) that the reversed order is the intended one.
- **notation_latex** — Subscript written ell in the definition and n in the conjecture.
  - suggested: Use n throughout and say so in the same remark.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The direction of the difference. The source's Definition 5.36 prints max{alpha_hat - alpha}, which is non-positive for every f and S, making the conjecture vacuous as printed; the direction that its title, its gloss and its Theorem 5.39 all require is alpha - alpha_hat. This is flagged in a dedicated remark and is the single thing a reviewer should check hardest.

