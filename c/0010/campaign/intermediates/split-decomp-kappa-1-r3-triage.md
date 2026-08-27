# Triage rulings — split-decomp-kappa-1-r3 (the six unadjudicated class-(C) findings)

Source of findings: `intermediates/split-decomp-kappa-1-r3-findings.md`, section
"Routine (C) findings, reported without forcing the verdict". One blind pass, verdict CLEAN,
no triage and no revision on record until now (PROGRESS.md §3).

**Tally: 4 UPHELD / 0 OVERRULED / 2 PEDANTIC / 0 NEEDS-SOURCE / 0 UNCLEAR.**
No UPHELD finding touches a numbered *theorem* statement. One narrows a *lemma* statement
(Lemma 0) with no downstream effect. Total repair: four localised edits, ~5 lines.

Every disputed quantitative point was checked by exact/grid computation rather than by
reasoning; the script is reproduced in §7 and its three results are quoted inline.

---

## 1. UPHELD — Lemma 0 asserts a single `D'` for both paired quantities; the proof gives one per pair

Lemma 0's statement is a conjunction: "there is a deterministic such `D'` with (i)
`Adv_{Y,D} <= Adv_{Y,D'}` **and** `|Pr[Real=1]-Pr[Real_0=1]|` no larger for `D` than for `D'`".
Its proof fixes one quantity, writes it as `|E_rho alpha(rho)| <= max_rho |alpha(rho)|`,
takes `rho*` a maximiser, and closes with "the argument is identical for either paired
experiment, which gives both parts of the statement". It does not: the two experiments have
different maximising coin strings, and domination of two averages by one coin fixing is not a
formal consequence of the argument given. Machine check (§7, check 3): with two deterministic
strategies of profiles `(A,B) = (1/2,0)` and `(0,1/2)` and equal weights the mixture sits at
`(1/4,1/4)` and the set of deterministic strategies dominating both is empty. So the proof
technique cannot deliver the conjunction; whether the conjunction is nevertheless true in the
experiment space is not established anywhere in r3.

**Minimal repair (one clause, no downstream effect).** Restate Lemma 0 per experiment, as
`kappa-2-r2` already does in its own restatement: "Fix either one of the two paired
experiments. For every ... there is a deterministic `D'` with the corresponding quantity no
smaller, and of the same challenge resolution." Every downstream use — Theorem A
(`kappa^na(q)`, `kappa(0)`), Theorem B (`kappa(q)`) — invokes exactly one quantity at a time,
so the scoped form suffices verbatim.

Not PEDANTIC: an unproved conjunction in a numbered lemma is citable, and it *was* cited —
`kappa-2-r2` had to re-derive the scoped version for itself.

## 2. UPHELD (scoping only, three words) — Lemma P Step 2 needs `S_zeta <= S-bar`; the order of the argument is nevertheless correct

Two separate questions; the referee got the first right and the second is fine.

*Does Step 2 need `S_zeta <= S-bar`?* Not for the part that matters. `delta_zeta` is defined
from the **actual** `S_zeta`, so CDGS Claim 2's parameter satisfies
`(S_zeta + log 1/gamma)/(delta_zeta log M) = P` identically; density, disjointness and
`|I_j| <= P` therefore hold at every `zeta`, bad or good, with no appeal to `S-bar`. But Step 2's
*case split* does need it: the sentence "If `delta_zeta > 1` the asserted bound exceeds
`q log M >= q`, hence is vacuous" compares `delta_zeta > 1`, i.e.
`S_zeta + log 1/gamma > P log M`, against a bound whose numerator carries `S-bar`, not `S_zeta`.
Machine check (§7, check 2): over a grid of `(log M, gamma, sigma, P, q, S_zeta)` the vacuity
claim fails at 299946 points, **every one of them with `S_zeta > S-bar`, and none with
`S_zeta <= S-bar`**. Smallest witness: `log M = 1`, `gamma = 1/8`, `sigma = 0` (so `S-bar = 5`),
`P = 11`, `q = 1`, `S_zeta = 9`; the asserted bound is `0.9773 < 1 = q log M`, so it is not
vacuous while `delta_zeta = 12/11 > 1`.

*Is the order wrong?* No. `S_zeta <= S-bar` off `B` is not "recovered in Step 4"; it is the
**definition of `B` in Step 1** (`B := {zeta : S_zeta > S-bar}`), available before Step 2 is
written. Step 4 additionally charges the whole of `B` at `Pr[z in B] < gamma`, bounding its
contribution by 1 — which covers bad `zeta` whatever family Step 2 assigns there, including the
uniform one. There is no circularity and no missing payment: the two `gamma`'s of Lemma P's
`+2gamma` are exactly `B` (Step 1) and the Claim-2 residue (Step 4), and Step 4's arithmetic
reproduces the stated `q(sigma+2+2 log gamma^{-1})/P + 2gamma` exactly.

**Minimal repair.** Step 2, opening: "Fix `zeta` **not in `B`**" (or a parenthesis: "for
`zeta in B` the bound need not be vacuous, and none is claimed: Step 4 charges all of `B` to
`Pr[z in B] < gamma`"). Nothing else moves. Lemma P's conclusion is untouched.

## 3. PEDANTIC — Lemma P Step 3 averages over the challenge but not over `D`'s coins

No repair recommended. Two independent reasons the omission cannot mislead. (i) Card S1
records that CDGS Claim 3's own proof "assumes without loss of generality that `D` is
deterministic", so the cited bound `T delta log M` is already a bound for every coin string;
being uniform in `rho`, it survives averaging by the same one-line argument the text spells out
for the challenge. (ii) Lemma 0 is available in the artifact if one prefers derandomisation
first. The referee states both exits itself. Adding "and over `D`'s coins" is a free three
words if a reviser is in the file anyway, but this is not a defect.

## 4. UPHELD — Section 0's item (C') drops the per-coin qualifier

Item (A) says "for each fixed coin string ... (and the coin quantifier is load-bearing)".
Item (C') says only "provided either the observer's query positions are independent of the
challenge value". That is verbatim the in-law phrasing whose ambiguity round 2 upheld as
finding G1 — the ruling that produced r3 — and r3's own Section 4 exhibits the `N = M = 2`,
`q = 1` observer that is challenge-independent in law and has per-coin resolution 2, i.e. lies
outside Theorem C''s branch 1 and inside Section 9's Barrier 1. Item (C') therefore advertises
a strictly larger class than Theorem C' proves. Theorem C' itself is unambiguous ("`D` has
challenge resolution 1", per-coin by Section 4), so this is scope-of-the-overview only; but
the same wording in the same document was already ruled a defect once, and consistency of the
record requires the same ruling here.

**Minimal repair.** In item (C'): "provided either the observer's query positions are, **for
each fixed coin string**, independent of the challenge value, or `M <= sigma'/sqrt(27 delta)`."

## 5. UPHELD — Section 0's item (C) writes `Y^{P,gamma}` where Theorem C proves `Y^{P,gamma/2}`

Real, and it makes item (C)'s display false as written; but it is confined to item (C).
Lemma P at slack `g` gives `q(sigma+2+2 log g^{-1})/P + 2g`. Theorem C instantiates `g = gamma/2`,
so the residue is `2(gamma/2) = gamma` and the numerator `sigma+2+2 log(2/gamma)` is at most
`2(sigma' + log gamma^{-1})` via `sigma+2 <= sigma'` and `2 <= sigma'`. At `g = gamma` the
residue is `2gamma`, not `gamma`. Machine check (§7, check 1): on the grid, item (C)'s displayed
bound fails to cover Lemma P at slack `gamma` at 159 points (e.g. `gamma = 1/2`, `q = 0`, any
`P`: proved `1.0` against claimed `0.5`), and covers it at **0 failures** when read at
`gamma/2`. The discrepancy is purely additive slack; the leading constant `2` in
`2(sigma'+log gamma^{-1})q/P` is correct at either slack.

**Minimal repair.** Item (C): write `Y^{P,gamma/2}`, matching Theorem C. (Equivalently keep
`Y^{P,gamma}` and write `+2gamma`; the superscript is the smaller edit and keeps the two
statements literally identical.)

## 6. PEDANTIC — Section 10's CDGS Claim 2 bullet leans on a card invariant written for the uniform variable

The observation is correct as bibliographic hygiene and changes no mathematics, so no repair
is required. Card S1 defines `X` as uniform over `[M]^N` and then records the invariant as
`Pr[Y=y] = Pr[X=y | X in supp(Y)]`; r3's Section 10 cites that invariant for two things —
that each `lambda_j X_j` is the restriction of `X_z` to `supp X_j`, and that the residue
carries `X_z`-mass at most `gamma`. Read with `X` uniform the invariant is false at
initialisation (`Y = X_z`, which is not flat in general), so its `X` must be `X_z`; that
referent was already settled on the record by the r2 triage (finding G14, same argument), and
r3's Section 10 was written to that ruling. Independently, both conclusions have the shorter
route the referee alludes to and the card already supplies: disjoint supports (card point 2)
plus each component being a conditioning of `Y` gives the restriction property, and Claim 2's
own "`X_z` is `gamma`-close to ..." measures the residue under `X_z` by definition. Two routes,
same conclusion.

*Note for the register, not a repair:* these two conclusions **are** load-bearing (Lemma P
Steps 3 and 4 both use them), so if a reviser is editing Section 10 for other reasons, naming
the shorter route alongside the invariant is cheap insurance. See §9 for the standing,
non-blocking source item.

---

## 7. Computation of record

`/private/tmp/.../scratchpad/tri.py`, three checks, exact `Fraction`/float grids:

1. Item (C) display vs Lemma P: 159 failures at slack `gamma`, 0 at slack `gamma/2`.
2. Step 2 vacuity claim: 299946 failures, all with `S_zeta > S-bar`, 0 with `S_zeta <= S-bar`;
   smallest witness `(log M, gamma, sigma, P, q, S_zeta) = (1, 1/8, 0, 11, 1, 9)`, bound `0.9773`.
3. Lemma 0: mixture profile `(1/4,1/4)` from deterministic profiles `(1/2,0)`, `(0,1/2)`;
   no deterministic dominator.

## 8. Escalation list (UNCLEAR)

Empty. All six were decidable from the artifact, the Contract and the two cards.

## 9. SOURCE REQUEST (consolidated)

**No finding was ruled NEEDS SOURCE; nothing here blocks the revision.** One advisory item,
which belongs in the source queue and *not* in the reviser's list:

- **CDGS**, ePrint 2017/937, Appendix A, p. 40 (proof of Claim 2), and p. 10 (Claim 2
  statement). Wanted: the referent of `X` in the recursion invariant
  `Pr[Y=y] = Pr[X=y | X in supp(Y)]` and in the halting test `Pr[X in supp(Y)] > gamma`, both
  transcribed on card S1 with `X` the uniform variable. Card S1 is the only witness and was
  transcribed from a local PDF; PROGRESS.md §3 records that no source card in this campaign has
  ever been checked against the paper it summarises. Purpose: replace an inference the campaign
  currently holds by an internal consistency argument (r2 triage G14) with a direct quotation.
  Ruling 6 does not depend on the answer.

## 10. Answers to the three campaign questions

**(a) Is any of the six load-bearing?** Only finding 6's two conclusions, and they are
licensed twice over, so nothing breaks. Findings 1, 3, 4, 5 are not load-bearing: Lemma 0 is
used one quantity at a time; Step 3's coin averaging is supplied by the cited claim itself;
items (C) and (C') are overview text that Theorems C and C' state correctly. Finding 2,
checked hardest as instructed: Step 2's inference does need `S_zeta <= S-bar`, *only* for its
vacuity case split, and the failures are confined to `zeta in B` (0 of 299946 off `B`). The
order of the argument is **right**, not wrong: `S_zeta <= S-bar` off `B` comes from Step 1's
definition of `B`, not from Step 4, and Step 4's separate `Pr[z in B] < gamma` charge covers
bad `zeta` irrespective of the family assigned there. Lemma P's conclusion, and hence Theorem C
and Theorem C', stand unchanged.

**(b) Does finding 5's factor of two propagate?** No. It is a statement-level slip in the
Section 0 overview and stops there. Theorem C already reads `Y := Y^{P,gamma/2}` and Theorem C'
already reads `Y = Y^{P,gamma/2}`; the `gamma/2` instantiation is what turns Lemma P's `2gamma`
into the Contract's `+gamma`, and it is legal because `gamma/2` is a function of `gamma`, so the
family still depends only on `(S_1,S_2,P,gamma)` as `conj:main` demands. No constant moves:
`c = 2` and `C = 8` are unaffected, and the leading `2(sigma'+log gamma^{-1})q/P` is correct at
either slack. Purely a typo in item (C).

**(c) Does any UPHELD finding change a THEOREM statement?** No numbered theorem's statement or
constant changes. Findings 4 and 5 edit Section 0 overview items; finding 2 scopes a proof
step. Finding 1 does narrow a numbered **lemma** statement (Lemma 0) — but strictly narrows it,
to what its own proof gives and what its two call sites use, so no theorem inherits a change.
An errata note is therefore defensible; the four edits together are about five lines, so a
mechanical r4 diff is cheaper than maintaining errata and is what we recommend. It needs no
re-proof and no new blind pass beyond the four passes r3 still owes.
