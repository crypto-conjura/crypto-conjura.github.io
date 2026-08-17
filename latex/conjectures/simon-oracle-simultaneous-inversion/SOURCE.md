# Provenance: Simultaneous Inversion of a One-Way Function and a Random Permutation With a Collision Finder

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Black-Box Uselessness: Composing Separations in Cryptography**
- Authors: Geoffroy Couteau, Pooya Farshim, Mohammad Mahmoody
- Venue/archive: IACR Cryptology ePrint Archive 2021
- Identifier: 2021/016
- Bibliographic detail: inferred
- File: `2021-016.pdf` (37 pages)
- sha256: `1e26d5d117922336451b0d29c368ba48cb6a9e9b0e78b7683b4c75230e36576f`
- Read on 2026-08-17T19:31:08Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Open. The paper states that the corresponding statement without the collision finder is known when the hard function is itself a random oracle, and that it is unknown when the hard function is an arbitrary one-way function; the version with the collision finder is a fortiori unknown. What the paper does prove is the two consequences: this conjecture implies both the distributional and the class-reduction relaxations of its main helpfulness conjecture.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 31 | 31 | exact (100%) | In our context, though, we need an even stronger version, which we still deem plausible, where the random permutation comes with a collision finder Coll: |
| statement | 30 | 30 | exact (100%) | Due to the random nature of RP, it seems plausible that a stronger statement holds, which states that the hardness of inverting simultaneously some one-way func... |
| openness | 7 | 8 ⚠ | exact (100%) | We did not manage to prove this conjecture, and leave it as an interesting open problem which might be of independent interest. |
| progress | 31 | 31 | exact (100%) | The above conjecture is known in the case where F is itself a random oracle, but not when it is an arbitrary one-way function. We believe that Conjecture 6.6 is... |
| progress | 31 | 31 | exact (100%) | Theorem 6.8. If Conjecture 6.7 holds, then Conjecture 6.5 holds. |
| definition | 7 | 7 | exact (100%) | Here π implements a random permutation, and Collπ is an oracle that takes as input a circuit with π-gates and returns a random collision for it (by first comput... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 6.7 is genuinely the paper's own, is stated on p.31 essentially as the draft renders it, and stays open — no appendix exists, and Theorems 6.8 and 6.12 are both conditional sketches. The one substantive error is in the informal: it transfers the paper's \"known when F is itself a random oracle\" from Conjecture 6.6, the version without the collision finder, onto the collision-finder version, which the paper never claims is known; the draft's own status_note states this correctly, so the fix is exact. Two unresolved points I could not settle from the paper: it writes the first challenge as the undefined P(x1) where the draft substitutes F_λ(x1), and its inline poly(λ) does not fix whether the polynomial precedes or follows the measure-one quantifier as the draft's ∃q ordering assumes.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 31 | The statement is in the paper verbatim as "Conjecture 6.7 (Amplification, strong version)", with the attacker A^{F,RP,Coll^RP} given both challenges and the bound ε(λ)·poly(λ)/2^λ. |
| Openness | pass | 31 | Never proved anywhere. Theorem 6.8 (p.31) and Theorem 6.12 (p.32) are both conditional implications from it, both given as proof sketches; §1.5 says "We did not manage to prove this conjecture, and leave it as an interesting open problem" (p.8), with footnote 9 anchoring "this conjecture" to the simultaneous-inversion problem. The paper has no appendix — references begin p.33 — so there is no later section that resolves it. |
| Strength | pass | 31 | Clause by clause the draft matches Conjecture 6.7 and not the weaker Conjecture 6.6: the collision finder is present, F is an arbitrary ε-secure one-way function oracle, success requires exact recovery of both x1 and x2, and the bound is the product form ε(λ)·poly/2^λ. One symbol differs: the paper writes the first challenge as P(x1) (P being its own symbol for a "generic implementation", undefined in that display); the draft silently reads it as F_λ(x1), which p.8 confirms is the intended object but which the draft does not flag as a repair. |
| Quantifiers and parameters | unclear | 31 | F is fixed before RP and Coll are sampled in both, and the draft's added independence note is supported by p.8 ("π is fully independent of F"). But the draft hoists "there exists a polynomial q" outside "with probability 1 over the choice of RP and Coll", asserting one polynomial uniform over the measure-one set; the paper's inline poly(λ) after "for a measure one of random permutation RP and collision-finders Coll^RP" reads more naturally the other way. The paper does not disambiguate, so I cannot settle which is meant. The draft also adds "for all sufficiently large λ", which the paper leaves implicit. |
| Attribution | pass | 31 | Conjecture 6.7 is the harvested paper's own numbered conjecture, not one it cites to someone else. Simon [Sim98], Impagliazzo–Rudich [IR89], Holmgren–Lombardi [HL18], Shaltiel [Sha20] and Bauer–Farshim–Mazaheri [BFM18] are correctly presented as background, and all five bibliography entries match the printed source bibliography on pp.33-37. |
| Definitions | pass | 30 | The collision finder matches: "a collision-finder Coll that samples a random collision for any oracle circuit with RP-gates and (recursively) Coll-gates" (p.30), elaborated on p.7 as "first computing the circuit on a random point and then picking a random preimage". The draft's ε-secure one-way definition uses the preimage-finding condition F(B(F(x)))=F(x), which the paper does not spell out (p.31 says only "cannot invert F(x) ... with probability better than ε(λ)"); the draft's own conjecture then demands exact recovery. That is a formalization the paper does not supply, but it errs conservatively and does not redefine anything the paper defines. |
| Fabrication | fail | 31 | The informal states that the conjecture — the one with the collision finder — "is known when the hard function is itself a random oracle". The paper attaches that sentence to Conjecture 6.6, the weak version WITHOUT the collision finder: it appears immediately after 6.6 and immediately before "In our context, though, we need an even stronger version ... where the random permutation comes with a collision finder Coll". The paper never claims the strong version is known in any case. Two lesser unsupported glosses: the setting describes HL18 as needing hardness "to within roughly the product of their individual hardnesses", where p.8 states the requirement as an absolute negl(n)/2^n bound for exponentially secure one-way product functions; and it calls the BFM18 route to the same conclusion without noting that the paper conditions it on a communication-complexity conjecture (pp.8, 32). |
| Self-containment | pass | - | A reader who has never seen the paper could work from the statement alone: both definitions are given inline, the measure on collision finders is made explicit, and the target inequality and its probability space are fully specified. |

### Unsupported by the paper

- The informal claims the collision-finder version of the conjecture is known when the hard function is a random oracle. The paper (p.31) says this only of Conjecture 6.6, the version without the collision finder, and makes no such claim about Conjecture 6.7.
- The setting characterizes the Holmgren-Lombardi hardness requirement as "roughly the product of their individual hardnesses"; the paper (p.8) states it as an absolute negl(n)/2^n bound for exponentially secure one-way product functions.
- The setting calls the BFM18 approach a route to "the same helpfulness conclusion" without the communication-complexity conjecture the paper attaches to it (pp.8, 32).

### Corrections the checker asked for

- **informal** — Says the conjecture "is known when the hard function is itself a random oracle", but the paper (p.31) says that of Conjecture 6.6, the weak version without the collision finder. The draft's own status_note states this correctly, so the informal contradicts it.
  - suggested: Replace "This is known when the hard function is itself a random oracle; the open case is an arbitrary hard function" with: "The paper's weaker version of this statement, in which the collision finder is dropped, is known when the hard function is itself a random oracle but not when it is an arbitrary one-way function; the version with the collision finder is stated here as a conjecture and is not claimed to be known in any case."
- **quotes[2].page** — The quote "We did not manage to prove this conjecture, and leave it as an interesting open problem which might be of independent interest" is cited to page 7. It is on PDF page 8 (printed page 6), at the end of §1.5's first approach, carrying footnote 9. Page 7 holds the Simon-oracle description quoted elsewhere in the draft.
  - suggested: page: 8
- **setting_latex** — Describes the Holmgren-Lombardi requirement as simultaneous hardness "to within roughly the product of their individual hardnesses". Page 8 states it as: CRHFs from exponentially secure one-way product functions, where an adversary inverts (F1(x1),...,Fk(xk)) on random inputs with probability at most negl(n)/2^n. Footnote 13 (p.31) adds that HL18 as stated needs F1=F2 injective, with an extra-loss reduction from an arbitrary pair.
  - suggested: "Holmgren and Lombardi \cite{HL18} show how to build collision-resistant hash functions in a black-box way from exponentially secure one-way product functions, i.e. tuples of functions no efficient adversary can invert simultaneously on random inputs with probability better than $\mathrm{negl}(n)/2^{n}$; the paper notes in a footnote that their result as stated requires the two components to be equal and injective, with an extra-loss black-box reduction from an arbitrary pair."
- **setting_latex** — Presents the BFM18 route as "A second, independent route to the same helpfulness conclusion" without recording that the paper conditions it on a communication-complexity conjecture, and that Section 6.4's conclusion is that a backdoored random oracle is itself black-box helpful for CRHFs, rather than a second proof that one-way functions are.
  - suggested: Add: "conditional on a communication-complexity conjecture related to set intersection, and yielding in Section 6.4 the conclusion that a single backdoored random oracle, though black-box separated from collision-resistant hashing, is black-box helpful for it."

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 0 warnings

## What to check hardest

The printed conjecture writes the first challenge as $\mathsf{P}(x_1)$ rather than $\mathsf{F}(x_1)$ in both the weak and the strong version. I have written $\mathsf{F}(x_1)$, which is what the surrounding prose and the proof of Theorem 6.8 require, but a reviewer should confirm this reading. Second, the printed display carries no quantifier over $\lambda$ and leaves $\mathrm{poly}(\lambda)$ unquantified; I have read this as ``there is a polynomial $q$, depending on the attacker, such that the bound holds for all sufficiently large $\lambda$'', and a reading with ``for all $\lambda$'' would be formally stronger. Third, the conjecture as printed demands exact recovery of both preimages, $(x_1,x_2)=A(\dots)$, whereas the statement derived from it in the proof of Theorem 6.8 is the weaker any-preimage form; I have kept the paper's exact-recovery form. Fourth, my definition of the collision finder spells out the recursion by nesting depth and the induced measure on deterministic finders, details the paper leaves to \cite{Sim98}; the intended object is Simon's, and any discrepancy should be resolved in Simon's favour. Finally, I have not exhaustively checked the post-2021 literature for a proof or a counterexample.

