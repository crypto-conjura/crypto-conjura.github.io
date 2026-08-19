# Provenance: No Expanding Weak Quadratic Pseudorandom Generators

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Sum-of-Squares Meets Program Obfuscation, Revisited**
- Authors: Boaz Barak, Samuel B. Hopkins, Aayush Jain, Pravesh Kothari, Amit Sahai
- Venue/archive: IACR Cryptology ePrint Archive 2018
- Identifier: ePrint 2018/1237
- Bibliographic detail: inferred
- File: `2018-1237.pdf` (28 pages)
- sha256: `6221bd8394c58980710670e310654de2c6725c737d69cd01311e0345ec828427`
- Read on 2026-08-18T23:53:50Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Settled only in the restricted case where $q_1, \dots, q_m$ are drawn independently and identically from a "nice" distribution (normalised, pairwise-independent coefficients) and the input is polynomially bounded and sub-Gaussian: there the paper's Theorem 2 gives a polynomial-time algorithm that recovers $x$ exactly from $m \ge n(\log n)^{O(1)}$ samples, which in particular distinguishes. The hypothesis as stated, with arbitrary (possibly correlated) polynomials and an arbitrary bounded input distribution, is open.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | We consider the following general hypothesis that, if true, would rule out not just the three proposed approaches based on quadratic polynomials for obtaining i... |
| openness | 5 | 5 | exact (100%) | However, in this work we give general attacks on candidates that have this form. As these are some of the most natural approaches to refute Hypothesis 1, our wo... |
| definition | 4 | 4 | exact (100%) | Below we say that an n-variate polynomial q is Λ-bounded if all of q's coefficients are integers in the interval [−Λ, +Λ]. |
| progress | 7 | 7 | exact (100%) | In particular, we are not aware of any candidate construction of weak pseudorandom generator computed by quadratic polynomials that is not broken experimentally... |
| progress | 3 | 3 | exact (100%) | In fact, we do not know of any degree-2 construction that does not fall prey to a variant of the same attack. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Hypothesis 1 is genuinely in the paper (PDF p.4), is the paper's own, and genuinely stays open — Theorem 2 settles only the i.i.d.-nice case, and §7's Theorem 5 and 3SAT candidate are degree-3, so nothing later closes the degree-2 question. The single most important defect is quantifier order: the paper places \"then there exists an algorithm A\" after the polynomials, the input distribution and the noise distributions are fixed, whereas the draft hoists one fixed efficient A and one fixed constant c in front of the instance and asserts in the informal that a single distinguisher beats every family — a strengthening the paper does not make, and one the draft's own one_line silently contradicts. Two further repairable errors: the \"Equivalently\" gloss drops the Pr[Δ_i = z] < 0.9 condition (making it false as written), and the [JLS] paragraph in the setting is not supported by this paper at all.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 4 | Hypothesis 1 ("No expanding weak quadratic pseudorandom generators") appears verbatim in Section 1.2 on PDF p.4, with exactly the components the draft reproduces: quadratic Λ(n)-bounded polynomials with m ⩾ n^{1+ε}, a Λ(n)-bounded distribution X over Z^n, per-index Λ(n)-bounded noise Δ_i with P[Δ_i = z] < 0.9, and the two distributions (q_1,…,q_m, q_i(x)) vs (q_1,…,q_m, q_i(x)+δ_i). |
| openness | pass | 5 | The paper leaves it open and it stays open. P.5: "As these are some of the most natural approaches to refute Hypothesis 1, our work can be seen as providing some (partial) evidence to its veracity." Theorem 2 (p.5) settles only the i.i.d.-nice case; §6 (pp.14-18) is experimental, not a proof; §7 (pp.19-21) — Theorem 5's linearization attack and the 3SAT-based candidate — is entirely about degree-3, explicitly not degree-2. No later section, footnote, or table resolves the degree-2 hypothesis. |
| strength | fail | 4 | The main body of the formal statement tracks the paper clause by clause, but the appended "Equivalently:" paragraph silently drops the non-degeneracy condition on the noise: it says only "perturbed by bounded independent noise", omitting P[Δ_i = z] < 0.9. Without that clause the restatement is false (δ_i ≡ 0 is bounded independent noise and makes D_1 = D_2, so no distinguisher can have advantage c > 0). The paper is careful to state this both in Hypothesis 1 and in the following paragraph on p.4 ("some distribution Δ over integers that satisfies P[Δ = 0] ⩽ 0.9"). |
| quantifiers | fail | 4 | Quantifier order is inverted. The paper reads "For every ε > 0, polynomial Λ(n), sufficiently large n ∈ N, if: [q_1,…,q_m / X / Δ_i] … then there exists an algorithm A that can distinguish … with Ω(1) bias" — ∃A sits after the polynomials, the input distribution and the noise distributions are all fixed, so A may depend on them. The draft hoists it: "there exist a constant c > 0 and an efficient algorithm A such that the following holds for all sufficiently large n ∈ N. Let m …, let q_1,…,q_m …", making A a single distinguisher uniform over every instance and every large n. The informal restates this strengthening explicitly ("a single efficient distinguisher that achieves constant advantage against every such family, no matter how the polynomials and the input distribution were chosen"), while the draft's own one_line uses the paper's weaker order — the draft is internally inconsistent. |
| attribution | pass | 4 | This is the harvested paper's own hypothesis, not one it cites: "We consider the following general hypothesis that, if true, would rule out not just the three proposed approaches based on quadratic polynomials for obtaining iO, but also a great many potential generalizations of them." The related objects it is contrasted with (ΔRG of [2], pseudo flawed-smudging of [21]) are correctly attributed elsewhere in the draft. |
| definitions | fail | 5 | Λ-bounded polynomial and Λ-bounded distribution are reproduced exactly as the paper defines them (p.4), and those are the only notions Hypothesis 1 uses — so the conjecture statement itself is safe. But "nice" is misdescribed in status_note and progress_note as "(normalised, pairwise-independent coefficients)" / "mild normalisation and pairwise-independence conditions". Definition 1 on p.5 has three clauses, and the first requires Q to be supported on HOMOGENEOUS (no linear term) degree-2 polynomials with \|\|q\|\|_2^2 ⩽ C E\|\|q\|\|_2^2. Dropping homogeneity overstates the reach of the settled case. |
| fabrication | fail | - | The setting's closing paragraph about [JLS] (Jain-Lin-Sahai 2021) — that later degree-two iO constructions "evade attacks of this kind by sampling public data jointly with the secret seed, so that the effective polynomials depend on the secret", and that "such objects fall outside the quantification above" — has no basis in this 2018 paper; the reference list (pp.21-22) contains no such entry, as the draft's own bibliography admits. Two smaller unsupported claims: that [4,24] showed the SoS relaxation "recovers the seed" (p.3 says only that the candidates "can be broken using semidefinite programming"), and that "a proof of the conjecture would have to dispense with them entirely" (the draft's inference, not the paper's). |
| self-containment | pass | 4 | A reader who has never seen the paper could work from the statement alone: Λ-boundedness for polynomials, for the input distribution and for the noise are all defined in definitions_latex, advantage and efficiency are defined in notation_latex, and D_1, D_2 are written out in full. Nothing in the statement depends on an undefined paper-internal notion ("nice" appears only in the status and progress notes, not in the conjecture). |

