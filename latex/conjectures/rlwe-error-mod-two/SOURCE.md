# Provenance: Recovering the Ring-LWE Error Modulo Two Is as Hard as Recovering It

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **A Thorough Treatment of Highly-Efficient NTRU Instantiations**
- Authors: Julien Duman, Kathrin Hövelmanns, Eike Kiltz, Vadim Lyubashevsky, Gregor Seiler, Dominique Unruh
- Venue/archive: Cryptology ePrint Archive 2021
- Identifier: 2021/1352
- Bibliographic detail: inferred
- File: `2021-1352.pdf` (37 pages)
- sha256: `0eeb5d7df3b2458c018befba860497d5036d7adf65e6d458da18cb1e595dc78a`
- Read on 2026-08-18T14:02:38Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. The direction $\mathcal{R}$-LWE2 $\le$ $\mathcal{R}$-LWE is trivial and is not in question. The converse, stated here, has no formal reduction in the paper; the paper substitutes two heuristics, one of which drifts off the prescribed error distribution and one of which reduces from a nonstandard first-is-errorless decision problem rather than from $\mathcal{R}$-LWE itself.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 19 | 19 | exact (100%) | We now define a version of the R-LWE problem in which the adversary is not asked to recover the entire vector e, but just e mod 2. |
| openness | 19 | 19 | exact (100%) | While we do not have a formal reduction from R-LWE to R-LWE2, based on the state of the art of how Ring-LWE problems are solved, the two are essentially equival... |
| statement | 5 | 5 | exact (100%) | The value of p has no effect on the hardness of any version of Ring-LWE (since ph is as uniform as just h), and based on the state of affairs regarding solving ... |
| progress | 20 | 20 | exact (100%) | While the version of the decision R-LWE problem where the first integer coefficient has no error is slightly different than usual, the current best-known algori... |

## Adversarial check

**Verdict: faithful** (confidence: high)

