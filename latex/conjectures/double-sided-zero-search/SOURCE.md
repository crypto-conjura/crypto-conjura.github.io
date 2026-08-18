# Provenance: Hardness of Double-Sided Zero Search

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

`paper-conjectures`. Open unconditionally. The paper proves it only under its own Conjecture 2 (soundness of the compressed permutation oracle), and says so explicitly when presenting the argument; that conditional argument is the paper's usage example, not a proof.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 12 | 12 | exact (100%) | Let H be a uniformly random permutation on {0, 1}2n . The following problem is hard for any adversary making polynomially many superposition queries to H and H ... |
| openness | 12 | 12 | exact (100%) | Because of this, even simple questions relating to (superposition access to) random permutations are to the best of our knowledge not in the scope of existing t... |
| openness | 2 | 2 | exact (100%) | To the best of our knowledge, no hardness results are known about invertible random permutations, not even simple query complexity results such as the hardness ... |
| progress | 13 | 13 | exact (100%) | We now illustrate how the CPO can be used by showing Conjecture 1 (double-sided zero-search) using the CPO. Of course, the validity of this example rests on Con... |
| parameter | 12 | 12 | exact (100%) | What we are interested in are, therefore, invertible random permutations (forward and backward queries). |
| progress | 12 | 12 | exact (100%) | Namely, we know that a random permutation is indistinguishable from a random function, even in the quantum setting [28]. So when analyzing a situation where the... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 1 is genuinely the paper's own (p. 12), genuinely open — the only proof offered rests explicitly on the unproven Conjecture 2 (p. 13), and Theorem 1 and Corollary 1 leave that unchanged through p. 19 — and the formal statement, quantifiers, and definitions all check out symbol by symbol. The one real failure is the draft's classical-complexity claim: it relabels the paper's conditional quantum bound Theta(2^{n/2}) as the classical answer and asserts the paper sketches that classical bound, when the paper gives no classical count and the true classical figure is Theta(2^n). That error is confined to the narrative fields and is precisely repairable, so the conjecture survives with corrections rather than being unfaithful.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 12 | Conjecture 1 (Double-sided zero-search) is stated verbatim on p. 12: "Let H be a uniformly random permutation on {0,1}^{2n}. The following problem is hard for any adversary making polynomially many superposition queries to H and H^{-1}: Find x in {0,1}^n such that H(x‖0^n) = y‖0^n for some y." The draft's problem is this problem. |
| Openness | pass | 13 | It is posed as a conjecture (p. 12), and the only argument for it (p. 13, "Usage example") is explicitly conditional: "Of course, the validity of this example rests on Conjecture 2." I read every remaining page (14-22): Theorem 1 (p. 14) and Corollary 1 (pp. 18-19) establish Conjecture 2 only under the hypothesis that some construction is indistinguishable from the CPO, a hypothesis the paper never discharges. Nothing resolves Conjecture 1 unconditionally. |
| Strength | pass | 12 | Clause by clause: same permutation domain {0,1}^{2n}, same input shape x‖0^n with x in {0,1}^n, same output condition (exists y with image = y‖0^n), same two oracles H and H^{-1}, same polynomial query bound. Neither strengthened nor weakened; the draft does not generalize the zero suffix, the domain split, or the oracle access. |
| Quantifiers and parameters | pass | 12 | The paper's "hard for any adversary making polynomially many superposition queries" is a query bound with no runtime bound; the draft's "every oracle algorithm A with query count at most p(n)" matches and correctly omits efficiency. The for-all-p / exists-negligible-mu order is the standard reading of "hard" and is not contradicted. The paper measures negligibility in log\|D\| (Conjecture 2, p. 13); with \|D\| = 2^{2n} the draft's negligible-in-n is equivalent. The parameter table (n, p, H) is consistent with p. 12. |
| Attribution | pass | 12 | This is the harvested paper's own numbered Conjecture 1, authored by Unruh, not a problem attributed to another work. The supporting claims the draft borrows (random permutation ~ random function) are correctly attributed to [28] = Zhandry 2015, as the paper does on p. 12. |
| Definitions | pass | 5 | U_G\|u>\|v> = \|u>\|v XOR G(u)> matches the paper's U_f : \|x>\|y> -> \|x>\|y XOR f(x)> (p. 5). Perm(S) is a rename of the paper's D <-> D ("injective functions from D to D", symbol index p. 21) - renamed, not redefined. Superposition access, query count, and negligible all carry the paper's meanings. No silent substitution found. |
| Fabrication | fail | 13 | setting_latex: "Classically it is a lazy-sampling exercise, and the expected answer is Theta(2^{n/2}) queries. The paper sketches exactly that bound..." The Theta(2^{n/2}) on p. 13 is the QUANTUM bound from the CPO invariant argument, not a classical bound; the paper states no classical query complexity for this problem (its p. 12 classical discussion is generic lazy sampling of permutations, with no count). The correct classical figure is Theta(2^n). informal repeats this as "a straightforward birthday-type question" - there is no birthday structure here. informal also asserts "no attack is known either", which appears nowhere in the paper and is in tension with the paper's own Theta(2^{n/2}) (a Grover-type search matches it). |
| Self-containment | pass | - | The formal statement plus notation block fixes the permutation domain, both oracles, the query bound, the success event, and the output type; a reader who has never seen the paper knows exactly what must be proved. No evidence needed from the paper for this check. |

