# Blind referee report: split-decomp-kappa-1-r3

Package: r3 at origin/main, the Contract, cards S1 (CDGS) and S2 (CFHS). Self-contained:
r3 supersedes its two predecessors and depends on no other artifact. kappa-2 and its
revision were deliberately excluded, the dependency running the other way.
Referee: fresh context, project's own REFEREE-PROMPT.md, no session context.

## VERDICT
STATUS: CLEAN

Every step of Theorems A, B, C, C' and of Lemmas 0-5 and P checks out against the Contract
and the two cards. The only defects are routine class (C) presentational or bookkeeping
gaps, and the referee makes that call explicitly.

## The four things the package was built to test, all passed

**CDGS Claim 2, three structural uses.** The card records that the paper states Claim 2 for
a narrower setting and that the artifact relies on the *proof* establishing more. All three
uses are licensed: generalisation to a non-uniform input distribution of deficiency S_zeta
(card point 1), pairwise disjoint supports so that J is a function of f (point 2), and fixed
values being values the sampled f takes, which is what delivers consistency in the Contract's
sense (point 3). A fourth use, that the decomposition is of mu_zeta itself, is licensed by the
card's proof sketch by a shorter route the artifact does not name.

**CDGS Claim 4 avoidance.** The card warns Claim 4 needs deterministic leakage. Lemma P's
Step 1 bounds mu_zeta(f) using only Pr[z = zeta | H = f] <= 1, so it is valid for randomised
leakage, and the artifact never invokes Claim 4 or CDGS Lemma 1 anywhere.

**CDGS Claim 3, the T accounting.** T = q is the number of oracle coordinates the observer
queries, which is the card's T. The card's w.l.o.g. that the distinguisher avoids fixed
positions only lowers it.

**Challenge resolution, the quantifier point.** The class is pinned by a definition in the
artifact with the coin quantifier explicit, and an N = M = 2 example separates the per-coin
reading from the in-law reading. Theorem A, Corollary A', Theorem C' branch 1 and section 9
all use the per-coin reading consistently. This is the defect the second review round found in
r2, and it is repaired.

## Also verified

No class (A) drift: the artifact proves a strict sub-region of the Contract's conjecture and
says so twice. The Contract's quantifier order is preserved, the family being built from
(P, gamma) before q. Consistency with f is delivered, so this is the Contract's conjecture and
not the weakening its rem:uses describes. The union bound over an index set depending on sigma
and N is paid for exactly inside C_0. The identical-until-bad step in Theorem C transfers the
bad-event probability correctly. CFHS Lemma 3, Lemma 4.3 and Theorem 3 all used within their
card hypotheses, and the asymptotic CFHS Theorem 3 arm is correctly kept out of Theorem C',
the only place explicit constants are claimed.

## Routine (C) findings, reported without forcing the verdict

Lemma 0 asserts a single D' optimal for both quantities where the proof supplies one per
paired experiment; nothing downstream needs both at once. Lemma P Step 2's inference needs
S_zeta <= S-bar, which holds only off the bad set, and is recovered in Step 4. Lemma P Step 3
mentions averaging over the challenge but not over D's own coins; the bound is uniform over
coin strings and Lemma 0 is available. Section 0's item (C') drops the per-coin qualifier that
item (A) calls load-bearing; Theorem C' itself is unambiguous. Section 0's item (C) writes the
family as Y^{P,gamma} where Theorem C proves it for Y^{P,gamma/2}. Section 10's CDGS Claim 2
bullet attributes two conclusions to a card invariant written for the uniform variable; both
are licensed by a shorter route.

## Standing

One pass. The kappa-1 lineage received five, across three model families and five angles.
A clean verdict here is evidence, not a freeze.
