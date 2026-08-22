# Triage rulings — split-decomp-kappa-1

4 UPHELD / 2 OVERRULED / 9 PEDANTIC / 0 NEEDS-SOURCE. Findings as collated in
split-decomp-kappa-1-findings.md. Overrulings are recorded so they are not
re-raised on a later pass.

| id | ruling | reason |
|---|---|---|
| F1 | **UPHELD** | Theorem C is stated with kappa(q); Corollary A' bounds only kappa^na(q); the artifact's only bound on kappa(q) (Theorem B) is insufficient in the resolution-1 branch — at N=2^60, delta=2^-60, sigma'=100, M=2^100, q=1 it gives 0.0295 against a target of 7.9e-8. C''s resolution-1 branch is not derivable from the results as stated. |
| F2 | PEDANTIC | Section 0 writes Y^{P,gamma} where Theorem C proves the bound for Y^{P,gamma/2}; the Contract asks only that some family exist per (P,gamma), and Theorem C is correct as stated. |
| F3 | **UPHELD** | The sentence is false — t(1,N) -> 1/sqrt(2) ~ 0.707 (0.7071 at N=2^20, 0.7173 at N=1000) against the claimed >= sqrt(L) ~ 3.86, 2.81 — and it is the artifact's only discharge of the Contract's explicit rem:ell1 demand. |
| F4 | PEDANTIC | The reason given is false (theta varies with f on the revealed set, so more than \|Z\| tests are reached), but Step 3's union bound is over \|Z\| * C(N,k1) * C(N,k2) with the T_{S0,w} partitioning, so nothing depends on the sentence. |
| F5 | **UPHELD** | kappa and kappa^na are suprema over observers the Contract permits to randomise; Proposition 6.2 is proved only for deterministic D; Theorems A and B cite Lemma 0 nowhere; and Lemma 0 nowhere asserts D' inherits challenge resolution 1, which Theorem A's claim requires. |
| F6 | PEDANTIC | Pass 1 is right and pass 4's justification wrong (the card says k in R_{>0}; k'=log floor(1/m)=0 when m>1/2, so the exponent is outside the range — integrality is not the issue), but at k'=0 the conclusion is the triviality pi = sum_u pi(u) delta_u. |
| F7 | **UPHELD** | M=1 is admissible under the Contract; delta_zeta then divides by log M = 0; and the escape clause "exceeds q log M >= q" reads 0 >= 1. Only N >= 2 is assumed. |
| F8 | PEDANTIC | The family is partial (defined only for zeta on-support), but no experiment draws an off-support index and completion by "uniform" is forced and contentless. |
| F9 | PEDANTIC | Correct that the chain needs S_zeta <= Sbar, i.e. zeta not in B; Step 4 charges all of B to Pr[z in B] < gamma, so the per-zeta argument is only ever invoked off B. |
| F10 | PEDANTIC | h is not required surjective, but ranging over image(h) only shrinks the budget, so Lemma 4's conclusion is unchanged. |
| F11 | PEDANTIC | The omitted derivation is two lines and checks out: 5 sqrt(sigma' delta) <= 5 sqrt(sigma' q+ delta), and q delta <= sigma' gives q^2 delta <= sigma' q <= sigma' q+, i.e. q delta <= sqrt(sigma' q+ delta). |
| F12 | **OVERRULED** | "That term" is the displayed 2(sigma'+log gamma^-1)q/P, which at q >= P is >= 2(sigma'+log gamma^-1) > 2 sigma' >= 4 > 1 using only q/P >= 1 and the sigma' >= 2 established in the same sentence. Pass 4 mis-identified the referent; no lower bound on the Lemma P numerator is needed. |
| F13 | PEDANTIC | N >= 2 is stated openly in Section 0 and again in Theorem C''s hypotheses, so it is not an unflagged narrowing; only section 9's list omits it. |
| F14 | PEDANTIC | The crossover claims are explicitly informal, rest on an O(.) the S2 card records as unextracted, and no numbered result depends on them. |
| F15 | **OVERRULED** | Exact arithmetic gives E[m1 m2] - delta_unp^2 = delta(1-delta)(1-1/N)^2 > 0 for every 2 <= M <= N, so the counterexample holds throughout its asserted range. Pass 2 tripped on the artifact's crude rounding E[m_i] <= 2 delta, not on the example. |

## Minimal changes, most load-bearing first

1. **F1.** Restate Theorem C in D-relative form: replace kappa(q) in its statement
   by |Pr[Real=1] - Pr[Real_0=1]| for the D at which it is instantiated — the
   quantity its own first hybrid actually bounds, "|G0 - G1| <= kappa(q)" being a
   weakening applied to that fixed D — and add the corollary "<= kappa(q)" for the
   unconditional form. Theorem C''s first proof line then reads: in the
   resolution-1 branch that quantity is bounded by 6 sqrt(sigma' q+ delta) by
   Corollary A' (equivalently by Proposition 6.2 at M'=1); in the second branch by
   Corollary B'. No new mathematics. The inequality kappa(q) <= kappa^na(q) must
   not be used and is not needed.
2. **F5.** Add to Lemma 0 that D' = D_{rho*} inherits D's challenge resolution
   (immediate once resolution is read per fixed coin string, which the definition
   should say), and cite Lemma 0 explicitly in the proofs of Theorems A and B
   before invoking Proposition 6.2.
3. **F7.** Assume M >= 2 alongside N >= 2, and dispose of M = 1 in one sentence
   (|Fun| = 1, so Real_0 and Dec_0 are identical and the bound is 0).
4. **F3.** Delete the false k1 = 1 computation and replace it with the correct
   mechanism, which the artifact already states a paragraph earlier: with a single
   source emitting a point of [N]^2 the posterior need not factor, so Lemma 1(i),
   and hence the rectangle structure Lemmas 2 and 3 require, is unavailable. The
   correct reading of k1 = 1 is a deterministic first coordinate, not one source.

## Closing

No UPHELD finding threatens the truth of any numbered conclusion. F1 alone
threatens more than presentation: Theorem C''s resolution-1 branch — the
artifact's headline claim — is unproved as written, though its conclusion is
recoverable from Proposition 6.2 already in the artifact via the restatement above.
