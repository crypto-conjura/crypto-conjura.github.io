# Provenance: A Dream Direct Product Theorem for a Moderately Hard Function

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Permissionless Consensus from a Common Random String**
- Authors: Damiano Abram, Marshall Ball, Juan Garay, Aggelos Kiayias
- Venue/archive: IACR Cryptology ePrint Archive; abridged version to appear in Proc. CRYPTO 2026 2026
- Identifier: 2026/1179
- Bibliographic detail: inferred
- File: `2026-1179.pdf` (33 pages)
- sha256: `46e589c2543acf0ca95cac43329b4b41aee4090496d733dfcb72855ceac255b3`
- Read on 2026-08-18T17:26:34Z via the `cli` backend

## How the paper leaves it open

`paper-asks-question`. Open. The paper reduces its consensus protocol to a proof of work with these parameters (Corollary 3), reduces that in turn to a moderately hard function via a subexponentially sound SNARG for P, and then leaves the construction of such a function from standard complexity conjectures explicitly open. Nothing later in the paper or its appendices supplies a candidate; the paper only remarks that ad hoc puzzles in current use are likely to satisfy the requirement.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| openness | 23 | 23 | exact (100%) | For example, can one show a (tight) “dream” strong direct product theorem for some function assuming, say, NSETH? |
| statement | 16 | 16 | exact (100%) | We note that given any function f that is moderately-hard (Def. 14) with parameters as required by Corollary 3 but not necessarily efficiently verifiable, can b... |
| progress | 4 | 4 | exact (100%) | Notice that not all proofs of work satisfy this property. Moreover, we cannot even hope to rely on complexity leveraging: If we select the security parameter of... |
| parameter | 4 | 4 | exact (100%) | The existence of a PoW with the properties we desire is nevertheless feasible. Indeed, observe that the candidate ad hoc constructions that are currently in use... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's and genuinely open: it is stated in Section 5, \"Extensions and Open Questions\" (pp. 22-23), tied to Corollary 3's epsilon(t,lambda) = 2^{-t*n^gamma} on p16, and nothing in the remaining sections or in Appendices A and B supplies a candidate. But the draft's central definition is not the paper's: Definition 14 on p27 contains no clause excluding z_1,...,z_t from the adversary's oracle queries, and the draft both inserts that clause and invents a rationale for it — the analogous restriction exists only in Definition 5 (p14), for multi-verifier signatures of work. Two further parameter constraints (s <= r(s,lambda) <= s*poly(lambda) and 1/beta(s,lambda) <= poly(lambda), the latter cutting against p5's lim_{lambda->infinity} beta = 0) and the entire NSETH definition with its \\cite{CGIMPS16} are supplied from outside the paper, which names NSETH exactly once, on p23, undefined and uncited.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 23 | The problem is posed in Section 5 (Extensions and Open Questions), in a sentence spanning pp. 22-23: "constructing this moderately (very) hard function from standard complexity conjectures is an interesting open problem in hardness amplification. For example, can one show a (tight) "dream" strong direct product theorem for some function assuming, say, NSETH?" The supporting reduction is on p16 (Corollary 3 plus the SNARG-for-P remark). All four of the draft's quotes are verbatim and on the pages claimed. |
| Openness | pass | 22 | It sits in the paper's final section, explicitly headed "Extensions and Open Questions", and is introduced as "an interesting open problem". Nothing after it resolves it: pp. 23-25 are acknowledgments and references; Appendix A (pp. 26-27) is background definitions (DDH, LWE, signatures, Defs 12-14 for proofs of work, NIZK); Appendix B (pp. 28-33) proves Theorems 1, 2 and 6 only. No candidate function, no partial construction, no table of results. The paper's only remark toward it is the negative-flavoured p4 observation that ad hoc deployed puzzles are "likely to satisfy our needs". |
| Strength | pass | 16 | The paper frames the DPT question as an instance of the construction problem it just stated, and Corollary 3 (p16) fixes the target as epsilon(t,lambda) = 2^{-t*n^gamma} for a constant gamma > 0 with challenge space {0,1}^{n(lambda)}, which the draft's formal statement reproduces exactly, including the quantification over every t <= d_0(lambda). Merging "construct this moderately (very) hard function from standard complexity conjectures" with "a (tight) dream strong DPT ... assuming, say, NSETH" into one statement is defensible, since the paper presents the second as an example of the first. Note the draft's clause-level renaming of Corollary 1/2's gamma to gamma' is legitimate, not a redefinition. |
| Quantifiers and parameters | fail | 27 | The formal statement imposes two parameter constraints the paper never states: "a function r with s <= r(s,lambda) <= s*poly(lambda)" and "beta with 1/beta(s,lambda) <= poly(lambda) for all s". Definition 14 (p27) types beta as ℕ×ℕ → [0,1] with no lower bound and places no relation between r_PoW(s,lambda) and s; Corollary 3 (p16) constrains only beta'(s,lambda,L) >= beta(s,lambda)/2 for sufficiently large polynomial s. On p5 the paper's own protocol has lim_{lambda→∞} beta = 0, so a polynomial bound on 1/beta is not something the paper asks of the sought function. These additions make the drafted conjecture strictly stronger than the paper's ask. Also: Def 14 types beta into [0,1], not the draft's (0,1]. |
| Attribution | pass | 22 | This is the harvested paper's own open problem, stated in its own concluding section and tied to its own Corollary 3 and Section 3. NSETH is invoked as an external hypothesis rather than as someone else's open problem, and the draft's openness_kind of paper-asks-question is correct. The draft does not present anyone else's question as this paper's. |
| Definitions | fail | 27 | Definition 14 (Moderate Hardness), p27, reads in full: A_1 "runs in time t(lambda)*beta(s,lambda)*r_PoW(s,lambda), makes at most d_1(lambda) queries to O^s_sigma and always outputs t candidate solutions". There is no clause forbidding oracle queries on z_1,...,z_t; the draft inserts one. The analogous exclusion exists only in Definition 5 (p14), as m_h not in Q union {m_j}_{j!=h}, for MV-SoWs. Separately, Def 14 is stated for a proof of work: win condition Verify(sigma,z_h,w_h)=1, oracle returning Solve(1^s,sigma,z), CRS from Setup(1^lambda,1^s). The draft's plain-function rewrite (w_h = f_{s,lambda}(z_h), oracle O_f, no CRS) tracks the paper's informal p16 remark, not the printed definition. Def 14 also samples only z_1,...,z_t via Gen while passing A_1 the tuple (z_h)_{h in [d_0]}; the draft silently makes all d_0 i.i.d. Finally, NSETH is nowhere defined in the paper (single occurrence, p23), so the draft's Definition (NSETH) is imported, not the paper's. |
| Fabrication | fail | 23 | NSETH appears exactly once in all 33 pages (p23) with no definition and no citation; there is no Carmosino/Gao/Impagliazzo/Mihajlin/Paturi/Schneider entry in the references (pp. 23-25 are alphabetical and go straight from CFG+23 to CJJ21). setting_latex nonetheless prints \cite{CGIMPS16} inline as if the paper carried the reference. Also fabricated: the oracle-exclusion clause and its stated rationale in definitions_latex; the two parameter constraints in formal_statement_latex. Minor over-extension: the notation block applies the Word RAM / O(log lambda)-bit-word convention to the moderately-hard-function setup, whereas the paper states it on p16 for the protocol execution model. Everything else the draft asserts checks out against pp. 2, 4, 5, 9, 11, 13, 16. |
| Self-containment | pass | - | A reader who has never opened the paper could tell what to prove: the notation block fixes lambda, s, n, Gen, f, r, beta, d_0, d_1, epsilon, gamma; the definitions block supplies both the hardness notion and NSETH; the formal statement quantifies the existentials explicitly. The caveat is that what such a reader would set out to prove is the draft's repaired notion, not the notion printed as Definition 14 on p27. |

