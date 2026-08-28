# Provenance: Quasi-Abelian Codes Meet the Gilbert-Varshamov Bound as the Group Grows

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Correlated Pseudorandomness from the Hardness of Quasi-Abelian Decoding**
- Authors: Maxime Bombar, Geoffroy Couteau, Alain Couvreur, Clément Ducros
- Venue/archive: IACR ePrint / CRYPTO 2023
- Identifier: IACR ePrint 2023/845
- Bibliographic detail: printed-in-source-bibliography
- File: `2023-845.pdf` (51 pages)
- sha256: `8db4c36ac220de2172539fbd14e34ecf86929f077fa8c2d9ae4969133ff4ef34`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. The source names the direction twice and prints no formal statement, saying the development is out of reach of the article and it leaves it as a conjecture. Two neighbouring regimes are theorems: Fan and Lin for fixed group and growing index, including the modular case, and Gaborit and Zemor for growing group but cyclic only. The regime the cryptographic parameters live in -- constant k and l, growing |G|, arbitrary abelian G -- is neither.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 9 | 9 | exact (100%) | We conjecture an extension of Gaborit and Zémor result to arbitrary abelian groups. The latter conjecture entails that the QA-SD problem cannot be broken by any... |
| openness | 20 | 20 | exact (100%) | Actually, to assert the resistance of QA-SD against linear attacks, it would be more relevant to consider the regime where k, ℓ are constant and \|G\| goes to i... |
| known-cyclic | 9 | 9 | exact (100%) | On the other hand, Gaborit and Zémor [GZ06] prove a similar result when the size of the group goes to infinity but restricted to the case where the group is cyc... |
| known-fanlin | 9 | 9 | exact (100%) | On one hand, a recent result of Fan and Lin [FL15] proves that quasi-Abelian codes asymptotically meet the Gilbert-Varshamov bound when the code length goes to ... |
| wrong-regime | 20 | 20 | exact (100%) | As it is often the case in coding theory, this result is stated asymptotically, but the convergence speed could be made more precise, the exponent depends on \|... |
| caveat | 20 | 20 | exact (100%) | In this case, the minimum distance could drop, but heuristically a random quasi-G code will have a minimum distance linear in its length as long as this bias is... |
| bias | 19 | 19 | exact (100%) | Therefore, when this ideal is not the full ring, there is an obvious bias. |
| hardness | 19 | 19 | exact (100%) | Those problems, especially their search version, have been studied for over 50 years by the coding theory community and to this day, no efficient algorithm is k... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

All eight quotes ground exact, with two page claims corrected by the grounder (Remark 18 and the fifty-years-of-study remark are on page 19, not 20). Existence and openness are clear and stated twice in the source's own voice. The correction that matters is on strength: the source prints no formal statement of the conjecture, so the formalisation is this page's and is flagged as such in its own remark, together with the two choices it makes -- the plain GV threshold rather than the logarithmic improvement, and the systematic form. Confidence is medium rather than high for exactly that reason. The distinction between the two asymptotic regimes was checked clause by clause against Theorem 20 as printed, since conflating them is the obvious way for a draft of this to be wrong. A forward literature check on 28 August 2026 found substantial recent progress (ePrint 2026/939) which does not settle it and which restates the conjecture as open; that follow-up is cited and marked UNVERIFIED because it postdates the source and is not in its reference list.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `LLXYY26` — Zhe Li, Hongqing Liu, Chaoping Xing, Yizhou Yao and Chen Yuan, *More efficient SNARKs via quasi-abelian codes*, IACR ePrint 2026/939 — found by literature search on 28 August 2026, not read off the source's reference list, which predates it. The bibliographic details were read off the ePrint PDF itself, but no third party has checked them.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

The formalisation on the page is not printed in the source, which names the direction and stops, so this is the largest editorial step in the batch and should be read as this statement's reading. Two choices in particular. It asks for the plain Gilbert-Varshamov threshold rather than the logarithmic improvement Gaborit and Zemor actually prove for double-circulant codes, on the grounds that the weaker target is what the linear-test reduction needs. And it fixes the systematic form, without which the statement is false. A proof of the stronger form, or a proof for a restricted family of abelian groups, is progress and should be reported as such rather than as a resolution.

