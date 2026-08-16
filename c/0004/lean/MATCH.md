# Match check: c/0004 informal statement against `Statement.lean`

**Checked by:** Claude Opus 5 (Anthropic), 16 August 2026. This is an **AI**
match check (`statement_match: ai`), not a human one. A human reading this
table against both artifacts is what moves the badge past sigma 3; nothing
here substitutes for that.

**Informal source:** the `## Statement` tab of `c/0004/index.qmd`, at
`statement_sha` `f1912b71a20280296f203bfc35d3a1cd32fd140957c06fdaa4f107207bf85e79`
(revision 1). If that hash moves, this table is stale by construction and
`scripts/status_badge.py` forces `statement_match` back to `open`.

**Formal source:** `Statement.lean`, theorem `Conjura0004.lhl_public_seed`,
built against Mathlib `v4.33.0` (`db584cd6d46c92f209a44c0f1c829460d327499d`)
on `leanprover/lean4:v4.33.0`.

## Setting

| Informal | Lean | Notes |
|---|---|---|
| `𝒦` nonempty finite (seeds) | `(K : Type) [Fintype K] [Nonempty K]` | |
| `𝒟` nonempty finite (inputs) | `(D : Type) [Fintype D] [Nonempty D]` | |
| `ℛ` nonempty finite (outputs) | `(R : Type) [Fintype R] [Nonempty R]` | |
| `K := \|𝒦\|` | `Fintype.card K` | |
| `D := \|𝒟\|` | `Fintype.card D` | |
| `R := \|ℛ\|` | `Fintype.card R` | |
| `Fun(𝒦 × 𝒟, ℛ)` | `Table K D R := K × D → R` | `abbrev`, so definitionally the function type |
| `H ←$ Fun(𝒦 × 𝒟, ℛ)` | `PMF.uniformOfFintype (Table K D R)` | uniform on the whole function space, not on any subfamily |
| `SD(·,·)`, `U_ℛ` | not used | the statement tab defines them but the conjecture is phrased via `Adv^{ext-pub}`, so neither appears in the formal statement |
| auxiliary information `z` | `(Z : Type)`, no instances | see Discrepancy 1 |

## The three adversaries

All three are "computationally unbounded and receive the entire function
table of `H` as an explicit input". Each is modelled as an **arbitrary
function** whose first argument is the whole table. Arbitrary is exactly
unbounded: there is no complexity class to quantify over, and no oracle
interface to restrict what they may read.

| Informal | Lean |
|---|---|
| source `S`, `(x, z) ←$ S(H)` | `Source K D R Z := Table K D R → PMF (D × Z)` |
| predictor `P`, `x' ←$ P(H, z)` | `Predictor K D R Z := Table K D R → Z → PMF D` |
| distinguisher `D`, `b' ←$ D(H, sd, y_b, z)` | `Distinguisher K D R Z := Table K D R → K → R → Z → PMF Bool` |

The predictor takes `z` and **not** `x`; the distinguisher takes `sd`
explicitly, which is what makes this the public-seed variant rather than the
secret-seed one. Both are visible in the arities above.

## Game `Pred^S_P`

| Line | Informal | Lean (`predGame`) |
|---|---|---|
| 1 | `H ←$ Fun(𝒦 × 𝒟, ℛ)` | `(PMF.uniformOfFintype (Table K D R)).bind fun H =>` |
| 2 | `(x, z) ←$ S(H)` | `(S H).bind fun xz =>` |
| 3 | `x' ←$ P(H, z)` | `(P H xz.2).bind fun x' =>` |
| 4 | `return (x = x')` | `PMF.pure (decide (xz.1 = x'))` |

`xz.1` is `x`, `xz.2` is `z`.

## Game `Ext-pub^S_D`

| Line | Informal | Lean (`extGame`) |
|---|---|---|
| 1 | `H ←$ Fun(𝒦 × 𝒟, ℛ)` | `(PMF.uniformOfFintype (Table K D R)).bind fun H =>` |
| 2 | `(x, z) ←$ S(H)` | `(S H).bind fun xz =>` |
| 2 | `sd ←$ 𝒦` | `(PMF.uniformOfFintype K).bind fun sd =>` |
| 3 | `y₁ ←$ ℛ` | `(PMF.uniformOfFintype R).bind fun y₁ =>` |
| 4 | `b ←$ {0,1}` | `(PMF.uniformOfFintype Bool).bind fun b =>` |
| 3 | `y₀ ← H(sd, x)` | inlined as the `else` branch below |
| 5 | `b' ←$ D(H, sd, y_b, z)` | `(Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>` |
| 6 | `return (b = b')` | `PMF.pure (decide (b = b'))` |

Bit convention: `b = false` is the real challenge `y₀ = H(sd, x)` and
`b = true` is the uniform one `y₁`, so that `false ↦ 0` and `true ↦ 1`
matches `y₀`/`y₁`.

Note what the sanity lemmas do *not* check. Swapping this convention would
leave `extAdv_eq_zero_of_subsingleton` provable, because under
`Subsingleton R` the two branches are equal and which one `b = true` selects
stops mattering. The convention is therefore held only by the definition and
its docstring, and it is a place a human match check should look. It is not
load-bearing for the conjecture either way, since the bound is symmetric in
the two branches, but it would matter to any proof that unfolds the game.

`y₀` is not sampled: it is a deterministic function of values already drawn,
so inlining it changes nothing about the distribution. Sampling `y₁`
unconditionally (rather than only when `b = true`) likewise changes nothing,
and matches the informal game, which also draws it unconditionally.

## Advantages and unpredictability

