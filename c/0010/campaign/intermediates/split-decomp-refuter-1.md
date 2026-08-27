# split-decomp-refuter-1 — the M-corner is a route artifact, and here is the identity that says why

The campaign's **first refuter pass**, and its first counterexample-search code. Target: the sharp
question `PROGRESS.md` §2.2 poses — does `κ(q)` carry *any* `M`-dependence at small `q`, which is
where (H2) binds?

Code and run record: `checks/refuter-mcorner.py` (12 stages, self-documenting, prints its own
grids) and `checks/refuter-mcorner-run.txt` (849 lines, `EXIT=0`). Requires numpy; the run of
record used `/usr/local/bin/python3` (3.13.2, numpy 2.2.3), which the script now states.

## VERDICT: NO COUNTEREXAMPLE FOUND — and the obstruction is identified in closed form

For a flat product source on a `K×K` rectangle (`δ = 1/K`), the **exact** optimal advantage of a
`q`-query observer probing the rectangle is
```
adv(q,M) = Phi(min(q,K²), M) / K²,     Phi(q,M) := (M/2)·E|Bin(q,1/M) − q/M|
```
because, conditioned on the observer's transcript, `E[ρ(v) | transcript] − 1/M = (n_v − q/M)/K²`.
**Averaging kills the histogram fluctuation; only the mass of the inspected cells survives, and
that carries no `M`.** Consequences, all measured:

- `Phi(q,M)` increases in `M` with limit **exactly `q`**, so `adv ≤ qδ²` for **every** `M`.
- Deficit law `1 − Phi(q,M)/q = (1−o(1))·q/M`.
- `δ√M` is reached only at `q = K² = 1/δ²`.

**Independently re-verified for this record**, not taken on the pass's word: the deficit law at
`q ∈ {16, 256, 4096}` and `M/q ∈ {64, 1024}` gives ratio-to-`q/M` of `0.9922`–`0.9995`; and the
exact values `κ(1) = 1/8, 1/6, 3/16, 5/24, 7/32` at `N=2`, `M = 2,3,4,6,8` reproduce
`δ²(1 − 1/M)` exactly.

## The separation, with a cleaner argument than the pass gave

The pass reported the `M`-dependence onset (`q ≈ M`) and the (H2)-failure corner
(`q < 4Mδ/σ' − 1`) as "separated by a factor `σ'/(4δ)`". That is true but understates it, and its
stated bound is backwards. **The two regions are disjoint in every non-vacuous instance, provably:**

Appreciable `M`-dependence needs `M ≲ q`. (H2) fails needs `M > σ'q⁺/(4δ)`. Both together give
`q ≳ M > σ'q⁺/(4δ)`, hence `4δq > σ'q⁺ > σ'q`, hence `4δ > σ'`. Since `σ' ≥ 2` and `δ ≤ 1`, this
needs `σ' < 4δ ≤ 4`, i.e. `2 log N ≤ σ' < 4`, i.e. `N ∈ {2,3}` with `δ` near `1`. **Every such
point is vacuous** (`5√(σ'δ) ≥ 5√(2·½) = 5 > 1`). Checked over a 30×4×5 grid: two points satisfy
`4δ > σ'` at all, both vacuous, zero non-vacuous.

**Correction to the pass.** It wrote the separation factor as "`σ'/(4δ) ≥ σ'N/4`". The direction is
wrong: `δ ∈ [1/N, 1]` gives `σ'/4 ≤ σ'/(4δ) ≤ σ'N/4`. The factor is *at most* `σ'N/4`, and it is
large exactly when `δ` is small — which is the regime of interest, so the point survives.

Made vivid by the pass's own stage 4, at `δ = 1/N`, `N = 2²⁰`: the FIT mechanism's `M`-dependence
has died by `M = 2³` at `q = 1` while the corner needs `M > 2²⁴`; by `M = 2¹³` at `q = 1024` while
the corner needs `M > 2³³`.

## Where the `δ√M` comes from, abstractly

