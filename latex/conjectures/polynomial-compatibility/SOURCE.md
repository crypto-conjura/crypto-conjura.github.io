# Provenance: The Polynomial Compatibility Conjecture

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **On the Impossibility of Key Agreements from Quantum Random Oracles**
- Authors: Per Austrin, Hao Chung, Kai-Min Chung, Shiuan Fu, Yao-Ting Lin, Mohammad Mahmoody
- Venue/archive: Cryptology ePrint Archive 2022
- Identifier: 2022/218
- Bibliographic detail: inferred
- File: `2022-218.pdf` (42 pages)
- sha256: `c2abbb98e76dd9794cd9551025f25e6c8761bdc8039d6477fd1d3c2603a9d7c8`
- Read on 2026-08-17T19:13:35Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Open as stated. The paper proves it (Theorem 4.4) whenever $\delta < |\mathcal{Y}|^{-d}/d$, i.e. for exponentially small influences, and shows (Theorem 5.6) that this polynomial formulation is equivalent to the quantum-state formulation, Conjecture 4.3. Appendix B rules out $\delta \ge 1/(2d)$ and shows the degree and influence hypotheses are needed on both distributions. Everything between $|\mathcal{Y}|^{-d}/d$ and $1/(2d)$ is open, and any $\delta$ that is $1/\mathrm{poly}(d,\log|\mathcal{Y}|)$ already suffices for a polynomial-query attack.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 1 | 1 | exact (100%) | Our conjecture, roughly speaking, states that the multiplication of any two degree-d real-valued polynomials over the Boolean hypercube of influence at most δ =... |
| openness | 19 | 19 | exact (100%) | While we have so far been unable to prove the conjecture, we can prove a weaker version of the conjecture with exponentially worse parameters, which still leads... |
| openness | 20 | 20 | exact (100%) | While we do not have a proof of Conjecture 4.3, we can prove the following theorem when the influences are exponentially small. The proof is deferred to Section... |
| progress | 41 | 41 | exact (100%) | In this section, we provide examples of functions that show the necessity of the properties of the polynomials (or quantum states) as stated in Conjectures 4.3 ... |
| progress | 11 | 11 | exact (100%) | One interesting similarity is that both conjectures hold, when we assume exponentially small influences [DFKO06]. Despite that, our conjecture and the AA conjec... |
| parameter | 20 | 20 | exact (100%) | In general, we pose the following question. How small should δ be, as a function of \|Y\| and d, in order to guarantee that any two (Y, δ, d, N )-states are com... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The drafted statement is Conjecture 5.5 (p. 25) reproduced faithfully clause by clause — including the detail most likely to be got wrong, that the influence bound is on the average over each distribution rather than worst-case over its support, and that delta is a function of d alone and not of N. It is the paper's own conjecture, the paper says twice that it cannot prove it (pp. 19, 20), and it is still an assumption in Section 6 and the appendices, so it stays open. The one defect is in the progress note, not the statement: the 2^d / 2^{-d} account of Theorem 4.4's proof is the p. 10 Boolean overview, whereas Theorem 4.4 is group-general and its Section 5.2 proof counts |Y|^d characters for a |Y|^{-d} loss — inconsistent with the |Y|^{-d}/d threshold quoted in the same sentence.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 25 | The statement is Conjecture 5.5 on p. 25, the group-general polynomial formulation. Its Boolean special case is Conjecture 1.2 (p. 5) and its quantum-state twin is Conjecture 4.3 (p. 20). The draft never names Conjecture 5.5 explicitly, but its status_note identifies it correctly by reference to Theorem 5.6 and Conjecture 4.3. |
| Openness | pass | 19 | p. 19: 'While we have so far been unable to prove the conjecture, we can prove a weaker version ... with exponentially worse parameters.' p. 20: 'While we do not have a proof of Conjecture 4.3 ...'. It stays open: Theorem 4.4 (p. 20) covers only delta < \|Y\|^{-d}/d; Theorem 5.6 (p. 25) only proves equivalence with Conjecture 4.3; Theorem 6.3 (p. 27) is explicitly stated 'Assuming Conjecture 5.5'; Appendix A proves only the complex-to-real reduction; Appendix B (pp. 41-42) gives counterexamples to relaxations, not a resolution. |
| Strength | pass | 25 | Clause by clause against Conjecture 5.5: unit l2 norm on every f in supp(F) and g in supp(G); deg(f), deg(g) <= d; per-coordinate average influence <= delta(d) for both distributions; conclusion is existence of one f, one g and one x with f(x)g(x) != 0. No strengthening, no weakening, no generalisation. |
| Quantifiers and parameters | pass | 25 | Order matches: exists Y, exists delta(.), for all d (and N), for all F, G. The influence bound is on the AVERAGE over the distribution, not worst-case over the support - the draft gets this right, which is the easiest place to slip. delta depends on d only, not on N; the draft's parameters entry flags this (corroborated by p. 5: 'a smaller influence delta which is independent of the size of the input space N = 2^kappa'). The draft's rendering delta(d) >= d^{-c} is the correct reading of '1/poly': larger delta is the stronger statement, so an existential lower bound is right. The paper writes '1/poly(.)' with a blank argument in Conjecture 5.5, but Conjecture 4.3 (p. 20) says '1/poly(d)' and Theorem 5.6 makes them equivalent, so poly-in-d is settled. |
| Attribution | pass | 20 | 'Our main conjecture is as follows' (p. 20); the abstract calls it 'our conjecture' and 'a natural conjecture'. It is the harvested paper's own. The draft correctly keeps the Aaronson-Ambainis conjecture separate and attributed to [AA14] (p. 11), and correctly credits the exponentially-small-influence regime of both conjectures to [DFKO06] and the no-communication case to [OSSS05], both as the paper does on p. 11. |
| Definitions | pass | 25 | deg(chi) = \|{i : chi_i != 0-hat}\|, deg(f) = max{deg(chi) : f-hat(chi) != 0}, Inf_i(f) = sum over chi with chi_i != 0-hat of \|f-hat(chi)\|^2 - all verbatim from p. 25. Dual group, trivial character 0-hat, \|Y-hat\| = \|Y\| match p. 12. The Boolean specialisation given in the definitions block (deg = max \|S\|, Inf_i = sum over S containing i of alpha_S^2) matches p. 4. 'Compatible' is not used as an undefined term in the statement; it is unfolded into the f(x)g(x) != 0 conclusion, exactly as Observation 5.4 (p. 25) licenses. |
| Fabrication | fail | 26 | The progress_note attributes to Theorem 4.4 a proof in which the constant term dominates 'all 2^d non-constant terms' with 'the 2^{-d} loss' coming from that count. Section 5.2 (p. 26) decomposes g over the \|Y\|^d characters in Y-hat^d and the threshold is \|Y\|^{-d}/d. The 2^d/2^{-d} figures are from the informal Boolean overview on p. 10, which describes Conjecture 1.2, not the group-general Theorem 4.4 the draft is citing. Everything else checked out: Theorem 4.4's threshold delta < \|Y\|^{-d}/d (p. 20), Theorem 4.5's poly(d, log\|Y\|)-query classical attack (p. 20), Theorem 4.6's \|Y\|^d d^2/lambda exponential attack (p. 21), Theorem 5.6's equivalence and the 'suffices to consider real functions' gloss (p. 25), Lemma 4.8's group-equivalence claim (p. 21, cf. p. 5), Appendix B's delta < 1/(2d) bound and the need for both hypotheses on both distributions (pp. 5, 41-42), Theorem 6.3's conditional black-box separation and the OT corollary (pp. 6, 27). All ten bibliography entries match the printed reference list (pp. 36-39). |
| Self-containment | pass | - | A reader who has never seen the paper could work from the statement alone: the notation block defines the character basis, Fourier expansion and l2 norm; the definitions block defines degree and influence; the statement is closed under those. Nothing is left dangling on the cryptographic setting. |

