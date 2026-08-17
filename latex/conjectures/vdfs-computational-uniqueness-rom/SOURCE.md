# Provenance: Ruling Out Computationally Unique VDFs in the Random Oracle Model

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Can Verifiable Delay Functions be Based on Random Oracles?**
- Authors: Mohammad Mahmoody, Caleb Smith, David J. Wu
- Venue/archive: Cryptology ePrint Archive (full version of the ICALP 2020 paper; subsumes the earlier note "A Note on the (Im)possibility of Verifiable Delay Functions in the Random Oracle Model") 2019
- Identifier: 2019/663
- Bibliographic detail: printed-on-page
- File: `2019-663.pdf` (19 pages)
- sha256: `8736041bbe2cc1feaa60cc31b8e8deee7ae6323ecff10a7c0383e641e6501569`
- Read on 2026-08-17T18:38:25Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Settled by the paper: perfect uniqueness with perfect completeness (impossible for every $\sigma \ge 2(s+t)$), and the tight regime $\sigma > T \cdot (1 - 1/2(s+t))$ or $\sigma = T - T^{\rho}$ even without uniqueness. Open: the same impossibility under computational uniqueness, which is the notion the definition of a VDF actually requires. The paper additionally asks, in the same sentence, that such an extension also tolerate negligible completeness error; the conjecture as stated here keeps perfect completeness, matching the hypotheses of the paper's first lower bound.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | The main open question remaining is whether a similar lower bound for computational uniqueness holds for VDF in the ROM or not. |
| openness | 17 | 17 | exact (100%) | The main open question remaining is whether we can extend our first lower bound to rule out VDFs satisfying computational uniqueness in the ROM, and ideally do ... |
| openness | 4 | 4 | exact (100%) | Observe that this argument critically relies on perfect uniqueness. |
| openness | 5 | 5 | exact (100%) | At the same time, we note that (even publicly-verifiable) proofs of sequential work do exist in the non-tight regime (e.g., σ = T /2) in the ROM [MMV13]. Thus, ... |
| definition | 7 | 7 | exact (100%) | We say that ΠVDF is computationally unique if A is the class of poly(λ, T )-time adversaries and ε(λ) is negligible. |
| parameter | 8 | 8 | exact (100%) | In particular, for sequentiality, we measure the running time of the adversary by the number of rounds of oracle queries the adversary makes (this is to model t... |
| progress | 8 | 8 | exact (100%) | In this section, we first show that perfectly unique VDFs (Definition 2.3) are impossible in the random oracle model. Then, as a corollary, we obtain barriers f... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's own and genuinely open: it is posed verbatim on p.4, re-posed as \"The main open question remaining\" in the Conclusion (p.17), and nothing in Sections 3 or 4 touches it — Theorem 3.1 covers only perfect uniqueness and Theorems 3.6/4.1 cover only the tight regime with no uniqueness assumption. The statement, its quantifiers and its definitions survive a clause-by-clause comparison against Defs 2.2, 2.3, 2.4 and 2.9 (pp.6-8), and all seven quotes are exact and correctly paged. What fails is check 7: the setting prose states the perfect-uniqueness attack runs in 2(s+t)+1 rounds where Theorem 3.1 (p.8) says 2(s+t) — contradicting the draft's own progress note — and it attributes to the paper a key-agreement analogy that appears nowhere in it and is false as stated.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 4 | Located verbatim on p.4: "Observe that this argument critically relies on perfect uniqueness. The main open question remaining is whether a similar lower bound for computational uniqueness holds for VDF in the ROM or not." Restated in the Conclusion, p.17. The draft's quotes at p.4, p.5, p.7, p.8 and p.17 are all exact and on the pages claimed. |
| openness | pass | 17 | Read past the introduction: Section 3.1 (Theorem 3.1, p.8) settles only perfect uniqueness; Section 3.2 (Theorem 3.6, Cor 3.7, p.11) and Section 4 (Theorem 4.1, Cor 4.2, p.15; random permutation model, p.16) settle only the tight regime and assume no uniqueness at all. The Conclusion (p.17) re-poses it as "The main open question remaining". Nothing in the paper resolves computational uniqueness in the non-tight regime. |
| strength | pass | 8 | The drafted statement is the analogue of Theorem 3.1 (p.8) with perfect uniqueness replaced by computational uniqueness — exactly what p.17 asks ("extend our first lower bound to rule out VDFs satisfying computational uniqueness"). It is not strengthened: it allows any universal polynomial p(lambda,s,t) rounds where Theorem 3.1 achieves the concrete 2(s+t). It is weakened in one disclosed respect — the paper adds "and ideally do so allowing negligible completeness error as well" (p.17), and the draft keeps gamma = 0; the status_note states this explicitly, and the p.4 formulation of the question carries no completeness clause. |
| quantifiers-parameters | pass | 7 | Checked symbol by symbol. Uniqueness (Def 2.3, p.7): adversary class poly(lambda,T)-time, error negligible, adversary outputs (x,y,pi) after seeing pp — draft matches, including the crucial Def 2.9 clause (p.8) that the probability is over Setup and adversary coins but not over the oracle, which the draft renders as "for every fixed O" (supported by p.8: "if a VDF in the ROM is perfectly unique, it means that for every sampled random oracle O, perfect uniqueness holds"). Sequentiality (Def 2.4, p.7): both Adv_0 and Adv_1 in total time poly(lambda,T), only Adv_1 bounded in parallel time by sigma, success = negl — draft matches. The monotonicity remark (breaking sigma-sequentiality also breaks sigma'-sequentiality for sigma' >= sigma) is correct. s and t are the query counts of Setup and Verify per p.6 and Theorem 3.1 (p.8). |
| attribution | pass | 17 | This is the harvested paper's own question, not one it credits elsewhere: "The main open question remaining is whether we can extend OUR FIRST lower bound to rule out VDFs satisfying computational uniqueness in the ROM" (p.17, emphasis on the possessive). The related open question about extending the tight lower bound (p.5) is also the paper's own and is correctly kept separate in the draft. |
| definitions | pass | 7 | Perfect completeness (Def 2.2, p.6), computational uniqueness (Def 2.3, p.7), perfect uniqueness as the epsilon=0 unbounded case (p.7, matching the existential phrasing on p.3), sigma-sequentiality (Def 2.4, p.7) and the ROM conventions (Def 2.7/Remark 2.8/Def 2.9, pp.7-8) are all rendered accurately. One deviation, immaterial: the draft says sigma may depend on lambda, T, s and t, where Def 2.4 says "lambda, T and t". The widening is forced by the paper's own usage (Theorem 3.1's 2(s+t) rounds, p.8; Cor 3.7's sigma = T(1-1/2(s+t)), p.11) and does not change what would count as a proof, since the conjecture pins sigma = p(lambda,s,t) explicitly. |
| fabrication | fail | 8 | Three unsupported assertions, all in setting_latex. (i) "after 2(s+t)+1 such rounds a majority vote" contradicts Theorem 3.1 (p.8), which gives 2(s+t) ROUNDS: Algorithm 1 (p.10) sets d = 2(s+t)+1 EMULATIONS but queries the real oracle only for i < d. The draft's own progress_note says 2(s+t), so the draft contradicts itself. (ii) "in the same sense that key agreement cannot [be based on ideal hash functions]" appears nowhere in the paper; [BM17] is cited only for epsilon-heavy queries (p.15), and its content is that Merkle-style key agreement from random oracles DOES exist up to a quadratic gap. (iii) "A proof would show that VDFs cannot be based on ideal hash functions in a black-box way at all" overreaches: the conjecture as drafted retains perfect completeness, and p.17 flags negligible completeness error as a further, unresolved desideratum. Everything else in the setting, status and progress notes traces to the paper (Prop 3.2 p.9; Claim 3.3 p.10; Thm 3.6/Cor 3.7 p.11; Thm 4.1/Cor 4.2 p.15; sec 4.2 p.16; PoSW at sigma=T/2 p.5). |
| self-containment | pass | - | The formal statement supplies its own Definitions 1-3 and defines lambda, T, s, t, sigma, gamma and p in the notation block; a reader who has never opened the paper knows precisely what object to build or rule out. No page evidence applies — this is a property of the draft. |

### Unsupported by the paper

- setting_latex: "after 2(s+t)+1 such rounds a majority vote over the simulated outputs returns the true value" — Theorem 3.1 (p.8) states 2(s+t) rounds of queries; 2(s+t)+1 is the number of emulations in Algorithm 1 (p.10), not rounds.
- setting_latex: "in the same sense that key agreement cannot" — no such claim or analogy appears anywhere in the paper; [BM17], the only key-agreement-from-random-oracles reference, is cited solely for the epsilon-heavy-query technique (p.15).
- setting_latex: "A proof would show that VDFs cannot be based on ideal hash functions in a black-box way at all" — unsupported as stated; p.17 explicitly leaves the negligible-completeness-error case outside what such a proof would cover.
- setting_latex: "any lower bound for non-tight parameters must therefore consume the uniqueness property" — the paper says only that "it is not clear whether our lower bound for PoSW can be extended to rule out (non-tight) VDFs" (p.3) and calls it "an intriguing open question" (p.5); the necessity claim is the draft's inference, not the paper's assertion.

### Corrections the checker asked for

- **setting_latex** — "after each simulated execution asks all previously unasked queries to the real oracle in a single round; after 2(s+t)+1 such rounds a majority vote" — off by one against Theorem 3.1 (p.8), which gives 2(s+t) rounds, and against the draft's own progress_note. Algorithm 1 (p.10) has d = 2(s+t)+1 emulations, with a real-oracle round only for i < d.
  - suggested: "...; after 2(s+t)+1 such simulated executions, using 2(s+t) rounds of real-oracle queries, a majority vote over the simulated outputs returns the true value."
- **setting_latex** — "in the same sense that key agreement cannot" — the paper never makes this comparison, and the claim is inaccurate on its own terms (Merkle-puzzle key agreement exists relative to a random oracle; [BM17] is cited only for epsilon-heavy queries, p.15).
  - suggested: Delete the clause: "A proof would show that VDFs with perfect completeness cannot be based on ideal hash functions in a black-box way."
- **setting_latex** — "A proof would show that VDFs cannot be based on ideal hash functions in a black-box way at all" — "at all" overstates what the drafted conjecture yields, since it keeps perfect completeness and the paper separately asks for the negligible-completeness-error extension (p.17).
  - suggested: "A proof would rule out black-box constructions of computationally unique VDFs with perfect completeness from ideal hash functions, leaving only the negligible-completeness-error case that the paper additionally asks for."

## Build

- pdflatex: ok
- chktex: 3 warnings
- lacheck: 0 warnings

## What to check hardest

First, resolution status. The problem was posed in 2019 (ICALP 2020) and I am not aware of a published resolution, but I have not verified this against the post-2020 literature; a reviewer should check for later work on random oracle lower bounds for VDFs before publishing. Second, the round bound. The paper says only that it would like to "extend our first lower bound"; it does not commit to a bound on the attacker's rounds, so the universal polynomial $p(\lambda, s, t)$ in the statement is my rendering of what extending Theorem 3.1 would mean. Someone who proved impossibility with a worse but still $o(T)$ round bound should count as having settled it. Third, and most worth checking hardest, the quantifier order in computational uniqueness. Following the paper's Definition 2.9, the uniqueness probability is taken over the coins of setup and of the adversary but not over the choice of oracle, so my Definition 2 imposes the bound for every fixed oracle against every query-bounded adversary. This is a strong reading, and a version quantified with high probability over the oracle instead would be a formally different (and arguably more standard) conjecture; the paper's model choice is explicit, so I followed it, but a reader should be aware the two are not obviously equivalent. Fourth, scope: the statement keeps perfect completeness, so it does not by itself answer the paper's "ideally" clause about negligible completeness error.