`δ√M` enters through Lemma B, whose union runs over **all `2^M` tests** `θ : [M] → {0,1}` — which
grants the observer a test depending on all of `f`. A `q`-query observer's decision on challenge
`v` depends on `f` only through that challenge's own `q`-cell transcript. `kappa-2-r3` §4 already
says this in words ("what is lossy — necessarily, and only for small `q` — is bounding a `q`-query
observer's advantage by the full statistical distance"); this pass turns it into an exact identity
and measures the gap.

## The near-miss

The attack that *would* carry `M` at `q = 1` is a one-query certificate: fix `u : [M] → [N]²`,
accept iff `f(u(y)) = y`. It accepts with probability `~1/M` in `Real₀` and probability `1` in
`Real` if every cell of the source's rectangle certifies — advantage `≈ 1` at arbitrarily small
`δ`. **What stops it:** each certifiable cell is an event of probability `≈ 2/M`, so planting it on
all `K²` cells costs `K² log M` bits against the `2K log(N/K)` bits of freedom in choosing the
rectangle, and the yield falls like `1/log M`. Measured exhaustively at `N = 8`, `K = 2`: max
certifiable density `0.80 → 0.66 → 0.44 → 0.35 → 0.28 → 0.215` as `M` goes `2 → 1024`. The
advantage *decreases* in `M`.

Also settled negatively: **steering buys nothing at `q = 1`** (challenge-steered vs fixed cell:
`0.0613` vs `0.0613` at `K=4`, `0.00367` vs `0.00386` at `K=16`, all `≈ δ²`), and **leakage cannot
create `M`-dependence** — it acts as `σ/log M` extra probed cells, i.e. it buys queries, and `σ`
enters the target as `√(σ'δ)` faster than it enters any attack.

## Method validation

The alternating maximisation was checked against **exhaustive enumeration of the entire observer
space** in 10/10 cases, agreeing to `≤ 1.2·10⁻¹³`, including 32768 observers at `(N,M,q) = (2,3,1)`.
66 best witnesses were recomputed in exact rational arithmetic *and* by an independent Monte-Carlo
simulation touching none of the algebra; all agree. Stage 5 used a **train/test split** — observer
fitted on 40000 oracles, scored on 40000 fresh ones — so overfitting cannot manufacture a witness,
and it visibly does not (train `0.895` vs test `0.390` at large `M`).

## What this does NOT rule out

Recorded because a negative result is only worth its stated scope.

1. **Anything at non-vacuous parameters by enumeration.** Non-vacuity with `δ ≥ 1/N` forces
   `N > 50 log N`, so the smallest non-vacuous instance has `N ≥ 512`, `N² ≥ 2.6·10⁵` cells and
   `|Fun| = M^{262144}`. The exact search probes the **functional form** at tiny `N`; only the
   model-based and sampled stages reach the corner.
2. **A mechanism outside the catalogue at large `N`.** Exact search at `N ≤ 3` found nothing
   outside {HIT, PLANT, FIT}, and a small theorem closes `q = 1` for all value-symmetric sources at
   every `M`. Neither is a proof at large `N`.
3. **`q ≥ 3` exactly.** Exact optima cover `q ≤ 2`; larger `q` rests on the identity and Monte
   Carlo.
4. **Randomised leakage.** Only deterministic `z_i = ξ_i(f)` was searched. Convexity suggests no
   gain, but it is a restriction on the search space and so weakens the negative.
5. **The `M`-free bound itself.** Nothing here proves `κ(q) ≤ O(√(σ'δ)) + μ'(q)`.

What it *does* rule out: the campaign's only lower-bound family, Proposition F's, as a possible
witness below `q ≈ M`. For that family `κ(q) = Phi(q,M)/N² ≤ qδ²` for every `M` — by the
posterior-mean identity, verified against the full adaptive steered optimum at `q ≤ 2`.

## Byproducts

1. **Proposition F off the diagonal, at `q = δ⁻²` instead of `N²`.** The FIT family with
   `K = 1/δ` gives `κ(1/δ²) ≈ δ√(M/2π)`, which is **1.57–2.22×** Proposition F's constant for
   `K ∈ {4,…,32}` and all `2 ≤ M ≤ K²`. Discharges part of §2.4's debt. It does *not* reach the
   corner: `1/δ² < σ'/(4δ³)` always, so the family is always inside (H2).
2. **Exact `κ` at the boundary:** `κ(q) = Phi(q,M)/N²` for every `M, q` when `δ = 1/N`, which
   forces both sources uniform.
3. **A gap no artifact states:** for `M ≥ 1/(4δ²)` with `q ≥ 1`, **both arms of Corollary D″
   exceed 1**, so the campaign has no non-trivial bound at all there. (`q = 0` is still covered
   `M`-freely by Theorem A.)

## The lead, and it is where proving effort should go

Replace Lemma B's union over `2^M` tests by a union over `q`-query **transcripts**:
`C₁ = M ln2 + ln(4N²/γ₀)` becomes `C₁' = q ln(N²M) + ln(4N²/γ₀)`, turning `δ√M` into
`δ√(q log(N²M))`. Over a 7840-point grid the resulting ratio to the target `√(σ'q⁺δ)` is
**≤ 1.78 inside the meaningful corner** and `≤ 3.94` anywhere, against **29.92** for the present
union. So the repair is arithmetically sufficient to close the corner.

What it does not supply, and this is the real work: the transcript-**conditioned** rectangle
discrepancy bound. The source's rectangle is chosen after seeing `f`, so it is not
transcript-measurable, and the union over rectangles must be taken *inside* the conditioning —
which is where `√(σ'δ)` comes from.

### END OF ARTIFACT split-decomp-refuter-1 ###
