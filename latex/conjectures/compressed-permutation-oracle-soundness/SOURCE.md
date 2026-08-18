# Provenance: Soundness of the Compressed Permutation Oracle

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Towards compressed permutation oracles**
- Authors: Dominique Unruh
- Venue/archive: IACR Cryptology ePrint Archive (preprint, University of Tartu) 2023
- Identifier: 2023/770
- Bibliographic detail: inferred
- File: `2023-770.pdf` (22 pages)
- sha256: `e32e1eb4a186bb3743828e494076f6cc1a35fc913dc4eedceab9b9b57ff3fc4c`
- Read on 2026-08-18T15:11:16Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Completely open as stated. The paper's Theorem 1 proves only a conditional converse: if some permutation-construction is indistinguishable from CPO then CPO is indistinguishable from a random permutation, so nothing about the conjecture itself is settled anywhere in the paper. Corollary 1 gives a computational variant of that same conditional statement.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 12 | 12 | exact (100%) | Define an oracle CPO (for “compressed permutation oracle”) that keeps a superposition of partial functions as its internal state, that responds to forward and b... |
| openness | 12 | 12 | exact (100%) | It turns out that defining such a CPO is not too hard. What is hard (and what we will only make a step towards in this paper) is to prove that the CPO is indeed... |
| openness | 1 | 1 | exact (100%) | A long-standing open question is whether a similar technique can also be used to reason about random (efficiently invertible) permutations. |
| openness | 3 | 3 | exact (100%) | In this paper, we are specifically interested in the second use case. The problem with that use case is that, even if we show (a), we still do not know whether ... |
| definition | 12 | 12 | exact (100%) | To define CPO, we need to define its behavior on forward and backwards queries. Forward queries are easy: The internal state is, like in the CFO case, a superpo... |
| progress | 14 | 14 | exact (100%) | In particular, the existence of such a construction shows Conjecture 2. |
| progress | 8 | 8 | exact (100%) | But if this does not hold, then we do not have a compressed oracle because we have no upper bound on the size of the oracle state. |

## Adversarial check

**Verdict: faithful** (confidence: high)

