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

## Outstanding

In dependency order. Nothing below is claimed.

1. **Fact 2.1, the bound** (`distAdv_le_SD`): for every unbounded, possibly
   randomized `A`, `distAdv P₀ P₁ A ≤ SD P₀ P₁`. The definitions are in place
   (`distGame`, `distAdv`); the algebra reduces the advantage to
   `∑ ω, A(ω)(true) · (P₁ ω - P₀ ω)`, which `sum_pos_part_eq_SD` then bounds.
2. **Fact 2.1, attainment**: the maximum-a-posteriori test attains it, so the
   `max` over `A` is a maximum and not just a supremum.
3. **Lemma 3.1 (analytic forms)**: `max_D extAdv = 𝔼[Δ_{H,Z}]` and
   `max_P predAdv = 𝔼[ε_{H,Z}]`. Needs 1 and 2, plus the factorization of the
   view distance over the `K` rows.
4. **Lemma 5.1 (flattening)**: reduce to sources supported on a fixed-size set.
5. **Lemma 5.2 (mean at a fixed support)**: the mean statistical distance for
   one fixed support.
6. **Fact 2.2 (bounded differences)**, finite special case over the uniform
   function space. The single largest item, and the one Mathlib does not help
   with.
7. **Lemma 5.3 (uniform deviation)**: 6 applied uniformly over all supports of
   all sizes, with the binomial estimate (Fact 2.3).
8. **Assembling** into `lhl_public_seed`.

Supporting facts the informal proof also uses, not yet formalized: Fact 2.3
(`C(D,t) ≤ (eD/t)^t`), Fact 2.4 (`𝔼|X - 𝔼X| ≤ √Var X`), Fact 2.5 (Jensen,
available in Mathlib), Fact 2.6 (two-term Cauchy-Schwarz, trivial), Fact 2.7
(`(1-1/R)^R ≥ 1/4` for `R ≥ 2`).

## Discipline

Every entry in the "proved" table compiles with no `sorry` and was committed
the moment it did. No proved lemma is deleted to chase the headline theorem.
`proof_formal` moves off `open` only if `lhl_public_seed` compiles
`sorry`-free and `#print axioms` shows nothing beyond the three standard
axioms.
