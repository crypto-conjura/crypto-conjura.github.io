# Triage rulings — round r2 (against split-decomp-kappa-1-r2)

1 UPHELD / 1 OVERRULED / 14 PEDANTIC / 0 NEEDS-SOURCE. Findings as collated in
split-decomp-kappa-1-r2-findings.md.

UPHELD: G1 only.
OVERRULED: G12 (the pass itself recorded no defect; the range comparison is
against the Contract's informal status note, not an internal claim).
PEDANTIC: G2-G11, G13-G16.

## G14, settled from the card and re-ranked down from a possible fatal

Pass A2 argued that Lemma P's Step 2 identification might be unlicensed, and that
under the alternative reading the residue's mass would be bounded only by
gamma * 2^sigma under mu_zeta, destroying Lemma P. It supported this by quoting
"For ease of notation, let S := S_z and X := X_z" as the card's notational
sentence. That sentence is NOT in the card. Triage settled the referent from what
the card does record -- observation 1's recursion invariant
Pr[Y=y] = Pr[X=y | X in supp(Y)], which at initialisation Y = X_z forces X = X_z,
since the uniform reading would make Y uniform on its support and contradict
Y = X_z for non-flat X_z. So the decomposition is of X_z itself, the residue's
mu_zeta-mass is at most gamma, each lambda_j X_j is the mu_zeta-restriction, and
nothing in Lemma P, Theorem C or Theorem C' changes. Only the Section 10
inventory entry recording this third consequence of the card's proof was missing;
r3 adds it.

## G1, upheld: the class was underdetermined

Section 4's definition of challenge resolution did not quantify coins, so for a
randomised observer it had no truth value; Section 0 glossed the class as
"query positions do not depend on the challenge value", which reads as a
statement about the law; and Lemma 0's proof -- added in r2 as the repair to
round-1 finding F5 -- asserted a per-coin-string reading that Section 4 did not
state. Under the in-law reading the inheritance step is false, witnessed at
N = M = 2, q = 1 by the observer that flips rho and queries (1,1) when
v XOR rho = 1 and (2,2) otherwise: challenge-independent in law, resolution 2 at
each coin fixing.

Ruling: the artifact must commit to the per-coin-string reading, which is exactly
what Proposition 6.2 at M' = 1 bounds. Required changes, all applied in r3:
 (a) Section 4's definition quantifies over every coin string;
 (b) Section 0's gloss says "for each fixed coin string";
 (c) Lemma 0's statement absorbs what its proof gives -- domination for either
     paired experiment, attainment for both kappa(q) and kappa^na(q), and
     resolution inheritance (this also closes G5);
 (d) Section 9's Barrier 1 records that an observer challenge-independent only in
     law has per-coin resolution M' > 1 and sits outside Theorem C' branch 1.

## Prior rulings confirmed, not reversed

G6/G16 (Lemma 4 presuming h surjective) and G7/G15 (the flat-decomposition lemma
at exponent 0) and G13 (the family undefined at off-support zeta) are round-1's
F10, F6 and F8, each ruled PEDANTIC then and each genuinely trivial on
re-examination: surjectivity is without loss, the exponent-0 instance is an
identity, and the off-support completion is forced. Because each has now been
raised by three independent passes across two rounds and each costs under a
sentence, they were listed as recommended-and-apply rather than optional, to end
the re-raising loop without promoting a non-defect. All three are applied in r3.

## Closing

No UPHELD finding threatens a numbered theorem's conclusion. G1 threatened the
scope of Theorem A and of Theorem C' branch 1, leaving the class kappa^na ranges
over undetermined between two genuinely different classes rather than falsifying
anything. Under the reading r3 commits to, every numbered conclusion stands, and
Theorem C''s headline claim stands.
