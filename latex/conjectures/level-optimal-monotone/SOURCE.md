# Provenance: Level-Optimal Search Trees Beyond Disjunctive Queries

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Optimizing Trees for Static Searchable Encryption**
- Authors: Mohammad Etemad, Mohammad Mahmoody, David Evans
- Venue/archive: IACR Cryptology ePrint Archive 2018
- Identifier: 2018/052
- Bibliographic detail: inferred
- File: `2018-052.pdf` (24 pages)
- sha256: `577000f7aec5e8406cfaf027d3671e6a53799072f6b69e52ecf0b5fb9978d62c`
- Read on 2026-08-17T17:48:51Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Proved for every distribution supported on disjunctive queries (the paper's Theorem B.1), where the $\log n$ factor is also shown to be necessary. Open for every larger class, and in particular wide open for distributions over conjunctive queries, where the paper's proof technique demonstrably fails. The only other proved case is $\mathcal{Q}$ uniform over single keywords, and there the comparison is against the optimal balanced tree, not against $\mathrm{Opt}_{\mathcal{Q}}(L)$, and it needs $n$ even plus a density hypothesis.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| openness | 23 | 23 | exact (100%) | On the other hand, our empirical results for larger n (see Section 4) also suggests a close relation between the balanced and unbalanced tree as our best-first ... |
| statement | 22 | 22 | exact (100%) | Our level-optimal algorithm (Algorithm 2) is optimal up to a logarithmic factor among all (even unbalanced) trees when Q is any distribution over disjunctive qu... |
| progress | 22 | 22 | exact (100%) | Note that in Theorem B.1 we cannot decrease the approximation factor to o(log n). |
| progress | 10 | 10 | exact (100%) | If qo is evaluated true at any internal node u, there is at least one leaf node satisfying qo on the subtree rooted at u. This is not the case for qa since w1 a... |
| definition | 6 | 6 | exact (100%) | Our second algorithm produces balanced OR trees with depth log(n), eliminating any shape leakage. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is genuinely the authors' own and genuinely open — p23 states it verbatim and nothing in Appendix B, the tables, or the Open questions section resolves it. But the paper conjectures the bound for "a broader class of query distributions" and pointedly names no class, whereas the draft's formal statement, title and one-line commit to every distribution over all monotone formulas — the maximal class, and precisely the "natural generalization" the strength check exists to catch; the draft's own informal paragraph says "a wider class", contradicting its own formal statement. Compounding this, the draft misreports the n = 8 exhaustive search as covering all 135,135 trees when p13 restricts that 4-of-25 figure to balanced trees, and attributes to the paper an Omega(m log n) lower bound on every balanced tree that p22 asserts only for the level-optimal output under a single-keyword distribution.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 23 | The paper explicitly conjectures this: "Thus, we conjecture that a more general theorem (than our Theorem B.1) holds for a broader class of query distributions." (p23, immediately after the "Theorem B.1 is optimal" paragraph). Theorem B.1 itself, the object being generalized, is on p22. |
| Openness | pass | 16 | Nothing later resolves it. Appendix B contains only Theorem B.1 (disjunctive Q, p22) and Theorem B.2 (uniform single-keyword Q against OptBal, p23); the proofs end on p24 with Claim B.3. The Open questions section (p16) leaves further theoretical analysis to future work. No table, footnote or appendix supplies a conjunctive or general-monotone result. |
| Strength | fail | 23 | The paper conjectures the bound for "a broader class of query distributions" and names no class. The draft's formal statement quantifies over "every distribution Q over M_m" — all monotone formulas, the maximal class — and carries that into the title, subtitle and one_line ("for arbitrary monotone query distributions"). The draft's own informal paragraph says "a wider class", contradicting its formal statement. The conjecture is motivated on p23 by the Section 4 experiments, which cover only AND/OR of two and three keywords (p12-14), not arbitrary monotone formulas. |
| Quantifiers and parameters | fail | 22 | Two deviations. (a) Definition B.2 (p22) defines T_LO(L) as a single tree, "the tree that is the result of running our level-optimal algorithm"; the draft defines LO(L,Q) as the set of all trees obtainable over all choices of minimum-weight matching and asserts the bound for every member — a strengthening the paper does not state. (b) The draft asserts an absolute constant c independent of m, n, L and Q; Theorem B.1's O(.) is consistent with this for the disjunctive case (Proof B.4 gives SLC_q(T_d) <= d*SLC_q(T) pointwise), but the paper commits to nothing about constants for the conjectured extension. |
| Attribution | pass | 23 | "we conjecture" — first person, the authors' own, generalizing their own Theorem B.1. Not a problem borrowed from a cited work. |
| Definitions | pass | 5 | OR tree (Definition 3.1, p5), full binary trees only (p5), P_Q(u) = Pr_{q<-Q}[q(u)=1] (p6), Algorithm 2 with minimum-total-weight perfect matching via Blossom (p7), SLC/Opt/OptBal (Definition B.2, p22), monotone formulas M (Lemma B.1, p21) all match the draft's usage. Balanced = depth ceil(log n) matches OptBal on p22. |
| Fabrication | fail | 13 | Three unsupported assertions. (i) p13: the 4-of-25 exhaustive-search figure is over all BALANCED trees, not "all 135,135 trees"; over all trees it is the best-first algorithm that is beaten, in 13 of 25, by 0.09. (ii) p22: the lower-bound family shows the level-optimal solution costs ~2m log n against the best-first solution's <2^{n+2}~4m under a uniform SINGLE-KEYWORD Q; the paper does not claim "every balanced tree costs Omega(m log n)", and the draft omits the single-keyword restriction. (iii) The Omega(n) gap between an arbitrary balanced tree and Opt, the alternative root-grouping of the Female/Dept2 example, and "any proof must use a property of the matchings" appear nowhere; p10 is a leakage discussion and says only that a conjunctive query can hold at u with no satisfying leaf below. Additionally, level-optimal was run only for n <= 2^10 (p12); the 2^14 points are the hybrid algorithm. |
| Self-containment | pass | - | Given the notation and definitions blocks, a reader who has not seen the paper knows what object to bound and against what. No evidence needed from the paper for this check. |

### Unsupported by the paper

- "an exhaustive search over all 135,135 trees on n = 8 leaves finds trees better than the level-optimal one in only 4 of 25 trials" — p13 states the 4-of-25 figure for exhaustive search over all BALANCED trees; over all trees it is the best-first tree that is beaten, in 13 of 25.
- "every balanced tree costs Omega(m log n)" in the lower-bound family — p22 asserts this only of the level-optimal solution, and only for a uniform single-keyword Q, a restriction the draft drops.
- "for conjunctive Q the gap between an arbitrary balanced tree and Opt_Q(L) can be Omega(n)" — this quantitative gap is nowhere in the paper; p10 discusses the Female/Dept2 example purely as leakage of extra visited nodes.
- "grouping the two halves under the two children of the root (also a balanced tree) makes only the root satisfy the query" — the paper gives only the alternating-leaf arrangement (p10); the alternative arrangement and its cost are the drafter's own construction.
- "any proof of the conjecture must use a property of the matchings that Definition 3.1 actually computes rather than only the height of the tree" — the paper makes no such claim anywhere.
- "the experiments (Enron corpus, n up to 2^14 ...) show the level-optimal trees tracking the best-first trees closely" — the level-optimal algorithm was run only for n <= 2^10 (p12).
- Framing the p10 conjunctive/disjunctive contrast as the paper explaining why the Theorem B.1 proof technique fails — p10 (Section 3.5, Leakage) predates Appendix B and never mentions Theorem B.1 or its proof.

### Corrections the checker asked for

- **formal_statement_latex, title, subtitle, one_line** — The draft states the bound for every distribution over M_m (all monotone formulas). The paper (p23) conjectures only "a more general theorem ... for a broader class of query distributions" and never names the class; the motivating experiments cover AND/OR of two and three keywords only.
  - suggested: State the conjecture as: there is a class C of query distributions strictly containing the disjunctive ones — the paper does not specify which — for which SLC_Q(T_LO(L)) = O(log n * Opt_Q(L)). The all-monotone version must be labelled explicitly as the drafter's maximal formalization, not as the paper's statement, and the title/subtitle must drop "for arbitrary monotone query distributions".
- **setting_latex, progress_note** — "an exhaustive search over all 135,135 trees on n = 8 leaves finds trees better than the level-optimal one in only 4 of 25 trials" conflates two distinct comparisons on p13.
  - suggested: Exhaustive search over all BALANCED trees on n = 8 finds a better tree than the level-optimal one in 4 of 25 experiment sets, worst-case difference 0.07; exhaustive search over all 135,135 trees finds a better tree than the BEST-FIRST one in 13 of 25, difference 0.09.
- **setting_latex, progress_note** — "the best-first tree costs O(m) while every balanced tree costs Omega(m log n)" attributes to the paper a claim about all balanced trees, and omits which Q the example uses (p22).
  - suggested: For n files with disjoint keyword sets, the i-th having 2^{i-1} keywords (m = 2^n - 1), and Q uniform over single keywords, the best-first solution costs less than 2^{n+2} ~ 4m while the LEVEL-OPTIMAL solution costs 2(2^n - 1) log n ~ 2m log n, so SLC(T_LO)/SLC(T_BF) = Omega(log n).
- **notation_latex, definitions_latex, formal_statement_latex** — LO(L,Q) is defined as the set of all outputs over all minimum-weight matchings and the bound is asserted for every T in it. Definition B.2 (p22) writes T_LO(L) as a single tree.
  - suggested: Either state the bound for T_LO(L) as the paper does, or flag the every-matching quantification as a deliberate strengthening of the paper's formulation.
- **setting_latex** — "the experiments (Enron corpus, n up to 2^14 ...) show the level-optimal trees tracking the best-first trees closely" — the level-optimal algorithm was run only for n <= 2^10 (p12); beyond that point Figure 5 plots the hybrid algorithm.
  - suggested: Level-optimal and best-first were compared for n <= 2^10; the hybrid algorithm was used for n > 2^10, up to n = 2^14 in Figure 5.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The main thing to check is whether the statement is the paper's. The paper writes only that it conjectures "a more general theorem ... holds for a broader class of query distributions" and does not name the class; I have taken the largest class available in the paper's own framework, all distributions over monotone Boolean formulas, which is where the algorithms are defined and where the experiments live. A reviewer may reasonably prefer the version restricted to distributions over conjunctive queries — that is the case the paper repeatedly singles out as the hard and interesting one, and settling it would in my view discharge the paper's intent. Second, the conjecture is about the algorithm's output, not about balanced trees in general: for disjunctive queries Theorem B.1 happens to hold for every balanced tree, but for conjunctive queries that is false (the paper's Female/Dept2 example gives an $\Omega(n)$ gap for a badly arranged balanced tree), so I have quantified over the trees the algorithm can output. That reading is mine, though it is forced if the statement is to be non-trivial. Third, the algorithm's output is not unique when several minimum-weight perfect matchings tie, and I have asked for the bound for all of them; a proof that only covers some canonical tie-breaking would be a partial answer worth reporting as such. Finally, I have not found a resolution in the literature, but this is a 2018 ePrint report that appears not to have been widely followed up, so the possibility that someone has settled the conjunctive case in the intervening years should be checked before publishing.