### Unsupported by the paper

- progress_note: 'a constant term dominating all $2^d$ non-constant terms of the restriction; the $2^{-d}$ loss comes from that count', asserted about Theorem 4.4. The paper's proof of Theorem 4.4 (p. 26) counts $|\mathcal{Y}|^d$ characters and loses $|\mathcal{Y}|^{-d}$; the $2^d$ figure appears only in the p. 10 overview of the Boolean Conjecture 1.2.

### Corrections the checker asked for

- **progress_note** — The account of Theorem 4.4's proof uses 2^d and 2^{-d}, which are the counts from the paper's informal Boolean overview on p. 10 (about Conjecture 1.2). Theorem 4.4 is stated for all finite Abelian groups Y, and its proof in Section 5.2 (p. 26) is over |Y|^d characters, matching the |Y|^{-d}/d threshold the same sentence quotes. As written the sentence is internally inconsistent: it states the threshold as |Y|^{-d}/d and then explains a 2^{-d} loss.
  - suggested: Theorem 4.4 proves the conjecture for $\delta < |\mathcal{Y}|^{-d}/d$ by fixing a maximum-degree term of $f$ and showing that a $g$ with small influences has, in expectation over a random assignment to the remaining variables, a constant term dominating all $|\mathcal{Y}|^{d}$ non-constant terms of the restriction; the $|\mathcal{Y}|^{-d}$ loss comes from that count (in the Boolean case $\mathcal{Y} = \mathbb{Z}_2$ this is the $2^{-d}$ of the paper's overview). The proof in fact uses no influence condition on $F$ and no degree bound on $G$.

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 2 warnings

## What to check hardest

(1) Whether it has been resolved since February 2022. I am not aware of a proof or refutation, but I did not search the literature and a reviewer should check for follow-ups before publishing; the paper's own Section 1.3 notes the exponential-influence case follows the pattern of [DFKO06], which is where a refutation might come from. (2) The strength of the group quantifier: Conjecture 4.3/5.5 says there \emph{exists} a finite Abelian group that works, while Conjecture 1.2 in the introduction fixes the Boolean case $\mathcal{Y} = \mathbb{Z}_2$. I have stated the existential version because that is the one Theorems 4.5 and 6.3 use; the Boolean version is strictly stronger and also open. Anyone stating the Boolean case must not present it as the paper's main conjecture. (3) The influence condition is on the \emph{average} over the distribution, not on each polynomial in the support -- easy to strengthen by accident. (4) Conjecture 5.5 leaves $N$ free in the text; I have quantified it universally, which is explicit in the equivalent Conjecture 4.3 (``for any $d, N \in \mathbb{N}$''). (5) The paper's introduction writes the $\ell_2$ norm without the square root; since the constraint is that the norm equals $1$ this makes no difference, and I have used the standard normalisation.