| Informal | Lean |
|---|---|
| `Adv^pred_{𝒦,𝒟,ℛ,S}(P) := Pr[Pred^S_P ⇒ 1]` | `predAdv S P := (predGame S P true).toReal` |
| `Adv^{ext-pub}_{𝒦,𝒟,ℛ}(S,D) := 2 Pr[Ext-pub^S_D ⇒ 1] − 1` | `extAdv S Dist := 2 * (extGame S Dist true).toReal - 1` |
| `S` is ε-unpredictable iff `Adv^pred(P) ≤ ε` for **every** unbounded `P` | `Unpredictable ε S := ∀ P : Predictor K D R Z, predAdv S P ≤ ε` |

`⇒ 1` is the game returning `true`, so the probability is the mass the
`PMF Bool` puts on `true`. `.toReal` moves from `ℝ≥0∞` to `ℝ`; the value is
never `⊤` (a `PMF` mass is at most 1), so nothing is lost.

## The conjecture

| Informal | Lean |
|---|---|
| "There is a universal constant `c > 0`, independent of `𝒦`, `𝒟`, `ℛ` and `ε`" | `∃ c : ℝ, 0 < c ∧ ∀ (K D R Z : Type) ... (ε : ℝ), ...` |
| "for all nonempty finite `𝒦, 𝒟, ℛ`" | the `∀ (K D R Z : Type)` block with its `Fintype`/`Nonempty` instances |
| "all `ε ∈ (0,1]`" | `(ε : ℝ), 0 < ε → ε ≤ 1 →` |
| "every ε-unpredictable source `S`" | `∀ S : Source K D R Z, Unpredictable ε S →` |
| "every unbounded distinguisher `D`" | `∀ Dist : Distinguisher K D R Z,` |
| `Adv^{ext-pub} ≤ c·(√(εR) + √(log₂ D / K))` | `extAdv S Dist ≤ c * (Real.sqrt (ε * Fintype.card R) + Real.sqrt (Real.logb 2 (Fintype.card D) / Fintype.card K))` |

**Quantifier order is the content.** `c` is bound outermost, before the
types, before `ε`, before `S` and `D`. A `c` allowed to depend on any of
them would make the statement vacuous. This is the one thing in the
translation most worth a human's attention.

`log₂ D` is `Real.logb 2 (Fintype.card D)`, with the cardinality coerced
`ℕ → ℝ`. `√` is `Real.sqrt`, which is the junk-value-free square root on
non-negative reals (`Real.sqrt x = 0` for `x < 0`; every argument here is
non-negative, since `ε > 0`, cards are non-negative, and `logb 2 D ≥ 0`
because `D ≥ 1`).

## Discrepancies and judgement calls

1. **`Z` is an arbitrary type, with no `Fintype`.** The informal statement
   never says what alphabet `z` is drawn from. Leaving `Z` unconstrained is
   the weaker assumption and therefore the safer translation: the formal
   claim quantifies over *all* auxiliary-information types, including
   infinite ones, so it implies the finite-alphabet reading rather than
   assuming it. Nothing in the file needs `Z` to be finite or decidable.
   Taxonomy: this is an `Underspecified`/`implicit conventions` point in the
   informal statement, resolved in the direction that does not weaken the
   claim.

2. **Randomized versus deterministic adversaries.** All three are
   `PMF`-valued, i.e. randomized. The informal games write `←$` for all
   three, so this matches. Note it makes `Unpredictable` a slightly stronger
   hypothesis than the deterministic reading would (it quantifies over more
   predictors), and the conclusion a slightly stronger claim (it covers more
   distinguishers); for unbounded adversaries the two readings coincide by
   an averaging argument, which is not formalized here.

3. **`SD` and `U_ℛ` are unused.** The statement tab introduces statistical
   distance and the uniform distribution on `ℛ` in its Setting paragraph,
   but the conjecture as stated is about `Adv^{ext-pub}`, which is defined
   through the game rather than through `SD`. Nothing is lost; they would be
   needed by the proof, not by the statement.

4. **`D ≥ 2` is not assumed.** The Corollary in the Proof tab restricts to
   `D ≥ 2` when quoting `c = 8/5`, and handles `D = 1` separately. The
   *conjecture* makes no such restriction and neither does this file. At
   `D = 1`, `logb 2 1 = 0`, so the second summand vanishes, which is the
   intended reading.

5. **No claim is made about tightness.** `form: tight-bound` in the
   frontmatter describes the problem, not this theorem; the formal statement
   is the upper bound alone, exactly as the informal Conjecture box is.

## What is proved

Nothing about the conjecture. `lhl_public_seed` is `sorry`, and
`#print axioms` reports `sorryAx` for it, as it should.

Six sanity lemmas are `sorry`-free, and `#print axioms` reports only
`propext`, `Classical.choice` and `Quot.sound` for each:

- `predAdv_nonneg`, `predAdv_le_one`, `predAdv_mem_unitInterval` -- the
  prediction advantage is a probability.
- `extAdv_le_one`, `neg_one_le_extAdv` -- the extraction advantage lies in
  `[-1, 1]`.
- `extAdv_eq_zero_of_subsingleton` -- when `\|ℛ\| = 1` the extraction
  advantage is exactly `0`. This is the load-bearing one: it says the two
  challenge branches really are interchangeable when they carry no
  information, which is false for several plausible ways of getting the
  game wrong.

Reproduce with:

```
cd c/0004/lean
lake exe cache get      # optional, but avoids rebuilding Mathlib
lake build              # one warning, on the sorry at Statement.lean:122
lake env lean Audit.lean
```
