# Provenance: Closing the Logarithmic Locality Gap for Almost k-Wise Independent Hashing

Read in-session following `prompts/harvest.md`, since `scripts/harvest_conjectures.py` could not run here (no CLI binary, no SDK, no credentials on this machine); quote grounding and the pdflatex/chktex/lacheck build were still run mechanically, from the script's own `PdfDoc.ground`, `check_candidate`, `compile_check` and `write_source_note`. Nothing here was checked by a human yet; this file is what the run believed and why.

## Source

- Paper: **Locally Computable High Independence Hashing**
- Authors: Yevgeniy Dodis, Shachar Lovett, Daniel Wichs
- Venue/archive: IACR Cryptology ePrint Archive 2026
- Identifier: 2026/622
- Bibliographic detail: inferred
- File: `2026-622.pdf` (22 pages)
- sha256: `4a54a528764b1ca6b481a7bd0555a25431296efee8a259e31479dedcf6ec9458`
- Read on 2026-08-24T21:45:33Z via the `in-session (no CLI binary, no SDK, no credentials on this machine)` backend

## How the paper leaves it open

`paper-states-open`. For w=1 and for w=Ω(log^2 k + log^2 n) up to n^2, the paper proves a locality lower bound of Ω(n/(√w log n)) (Theorem 5.1, specialized to output length n, error 2^{-n}, k=poly(n)) and gives an explicit construction achieving locality O(n/√w) (Theorem 5.7 at w=1, Theorem 5.10 for w=Ω(log^2 k+log^2 n)); the two match only up to a Θ(log n) multiplicative factor, and closing this gap in either direction is left open. For 2≤w=o(log^2 n), no explicit construction matching the lower bound is given by the paper at all -- that intermediate range is the subject of a separate, distinct remark in the paper about unifying the bit-local and word-local constructions, not part of this open problem.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| openness | 20 | 20 | near (100%) | Another open problem is to close the logarithmic gaps between the lower bounds and explicit constructions of almost-independent hashing when the input and outpu... |
| statement | 20 | 20 | near (100%) | In the case of hash functions having input and output size n and statistical error ε = 2−n, our constructions are nearly optimal we provide almost matching lowe... |
| progress | 12 | 12 | exact (100%) | Below we give a lower bound on the locality of ε-almost-independent hash functions. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: 0.85)

The paper genuinely poses and leaves open 'closing the logarithmic gap' for almost-k-wise-independent locality when input/output size is n and ε=2^-n (Section 6, page 20), so the core problem is real. However, the draft's formal statement claims the O(n/√w) upper-bound construction is established uniformly for all 1 <= w <= n^2, when Theorem 5.10 explicitly requires w = Ω(log^2 k + log^2 n) (confirmed both in the theorem itself, page 18, and in the paper's own results summary, page 4) and Theorem 5.7 only covers w=1; the draft has silently imported its word-size range from the paper's separate, second open problem (unifying the bit-local and word-local constructions, page 20) and attached it to the log-gap problem, which the paper itself states without any such range.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 20 | Section 6 (physical page 20 of 22): 'Another open problem is to close the logarithmic gaps between the lower bounds and explicit constructions of almost-independent hashing when the input and output size is n and the error is ε = 2−n.' This is an exact match for the draft's 'openness' quote. |
| openness | pass | 20 | This sentence occurs in Section 6, 'Summary and Open Problems', which is the last technical section of the paper (only the reference list follows, pages 19-22 physical / 17-20 printed). Nothing later in the paper resolves it; it stays open through the end of the document. |
| strength | fail | 20 | The paper's own open-problem sentence (page 20) carries no word-size range at all. The very next sentences in the same Section 6 paragraph pose a DIFFERENT, separate open problem: 'currently we have two separate but related constructions for almost independent hashing: one for bit-local hash functions and one for word-local hash functions. It would be nice to unify them into a single construction that works for all word sizes 1 ≤ w ≤ n^2.' The draft's formal statement takes the range '1 <= w <= n^2' from this second, distinct unification problem and grafts it onto the first (log-gap) problem, presenting a single formal statement that conflates the two. This is a strengthening/distortion of what the paper actually poses as the log-gap problem's domain. |
| quantifiers-and-parameters | fail | 18 | Theorem 5.10 (page 18) has the standing hypothesis 'w = Ω(log^2 k + log^2 n)' (with k = poly(n), so effectively w = Ω(log^2 n)) — this is required for the WHOLE theorem, including all of its internal case splits (w ≤ min(k^2,n^2), w > k^2, w ≥ n^2). This is reaffirmed in the Introduction's own summary (page 4): 'In the word model with sufficiently large word size w = Ω(log^2 n + log^2 k), we get optimal key [size]...' The only other explicit construction is Theorem 5.7 (page 15), which covers exactly w=1 (the bit model), giving t=O(n) = O(n/√1). For 2 ≤ w = o(log^2 n), the paper gives NO construction achieving O(n/√w) locality — that gap is exactly what the paper's separate 'unify into a single construction... for all word sizes 1 ≤ w ≤ n^2' remark (page 20) is about. The draft's t_ub(n,w) = O(n/√w) is therefore not established uniformly for 1 <= w <= n^2 as claimed; it is established only at w=1 and for w = Ω(log^2 n) up to n^2. Secondarily (page 11), Theorem 5.1's specialization 't ≥ Ω(n/(√w log n))' additionally requires the standing hypothesis 'k > tw/n + 1', which the draft's 'k = poly(n)' does not make explicit; this is likely satisfiable in the intended regime but is an omitted condition. |
| attribution | pass | 20 | The log-gap open problem is this paper's own (Dodis-Lovett-Wichs), stated in their own Section 6, not attributed to prior work. The cited bibliography keys Sie89, Sie04, LPP+24 are all printed in the paper's own reference list (pages 19-20) and cited elsewhere in the paper (Sie89/Sie04 for the PERFECT k-wise independence lower bound, Section 1.1/Section 4/Corollary 4.6; LPP+24 for Larsen et al.'s improved perfect-independence construction, Section 1.1, page 3) — but note these citations concern the perfectly-independent case (Section 4), not directly the almost-independent log-gap problem (Section 5/6) this draft is about. The draft does not claim otherwise (it only lists them as verified-printed), so this is a minor context note rather than a failure. |
| definitions | pass | 8 | 't-word-local', 'explicit', and 'ε-almost k-wise independent' as used in the draft match the paper's own definitions (page 8 for word-locality/explicitness; Section 3 and the Introduction, page 1, for ε-almost k-wise independence). No swapped or non-standard definition detected. |
| fabrication | fail | 4 | The status_note's claim that the O(n/√w) upper bound 'matches' the Ω(n/(√w log n)) lower bound 'up to a Θ(log n) multiplicative factor' uniformly across 1 <= w <= n^2 is not supported: for 2 ≤ w = o(log^2 n) no O(n/√w)-locality construction is given by the paper at all (see quantifiers-and-parameters check, and the Introduction's explicit 'sufficiently large word size w = Ω(log^2 n + log^2 k)' caveat on page 4). |
| self-containment | unclear | - | The draft JSON provided for verification has no notation_latex/definitions_latex fields, so I cannot confirm whether every symbol used in formal_statement_latex (t-word-local family, Σ, ℓ, etc.) is actually defined elsewhere in the full record. This may simply be because those fields were not included in what was pasted for review, rather than a defect in the underlying record. |

