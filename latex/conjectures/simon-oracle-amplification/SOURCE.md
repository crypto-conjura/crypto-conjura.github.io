# Provenance: Simultaneous Inversion of a One-Way Function and a Random Permutation Given a Collision Finder

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Black-Box Uselessness: Composing Separations in Cryptography**
- Authors: Geoffroy Couteau, Pooya Farshim, Mohammad Mahmoody
- Venue/archive: Cryptology ePrint Archive 2021
- Identifier: 2021/016
- Bibliographic detail: inferred
- File: `2021-016.pdf` (37 pages)
- sha256: `1e26d5d117922336451b0d29c368ba48cb6a9e9b0e78b7683b4c75230e36576f`
- Read on 2026-08-17T19:17:35Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Open in the stated generality. The corresponding statement is known when the one-way function is itself a random oracle, and the pure random-permutation inversion bound without a second function is classical; the case of an arbitrary one-way function, with or without the collision finder present, is not established.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 30 | 30 | exact (100%) | Due to the random nature of RP, it seems plausible that a stronger statement holds, which states that the hardness of inverting simultaneously some one-way func... |
| statement | 31 | 31 | exact (100%) | In our context, though, we need an even stronger version, which we still deem plausible, where the random permutation comes with a collision finder Coll: |
| openness | 8 | 8 | exact (100%) | We did not manage to prove this conjecture, and leave it as an interesting open problem which might be of independent interest. |
| progress | 31 | 31 | exact (100%) | The above conjecture is known in the case where F is itself a random oracle, but not when it is an arbitrary one-way function. We believe that Conjecture 6.6 is... |
| definition | 30 | 30 | exact (100%) | By Simon’s result, this still holds even in the presence of a collision-finder Coll that samples a random collision for any oracle circuit with RP-gates and (re... |
| progress | 31 | 31 | exact (100%) | We now sketch why proving the above conjecture would establish that OWFs are distributionally black-box helpful for collision-resistant hash functions: |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is real, is the paper's own (Conjecture 6.7, PDF p. 31), and is explicitly left unproven on PDF p. 8 with nothing in the rest of the paper resolving it; the formal statement, quantifier order, bound and definitions all match the paper symbol for symbol, and the draft correctly drafts the strong version rather than the weak Conjecture 6.6. The most important defect is that the draft transplants the paper's remark "known in the case where F is itself a random oracle" -- made about Conjecture 6.6, the version WITHOUT the collision finder -- onto the strong version it is stating, so the informal and status_note report partial progress the paper does not claim. A second defect is the BFM18 paragraph, which presents a conclusion about backdoored random oracles as if it were a second route to the same OWF-helpfulness statement and drops the communication-complexity conjecture it depends on.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 31 | Conjecture 6.7 (Amplification, strong version) appears verbatim on PDF p. 31 (printed p. 29), immediately after Conjecture 6.6 and the sentence "In our context, though, we need an even stronger version ... where the random permutation comes with a collision finder Coll". The draft's page citations are in PDF numbering and all check out: p. 8, p. 30, p. 31. |
| Openness | pass | 8 | PDF p. 8 (printed p. 6): "To get a positive helpfulness result we need to show that for any one-way function F the pair of functions (F, (pi, Coll^pi)) is product one-way ... We did not manage to prove this conjecture, and leave it as an interesting open problem which might be of independent interest." "This conjecture" is precisely Conjecture 6.7. It stays open: the only later uses are Theorem 6.8 and Theorem 6.12, both of the form "If Conjecture 6.7 holds, then ...", and the paper ends at the references (PDF pp. 33-37) with no appendix and no further mention of 6.6 or 6.7. |
| Strength | pass | 31 | Clause by clause identical to the paper's Conjecture 6.7: same hypothesis (F an oracle implementing an epsilon-secure OWF), same oracles for A (F, RP, Coll^RP), same success event (exact equality (x1,x2) = A(...), not "some preimage"), same bound epsilon(lambda)*poly(lambda)/2^lambda, same probability space ((x1,x2) uniform in ({0,1}^lambda)^2 and A's coins). The draft correctly drafts the strong version (with Coll), not the weak Conjecture 6.6. Note: the paper's display literally reads A^{F,RP,Coll}(P(x1), RP(x2)) in both 6.6 and 6.7 -- P is an evident typo for F, which the draft silently repairs; the repair is correct but undeclared. |
| Quantifiers and parameters | pass | 31 | Paper: "Then for any oracle-aided PPT machine A and for a measure one of random permutation RP and collision-finders Coll^RP". The draft preserves the order -- for every A, then a measure-one set (allowed to depend on A) of (RP, Coll), then the bound -- and makes the paper's unquantified poly explicit as "there exists a polynomial poly depending on A", which is the only sensible reading. epsilon is left arbitrary (not required negligible) in both, matching the paper, which imposes no condition on epsilon. Adding "for all sufficiently large lambda" neither strengthens nor weakens given the existential poly. |
| Attribution | pass | 31 | This is the harvested paper's own numbered conjecture (Conjecture 6.7), not a problem it credits to someone else. The surrounding prior results are correctly credited elsewhere: the poly(lambda)/2^lambda inversion bound to [IR89] and its survival under a collision finder to [Sim98] (PDF p. 30), and the OWPF-to-CRHF construction to [HL18] (PDF pp. 8, 31). The abstract independently confirms authorship: "a natural conjecture regarding random permutations equipped with a collision finder oracle, as defined by Simon". |
| Definitions | pass | 30 | The paper never gives a numbered definition of Coll; it describes it twice -- PDF p. 8: "an oracle that takes as input a circuit with pi-gates and returns a random collision for it (by first computing the circuit on a random point and then picking a random preimage)", and PDF p. 30: "a collision-finder Coll that samples a random collision for any oracle circuit with RP-gates and (recursively) Coll-gates". The draft's definition is the union of these two and matches. The added clause "its answers are fixed in advance by independent uniform choices, so that a measure one of collision-finders refers to the product measure" is a gloss not stated in the paper, but it is the reading needed to make the paper's own phrase "a measure one of ... collision-finders Coll^RP" meaningful. The epsilon-secure OWF definition is the paper's, quoted almost verbatim from Conjecture 6.6. |
| Fabrication | fail | 31 | Two unsupported assertions. (1) The draft's informal and status_note say the conjecture "is known when the hard function is itself a random oracle". The paper's sentence "The above conjecture is known in the case where F is itself a random oracle, but not when it is an arbitrary one-way function" (PDF p. 31) sits between Conjecture 6.6 and Conjecture 6.7 and refers to 6.6, the version WITHOUT the collision finder. The paper says nothing about the strong version being known in any case. (2) The setting_latex calls the BFM18 route "a second, independent route to the same helpfulness statement"; PDF p. 33 (section 6.4) actually concludes only that a backdoored random oracle is "an idealized primitive which does not black-box imply CRHFs, yet is BB helpful for CRHFs" -- a different statement -- and both PDF p. 8 and p. 33 make it conditional on "a communication complexity conjecture related to the set-intersection problem", a caveat the draft drops. Additionally, progress_note's description of footnote 9 is wrong in detail: the footnote (PDF p. 8) replaces the random permutation together with its collision finder by a random oracle, not "the collision finder by a random oracle". |
| Self-containment | pass | - | The formal statement, notation and definitions together let a reader who has not seen the paper know what to prove: the collision finder, the epsilon-security hypothesis, the probability space, and the meaning of "measure one" are all supplied. No evidence needed from the paper for this check; it is a property of the draft. |

