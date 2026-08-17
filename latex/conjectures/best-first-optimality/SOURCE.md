# Provenance: A Constant-Factor Guarantee for Huffman-Style Search Tree Construction

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

`paper-states-open`. Nothing is proved about the best-first algorithm's approximation ratio, for any class of query distributions. The paper's exhaustive experiments show it is not exactly optimal, so the exact-optimality version is already refuted; the approximation-ratio version is untouched. The paper's proved bounds all concern the level-optimal algorithm instead.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| openness | 16 | 16 | exact (100%) | However, a theoretical analysis of the optimality of our best first and hybrid algorithms are left as interesting directions for future work. |
| statement | 16 | 16 | exact (100%) | Our experimental analysis of our algorithms in Section 4 suggest that when it comes to real data, all our algorithms lead to search time that beat random trees ... |
| progress | 13 | 13 | exact (100%) | Similarly, our best-first algorithm finds search trees very close in cost to the optimum tree. Checking all possible trees found slightly better trees in 13 out... |
| progress | 16 | 16 | exact (100%) | As we showed, when it comes to small number of files, an exhaustive search shows that our best-first algorithm is very close to being optimal. |
| definition | 6 | 6 | exact (100%) | Our first approach is inspired by the idea behind the Huffman codes and leads to potentially unbalanced trees. |
| definition | 6 | 6 | exact (100%) | At each step, we choose to match a pair that gives us a parent node z with minimum “local cost” PQ (z) among all possible choices of z that are available at the... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's own and genuinely open: p. 16 leaves \"a theoretical analysis of the optimality of our best first and hybrid algorithms\" to future work, and Appendix B.2 proves bounds only for the level-optimal algorithm (Theorems B.1 and B.2, pp. 22-23), so nothing later closes it. The single most important defect is in the setting, which claims the paper's proofs cover \"its other two algorithms, which build the tree level by level using a minimum-weight perfect matching\": the paper proves nothing about the hybrid algorithm, leaves it open in the same sentence as best-first, and says on p. 7 that it deliberately avoids Blossom's matching. That plus the misdescribed n=8 experiment (25 experiment sets, not 25 random file sets) and the \"all three heuristics\" overstatement are precisely repairable; separately, the draft's universal worst-case constant factor is stronger than the paper's expectation, which is hedged to \"real data.\"

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 16 | The Open questions paragraph on p. 16 poses exactly this: "However, a theoretical analysis of the optimality of our best first and hybrid algorithms are left as interesting directions for future work," together with the expectation that the algorithms are "probably within a constant factor of optimal search produced by optimal search trees." The best-first algorithm is Algorithm 1 (p. 6); SLC_Q and Opt_Q are Definition B.2 (p. 22). Both quotes the draft attributes to p. 16 are verbatim. |
| openness | pass | 22 | Reading past p. 16: Appendix B.2 contains only Theorem B.1 (level-optimal, O(log n) against Opt, disjunctive Q, p. 22) and Theorem B.2 (level-optimal, constant factor against OptBal, uniform single-keyword Q, n even, alpha > 1/2, p. 23). Neither concerns best-first; best-first appears on p. 22 only as the cheap side of the tightness example for B.1. The conjecture on p. 23 is about broadening Theorem B.1 to more query distributions, still for level-optimal. No bound on best-first's ratio anywhere in the paper, so the question stays open through the appendix. |
| strength | unclear | 16 | The paper's constant-factor expectation is explicitly qualified "when it comes to real data"; the draft renders it as a universal worst-case bound over every m, n, L and Q. The open item the paper actually poses is the vaguer "a theoretical analysis of the optimality," which admits a worst-case approximation-ratio formalization (the paper's own theorems are worst-case), and the draft is candid that an unbounded-ratio workload also settles it. But the paper's proved constant-factor analogue (Thm B.2, p. 23) is against OptBal under a density condition, not against Opt, so the draft's version is stronger than anything the paper asserts. I cannot settle from the paper whether the authors intended the universal worst-case reading. |
| quantifiers | pass | 22 | Opt_Q(L) is correctly the minimum over all possibly unbalanced OR trees on L (Definition B.2, p. 22: "the optimal (average) search cost among all (possibly unbalanced) OR trees for given leaves L"), SLC_Q(T) is correctly the sum of P_Q(u) over internal nodes, c is absolute, and no height restriction is imposed on either side, matching the paper. One deviation: the draft quantifies over every tree obtainable under any tie-breaking of the greedy step, whereas the paper's T_BF(L) is the single tree its algorithm returns; since Algorithm 1 (p. 6) does not specify tie-breaking, this is the only well-defined version, but it is formally stronger. |
| attribution | pass | 16 | The open question is the harvested paper's own, stated in its own Open questions paragraph about its own Algorithm 1, not a problem it attributes to anyone else. The five bibliography entries the draft carries (Goh03=[18], KP13=[21], BlindSeer=[36], Meh75=[30], Nag97=[33]) all appear in the paper's reference list with the venues and years as printed (pp. 16-18), and the BST analogy is the paper's own framing on p. 3. |
| definitions | pass | 5 | OR tree matches Definition 3.1 (p. 5) plus the paper's convention of working only with full binary trees; monotone formulas match Lemma B.1 (p. 21) and the Algorithm 1 input spec (p. 6); P_Q(u) = Pr_{q<-Q}[q(u)=1], SLC_Q, Opt_Q match Definition B.2 (p. 22); the best-first definition matches Algorithm 1 line by line. The 1+2*SLC identity in the setting is Lemma B.3 (p. 21), the product (2i-1) count is p. 13, and the HW(u)/m specialization for uniform single keywords is p. 8. Renamed notation only (M_m, BF(L,Q)), nothing redefined. |
| fabrication | fail | 7 | Three unsupported assertions. (i) The setting says "What the paper proves instead concerns its other two algorithms, which build the tree level by level using a minimum-weight perfect matching" - the paper proves nothing about the hybrid algorithm, which p. 16 leaves open alongside best-first, and p. 7 states the hybrid "uses a heuristic matching algorithm based on our first algorithm, rather than running Blossom's algorithm." (ii) The n=8 exhaustive experiment is described as "repeated on 25 random file sets"; p. 13 and Table 2 (p. 19) show five randomly selected file sets crossed with five query distributions, i.e. 25 experiment sets, not 25 file sets. (iii) The progress note's "lowest cost of all three heuristics" overstates Table 1 and Appendix A (p. 18), which compare best-first against level-optimal and random trees only; the hybrid was run only for n > 2^10 and never compared against best-first on the same data. |
| self-containment | pass | - | The formal statement together with the notation and the two definitions is closed: leaf labels, the local cost, SLC, Opt over all OR trees, and the greedy procedure are all spelled out, so a reader who has never opened the paper knows what has to be proved or refuted. No evidence needed from the paper for this check. |

