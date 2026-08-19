# Provenance: Subexponential Best Separable State with Imperfect Completeness

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Quantum entanglement, sum of squares, and the log rank conjecture**
- Authors: Boaz Barak, Pravesh K. Kothari, David Steurer
- Venue/archive: arXiv preprint (quant-ph), dated July 11, 2017; v2 submitted 9 Jul 2017 2017
- Identifier: arXiv:1701.06321v2 [quant-ph]
- Bibliographic detail: printed-on-page
- File: `1701.06321v2.pdf` (25 pages)
- sha256: `86e9ffb81edc99fcd7814139743b277020279e7013c54fe7eb78af53395db9db`
- Read on 2026-08-19T15:30:30Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Settled for c = 1 and for c = 1 - 1/n, by Theorem 1.3 together with Remarks 1.4 and 4.3. Open for every constant c strictly below 1; the paper lists this first among its open questions in Section 8 and conjectures the affirmative answer.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 5 | 5 | exact (100%) | It is an interesting open problem to find out whether our results can extend to the setting where in the YES case Tr(ρM) = 1 − ε for some absolute constant ε. W... |
| openness | 21 | 21 | exact (100%) | One question, mentioned in Remark 1.4 is whether we can remove the perfect, or near-perfect, completeness condition. |
| progress | 5 | 5 | exact (100%) | We state our results for the case of perfect completeness for simplicity, but all of the proofs extend to the case of “near perfect completeness” where in the Y... |
| progress | 12 | 12 | exact (100%) | Note that the proof would have gone through even if the pseudo-distribution µ did not satisfy the condition that uv⊺ ∈ W but merely that kΠW ⊥ uv⊺ k ≪ ku0 v0⊺ k... |
| definition | 5 | 5 | near (99%) | A quantum measurement operator is an m × m complex Hermitian matrix M such that 0  M  I. The probability that a measurement M accepts a state ρ is Tr(ρM). |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely in the paper and genuinely open: Remark 1.4 (PDF p.5) poses constant completeness error and explicitly conjectures the affirmative, Section 8 (PDF p.21) re-poses it first among the open questions, and no later section or appendix touches it. The single substantive defect is that the formal statement demands a deterministic algorithm, which over-specifies the conjecture — the paper's own algorithm is randomized, since Lemma 7.1 (PDF p.19) finds the needed unit vector by showing a random one succeeds with probability 2^{-O(k)}, and no derandomization is offered; a randomized 2^{Otilde(sqrt n)} algorithm would settle the paper's conjecture while failing the draft's. Secondary repairs: the invented poly(n)-bit input encoding, and the setting's attribution to Remark 4.3 of an "obstruction" framing and a factor-n gap claim that the paper never makes.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 5 | Remark 1.4 (PDF p.5, printed p.3) poses exactly this: "It is an interesting open problem to find out whether our results can extend to the setting where in the YES case Tr(rho M) = 1 - eps for some absolute constant eps. We conjecture that this is indeed the case." The draft's quotes are verbatim. |
| Openness | pass | 21 | Read past Remark 1.4: Section 8 (PDF p.21, printed p.19) re-poses it as the first listed question — "One question, mentioned in Remark 1.4 is whether we can remove the perfect, or near-perfect, completeness condition" — and then moves to a different question (improving the sqrt(n) exponent). Sections 4-7 prove only the c=1 case (Thm 1.3/4.2, PDF pp.11-12); Appendix A proves Thm 5.3, Appendix B is the complex-to-real reduction, Appendix C is a higher-rank structure theorem. Nothing resolves constant completeness error anywhere in the paper. |
| Strength | pass | 5 | Paper's conjecture: YES case Tr(rho M) = 1 - eps for absolute constant eps, with "our results" = Thm 1.3's "for every s < 1, a 2^{Otilde(sqrt n)} time algorithm for BSS_{1,s}" (PDF p.5) and abstract's exp(Otilde(sqrt n / eps^2)) (PDF p.1). The draft's c = 1 - eps constant, s constant below c, running time 2^{C sqrt n (log n)^C} is the same statement, neither strengthened nor weakened on the completeness/soundness axis. Excluding c = 1 is correct — that case is proved. |
| Quantifiers and parameters | pass | 11 | Theorem 4.1 (PDF p.11) sets k = sqrt(n) log^C n / eps^2, so the paper's exponent is Otilde(sqrt n)/eps^2 with eps tied to the soundness gap via Lemma 2.1 (Tr(M rho) >= 1 - 2 eps^2, PDF p.6). The draft's C = C(c,s) depending on c,s but not on n or M correctly absorbs this; c and s are constants independent of n, as the paper's "absolute constant" requires. Order of quantifiers (constants first, then algorithm, then all inputs) matches. |
| Attribution | pass | 21 | This is the harvested paper's own conjecture ("We conjecture that this is indeed the case", PDF p.5), and the draft presents it as such. The draft does not conflate it with the separate AIM14 suggestion about quasi-polynomial time, which the paper cites on PDF p.21 and which the draft correctly attributes to Aaronson-Impagliazzo-Moshkovitz in the setting. |
| Definitions | pass | 5 | Measurement operator, separable state, entangled and Tr(rho M) all match Definition 1.2 and the surrounding text on PDF p.5 clause for clause, including the identification of [n^2] with [n]x[n] and w = uv*. One divergence: the paper's Definition 1.2 says only "complex Hermitian matrix rho such that Tr rho = 1"; the draft adds positive semidefiniteness. This restores the standard notion the paper plainly intends (it immediately calls every mixed state a convex combination of pure states) and cannot change what counts as a proof, since BSS quantifies only over separable states, which are PSD by construction in both readings. |
| Fabrication | fail | 19 | The formal statement asserts a DETERMINISTIC algorithm. The paper's algorithm is randomized as presented: Section 7 / Lemma 7.1 (PDF p.19) finds the required unit vector by sampling — "It remains to argue that we can find such a unit vector in time 2^{O(k)}. To that end we will show that a random unit vector succeeds with probability 2^{-O(k)}" — and no derandomization is given or claimed anywhere. Remark 1.4 conjectures that "our results" extend, i.e. whatever Theorem 1.3 delivers. Also unsupported: the poly(n)-bit rational input encoding (the paper specifies no input model), and the framing that Remark 4.3 "isolates exactly how much slack the argument has" / is a "named quantitative obstruction" with "nothing in the analysis clos[ing] that gap" — Remark 4.3 (PDF p.12) presents k^2/n^2 as an extension enabling near-perfect completeness, not as a barrier, and never states the factor-n shortfall the draft attributes to it. The arithmetic is right; the attribution to the paper is the draft's own. |
| Self-containment | pass | - | The four definitions supplied (state, measurement operator, separable state, BSS_{c,s}) plus the notation block make the statement readable without the paper; the internal "Definition 2"/"Definition 4" references point into the draft's own definitions block, not the paper's numbering. A reader would know what to prove. |