### Unsupported by the paper

- informal and status_note claim the strong version (with the collision finder) is known when the one-way function is a random oracle. The paper's remark "The above conjecture is known in the case where F is itself a random oracle" (PDF p. 31) refers to Conjecture 6.6, the weak version without the collision finder.
- setting_latex calls the BFM18 backdoored-random-oracle material "a second, independent route to the same helpfulness statement". Section 6.4 (PDF p. 33) concludes only that an idealized primitive (a BRO) is black-box helpful for CRHFs, not that one-way functions are.
- setting_latex and progress_note omit that the BFM18 route is conditional on a communication-complexity conjecture about set intersection, stated as a condition on both PDF p. 8 and PDF p. 33.
- progress_note states footnote 9 replaces "the collision finder by a random oracle". The footnote (PDF p. 8) replaces the random permutation together with its collision finder by a random oracle.

### Corrections the checker asked for

- **informal** — Asserts that the conjecture as stated (with the collision finder) "is known when the hard function is itself a random oracle". The paper makes that remark about Conjecture 6.6, the weak version without the collision finder (PDF p. 31); it says nothing about the strong version being known in any case.
  - suggested: Replace with: "The paper's weaker version of this statement -- the same product bound but without the collision finder present (Conjecture 6.6) -- is known when the hard function is itself a random oracle, but not when it is an arbitrary one-way function. The strong version stated here, with the collision finder, is not claimed to be known in any case."
