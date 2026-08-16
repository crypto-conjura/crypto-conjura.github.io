# Proof ledger for c/0004

What is proved in Lean, and what is not. The page's `proof_formal` stays
`open` until `lhl_public_seed` itself compiles with no `sorry`; this file is
the honest account of the distance still to go.

Last updated: 16 August 2026. Mathlib `v4.33.0`
(`db584cd6d46c92f209a44c0f1c829460d327499d`), `leanprover/lean4:v4.33.0`.

## Mathlib audit

Done before any formalizing, because the shape of the campaign depends on it.
Searched the pinned Mathlib tree for the concentration inequality the informal
proof's third step needs:

| Sought | Found in Mathlib v4.33.0 |
|---|---|
| McDiarmid / bounded differences | **absent** (zero occurrences of `McDiarmid`; one incidental `bounded_difference`) |
| Azuma-Hoeffding | present, but only in the martingale/measure-theoretic setting (`Mathlib/Probability/Martingale/`) |
| Hoeffding (iid sums) | one incidental occurrence, not the inequality in usable form |
| Chebyshev, Bernstein, Chernoff | present in various forms, none of them the bounded-differences statement |
| Statistical / total variation distance on a `PMF` | **absent** (`totalVariation` exists only for vector/signed measures) |

Consequence, and it is the main structural finding of this campaign: the
informal proof's Fact 2.2 (McDiarmid) is not available off the shelf, and
neither is its Fact 2.1 (statistical distance as optimal advantage). Both have
to be proved here. Fact 2.1 is done; Fact 2.2 is not started.

Using the measure-theoretic Azuma would mean carrying the whole
`ProbabilityTheory` filtration apparatus into a setting that is finite in
every direction, which is the opposite of the design decision recorded in
`Statement.lean`. The finite special case should be proved directly.

## Proved, `sorry`-free

`#print axioms` shows only `propext`, `Classical.choice`, `Quot.sound` for
each of these.

### `Statement.lean` (sanity lemmas, from T7)

| Declaration | Says |
|---|---|
| `predAdv_nonneg` | prediction advantage is `≥ 0` |
| `predAdv_le_one` | prediction advantage is `≤ 1` |
| `predAdv_mem_unitInterval` | prediction advantage is a probability |
| `extAdv_le_one` | extraction advantage is `≤ 1` |
| `neg_one_le_extAdv` | extraction advantage is `≥ -1` |
| `extAdv_eq_zero_of_subsingleton` | `\|R\| = 1` gives extraction advantage exactly `0` |

### `Proof.lean` section 1: statistical distance

| Declaration | Says |
|---|---|
| `rmass`, `rmass_nonneg`, `rmass_le_one` | real-valued point mass of a `PMF`, in `[0,1]` |
| `sum_rmass` | a `PMF` on a finite type has total real mass `1` |
| `SD` | statistical distance as half the l1 distance |
| `SD_nonneg`, `SD_le_one`, `SD_comm`, `SD_self` | it is a `[0,1]`-valued symmetric quantity vanishing on the diagonal |
| `sum_pos_part_eq_SD` | `∑ max(Q ω - P ω, 0) = SD P Q` |

`sum_pos_part_eq_SD` is the identity the optimal-distinguisher bound turns on:
a distinguisher can only collect mass where `Q` outweighs `P`, and because the
two totals agree, that one-sided sum is the whole statistical distance.

### `Proof.lean` section 2: Fact 2.1, in full

| Declaration | Says |
|---|---|
| `distGame`, `distAdv` | the distinguishing game and its advantage |
| `distGame_apply_true`, `distGame_toReal` | the winning probability, written out, in `ℝ≥0∞` and in `ℝ` |
| `distAdv_eq` | `distAdv = ∑ ω, A(ω)(true) · (P₁ ω - P₀ ω)` |
| **`distAdv_le_SD`** | **Fact 2.1, bound**: no unbounded randomized `A` beats `SD P₀ P₁` |
| `mapTest`, **`distAdv_mapTest`** | **Fact 2.1, attainment**: the MAP test achieves it |
| `isGreatest_distAdv` | so `SD P₀ P₁` is the *greatest* achievable advantage, not just an upper bound |

### `Proof.lean` section 3: the bridge from the game to the analysis

