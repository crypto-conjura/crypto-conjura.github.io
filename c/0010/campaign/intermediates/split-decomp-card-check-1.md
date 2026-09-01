# split-decomp-card-check-1 — both source cards checked against their papers

The first time any card in this campaign has been checked against the paper it summarises.
`PROGRESS.md` had named this the weakest link, on the grounds that CDGS Claims 2 and 3 enter the
entire chain through r3's Lemma P on transcription alone.

Both cards reached **full text**, including the CDGS appendix that everything turns on.

## Verdict: both cards are substantively sound. No mathematical defect in either.

**Card S1 (CDGS, ePrint 2017/937, 8 Aug 2022).** Claims 25 and 26 exist with exactly those numbers
on printed p. 40, saying exactly what the card says. All three "consequences beyond the statement"
are genuinely established by the proof text, and the card's concession that they are not in the
statement is honest and accurate. Claim 2's `P' = (S_z + log 1/γ)/(δ log M)` matches character for
character. Claim 3 matches, both arms, along with the H-coefficient proof description, the wlog,
and `p_{X'} ≤ M^{-(1-δ)T}`, `p_{Y'} = M^{-T}`.

**Definition 1's "at most P" is verbatim, p. 10, for both notions** — the thing
`split-decomp-kappa-4`'s Theorem H turns on. It is load-bearing *in the paper itself*: the
γ-closeness step (p. 41) replaces `Y_final` by the uniform distribution, which fixes **zero**
coordinates, so Claim 2 is *false* under an "exactly P" reading.

**Card S2 (CFHS, ePrint 2025/1258 and LIPIcs 343:10).** Every transcription is faithful — Theorem
3's statement, the MSE and Pred games, `Adv^mse := 2 Pr[·] − 1`, the §1.4 example symbol for
symbol, and Lemma 3's and Lemma 4(3)'s content. Both observations the card records against Theorem
3 are correct, and one is stronger than the card claimed.

## What the check found that nobody knew

**S1-A. The chain uses four consequences beyond Claim 2's statement, not three.** The exact
decomposition with bounded residue — `μ_ζ = Σ λ_j X_j + λ_fin Y_fin`, each `λ_j X_j` a restriction
of `μ_ζ`, and `λ_fin ≤ γ` from the loop condition — is what r3's Lemma P uses, and is not Claim 2's
stated γ-closeness. Added to the card.

**S1-B. Disjointness holds for the exact decomposition only, and this is a trap.** Claim 2's
γ-close object, as the paper realises it, replaces `Y_final` by uniform, whose support is all of
`[M]^N`. Lemma P is safe because it uses the exact form. Anyone "simplifying" Lemma P to quote
Claim 2 literally would silently lose the deterministic-index property that makes `Y_{f,ζ}` well
defined and `lem:hit` applicable. Warned on the card.

**S1-C. A fillable hole in the source.** Claim 26 as printed bounds `|I| ≤ S/(δ log M)` — with `S`,
not `S + log γ⁻¹`. The version Lemma P needs at every recursion step exists only in **footnote 15,
p. 41**: "easily adapted to account for entropy deficiency `S + log 1/γ`". It genuinely is easy, by
the card's own first consequence, but the numerator Lemma P sets equal to `P δ_ζ log M` rests on a
one-line footnote in someone else's appendix. Recorded nowhere in the campaign until now.

**S1-D. Also worth knowing:** the paper states Claims 25/26 once, for the first recursion step
only; their re-application at every later step is left implicit, licensed by exactly the card's
first consequence. So that consequence is not a re-reading of the paper — it is a step the paper
itself needs and does not write down. And Lemma 1 has a *second* multiplicative arm,
`2^{(S+2 log 1/γ)T/P}·(·) + 2γ`, which the card omitted; `PROGRESS.md`'s note ruling out "the
multiplicative form of Claim 3" does not cover it.

**S2-A. A defect in CFHS itself, verified three ways.** Theorem 3's statement has radical index
`ℓ+1`; the final case of its proof delivers `ℓ+2`. Confirmed from the **text layer** of both the
ePrint (statement p. 28, proof p. 33) and the independently typeset LIPIcs version (10:16, 10:20).
The mechanism was re-derived by hand: the incompressibility gain is *quadratic* in `ε`, giving
`ε^{ℓ+2} 2^{kℓ}(1−α)^ℓ/((bℓ)^ℓ (log M)^{ℓ+2})`, exactly the paper's displayed line, whereas Theorem
2's gain is *linear*, giving `ε^{ℓ+1}` — which is why Theorem 2/21 states its exponent correctly. In
the only regime where the bound says anything (`u < 1`), `u^{1/(ℓ+2)} > u^{1/(ℓ+1)}`, so the stated
bound is strictly stronger than the proved one. **Inert for this chain** — Theorem 3's bound is used
nowhere in it — and live only for prose quoting CFHS's rate.

**S2-B. `[CFHS, Lemma 4.3]` does not exist.** It is Lemma 4, item 3, of a three-item lemma titled
"Numeric inequalities", p. 9. Every citation in that form is unresolvable. This had propagated into
`c/0010/latex/capping.tex`'s Assumption 4 and was fixed there. That file was removed from the
working tree on 1 September 2026 and survives only in git history.

**S2-C. The reference number differs between versions.** Lemma 3 cites `[33]` in the ePrint and
`[34]` in LIPIcs, where `[33]` is **Unruh, CRYPTO 2007** — a different paper, separately
load-bearing here. The work cited is Vadhan, *Pseudorandomness*, Now Publishers 2012.

**S2-D. Footnote 4/8 was dropped and mattered.** CFHS themselves write that their §1.4 example "is
an attack on directly applying decomposition as a proof technique", and that the leakages "can be
made unpredictable by simply appending random bits". The first half **corroborates the campaign's
own reading** that the `Pδ` cost is a defect of the route rather than of the statement — from the
source paper. The second half is needed because the example as written specifies only the leakages,
never the points, so it does not by itself exhibit an unpredictable pair.

**S2-E. Two glosses were backwards.** "Up to the factor-of-two convention" — the `2p−1`
normalisation *removes* the factor, so `sup_D Adv^mse` equals `κ(q)` exactly. And "exactly the
Contract's κ" is true of the advantage *measure* only; the bounds differ in exponent and carry
`+ℓN` against `+2 log N`.

## Corrected on the cards

Page citations: S1's Claim 2 is on p. 11 not p. 10, and Claim 3 is stated p. 11 and proved
pp. 11–12; S2's Lemma 3 and Lemma 4 are on p. 9 not p. 8. Both cards said "read from a local PDF
copy", which is unreproducible — no copy of 2017/937 exists on this machine — and now cite
retrievable URLs. S1's stated version date, 8 August 2022, is confirmed against the file's own
title page.

## What remains open

The EUROCRYPT proceedings version of CDGS was not reached (paywall) and **cannot** substitute: the
paper's own bibliography marks the ePrint as the full version, and a 32-page proceedings version
cannot contain the p. 40 appendix. Every campaign citation to "Appendix A, p. 40" is necessarily an
ePrint citation and must stay one.

A live lead, not reached: the general one-source form of Claim 2 — for an arbitrary
bounded-deficiency source, with disjoint components — circulates in the lifting literature as the
"density-restoring partition". If a numbered statement of it exists, the campaign's three (now four)
consequences become citable instead of proof-read, and its most-flagged fragility disappears.
Candidate sources are Göös's thesis and Kothari–Meka–Raghavendra (STOC 2017), neither reached.

### END OF ARTIFACT split-decomp-card-check-1 ###