- **status_note** — "The corresponding statement is known when the one-way function is itself a random oracle" reads, in context, as a claim about the conjecture being drafted. The paper's known-case remark covers only Conjecture 6.6 (no collision finder).
  - suggested: "Open in the stated generality. The paper's weak version without the collision finder (Conjecture 6.6) is known when the one-way function is itself a random oracle, but not for an arbitrary one-way function; the strong version with the collision finder is not claimed to be known in any case. The pure random-permutation inversion bound without a second function is classical [IR89], and survives the collision finder [Sim98]."
- **setting_latex** — Describes the BFM18 material as "a second, independent route to the same helpfulness statement", and omits that it is conditional. Section 6.4 (PDF p. 33) concludes that a backdoored random oracle -- an idealized primitive, not one-way functions -- is black-box helpful for CRHFs, and both PDF p. 8 and p. 33 condition this on a communication-complexity conjecture about set intersection.
  - suggested: "The paper also presents a second, unrelated approach via backdoored random oracles [BFM18], whose leakage oracle is powerful enough to implement Simon's collision finder. Under a communication-complexity conjecture related to set intersection, two independent BROs yield a CRHF, so a single BRO -- an idealized primitive black-box separated from CRHFs -- is conjecturally black-box helpful for them. This yields a helpful idealized primitive, not the helpfulness of one-way functions, and does not bear on the conjecture stated here."
- **progress_note** — Misdescribes footnote 9 (PDF p. 8), which reads: "given an epsilon-secure one-way permutation and a random oracle, can an attacker invert both simultaneously with probability better than negl(n)/2^n?" The footnote replaces the random permutation together with its collision finder by a random oracle; it does not replace only the collision finder.
  - suggested: "A weaker warm-up is suggested in footnote 9: replace the arbitrary one-way function by an epsilon-secure one-way permutation and the random permutation with its collision finder by a random oracle, and ask whether an attacker can invert both simultaneously with probability better than negl(n)/2^n."
- **formal_statement_latex** — The paper's displayed inequality in both Conjecture 6.6 and Conjecture 6.7 literally reads A^{F,RP,Coll^{RP}}(P(x_1), RP(x_2)) -- P, not F. This is plainly a typo (F is the only function in scope and P is used elsewhere in the paper for the implementation machine of a black-box reduction), and the draft's F(x_1) is the right reading, but the repair is undeclared.
  - suggested: Keep F(x_1) in the statement, and add a note: "The paper writes P(x_1) here; this is a typo for F(x_1), as F is the only function in scope and P denotes the implementation machine of a black-box reduction elsewhere in the paper."

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

(1) The displayed inequality in the paper prints $A^{\mathsf F,\mathsf{RP}}(\mathsf P(x_1),\mathsf{RP}(x_2))$ and its collision-finder analogue; the symbol $\mathsf P$ appears nowhere else and is evidently a typo for $\mathsf F$, as confirmed by the proof sketch of Theorem 6.8, which instantiates $\mathsf F_1:=\mathsf F$ and $\mathsf F_2:=\mathsf{RP}$ and writes $\mathsf F_1(x_1)$. I have written $\mathsf F$. (2) The quantifier on $\mathrm{poly}(\lambda)$ is left implicit in the paper; I have read it as existentially quantified after the adversary, which is the standard reading, but a reviewer should confirm. (3) The paper does not say whether the $\varepsilon$-security of $\mathsf F$ is required to hold against adversaries with access only to $\mathsf F$, or also to $\mathsf{RP}$ and $\mathsf{Coll}^{\mathsf{RP}}$; I have written the former, which makes the conjecture stronger and matches the phrase "no oracle-aided PPT machine can invert $\mathsf F(x)$". Note that $\mathsf F$ must be fixed before $\mathsf{RP}$ is sampled for the measure-one quantifier to make sense. (4) The precise sampling convention for $\mathsf{Coll}^{\mathsf{RP}}$ that makes "measure one of collision-finders" well defined is Simon's; I have summarized it. (5) I am not aware of a proof or refutation since January 2021, but the one-way-product-function literature has been active and a reviewer should check it.