### Unsupported by the paper

- The [JLS] paragraph in setting_latex: that later degree-two iO constructions "evade attacks of this kind by sampling public data jointly with the secret seed, so that the effective polynomials depend on the secret", and that "such objects fall outside the quantification above and are not refutations of it". The paper is from 2018 and its reference list (pp.21-22) contains no Jain-Lin-Sahai entry; the draft's own bibliography flags the citation as "recalled from memory; not in this paper's reference list".
- "the degree-two sum-of-squares relaxation recovers the seed", attributed to BBKK and Lombardi-Vaikuntanathan. P.3 says only that the Lin-Tessaro candidate and any generator with those parameters "can be broken using semidefinite programming" — breaking, not seed recovery.
- "a proof of the conjecture would have to dispense with them entirely, since the polynomials are adversarial" (about matrix RIP and Gross's incoherence). The paper observes on p.4 that Hypothesis 1's polynomials are arbitrary and on p.8 that its own proof routes through Gross's theorem, but nowhere states this consequence for a hypothetical proof.
- "whenever you have more than about $n$ polynomials in $n$ variables" (informal). The hypothesis requires m ⩾ n^{1+ε}, a polynomial factor above n, not "about n". The n(log n)^{O(1)} threshold belongs to Theorem 2 (p.5), which is the settled special case, not to the hypothesis.

### Corrections the checker asked for

- **formal_statement_latex** — The existential quantifier over the distinguishing algorithm is hoisted in front of the instance, strengthening the hypothesis. The paper places "then there exists an algorithm A" after m, q_1,…,q_m, X and the Δ_i have been fixed, so A is permitted to depend on them; the draft demands one fixed A that works against every family at every sufficiently large n.
  - suggested: Restructure as: "For every constant ε > 0 and every polynomially bounded Λ : N → N there is a constant c > 0 such that for all sufficiently large n ∈ N the following holds. Let m ⩾ n^{1+ε} …, let q_1,…,q_m be quadratic Λ(n)-bounded polynomials, let X be a Λ(n)-bounded distribution over Z^n, and for each i let Δ_i be a Λ(n)-bounded distribution over Z with Pr[Δ_i = z] < 0.9 for every z ∈ Z. Then there exists an efficient algorithm A with Adv_A(D_1, D_2) ⩾ c." The corresponding informal sentence must lose "a single efficient distinguisher … no matter how the polynomials and the input distribution were chosen" and instead read, as the draft's own one_line already does, that for every such family there is an efficient distinguisher.
- **formal_statement_latex** — The "Equivalently:" paragraph omits the condition Pr[Δ_i = z] < 0.9, which makes the restatement false: with δ_i ≡ 0 the two distributions coincide.
  - suggested: "… are computationally indistinguishable from those evaluations perturbed by bounded independent noise no one value of which is taken with probability 0.9 or more." (The paper's own gloss on p.4 keeps the condition: "some distribution Δ over integers that satisfies P[Δ = 0] ⩽ 0.9".)
- **status_note / progress_note / informal** — "Nice" is described as normalisation plus pairwise independence, omitting the first clause of Definition 1 (p.5), which also requires the distribution to be supported on homogeneous degree-2 polynomials — i.e. polynomials with no linear term. This overstates what the settled case covers.
  - suggested: "… drawn independently and identically from a \emph{nice} distribution: supported on homogeneous (no linear term) degree-2 polynomials with ||q||_2^2 ⩽ C·E||q||_2^2 for a constant C, with Var(Q_{i,j}) = 1 and with the coefficients Q_{i,j} pairwise independent."
- **setting_latex** — The final paragraph attributes to [JLS] (2021) a claim about later degree-two iO constructions sampling public data jointly with the secret seed. Nothing in this 2018 paper supports it, and the reference list contains no such entry.
  - suggested: Delete the paragraph, or relocate it outside the paper-sourced setting and mark it plainly as the harvester's own commentary postdating the paper.
- **setting_latex** — "Barak, Brakerski, Komargodski and Kothari [BBKK], and independently Lombardi and Vaikuntanathan [LV], then showed that no generator with those parameters can be secure: the degree-two sum-of-squares relaxation recovers the seed." The paper (p.3) says these works showed such generators "can be broken using semidefinite programming, and specifically the degree two sum of squares program" — it does not claim seed recovery.
  - suggested: "… showed that the Lin-Tessaro candidate, and indeed any generator with their required parameters, can be broken using the degree-two sum-of-squares semidefinite program."

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `JLS` — Jain, A., Lin, H., Sahai, A., *Indistinguishability obfuscation from well-founded assumptions*, STOC (recalled from memory; not in this paper's reference list) 2021

## Build

- pdflatex: ok
- chktex: 4 warnings
- lacheck: 2 warnings

## What to check hardest

Two points a reviewer should check hardest. (1) The paper writes "then there exists an algorithm $\mathcal{A}$ that can distinguish" without the word "efficient"; I have made polynomial time explicit, because the very next paragraph of the paper reasons about "an efficient algorithm to recover $x$", and because the accompanying Theorem 2 supplies a polynomial-time algorithm. Read literally without an efficiency requirement, the hypothesis is far weaker and arguably close to trivial, so this reading is almost certainly the intended one --- but it is a reading, not a transcription. (2) The paper's quantifier order is "For every $\varepsilon > 0$, polynomial $\Lambda(n)$, sufficiently large $n$, if ... then there exists an algorithm $\mathcal{A}$"; I have hoisted $\mathcal{A}$ and the constant $c$ out in front of $n$ and the instance, which is the only reading under which $\mathcal{A}$ is a distinguisher rather than an instance-dependent object (the polynomials are inputs to $\mathcal{A}$). Also: I believe this hypothesis is still open, and in particular that later degree-two iO constructions with jointly sampled public and secret seed do not refute it, because the hypothesis fixes the polynomials independently of the input distribution --- but I have not verified the current literature, and a reviewer should confirm no refutation has appeared. Finally, the paper does not upper-bound $m$; I have not imposed one, and efficiency is measured in the input length, which grows with $m$.