### Unsupported by the paper

- Setting: that the paper's proved bounds cover "its other two algorithms" (level-optimal and hybrid). The paper proves results only for the level-optimal algorithm (Theorems B.1, B.2, pp. 22-23); p. 16 explicitly leaves the hybrid open together with best-first. The draft's own status_note contradicts its setting on this point.
- Setting: that the hybrid algorithm builds its tree "using a minimum-weight perfect matching." Page 7: it "uses a heuristic matching algorithm based on our first algorithm, rather than running Blossom's algorithm."
- Setting: that the n=8 exhaustive comparison was "repeated on 25 random file sets." The paper (p. 13, Table 2 on p. 19) reports 25 experiment sets = five randomly selected eight-file sets x five query distributions.
- Progress note: that best-first has the lowest cost "of all three heuristics." Table 1 / Appendix A (p. 18) compare best-first only against the level-optimal algorithm and random trees; the hybrid is run only for n > 2^10 (p. 12).

### Corrections the checker asked for

- **setting_latex** — "What the paper proves instead concerns its other two algorithms, which build the tree level by level using a minimum-weight perfect matching." The paper proves nothing about the hybrid algorithm - p. 16 leaves "our best first and hybrid algorithms" open together - and the hybrid does not use minimum-weight perfect matching: p. 7 says it "uses a heuristic matching algorithm based on our first algorithm, rather than running Blossom's algorithm."
  - suggested: What the paper proves instead concerns only its second algorithm, the level-optimal algorithm (Algorithm 2), which builds the tree level by level using Blossom minimum-weight matching; the hybrid algorithm is left unanalyzed alongside best-first.
- **setting_latex** — "on the largest exhaustively checkable instance ($n=8$, all $135{,}135$ trees enumerated, repeated on 25 random file sets)". Page 13 and Table 2 (p. 19) describe five groups of experiments - one single-keyword and four Boolean - on five randomly selected sets of eight files, giving 25 experiment sets in total, not 25 file sets.
  - suggested: on the largest exhaustively checkable instance ($n=8$, all $135{,}135$ trees enumerated, across 25 experiment sets: five randomly selected sets of eight files crossed with five query distributions)
- **progress_note** — "the best-first tree has the lowest cost of all three heuristics in almost all experiment groups". Table 1 and Appendix A (p. 18) compare best-first only against the level-optimal algorithm and against 100 random trees; the hybrid algorithm was used only for $n > 2^{10}$ (p. 12) and is never compared with best-first on the same data.
  - suggested: the best-first tree has the lowest cost of the two of the paper's algorithms compared there - it beats the level-optimal tree in every experiment group of Table 1 and roughly halves the cost of a random tree; the hybrid algorithm is run only for $n > 2^{10}$ and is never compared against best-first.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The strength of the statement is the thing to check hardest. The paper leaves open "a theoretical analysis of the optimality" of best-first without stating a target bound; the constant factor comes from the neighbouring sentence, which says all the paper's algorithms are "probably within a constant factor of optimal", and that sentence is hedged with "when it comes to real data". A worst-case constant-factor claim over all monotone $\mathcal{Q}$ is therefore the maximal reading, and it may well be false — a counterexample would settle the problem but would not contradict anything the paper asserts. Reviewers who want a version closer to what the paper proves elsewhere should consider $\mathcal{Q}$ uniform over single keywords, where the objective is total Hamming weight of the internal labels; that special case is the natural first target and I would regard it as the real content. Second, greedy is only defined up to tie-breaking and I quantify over all minimizing choices; a bound for a canonical tie-break would be a partial answer. Third, unlike the other candidate this problem comes with no obstruction named by the authors: the only evidence about difficulty is that greedy is not exactly optimal and that the paper's own layered proof technique does not apply to an unlayered algorithm, the latter being my reading of their proof rather than their statement. Finally, the general problem of computing $\mathrm{Opt}_{\mathcal{Q}}(L)$ may be NP-hard, which the paper never discusses; that would not affect the conjecture, which is about an approximation ratio, but a solver should be aware of it.