| Declaration | Says |
|---|---|
| `View`, `viewDist`, `onView` | the distinguisher's view, and its law under each challenge bit |
| `distGame_viewDist` | `distGame` on the two view laws, binds flattened |
| `extGame_eq_distGame` | the extraction game **is** a distinguishing game between the two view laws |
| **`extAdv_le_SD_views`** | `extAdv S Dist ≤ SD (viewDist S false) (viewDist S true)` |
| `mapDist`, `extAdv_mapDist` | the MAP test, curried back into a legal `Distinguisher`, attains it |
| **`isGreatest_extAdv`** | **Lemma 3.1, first half**: the best extraction advantage *is* the view distance |

### `Proof.lean` section 3b: the predictor side

| Declaration | Says |
|---|---|
| `maxMass` | `∑ z, max_x Pr[(x, z)]`, the analytic form of the best prediction advantage on a fixed table |
| `predGame_toReal` | the prediction probability, written out in `ℝ` |
| **`predAdv_le_maxMass`** | **Lemma 3.1, predictor half (bound)**: no unbounded predictor beats `𝔼_H[maxMass]` |

With everything finite, `𝔼_{(H,Z)}[ε_{H,Z}]` needs no conditioning to write
down: `p(z) · max_x p(x \| z) = max_x p(x, z)`, so the quantity is just
`∑ z, max_x p(x, z)` averaged over the table. Attainment (the mode predictor)
is not done; only the bound.

`extGame_eq_distGame` is the only structurally awkward step, and it is
entirely bookkeeping: the game samples the challenge bit last, a distinguishing
game samples it first, so the bit is walked outwards through four
`PMF.bind_comm`s.

**One restriction, recorded honestly.** Section 3 assumes `[Fintype Z]`, which
the conjecture does not. `SD` is a `Finset` sum, so the view type has to be
finite, and the view carries the auxiliary information `z`. `Statement.lean`
deliberately leaves `Z` arbitrary. Removing the restriction means redoing
section 1 with `tsum` (legitimate, since a `PMF` is countably supported) and is
listed below.

## Outstanding

In dependency order. Nothing below is claimed.

1. **Drop `[Fintype Z]` from section 3.** Redo `SD` and section 1 with `tsum`
   rather than `Finset.sum`. Mechanical but not short: it needs summability
   side conditions that the finite version gets for free.
2. **Lemma 3.1, second half**: factor `SD (viewDist S false) (viewDist S true)`
   as `𝔼_{(H,Z)}[Δ_{H,Z}]`, the average over the `K` rows of
   `SD(ν^{H,z}_k, U_R)`. This is where the informal proof's one structural
   observation lives, that publishing the seed moves the average over rows
   *outside* the statistical distance. Needs conditioning on `(H, Z)`, which
   in `PMF` terms means exhibiting the view law as a product.
3. **Lemma 3.1, predictor half, attainment**: the bound is proved
   (`predAdv_le_maxMass`); the mode predictor witnessing equality is not.
   Needs a choice of argmax per `(H, z)`, which is routine but unwritten.
4. **Lemma 5.1 (flattening)**: reduce to sources supported on a fixed-size set.
5. **Lemma 5.2 (mean at a fixed support)**.
6. **Fact 2.2 (bounded differences)**, finite special case over the uniform
   function space. The single largest item, and the one Mathlib does not help
   with at all.
7. **Lemma 5.3 (uniform deviation)**: 6 applied uniformly over all supports of
   all sizes, with the binomial estimate (Fact 2.3).
8. **Assembling** into `lhl_public_seed`.

Supporting facts the informal proof also uses, not formalized and not
attempted: Fact 2.3 (`C(D,t) ≤ (eD/t)^t`), Fact 2.4 (`𝔼|X - 𝔼X| ≤ √Var X`),
Fact 2.5 (Jensen, available in Mathlib), Fact 2.6 (two-term Cauchy-Schwarz,
trivial), Fact 2.7 (`(1-1/R)^R ≥ 1/4` for `R ≥ 2`, which needs the
monotonicity of `(1-1/R)^R` and so is not the one-liner it looks like).

Realistic assessment: items 4 through 8 are the mathematics, and item 6 alone
is a substantial project. What is done here is Fact 2.1 in full, the
game-to-analysis bridge in both directions, and the predictor bound: the part
that had to come first, because everything above it is phrased in terms of
it.

## Discipline

Every entry in the "proved" table compiles with no `sorry` and was committed
the moment it did. No proved lemma is deleted to chase the headline theorem.
`proof_formal` moves off `open` only if `lhl_public_seed` compiles
`sorry`-free and `#print axioms` shows nothing beyond the three standard
axioms.