Conjecture 2 is on p.13 with exactly the two experiments and the exact negligibility-in-log|D| the draft formalizes, and it stays open: the abstract calls soundness a conjecture, Theorem 1 (p.14) and Corollary 1 (pp.18-19) are conditional on a construction being indistinguishable from CPO, and pp.19-22 are only references and indices, so nothing later discharges it. The place a draft like this usually breaks — the unconstrained Flip — survives scrutiny: Definition 1 and footnote 20 (p.12) require only ‖Flip‖ ≤ 1 with Flip|h⟩=|h^{-1}⟩ on injective h and explicitly intend the results to hold for any such choice, and the p.16 argument shows the non-injective branch shifts the advantage only negligibly, so the draft's ∀Flip is faithful rather than a strengthening. The only two things worth recording are non-defects: the quote tagged 'statement' is the informal p.12 desideratum (which also demands the ≤1-growth property) rather than Conjecture 2's text, and the sub-normalized output-probability convention is draft-supplied but matches footnote a on p.18.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 13 | Conjecture 2, eq. (7), is stated verbatim on p.13 directly after Definition 1 (Compressed permutation oracle): \|Pr[A^CPO ⇒ 1] − Pr[A^{π,π^{-1}} ⇒ 1 : π ←$ (D ↪ D)]\| is negligible, negligible in log\|D\|. The draft's formal_statement_latex is a formalization of exactly this. |
| Openness | pass | 1 | Abstract p.1: 'While the soundness of this technique (i.e., the indistinguishability from a random permutation) remains a conjecture...'. Reading past the passage: Theorem 1 (p.14) and Corollary 1 (pp.18-19) are both conditional on assumptions (9)/(20) about an existing permutation-construction; the Lemma 1 proof (pp.15-18) proves only the symmetry step. Pages 19-22 contain nothing but references, symbol index and keyword index — there is no appendix, footnote or results table anywhere that discharges Conjecture 2. |
| Strength | pass | 13 | Clause-by-clause the draft states the same thing as (7): same two experiments, same oracle pair (CFO_s, Flip·CFO_s·Flip) from Definition 1, same uniform draw from the permutations of D, same negligibility in log\|D\|. It is neither strengthened (the ≤1-growth requirement from the informal desideratum on p.12 is correctly NOT added — that is a property of the defined CPO, not of Conjecture 2) nor weakened (no efficiency restriction on A is smuggled in; polynomial-query is the paper's wording, and the poly-time version is Corollary 1). |
| Quantifiers and parameters | pass | 13 | Checked symbol by symbol. Query bound: 'polynomial-query algorithm' → query count ≤ p(log\|D\|), with security parameter log\|D\| as the paper's parenthetical '(Negligible in log\|D\|.)' dictates. Domain: D fixed once and for all with commutative ⊕ satisfying x⊕x=0 (p.5); since such a group forces \|D\|=2^m, all admissible (D,⊕) of a given size are isomorphic, so the draft's ∀D and single-μ-per-polynomial rendering is equivalent to the paper's per-adversary phrasing (adversaries here are non-uniform families, so sup-over-A is attained). Flip: ‖Flip‖ ≤ 1 and Flip\|h⟩=\|h^{-1}⟩ on injective h only, unconstrained elsewhere (p.12), and the ∀Flip quantification is the paper's own stance per footnote 20, p.12 ('our results hold independent of the design choices for that case'); it is also harmless, since p.16 shows the injective invariant is preserved up to O(i/N). U_π\|x⟩\|y⟩=\|x⟩\|y⊕π(x)⟩ matches U_f on p.5. Nothing is allowed to depend on anything the paper forbids. |
| Attribution | pass | 13 | This is the harvested paper's own conjecture, labelled 'Conjecture 2' and introduced by 'We conjecture:' (p.13). The draft does not present it as someone else's, and does not confuse it with Conjecture 1 (double-sided zero-search, p.12), which is also the paper's own and which the draft correctly leaves out of the formal statement. Cited prior work ([28] random-permutation/random-function indistinguishability, [27] qPRPs, [24] the withdrawn Sponge proof) is attributed to those works, not to this paper. |
| Definitions | pass | 10 | Every notion matches: partial functions, dom, im, ∅ (p.4); D ↪ D = total injections, i.e. permutations for D→D (pp.4, 14); Decomp_1 \|⊥⟩=\|*⟩, \|y⟩↦\|y⟩+⟨*\|y⟩(\|⊥⟩−\|*⟩) is eq. (2) p.8 (and eq. (3) p.9); Decomp = ⊗_x Decomp_1 is eq. (1) p.7; StO_s is the displayed sanitized standard oracle on p.10 (0 when h(x)=⊥); CFO_s = Decomp†·StO_s·Decomp is eq. (6) p.10; CFO_s not unitary, p.10. N=\|R\|=\|D\| in the permutation case (p.5, p.12). No definition is swapped for a standard one. One draft-supplied item: Pr[A^{O_1,O_2} ⇒ 1] := ‖Π_1 ψ_final‖² for sub-normalized states is nowhere defined in the paper, but it agrees with the abort-path reading given in footnote a on p.18. |
| Fabrication | pass | 4 | Every assertion in setting/status/progress was located: compressed-oracle record grows by ≤1 per query, size ≤q after q queries (p.7); invariant-based proofs with 'no zero-preimage' and 'h injective' invariants (pp.10-11); [12] generalizes to abelian-group Fourier transforms and parallel queries, [15] to non-uniform but independently sampled outputs (pp.3-4), and independence is exactly what fails for permutations (p.8); non-invertible permutations reducible to random functions via [28] (pp.4, 12); no hardness results at all for invertible random permutations, not even query complexity, hence nothing on SHA3 [22] (p.2); the withdrawn flawed collision-resistance proof is [24] Unruh, ePrint 2021/062 (footnote 5, p.4 + p.21); efficient simulation via strong qPRPs from quantum one-way functions [27] but no proof technique (p.4); Theorem 1 and its footnote-23 domain caveat (p.14); Corollary 1's extra hypotheses — C efficiently implementable, strong qPRP on D exists, poly-time adversaries (pp.18-19); the failed direct approach with domain-ordering dependence, no explicit basis-state description, and no ≤ℓ+1 size bound (footnote 14, pp.8-9). Bibliography: all seven entries match refs [12], [15], [22], [24], [27], [28], [30] as printed on pp.20-21. No fabricated prior result. |
| Self-containment | pass | - | The notation and definitions blocks fix D, ⊕, ⇀, injectivity of partial functions, h^{-1}, the registers X/Y/H_x, \|*⟩, Decomp_1, Decomp, StO_s, CFO_s, Flip, CPO with H private and initialized to \|∅⟩, U_π, oracle algorithm, query count, output probability for sub-normalized states, and negligibility. Decomp_1 is specified on a full basis, so it is uniquely determined. A reader who has never seen the paper knows precisely what would have to be proved. |
| Quote provenance and accuracy | pass | 12 | All seven quotes are verbatim and on the pages claimed, including the paper's own typo 'those partial function' (p.12) and the footnote-14 sentence on p.8. One curation note, not a misstatement: the quote tagged role 'statement' is the informal desideratum block on p.12, which additionally demands that queries grow the record by only 1 — so it does not state what formal_statement_latex states; Conjecture 2's actual text (7), p.13, is never quoted, only referenced in the status and progress notes. |

## Build

- pdflatex: ok
- chktex: 3 warnings
- lacheck: 0 warnings

## What to check hardest

(1) Resolution status. This is a 2023 eprint, and 2024--2025 saw substantial work on recording techniques for random unitaries and random permutations (path-recording style frameworks). I am not confident whether any of it verifies or refutes this exact CPO, so a reviewer should check the follow-up literature and this eprint's later versions before publishing. (2) Quantifier over $\mathsf{Flip}$. The paper's Conjecture 2 is stated for ``the'' CPO after Definition 1 leaves $\mathsf{Flip}$ underspecified on non-injective records; footnote 20 says the paper makes sure its results hold independent of that design choice, which is why I quantified universally over admissible $\mathsf{Flip}$. A reviewer may prefer to note explicitly that the existential reading (some admissible $\mathsf{Flip}$ works) is formally weaker. (3) Sub-normalization. Because $\mathsf{CFO_s}$ is not unitary, $\Pr[A^{\mathsf{CPO}} \Rightarrow 1]$ must be read as a sub-normalized probability; I have made that explicit in the notation, but it is not spelled out in the paper's own equation (7). (4) The paper writes the permutation set as $D \hookrightarrow D$ (total injections), which coincides with $\mathrm{Perm}(D)$ for finite $D$; I used the latter.