### Unsupported by the paper

- "deterministic algorithm" in formal_statement_latex — the paper's algorithm finds its reweighting direction by random sampling (Lemma 7.1, PDF p.19: "a random unit vector succeeds with probability 2^{-O(k)}") and the paper never claims or proves determinism.
- The input-encoding stipulation "complex numbers with rational real and imaginary parts of bit length at most poly(n)" — no input model is specified anywhere in the paper.
- "tolerates a completeness error of one over the dimension, and no more" (informal) and "This is the named quantitative obstruction ... nothing in the analysis closes that gap" (setting_latex) — the paper presents Remark 4.3 as an extension to near-perfect completeness (PDF p.12), never as an obstruction, and never states that the analysis cannot be pushed further.
- Minor: the draft's Definition 1 adds positive semidefiniteness, which the paper's Definition 1.2 (PDF p.5) omits. This is the standard notion the paper evidently intends and has no effect on BSS, so it is noted rather than counted against the statement.

### Corrections the checker asked for

- **formal_statement_latex** — Requires a "deterministic algorithm". The paper's own algorithm is randomized: Lemma 7.1 (PDF p.19) locates the reweighting direction by showing "a random unit vector succeeds with probability 2^{-O(k)}", and no derandomization appears in the paper. Remark 1.4 conjectures that the paper's results extend, so a randomized 2^{Otilde(sqrt n)} algorithm would settle it while failing the draft's statement.
  - suggested: Replace "a deterministic algorithm $\mathcal{A}$" with "an algorithm $\mathcal{A}$" (or "a randomized algorithm $\mathcal{A}$ succeeding with probability at least $2/3$", matching the paper's own algorithm).
- **formal_statement_latex** — Stipulates an input encoding — "complex numbers with rational real and imaginary parts of bit length at most poly(n)" — that the paper nowhere specifies.
  - suggested: Drop the encoding clause, or mark it as a formalization choice added for definiteness rather than a condition taken from the paper.
- **setting_latex** — Attributes to Remark 4.3 a role it does not play in the paper: "isolates exactly how much slack the argument has", "This is the named quantitative obstruction", "nothing in the analysis closes that gap". Remark 4.3 (PDF p.12) states only that ||u_0 v_0^T|| >= k/n, hence ||Pi_W uv^T||^2 >= 1 - k^2/n^2 suffices, "hence implying that the proof works for the near perfect completeness case". It is framed as an extension, not a barrier, and the factor-n comparison to constant error is not made in the paper.
  - suggested: State that Remark 4.3 gives the bound (k/n, k^2/n^2, k = Otilde(sqrt n)) that yields the 1 - 1/n case, and present the factor-of-n shortfall relative to constant error as an inference from those numbers rather than as something the paper names or asserts.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

Three points to check. (i) Quantifier reading: the paper writes 'the setting where in the YES case Tr(rho M) = 1 - eps for some absolute constant eps', which is literally an existential over eps, but Remark 1.4 frames it as 'whether our results can extend', and Theorem 1.3 which is being extended is universally quantified over the soundness parameter. I have therefore stated it for all constants 0 <= s < c < 1. A reviewer should decide whether the weaker existential reading is the intended one; I judge it is not, since a single unspecified constant eps would be an odd thing to conjecture. (ii) Strength of the conclusion: the paper conjectures that its own proofs extend, which is formally stronger than the existence of some 2^{O~(sqrt n)} algorithm, since it asserts that the specific sum-of-squares algorithm of Section 4 with O~(sqrt n) rounds works. I have stated the algorithmic consequence rather than the sum-of-squares-specific claim, because pinning down 'the same algorithm' would require reproducing the paper's program. A solver who wants to match the paper exactly should aim at the sum-of-squares version. (iii) Currency: I am not aware of any subexponential algorithm for constant-completeness BSS having appeared since 2017, but this is recall rather than a checked fact, and a reviewer should sweep forward citations before publishing.