### Unsupported by the paper

- Classical query complexity of double-sided zero-search given as Theta(2^{n/2}) (setting_latex) / "about two to the n over two queries" (informal). The paper states no classical bound for this problem anywhere; the correct classical figure is Theta(2^n).
- "The paper sketches exactly that bound" applied to the alleged classical bound (setting_latex). The paper's Theta(2^{n/2}) on p. 13 is the conditional quantum bound, not a classical one.
- Characterizing the problem as "birthday-type" (informal). No birthday or collision structure is present in the problem or claimed by the paper.
- "no attack is known either" (informal). Absent from the paper, and in tension with the paper's own Theta(2^{n/2}) tightness claim on p. 13.

### Corrections the checker asked for

- **setting_latex** — Claims the classical query complexity of double-sided zero-search is Theta(2^{n/2}) and that the paper's CPO sketch establishes "exactly that bound". The paper gives no classical bound for this problem, and its Theta(2^{n/2}) (p. 13) is the conditional quantum bound.
  - suggested: Classically the problem is an easy lazy-sampling exercise and takes Theta(2^n) queries: there are about 2^n candidate inputs x‖0^n, and each forward (or backward) query hits the 2^n-element zero-suffix set with probability about 2^{-n}. The paper itself states no classical bound. What the paper sketches in the compressed-permutation-oracle framework is the quantum bound Theta(2^{n/2}) (p. 13), and only under Conjecture 2.
- **informal** — "Classically this is a straightforward birthday-type question and the answer is that you need about two to the n over two queries" - wrong count and wrong reason; there is no collision structure, and this sentence silently reuses the paper's quantum figure. It also contradicts the next sentence's claim that no quantum bound is provable.
  - suggested: Classically this is a plain search question - not a birthday question - and about two to the n queries are needed. Quantumly, no lower bound can currently be proved at all; the two-to-the-n-over-two figure appearing in the paper is the quantum bound its conditional CPO argument yields.
- **informal** — "The reason is not that the problem looks easy - no attack is known either" is not supported anywhere in the paper, and the paper's own Theta(2^{n/2}) claim indicates a matching quantum search attack.
  - suggested: Delete. The paper's position is only that no hardness results are known for invertible random permutations (p. 2); it makes no claim about the absence of attacks.

## Build

- pdflatex: ok
- chktex: 1 warnings
- lacheck: 1 warnings

## What to check hardest

(1) Resolution status. This is the paper's flagship example and an obvious target, and there has been significant activity since 2023 on recording techniques for random permutations and random unitaries; I am not confident it has not been settled, and a reviewer should check the follow-up literature before publishing. (2) Strength. The paper's Conjecture 1 says only that the problem is ``hard'' for polynomially many queries; the $\Theta(2^{n/2})$ figure appears only in the conditional usage example, so I deliberately kept it out of the formal statement and put it in the progress note. (3) The paper does not fix the query model for the inverse oracle beyond calling it a ``backward query''; I used the standard XOR unitary for $H^{-1}$, which is the natural reading and matches the paper's $A^{\pi,\pi^{-1}}$ notation elsewhere. (4) The paper's phrasing ``Find $x \in \{0,1\}^n$'' leaves implicit that the adversary must output $x$ rather than merely a witness pair; I made the output convention explicit.

