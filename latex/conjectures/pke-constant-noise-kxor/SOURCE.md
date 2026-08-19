# Provenance: Public-Key Encryption from Constant-Noise Planted k-XOR

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **The Complexity of Public-Key Cryptography**
- Authors: Boaz Barak
- Venue/archive: Cryptology ePrint Archive 2017
- Identifier: 2017/365
- Bibliographic detail: inferred
- File: `2017-365.pdf` (33 pages)
- sha256: `783db89538f26c3bdba6e5efbd019977d75f405771d71bb31cd1a83dd263a789`
- Read on 2026-08-18T23:26:18Z via the `cli` backend

## How the paper leaves it open

`paper-asks-question`. Open in the paper, and posed there as a question rather than a conjecture. The paper's own reference point, the Applebaum-Barak-Wigderson linear variant, builds public-key encryption from planted noisy linear equations only when the noise rate is sub-constant (it needs the noise rate times the arity to be O(1/log n)); Alekhnovich's scheme needs noise about one over the square root of the dimension, on dense rather than sparse equations. No scheme in the survey is based on constant noise at linear density.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 20 | 20 | near (96%) | Can we base a public-key encryption scheme on the difficulty of solving O(n) random kXOR equations on n variables with a planted solution satisfying 1 − ε of th... |
| openness | 20 | 20 | exact (100%) | This viewpoint raises the following open questions: |
| progress | 20 | 20 | exact (100%) | The noise level δ should satisfy δk = O(1/ log n) for efficient decryption, and so the lower the noise level we consider (and hence the stronger we make our ass... |
| progress | 14 | 14 | exact (100%) | A recent result of Ben-Sasson et al. [BBD+ 16] suggests that using such a small amount of noise might be an inherent limitation of schemes of this general type. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is on p. 20 word for word, is posed in the survey author's own voice as an open question, and nothing in Sections 5.4, 6, or the references (pp. 21–33) resolves it, so the conjecture is genuine and the formal statement is a fair rendering of it. The single most important defect is a fabricated premise repeated in both informal and setting_latex — that every non-algebraic scheme in the survey requires noise below 1/√n — which Figure 3 on p. 15 directly contradicts, since ABW Scheme 1 is listed with noise n^{-0.1} and ABW Scheme 3 uses no noise at all; the paper's actual constraint on the ABW linear variant is only δk = O(1/log n), i.e. sub-constant. That error, plus five smaller unsupported assertions in the prose, is repairable without touching the formal statement.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 20 | The question appears verbatim on p. 20 as the first bullet of Section 5.3's closing list: "Can we base a public-key encryption scheme on the difficulty of solving O(n) random kXOR equations on n variables with a planted solution satisfying 1 − ε of them for some constant ε > 0?" The draft's quote is exact. |
| Openness | pass | 20 | Introduced by "This viewpoint raises the following open questions:" (p. 20). I read past it: the remainder of 5.3 (p. 21) discusses only the second bullet (unbalanced expansion), Section 5.4 (pp. 21–22) is about IO, Section 6 (pp. 22–24) is philosophical, and pp. 24–33 are references. The paper never returns to the kXOR question, and no table or footnote answers it. |
| Strength | pass | 20 | The draft's existential (∃ k, c, ε, Π such that hardness of planted k-XOR ⇒ CPA security of Π) matches "Can we base a public-key encryption scheme on ... for some constant ε > 0". Reading "base on" as a single-assumption reduction is supported by the immediate context, where ABW's schemes are explicitly said to rest on two assumptions (pp. 18–19). Requiring correctness unconditionally is an addition but does not change what would count as a proof. |
| Quantifiers and parameters | pass | 20 | m = ⌈cn⌉ for an existentially quantified constant c faithfully renders "O(n) ... equations"; ε is a constant existentially quantified, matching "for some constant ε > 0". Narrowing to ε ∈ (0,1/2) and k ≥ 3 restricts the existential slightly beyond what the paper writes, but excludes only trivial ranges (a random assignment already achieves ≈1/2). Order of quantifiers is correct. |
| Attribution | pass | 20 | This is the survey author's own open question, posed in his own voice in Section 5.3, not one he attributes to ABW or anyone else; openness_kind "paper-asks-question" is right. Section 5.3's framing on p. 18 ("[ABW10] tried to explore the question of whether public-key encryption can be based on the conjectured average-case difficulty of combinatorial problems") is correctly presented as background, not as the open problem. |
| Definitions | unclear | 7 | The paper gives no formal definition of the kXOR problem where it asks the question, so the draft must supply one — but its choices diverge from the paper's own machinery. Definition 2 (p. 6) calls a planted problem hard when no PPT algorithm succeeds with probability ≥ 0.9, not with negligible probability; the planted-CSP problem on p. 7 is defined as finding an assignment of value ≥ μ_D/2 + μ/2, a strictly lower bar than the draft's val ≥ 1−ε; and the draft's fixed-weight noise (exactly ⌊εm⌋ flipped equations) replaces the i.i.d. δ-mixture of Definition 3 (p. 7, from [BKS13]). I cannot settle from the paper which formalization it intends. |
| Fabrication | fail | 15 | setting_latex asserts "every construction in the survey needs either group structure or noise well below 1/√n", and informal asserts every non-algebraic scheme needs noise "below one over the square root of the number of variables". Figure 3 (p. 15) contradicts this: ABW Scheme 1 is listed with noise n^{-0.1}, far above 1/√n, and ABW Scheme 3 (nonlinear-PRG based, p. 19) uses no noise at all. The paper's own constraint on the ABW linear variant is only δk = O(1/log n), i.e. sub-constant (p. 20). Five further unsupported items are listed in fabrications. |
| Self-containment | pass | - | notation_latex and definitions_latex fix [n], ⊕, val_Φ, the planted distribution, and CPA security; a reader who has never seen the survey could tell what would count as a proof. No page evidence is needed for this check. |

### Unsupported by the paper

- setting_latex and informal: the claim that every non-group-based scheme in the survey requires noise below 1/√n. Figure 3 (p. 15) lists ABW Scheme 1 at noise n^{-0.1}, and ABW Scheme 3 uses a nonlinear PRG with no noise (p. 19). The paper's stated constraint on the ABW linear variant is only δk = O(1/log n) (p. 20).
- setting_latex: "planted problems of this shape get easier as equations pile up, and O(n) is the sparsest and therefore strongest form." Not in the paper; the p. 19 remark about larger m concerns the trade-off between ABW's two assumptions, not the difficulty of planted k-XOR.
- setting_latex: Alekhnovich's scheme described as using "dense rather than sparse equations." The paper (pp. 12, 15) characterises it only by noise level, never by density.
- informal: the NP ∩ coNP oracle described as "a problem believed to be much easier than the encryption scheme itself." The paper states the opposite belief on p. 14 (most experts believe NP ∩ coNP ⊄ P) and frames the result as evidence of structure, not of easiness.
- setting_latex: ABW called "the most serious attempt at a public-key scheme from a combinatorial assumption." The paper makes no such comparative judgement (p. 18).
- informal: "there is evidence that noise this large may be incompatible with the way all known schemes of this kind work." The [BBD+16] evidence (p. 14 and fn. 13) covers a specific family of noisy-codeword schemes containing Alekhnovich's, Regev's, and some other lattice schemes — not all known schemes, and notably not ABW's.

### Corrections the checker asked for

- **setting_latex** — "every construction in the survey needs either group structure or noise well below $1/\sqrt{n}$" is contradicted by Figure 3 on p. 15, which lists ABW Scheme 1 with noise $n^{-0.1}$, and by ABW Scheme 3, which uses a nonlinear PRG and no noise at all.
  - suggested: "no scheme in the survey is based on constant noise: ABW's linear-function variant needs $\delta k = O(1/\log n)$ (p. 20), and Alekhnovich's uses noise $\approx 1/\sqrt{n}$ (Figure 3, p. 15)." The $1/\sqrt{n}$ threshold belongs to Alekhnovich and LPN, not to every non-algebraic scheme.
- **informal** — "every non-algebraic scheme we have needs the noise to be far smaller than a constant, below one over the square root of the number of variables" conflates the paper's two distinct thresholds: sub-constant (ABW linear variant, p. 20) and below $1/\sqrt{n}$ (Alekhnovich and LPN, p. 9 fn. 10 and p. 15).
  - suggested: "every non-algebraic scheme we have needs the noise to be sub-constant — for the ABW linear variant, noise rate times arity $O(1/\log n)$; for Alekhnovich, about $1/\sqrt{n}$, which is where the paper locates the structural weakness."
- **informal** — "broken by an oracle for a problem believed to be much easier than the encryption scheme itself" inverts the paper's caveat on p. 14: "while most experts believe that NP ∩ coNP is not contained in P, this result can still be viewed as showing that these lattice-based schemes have some computational structure that is not shared with many one-way function candidates."
  - suggested: "broken given an oracle for a problem in $\mathbf{NP} \cap \mathbf{coNP}$ — not a problem believed to be easy, but a form of computational structure that generic one-way function candidates do not have."
- **setting_latex** — "planted problems of this shape get easier as equations pile up, and $O(n)$ is the sparsest and therefore strongest form" is nowhere in the paper. The nearest passage (p. 19) says larger $m$ strengthens ABW's PRG assumption while weakening their expansion assumption — a trade-off between two different assumptions, not a monotonicity claim about planted $k$-XOR.
  - suggested: Drop the claim or attribute it outside the paper; report the density $O(n)$ simply as what the question on p. 20 fixes.
- **setting_latex** — "on dense rather than sparse equations" for Alekhnovich's scheme is unsupported: Figure 3 (p. 15) and Section 4.2 (p. 12) characterise it only as solving linear mod 2 equations with $\approx 1/\sqrt{n}$ noise, a variant of Ajtai–Dwork based on learning parity with very small noise. Equation density is never mentioned.
  - suggested: Drop "on dense rather than sparse equations"; the paper's contrast is noise level, not density.
- **setting_latex** — "made the most serious attempt at a public-key scheme from a combinatorial assumption" is an evaluative claim the paper does not make.
  - suggested: The paper says only that ABW "tried to explore the question of whether public-key encryption can be based on the conjectured average-case difficulty of combinatorial problems" (p. 18).
- **informal** — "there is evidence that noise this large may be incompatible with the way all known schemes of this kind work" overstates [BBD+16], which p. 14 and footnote 13 describe as covering a specific family of noisy-codeword schemes containing Alekhnovich's, Regev's, and some other lattice schemes.
  - suggested: "there is evidence that noise this sparse may be an inherent limitation of one general family of schemes built from noisy codewords — the family containing Alekhnovich's and Regev's schemes."

## Build

- pdflatex: ok
- chktex: 5 warnings
- lacheck: 1 warnings

## What to check hardest

Four things a reviewer should check hardest. (1) The mechanical grounding of the statement quote: the two occurrences of the Greek epsilon in the open-question bullet on page 20 do not survive text extraction (pdftotext renders each as a control character), so a character-exact match on that quote may come back partial even though the sentence is verbatim from the page. (2) Whether this has been resolved since 2017. I have a recollection of post-2017 work building public-key encryption and lossy primitives from sparse LPN, but in the regime of a slightly super-linear number of samples rather than the O(n) equations asked for here; I am not confident enough of the authors, venue or exact parameters to cite it, and a reviewer should look at the sparse-LPN literature and check whether the linear-density constant-noise case Barak asks about is still open. If it has been settled, this candidate should be withdrawn. (3) The formalisation of 'base a public-key encryption scheme on the difficulty of' as a bare implication from hardness to CPA security is mine; one could reasonably instead demand a black-box reduction with polynomial loss, which would be a stronger conjecture. (4) I have taken 'solving' in the paper's sentence to mean the search problem (find an assignment of the promised value); if one substitutes the distinguishing version of the assumption the conjecture becomes weaker, and the paper does not say which it means. Minor: I fix the noise model so that exactly an epsilon fraction of equations is falsified, matching the paper's 'satisfying 1 - epsilon of them'; the i.i.d. Bernoulli variant differs only by o(1) in the value and should be considered equivalent here. I also read 'O(n)' as 'cn for some constant c we are free to choose'; a stricter reading would fix c in advance.

