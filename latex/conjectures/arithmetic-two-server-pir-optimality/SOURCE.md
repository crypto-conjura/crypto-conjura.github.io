# Provenance: Optimality of Cube-Root Communication for Two-Server Arithmetic PIR

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **On Arithmetic Private Information Retrieval: Why Code-Based PIR (Usually) Fails**
- Authors: Benny Applebaum, Yuval Ishai, Shahar Shechter
- Venue/archive: IACR ePrint 2026
- Identifier: IACR ePrint 2026/1224
- Bibliographic detail: inferred
- File: `2026-1224.pdf` (43 pages)
- sha256: `8a6053190cf0221ab77a129cbf6651f4c2075a90b42d20ac8ae723fd8c2644f3`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. O(n^{1/3}) is achieved by arithmetizing the classical two-server schemes. The source states that whether it can be improved -- let alone brought to sub-polynomial -- is unknown, and supplies a linear-algebraic characterization of what an improvement would require.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 5 | 5 | exact (100%) | At present, it is unknown whether one can improve upon the O(n1/3 ) communication bound, let alone achieve sub-polynomial communication, in the arithmetic setti... |
| openness | 1 | 1 | exact (100%) | The optimality of this result remains an interesting open question. |
| openness | 4 | 4 | exact (100%) | However, we do not know how to arithmetize the best existing binary schemes [35, 5], |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open question is verbatim and the linear-algebraic reformulation is the source's own Theorem 5.3. Two repairs: the informal version of that theorem was replaced by the formal one, and three citation groups were reassigned against the source's own bracketed references.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 5 | The open question is stated on page 5 and again in the abstract ('The optimality of this result remains an interesting open question'). |
| openness | pass | 5 | Stays open: it appears after the O(n^{1/3}) construction and after Theorem 5.3, and nothing in Sections 5-6 resolves it. |
| strength | pass | 5 | Strength matches: the source asks whether O(n^{1/3}) can be improved, so the draft poses both directions rather than picking one. |
| quantifiers-and-parameters | fail | 19 | The draft first reproduced Informal Theorem 1.4's four conditions, including a support-size bound. Theorem 5.3's formal version has three, with the two-step sampling condition implying the support bound (the source says so in a footnote). Corrected to the formal version. |
| attribution | fail | 4 | Citation groupings had to be fixed against the source's own text: the classical schemes that arithmetize are [25,14,63] = CGKS, BIK, WY; the unarithmetizable binary schemes are [35,5] = Dvir-Gopi and Alon-Beimel-Lasri; the prior linear-PIR studies are [39,36] = GKST and Dvir-Shpilka. An earlier draft had Chor-Gilboa and Beimel-Ishai-Kushilevitz-Orlov in those roles. |
| definitions | pass | 20 | 'Arithmetic', 'finite degree' and 'fully linear' are used in the source's senses, and the Woodruff-Yekhanin arithmetization is described as the source describes it. |
| fabrication | pass | - | No fabrication after the citation corrections. The single-server impossibility, the two-server computational result and the secret-key result are attributed to the source's own informal theorems. |
| self-containment | pass | - | Self-contained: the linear-algebraic form needs no cryptographic background at all. |

### Corrections the checker asked for

- **definitions_latex** — Used the informal version of the equivalence rather than Theorem 5.3.
  - suggested: State Theorem 5.3's three conditions, with the two-step sampling condition in place of the separate support-size bound.
- **bibliography** — Three citation groups misassigned.
  - suggested: Classical arithmetizing schemes: CGKS, BIK, WY. Unarithmetizable binary schemes: Dvir-Gopi, Alon-Beimel-Lasri. Prior two-server linear PIR: GKST, Dvir-Shpilka. Bilinear lower bound: Razborov-Yekhanin.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the equivalence is stated for perfect security and finite degree, where it is clean, and that the relaxations the source records (statistical privacy, statistical correctness, division gates via Remark 5.4) are named as relaxations rather than folded in. Also that a Boolean database changes the question: the source notes matching-vector PIR is linear over a small field when the database is Boolean, with a non-linear decoder.