The problem is genuinely in the paper (Definitions 4.3 and 4.5, p. 19), and the paper genuinely leaves it open — \"we do not have a formal reduction from R-LWE to R-LWE2\" (p. 19) is never repaired: p. 20 offers only the two heuristics the draft describes, Table 4 (p. 23) still carries Adv^{R-LWE2_η} as an assumption, and Appendices A–D are about the ACWC/FO transformations. The thing I checked hardest is the one most drafts get wrong here, and this one has it right: the paper's \"reduction from R-LWE to R-LWE2\" means using an R-LWE2 solver to solve R-LWE (fixed by the first heuristic on p. 20), which is exactly the direction the drafted statement asserts, and the draft's insistence that A's guarantee holds only on-distribution is precisely what makes the paper's distribution-narrowing heuristic fall short. Three hypotheses are the draft's own rather than the paper's (q > 4, i and j ≥ 1, classical algorithms only, plus fixing η = ψ_2^d where Definition 4.5 allows general η); each narrows the claim without misstating the paper, and q > 4 is needed for the draft's mod-2 convention to be well defined, so none is a defect to correct.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 19 | Definition 4.5 (R-LWE2_η) — "one is given (h, hr + e), where h ← R and r, e ← η, and is asked to recover e mod 2" — sits directly after Definition 4.3 (R-LWE_η, recover e). The informal version also appears on p. 5 ("finding m mod 2 is as hard as finding m"). Both drafted definitions correspond clause for clause. |
| openness | pass | 19 | "While we do not have a formal reduction from R-LWE to R-LWE2 ... the two are essentially equivalent. We now present two heuristic arguments" (p. 19, verbatim). Read past it: p. 20 gives only the two heuristics and concludes it is "very reasonable to assume" equal concrete hardness; Table 4 (p. 23) still carries Adv^{R-LWE2_η} as an unproven assumption in the CCA-NTRU-A bound; Appendices A–D (pp. 26–37) prove the O2H/measure-and-reprogram results for ACWC_0/ACWC and FO-perp, nothing about this equivalence. No reduction anywhere in pp. 1–37. |
| strength | pass | 20 | Direction is right, which is where this could easily have gone wrong. The paper's "reduction from R-LWE to R-LWE2" is fixed by the first heuristic on p. 20: an R-LWE2 solver is fed an R-LWE instance. The draft's statement is exactly that — A solves R-LWE2 ⟹ B^A solves R-LWE — neither the trivial converse nor a decision/search swap. The draft also correctly does not claim the paper's concrete-hardness equality (p. 20, "the concrete hardness ... is the same"); asking only for a polynomial-loss reduction is the honest formalization of the "formal reduction" the paper says it lacks. |
| quantifiers-and-parameters | pass | 17 | §4.1 (p. 17): ring Z_q[X]/(X^d − X^{d/2} + 1), d of the form 2^i 3^j, q prime, mod^± q into {−(q−1)/2,…,(q−1)/2}. Definitions 4.3/4.5 (p. 19) draw h ← R and r, e ← η independently, matching the draft's advantage functions. Three draft-added hypotheses are NOT in the paper: q > 4 (paper says only "the prime q"), i, j ≥ 1 (paper writes d = 2^i 3^j unrestricted, so j = 0 is not excluded there, though every Table 1 parameter has j ≥ 1), and "algorithms are classical" (narrower than the paper's use — Table 4's QROM row on p. 23 implicitly quantifies Adv^{R-LWE2} over quantum adversaries). All three narrow the statement rather than misstate the paper, and q > 4 is required for the draft's own mod-2 convention to be well defined, so none is a repairable error. Fixing η = ψ_2^d where Definitions 4.3/4.5 allow general η is likewise a narrowing to §4.4's case ("for η = ψ_2^d", p. 20) and Table 4, and the draft states this explicitly. |
| attribution | pass | 20 | The gap is the harvested paper's own: R-LWE2 is introduced by Definition 4.5 (p. 19) and the missing reduction is the paper's own admission, underpinning its own scheme (Table 4, p. 23). The cited prior work is correctly kept at arm's length — p. 20: "[BLP+13] considers this 'First-is-Errorless' version of LWE and shows that it is essentially as hard as the usual version. Boudgoust et al. [BJRW21] extend this problem to it's Module-LWE variant and showed that an even stronger assumption has a (non-tight) reduction from the usual Module-LWE problem." The draft's rendering matches, and neither is presented as this paper's own result. |
| definitions | pass | 17 | ψ_2^d: eq. (6) with k = 2 is Σa_i − Σb_i, b_i ← {0,1}^d, i.e. the draft's a_1+a_2−b_1−b_2, and eq. (7)'s table (1/16, 4/16, 6/16, 4/16, 1/16 on −2..2) matches the draft exactly. "e mod 2" as (e mod^± q) mod 2 is the paper's composition (p. 17: mod^± q, then "Reducing an integer modulo 2 always maps it to a bit. These functions naturally extend to vectors and polynomials"), confirmed by Fig. 7 line 14 and eq. (9) on p. 21 and by Lemma 4.1 (p. 18). No definition silently swapped; problem names renamed only (R-LWE_η → "with binomial noise"), which is permitted. |
| fabrication | pass | 21 | Every scheme claim in the setting checks out: f := 2f' + 1 and Dec's u := (cf mod^± q) mod 2 are Fig. 7 lines 06 and 14 (p. 21); "equals e mod 2 whenever the noise stays inside the decoding radius" is eq. (9) plus the \|gr + ef'\| < q/4 − 1 condition (p. 21); the adversary-controls-only-the-parity / no-transformation-needed claim is p. 20 plus eq. (13) and the worst-case = average-case conclusion on p. 22, and p. 6 ("the scheme in Figure 7 which did not require any transformation"); "appears in the paper's concrete security bounds for the resulting KEM" is Table 4, p. 23 (ε_A = Adv^{R-NTRU_η} + Adv^{R-LWE2_η}, η = ψ_2^d) — a page the draft does not list. Both heuristics are reproduced accurately, including the (2^{-1}h, 2^{-1}hr + 2^{-1}(e−f)) step and the named obstruction that e' is "narrower" (p. 20). All eight bibliography entries match the reference list on pp. 25–26 verbatim (BLP13 is the paper's BLP+13 — key renaming only). All four quotes are verbatim against the text layer. |
| self-containment | pass | 19 | The draft supplies the ring, the mod^± q and mod 2 conventions, the full ψ_2^d distribution, both advantage functions, and the exact reduction obligation including the on-distribution-only restriction on the oracle. A reader who has never opened the paper knows what would count as a proof. |

## Build

- pdflatex: ok
- chktex: 6 warnings
- lacheck: 3 warnings

## What to check hardest

First, the quantification over the noise distribution must stay pinned to $\psi_2^{d}$, the paper's instantiation. Stated for an arbitrary distribution $\eta$ the claim is false for a silly reason: if $\eta$ is supported on polynomials with even coefficients then the parity problem is trivial while the search problem need not be. A reviewer should check that fixing $\eta = \psi_2^{d}$ is the right reading of the paper's ``the two are essentially equivalent'' — I believe it is, since $\mathcal{R}$-LWE2 is used only at $\eta = \psi_2^{d}$ in the paper's security bounds. Second, formalising ``essentially equivalent'' as a uniform polynomial-time reduction with inverse-polynomial success is my choice; the paper's own wording is about concrete hardness being the same, and one could reasonably ask instead for a tight reduction, which would be a strictly stronger conjecture. Third, I have not verified against the literature that no such reduction has appeared since 2021; the binary-secret and first-is-errorless Module-LWE line of work descending from \cite{BLP13} and \cite{BJRW21} is where to look, and this ePrint report has later versions and a published version that should be checked for a resolution. Fourth, Definition 4.5 in the paper misnames the problem in its own body text (``In the R-LWE problem'' where $\mathcal{R}$-LWE2 is meant); the intended reading is unambiguous from the ``asked to recover $\mathbf{e}$ mod 2'' clause.

