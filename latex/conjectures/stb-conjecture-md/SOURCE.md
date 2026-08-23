# Provenance: The STB Conjecture for Short Collisions in Merkle-Damgård Hashing

Written by hand, following `prompts/harvest.md`, on 2026-08-23.
`scripts/harvest_conjectures.py` could not be used on this machine
(neither model backend was available: no `claude` CLI binary on `PATH`, no
Anthropic SDK, no API credentials), so the extract/verify/typeset steps were
carried out in-session instead. The two mechanical steps the pipeline owns
were still run: every quote below was grounded against the PDF's `pdftotext
-layout` text layer using `PdfDoc.ground` from `scripts/harvest_conjectures.py`
itself, and the build was checked with `pdflatex`, `chktex` and `lacheck`.
**Nothing here has been checked by a human.**

## Source

- Paper: **Time-Space Tradeoffs and Short Collisions in Merkle-Damgård Hash Functions**
- Authors: Akshima, David Cash, Andrew Drucker, Hoeteck Wee
- Venue/archive: CRYPTO 2020, Part I, LNCS 12170, pp. 157–186; IACR ePrint 2020/770
- Identifier: IACR ePrint 2020/770
- Bibliographic detail: printed-on-page
- File: `2020-770.pdf` (36 pages)
- sha256: `faac848be8ba953d2467016ebcdcee68f6b0bfdca8aac272510a1f6d7d5853fb`
- Read on 2026-08-23 in-session (no backend)

## How the paper leaves it open

`paper-conjectures`. The paper prints the conjecture as a displayed,
named statement ("STB conjecture", p. 2) and says on p. 1 that it "put[s]
forth and stud[ies]" it. It proves the conjecture's own lower-bound half
(Theorem 3, an attack) and proves the upper-bound half only at *B* = 2
(Theorem 7); on p. 5 it says *B* = 3 and *B* = 4 are possible "in
principle" but too long to write down, and that arbitrary *B* "seems to be
out of reach". Later literature narrows the open region to non-constant
*B* with *ST*² > *N*: Ghoshal–Komargodski (CRYPTO 2022) settled every
constant *B*, and Akshima–Guo–Liu (CRYPTO 2022) settled every 2 < *B* < *T*
with *ST*² ≤ *N*.

## Quotes, checked against the PDF text layer

Matched mechanically against `pdftotext -layout` output after undoing
ligatures, line-broken hyphens and curly quotes, using this repository's
own `ground()`. `exact` is a verbatim hit; `near` means the span is present
with a symbol mangled by the extractor.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 1 | 1 | exact (100%) | Concretely, we put forth and study the following conjecture: |
| statement | 2 | 2 | exact (100%) | The best attack with time T and space S for finding collisions of length B in salted MD hash functions built from hash functions with n-bit outputs achieves success probability |
| openness | 5 | 5 | exact (100%) | It appears that we could, in principle, obtain similar bounds for other small length bounds like 3 and 4, but these proofs would be too long and complex for us to write down; Going to arbitrary length bounds seems to be out of reach, but there is no inherent obstruction in applying our technique to the general case with new ideas. |
| hardness | 4 | 4 | exact (100%) | We show that the BF-to-AI template inherently cannot give a lower bound for finding short collisions, because finding short collisions in the BF-RO model is relatively easy. |
| significance | 6 | 6 | exact (100%) | Our STB conjecture, if true, would explain the non-existence of these attacks |
| partial | 2 | 2 | exact (100%) | They proved the STB conjecture in the setting B = T , showing an attack with success probability |
| definition | 6 | 6 | exact (100%) | Merkle-Damgård hashing is defined MDh : [N ] × [M ]+ → [N ] recursively by MDh (a, α) = h(a, α) for α ∈ [M ], and |

The displayed formula Θ((*STB* + *T*²)/2ⁿ) sits inside the statement quote
and was read from the rendered page rather than the text layer, which
flattens it; the prose either side of it grounds exactly, and the formula
was transcribed from the rendered page 2 and cross-checked against the two
verbatim restatements of the same conjecture in `2022-885.pdf` (p. 2) and
`2023-1444.pdf` (p. 8), which print it identically.

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium-high)

The conjecture is in the paper, printed and named, and is genuinely open in
the region the statement says it is. Three defects were found in the first
draft and repaired before this file was written; all three concern
*strength*, which is where the harvest prompt says a faithful-looking draft
is most often wrong.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 2 | Printed as a set-off, named statement ("STB conjecture") on p. 2, introduced on p. 1 by "we put forth and study the following conjecture". |
| Openness | pass | 5, 27 | Read past p. 2. §3 proves only the attack (Theorem 3). §4 proves the BF-model barrier. §6 proves the *B* = 2 upper bound (Theorem 7). §7 shows the Impagliazzo–Kabanets technique needs modifying. §8 proves the upper bound only against the restricted zero-walk class (Theorem 8), and says on p. 27 "It is tempting to conjecture such an attack is optimal for the bounded case ... and we are not aware of a better attack" — i.e. still a conjecture there too. §§9–11 are appendices proving Theorems 1, 3 and 7. Nothing in the paper settles general *B*. |
| Strength | **fail → corrected** | 2 | The paper's printed sentence carries **no range for *B***, and the first draft silently stated the conjecture for all *B* ≥ 1. That is false as stated: *B* = 1 is known to be Θ(*S*/*N* + *T*²/*N*) (Dodis–Guo–Katz, cited by the paper as [6]), not Θ(*ST*/*N* + *T*²/*N*). Corrected to 2 ≤ *B* ≤ *T* — the upper limit from the paper's own Theorem 3 — with Remark "the range of *B*" recording that the range is supplied rather than quoted, and citing the later restatement "for finding collisions of length *B* ≥ 2" in `2023-1444.pdf` p. 8 as support for the reading. |
| Quantifiers and parameters | **fail → corrected** | 8 | Theorem 3 delivers (*STB* − 96*S*)/(48 *N* log *N*), so the **literal Θ printed on p. 2 is not established even on its lower half** — it is short by a factor of log *N*. The first draft asserted the lower half as proved. Corrected: Theorem 3 is now reproduced verbatim as Theorem 1 of the statement, the text says the lower bound holds "up to a logarithmic factor", and Remark "whether the Θ is meant up to logarithmic factors" records that all later treatments use Ω̃/Õ and that the polylogarithmic reading is the intended one. The side conditions of Theorem 3 (*B* ≤ *T* < *N*/4, *STB* ≤ *N*/2, *M* ≥ *N*) are carried over unchanged. |
| Attribution | pass | 2, 3 | The conjecture is the harvested paper's own. The *B* = *T* case is correctly attributed to Coretti–Dodis–Guo–Steinberger ([3] in the paper), the *B* = 1 case to Dodis–Guo–Katz ([6]), the pre-sampling technique to Unruh ([15]) as tightened by [3], and the concentration technique to Impagliazzo–Kabanets ([13]). Ghoshal–Komargodski and Akshima–Guo–Liu postdate the paper and are flagged as such in the bibliography. |
| Definitions | pass | 6, 7 | Definition 1 (Merkle-Damgård) reproduces the paper's p. 6 definition clause for clause, including MD over [*M*]⁺ and "we refer to elements of [*M*] as blocks". Definition 2 (auxiliary-input collision resistance) reproduces the paper's Definition 1 and Definition 2 (p. 7), including that **h** and **a** are independent and uniform, that σ is computed from the whole table of *h*, and the (*S*,*T*,*B*) resource convention. One clarification added, not taken from the paper: that the three resource bounds hold "for every input and every oracle, not merely on average" — the paper's Definition 2 says "for any inputs and oracles" of the (*S*,*T*) case, so this is the paper's own convention made explicit. |
| Fabrication | **fail → corrected** | 27 | The first draft claimed the paper had "no account of why arbitrary *B* is hard". It has two, and both are now stated: Theorem 5 (p. 9), which proves the bit-fixing route cannot see collision length, and Theorem 8 (p. 28), which proves the conjecture's upper bound against all zero-walk adversaries up to a ln(*NB*) factor. The claim that Hellman's attack is "likewise only known to be optimal below the threshold *ST*² ≤ *N*" is attributed in the text to Akshima–Guo–Liu, whose open-problems section says it, and not to the harvested paper. |
| Self-containment | pass | – | Definitions 1 and 2 plus the notation list make the statement readable without the paper: a solver is told the exact quantity to bound, the resource conventions, the asymptotic convention, and which parameter regime is still open. |

### Unsupported by the paper, and marked as such on the page

- The range 2 ≤ *B* ≤ *T* in Conjecture 1 (the printed sentence gives none) — recorded in the remark "the range of *B*".
- The polylogarithmic reading of the Θ — recorded in the remark "whether the Θ is meant up to logarithmic factors".
- The regime boundary "non-constant *B* with *ST*² > *N*" for what remains open, which comes from Ghoshal–Komargodski and Akshima–Guo–Liu, both later than the source. Attributed to them in the text and in the status line.

### Citations not in the source paper's reference list

Three cited works postdate the source paper and therefore cannot appear in
its reference list. None is supplied from memory: each was read off a
printed reference list in another PDF in this same harvest batch, and the
bibliography entry says which.

- `AGL22` — details from the reference list of `2023-1444.pdf` (p. 32).
- `GK22` — details from the reference list of `2022-885.pdf` (p. 33).
- `ADGL23` — read from the paper itself (`2023-1444.pdf`, title page).

## Forward literature check, 2026-08-23

Searched for any post-2023 work proving or refuting the STB conjecture in
the region left open. Found none. The most recent relevant items located
were the *Journal of Cryptology* 37 (2024) version of Akshima–Guo–Liu and
Akshima's ITC 2024 paper on multi-collisions in Merkle-Damgård, whose own
open-problems section conjectures optimality of a *different* attack (for
*B* < log *m* multi-collisions) and treats the *STB* line as it stood.
**This is a targeted check, not an exhaustive sweep**, and a reviewer should
search for papers citing IACR ePrint 2020/770 before relying on "still
open".

## Build

- pdflatex: ok (3 passes, 0 LaTeX warnings)
- chktex: 0 warnings
- lacheck: 0 warnings