### Unsupported by the paper

- The formal_statement_latex and status_note assert that the best known explicit construction achieves locality t_ub(n,w) = O(n/√w) uniformly for the whole range 1 <= w <= n^2, citing Theorems 5.7 and 5.10 together. This is not accurate: Theorem 5.10 requires w = Ω(log^2 k + log^2 n) as a standing hypothesis (page 18), reaffirmed in the paper's own results summary on page 4 ('In the word model with sufficiently large word size w = Ω(log^2 n + log^2 k), we get optimal...'). Theorem 5.7 covers only w=1. For 2 ≤ w = o(log^2 n), the paper establishes no matching construction; instead it names unifying the bit-local and word-local constructions across '1 ≤ w ≤ n^2' as a second, separate open problem (page 20). The draft appears to have imported the word-size range from that second problem and attached it to the first (log-gap) problem's established-upper-bound claim.

### Corrections the checker asked for

- **(see reason)** — Restrict the word-size domain over which the O(n/√w) vs Ω(n/(√w log n)) gap is stated to hold: w = 1 (via the bit-local Theorem 5.7) or w = Ω(log^2 k + log^2 n) up to n^2 (via the word-local Theorem 5.10), rather than the full 1 <= w <= n^2. For 2 ≤ w = o(log^2 n) the paper does not claim, and does not establish, an O(n/√w) construction; that sub-range is where the paper's separate 'unify bit-local and word-local constructions for all word sizes 1 ≤ w ≤ n^2' remark (page 20) applies instead, and should not be folded into this conjecture's formal statement.
  - suggested: applied, per this note
- **(see reason)** — Make explicit the standing hypothesis k > tw/n + 1 required by Theorem 5.1's specialization (page 11) rather than silently assuming any k = poly(n) suffices unconditionally across the whole w-range; in the intended cryptographic regime (k a sufficiently large fixed polynomial in n) this is satisfied, but the formal statement should say so rather than omit it.
  - suggested: applied, per this note
- **(see reason)** — If the intent was to also capture the 'unify the two constructions across all word sizes' problem, that should be written as a second, separate conjecture (per the house rule against merging two open problems the paper poses separately), not merged into this one's formal statement via the shared '1 <= w <= n^2' range.
  - suggested: applied, per this note

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

A reviewer should independently confirm that O(n/sqrt(w)) and Omega(n/(sqrt(w) log n)) are exactly what Theorems 5.1, 5.7, and 5.10 give once specialized to output length n, error 2^{-n}, and k=poly(n) (Theorem 5.1's general statement needs combining with its own 'in particular' specialization, and its standing hypothesis k > tw/n+1 should be checked to hold throughout). Crucially, the word-size domain here is restricted to w=1 (Theorem 5.7) and w=Ω(log^2 k+log^2 n) up to n^2 (Theorem 5.10, whose 'sufficiently large word size' standing hypothesis is confirmed both in the theorem statement, page 18, and the paper's own results summary, page 4) -- NOT the full range 1<=w<=n^2, since no matching construction is given for 2<=w=o(log^2 n). That intermediate range is where the paper's separate 'unify the two constructions' remark applies instead, and should not be folded into this statement.

