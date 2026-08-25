# Provenance: Malicious NISC with Constant Communication Overhead from a Black-Box PRG

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Non-Interactive Secure Computation with Constant Communication Overhead**
- Authors: Yuval Ishai, Ziyang Jin, Naty Peter, Akshayaram Srinivasan
- Venue/archive: IACR ePrint 2026
- Identifier: IACR ePrint 2026/1555
- Bibliographic detail: inferred
- File: `2026-1555.pdf` (75 pages)
- sha256: `58b4fff565663b51052f29f1080e4e50e3526e36fcd6db1c33b8a9e2863112c5`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. The source poses this question and then answers the variant in which the PRG is replaced by a random oracle (its Theorem 1.1), which leaves the question as posed unresolved. Every single relaxation of it is already known: polylogarithmic overhead, correlated-abort security, more rounds, or programmable OLE correlations.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 2 | 2 | exact (100%) | Is there a malicious-secure NISC protocol with communication cost O(\|C\|λ) assuming random OT |
| openness | 2 | 2 | exact (100%) | The above state of the art leaves the following natural question open: |
| openness | 3 | 3 | exact (100%) | For the question above, we show that if we replace a PRG by a random oracle, we can indeed close the above gap. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The question is displayed verbatim on page 2 and the source answers only the random-oracle variant of it, which strengthens rather than weakens the hypothesis. The one thing needing care -- and given a dedicated remark -- is that a reader must not take Theorem 1.1 for a resolution.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 2 | The question is set as its own display on page 2, introduced by 'The above state of the art leaves the following natural question open'. |
| openness | fail | 3 | The paper does answer a version of its own question: 'if we replace a PRG by a random oracle, we can indeed close the above gap'. Checked whether that settles the question as posed -- it does not, since a random oracle is a stronger hypothesis than black-box use of a PRG, and the source does not claim otherwise. Recorded as the central thing a reader must not misread, in its own remark, and reflected in the status line. |
| strength | pass | 2 | Strength matches the displayed question exactly: malicious-secure, O(\|C\| lambda), random OT correlations, black-box PRG. |
| quantifiers-and-parameters | pass | 3 | Checked that Theorem 1.1's security is standard rather than correlated-abort (Table 1 confirms), so the drafted statement must ask for standard security too. |
| attribution | pass | 2 | The question is the harvested paper's own; each prior result in the comparison is attributed as the paper's Table 1 attributes it. |
| definitions | pass | 2 | 'Correlated abort' is used in the source's sense (the sender can force an abort depending on a predicate of the receiver's input), which is what makes it a weaker notion. |
| fabrication | pass | 3 | No fabrication. The two places the oracle is used -- Fiat-Shamir for the watchlist, and the Ligero-style commitments -- are read off the source's Section 2, not guessed. |
| self-containment | pass | - | Self-contained: two messages, an OT-correlation setup, and a communication bound. |

### Corrections the checker asked for

- **status_note** — Must not read as though the source leaves the question wholly untouched.
  - suggested: State that the source answers the random-oracle variant and that this leaves the question as posed unresolved, and give the same point its own remark.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That this is not settled by the source's own Theorem 1.1: replacing a black-box PRG with a random oracle strengthens the assumption. And that all four of the tight constraints (constant overhead, standard rather than correlated-abort security, two messages, OT rather than OLE correlations) are held fixed at once -- dropping any one makes the statement a known result.