### Unsupported by the paper

- The restriction that the adversary's oracle queries avoid {z_1,...,z_t} in the moderately-hard-function definition. Definition 14 (p27) has no such clause; it bounds only the query count by d_1(lambda).
- The parenthetical claim that this oracle restriction "is what makes the notion non-trivial when d_1 >= t". The paper offers no such remark about Def 14.
- The constraint s <= r(s,lambda) <= s*poly(lambda) on the honest evaluation cost. No such bound appears anywhere in the paper (checked Def 12, Def 14, Theorem 3, Corollary 3).
- The constraint 1/beta(s,lambda) <= poly(lambda) for all s. Not in the paper; and p5 states lim_{lambda->infinity} beta = 0 for the paper's own protocol, so the paper does not treat 1/beta as polynomially bounded.
- The definition of NSETH (k-TAUT, k-DNF tautology, nondeterministic time O(2^{(1-eps)N})). Correct as standard mathematics, but the paper never defines NSETH; it names it once on p23.
- The citation \cite{CGIMPS16} for NSETH inside setting_latex, presented as a reference of the paper. The paper's reference list (pp. 23-25) contains no Carmosino et al. entry, and the p23 mention of NSETH carries no citation at all.
- Presenting a CRS-free plain-function notion with win condition w_h = f_{s,lambda}(z_h) as the paper's "Definition 14". Def 14 (p27) is stated for a proof of work with win condition Verify(sigma, z_h, w_h) = 1 and an oracle returning Solve(1^s, sigma, z).
- The claim in notation_latex that running time in this setting is counted in the Word RAM model with O(log lambda)-bit words. The paper states this on p16 for its protocol execution and security model, not for Def 14 or Corollary 3. (Minor over-extension rather than a false assertion about the paper's content.)

### Corrections the checker asked for

- **definitions_latex (Moderately hard function)** — The draft's definition forbids the adversary's oracle queries from lying in {z_1,...,z_t}, and adds a parenthetical claiming this restriction "is what makes the notion non-trivial when d_1 >= t". Definition 14 on p27 contains no such restriction and the paper offers no such rationale; it bounds only the number of queries by d_1(lambda).
  - suggested: Either drop the clause "none of which lies in {z_1,...,z_t}" and its parenthetical, or keep it while stating explicitly that it is the draft's own repair of an apparent omission in Definition 14 (p27), noting that the analogous restriction does appear in Definition 5 (p14) as "m_h not in Q union {m_j}_{j != h}". As printed, Def 14 with d_1 >= t is trivially breakable, so the repair is substantive and must not be attributed to the paper.
- **formal_statement_latex** — Two side conditions are asserted that the paper never states: "a function r with s <= r(s,lambda) <= s*poly(lambda)" and "a function beta : NxN -> (0,1] with 1/beta(s,lambda) <= poly(lambda) for all s". Corollary 3 (p16) constrains only beta'(s,lambda,L) >= beta(s,lambda)/2 for sufficiently large polynomial s; Def 14 (p27) places no relation between r_PoW and s; and p5 reports lim_{lambda->infinity} beta = 0 for the paper's own protocol.
  - suggested: Delete both constraints, leaving "polynomials n, d_0, d_1, a function r, a function beta : NxN -> [0,1], a PPT challenge sampler Gen with output length n(lambda), and a family f = {f_{s,lambda}} with evaluation cost r(s,lambda)". If the drafter wants them for meaningfulness, mark them as the drafter's own additions rather than the paper's parameters.
- **definitions_latex (NSETH) and bibliography entry CGIMPS16, and the inline \cite{CGIMPS16} in setting_latex** — The paper mentions NSETH exactly once (p23), undefined and uncited; there is no Carmosino et al. entry in its references (pp. 23-25). The setting text nevertheless prints \cite{CGIMPS16} as though the paper supplied the citation, and the definitions block presents NSETH as if it were the paper's definition.
  - suggested: Drop the inline \cite{CGIMPS16} from setting_latex, or replace it with an explicit note such as "NSETH, which the paper invokes by name on p23 without defining or citing it". Label the NSETH definition as supplied by the drafter from the standard literature, and keep the bibliography entry's honest "unverified" marking.
- **definitions_latex / notation_latex (which object Def 14 governs)** — Definition 14 (p27) is stated for a proof of work PoW = (Setup, Gen, Solve, Verify): the win condition is Verify(sigma, z_h, w_h) = 1, the oracle O^s_sigma returns Solve(1^s, sigma, z), and there is a CRS sigma from Setup(1^lambda, 1^s). The draft presents a CRS-free, plain-function version with win condition w_h = f_{s,lambda}(z_h) and oracle O_f as if it were the paper's Definition 14.
  - suggested: State that the paper's Def 14 is for a proof of work, and that the function-only reading follows the paper's informal remark on p16 ("given any function f that is moderately-hard (Def. 14) ... but not necessarily efficiently verifiable"), which drops Verify and the CRS. Also flag that Def 14 samples only z_1,...,z_t via Gen while handing A_1 the tuple (z_h)_{h in [d_0]}, an apparent typo the draft repairs by making all d_0 challenges i.i.d.
- **notation_latex (beta range and running-time model)** — The draft types beta into (0,1]; Def 14 (p27) types it into [0,1]. The draft also asserts the Word RAM model with O(log lambda)-bit words as part of the moderately-hard-function setup, whereas the paper states this on p16 for its protocol execution model, not for Def 14.
  - suggested: Change the range to [0,1], and attribute the Word RAM convention to Section 4.1 (p16) as the paper's ambient computational model rather than as part of Def 14.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `CGIMPS16` — Marco L. Carmosino, Jiawei Gao, Russell Impagliazzo, Ivan Mihajlin, Ramamohan Paturi, and Stefan Schneider, *Nondeterministic extensions of the strong exponential time hypothesis and consequences for non-reducibility*, ITCS 2016 (recalled from memory; not cited in the source paper) 2016

## Build

- pdflatex: ok
- chktex: 6 warnings
- lacheck: 1 warnings

## What to check hardest

Three things a reviewer should check hardest. (1) The paper writes ``assuming, say, NSETH'', so NSETH is its example rather than its commitment; hard-coding NSETH narrows the question, and a solver should feel free to substitute another standard fine-grained hypothesis. (2) The NSETH statement above is written from memory — it is not stated anywhere in the paper — and I have not verified the current status of NSETH in the literature (barriers, conditional refutations); the accompanying citation is marked unverified for the same reason. (3) The paper's Definition 14, which I have adapted here, does not as printed forbid the adversary from querying the solving oracle on the very challenges it must solve, which would make the property trivially false whenever $d_1 \ge t$; I have added that restriction, and a reviewer should confirm this matches the intent (the reduction in the proof of Theorem 3 only ever queries the oracle on challenges derived from oracle-queried messages). Two further choices are mine: the requirement $1/\beta \le \mathrm{poly}(\lambda)$ (without some such condition the statement is vacuous, but the paper's own instantiations have $\beta \to 0$), and stating only the upper bound rather than also demanding that the per-instance bound be achievable, which is what ``tight'' would additionally require.

