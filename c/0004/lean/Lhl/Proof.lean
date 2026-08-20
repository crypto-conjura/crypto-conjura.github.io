import Lhl.Statement

/-!
# Proof of the public-seed leftover-hash-lemma conjecture

This file proves `Lhl.PublicSeedConjecture` (Conjecture 2 of `statement.tex`), following the proof
of Theorem `thm:main` / Corollary `cor:pub` in `resolution.tex`. `Lhl.SecretSeedConjecture` is not
addressed here: the note itself leaves it open.

Only the parts of `resolution.tex` on the dependency chain to `cor:pub` are formalized. In
particular the following are all skipped: the "closed form" second inequality of `eq:main-plain`
(not used by `cor:pub`), part (ii) of Lemma `unif` (feeds only the unused `eq:main-sharp`), and
`Fact cover` / `Fact hidden` / `Proposition prop:false` (about a third, different conjecture that
does not appear in `Basic.lean`).

A handful of facts `resolution.tex` imports as "standard facts", confirmed absent from Mathlib and
substantial to formalize from scratch, are recorded as axioms rather than reproved: McDiarmid's
inequality (`fact_mcd`) and the binomial estimate `(D.choose t : ℝ) ≤ (e*D/t)^t` (`fact_binom`).
Everything else the note calls a standard fact (Cauchy-Schwarz, mean absolute deviation, the
optimal distinguishing-advantage bound, Jensen's inequality) is proved directly: for our finite
alphabets these are short, and Jensen is already in Mathlib.
-/

namespace Lhl.PublicSeed

/- `PublicSeedConjecture` quantifies over `R` without `DecidableEq R`, while the row-empirical
definitions below need it. Everything here is already noncomputable, so classical decidability is
brought in globally: an explicit `[DecidableEq R]` in context (as in the ambient section variables
below) is still used preferentially by instance search, and this only fills the gap at the final
theorem, where `R` arrives with no such instance supplied. -/
set_option linter.style.openClassical false
open scoped Classical

open Finset

variable {K D R : Type} [Fintype K] [Fintype D] [Fintype R]
  [Nonempty K] [Nonempty D] [Nonempty R] [DecidableEq K] [DecidableEq D] [DecidableEq R]

section StandardFacts

/-- Statistical distance between two real-valued weight functions on a `Fintype`. -/
noncomputable def SD {α : Type*} [Fintype α] (f g : α → ℝ) : ℝ :=
  (1 / 2) * ∑ a, |f a - g a|

/-- **Fact (Cauchy-Schwarz, two terms).** -/
theorem fact_cs (a1 a2 b1 b2 : ℝ) :
    (a1 * b1 + a2 * b2) ^ 2 ≤ (a1 ^ 2 + a2 ^ 2) * (b1 ^ 2 + b2 ^ 2) := by
  nlinarith [sq_nonneg (a1 * b2 - a2 * b1)]

/-- `max 0 a` is the average of `|a|` and `a`; the elementary identity driving both `fact_mad` and
`fact_sd`. -/
theorem max_zero_eq_half_add_abs (a : ℝ) : max 0 a = (|a| + a) / 2 := by
  rcases le_total 0 a with h | h
  · rw [max_eq_right h, abs_of_nonneg h]; ring
  · rw [max_eq_left h, abs_of_nonpos h]; ring

/-- **Fact (mean absolute deviation).** For a real random variable of finite support (modelled
here as a `Fintype`-indexed family with weights `p`), `E|X - EX| ≤ √(Var X)`, via Cauchy-Schwarz
applied to `⟪√p·|X - EX|, √p⟫`. -/
theorem fact_mad {α : Type*} [Fintype α] (p : α → ℝ) (hp0 : ∀ a, 0 ≤ p a)
    (hp1 : ∑ a, p a = 1) (X : α → ℝ) :
    ∑ a, p a * |X a - ∑ a, p a * X a| ≤
      Real.sqrt (∑ a, p a * (X a - ∑ a, p a * X a) ^ 2) := by
  set m := ∑ a, p a * X a
  have hCS : (∑ a, Real.sqrt (p a) * |X a - m| * Real.sqrt (p a)) ^ 2 ≤
      (∑ a, (Real.sqrt (p a) * |X a - m|) ^ 2) * ∑ a, (Real.sqrt (p a)) ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq Finset.univ _ _
  have e1 : ∀ a, Real.sqrt (p a) * |X a - m| * Real.sqrt (p a) = p a * |X a - m| := by
    intro a; rw [mul_right_comm, Real.mul_self_sqrt (hp0 a)]
  have e2 : ∀ a, (Real.sqrt (p a) * |X a - m|) ^ 2 = p a * (X a - m) ^ 2 := by
    intro a; rw [mul_pow, Real.sq_sqrt (hp0 a), sq_abs]
  have e3 : ∀ a, (Real.sqrt (p a)) ^ 2 = p a := fun a => Real.sq_sqrt (hp0 a)
  simp_rw [e1, e2, e3] at hCS
  rw [hp1, mul_one] at hCS
  have hpos : 0 ≤ ∑ a, p a * |X a - m| :=
    Finset.sum_nonneg (fun a _ => mul_nonneg (hp0 a) (abs_nonneg _))
  have hpos2 : 0 ≤ ∑ a, p a * (X a - m) ^ 2 :=
    Finset.sum_nonneg (fun a _ => mul_nonneg (hp0 a) (sq_nonneg _))
  exact (Real.le_sqrt hpos hpos2).mpr hCS

/-- **Fact (optimal distinguishing advantage).** For any two weight functions `P0, P1` on a
`Fintype` of equal total mass, and any `[0,1]`-valued `α` (the probability that a possibly
randomized test outputs `1`), the advantage `∑ α*(P1-P0)` is bounded by the statistical distance.
-/
theorem fact_sd {Ω : Type*} [Fintype Ω] (P0 P1 α : Ω → ℝ)
    (hα0 : ∀ ω, 0 ≤ α ω) (hα1 : ∀ ω, α ω ≤ 1) (hmass : ∑ ω, P0 ω = ∑ ω, P1 ω) :
    ∑ ω, α ω * (P1 ω - P0 ω) ≤ SD P0 P1 := by
  have hpt : ∀ ω, α ω * (P1 ω - P0 ω) ≤ max 0 (P1 ω - P0 ω) := by
    intro ω
    rcases le_total 0 (P1 ω - P0 ω) with h | h
    · calc α ω * (P1 ω - P0 ω) ≤ 1 * (P1 ω - P0 ω) :=
            mul_le_mul_of_nonneg_right (hα1 ω) h
        _ = max 0 (P1 ω - P0 ω) := by rw [one_mul, max_eq_right h]
    · calc α ω * (P1 ω - P0 ω) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos (hα0 ω) h
        _ = max 0 (P1 ω - P0 ω) := by rw [max_eq_left h]
  calc ∑ ω, α ω * (P1 ω - P0 ω) ≤ ∑ ω, max 0 (P1 ω - P0 ω) :=
        Finset.sum_le_sum (fun ω _ => hpt ω)
    _ = ∑ ω, (|P1 ω - P0 ω| + (P1 ω - P0 ω)) / 2 := by
        simp_rw [max_zero_eq_half_add_abs]
    _ = SD P0 P1 := by
        rw [← Finset.sum_div, Finset.sum_add_distrib]
        have hz : ∑ ω, (P1 ω - P0 ω) = 0 := by
          rw [Finset.sum_sub_distrib, hmass, sub_self]
        rw [hz, add_zero]
        have habs : ∑ ω, |P1 ω - P0 ω| = ∑ ω, |P0 ω - P1 ω| :=
          Finset.sum_congr rfl (fun ω _ => by rw [abs_sub_comm])
        rw [habs]
        change (∑ ω, |P0 ω - P1 ω|) / 2 = (1 / 2) * ∑ ω, |P0 ω - P1 ω|
        ring

/-- **Fact (McDiarmid / bounded differences), finitary form.** Axiomatized: absent from Mathlib,
and deriving it from Mathlib's sub-Gaussian Azuma machinery would require constructing a
Doob martingale from the bounded-differences hypothesis, a substantial project on its own. Stated
purely combinatorially (fraction of a finite product type, no measure theory) since every space in
this file's application is finite. -/
axiom fact_mcd {ι Ω : Type*} [Fintype ι] [DecidableEq ι] [Fintype Ω] [Nonempty Ω]
    (g : (ι → Ω) → ℝ) (c : ι → ℝ)
    (hbd : ∀ i (v v' : ι → Ω), (∀ j, j ≠ i → v j = v' j) → |g v - g v'| ≤ c i)
    {lam : ℝ} (_hlam : 0 < lam) :
    ((Finset.univ.filter
        (fun v : ι → Ω => (Fintype.card (ι → Ω) : ℝ)⁻¹ * ∑ v', g v' + lam ≤ g v)).card : ℝ)
      / Fintype.card (ι → Ω)
      ≤ Real.exp (-(2 * lam ^ 2) / ∑ i, c i ^ 2)

/-- **Fact (binomial estimate).** `resolution.tex` cites this as a standard fact, and it's an
explicit TODO in Mathlib's own source (`Mathlib/Data/Nat/Choose/Bounds.lean`'s docstring: "we
might want to add ... `n.choose r ≤ e^r n^r / r^r` in the future") — but it turns out to be a
short combination of two pieces Mathlib already has (`Nat.choose_le_pow_div` and
`Stirling.le_factorial_stirling`), so it gets a real proof rather than an axiom. -/
theorem fact_binom (Dcard t : ℕ) (_ht1 : 1 ≤ t) (_htD : t ≤ Dcard) :
    (Dcard.choose t : ℝ) ≤ (Real.exp 1 * Dcard / t) ^ t := by
  have ht0 : (0 : ℕ) < t := _ht1
  have htR : (0 : ℝ) < (t : ℝ) := by exact_mod_cast ht0
  have ht1R : (1 : ℝ) ≤ (t : ℝ) := by exact_mod_cast _ht1
  -- Step 1: `C(D,t) ≤ D^t / t!`.
  have h1 : (Dcard.choose t : ℝ) ≤ (Dcard : ℝ) ^ t / (Nat.factorial t : ℝ) :=
    Nat.choose_le_pow_div t Dcard
  -- Step 2: `(t/e)^t ≤ t!`, via Stirling's lower bound `√(2πt)·(t/e)^t ≤ t!` and `√(2πt) ≥ 1`.
  have hsqrt : (1 : ℝ) ≤ Real.sqrt (2 * Real.pi * t) := by
    rw [Real.le_sqrt' (by norm_num : (0 : ℝ) < 1)]
    nlinarith [Real.pi_gt_three, ht1R]
  have hstirling : Real.sqrt (2 * Real.pi * t) * ((t : ℝ) / Real.exp 1) ^ t ≤
      (Nat.factorial t : ℝ) :=
    Stirling.le_factorial_stirling t
  have hpowpos : (0 : ℝ) ≤ ((t : ℝ) / Real.exp 1) ^ t := by positivity
  have h2 : ((t : ℝ) / Real.exp 1) ^ t ≤ (Nat.factorial t : ℝ) := by
    have hmul := mul_le_mul_of_nonneg_right hsqrt hpowpos
    rw [one_mul] at hmul
    exact hmul.trans hstirling
  -- Step 3: flat multiplicative identity `(eD/t)^t · (t/e)^t = D^t` (no nested division/inverses,
  -- which `ring`/`field_simp` cannot cancel automatically).
  have hDpowpos : (0 : ℝ) ≤ (Real.exp 1 * Dcard / t) ^ t := by positivity
  have key : (Real.exp 1 * Dcard / t) ^ t * ((t : ℝ) / Real.exp 1) ^ t = (Dcard : ℝ) ^ t := by
    rw [← mul_pow]
    have : Real.exp 1 * (Dcard : ℝ) / t * ((t : ℝ) / Real.exp 1) = (Dcard : ℝ) := by
      field_simp
    rw [this]
  -- Step 4: combine via `D^t = (eD/t)^t·(t/e)^t ≤ (eD/t)^t · t!`, then divide by `t! > 0`.
  have hfactpos : (0 : ℝ) < (Nat.factorial t : ℝ) := by exact_mod_cast Nat.factorial_pos t
  have step : (Dcard : ℝ) ^ t ≤ (Real.exp 1 * Dcard / t) ^ t * (Nat.factorial t : ℝ) := by
    calc (Dcard : ℝ) ^ t = (Real.exp 1 * Dcard / t) ^ t * ((t : ℝ) / Real.exp 1) ^ t := key.symm
      _ ≤ (Real.exp 1 * Dcard / t) ^ t * (Nat.factorial t : ℝ) :=
          mul_le_mul_of_nonneg_left h2 hDpowpos
  have final : (Dcard : ℝ) ^ t / (Nat.factorial t : ℝ) ≤ (Real.exp 1 * Dcard / t) ^ t := by
    rw [div_le_iff₀ hfactpos]
    exact step
  exact h1.trans final

end StandardFacts

section Setup

/-- The uniform weight function on `R`. -/
noncomputable def unifR (R : Type*) [Fintype R] : R → ℝ := fun _ => (Fintype.card R : ℝ)⁻¹

variable (S : Source K D R)

/-- `Pr[X=x, Z=z | H]`, as a real number, from the source's PMF. -/
noncomputable def sourceProb (H : Table K D R) (x : D) (z : Aux) : ℝ := (S H (x, z)).toReal

/-- `Pr[Z=z | H] = ∑_x Pr[X=x,Z=z|H]`, the marginal probability of the auxiliary output. -/
noncomputable def margZ (H : Table K D R) (z : Aux) : ℝ := ∑ x : D, sourceProb S H x z

/-- `p^{H,z}_x := Pr[X=x | H, Z=z]` (junk value `0` when the view `(H,z)` has probability `0`). -/
noncomputable def condX (H : Table K D R) (z : Aux) (x : D) : ℝ :=
  sourceProb S H x z / margZ S H z

/-- `ε_{H,z} := max_x p^{H,z}_x`. -/
noncomputable def epsHz (H : Table K D R) (z : Aux) : ℝ :=
  Finset.univ.sup' Finset.univ_nonempty (condX S H z)

variable (K D R) in
/-- The pushforward of a weight function `p` on `D` along the row `H(k,·)`. Applied to
`p = condX S H z` this is `ν^{H,z}_k`; applied to `p = ` the uniform indicator of `T`, this is
`emp^H_{k,T}`. Unifying the two makes the convexity argument of `lemma_flat` a single computation
rather than two parallel ones. -/
noncomputable def rowDistOf (H : Table K D R) (p : D → ℝ) (k : K) (r : R) : ℝ :=
  ∑ x : D, if H (k, x) = r then p x else 0

variable (K D R) in
/-- `(1/K) ∑_k SD(rowDistOf H p k, U_R)`; specializes to `Δ_{H,z}` and to `F_T(H)`. -/
noncomputable def DeltaOf (H : Table K D R) (p : D → ℝ) : ℝ :=
  (Fintype.card K : ℝ)⁻¹ * ∑ k : K, SD (rowDistOf K D R H p k) (unifR R)

/-- `Δ_{H,z} := (1/K) ∑_k SD(ν^{H,z}_k, U_R)`. -/
noncomputable def DeltaHz (H : Table K D R) (z : Aux) : ℝ :=
  DeltaOf K D R H (condX S H z)

/-- `E_{(H,Z)}[f] := (1/|Table|) ∑_H ∑'_z Pr[Z=z|H] * f(H,z)`. -/
noncomputable def expectHZ (f : Table K D R → Aux → ℝ) : ℝ :=
  (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, ∑' z : Aux, margZ S H z * f H z

variable (K D R) in
/-- The uniform weight function on a `t`-subset `T ⊆ D` (junk `0` outside `T`). -/
noncomputable def Tindicator (T : Finset D) : D → ℝ := fun x => if x ∈ T then (T.card : ℝ)⁻¹ else 0

variable (K D R) in
/-- `F_T(H) := (1/K) ∑_k SD(emp^H_{k,T}, U_R)`. -/
noncomputable def Fdist (H : Table K D R) (T : Finset D) : ℝ :=
  DeltaOf K D R H (Tindicator D T)

variable (K D R) in
/-- `Φ_H(t) := max_{|T|=t} F_T(H)`. -/
noncomputable def Phi (H : Table K D R) (t : ℕ) : ℝ :=
  if h : (Finset.univ.filter (fun T : Finset D => T.card = t)).Nonempty
  then (Finset.univ.filter (fun T : Finset D => T.card = t)).sup' h (Fdist K D R H)
  else 0

variable (K D R) in
/-- `a := 1 + ln D`. -/
noncomputable def aConst : ℝ := 1 + Real.log (Fintype.card D)

variable (K D R) in
/-- `W₁(H) := max_{1≤t≤D} (Φ_H(t) - (1/2)√(R/t))`. -/
noncomputable def W1 (H : Table K D R) : ℝ :=
  (Finset.Icc 1 (Fintype.card D)).sup'
    (Finset.nonempty_Icc.mpr Fintype.card_pos)
    (fun t => Phi K D R H t - (1 / 2) * Real.sqrt (Fintype.card R / t))

end Setup

section Analytic

variable (S : Source K D R)

/-- A mode of `p^{H,z}`: an input achieving the maximum `ε_{H,z}`. -/
noncomputable def modeX (H : Table K D R) (z : Aux) : D :=
  (Finset.exists_mem_eq_sup' Finset.univ_nonempty (condX S H z)).choose

theorem condX_modeX (H : Table K D R) (z : Aux) :
    condX S H z (modeX S H z) = epsHz S H z :=
  (Finset.exists_mem_eq_sup' Finset.univ_nonempty (condX S H z)).choose_spec.2.symm

/-- The mode predictor: on view `(H,z)`, deterministically outputs a mode of `p^{H,z}`. -/
noncomputable def Pmode : Predictor K D R := fun H z => PMF.pure (modeX S H z)

/-- Half of `Lemma analytic`: the mode predictor's advantage equals `E_{(H,Z)}[ε_{H,Z}]`. Combined
with `IsUnpredictable`, applied to this one predictor, this is enough to bound the mean deficiency
— we never need the full "these games' value *equals* this statistic" equality for an arbitrary
optimal predictor. -/
theorem predAdv_Pmode_eq : predAdv S (Pmode S) = expectHZ S (epsHz S) := by
  -- Crux per-term identity: `sourceProb = margZ * condX`, unconditionally (no case split needed
  -- at call sites below: when `margZ = 0`, every individual `sourceProb` is `0` too).
  have hsp : ∀ (H : Table K D R) (z : Aux) (x : D),
      sourceProb S H x z = margZ S H z * condX S H z x := by
    intro H z x
    by_cases hz : margZ S H z = 0
    · have hnn : ∀ y ∈ (Finset.univ : Finset D), 0 ≤ sourceProb S H y z :=
        fun y _ => ENNReal.toReal_nonneg
      have hsum0 : ∑ y : D, sourceProb S H y z = 0 := hz
      have hx0 := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hsum0 x (Finset.mem_univ x)
      rw [hx0, hz, zero_mul]
    · rw [condX, mul_div_cancel₀ _ hz]
  -- Bridge the `do`-notation defining `predGame` down to concrete `PMF.bind`/`PMF.pure`
  -- (purely structural: provable by `rfl` since `PMF.bind_apply`/`PMF.pure_apply` are `rfl`, and
  -- the `do`-notation elaborates through the generic `Monad`/`Bind`/`Pure` classes, which `simp`
  -- cannot see through to match those lemmas syntactically, but `rfl` can).
  have hbridge : predGame S (Pmode S) = (PMF.uniformOfFintype (Table K D R)).bind (fun H =>
      (S H).bind (fun p => (Pmode S H p.2).bind (fun x' => PMF.pure (decide (p.1 = x'))))) := rfl
  have hcard0 : (Fintype.card (Table K D R) : ENNReal) ≠ 0 := by
    exact_mod_cast (Fintype.card_pos (α := Table K D R)).ne'
  have hcardTop : ((Fintype.card (Table K D R) : ENNReal))⁻¹ ≠ ⊤ := ENNReal.inv_ne_top.mpr hcard0
  -- Value of the game at `true`, as a tsum-of-tsum in `ENNReal`.
  have hval : predGame S (Pmode S) true =
      ∑' H : Table K D R, (Fintype.card (Table K D R) : ENNReal)⁻¹ *
        ∑' z : Aux, S H (modeX S H z, z) := by
    rw [hbridge, PMF.bind_apply]
    apply tsum_congr
    intro H
    rw [PMF.uniformOfFintype_apply, PMF.bind_apply]
    have step : ∀ p : D × Aux,
        S H p * ((Pmode S H p.2).bind (fun x' => PMF.pure (decide (p.1 = x')))) true =
          if p.1 = modeX S H p.2 then S H p else 0 := by
      intro p
      have hcollapse : (Pmode S H p.2).bind (fun x' => PMF.pure (decide (p.1 = x'))) =
          PMF.pure (decide (p.1 = modeX S H p.2)) := by
        change (PMF.pure (modeX S H p.2)).bind (fun x' => PMF.pure (decide (p.1 = x'))) = _
        rw [PMF.pure_bind]
      rw [hcollapse, PMF.pure_apply]
      by_cases hc : p.1 = modeX S H p.2
      · simp [hc]
      · simp [hc]
    have hsum : ∑' p : D × Aux,
        S H p * ((Pmode S H p.2).bind (fun x' => PMF.pure (decide (p.1 = x')))) true =
          ∑' z : Aux, S H (modeX S H z, z) := by
      simp_rw [step]
      rw [ENNReal.tsum_prod', ENNReal.tsum_comm]
      apply tsum_congr
      intro z
      exact tsum_ite_eq (modeX S H z) (fun x => S H (x, z))
    rw [hsum]
  -- Finiteness of the inner sum, needed to push `.toReal` through the outer one.
  have hHfin : ∀ H : Table K D R, ∑' z : Aux, S H (modeX S H z, z) ≠ ⊤ := by
    intro H
    have hinj : Function.Injective (fun z : Aux => (modeX S H z, z)) :=
      fun z1 z2 h => congrArg Prod.snd h
    have hle := ENNReal.tsum_comp_le_tsum_of_injective hinj (S H)
    rw [PMF.tsum_coe] at hle
    exact ne_top_of_le_ne_top ENNReal.one_ne_top hle
  -- Push `.toReal` through both layers of `tsum`, then identify each term with `margZ * epsHz`.
  unfold predAdv
  rw [hval, ENNReal.tsum_toReal_eq (fun H => ENNReal.mul_ne_top hcardTop (hHfin H))]
  have hHterm : ∀ H : Table K D R,
      ((Fintype.card (Table K D R) : ENNReal)⁻¹ * ∑' z : Aux, S H (modeX S H z, z)).toReal =
        (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑' z : Aux, margZ S H z * epsHz S H z := by
    intro H
    rw [ENNReal.toReal_mul, ENNReal.toReal_inv, ENNReal.toReal_natCast,
      ENNReal.tsum_toReal_eq (fun z => (S H).apply_ne_top _)]
    have hz : ∑' z : Aux, (S H (modeX S H z, z)).toReal =
        ∑' z : Aux, margZ S H z * epsHz S H z := by
      apply tsum_congr
      intro z
      change sourceProb S H (modeX S H z) z = margZ S H z * epsHz S H z
      rw [hsp H z (modeX S H z), condX_modeX]
    rw [hz]
  simp_rw [hHterm]
  rw [tsum_fintype, expectHZ, Finset.mul_sum]

set_option maxHeartbeats 8000000 in
/-- Half of `Lemma analytic`: for an *arbitrary* distinguisher (not necessarily optimal),
`Adv^extp ≤ E_{(H,Z)}[Δ_{H,Z}]`. This is the direction `Theorem thm:main` actually needs. -/
theorem extPubAdv_le_mean (Dist : PubDistinguisher K D R) :
    extPubAdv S Dist ≤ expectHZ S (DeltaHz S) := by
  -- ===== Phase 1: ENNReal bridging =====
  have hcollapse : ∀ (p : PMF Bool) (b : Bool),
      (p.bind (fun b' => PMF.pure (decide (b = b')))) true = p b := by
    intro p b
    rw [PMF.bind_apply, tsum_fintype, Fintype.sum_bool]
    rcases b with _ | _ <;> simp [PMF.pure_apply]
  have hbridge : extPubGame S Dist = (PMF.uniformOfFintype (Table K D R)).bind (fun H =>
      (S H).bind (fun p =>
        (PMF.uniformOfFintype K).bind (fun sd =>
          (PMF.uniformOfFintype R).bind (fun y₁ =>
            (PMF.uniformOfFintype Bool).bind (fun b =>
              (Dist H sd (if b then y₁ else H (sd, p.1)) p.2).bind (fun b' =>
                PMF.pure (decide (b = b')))))))) := rfl
  have hinner : ∀ (H : Table K D R) (x : D) (z : Aux),
      ((PMF.uniformOfFintype K).bind (fun sd =>
        (PMF.uniformOfFintype R).bind (fun y₁ =>
          (PMF.uniformOfFintype Bool).bind (fun b =>
            (Dist H sd (if b then y₁ else H (sd, x)) z).bind (fun b' =>
              PMF.pure (decide (b = b'))))))) true
        = ∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
            ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
              ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
                Dist H sd (if b then y₁ else H (sd, x)) z b := by
    intro H x z
    rw [PMF.bind_apply]
    apply tsum_congr
    intro sd
    rw [PMF.uniformOfFintype_apply]
    have hy : ((PMF.uniformOfFintype R).bind (fun y₁ =>
        (PMF.uniformOfFintype Bool).bind (fun b =>
          (Dist H sd (if b then y₁ else H (sd, x)) z).bind (fun b' =>
            PMF.pure (decide (b = b')))))) true
        = ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
            ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
              Dist H sd (if b then y₁ else H (sd, x)) z b := by
      rw [PMF.bind_apply]
      apply tsum_congr
      intro y₁
      rw [PMF.uniformOfFintype_apply]
      have hb : ((PMF.uniformOfFintype Bool).bind (fun b =>
          (Dist H sd (if b then y₁ else H (sd, x)) z).bind (fun b' =>
            PMF.pure (decide (b = b'))))) true
          = ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
              Dist H sd (if b then y₁ else H (sd, x)) z b := by
        rw [PMF.bind_apply]
        apply tsum_congr
        intro b
        rw [PMF.uniformOfFintype_apply, hcollapse]
      rw [hb]
    rw [hy]
  have hval : extPubGame S Dist true =
      ∑' H : Table K D R, (Fintype.card (Table K D R) : ENNReal)⁻¹ *
        ∑' p : D × Aux, S H p *
          (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
            ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
              ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
                Dist H sd (if b then y₁ else H (sd, p.1)) p.2 b) := by
    rw [hbridge, PMF.bind_apply]
    apply tsum_congr
    intro H
    rw [PMF.uniformOfFintype_apply, PMF.bind_apply]
    have hsum : ∑' p : D × Aux, S H p *
        ((PMF.uniformOfFintype K).bind (fun sd =>
          (PMF.uniformOfFintype R).bind (fun y₁ =>
            (PMF.uniformOfFintype Bool).bind (fun b =>
              (Dist H sd (if b then y₁ else H (sd, p.1)) p.2).bind (fun b' =>
                PMF.pure (decide (b = b'))))))) true
        = ∑' p : D × Aux, S H p *
          (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
            ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
              ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
                Dist H sd (if b then y₁ else H (sd, p.1)) p.2 b) := by
      apply tsum_congr
      intro p
      rw [hinner H p.1 p.2]
    rw [hsum]
  -- ===== Phase 2: real-number value of the (sd,y₁,b) block, and its ENNReal boundedness =====
  have havg_le_one : ∀ {ι : Type} [Fintype ι] [Nonempty ι] (f : ι → ENNReal), (∀ i, f i ≤ 1) →
      ∑' i : ι, (Fintype.card ι : ENNReal)⁻¹ * f i ≤ 1 := by
    intro ι _ _ f hf
    have hιne0 : (Fintype.card ι : ENNReal) ≠ 0 := by exact_mod_cast (Fintype.card_ne_zero (α := ι))
    rw [tsum_fintype]
    calc ∑ i, (Fintype.card ι : ENNReal)⁻¹ * f i
        ≤ ∑ _i : ι, (Fintype.card ι : ENNReal)⁻¹ * 1 := by
          apply Finset.sum_le_sum; intro i _; gcongr; exact hf i
      _ = 1 := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one, mul_comm]
          exact ENNReal.inv_mul_cancel hιne0 (ENNReal.natCast_ne_top _)
  have hRne0 : (Fintype.card R : ENNReal) ≠ 0 := by exact_mod_cast (Fintype.card_ne_zero (α := R))
  have hBne0 : (Fintype.card Bool : ENNReal) ≠ 0 := by
    exact_mod_cast (Fintype.card_ne_zero (α := Bool))
  have hKne0 : (Fintype.card K : ENNReal) ≠ 0 := by exact_mod_cast (Fintype.card_ne_zero (α := K))
  have hcomplement : ∀ (p : PMF Bool), (p false).toReal = 1 - (p true).toReal := by
    intro p
    have h1 : p true + p false = 1 := by
      have h := p.tsum_coe
      rwa [tsum_fintype, Fintype.sum_bool] at h
    have h2 : (p true).toReal + (p false).toReal = 1 := by
      rw [← ENNReal.toReal_add (p.apply_ne_top true) (p.apply_ne_top false), h1, ENNReal.toReal_one]
    linarith
  have hb_le1 : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K) (y₁ : R),
      (∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b) ≤ 1 :=
    fun H x z sd y₁ => havg_le_one _ (fun b => PMF.coe_le_one _ _)
  have hb_ne_top : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K) (y₁ : R),
      (∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b) ≠ ⊤ :=
    fun H x z sd y₁ => ne_top_of_le_ne_top ENNReal.one_ne_top (hb_le1 H x z sd y₁)
  have hy_le1 : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K),
      (∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
        ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b) ≤ 1 :=
    fun H x z sd => havg_le_one _ (hb_le1 H x z sd)
  have hy_ne_top : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K),
      (∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
        ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b) ≠ ⊤ :=
    fun H x z sd => ne_top_of_le_ne_top ENNReal.one_ne_top (hy_le1 H x z sd)
  have hsd_le1 : ∀ (H : Table K D R) (x : D) (z : Aux),
      (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b) ≤ 1 :=
    fun H x z => havg_le_one _ (hy_le1 H x z)
  have hsd_ne_top : ∀ (H : Table K D R) (x : D) (z : Aux),
      (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b) ≠ ⊤ :=
    fun H x z => ne_top_of_le_ne_top ENNReal.one_ne_top (hsd_le1 H x z)
  have hbfin : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K) (y₁ : R) (b : Bool),
      (Fintype.card Bool : ENNReal)⁻¹ * Dist H sd (if b then y₁ else H (sd, x)) z b ≠ ⊤ := by
    intro H x z sd y₁ b
    exact ENNReal.mul_ne_top (ENNReal.inv_ne_top.mpr hBne0) ((Dist H sd _ z).apply_ne_top b)
  have hmid : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K) (y₁ : R),
      (∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
        Dist H sd (if b then y₁ else H (sd, x)) z b).toReal
      = (1/2) * ((Dist H sd y₁ z true).toReal + (1 - (Dist H sd (H (sd,x)) z true).toReal)) := by
    intro H x z sd y₁
    rw [tsum_fintype, ENNReal.toReal_sum (fun b _ => hbfin H x z sd y₁ b), Fintype.sum_bool,
      show (if true then y₁ else H (sd,x)) = y₁ from if_pos rfl,
      show (if false then y₁ else H (sd,x)) = H (sd,x) from if_neg (by decide)]
    rw [ENNReal.toReal_mul, ENNReal.toReal_mul, ENNReal.toReal_inv, ENNReal.toReal_natCast,
      hcomplement (Dist H sd (H (sd,x)) z)]
    have hcard2 : (Fintype.card Bool : ℝ) = 2 := by rw [Fintype.card_bool]; norm_num
    rw [hcard2]; ring
  have houter : ∀ (H : Table K D R) (x : D) (z : Aux) (sd : K),
      (∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
        ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
          Dist H sd (if b then y₁ else H (sd, x)) z b).toReal
      = (1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
        (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal) := by
    intro H x z sd
    rw [tsum_fintype,
      ENNReal.toReal_sum (fun y₁ _ => ENNReal.mul_ne_top (ENNReal.inv_ne_top.mpr hRne0)
        (hb_ne_top H x z sd y₁))]
    simp_rw [ENNReal.toReal_mul, ENNReal.toReal_inv, ENNReal.toReal_natCast, hmid H x z sd]
    rw [← Finset.mul_sum]
    have hsplit : ∑ r : R, (1/2 : ℝ) * ((Dist H sd r z true).toReal + (1 - (Dist H sd (H (sd,x)) z true).toReal))
        = (∑ r : R, (1/2 : ℝ) * (Dist H sd r z true).toReal) +
          (Fintype.card R : ℝ) * ((1/2) * (1 - (Dist H sd (H (sd,x)) z true).toReal)) := by
      have hpt : ∀ r : R, (1/2 : ℝ) * ((Dist H sd r z true).toReal + (1 - (Dist H sd (H (sd,x)) z true).toReal))
          = (1/2 : ℝ) * (Dist H sd r z true).toReal + (1/2) * (1 - (Dist H sd (H (sd,x)) z true).toReal) := by
        intro r; ring
      simp_rw [hpt]
      rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    rw [hsplit, ← Finset.mul_sum]
    have hRpos : (Fintype.card R : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
    field_simp
    ring
  have hinnerE_toReal : ∀ (H : Table K D R) (x : D) (z : Aux),
      (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
            Dist H sd (if b then y₁ else H (sd, x)) z b).toReal
        = (Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
             (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal)) := by
    intro H x z
    rw [tsum_fintype,
      ENNReal.toReal_sum (fun sd _ => ENNReal.mul_ne_top (ENNReal.inv_ne_top.mpr hKne0)
        (hy_ne_top H x z sd))]
    simp_rw [ENNReal.toReal_mul, ENNReal.toReal_inv, ENNReal.toReal_natCast, houter H x z]
    rw [← Finset.mul_sum]
  -- ===== Phase 2b: the H/p outer layer, to get the real master identity =====
  have hp_to_zx : ∀ H : Table K D R, ∑' p : D × Aux, S H p *
      (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
            Dist H sd (if b then y₁ else H (sd, p.1)) p.2 b)
      = ∑' z : Aux, ∑ x : D, S H (x, z) *
          (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
            ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
              ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
                Dist H sd (if b then y₁ else H (sd, x)) z b) := by
    intro H
    rw [ENNReal.tsum_prod', ENNReal.tsum_comm]
    apply tsum_congr
    intro z
    rw [tsum_fintype]
  have hpz_ne_top : ∀ (H : Table K D R) (z : Aux) (x : D),
      S H (x, z) * (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
            Dist H sd (if b then y₁ else H (sd, x)) z b) ≠ ⊤ :=
    fun H z x => ENNReal.mul_ne_top ((S H).apply_ne_top _) (hsd_ne_top H x z)
  have hz_ne_top : ∀ (H : Table K D R) (z : Aux),
      (∑ x : D, S H (x, z) * (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
            Dist H sd (if b then y₁ else H (sd, x)) z b)) ≠ ⊤ := by
    intro H z
    exact ENNReal.sum_lt_top.mpr (fun x _ => (hpz_ne_top H z x).lt_top) |>.ne
  have hcardTable0 : (Fintype.card (Table K D R) : ENNReal) ≠ 0 := by
    exact_mod_cast (Fintype.card_ne_zero (α := Table K D R))
  have hp_sum_ne_top : ∀ H : Table K D R, (∑' p : D × Aux, S H p *
      (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
        ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
          ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
            Dist H sd (if b then y₁ else H (sd, p.1)) p.2 b)) ≠ ⊤ := by
    intro H
    rw [hp_to_zx]
    apply ne_top_of_le_ne_top ENNReal.one_ne_top
    calc ∑' z : Aux, ∑ x : D, S H (x, z) *
          (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
            ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
              ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
                Dist H sd (if b then y₁ else H (sd, x)) z b)
        ≤ ∑' z : Aux, ∑ x : D, S H (x, z) * 1 := by
          apply ENNReal.tsum_le_tsum
          intro z
          apply Finset.sum_le_sum
          intro x _
          gcongr
          exact hsd_le1 H x z
      _ = 1 := by
          have step1 : ∀ z : Aux, ∑ x : D, S H (x, z) * 1 = ∑' x : D, S H (x, z) := by
            intro z
            rw [tsum_fintype]
            exact Finset.sum_congr rfl (fun x _ => mul_one _)
          simp_rw [step1]
          rw [← ENNReal.tsum_comm, ← ENNReal.tsum_prod']
          exact PMF.tsum_coe (S H)
  -- Abbreviate the (already fully-computed) inner `sd`-average: purely a size/performance
  -- device for the rest of the proof (`set` keeps it definitionally transparent), since spelling
  -- this expression out at every one of the many later usage sites makes several `rw`/`Summable`
  -- elaborations time out.
  set Qexpr : Table K D R → D → Aux → ℝ := fun H x z =>
      (Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
        ((1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
         (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal))
    with hQexpr_def
  have hval2 : (extPubGame S Dist true).toReal =
      (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, ∑' z : Aux, ∑ x : D,
        sourceProb S H x z * Qexpr H x z := by
    rw [hval, ENNReal.tsum_toReal_eq (fun H => ENNReal.mul_ne_top
      (ENNReal.inv_ne_top.mpr hcardTable0) (hp_sum_ne_top H))]
    have hHterm : ∀ H : Table K D R,
        ((Fintype.card (Table K D R) : ENNReal)⁻¹ * ∑' p : D × Aux, S H p *
          (∑' sd : K, (Fintype.card K : ENNReal)⁻¹ *
            ∑' y₁ : R, (Fintype.card R : ENNReal)⁻¹ *
              ∑' b : Bool, (Fintype.card Bool : ENNReal)⁻¹ *
                Dist H sd (if b then y₁ else H (sd, p.1)) p.2 b)).toReal
        = (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑' z : Aux, ∑ x : D,
            sourceProb S H x z *
              ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
                ((1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
                 (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal))) := by
      intro H
      rw [ENNReal.toReal_mul, ENNReal.toReal_inv, ENNReal.toReal_natCast, hp_to_zx H,
        ENNReal.tsum_toReal_eq (hz_ne_top H)]
      congr 1
      apply tsum_congr
      intro z
      rw [ENNReal.toReal_sum (fun x _ => hpz_ne_top H z x)]
      apply Finset.sum_congr rfl
      intro x _
      rw [ENNReal.toReal_mul, hinnerE_toReal H x z]
      rfl
    simp_rw [hHterm]
    rw [tsum_fintype, Finset.mul_sum]
  -- Only `hval2` (and `Qexpr`) survive into Phases 3-4; drop the rest of the (large) ENNReal
  -- bridging context so later elaboration/unification isn't dragging it all along.
  clear hcollapse hbridge hinner hval havg_le_one hRne0 hBne0 hKne0 hcomplement hb_le1 hb_ne_top
    hy_le1 hy_ne_top hsd_le1 hsd_ne_top hbfin hmid houter hinnerE_toReal hp_to_zx hpz_ne_top
    hz_ne_top hcardTable0 hp_sum_ne_top
  -- ===== Phase 3: local infrastructure, then the crux per-(H,z) bound =====
  have margZ_nonneg' : ∀ (H : Table K D R) (z : Aux), 0 ≤ margZ S H z := fun H z =>
    Finset.sum_nonneg (fun x _ => ENNReal.toReal_nonneg)
  have rowDistOf_sum_eq' : ∀ (H : Table K D R) (p : D → ℝ) (k : K),
      ∑ r : R, rowDistOf K D R H p k r = ∑ x : D, p x := by
    intro H p k
    unfold rowDistOf
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl (fun x _ => ?_)
    simp
  have crux_bound : ∀ (H : Table K D R) (z : Aux),
      ∑ x : D, sourceProb S H x z *
        (2 * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
          ((1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
           (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal))) - 1)
        ≤ margZ S H z * DeltaHz S H z := by
    intro H z
    set α : K → R → ℝ := fun sd r => (Dist H sd r z true).toReal with hα_def
    have hα0 : ∀ sd r, 0 ≤ α sd r := fun sd r => ENNReal.toReal_nonneg
    have hα1 : ∀ sd r, α sd r ≤ 1 := fun sd r => by
      have := ENNReal.toReal_mono ENNReal.one_ne_top (PMF.coe_le_one (Dist H sd r z) true)
      rwa [ENNReal.toReal_one] at this
    have hQ_eq : ∀ x : D,
        2 * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
          ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r))) - 1
        = (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd,x))) := by
      intro x
      have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
      have hsum2 : ∑ sd : K, ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd,x)))
          = 2 * (∑ sd : K, ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r)))
            - Fintype.card K := by
        rw [Finset.mul_sum,
          show (Fintype.card K : ℝ) = ∑ _sd : K, (1:ℝ) from by
            rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one],
          ← Finset.sum_sub_distrib]
        apply Finset.sum_congr rfl
        intro sd _
        ring
      have hCcardK : (Fintype.card K : ℝ)⁻¹ * (Fintype.card K : ℝ) = 1 := inv_mul_cancel₀ hKne
      calc 2 * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r))) - 1
          = (Fintype.card K : ℝ)⁻¹ *
              (2 * ∑ sd : K, ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r)))
            - (Fintype.card K : ℝ)⁻¹ * (Fintype.card K : ℝ) := by rw [hCcardK]; ring
        _ = (Fintype.card K : ℝ)⁻¹ *
              (2 * ∑ sd : K, ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r))
                - Fintype.card K) := by ring
        _ = (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd,x))) := by
            rw [hsum2]
    have hsp : ∀ x : D, sourceProb S H x z = margZ S H z * condX S H z x := by
      intro x
      by_cases hz : margZ S H z = 0
      · have hnn : ∀ y ∈ (Finset.univ : Finset D), 0 ≤ sourceProb S H y z :=
          fun y _ => ENNReal.toReal_nonneg
        have hsum0 : ∑ y : D, sourceProb S H y z = 0 := hz
        have hx0 := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hsum0 x (Finset.mem_univ x)
        rw [hx0, hz, zero_mul]
      · rw [condX, mul_div_cancel₀ _ hz]
    have hgroup : ∀ (sd : K) (f : D → ℝ) (g : R → ℝ),
        ∑ x : D, f x * g (H (sd, x)) = ∑ r : R, g r * rowDistOf K D R H f sd r := by
      intro sd f g
      simp only [rowDistOf, Finset.mul_sum]
      simp_rw [mul_ite, mul_zero]
      rw [Finset.sum_comm]
      refine Finset.sum_congr rfl (fun x _ => ?_)
      rw [Finset.sum_ite_eq Finset.univ (H (sd, x)) (fun r => g r * f x)]
      simp [mul_comm]
    have hrow_scalar : ∀ (sd : K) (r : R),
        rowDistOf K D R H (fun x => sourceProb S H x z) sd r
          = margZ S H z * rowDistOf K D R H (condX S H z) sd r := by
      intro sd r
      unfold rowDistOf
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro x _
      by_cases hc : H (sd, x) = r
      · rw [if_pos hc, if_pos hc]; exact hsp x
      · rw [if_neg hc, if_neg hc, mul_zero]
    rcases (margZ_nonneg' H z).lt_or_eq with hpos | hz0
    · have hpersd : ∀ sd : K, ∑ x : D, sourceProb S H x z *
          ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd, x)))
          = margZ S H z * ∑ r : R, α sd r * ((Fintype.card R : ℝ)⁻¹ - rowDistOf K D R H (condX S H z) sd r) := by
        intro sd
        have e1 : ∀ x : D, sourceProb S H x z *
            ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd, x)))
            = (Fintype.card R : ℝ)⁻¹ * (∑ r : R, α sd r) * sourceProb S H x z
              - sourceProb S H x z * α sd (H (sd, x)) := by
          intro x; ring
        simp_rw [e1]
        rw [Finset.sum_sub_distrib, ← Finset.mul_sum,
          show (∑ i : D, sourceProb S H i z) = margZ S H z from rfl]
        rw [hgroup sd (fun x => sourceProb S H x z) (α sd)]
        simp_rw [hrow_scalar]
        have e1b : ∀ r : R, α sd r * (margZ S H z * rowDistOf K D R H (condX S H z) sd r)
            = margZ S H z * (α sd r * rowDistOf K D R H (condX S H z) sd r) := fun r => by ring
        simp_rw [e1b]
        rw [← Finset.mul_sum]
        have e2 : (Fintype.card R : ℝ)⁻¹ * (∑ r : R, α sd r) * margZ S H z
            - margZ S H z * ∑ r : R, α sd r * rowDistOf K D R H (condX S H z) sd r
            = margZ S H z * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r
                - ∑ r : R, α sd r * rowDistOf K D R H (condX S H z) sd r) := by ring
        rw [e2]
        congr 1
        rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
        apply Finset.sum_congr rfl
        intro r _
        ring
      have hcombine : ∑ x : D, sourceProb S H x z *
          (2 * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r))) - 1)
          = margZ S H z * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ∑ r : R,
              α sd r * ((Fintype.card R : ℝ)⁻¹ - rowDistOf K D R H (condX S H z) sd r)) := by
        have step1 : ∀ x : D, sourceProb S H x z *
            (2 * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
              ((1/2) * (1 - α sd (H (sd,x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r))) - 1)
            = (Fintype.card K : ℝ)⁻¹ * (sourceProb S H x z *
                ∑ sd : K, ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd,x)))) :=
          fun x => by rw [hQ_eq x]; ring
        simp_rw [step1]
        rw [← Finset.mul_sum,
          show margZ S H z * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ∑ r : R,
                α sd r * ((Fintype.card R : ℝ)⁻¹ - rowDistOf K D R H (condX S H z) sd r))
              = (Fintype.card K : ℝ)⁻¹ * (margZ S H z * ∑ sd : K, ∑ r : R,
                α sd r * ((Fintype.card R : ℝ)⁻¹ - rowDistOf K D R H (condX S H z) sd r)) from by ring]
        congr 1
        have step2 : ∀ x : D, sourceProb S H x z *
            ∑ sd : K, ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd,x)))
            = ∑ sd : K, sourceProb S H x z * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r - α sd (H (sd,x))) :=
          fun x => Finset.mul_sum _ _ _
        simp_rw [step2]
        rw [Finset.sum_comm]
        simp_rw [hpersd]
        rw [← Finset.mul_sum]
      rw [hcombine]
      have hfs := fact_sd (fun p : K × R => (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2)
        (fun p : K × R => (Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹) (fun p : K × R => α p.1 p.2)
        (fun p => hα0 p.1 p.2) (fun p => hα1 p.1 p.2) ?_
      · apply mul_le_mul_of_nonneg_left _ hpos.le
        calc (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ∑ r : R,
              α sd r * ((Fintype.card R : ℝ)⁻¹ - rowDistOf K D R H (condX S H z) sd r)
            = ∑ p : K × R, α p.1 p.2 *
                ((Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹
                  - (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2) := by
              have hnested : ∑ sd : K, ∑ r : R,
                  α sd r * ((Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹
                    - (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) sd r)
                  = (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ∑ r : R,
                      α sd r * ((Fintype.card R : ℝ)⁻¹ - rowDistOf K D R H (condX S H z) sd r) := by
                simp_rw [Finset.mul_sum]
                exact Finset.sum_congr rfl (fun sd _ => Finset.sum_congr rfl (fun r _ => by ring))
              rw [← hnested,
                Fintype.sum_prod_type (f := fun p : K × R => α p.1 p.2 *
                  ((Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹
                    - (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2))]
          _ ≤ SD (fun p : K × R => (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2)
                (fun p : K × R => (Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹) := hfs
          _ = DeltaHz S H z := by
              simp only [SD, DeltaHz, DeltaOf]
              have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
              have hKpos : (0:ℝ) ≤ (Fintype.card K:ℝ)⁻¹ := by positivity
              have e1 : ∀ p : K × R,
                  |(Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2
                    - (Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹|
                  = (Fintype.card K : ℝ)⁻¹ * |rowDistOf K D R H (condX S H z) p.1 p.2 - unifR R p.2| := by
                intro p
                unfold unifR
                rw [← mul_sub, abs_mul, abs_of_nonneg hKpos]
              simp_rw [e1]
              have hLHS : (1/2 : ℝ) * ∑ p : K × R,
                  (Fintype.card K : ℝ)⁻¹ * |rowDistOf K D R H (condX S H z) p.1 p.2 - unifR R p.2|
                  = (1/2 : ℝ) * (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ∑ r : R,
                      |rowDistOf K D R H (condX S H z) sd r - unifR R r| := by
                rw [Fintype.sum_prod_type (f := fun p : K × R =>
                  (Fintype.card K : ℝ)⁻¹ * |rowDistOf K D R H (condX S H z) p.1 p.2 - unifR R p.2|)]
                simp_rw [← Finset.mul_sum]
                ring
              have hRHS : (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, (1/2 : ℝ) * ∑ r : R,
                  |rowDistOf K D R H (condX S H z) sd r - unifR R r|
                  = (1/2 : ℝ) * (Fintype.card K : ℝ)⁻¹ * ∑ sd : K, ∑ r : R,
                      |rowDistOf K D R H (condX S H z) sd r - unifR R r| := by
                rw [← Finset.mul_sum]; ring
              rw [hLHS, hRHS]
      · have hcx1 : ∑ x : D, condX S H z x = 1 := by
          unfold condX
          rw [← Finset.sum_div]
          exact div_self hpos.ne'
        have hP1sum : ∑ p : K × R, (Fintype.card K : ℝ)⁻¹ * (Fintype.card R : ℝ)⁻¹ = 1 := by
          rw [Finset.sum_const, Finset.card_univ, Fintype.card_prod, nsmul_eq_mul]
          have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
          have hRne : (Fintype.card R : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
          push_cast
          field_simp
        have hP0sum : ∑ p : K × R, (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2 = 1 := by
          rw [Fintype.sum_prod_type (f := fun p : K × R =>
            (Fintype.card K : ℝ)⁻¹ * rowDistOf K D R H (condX S H z) p.1 p.2)]
          simp_rw [← Finset.mul_sum]
          have : ∀ sd : K, ∑ r : R, rowDistOf K D R H (condX S H z) sd r = 1 := by
            intro sd; rw [rowDistOf_sum_eq']; exact hcx1
          simp_rw [this]
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
          exact inv_mul_cancel₀ (by exact_mod_cast Fintype.card_ne_zero : (Fintype.card K:ℝ) ≠ 0)
        rw [hP0sum, hP1sum]
    · have hall0 : ∀ x : D, sourceProb S H x z = 0 := by
        intro x
        rw [hsp x, ← hz0, zero_mul]
      have hLHS0 : ∑ x : D, sourceProb S H x z *
          (2 * ((Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - α sd (H (sd, x))) + (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, α sd r))) - 1) = 0 := by
        apply Finset.sum_eq_zero
        intro x _
        rw [hall0 x, zero_mul]
      rw [hLHS0, ← hz0, zero_mul]
  -- ===== Phase 4: summability, and assembling the mean bound =====
  have tsum_sum_comm : ∀ {M : Type} [AddCommMonoid M] [TopologicalSpace M] [T2Space M]
      [ContinuousAdd M] (s : Finset D) (f : D → Aux → M), (∀ i ∈ s, Summable (f i)) →
      ∑' z, ∑ i ∈ s, f i z = ∑ i ∈ s, ∑' z, f i z := by
    intro M _ _ _ _ s f hf
    induction s using Finset.cons_induction with
    | empty => simp
    | cons a s ha ih =>
      simp_rw [Finset.sum_cons]
      have hfa : Summable (f a) := hf a (Finset.mem_cons_self a s)
      have hfs : Summable (fun z => ∑ i ∈ s, f i z) := by
        apply summable_sum
        intro i hi
        exact hf i (Finset.mem_cons.mpr (Or.inr hi))
      rw [hfa.tsum_add hfs, ih (fun i hi => hf i (Finset.mem_cons.mpr (Or.inr hi)))]
  have margZ_tsum1 : ∀ H : Table K D R, ∑' z : Aux, margZ S H z = 1 := by
    intro H
    have h1 : ∑' p : D × Aux, S H p = 1 := PMF.tsum_coe (S H)
    have h2 : ∑' p : D × Aux, S H p = ∑' x : D, ∑' z : Aux, S H (x, z) := ENNReal.tsum_prod'
    have h3 : ∑' x : D, ∑' z : Aux, S H (x, z) = ∑ x : D, ∑' z : Aux, S H (x, z) := tsum_fintype _
    have h4 : (∑ x : D, ∑' z : Aux, S H (x, z)) = 1 := by rw [← h3, ← h2, h1]
    have h5 : ∀ x : D, ∑' z : Aux, S H (x, z) ≠ ⊤ := by
      intro x
      have hle : ∑' z : Aux, S H (x, z) ≤ ∑' p : D × Aux, S H p := by
        apply ENNReal.tsum_comp_le_tsum_of_injective (f := fun z => (x, z))
        intro a b hab
        exact (Prod.mk.injEq .. ▸ hab).2
      rw [h1] at hle
      exact ne_top_of_le_ne_top ENNReal.one_ne_top hle
    have h6 : (∑ x : D, ∑' z : Aux, S H (x, z)).toReal = 1 := by rw [h4]; simp
    rw [ENNReal.toReal_sum (fun x _ => h5 x)] at h6
    have h7 : ∀ x : D, (∑' z : Aux, S H (x, z)).toReal = ∑' z : Aux, (S H (x, z)).toReal := by
      intro x
      exact ENNReal.tsum_toReal_eq (fun z => (S H).apply_ne_top _)
    simp_rw [h7] at h6
    show ∑' z : Aux, ∑ x : D, sourceProb S H x z = 1
    rw [← h6]
    exact tsum_sum_comm Finset.univ (fun x z => (S H (x, z)).toReal)
      (fun x _ => ENNReal.summable_toReal (h5 x))
  have margZ_summable' : ∀ H : Table K D R, Summable (margZ S H) := by
    intro H
    by_contra hns
    have h1 := margZ_tsum1 H
    rw [tsum_eq_zero_of_not_summable hns] at h1
    norm_num at h1
  -- `DeltaHz ∈ [0,1]`, following the `Fdist_le_one` pattern with `condX` in place of `Tindicator`.
  have rowDistOf_nonneg' : ∀ (H : Table K D R) (p : D → ℝ), (∀ x, 0 ≤ p x) →
      ∀ (k : K) (r : R), 0 ≤ rowDistOf K D R H p k r := by
    intro H p hp0 k r
    unfold rowDistOf
    apply Finset.sum_nonneg
    intro x _
    split
    · exact hp0 x
    · exact le_refl 0
  have abs_sub_le_add' : ∀ x y : ℝ, 0 ≤ x → 0 ≤ y → |x - y| ≤ x + y := by
    intro x y hx hy; rw [abs_le]; constructor <;> linarith
  have SD_le_one' : ∀ {α : Type} [Fintype α] (f g : α → ℝ), (∀ a, 0 ≤ f a) → (∀ a, 0 ≤ g a) →
      (∑ a, f a ≤ 1) → (∑ a, g a ≤ 1) → SD f g ≤ 1 := by
    intro α _ f g hf0 hg0 hf1 hg1
    unfold SD
    have hpt : ∀ a, |f a - g a| ≤ f a + g a := fun a => abs_sub_le_add' _ _ (hf0 a) (hg0 a)
    calc (1/2 : ℝ) * ∑ a, |f a - g a| ≤ (1/2) * ∑ a, (f a + g a) :=
          mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun a _ => hpt a)) (by norm_num)
      _ = (1/2) * (∑ a, f a + ∑ a, g a) := by rw [Finset.sum_add_distrib]
      _ ≤ (1/2) * (1 + 1) := by linarith
      _ = 1 := by norm_num
  have hDeltaHz_le1 : ∀ (H : Table K D R) (z : Aux), DeltaHz S H z ≤ 1 := by
    intro H z
    unfold DeltaHz DeltaOf
    have hcx0 : ∀ x, 0 ≤ condX S H z x := fun x => div_nonneg ENNReal.toReal_nonneg (margZ_nonneg' H z)
    have hcx1_le : ∑ x, condX S H z x ≤ 1 := by
      rcases (margZ_nonneg' H z).lt_or_eq with hp | h0
      · have heq : ∑ x, condX S H z x = 1 := by
          unfold condX; rw [← Finset.sum_div]; exact div_self hp.ne'
        linarith
      · have heq0 : ∀ x, condX S H z x = 0 := fun x => by unfold condX; rw [← h0, div_zero]
        rw [Finset.sum_congr rfl (fun x _ => heq0 x)]
        simp
    have hbound : ∀ k : K, SD (rowDistOf K D R H (condX S H z) k) (unifR R) ≤ 1 := by
      intro k
      apply SD_le_one'
      · exact rowDistOf_nonneg' H (condX S H z) hcx0 k
      · intro r; unfold unifR; positivity
      · rw [rowDistOf_sum_eq']; exact hcx1_le
      · unfold unifR
        rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
        have hRpos : 0 < Fintype.card R := Fintype.card_pos
        have hRne : (Fintype.card R : ℝ) ≠ 0 := by exact_mod_cast hRpos.ne'
        rw [mul_inv_cancel₀ hRne]
    have hKpos : 0 < Fintype.card K := Fintype.card_pos
    have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast hKpos.ne'
    calc (Fintype.card K : ℝ)⁻¹ * ∑ k : K, SD (rowDistOf K D R H (condX S H z) k) (unifR R)
        ≤ (Fintype.card K : ℝ)⁻¹ * ∑ _k : K, (1:ℝ) := by
          apply mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun k _ => hbound k)); positivity
      _ = (Fintype.card K : ℝ)⁻¹ * (Fintype.card K : ℝ) := by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
      _ = 1 := inv_mul_cancel₀ hKne
  have hDeltaHz_nonneg : ∀ (H : Table K D R) (z : Aux), 0 ≤ DeltaHz S H z := by
    intro H z
    unfold DeltaHz DeltaOf
    apply mul_nonneg (by positivity)
    apply Finset.sum_nonneg
    intro k _
    unfold SD
    apply mul_nonneg (by norm_num)
    apply Finset.sum_nonneg
    intro a _
    exact abs_nonneg _
  -- `Q(H,x,z) ∈ [0,1]`: an average (over `sd`) of averages of `[0,1]`-valued things.
  have hQbound : ∀ (H : Table K D R) (x : D) (z : Aux),
      0 ≤ (Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
             (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal))
      ∧ (Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - (Dist H sd (H (sd, x)) z true).toReal) +
             (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal)) ≤ 1 := by
    intro H x z
    have hα0 : ∀ sd r, 0 ≤ (Dist H sd r z true).toReal := fun sd r => ENNReal.toReal_nonneg
    have hα1 : ∀ sd r, (Dist H sd r z true).toReal ≤ 1 := fun sd r => by
      have := ENNReal.toReal_mono ENNReal.one_ne_top (PMF.coe_le_one (Dist H sd r z) true)
      rwa [ENNReal.toReal_one] at this
    have hRavg_nonneg : ∀ sd : K, 0 ≤ (Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal :=
      fun sd => mul_nonneg (by positivity) (Finset.sum_nonneg (fun r _ => hα0 sd r))
    have hRavg_le1 : ∀ sd : K, (Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal ≤ 1 := by
      intro sd
      have h1 : ∑ r : R, (Dist H sd r z true).toReal ≤ ∑ _r : R, (1:ℝ) :=
        Finset.sum_le_sum (fun r _ => hα1 sd r)
      rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one] at h1
      have hRpos : 0 < Fintype.card R := Fintype.card_pos
      have hRne : (Fintype.card R : ℝ) ≠ 0 := by exact_mod_cast hRpos.ne'
      calc (Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal
          ≤ (Fintype.card R : ℝ)⁻¹ * (Fintype.card R : ℝ) :=
            mul_le_mul_of_nonneg_left h1 (by positivity)
        _ = 1 := inv_mul_cancel₀ hRne
    have hT_nonneg : ∀ sd : K, 0 ≤ (1/2) * (1 - (Dist H sd (H (sd,x)) z true).toReal) +
        (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal) := fun sd => by
      have h1 := hα1 sd (H (sd,x)); have h2 := hRavg_nonneg sd; linarith
    have hT_le1 : ∀ sd : K, (1/2) * (1 - (Dist H sd (H (sd,x)) z true).toReal) +
        (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal) ≤ 1 := fun sd => by
      have h1 := hα0 sd (H (sd,x)); have h2 := hRavg_le1 sd; linarith
    have hKpos : 0 < Fintype.card K := Fintype.card_pos
    have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast hKpos.ne'
    constructor
    · exact mul_nonneg (by positivity) (Finset.sum_nonneg (fun sd _ => hT_nonneg sd))
    · have h1 : ∑ sd : K, ((1/2) * (1 - (Dist H sd (H (sd,x)) z true).toReal) +
          (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal))
          ≤ ∑ _sd : K, (1:ℝ) := Finset.sum_le_sum (fun sd _ => hT_le1 sd)
      rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one] at h1
      calc (Fintype.card K : ℝ)⁻¹ * ∑ sd : K,
            ((1/2) * (1 - (Dist H sd (H (sd,x)) z true).toReal) +
             (1/2) * ((Fintype.card R : ℝ)⁻¹ * ∑ r : R, (Dist H sd r z true).toReal))
          ≤ (Fintype.card K : ℝ)⁻¹ * (Fintype.card K : ℝ) := mul_le_mul_of_nonneg_left h1 (by positivity)
        _ = 1 := inv_mul_cancel₀ hKne
  have hxsum_nonneg : ∀ (H : Table K D R) (z : Aux), 0 ≤ ∑ x : D, sourceProb S H x z *
      Qexpr H x z := fun H z =>
    Finset.sum_nonneg (fun x _ => mul_nonneg ENNReal.toReal_nonneg (hQbound H x z).1)
  have hxsum_le_margZ : ∀ (H : Table K D R) (z : Aux), (∑ x : D, sourceProb S H x z *
      Qexpr H x z) ≤ margZ S H z := by
    intro H z
    unfold margZ
    apply Finset.sum_le_sum
    intro x _
    calc sourceProb S H x z * Qexpr H x z
        ≤ sourceProb S H x z * 1 :=
          mul_le_mul_of_nonneg_left (hQbound H x z).2 ENNReal.toReal_nonneg
      _ = sourceProb S H x z := mul_one _
  have hxsum_summable : ∀ H : Table K D R, Summable (fun z => ∑ x : D, sourceProb S H x z *
      Qexpr H x z) := fun H =>
    Summable.of_nonneg_of_le (hxsum_nonneg H) (hxsum_le_margZ H) (margZ_summable' H)
  have hf2_nonneg : ∀ (H : Table K D R) (z : Aux), 0 ≤ margZ S H z * DeltaHz S H z := fun H z =>
    mul_nonneg (margZ_nonneg' H z) (hDeltaHz_nonneg H z)
  have hf2_le_margZ : ∀ (H : Table K D R) (z : Aux), margZ S H z * DeltaHz S H z ≤ margZ S H z := by
    intro H z
    calc margZ S H z * DeltaHz S H z ≤ margZ S H z * 1 :=
          mul_le_mul_of_nonneg_left (hDeltaHz_le1 H z) (margZ_nonneg' H z)
      _ = margZ S H z := mul_one _
  have hf2_summable : ∀ H : Table K D R, Summable (fun z => margZ S H z * DeltaHz S H z) := fun H =>
    Summable.of_nonneg_of_le (hf2_nonneg H) (hf2_le_margZ H) (margZ_summable' H)
  have hpointwise : ∀ (H : Table K D R) (z : Aux),
      2 * (∑ x : D, sourceProb S H x z *
        Qexpr H x z) - margZ S H z
        ≤ margZ S H z * DeltaHz S H z := by
    intro H z
    have heq : 2 * (∑ x : D, sourceProb S H x z *
        Qexpr H x z) - margZ S H z
        = ∑ x : D, sourceProb S H x z *
            (2 * Qexpr H x z - 1) := by
      unfold margZ
      rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro x _
      ring
    rw [heq]
    exact crux_bound H z
  have htsum_le : ∀ H : Table K D R, ∑' z : Aux, (2 * (∑ x : D, sourceProb S H x z *
        Qexpr H x z) - margZ S H z)
      ≤ ∑' z : Aux, margZ S H z * DeltaHz S H z := fun H =>
    Summable.tsum_le_tsum (hpointwise H)
      ((Summable.mul_left 2 (hxsum_summable H)).sub (margZ_summable' H)) (hf2_summable H)
  have hsplit_tsum : ∀ H : Table K D R, ∑' z : Aux, (2 * (∑ x : D, sourceProb S H x z *
        Qexpr H x z) - margZ S H z)
      = 2 * (∑' z : Aux, ∑ x : D, sourceProb S H x z *
          Qexpr H x z) - 1 := by
    intro H
    rw [Summable.tsum_sub (Summable.mul_left 2 (hxsum_summable H)) (margZ_summable' H),
      tsum_mul_left, margZ_tsum1 H]
  have hHbound : ∀ H : Table K D R, 2 * (∑' z : Aux, ∑ x : D, sourceProb S H x z *
      Qexpr H x z) - 1
      ≤ ∑' z : Aux, margZ S H z * DeltaHz S H z := by
    intro H
    rw [← hsplit_tsum H]
    exact htsum_le H
  unfold extPubAdv expectHZ
  rw [hval2]
  have hTable_ne0 : (Fintype.card (Table K D R) : ℝ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  have htelescope : (2:ℝ) * ((Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, ∑' z : Aux,
      ∑ x : D, sourceProb S H x z *
        Qexpr H x z) - 1
      = (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R,
          (2 * (∑' z : Aux, ∑ x : D, sourceProb S H x z *
            Qexpr H x z) - 1) := by
    have hsum2 : ∑ H : Table K D R, (2 * (∑' z : Aux, ∑ x : D, sourceProb S H x z *
          Qexpr H x z) - 1)
        = 2 * (∑ H : Table K D R, ∑' z : Aux, ∑ x : D, sourceProb S H x z *
            Qexpr H x z)
          - Fintype.card (Table K D R) := by
      rw [Finset.mul_sum,
        show (Fintype.card (Table K D R) : ℝ) = ∑ _H : Table K D R, (1:ℝ) from by
          rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one],
        ← Finset.sum_sub_distrib]
    have hcancel : (Fintype.card (Table K D R) : ℝ)⁻¹ * (Fintype.card (Table K D R) : ℝ) = 1 :=
      inv_mul_cancel₀ hTable_ne0
    calc (2:ℝ) * ((Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, ∑' z : Aux,
          ∑ x : D, sourceProb S H x z *
            Qexpr H x z) - 1
        = (Fintype.card (Table K D R) : ℝ)⁻¹ *
            (2 * ∑ H : Table K D R, ∑' z : Aux, ∑ x : D, sourceProb S H x z *
              Qexpr H x z)
          - (Fintype.card (Table K D R) : ℝ)⁻¹ * (Fintype.card (Table K D R) : ℝ) := by
          rw [hcancel]; ring
      _ = (Fintype.card (Table K D R) : ℝ)⁻¹ *
            (2 * ∑ H : Table K D R, ∑' z : Aux, ∑ x : D, sourceProb S H x z *
              Qexpr H x z
              - Fintype.card (Table K D R)) := by ring
      _ = (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R,
            (2 * (∑' z : Aux, ∑ x : D, sourceProb S H x z *
              Qexpr H x z) - 1) := by
          rw [hsum2]
  rw [htelescope]
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  apply Finset.sum_le_sum
  intro H _
  exact hHbound H

/-- Consequence used in `Assemble`: unpredictability bounds the mean deficiency. -/
theorem expectHZ_epsHz_le {ε : ℝ} (hU : IsUnpredictable S ε) :
    expectHZ S (epsHz S) ≤ ε := by
  rw [← predAdv_Pmode_eq]; exact hU (Pmode S)

end Analytic

section Flat

/-- Two-point mass perturbation of a weight function `f`: the sum is unchanged up to the net
shift `c + d`. A single reusable computation for both perturbation directions used in
`hypersimplex_decomp`. -/
private theorem sum_perturb_two {ι : Type} [Fintype ι] [DecidableEq ι]
    (f : ι → ℝ) (x y : ι) (hxy : x ≠ y) (c d : ℝ) :
    ∑ z, (if z = y then f y + c else if z = x then f x + d else f z)
      = (∑ z, f z) + c + d := by
  have hpt : ∀ z, (if z = y then f y + c else if z = x then f x + d else f z)
      = f z + ((if z = y then c else 0) + (if z = x then d else 0)) := by
    intro z
    rcases eq_or_ne z y with hzy | hzy
    · simp [hzy, Ne.symm hxy]
    · rcases eq_or_ne z x with hzx | hzx
      · simp [hzx, hxy]
      · simp [hzy, hzx]
  simp_rw [hpt]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
  have h1 : ∑ z : ι, (if z = y then c else (0 : ℝ)) = c := by simp
  have h2 : ∑ z : ι, (if z = x then d else (0 : ℝ)) = d := by simp
  rw [h1, h2]
  ring

/-- Combining two hypersimplex decompositions (for the same `t`) of `p1` and `p2` into one for a
convex combination `p = w1 • p1 + w2 • p2`, by concatenating the index types via `Fin.append`.
The "convex combination of two already-decomposed points" step of the induction, as its own
piece. -/
private theorem combine_two_decomp {t : ℕ} {p p1 p2 : D → ℝ} {w1 w2 : ℝ}
    (hw1 : 0 ≤ w1) (hw2 : 0 ≤ w2) (hw : w1 + w2 = 1) (hp : ∀ x, p x = w1 * p1 x + w2 * p2 x)
    (h1 : ∃ (n : ℕ) (α : Fin n → ℝ) (T : Fin n → Finset D),
      (∀ i, 0 ≤ α i) ∧ (∑ i, α i = 1) ∧ (∀ i, (T i).card = t) ∧
        (∀ x, p1 x = ∑ i, α i * Tindicator D (T i) x))
    (h2 : ∃ (n : ℕ) (α : Fin n → ℝ) (T : Fin n → Finset D),
      (∀ i, 0 ≤ α i) ∧ (∑ i, α i = 1) ∧ (∀ i, (T i).card = t) ∧
        (∀ x, p2 x = ∑ i, α i * Tindicator D (T i) x)) :
    ∃ (n : ℕ) (α : Fin n → ℝ) (T : Fin n → Finset D),
      (∀ i, 0 ≤ α i) ∧ (∑ i, α i = 1) ∧ (∀ i, (T i).card = t) ∧
        (∀ x, p x = ∑ i, α i * Tindicator D (T i) x) := by
  obtain ⟨n1, α1, T1, hα10, hα11, hT1, hp1eq⟩ := h1
  obtain ⟨n2, α2, T2, hα20, hα21, hT2, hp2eq⟩ := h2
  refine ⟨n1 + n2, Fin.append (fun i => w1 * α1 i) (fun i => w2 * α2 i), Fin.append T1 T2,
    ?_, ?_, ?_, ?_⟩
  · refine Fin.addCases (fun j => ?_) (fun j => ?_)
    · rw [Fin.append_left]; exact mul_nonneg hw1 (hα10 j)
    · rw [Fin.append_right]; exact mul_nonneg hw2 (hα20 j)
  · rw [Fin.sum_univ_add]
    simp only [Fin.append_left, Fin.append_right]
    rw [← Finset.mul_sum, ← Finset.mul_sum, hα11, hα21, mul_one, mul_one]
    exact hw
  · refine Fin.addCases (fun j => ?_) (fun j => ?_)
    · rw [Fin.append_left]; exact hT1 j
    · rw [Fin.append_right]; exact hT2 j
  · intro x
    rw [hp x, hp1eq x, hp2eq x, Finset.mul_sum, Finset.mul_sum, Fin.sum_univ_add]
    simp only [Fin.append_left, Fin.append_right]
    congr 1
    · exact Finset.sum_congr rfl (fun i _ => by ring)
    · exact Finset.sum_congr rfl (fun i _ => by ring)

/-- Auxiliary form of `hypersimplex_decomp`, generalized to strong induction on the number `m` of
"fractional" coordinates (strictly between `0` and `1/t`). -/
private theorem hypersimplex_decomp_aux (t : ℕ) (ht1 : 1 ≤ t) (_htD : t ≤ Fintype.card D) :
    ∀ (m : ℕ) (p : D → ℝ),
      (Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹)).card = m →
      (∀ x, 0 ≤ p x) → (∑ x, p x = 1) → (∀ x, p x ≤ (t : ℝ)⁻¹) →
      ∃ (n : ℕ) (α : Fin n → ℝ) (T : Fin n → Finset D),
        (∀ i, 0 ≤ α i) ∧ (∑ i, α i = 1) ∧ (∀ i, (T i).card = t) ∧
          (∀ x, p x = ∑ i, α i * Tindicator D (T i) x) := by
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    intro p hm hp0 hp1 hpcap
    by_cases hzero : m = 0
    · -- Base case: no fractional coordinates, so `p` is already a single `t`-indicator.
      subst hzero
      rw [Finset.card_eq_zero] at hm
      have hzo : ∀ x, p x = 0 ∨ p x = (t : ℝ)⁻¹ := by
        intro x
        by_contra hc
        push_neg at hc
        have hmem : x ∈ Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹) :=
          Finset.mem_filter.mpr ⟨Finset.mem_univ x, hc.1, hc.2⟩
        rw [hm] at hmem
        simp at hmem
      set T0 : Finset D := Finset.univ.filter (fun x => p x ≠ 0) with hT0def
      have hAval : ∀ x ∈ T0, p x = (t : ℝ)⁻¹ := by
        intro x hx
        rw [hT0def, Finset.mem_filter] at hx
        rcases hzo x with h0 | hinv
        · exact absurd h0 hx.2
        · exact hinv
      have hBval : ∀ x ∉ T0, p x = 0 := by
        intro x hx
        rw [hT0def, Finset.mem_filter] at hx
        push_neg at hx
        exact hx (Finset.mem_univ x)
      have hsum_eq : ∑ x ∈ T0, p x + ∑ x ∈ T0ᶜ, p x = 1 := by
        rw [Finset.sum_add_sum_compl]; exact hp1
      have hrest0 : ∑ x ∈ T0ᶜ, p x = 0 :=
        Finset.sum_eq_zero (fun x hx => hBval x (Finset.mem_compl.mp hx))
      have hTcardsum : ∑ x ∈ T0, p x = (T0.card : ℝ) * (t : ℝ)⁻¹ := by
        rw [Finset.sum_congr rfl hAval, Finset.sum_const, nsmul_eq_mul]
      rw [hTcardsum, hrest0, add_zero] at hsum_eq
      have ht0 : 0 < t := by omega
      have htpos : (0 : ℝ) < (t : ℝ) := by exact_mod_cast ht0
      have hcardt : (T0.card : ℝ) = (t : ℝ) := by
        have h1 : (T0.card : ℝ) * (t : ℝ)⁻¹ * (t : ℝ) = 1 * (t : ℝ) := by rw [hsum_eq]
        rw [mul_assoc, inv_mul_cancel₀ (ne_of_gt htpos), mul_one, one_mul] at h1
        exact h1
      have hcardteq : T0.card = t := by exact_mod_cast hcardt
      refine ⟨1, fun _ => 1, fun _ => T0, fun _ => zero_le_one, by simp, fun _ => hcardteq, ?_⟩
      intro x
      simp only [Fin.sum_univ_one, one_mul, Tindicator]
      rw [hcardteq]
      by_cases hx : x ∈ T0
      · rw [if_pos hx]; exact hAval x hx
      · rw [if_neg hx]; exact hBval x hx
    · -- Inductive step: at least two fractional coordinates; perturb and recurse.
      have hFcard : (Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹)).card = m := hm
      have hne : (Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹)).Nonempty := by
        rw [← Finset.card_pos, hFcard]; omega
      have h2card : 1 < (Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹)).card := by
        rcases hne with ⟨x0, hx0⟩
        rw [Finset.mem_filter] at hx0
        obtain ⟨-, hx0ne0, hx0neinv⟩ := hx0
        by_contra hcon
        push_neg at hcon
        have hcard1 : (Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹)).card = 1 :=
          le_antisymm hcon
            (Finset.card_pos.mpr
              ⟨x0, Finset.mem_filter.mpr ⟨Finset.mem_univ x0, hx0ne0, hx0neinv⟩⟩)
        obtain ⟨x1, hx1⟩ := Finset.card_eq_one.mp hcard1
        have hx0eq : x0 = x1 := Finset.mem_singleton.mp
          (hx1 ▸ Finset.mem_filter.mpr ⟨Finset.mem_univ x0, hx0ne0, hx0neinv⟩)
        have hset : Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹) = {x0} := by
          rw [hx0eq]; exact hx1
        have hy : ∀ y : D, y ≠ x0 → p y = 0 ∨ p y = (t : ℝ)⁻¹ := by
          intro y hyx0
          by_contra hcy
          push_neg at hcy
          have hmemy : y ∈ Finset.univ.filter (fun x => p x ≠ 0 ∧ p x ≠ (t : ℝ)⁻¹) :=
            Finset.mem_filter.mpr ⟨Finset.mem_univ y, hcy.1, hcy.2⟩
          rw [hset] at hmemy
          exact hyx0 (Finset.mem_singleton.mp hmemy)
        set S : Finset D := Finset.univ.filter (fun y => p y = (t : ℝ)⁻¹) with hSdef
        have hx0S : x0 ∉ S := by
          rw [hSdef, Finset.mem_filter]
          exact fun h => hx0neinv h.2
        have hSsub : S ⊆ Finset.univ.erase x0 := by
          intro y hyS
          rw [Finset.mem_erase]
          exact ⟨fun hyx0 => hx0S (hyx0 ▸ hyS), Finset.mem_univ y⟩
        have hrest0 : ∀ y ∈ Finset.univ.erase x0, y ∉ S → p y = 0 := by
          intro y hy' hyS
          rw [Finset.mem_erase] at hy'
          rcases hy y hy'.1 with h0 | hinv
          · exact h0
          · exact absurd (Finset.mem_filter.mpr ⟨Finset.mem_univ y, hinv⟩) hyS
        have herase : ∑ y ∈ S, p y = ∑ y ∈ Finset.univ.erase x0, p y :=
          Finset.sum_subset hSsub hrest0
        have hSsum : ∑ y ∈ S, p y = (S.card : ℝ) * (t : ℝ)⁻¹ := by
          rw [Finset.sum_congr rfl (fun y hyS => (Finset.mem_filter.mp hyS).2), Finset.sum_const,
            nsmul_eq_mul]
        have hsplit : p x0 + ∑ y ∈ Finset.univ.erase x0, p y = ∑ y, p y :=
          Finset.add_sum_erase Finset.univ p (Finset.mem_univ x0)
        rw [← herase, hSsum, hp1] at hsplit
        have hpx0_pos : 0 < p x0 := lt_of_le_of_ne (hp0 x0) (Ne.symm hx0ne0)
        have hpx0_lt : p x0 < (t : ℝ)⁻¹ := lt_of_le_of_ne (hpcap x0) hx0neinv
        have ht0 : 0 < t := by omega
        have htpos : (0 : ℝ) < (t : ℝ) := by exact_mod_cast ht0
        have hc1 : p x0 * (t : ℝ) + (S.card : ℝ) = (t : ℝ) := by
          have h1 : (p x0 + (S.card : ℝ) * (t : ℝ)⁻¹) * (t : ℝ) = 1 * (t : ℝ) := by rw [hsplit]
          rw [add_mul, mul_assoc, inv_mul_cancel₀ (ne_of_gt htpos), mul_one, one_mul] at h1
          linarith [h1]
        have hlt1 : p x0 * (t : ℝ) < 1 := by
          have hstep := mul_lt_mul_of_pos_right hpx0_lt htpos
          rwa [inv_mul_cancel₀ (ne_of_gt htpos)] at hstep
        have hgt0 : 0 < p x0 * (t : ℝ) := mul_pos hpx0_pos htpos
        have hn1 : S.card < t := by
          have hh : (S.card : ℝ) < (t : ℝ) := by linarith [hc1, hgt0]
          exact_mod_cast hh
        have hn2 : t < S.card + 1 := by
          have hh : (t : ℝ) < (S.card : ℝ) + 1 := by linarith [hc1, hlt1]
          exact_mod_cast hh
        omega
      obtain ⟨x1, x2, hx1F, hx2F, hx1x2⟩ := Finset.one_lt_card_iff.mp h2card
      rw [Finset.mem_filter] at hx1F hx2F
      obtain ⟨-, hx1ne0, hx1neinv⟩ := hx1F
      obtain ⟨-, hx2ne0, hx2neinv⟩ := hx2F
      have hpx1_pos : 0 < p x1 := lt_of_le_of_ne (hp0 x1) (Ne.symm hx1ne0)
      have hpx1_lt : p x1 < (t : ℝ)⁻¹ := lt_of_le_of_ne (hpcap x1) hx1neinv
      have hpx2_pos : 0 < p x2 := lt_of_le_of_ne (hp0 x2) (Ne.symm hx2ne0)
      have hpx2_lt : p x2 < (t : ℝ)⁻¹ := lt_of_le_of_ne (hpcap x2) hx2neinv
      set δp : ℝ := min (p x1) ((t : ℝ)⁻¹ - p x2) with hδpdef
      set δm : ℝ := min ((t : ℝ)⁻¹ - p x1) (p x2) with hδmdef
      have hδp_pos : 0 < δp := lt_min hpx1_pos (by linarith [hpx2_lt])
      have hδm_pos : 0 < δm := lt_min (by linarith [hpx1_lt]) hpx2_pos
      have hδp_le1 : δp ≤ p x1 := min_le_left _ _
      have hδp_le2 : δp ≤ (t : ℝ)⁻¹ - p x2 := min_le_right _ _
      have hδm_le1 : δm ≤ (t : ℝ)⁻¹ - p x1 := min_le_left _ _
      have hδm_le2 : δm ≤ p x2 := min_le_right _ _
      -- `pp`, `pm` shift mass `δp`/`δm` between `x1` and `x2` in opposite directions.
      set pp : D → ℝ := fun z => if z = x2 then p x2 + δp else if z = x1 then p x1 + (-δp) else p z
        with hppdef
      set pm : D → ℝ := fun z => if z = x2 then p x2 + (-δm) else if z = x1 then p x1 + δm else p z
        with hpmdef
      have hpp_x2 : pp x2 = p x2 + δp := by simp [hppdef]
      have hpp_x1 : pp x1 = p x1 + (-δp) := by simp [hppdef, hx1x2]
      have hpp_o : ∀ z, z ≠ x2 → z ≠ x1 → pp z = p z := by
        intro z hzx2 hzx1; simp [hppdef, hzx2, hzx1]
      have hpm_x2 : pm x2 = p x2 + (-δm) := by simp [hpmdef]
      have hpm_x1 : pm x1 = p x1 + δm := by simp [hpmdef, hx1x2]
      have hpm_o : ∀ z, z ≠ x2 → z ≠ x1 → pm z = p z := by
        intro z hzx2 hzx1; simp [hpmdef, hzx2, hzx1]
      have hpp0 : ∀ z, 0 ≤ pp z := by
        intro z
        by_cases hzx2 : z = x2
        · rw [hzx2, hpp_x2]; linarith [hpx2_pos]
        · by_cases hzx1 : z = x1
          · rw [hzx1, hpp_x1]; linarith [hδp_le1]
          · rw [hpp_o z hzx2 hzx1]; exact hp0 z
      have hppcap : ∀ z, pp z ≤ (t : ℝ)⁻¹ := by
        intro z
        by_cases hzx2 : z = x2
        · rw [hzx2, hpp_x2]; linarith [hδp_le2]
        · by_cases hzx1 : z = x1
          · rw [hzx1, hpp_x1]; linarith [hpx1_lt]
          · rw [hpp_o z hzx2 hzx1]; exact hpcap z
      have hpp1 : ∑ z, pp z = 1 := by
        simp only [hppdef]
        rw [sum_perturb_two p x1 x2 hx1x2 δp (-δp), hp1]
        ring
      have hpm0 : ∀ z, 0 ≤ pm z := by
        intro z
        by_cases hzx2 : z = x2
        · rw [hzx2, hpm_x2]; linarith [hδm_le2]
        · by_cases hzx1 : z = x1
          · rw [hzx1, hpm_x1]; linarith [hpx1_pos]
          · rw [hpm_o z hzx2 hzx1]; exact hp0 z
      have hpmcap : ∀ z, pm z ≤ (t : ℝ)⁻¹ := by
        intro z
        by_cases hzx2 : z = x2
        · rw [hzx2, hpm_x2]; linarith [hpx2_lt]
        · by_cases hzx1 : z = x1
          · rw [hzx1, hpm_x1]; linarith [hδm_le1]
          · rw [hpm_o z hzx2 hzx1]; exact hpcap z
      have hpm1 : ∑ z, pm z = 1 := by
        simp only [hpmdef]
        rw [sum_perturb_two p x1 x2 hx1x2 (-δm) δm, hp1]
        ring
      have hFpp_sub : (Finset.univ.filter (fun z => pp z ≠ 0 ∧ pp z ≠ (t : ℝ)⁻¹)) ⊆
          Finset.univ.filter (fun z => p z ≠ 0 ∧ p z ≠ (t : ℝ)⁻¹) := by
        intro z hz
        rw [Finset.mem_filter] at hz ⊢
        refine ⟨Finset.mem_univ z, ?_⟩
        by_cases hzx2 : z = x2
        · rw [hzx2]; exact ⟨hx2ne0, hx2neinv⟩
        · by_cases hzx1 : z = x1
          · rw [hzx1]; exact ⟨hx1ne0, hx1neinv⟩
          · rw [← hpp_o z hzx2 hzx1]; exact hz.2
      have hFpm_sub : (Finset.univ.filter (fun z => pm z ≠ 0 ∧ pm z ≠ (t : ℝ)⁻¹)) ⊆
          Finset.univ.filter (fun z => p z ≠ 0 ∧ p z ≠ (t : ℝ)⁻¹) := by
        intro z hz
        rw [Finset.mem_filter] at hz ⊢
        refine ⟨Finset.mem_univ z, ?_⟩
        by_cases hzx2 : z = x2
        · rw [hzx2]; exact ⟨hx2ne0, hx2neinv⟩
        · by_cases hzx1 : z = x1
          · rw [hzx1]; exact ⟨hx1ne0, hx1neinv⟩
          · rw [← hpm_o z hzx2 hzx1]; exact hz.2
      have hFpp_lt : (Finset.univ.filter (fun z => pp z ≠ 0 ∧ pp z ≠ (t : ℝ)⁻¹)).card < m := by
        rw [← hFcard]
        apply Finset.card_lt_card
        rw [Finset.ssubset_iff_of_subset hFpp_sub]
        rcases le_total (p x1) ((t : ℝ)⁻¹ - p x2) with hAB | hAB
        · have hval : pp x1 = 0 := by rw [hpp_x1, hδpdef, min_eq_left hAB]; ring
          refine ⟨x1, Finset.mem_filter.mpr ⟨Finset.mem_univ x1, hx1ne0, hx1neinv⟩, ?_⟩
          rw [Finset.mem_filter]
          rintro ⟨-, hne0, -⟩
          exact hne0 hval
        · have hval : pp x2 = (t : ℝ)⁻¹ := by rw [hpp_x2, hδpdef, min_eq_right hAB]; ring
          refine ⟨x2, Finset.mem_filter.mpr ⟨Finset.mem_univ x2, hx2ne0, hx2neinv⟩, ?_⟩
          rw [Finset.mem_filter]
          rintro ⟨-, -, hneinv⟩
          exact hneinv hval
      have hFpm_lt : (Finset.univ.filter (fun z => pm z ≠ 0 ∧ pm z ≠ (t : ℝ)⁻¹)).card < m := by
        rw [← hFcard]
        apply Finset.card_lt_card
        rw [Finset.ssubset_iff_of_subset hFpm_sub]
        rcases le_total ((t : ℝ)⁻¹ - p x1) (p x2) with hAB | hAB
        · have hval : pm x1 = (t : ℝ)⁻¹ := by rw [hpm_x1, hδmdef, min_eq_left hAB]; ring
          refine ⟨x1, Finset.mem_filter.mpr ⟨Finset.mem_univ x1, hx1ne0, hx1neinv⟩, ?_⟩
          rw [Finset.mem_filter]
          rintro ⟨-, -, hneinv⟩
          exact hneinv hval
        · have hval : pm x2 = 0 := by rw [hpm_x2, hδmdef, min_eq_right hAB]; ring
          refine ⟨x2, Finset.mem_filter.mpr ⟨Finset.mem_univ x2, hx2ne0, hx2neinv⟩, ?_⟩
          rw [Finset.mem_filter]
          rintro ⟨-, hne0, -⟩
          exact hne0 hval
      have hpp_decomp := ih _ hFpp_lt pp rfl hpp0 hpp1 hppcap
      have hpm_decomp := ih _ hFpm_lt pm rfl hpm0 hpm1 hpmcap
      have hδsum_pos : 0 < δp + δm := by linarith [hδp_pos, hδm_pos]
      have hcombine' : ∀ x, p x * (δp + δm) = δm * pp x + δp * pm x := by
        intro x
        by_cases hxc2 : x = x2
        · subst hxc2; rw [hpp_x2, hpm_x2]; ring
        · by_cases hxc1 : x = x1
          · subst hxc1; rw [hpp_x1, hpm_x1]; ring
          · rw [hpp_o x hxc2 hxc1, hpm_o x hxc2 hxc1]; ring
      have hcombine : ∀ x, p x = (δm / (δp + δm)) * pp x + (δp / (δp + δm)) * pm x := by
        intro x
        have h := hcombine' x
        have hne : δp + δm ≠ 0 := hδsum_pos.ne'
        field_simp
        linear_combination h
      exact combine_two_decomp (p1 := pp) (p2 := pm)
        (w1 := δm / (δp + δm)) (w2 := δp / (δp + δm))
        (div_nonneg hδm_pos.le hδsum_pos.le) (div_nonneg hδp_pos.le hδsum_pos.le)
        (by
          have heq1 : δm / (δp + δm) + δp / (δp + δm) = (δm + δp) / (δp + δm) := by ring
          rw [heq1, add_comm δm δp, div_self hδsum_pos.ne'])
        hcombine hpp_decomp hpm_decomp

/-- **Hypersimplex decomposition.** Every probability vector on `D` capped pointwise at `1/t`
(`t` a positive integer `≤ |D|`) is a convex combination of the uniform indicators of `t`-subsets.
Proved by strong induction on the number of fractional coordinates: while two coordinates are
strictly between `0` and `1/t`, shift mass between them until one saturates. Not one of
`resolution.tex`'s 7 cited "standard facts" (it's internal to `Lemma flat`'s own proof), but absent
from Mathlib too (`hypersimplex`/`permutohedron` get zero hits); Mathlib's `Birkhoff.lean` for
doubly-stochastic matrices is the nearest structural analogue but not directly reusable. -/
theorem hypersimplex_decomp (t : ℕ) (_ht1 : 1 ≤ t) (_htD : t ≤ Fintype.card D)
    (p : D → ℝ) (_hp0 : ∀ x, 0 ≤ p x) (_hp1 : ∑ x, p x = 1) (_hpcap : ∀ x, p x ≤ (t : ℝ)⁻¹) :
    ∃ (n : ℕ) (α : Fin n → ℝ) (T : Fin n → Finset D),
      (∀ i, 0 ≤ α i) ∧ (∑ i, α i = 1) ∧ (∀ i, (T i).card = t) ∧
        (∀ x, p x = ∑ i, α i * Tindicator D (T i) x) :=
  hypersimplex_decomp_aux t _ht1 _htD _ p rfl _hp0 _hp1 _hpcap

/-- `rowDistOf H (·) k r` is linear in its weight-function argument (it's a single sum swap). -/
private theorem rowDistOf_convex_combination (H : Table K D R) {n : ℕ} (α : Fin n → ℝ)
    (p : Fin n → D → ℝ) (k : K) (r : R) :
    rowDistOf K D R H (fun x => ∑ i, α i * p i x) k r
      = ∑ i, α i * rowDistOf K D R H (p i) k r := by
  simp only [rowDistOf, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun x _ => ?_)
  by_cases hc : H (k, x) = r <;> simp [hc]

/-- `SD (·, g)` is convex: a convex combination of weight functions has statistical distance to a
fixed `g` at most the same convex combination of the individual statistical distances. -/
private theorem SD_convex_combination {Ω : Type} [Fintype Ω] {n : ℕ} (w : Fin n → ℝ)
    (f : Fin n → Ω → ℝ) (g : Ω → ℝ) (hw0 : ∀ i, 0 ≤ w i) (hw1 : ∑ i, w i = 1) :
    SD (fun a => ∑ i, w i * f i a) g ≤ ∑ i, w i * SD (f i) g := by
  have hpt : ∀ a, |(∑ i, w i * f i a) - g a| ≤ ∑ i, w i * |f i a - g a| := by
    intro a
    have heq : (∑ i, w i * f i a) - g a = ∑ i, w i * (f i a - g a) := by
      have h1 : ∀ i, w i * (f i a - g a) = w i * f i a - w i * g a := fun i => mul_sub _ _ _
      simp_rw [h1, Finset.sum_sub_distrib, ← Finset.sum_mul, hw1, one_mul]
    rw [heq]
    calc |∑ i, w i * (f i a - g a)| ≤ ∑ i, |w i * (f i a - g a)| := Finset.abs_sum_le_sum_abs _ _
      _ = ∑ i, w i * |f i a - g a| :=
          Finset.sum_congr rfl (fun i _ => by rw [abs_mul, abs_of_nonneg (hw0 i)])
  change (1 / 2 : ℝ) * ∑ a, |(∑ i, w i * f i a) - g a| ≤ ∑ i, w i * ((1 / 2) * ∑ a, |f i a - g a|)
  calc (1 / 2 : ℝ) * ∑ a, |(∑ i, w i * f i a) - g a|
      ≤ (1 / 2 : ℝ) * ∑ a, ∑ i, w i * |f i a - g a| :=
        mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun a _ => hpt a)) (by norm_num)
    _ = (1 / 2 : ℝ) * ∑ i, ∑ a, w i * |f i a - g a| := by rw [Finset.sum_comm]
    _ = ∑ i, w i * ((1 / 2) * ∑ a, |f i a - g a|) := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl (fun i _ => ?_)
        rw [← Finset.mul_sum]
        ring

/-- `DeltaOf H` is convex: a nonnegative average (over `k`) of `SD(·, U_R)` (convex) precomposed
with the linear pushforward `p ↦ rowDistOf H p k`. -/
theorem DeltaOf_convex (H : Table K D R) (n : ℕ) (α : Fin n → ℝ) (p : Fin n → D → ℝ)
    (_hα0 : ∀ i, 0 ≤ α i) (_hα1 : ∑ i, α i = 1) :
    DeltaOf K D R H (fun x => ∑ i, α i * p i x) ≤ ∑ i, α i * DeltaOf K D R H (p i) := by
  have hk : ∀ k : K, SD (rowDistOf K D R H (fun x => ∑ i, α i * p i x) k) (unifR R)
      ≤ ∑ i, α i * SD (rowDistOf K D R H (p i) k) (unifR R) := by
    intro k
    have heq : rowDistOf K D R H (fun x => ∑ i, α i * p i x) k
        = fun r => ∑ i, α i * rowDistOf K D R H (p i) k r :=
      funext (fun r => rowDistOf_convex_combination H α p k r)
    rw [heq]
    exact SD_convex_combination α (fun i r => rowDistOf K D R H (p i) k r) (unifR R) _hα0 _hα1
  change (Fintype.card K : ℝ)⁻¹ *
        ∑ k, SD (rowDistOf K D R H (fun x => ∑ i, α i * p i x) k) (unifR R)
      ≤ ∑ i, α i * ((Fintype.card K : ℝ)⁻¹ * ∑ k, SD (rowDistOf K D R H (p i) k) (unifR R))
  calc (Fintype.card K : ℝ)⁻¹ * ∑ k, SD (rowDistOf K D R H (fun x => ∑ i, α i * p i x) k) (unifR R)
      ≤ (Fintype.card K : ℝ)⁻¹ * ∑ k, ∑ i, α i * SD (rowDistOf K D R H (p i) k) (unifR R) :=
        mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun k _ => hk k)) (by positivity)
    _ = (Fintype.card K : ℝ)⁻¹ * ∑ i, ∑ k, α i * SD (rowDistOf K D R H (p i) k) (unifR R) := by
        rw [Finset.sum_comm]
    _ = (Fintype.card K : ℝ)⁻¹ * ∑ i, α i * ∑ k, SD (rowDistOf K D R H (p i) k) (unifR R) := by
        congr 1
        refine Finset.sum_congr rfl (fun i _ => ?_)
        rw [Finset.mul_sum]
    _ = ∑ i, α i * ((Fintype.card K : ℝ)⁻¹ * ∑ k, SD (rowDistOf K D R H (p i) k) (unifR R)) := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl (fun i _ => ?_)
        ring

/-- **Lemma (flattening).** `Δ_{H,z} ≤ Φ_H(t)` where `t = ⌊1/ε_{H,z}⌋`, provided the view `(H,z)`
has positive probability (elsewhere `Δ_{H,z}` is junk, killed by its zero weight in `Assemble`). -/
theorem lemma_flat (S : Source K D R) (H : Table K D R) (z : Aux) (hpos : 0 < margZ S H z) :
    DeltaHz S H z ≤ Phi K D R H ⌊(epsHz S H z)⁻¹⌋₊ := by
  set t := ⌊(epsHz S H z)⁻¹⌋₊ with htdef
  -- (a) `condX S H z` is a genuine probability vector on `D`.
  have hcx0 : ∀ x, 0 ≤ condX S H z x := fun x =>
    div_nonneg ENNReal.toReal_nonneg hpos.le
  have hcx1 : ∑ x, condX S H z x = 1 := by
    have hs : ∑ x, condX S H z x = (∑ x, sourceProb S H x z) / margZ S H z := by
      simp only [condX]
      rw [Finset.sum_div]
    rw [hs]
    have hmz : (∑ x, sourceProb S H x z) = margZ S H z := rfl
    rw [hmz, div_self hpos.ne']
  -- (b) `epsHz S H z > 0`.
  have heps_pos : 0 < epsHz S H z := by
    by_contra hc
    push_neg at hc
    have hle0 : ∀ x, condX S H z x ≤ 0 := fun x =>
      le_trans (Finset.le_sup' (condX S H z) (Finset.mem_univ x)) hc
    have hsum_le : ∑ x, condX S H z x ≤ 0 := Finset.sum_nonpos (fun x _ => hle0 x)
    rw [hcx1] at hsum_le
    linarith
  -- (c) `epsHz S H z ≤ 1`.
  have heps_le1 : epsHz S H z ≤ 1 := by
    apply Finset.sup'_le
    intro x _
    change sourceProb S H x z / margZ S H z ≤ 1
    rw [div_le_one hpos]
    have hle : sourceProb S H x z ≤ ∑ x' : D, sourceProb S H x' z :=
      Finset.single_le_sum (f := fun x' => sourceProb S H x' z)
        (fun x' _ => ENNReal.toReal_nonneg) (Finset.mem_univ x)
    exact hle
  -- `epsHz S H z ≥ 1 / |D|` (the max of a nonneg family is at least its average).
  have hcard_pos : (0 : ℝ) < (Fintype.card D : ℝ) := by
    have h := Fintype.card_pos (α := D); exact_mod_cast h
  have heps_ge : (Fintype.card D : ℝ)⁻¹ ≤ epsHz S H z := by
    by_contra hc
    push_neg at hc
    have hlt : ∀ x, condX S H z x < (Fintype.card D : ℝ)⁻¹ := fun x =>
      lt_of_le_of_lt (Finset.le_sup' (condX S H z) (Finset.mem_univ x)) hc
    have hsum_lt : ∑ x, condX S H z x < ∑ _x : D, (Fintype.card D : ℝ)⁻¹ :=
      Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun x _ => hlt x)
    have hsum_const : ∑ _x : D, (Fintype.card D : ℝ)⁻¹ = 1 := by
      rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_inv_cancel₀ hcard_pos.ne']
    rw [hcx1, hsum_const] at hsum_lt
    exact absurd hsum_lt (lt_irrefl 1)
  -- `1 ≤ t` and `t ≤ |D|`.
  have hinv_ge1 : (1 : ℝ) ≤ (epsHz S H z)⁻¹ := by
    have h2 := mul_le_mul_of_nonneg_left heps_le1 (inv_pos.mpr heps_pos).le
    rwa [inv_mul_cancel₀ heps_pos.ne', mul_one] at h2
  have ht1 : 1 ≤ t := by
    rw [htdef]; exact Nat.le_floor (by exact_mod_cast hinv_ge1)
  have hb : (epsHz S H z)⁻¹ ≤ (Fintype.card D : ℝ) := by
    have h2 : (1 : ℝ) ≤ epsHz S H z * (Fintype.card D : ℝ) := by
      have h3 := mul_le_mul_of_nonneg_right heps_ge hcard_pos.le
      rwa [inv_mul_cancel₀ hcard_pos.ne'] at h3
    have h4 := mul_le_mul_of_nonneg_left h2 (inv_pos.mpr heps_pos).le
    rwa [mul_one, ← mul_assoc, inv_mul_cancel₀ heps_pos.ne', one_mul] at h4
  have htD : t ≤ Fintype.card D := by
    rw [htdef]
    calc ⌊(epsHz S H z)⁻¹⌋₊ ≤ ⌊(Fintype.card D : ℝ)⌋₊ := Nat.floor_mono hb
      _ = Fintype.card D := Nat.floor_natCast _
  -- (d) `condX S H z` is capped at `1/t`.
  have htpos : (0 : ℝ) < (t : ℝ) := by
    have ht0 : 0 < t := by omega
    exact_mod_cast ht0
  have ht_le_inv : (t : ℝ) ≤ (epsHz S H z)⁻¹ := by
    rw [htdef]; exact Nat.floor_le (by positivity)
  have heps_le_inv_t : epsHz S H z ≤ (t : ℝ)⁻¹ := by
    have hstep : epsHz S H z * (t : ℝ) ≤ 1 := by
      have h2 := mul_le_mul_of_nonneg_left ht_le_inv heps_pos.le
      rwa [mul_inv_cancel₀ heps_pos.ne'] at h2
    have h3 : epsHz S H z * (t : ℝ) * (t : ℝ)⁻¹ ≤ 1 * (t : ℝ)⁻¹ :=
      mul_le_mul_of_nonneg_right hstep (by positivity)
    rwa [mul_assoc, mul_inv_cancel₀ htpos.ne', mul_one, one_mul] at h3
  have hcap : ∀ x, condX S H z x ≤ (t : ℝ)⁻¹ := fun x =>
    le_trans (Finset.le_sup' (condX S H z) (Finset.mem_univ x)) heps_le_inv_t
  -- Apply the hypersimplex decomposition and convexity of `DeltaOf`.
  obtain ⟨n, α, T, hα0, hα1, hTcard, hpdecomp⟩ :=
    hypersimplex_decomp t ht1 htD (condX S H z) hcx0 hcx1 hcap
  have heq : DeltaHz S H z = DeltaOf K D R H (fun x => ∑ i, α i * Tindicator D (T i) x) := by
    simp only [DeltaHz]
    congr 1
    funext x
    exact hpdecomp x
  have hconv : DeltaOf K D R H (fun x => ∑ i, α i * Tindicator D (T i) x)
      ≤ ∑ i, α i * DeltaOf K D R H (Tindicator D (T i)) :=
    DeltaOf_convex H n α (fun i => Tindicator D (T i)) hα0 hα1
  have hbound : ∀ i, DeltaOf K D R H (Tindicator D (T i)) ≤ Phi K D R H t := by
    intro i
    have hmem : T i ∈ Finset.univ.filter (fun T : Finset D => T.card = t) :=
      Finset.mem_filter.mpr ⟨Finset.mem_univ _, hTcard i⟩
    simp only [Phi]
    rw [dif_pos ⟨T i, hmem⟩]
    exact Finset.le_sup' (Fdist K D R H) hmem
  have hfinal : ∑ i, α i * DeltaOf K D R H (Tindicator D (T i)) ≤ ∑ i, α i * Phi K D R H t := by
    apply Finset.sum_le_sum
    intro i _
    exact mul_le_mul_of_nonneg_left (hbound i) (hα0 i)
  have hsum_phi : ∑ i, α i * Phi K D R H t = Phi K D R H t := by
    rw [← Finset.sum_mul, hα1, one_mul]
  rw [heq]
  exact hconv.trans (hfinal.trans (le_of_eq hsum_phi))

end Flat

section Restriction

/-- Splits a function on `ι` into its restriction to a subset `S` and to the complement. -/
noncomputable def restrictEquiv {ι : Type} [Fintype ι] [DecidableEq ι] (γ : Type) (S : Finset ι) :
    (ι → γ) ≃ (↥S → γ) × (↥(Sᶜ : Finset ι) → γ) where
  toFun H := (fun x => H x, fun x => H x)
  invFun q x := if h : x ∈ S then q.1 ⟨x, h⟩ else q.2 ⟨x, by simpa using h⟩
  left_inv H := by
    funext x; dsimp only; split
    · rfl
    · rfl
  right_inv q := by
    ext p
    · dsimp only; rw [dif_pos p.2]
    · dsimp only; rw [dif_neg (Finset.mem_compl.mp p.2)]

/-- Averaging a function that factors through the restriction of a uniformly-random `ι → γ` to a
subset `S` reduces to averaging directly over the (uniform) restricted type `↥S → γ`: restricting
a uniform table stays uniform. This is the one piece of genuinely novel combinatorial machinery
`Lemma unif`'s McDiarmid application and `Lemma mean` both need — no Mathlib precedent for this
style of "sub-table is still uniform" argument exists. -/
theorem restrict_average {ι : Type} [Fintype ι] [DecidableEq ι] (γ : Type) [Fintype γ]
    [Nonempty γ] (S : Finset ι) (g : (↥S → γ) → ℝ) :
    (Fintype.card (ι → γ) : ℝ)⁻¹ * ∑ H : ι → γ, g (fun x => H x) =
      (Fintype.card (↥S → γ) : ℝ)⁻¹ * ∑ ρ : ↥S → γ, g ρ := by
  set e := restrictEquiv γ S with he
  have hproj : ∀ H : ι → γ, (e H).1 = fun x : ↥S => H x := fun _ => rfl
  have hcard : Fintype.card (ι → γ) =
      Fintype.card (↥S → γ) * Fintype.card (↥(Sᶜ : Finset ι) → γ) := by
    rw [← Fintype.card_prod]; exact Fintype.card_congr e
  have hstep : ∑ H : ι → γ, g (fun x => H x) =
      Fintype.card (↥(Sᶜ : Finset ι) → γ) * ∑ ρ : ↥S → γ, g ρ := by
    calc ∑ H : ι → γ, g (fun x => H x)
        = ∑ H : ι → γ, g (e H).1 := by simp_rw [hproj]
      _ = ∑ q : (↥S → γ) × (↥(Sᶜ : Finset ι) → γ), g q.1 := Equiv.sum_comp e (fun q => g q.1)
      _ = ∑ _a : ↥S → γ, ∑ _b : ↥(Sᶜ : Finset ι) → γ, g _a := Fintype.sum_prod_type _
      _ = ∑ a : ↥S → γ, (Fintype.card (↥(Sᶜ : Finset ι) → γ) : ℕ) * g a := by
          simp_rw [Finset.sum_const, nsmul_eq_mul, Finset.card_univ]
      _ = Fintype.card (↥(Sᶜ : Finset ι) → γ) * ∑ a : ↥S → γ, g a := by rw [← Finset.mul_sum]
  rw [hstep, hcard]
  have hne : (Fintype.card (↥(Sᶜ : Finset ι) → γ) : ℝ) ≠ 0 := by positivity
  push_cast
  field_simp

/-- The joint law of any finite tuple of coordinates of a uniformly-random `ι → γ` is itself
uniform: `Pr[ρ|_A = c₀] = |γ|⁻¹^|A|`. Specializes (`|A|=1`) to a single coordinate being uniform,
and (`|A|=2`) to the pairwise-independence fact `Lemma mean`'s variance computation needs. -/
theorem coords_prob {ι γ : Type} [Fintype ι] [DecidableEq ι] [Fintype γ] [Nonempty γ]
    [DecidableEq γ] (A : Finset ι) (c0 : ↥A → γ) :
    (Fintype.card (ι → γ) : ℝ)⁻¹ *
      (Finset.univ.filter (fun ρ : ι → γ => ∀ a : ↥A, ρ a = c0 a)).card
      = (Fintype.card γ : ℝ)⁻¹ ^ A.card := by
  have hmain := restrict_average γ A (fun ρ' : ↥A → γ => if ρ' = c0 then (1 : ℝ) else 0)
  have hL : ∀ H : ι → γ,
      (if (fun y : ↥A => H y) = c0 then (1 : ℝ) else 0) =
        (if ∀ a : ↥A, H a = c0 a then (1 : ℝ) else 0) := by
    intro H
    congr 1
    exact propext (by rw [funext_iff])
  simp_rw [hL] at hmain
  rw [Finset.sum_boole] at hmain
  rw [hmain]
  have hcard1 : Fintype.card (↥A → γ) = Fintype.card γ ^ A.card := by
    rw [Fintype.card_fun, Fintype.card_coe]
  rw [hcard1]
  have hsum : ∑ ρ' : (↥A → γ), (if ρ' = c0 then (1 : ℝ) else 0) = 1 := by
    rw [Finset.sum_boole]
    have : (Finset.univ.filter (fun ρ' : (↥A → γ) => ρ' = c0)) = {c0} := by
      ext ρ'; simp
    rw [this, Finset.card_singleton]; norm_num
  rw [hsum, mul_one, inv_pow]
  norm_cast

/-- A single-coordinate specialization of `coords_prob`, stated without the `↥A`-indexed
function-equality wrapper: `Pr[ρ x = c] = |γ|⁻¹`. -/
theorem coord_prob {ι γ : Type} [Fintype ι] [DecidableEq ι] [Fintype γ] [Nonempty γ]
    [DecidableEq γ] (x : ι) (c : γ) :
    (Fintype.card (ι → γ) : ℝ)⁻¹ * (Finset.univ.filter (fun ρ : ι → γ => ρ x = c)).card
      = (Fintype.card γ : ℝ)⁻¹ := by
  have hpt : x ∈ ({x} : Finset ι) := Finset.mem_singleton_self x
  have hmain := coords_prob ({x} : Finset ι) (fun _ : ↥({x} : Finset ι) => c)
  have hL : (Finset.univ.filter
      (fun ρ : ι → γ => ∀ a : ↥({x} : Finset ι), ρ a = c)) =
      (Finset.univ.filter (fun ρ : ι → γ => ρ x = c)) := by
    ext ρ
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    constructor
    · intro h; exact h ⟨x, hpt⟩
    · intro h a
      have : (a : ι) = x := Finset.mem_singleton.mp a.2
      rw [this]; exact h
  rw [hL, Finset.card_singleton, pow_one] at hmain
  exact hmain

/-- Given a fixed row `k`, a `t`-subset `T ⊆ D` and a table restricted to `K × T`, the `t`
coordinates of row `k` restricted to `T` correspond exactly to the `t` elements of `↥T`. -/
noncomputable def rowEquiv (k : K) (T : Finset D) :
    ↥T ≃ ↥(({k} : Finset K) ×ˢ T : Finset (K × D)) where
  toFun x := ⟨(k, x.1), by simp [x.2]⟩
  invFun p := ⟨p.1.2, by
    have h := p.2
    rw [Finset.mem_product, Finset.mem_singleton] at h
    exact h.2⟩
  left_inv x := by simp
  right_inv p := by
    obtain ⟨⟨k', x'⟩, hp⟩ := p
    simp only [Finset.mem_product, Finset.mem_singleton] at hp
    obtain ⟨hk', hx'⟩ := hp
    subst hk'
    rfl

end Restriction

section Mean

/-- `∑ x : D, (if x ∈ T then f x else 0) = ∑ x : ↥T, f x`: bookkeeping bridge between a `D`-indexed
sum with a membership guard and the corresponding `↥T`-indexed sum. -/
private theorem sum_coe_of_ite_mem {β : Type*} [AddCommMonoid β] (T : Finset D) (f : D → β) :
    ∑ x : D, (if x ∈ T then f x else 0) = ∑ x : T, f x := by
  rw [Finset.sum_coe_sort T f, ← Finset.sum_filter]
  congr 1
  ext x
  simp

/-- `rowDistOf`'s `D`-indexed sum, restricted along `Tindicator`, is really only a sum over `↥T`. -/
private theorem rowDistOf_Tindicator_eq (H : Table K D R) (T : Finset D) (k : K) (r : R) :
    rowDistOf K D R H (Tindicator D T) k r
      = ∑ x : T, if H (k, (x:D)) = r then (T.card:ℝ)⁻¹ else 0 := by
  have hpt : ∀ x : D, (if H (k,x) = r then Tindicator D T x else 0)
      = (if x ∈ T then (if H (k,x) = r then (T.card:ℝ)⁻¹ else 0) else 0) := by
    intro x
    by_cases hxT : x ∈ T
    · simp [Tindicator, hxT]
    · simp [Tindicator, hxT]
  show (∑ x : D, if H (k,x) = r then Tindicator D T x else 0) = _
  rw [Finset.sum_congr rfl (fun x _ => hpt x)]
  exact sum_coe_of_ite_mem T (fun x => if H (k,x) = r then (T.card:ℝ)⁻¹ else 0)

/-- Bridging further to the `↥S_k`-indexed sum (`S_k = {k} ×ˢ T`) via `rowEquiv`. -/
private theorem rowDistOf_eq_Sk (H : Table K D R) (T : Finset D) (k : K) (r : R) :
    rowDistOf K D R H (Tindicator D T) k r
      = ∑ y : (({k} : Finset K) ×ˢ T : Finset (K × D)),
          if H (y : K × D) = r then (T.card:ℝ)⁻¹ else 0 := by
  rw [rowDistOf_Tindicator_eq]
  apply Fintype.sum_equiv (rowEquiv k T)
  intro x
  have hcoe : ((rowEquiv k T) x : K × D) = (k, (x:D)) := by simp [rowEquiv]
  simp [hcoe]

/-- Reduce the per-`k` mean of `SD(rowDistOf ⋯, U_R)` over the whole table to the analogous
statement about `ρ : ↥S_k → R` uniform, via `restrict_average`. -/
private theorem Fdist_row_reduce (T : Finset D) (k : K) :
    (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R,
        SD (rowDistOf K D R H (Tindicator D T) k) (unifR R)
      = (Fintype.card (↥(({k}:Finset K) ×ˢ T : Finset (K×D)) → R) : ℝ)⁻¹ *
        ∑ ρ : (↥(({k}:Finset K) ×ˢ T : Finset (K×D)) → R),
          SD (fun r => ∑ y : (({k}:Finset K) ×ˢ T : Finset (K×D)),
              if ρ y = r then (T.card:ℝ)⁻¹ else 0)
            (unifR R) := by
  rw [← restrict_average R (({k}:Finset K) ×ˢ T)
    (fun ρ => SD (fun r => ∑ y : (({k}:Finset K) ×ˢ T : Finset (K×D)),
        if ρ y = r then (T.card:ℝ)⁻¹ else 0) (unifR R))]
  congr 1
  apply Finset.sum_congr rfl
  intro H _
  congr 1
  funext r
  exact rowDistOf_eq_Sk H T k r

/-- **Mean of the empirical frequency.** For `ρ : ι → R` uniform (`Fintype.card ι = t`), the
empirical frequency of a fixed `r : R` averages to exactly `1/|R|`, via `coord_prob`. -/
private theorem emp_mean {ι : Type} [Fintype ι] [DecidableEq ι] (t : ℕ) (ht : Fintype.card ι = t)
    (ht1 : 1 ≤ t) (r : R) :
    (Fintype.card (ι → R) : ℝ)⁻¹ * ∑ ρ : ι → R,
        ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0)
      = (Fintype.card R : ℝ)⁻¹ := by
  have htR : (t:ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have step1 : ∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0)
      = (t:ℝ)⁻¹ * ∑ y : ι, ∑ ρ : ι → R, (if ρ y = r then (1:ℝ) else 0) := by
    rw [← Finset.mul_sum, Finset.sum_comm]
  rw [step1, mul_left_comm, Finset.mul_sum]
  have step2 : ∀ y : ι, (Fintype.card (ι → R):ℝ)⁻¹ * ∑ ρ : ι → R, (if ρ y = r then (1:ℝ) else 0)
      = (Fintype.card R:ℝ)⁻¹ := by
    intro y
    rw [Finset.sum_boole]
    exact coord_prob y r
  rw [Finset.sum_congr rfl (fun y _ => step2 y)]
  rw [Finset.sum_const, Finset.card_univ, ht, nsmul_eq_mul]
  rw [← mul_assoc, inv_mul_cancel₀ htR, one_mul]

/-- **Variance bound of the empirical frequency.** For `ρ : ι → R` uniform (`Fintype.card ι = t`),
`Var[emp(r)] ≤ 1/(tR)`, via the exact closed form `Var = 1/(tR) - 1/(tR²)` (diagonal terms of the
variance's double sum handled by `coord_prob`, off-diagonal by `coords_prob` at pairs). -/
private theorem emp_var_le {ι : Type} [Fintype ι] [DecidableEq ι] (t : ℕ) (ht : Fintype.card ι = t)
    (ht1 : 1 ≤ t) (r : R) :
    (Fintype.card (ι → R) : ℝ)⁻¹ * ∑ ρ : ι → R,
        (((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) - (Fintype.card R : ℝ)⁻¹) ^ 2
      ≤ ((t:ℝ) * Fintype.card R)⁻¹ := by
  have htR : (t:ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have hRpos : (0:ℝ) < (Fintype.card R : ℝ) := by
    have := Fintype.card_pos (α := R); exact_mod_cast this
  rw [mul_inv]
  set c : ℝ := (Fintype.card R : ℝ)⁻¹ with hcdef
  set K0 : ℝ := (Fintype.card (ι → R) : ℝ)⁻¹ with hK0def
  have hcard_pos : (0:ℝ) < (Fintype.card (ι → R) : ℝ) := by positivity
  have h1 : K0 * (Fintype.card (ι → R) : ℝ) = 1 := by
    rw [hK0def]; exact inv_mul_cancel₀ hcard_pos.ne'
  have h2 : K0 * ∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) = c :=
    emp_mean t ht ht1 r
  have h3 : K0 * ∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) ^ 2
      = c ^ 2 + (t:ℝ)⁻¹ * c - (t:ℝ)⁻¹ * c ^ 2 := by
    have hSsq : ∀ ρ : ι → R, (∑ y : ι, if ρ y = r then (1:ℝ) else 0) ^ 2
        = ∑ y : ι, ∑ y' : ι, (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0) := by
      intro ρ
      rw [sq, Finset.sum_mul_sum]
    have hXsq : ∀ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) ^ 2
        = (t:ℝ)⁻¹ ^ 2 * ∑ y : ι, ∑ y' : ι,
            (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0) := by
      intro ρ
      rw [mul_pow, hSsq ρ]
    rw [Finset.sum_congr rfl (fun ρ _ => hXsq ρ)]
    have hswap : ∑ ρ : ι → R, ∑ y : ι, ∑ y' : ι,
        (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0)
        = ∑ y : ι, ∑ y' : ι, ∑ ρ : ι → R,
            (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0) := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro y _
      rw [Finset.sum_comm]
    have hpull : K0 * ((t:ℝ)⁻¹ ^ 2 * ∑ y : ι, ∑ y' : ι, ∑ ρ : ι → R,
        (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0))
        = (t:ℝ)⁻¹ ^ 2 * ∑ y : ι, ∑ y' : ι, (K0 * ∑ ρ : ι → R,
            (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0)) := by
      rw [← mul_assoc, mul_comm K0 ((t:ℝ)⁻¹ ^ 2), mul_assoc]
      congr 1
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro y _
      rw [Finset.mul_sum]
    have hpullt : ∑ ρ : ι → R, ((t:ℝ)⁻¹ ^ 2 * ∑ y : ι, ∑ y' : ι,
        (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0))
        = (t:ℝ)⁻¹ ^ 2 * ∑ ρ : ι → R, ∑ y : ι, ∑ y' : ι,
            (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0) :=
      (Finset.mul_sum _ _ _).symm
    rw [hpullt, hswap, hpull]
    have hpt : ∀ y y' : ι, K0 * ∑ ρ : ι → R,
        (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0)
        = if y = y' then c else c ^ 2 := by
      intro y y'
      have hprod : ∀ ρ : ι → R, (if ρ y = r then (1:ℝ) else 0) * (if ρ y' = r then (1:ℝ) else 0)
          = if (ρ y = r ∧ ρ y' = r) then (1:ℝ) else 0 := by
        intro ρ
        by_cases h1 : ρ y = r <;> by_cases h2 : ρ y' = r <;> simp [h1, h2]
      rw [Finset.sum_congr rfl (fun ρ _ => hprod ρ), Finset.sum_boole]
      by_cases hyy : y = y'
      · subst hyy
        have hfeq : (Finset.univ.filter (fun ρ : ι → R => ρ y = r ∧ ρ y = r))
            = (Finset.univ.filter (fun ρ : ι → R => ρ y = r)) := by
          apply Finset.filter_congr
          intro ρ _
          simp
        rw [hfeq, if_pos rfl]
        exact coord_prob y r
      · rw [if_neg hyy]
        have hA : ({y, y'} : Finset ι).card = 2 := Finset.card_pair hyy
        have hset : (Finset.univ.filter (fun ρ : ι → R => ρ y = r ∧ ρ y' = r))
            = (Finset.univ.filter (fun ρ : ι → R => ∀ a : ↥({y, y'} : Finset ι), ρ a = r)) := by
          ext ρ
          simp only [Finset.mem_filter, Finset.mem_univ, true_and]
          constructor
          · rintro ⟨hy, hy'⟩ a
            rcases Finset.mem_insert.mp a.2 with h | h
            · rw [h]; exact hy
            · rw [Finset.mem_singleton.mp h]; exact hy'
          · intro h
            exact ⟨h ⟨y, Finset.mem_insert_self y {y'}⟩,
              h ⟨y', Finset.mem_insert_of_mem (Finset.mem_singleton_self y')⟩⟩
        rw [hset]
        have hcp := coords_prob ({y, y'} : Finset ι) (fun _ : ↥({y, y'} : Finset ι) => r)
        rw [hA] at hcp
        rw [hcp]
    rw [Finset.sum_congr rfl (fun y (_ : y ∈ Finset.univ) =>
      Finset.sum_congr rfl (fun y' (_ : y' ∈ Finset.univ) => hpt y y'))]
    have hdelta : ∀ y : ι, ∑ y' : ι, (if y = y' then c else c ^ 2)
        = (Fintype.card ι : ℝ) * c ^ 2 + (c - c ^ 2) := by
      intro y
      have hrw : ∀ y' : ι, (if y = y' then c else c ^ 2)
          = c ^ 2 + if y = y' then (c - c ^ 2) else 0 := by
        intro y'
        by_cases h : y = y' <;> simp [h]
      rw [Finset.sum_congr rfl (fun y' _ => hrw y')]
      rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      congr 1
      rw [Finset.sum_ite_eq Finset.univ y (fun _ => c - c ^ 2)]
      simp
    rw [Finset.sum_congr rfl (fun y _ => hdelta y)]
    rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, ht,
      Finset.sum_const, Finset.card_univ, ht, nsmul_eq_mul, nsmul_eq_mul]
    field_simp
    ring
  have hsum_expand : ∑ ρ : ι → R,
      (((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) - c) ^ 2
      = (∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) ^ 2)
        - 2 * c * (∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0))
        + c ^ 2 * (Fintype.card (ι → R) : ℝ) := by
    have hpt2 : ∀ ρ : ι → R,
        (((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) - c) ^ 2
          = ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) ^ 2
            - 2 * c * ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) + c ^ 2 := by
      intro ρ; ring
    rw [Finset.sum_congr rfl (fun ρ _ => hpt2 ρ)]
    rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum, Finset.sum_const,
      Finset.card_univ, nsmul_eq_mul]
    ring
  have hfinal_eq : K0 * ∑ ρ : ι → R,
      (((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) - c) ^ 2
      = K0 * (∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) ^ 2)
        - 2 * c * (K0 * ∑ ρ : ι → R, ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0))
        + c ^ 2 * (K0 * (Fintype.card (ι → R) : ℝ)) := by
    rw [hsum_expand]; ring
  rw [hfinal_eq, h1, h2, h3]
  have ht_inv_nonneg : (0:ℝ) ≤ (t:ℝ)⁻¹ := by positivity
  nlinarith [mul_nonneg ht_inv_nonneg (sq_nonneg c)]

/-- Combine `fact_mad` with `emp_mean`/`emp_var_le` (per `r : R`), then sum over `r`, to bound the
`SD`-average for a generic uniform `ι → R`. This isolates all of the probability content of
`Lemma mean` from the `K,D,S_k`-specific bookkeeping, which `lemma_mean_row` supplies afterward. -/
private theorem mean_bound_generic {ι : Type} [Fintype ι] [DecidableEq ι] (t : ℕ)
    (ht : Fintype.card ι = t) (ht1 : 1 ≤ t) :
    (Fintype.card (ι → R) : ℝ)⁻¹ * ∑ ρ : ι → R,
        SD (fun r => ∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) (unifR R)
      ≤ (1 / 2) * Real.sqrt (Fintype.card R / t) := by
  have htR : (t:ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have hRpos : (0:ℝ) < (Fintype.card R : ℝ) := by
    have := Fintype.card_pos (α := R); exact_mod_cast this
  have hcard_pos : (0:ℝ) < (Fintype.card (ι → R) : ℝ) := by positivity
  have hbound : ∀ r : R, (Fintype.card (ι → R) : ℝ)⁻¹ *
      ∑ ρ : ι → R, |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹|
      ≤ Real.sqrt (((t:ℝ) * Fintype.card R)⁻¹) := by
    intro r
    have hpteq : ∀ ρ : ι → R, (∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0)
        = (t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0 := by
      intro ρ
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro y _
      by_cases h : ρ y = r <;> simp [h]
    rw [Finset.sum_congr rfl (fun ρ (_ : ρ ∈ Finset.univ) => by rw [hpteq ρ])]
    have hp0 : ∀ _ρ : ι → R, (0:ℝ) ≤ (Fintype.card (ι→R):ℝ)⁻¹ := fun _ => by positivity
    have hp1 : ∑ _ρ : ι → R, (Fintype.card (ι→R):ℝ)⁻¹ = 1 := by
      rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      exact mul_inv_cancel₀ hcard_pos.ne'
    have hmad := fact_mad (fun _ : ι → R => (Fintype.card (ι→R):ℝ)⁻¹) hp0 hp1
      (fun ρ => (t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0)
    have hmean' : ∑ ρ : ι → R, (Fintype.card (ι→R):ℝ)⁻¹ *
        ((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) = (Fintype.card R:ℝ)⁻¹ := by
      rw [← Finset.mul_sum]
      exact emp_mean t ht ht1 r
    rw [hmean'] at hmad
    have hvar' : ∑ ρ : ι → R, (Fintype.card (ι→R):ℝ)⁻¹ *
        (((t:ℝ)⁻¹ * ∑ y : ι, if ρ y = r then (1:ℝ) else 0) - (Fintype.card R:ℝ)⁻¹) ^ 2
        ≤ ((t:ℝ) * Fintype.card R)⁻¹ := by
      rw [← Finset.mul_sum]
      exact emp_var_le t ht ht1 r
    have hfin := hmad.trans (Real.sqrt_le_sqrt hvar')
    rwa [← Finset.mul_sum] at hfin
  have hSDeq : ∀ ρ : ι → R, SD (fun r => ∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) (unifR R)
      = (1/2:ℝ) * ∑ r : R, |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹| := by
    intro ρ
    rfl
  rw [Finset.sum_congr rfl (fun ρ (_ : ρ ∈ Finset.univ) => hSDeq ρ)]
  have hstep1 : (Fintype.card (ι→R):ℝ)⁻¹ * ∑ ρ : ι → R, (1/2:ℝ) * ∑ r : R,
      |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹|
      = (1/2:ℝ) * ∑ r : R, ((Fintype.card (ι→R):ℝ)⁻¹ * ∑ ρ : ι → R,
          |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹|) := by
    have ha : ∑ ρ : ι → R, (1/2:ℝ) * ∑ r : R,
        |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹|
        = (1/2:ℝ) * ∑ ρ : ι → R, ∑ r : R,
            |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹| :=
      (Finset.mul_sum _ _ _).symm
    rw [ha, Finset.sum_comm, mul_left_comm, Finset.mul_sum]
  rw [hstep1]
  have hA_nonneg : 0 ≤ (Fintype.card R:ℝ) * Real.sqrt (((t:ℝ)*Fintype.card R)⁻¹) := by positivity
  have hA_sq : ((Fintype.card R:ℝ) * Real.sqrt (((t:ℝ)*Fintype.card R)⁻¹))^2
      = (Fintype.card R:ℝ)/t := by
    rw [mul_pow, Real.sq_sqrt (by positivity : (0:ℝ) ≤ ((t:ℝ)*Fintype.card R)⁻¹)]
    field_simp
  have hA : (Fintype.card R:ℝ) * Real.sqrt (((t:ℝ)*Fintype.card R)⁻¹)
      = Real.sqrt ((Fintype.card R:ℝ)/t) := by
    rw [← hA_sq, Real.sqrt_sq hA_nonneg]
  calc (1/2:ℝ) * ∑ r : R, ((Fintype.card (ι→R):ℝ)⁻¹ * ∑ ρ : ι → R,
        |(∑ y : ι, if ρ y = r then (t:ℝ)⁻¹ else 0) - (Fintype.card R:ℝ)⁻¹|)
      ≤ (1/2:ℝ) * ∑ _r : R, Real.sqrt (((t:ℝ) * Fintype.card R)⁻¹) :=
        mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun r _ => hbound r)) (by norm_num)
    _ = (1/2:ℝ) * (Fintype.card R : ℝ) * Real.sqrt (((t:ℝ) * Fintype.card R)⁻¹) := by
        rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]; ring
    _ = (1/2:ℝ) * Real.sqrt (Fintype.card R / t) := by
        rw [mul_assoc, hA]

/-- Per-`k` row bound: specialize `mean_bound_generic` to `ι := ↥S_k` via `Fdist_row_reduce`. -/
private theorem lemma_mean_row (T : Finset D) (t : ℕ) (hT : T.card = t) (ht1 : 1 ≤ t) (k : K) :
    (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R,
        SD (rowDistOf K D R H (Tindicator D T) k) (unifR R)
      ≤ (1 / 2) * Real.sqrt (Fintype.card R / t) := by
  rw [Fdist_row_reduce T k, hT]
  exact mean_bound_generic (ι := ↥(({k}:Finset K) ×ˢ T : Finset (K×D))) t
    (by rw [Fintype.card_coe, Finset.card_product, Finset.card_singleton, one_mul, hT]) ht1

/-- **Lemma (mean at a fixed support).** `E_H[F_T(H)] ≤ (1/2)√(R/t)` for any fixed `T` with
`|T| = t ≥ 1`, the expectation taken over `H` uniform on the whole table. -/
theorem lemma_mean (T : Finset D) (t : ℕ) (_ht : T.card = t) (_ht1 : 1 ≤ t) :
    (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, Fdist K D R H T ≤
      (1 / 2) * Real.sqrt (Fintype.card R / t) := by
  have hKpos : (0:ℝ) < (Fintype.card K:ℝ) := by
    have := Fintype.card_pos (α:=K); exact_mod_cast this
  have hstep : (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, Fdist K D R H T
      = (Fintype.card K:ℝ)⁻¹ * ∑ k : K, ((Fintype.card (Table K D R):ℝ)⁻¹ *
          ∑ H : Table K D R, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R)) := by
    have hFdist : ∀ H : Table K D R, Fdist K D R H T
        = (Fintype.card K:ℝ)⁻¹ * ∑ k : K, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R) := by
      intro H; rfl
    rw [Finset.sum_congr rfl (fun H (_ : H ∈ Finset.univ) => hFdist H)]
    have ha : ∑ H : Table K D R, (Fintype.card K:ℝ)⁻¹ * ∑ k : K,
        SD (rowDistOf K D R H (Tindicator D T) k) (unifR R)
        = (Fintype.card K:ℝ)⁻¹ * ∑ H : Table K D R, ∑ k : K,
            SD (rowDistOf K D R H (Tindicator D T) k) (unifR R) :=
      (Finset.mul_sum _ _ _).symm
    rw [ha, Finset.sum_comm, mul_left_comm, Finset.mul_sum]
  rw [hstep]
  calc (Fintype.card K:ℝ)⁻¹ * ∑ k : K, ((Fintype.card (Table K D R):ℝ)⁻¹ *
        ∑ H : Table K D R, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R))
      ≤ (Fintype.card K:ℝ)⁻¹ * ∑ _k : K, ((1/2:ℝ) * Real.sqrt (Fintype.card R / t)) :=
        mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun k _ => lemma_mean_row T t _ht _ht1 k))
          (by positivity)
    _ = (1/2:ℝ) * Real.sqrt (Fintype.card R / t) := by
        rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
        rw [← mul_assoc, inv_mul_cancel₀ hKpos.ne', one_mul]

end Mean

section Unif

/-- **Tail-integration fact.** resolution.tex gets `E_H[W_{1,+}] ≤ (6/5)√(a/K)` from the tail bound
`Pr[W_1 > √((a+u)/(2K))] ≤ ψ(u) := e^{-u}/(1-e^{-u})` (`u > 0` arbitrary) by writing
`E[W_{1,+}] = ∫_0^∞ Pr[W_{1,+} > s] ds` (valid since `W_{1,+} ≥ 0`), substituting `s = √((a+u)/(2K))`,
and evaluating the resulting integral (splitting at `u = ln 2`, the point where `ψ(u) = 1`). This
is a routine calculus computation, not particular to this paper's argument — the same kind of
borrowed "standard fact" as `fact_mcd`/`fact_binom` above, just needing Lebesgue/Riemann integration
machinery from scratch to formalize rather than the finite combinatorics the rest of this file
stays inside, so it is axiomatized rather than built via `MeasureTheory.integral` here. Stated
directly for a `[0,1]`-valued function on a finite population, matching exactly how it is used
below (no probability-theoretic apparatus needed beyond that). -/
axiom fact_tail_integrate {Ω : Type*} [Fintype Ω] [Nonempty Ω] (Y : Ω → ℝ)
    (_hY0 : ∀ ω, 0 ≤ Y ω) (_hY1 : ∀ ω, Y ω ≤ 1) (a K : ℝ) (_ha : 1 ≤ a) (_hK : 1 ≤ K)
    (_htail : ∀ u : ℝ, 0 < u →
      ((Finset.univ.filter (fun ω => Real.sqrt ((a + u) / (2 * K)) < Y ω)).card : ℝ)
        / Fintype.card Ω ≤ Real.exp (-u) / (1 - Real.exp (-u))) :
    (Fintype.card Ω : ℝ)⁻¹ * ∑ ω, Y ω ≤ (6 / 5) * Real.sqrt (a / K)

/-- For nonnegative reals, `|x - y| ≤ x + y`. -/
private theorem abs_sub_le_add_of_nonneg {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) : |x - y| ≤ x + y := by
  rw [abs_le]
  constructor <;> linarith

private theorem Tindicator_nonneg (T : Finset D) (x : D) : 0 ≤ Tindicator D T x := by
  unfold Tindicator
  split <;> positivity

private theorem Tindicator_sum_le_one (T : Finset D) : ∑ x : D, Tindicator D T x ≤ 1 := by
  have hfilter : Finset.univ.filter (fun x : D => x ∈ T) = T := by
    ext x; simp
  have heq : ∑ x : D, Tindicator D T x = ∑ x ∈ T, (T.card : ℝ)⁻¹ := by
    unfold Tindicator
    rw [← Finset.sum_filter, hfilter]
  rw [heq, Finset.sum_const, nsmul_eq_mul]
  rcases Nat.eq_zero_or_pos T.card with h0 | hpos
  · rw [h0]; norm_num
  · have hne : (T.card : ℝ) ≠ 0 := by exact_mod_cast hpos.ne'
    exact le_of_eq (mul_inv_cancel₀ hne)

private theorem rowDistOf_nonneg (H : Table K D R) (p : D → ℝ) (hp0 : ∀ x, 0 ≤ p x)
    (k : K) (r : R) : 0 ≤ rowDistOf K D R H p k r := by
  unfold rowDistOf
  apply Finset.sum_nonneg
  intro x _
  split
  · exact hp0 x
  · exact le_refl 0

private theorem rowDistOf_sum_eq (H : Table K D R) (p : D → ℝ) (k : K) :
    ∑ r : R, rowDistOf K D R H p k r = ∑ x : D, p x := by
  unfold rowDistOf
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl (fun x _ => ?_)
  simp

private theorem SD_le_one_of_le_one {α : Type*} [Fintype α] (f g : α → ℝ)
    (hf0 : ∀ a, 0 ≤ f a) (hg0 : ∀ a, 0 ≤ g a) (hf1 : ∑ a, f a ≤ 1) (hg1 : ∑ a, g a ≤ 1) :
    SD f g ≤ 1 := by
  unfold SD
  have hpt : ∀ a, |f a - g a| ≤ f a + g a := fun a => abs_sub_le_add_of_nonneg (hf0 a) (hg0 a)
  calc (1 / 2 : ℝ) * ∑ a, |f a - g a| ≤ (1 / 2) * ∑ a, (f a + g a) :=
        mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun a _ => hpt a)) (by norm_num)
    _ = (1 / 2) * (∑ a, f a + ∑ a, g a) := by rw [Finset.sum_add_distrib]
    _ ≤ (1 / 2) * (1 + 1) := by linarith
    _ = 1 := by norm_num

private theorem Fdist_le_one (H : Table K D R) (T : Finset D) : Fdist K D R H T ≤ 1 := by
  unfold Fdist DeltaOf
  have hbound : ∀ k : K, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R) ≤ 1 := by
    intro k
    apply SD_le_one_of_le_one
    · exact rowDistOf_nonneg H (Tindicator D T) (Tindicator_nonneg T) k
    · intro r; unfold unifR; positivity
    · rw [rowDistOf_sum_eq]; exact Tindicator_sum_le_one T
    · unfold unifR
      rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      have hRpos : 0 < Fintype.card R := Fintype.card_pos
      have hRne : (Fintype.card R : ℝ) ≠ 0 := by exact_mod_cast hRpos.ne'
      rw [mul_inv_cancel₀ hRne]
  have hKpos : 0 < Fintype.card K := Fintype.card_pos
  have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast hKpos.ne'
  calc (Fintype.card K : ℝ)⁻¹ * ∑ k : K, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R)
      ≤ (Fintype.card K : ℝ)⁻¹ * ∑ _k : K, (1 : ℝ) := by
        apply mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun k _ => hbound k))
        positivity
    _ = (Fintype.card K : ℝ)⁻¹ * (Fintype.card K : ℝ) := by
        rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
    _ = 1 := inv_mul_cancel₀ hKne

private theorem Phi_le_one (H : Table K D R) (t : ℕ) : Phi K D R H t ≤ 1 := by
  unfold Phi
  by_cases h : (Finset.univ.filter (fun T : Finset D => T.card = t)).Nonempty
  · rw [dif_pos h]
    exact Finset.sup'_le h (Fdist K D R H) (fun T _ => Fdist_le_one H T)
  · rw [dif_neg h]; norm_num

private theorem SD_comm {α : Type*} [Fintype α] (f g : α → ℝ) : SD f g = SD g f := by
  unfold SD
  congr 1
  refine Finset.sum_congr rfl (fun a _ => ?_)
  rw [abs_sub_comm]

private theorem SD_sub_le {α : Type*} [Fintype α] (f f' g : α → ℝ) :
    SD f g - SD f' g ≤ SD f f' := by
  unfold SD
  rw [← mul_sub, ← Finset.sum_sub_distrib]
  apply mul_le_mul_of_nonneg_left _ (by norm_num : (0:ℝ) ≤ 1/2)
  apply Finset.sum_le_sum
  intro a _
  have habs : ∀ x y : ℝ, |x| - |y| ≤ |x - y| := by
    intro x y
    have hx : |x| ≤ |y| + |x - y| := by
      rw [abs_le]
      constructor
      · have h1 : -|y| ≤ y := neg_abs_le y
        have h2 : -|x - y| ≤ x - y := neg_abs_le (x - y)
        linarith
      · have h1 : y ≤ |y| := le_abs_self y
        have h2 : x - y ≤ |x - y| := le_abs_self (x - y)
        linarith
    linarith
  have hthis := habs (f a - g a) (f' a - g a)
  rwa [show (f a - g a) - (f' a - g a) = f a - f' a from by ring] at hthis

private theorem SD_sub_abs_le {α : Type*} [Fintype α] (f f' g : α → ℝ) :
    |SD f g - SD f' g| ≤ SD f f' := by
  rw [abs_le]
  refine ⟨?_, SD_sub_le f f' g⟩
  have h1 := SD_sub_le f' f g
  rw [SD_comm f' f] at h1
  linarith

private theorem rowDistOf_Tindicator_congr {H H' : Table K D R} (T : Finset D) (k : K)
    (hagree : ∀ x ∈ T, H (k, x) = H' (k, x)) :
    rowDistOf K D R H (Tindicator D T) k = rowDistOf K D R H' (Tindicator D T) k := by
  funext r
  unfold rowDistOf
  refine Finset.sum_congr rfl (fun x _ => ?_)
  by_cases hx : x ∈ T
  · rw [hagree x hx]
  · unfold Tindicator
    rw [if_neg hx]
    by_cases hc : H (k, x) = r <;> by_cases hc' : H' (k, x) = r <;> simp [hc, hc']

private theorem Fdist_congr_of_agree {H H' : Table K D R} (T : Finset D)
    (hagree : ∀ k x, x ∈ T → H (k, x) = H' (k, x)) :
    Fdist K D R H T = Fdist K D R H' T := by
  unfold Fdist DeltaOf
  have heq : ∀ k : K, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R) =
      SD (rowDistOf K D R H' (Tindicator D T) k) (unifR R) := by
    intro k
    rw [rowDistOf_Tindicator_congr T k (fun x hx => hagree k x hx)]
  rw [Finset.sum_congr rfl (fun k _ => heq k)]

private theorem rowDistOf_Tindicator_bdd_diff (T : Finset D) (t : ℕ) (ht : T.card = t)
    (H H' : Table K D R) (k0 : K) (x0 : D)
    (hagree : ∀ p : K × D, p ≠ (k0, x0) → H p = H' p) :
    SD (rowDistOf K D R H (Tindicator D T) k0) (rowDistOf K D R H' (Tindicator D T) k0) ≤
      (t : ℝ)⁻¹ := by
  set c : ℝ := Tindicator D T x0 with hcdef
  have hcnn : 0 ≤ c := Tindicator_nonneg T x0
  have hcle : c ≤ (t : ℝ)⁻¹ := by
    rw [hcdef]; unfold Tindicator
    split
    · rw [ht]
    · positivity
  have hcol_eq : ∀ x : D, x ≠ x0 → H (k0, x) = H' (k0, x) := fun x hx =>
    hagree (k0, x) (fun heq => hx (congrArg Prod.snd heq))
  have hdiff_r : ∀ r : R, rowDistOf K D R H (Tindicator D T) k0 r -
      rowDistOf K D R H' (Tindicator D T) k0 r =
      (if H (k0, x0) = r then c else 0) - (if H' (k0, x0) = r then c else 0) := by
    intro r
    unfold rowDistOf
    rw [← Finset.add_sum_erase Finset.univ
          (fun x => if H (k0, x) = r then Tindicator D T x else 0) (Finset.mem_univ x0),
        ← Finset.add_sum_erase Finset.univ
          (fun x => if H' (k0, x) = r then Tindicator D T x else 0) (Finset.mem_univ x0)]
    have herase_eq :
        ∑ x ∈ Finset.univ.erase x0, (if H (k0, x) = r then Tindicator D T x else 0) =
        ∑ x ∈ Finset.univ.erase x0, (if H' (k0, x) = r then Tindicator D T x else 0) :=
      Finset.sum_congr rfl (fun x hx => by rw [hcol_eq x (Finset.ne_of_mem_erase hx)])
    rw [herase_eq]; ring
  have hpt : ∀ r : R, |rowDistOf K D R H (Tindicator D T) k0 r -
      rowDistOf K D R H' (Tindicator D T) k0 r| ≤
      (if H (k0, x0) = r then c else 0) + (if H' (k0, x0) = r then c else 0) := by
    intro r
    rw [hdiff_r r]
    exact abs_sub_le_add_of_nonneg
      (by by_cases h : H (k0, x0) = r <;> simp [h, hcnn])
      (by by_cases h : H' (k0, x0) = r <;> simp [h, hcnn])
  unfold SD
  have hsum_a : (∑ r : R, if H (k0, x0) = r then c else 0) = c := by simp
  have hsum_b : (∑ r : R, if H' (k0, x0) = r then c else 0) = c := by simp
  have hsum_le : ∑ r : R, |rowDistOf K D R H (Tindicator D T) k0 r -
      rowDistOf K D R H' (Tindicator D T) k0 r| ≤ 2 * c := by
    calc ∑ r : R, |rowDistOf K D R H (Tindicator D T) k0 r -
            rowDistOf K D R H' (Tindicator D T) k0 r|
        ≤ ∑ r : R, ((if H (k0, x0) = r then c else 0) + (if H' (k0, x0) = r then c else 0)) :=
          Finset.sum_le_sum (fun r _ => hpt r)
      _ = (∑ r : R, if H (k0, x0) = r then c else 0) +
            ∑ r : R, if H' (k0, x0) = r then c else 0 := Finset.sum_add_distrib
      _ = c + c := by rw [hsum_a, hsum_b]
      _ = 2 * c := by ring
  calc (1 / 2 : ℝ) * ∑ r : R, |rowDistOf K D R H (Tindicator D T) k0 r -
          rowDistOf K D R H' (Tindicator D T) k0 r|
      ≤ (1 / 2 : ℝ) * (2 * c) := by linarith [hsum_le]
    _ = c := by ring
    _ ≤ (t : ℝ)⁻¹ := hcle

private theorem Fdist_bdd_diff (T : Finset D) (t : ℕ) (ht : T.card = t)
    (H H' : Table K D R) (k0 : K) (x0 : D)
    (hagree : ∀ p : K × D, p ≠ (k0, x0) → H p = H' p) :
    |Fdist K D R H T - Fdist K D R H' T| ≤ (Fintype.card K * t : ℝ)⁻¹ := by
  have hrow_eq : ∀ k : K, k ≠ k0 →
      rowDistOf K D R H (Tindicator D T) k = rowDistOf K D R H' (Tindicator D T) k := by
    intro k hk
    funext r
    unfold rowDistOf
    refine Finset.sum_congr rfl (fun x _ => ?_)
    have hpne : (k, x) ≠ (k0, x0) := fun heq => hk (congrArg Prod.fst heq)
    rw [hagree (k, x) hpne]
  have herase_eq :
      ∑ k ∈ Finset.univ.erase k0, SD (rowDistOf K D R H (Tindicator D T) k) (unifR R) =
      ∑ k ∈ Finset.univ.erase k0, SD (rowDistOf K D R H' (Tindicator D T) k) (unifR R) :=
    Finset.sum_congr rfl (fun k hk => by rw [hrow_eq k (Finset.ne_of_mem_erase hk)])
  have hFdist_diff : Fdist K D R H T - Fdist K D R H' T =
      (Fintype.card K : ℝ)⁻¹ * (SD (rowDistOf K D R H (Tindicator D T) k0) (unifR R) -
        SD (rowDistOf K D R H' (Tindicator D T) k0) (unifR R)) := by
    unfold Fdist DeltaOf
    rw [← Finset.add_sum_erase Finset.univ
          (fun k => SD (rowDistOf K D R H (Tindicator D T) k) (unifR R)) (Finset.mem_univ k0),
        ← Finset.add_sum_erase Finset.univ
          (fun k => SD (rowDistOf K D R H' (Tindicator D T) k) (unifR R)) (Finset.mem_univ k0),
        herase_eq]
    ring
  have hKpos : 0 < Fintype.card K := Fintype.card_pos
  rw [hFdist_diff, abs_mul, abs_of_nonneg (by positivity : (0:ℝ) ≤ (Fintype.card K:ℝ)⁻¹)]
  have hrk0 : |SD (rowDistOf K D R H (Tindicator D T) k0) (unifR R) -
        SD (rowDistOf K D R H' (Tindicator D T) k0) (unifR R)| ≤ (t : ℝ)⁻¹ :=
    (SD_sub_abs_le _ _ _).trans (rowDistOf_Tindicator_bdd_diff T t ht H H' k0 x0 hagree)
  have hKt : (Fintype.card K * t : ℝ)⁻¹ = (Fintype.card K : ℝ)⁻¹ * (t : ℝ)⁻¹ := mul_inv _ _
  rw [hKt]
  exact mul_le_mul_of_nonneg_left hrk0 (by positivity)

private noncomputable def extendVal (S : Finset (K × D)) (ρ : ↥S → R) : Table K D R :=
  fun p => if h : p ∈ S then ρ ⟨p, h⟩ else Classical.arbitrary R

private noncomputable def gT (T : Finset D) (S : Finset (K × D)) (ρ : ↥S → R) : ℝ :=
  Fdist K D R (extendVal S ρ) T

private theorem Fdist_eq_g (T : Finset D) (H : Table K D R) :
    Fdist K D R H T = gT T ((Finset.univ : Finset K) ×ˢ T) (fun x => H x) := by
  unfold gT
  apply Fdist_congr_of_agree
  intro k x hx
  have hmem : (k, x) ∈ ((Finset.univ : Finset K) ×ˢ T : Finset (K × D)) :=
    Finset.mem_product.mpr ⟨Finset.mem_univ k, hx⟩
  unfold extendVal
  rw [dif_pos hmem]

private theorem gT_bdd_diff (T : Finset D) (t : ℕ) (ht : T.card = t)
    (i : ↥((Finset.univ : Finset K) ×ˢ T)) (ρ ρ' : ↥((Finset.univ : Finset K) ×ˢ T) → R)
    (hagree : ∀ j, j ≠ i → ρ j = ρ' j) :
    |gT T ((Finset.univ : Finset K) ×ˢ T) ρ - gT T ((Finset.univ : Finset K) ×ˢ T) ρ'| ≤
      (Fintype.card K * t : ℝ)⁻¹ := by
  unfold gT
  apply Fdist_bdd_diff T t ht (extendVal ((Finset.univ : Finset K) ×ˢ T) ρ)
    (extendVal ((Finset.univ : Finset K) ×ˢ T) ρ') (↑i : K × D).1 (↑i : K × D).2
  intro p hp
  unfold extendVal
  by_cases hpS : p ∈ ((Finset.univ : Finset K) ×ˢ T : Finset (K × D))
  · have hne : (⟨p, hpS⟩ : ↥((Finset.univ : Finset K) ×ˢ T)) ≠ i :=
      fun heq => hp (congrArg Subtype.val heq)
    rw [dif_pos hpS, dif_pos hpS, hagree ⟨p, hpS⟩ hne]
  · rw [dif_neg hpS, dif_neg hpS]

private theorem restrict_average_card {ι : Type} [Fintype ι] [DecidableEq ι] (γ : Type)
    [Fintype γ] [Nonempty γ] (S : Finset ι) (q : (↥S → γ) → Prop) [DecidablePred q] :
    ((Finset.univ.filter (fun H : ι → γ => q (fun x : ↥S => H x))).card : ℝ) /
        Fintype.card (ι → γ) =
      ((Finset.univ.filter q).card : ℝ) / Fintype.card (↥S → γ) := by
  rw [div_eq_inv_mul, div_eq_inv_mul, ← Finset.sum_boole, ← Finset.sum_boole]
  exact restrict_average γ S (fun ρ => if q ρ then (1:ℝ) else 0)

private theorem card_filter_card_eq_choose (t : ℕ) :
    (Finset.univ.filter (fun T : Finset D => T.card = t)).card = (Fintype.card D).choose t := by
  have hpowerset_eq : (Finset.univ.filter (fun T : Finset D => T.card = t)) =
      Finset.univ.powersetCard t := by
    ext T
    simp
  rw [hpowerset_eq, Finset.card_powersetCard, Finset.card_univ]

private theorem choose_exp_bound (t : ℕ) (ht1 : 1 ≤ t) (htD : t ≤ Fintype.card D) :
    ((Fintype.card D).choose t : ℝ) ≤ Real.exp ((t : ℝ) * aConst D) := by
  have hDcard_pos : (0 : ℝ) < (Fintype.card D : ℝ) := by
    have := Fintype.card_pos (α := D); exact_mod_cast this
  have htR : (0 : ℝ) < (t : ℝ) := by exact_mod_cast ht1
  have ht1R : (1 : ℝ) ≤ (t : ℝ) := by exact_mod_cast ht1
  have hbinom := fact_binom (Fintype.card D) t ht1 htD
  have heq1 : Real.exp 1 * (Fintype.card D : ℝ) / (t : ℝ) =
      Real.exp 1 * ((Fintype.card D : ℝ) / t) := by ring
  have heq2 : Real.exp 1 ^ t = Real.exp (t : ℝ) := by
    rw [← Real.exp_nat_mul, mul_one]
  have hle : ((Fintype.card D : ℝ) / t) ^ t ≤ (Fintype.card D : ℝ) ^ t := by
    gcongr
    rw [div_le_iff₀ htR]
    nlinarith [ht1R, hDcard_pos.le]
  have hexp_eq : Real.exp ((t : ℝ) * aConst D) =
      Real.exp (t : ℝ) * (Fintype.card D : ℝ) ^ t := by
    unfold aConst
    rw [mul_add, mul_one, Real.exp_add, Real.exp_nat_mul, Real.exp_log hDcard_pos]
  have hstep : (Real.exp 1 * (Fintype.card D : ℝ) / t) ^ t ≤ Real.exp ((t : ℝ) * aConst D) := by
    rw [heq1, mul_pow, heq2, hexp_eq]
    exact mul_le_mul_of_nonneg_left hle (Real.exp_pos _).le
  exact hbinom.trans hstep

private theorem geom_sum_Icc_one_eq (r : ℝ) (n : ℕ) :
    (1 - r) * ∑ t ∈ Finset.Icc 1 n, r ^ t = r - r ^ (n + 1) := by
  induction n with
  | zero =>
    have hempty : Finset.Icc 1 0 = (∅ : Finset ℕ) := Finset.Icc_eq_empty_of_lt (by omega)
    rw [hempty]
    simp
  | succ n ih =>
    have hins : Finset.Icc 1 (n + 1) = insert (n + 1) (Finset.Icc 1 n) := by
      ext t; simp only [Finset.mem_Icc, Finset.mem_insert]; omega
    have hnotmem : (n + 1) ∉ Finset.Icc 1 n := by simp
    have hpow : r ^ (n + 1 + 1) = r ^ (n + 1) * r := pow_succ r (n + 1)
    rw [hins, Finset.sum_insert hnotmem, mul_add, ih, hpow]
    ring

private theorem geom_sum_Icc_one_le {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r < 1) (n : ℕ) :
    ∑ t ∈ Finset.Icc 1 n, r ^ t ≤ r / (1 - r) := by
  have heq := geom_sum_Icc_one_eq r n
  have hpos : 0 < 1 - r := by linarith
  have hpow_nonneg : 0 ≤ r ^ (n + 1) := pow_nonneg hr0 _
  rw [le_div_iff₀ hpos, mul_comm, heq]
  linarith [hpow_nonneg]

/-- The McDiarmid + mean-centering estimate for a single fixed support `T` of size `t`: the
fraction of tables on which `F_T(H)` exceeds `lam` above its `lemma_mean` centering is at most
`exp(-2·lam²·(K·t))`. This is the "fix `T`" content of `resolution.tex`'s proof of `Lemma unif`. -/
private theorem Fdist_tail_bound (T : Finset D) (t : ℕ) (ht : T.card = t) (ht1 : 1 ≤ t)
    (lam : ℝ) (hlam : 0 < lam) :
    ((Finset.univ.filter
        (fun H : Table K D R =>
          lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < Fdist K D R H T)).card : ℝ) /
      Fintype.card (Table K D R) ≤
      Real.exp (-2 * lam ^ 2 * ((Fintype.card K : ℝ) * t)) := by
  set S : Finset (K × D) := (Finset.univ : Finset K) ×ˢ T with hSdef
  set g : (↥S → R) → ℝ := gT T S with hgdef
  have hgH : ∀ H : Table K D R, g (fun x : ↥S => H x) = Fdist K D R H T := by
    intro H
    rw [hgdef, hSdef]
    exact (Fdist_eq_g T H).symm
  have hmean_eq : (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, Fdist K D R H T =
      (Fintype.card (↥S → R) : ℝ)⁻¹ * ∑ ρ : ↥S → R, g ρ := by
    have hsum_eq : ∑ H : Table K D R, Fdist K D R H T =
        ∑ H : Table K D R, g (fun x : ↥S => H x) :=
      Finset.sum_congr rfl (fun H _ => (hgH H).symm)
    rw [hsum_eq]
    exact restrict_average R S g
  have hmean_le : (Fintype.card (↥S → R) : ℝ)⁻¹ * ∑ ρ : ↥S → R, g ρ ≤
      (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) := by
    rw [← hmean_eq]
    exact lemma_mean T t ht ht1
  have hpred_eq : (Finset.univ.filter
      (fun H : Table K D R =>
        lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < Fdist K D R H T)) =
      (Finset.univ.filter
        (fun H : Table K D R =>
          lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < g (fun x : ↥S => H x))) := by
    ext H
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    rw [hgH H]
  have hratio_eq :
      ((Finset.univ.filter
          (fun H : Table K D R =>
            lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < Fdist K D R H T)).card : ℝ) /
        Fintype.card (Table K D R) =
      ((Finset.univ.filter
          (fun ρ : ↥S → R => lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < g ρ)).card
          : ℝ) /
        Fintype.card (↥S → R) := by
    rw [hpred_eq]
    exact restrict_average_card R S
      (fun ρ : ↥S → R => lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < g ρ)
  have hsub :
      (Finset.univ.filter
        (fun ρ : ↥S → R => lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < g ρ)) ⊆
      (Finset.univ.filter
        (fun ρ : ↥S → R => (Fintype.card (↥S → R) : ℝ)⁻¹ * ∑ ρ', g ρ' + lam ≤ g ρ)) := by
    intro ρ hρ
    rw [Finset.mem_filter] at hρ ⊢
    exact ⟨Finset.mem_univ _, by linarith [hρ.2, hmean_le]⟩
  have hmcd := fact_mcd g (fun _ : ↥S => (Fintype.card K * t : ℝ)⁻¹)
    (fun i v v' hagree => gT_bdd_diff T t ht i v v' (fun j hj => hagree j hj)) hlam
  have hcardS : Fintype.card (↥S) = Fintype.card K * t := by
    rw [Fintype.card_coe, hSdef, Finset.card_product, Finset.card_univ, ht]
  have ht0 : (t : ℝ) ≠ 0 := by
    have ht0' : (0:ℕ) < t := ht1
    exact_mod_cast ht0'.ne'
  have hKpos : 0 < Fintype.card K := Fintype.card_pos
  have hKne : (Fintype.card K : ℝ) ≠ 0 := by exact_mod_cast hKpos.ne'
  have hcard_eq : (Fintype.card (↥S) : ℝ) = (Fintype.card K : ℝ) * t := by
    rw [hcardS]; push_cast; ring
  have hsumsq : ∑ _i : ↥S, ((Fintype.card K * t : ℝ)⁻¹) ^ 2 = ((Fintype.card K : ℝ) * t)⁻¹ := by
    rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, hcard_eq]
    have hKt_ne : (Fintype.card K : ℝ) * t ≠ 0 := mul_ne_zero hKne ht0
    field_simp
  rw [hratio_eq]
  calc ((Finset.univ.filter
        (fun ρ : ↥S → R => lam + (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t) < g ρ)).card
        : ℝ) / Fintype.card (↥S → R)
      ≤ ((Finset.univ.filter
        (fun ρ : ↥S → R => (Fintype.card (↥S → R) : ℝ)⁻¹ * ∑ ρ', g ρ' + lam ≤ g ρ)).card : ℝ) /
        Fintype.card (↥S → R) := by
        gcongr
    _ ≤ Real.exp (-(2 * lam ^ 2) / ∑ _i : ↥S, ((Fintype.card K * t : ℝ)⁻¹) ^ 2) := hmcd
    _ = Real.exp (-2 * lam ^ 2 * ((Fintype.card K : ℝ) * t)) := by
        rw [hsumsq]
        congr 1
        rw [div_eq_mul_inv, inv_inv]
        ring

/-- **Lemma (uniform deviation), part (i) only** (part (ii) feeds only the unused
`eq:main-sharp`). Bounds `E_H[W₁⁺]`, combining `fact_mcd` (applied to the sub-table on `K × T` via
`restrict_average`'s "restricting a uniform table is still uniform" counting argument),
`lemma_mean`'s centering, `fact_binom` for the union bound over supports of every size, and
`fact_tail_integrate` for the final tail-to-expectation step. -/
theorem lemma_unif :
    (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H : Table K D R, max (W1 K D R H) 0 ≤
      (6 / 5) * Real.sqrt (aConst D / Fintype.card K) := by
  set Y : Table K D R → ℝ := fun H => max (W1 K D R H) 0 with hYdef
  have hY0 : ∀ H, 0 ≤ Y H := fun H => le_max_right _ _
  have hY1 : ∀ H, Y H ≤ 1 := by
    intro H
    apply max_le _ (by norm_num)
    apply Finset.sup'_le
    intro t _
    have hphi := Phi_le_one H t
    have hnn : (0:ℝ) ≤ (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) := by positivity
    linarith
  have ha1 : 1 ≤ aConst D := by
    have hD1 : (1:ℝ) ≤ (Fintype.card D : ℝ) := by
      have := Fintype.card_pos (α := D); exact_mod_cast this
    have hlog : 0 ≤ Real.log (Fintype.card D : ℝ) := Real.log_nonneg hD1
    unfold aConst
    linarith
  have hK1 : (1:ℝ) ≤ (Fintype.card K : ℝ) := by
    have := Fintype.card_pos (α := K); exact_mod_cast this
  have hcard_table_pos : (0:ℝ) < (Fintype.card (Table K D R):ℝ) := by
    have := Fintype.card_pos (α := Table K D R); exact_mod_cast this
  have hKcard_pos : (0:ℝ) < (Fintype.card K:ℝ) := by
    have := Fintype.card_pos (α := K); exact_mod_cast this
  have htail : ∀ u : ℝ, 0 < u →
      ((Finset.univ.filter
          (fun H => Real.sqrt ((aConst D + u) / (2 * Fintype.card K)) < Y H)).card : ℝ)
        / Fintype.card (Table K D R) ≤ Real.exp (-u) / (1 - Real.exp (-u)) := by
    intro u hu
    set lam : ℝ := Real.sqrt ((aConst D + u) / (2 * Fintype.card K)) with hlamdef
    have hlam_pos : 0 < lam := by
      rw [hlamdef]
      exact Real.sqrt_pos.mpr (div_pos (by linarith [ha1]) (by positivity))
    have hlamsq2 : 2 * lam ^ 2 * (Fintype.card K : ℝ) = aConst D + u := by
      have hKne : (Fintype.card K:ℝ) ≠ 0 := hKcard_pos.ne'
      have hlamsq : lam ^ 2 = (aConst D + u) / (2 * (Fintype.card K:ℝ)) := by
        rw [hlamdef]
        exact Real.sq_sqrt (div_nonneg (by linarith [ha1, hu]) (by positivity))
      rw [hlamsq]
      field_simp
    have hYW1 : ∀ H, lam < Y H → lam < W1 K D R H := by
      intro H h
      rcases lt_max_iff.mp h with h1 | h2
      · exact h1
      · linarith
    have hstep1 : (Finset.univ.filter (fun H : Table K D R => lam < Y H)).card ≤
        ∑ t ∈ Finset.Icc 1 (Fintype.card D),
          (Finset.univ.filter
            (fun H => lam < Phi K D R H t - (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t))).card := by
      have hsub : (Finset.univ.filter (fun H : Table K D R => lam < Y H)) ⊆
          (Finset.Icc 1 (Fintype.card D)).biUnion
            (fun t => Finset.univ.filter
              (fun H => lam < Phi K D R H t - (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t))) := by
        intro H hH
        rw [Finset.mem_filter] at hH
        have hW1 : lam < W1 K D R H := hYW1 H hH.2
        unfold W1 at hW1
        rw [Finset.lt_sup'_iff] at hW1
        obtain ⟨t, htmem, hlt⟩ := hW1
        exact Finset.mem_biUnion.mpr ⟨t, htmem, Finset.mem_filter.mpr ⟨Finset.mem_univ H, hlt⟩⟩
      calc (Finset.univ.filter (fun H : Table K D R => lam < Y H)).card
          ≤ _ := Finset.card_le_card hsub
        _ ≤ _ := Finset.card_biUnion_le
    have hstep2 : ∀ t ∈ Finset.Icc 1 (Fintype.card D),
        (Finset.univ.filter
          (fun H => lam < Phi K D R H t - (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t))).card ≤
        ∑ T ∈ Finset.univ.filter (fun T : Finset D => T.card = t),
          (Finset.univ.filter
            (fun H =>
              lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card := by
      intro t _
      have hsub : (Finset.univ.filter
          (fun H => lam < Phi K D R H t - (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t))) ⊆
          (Finset.univ.filter (fun T : Finset D => T.card = t)).biUnion
            (fun T => Finset.univ.filter
              (fun H =>
                lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)) := by
        intro H hH
        rw [Finset.mem_filter] at hH
        have hlt' : lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Phi K D R H t := by
          linarith [hH.2]
        unfold Phi at hlt'
        by_cases hne : (Finset.univ.filter (fun T : Finset D => T.card = t)).Nonempty
        · rw [dif_pos hne, Finset.lt_sup'_iff] at hlt'
          obtain ⟨T, hTmem, hTlt⟩ := hlt'
          exact Finset.mem_biUnion.mpr ⟨T, hTmem, Finset.mem_filter.mpr ⟨Finset.mem_univ H, hTlt⟩⟩
        · rw [dif_neg hne] at hlt'
          exfalso
          have hnn : (0:ℝ) ≤ (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) := by positivity
          linarith
      calc (Finset.univ.filter
            (fun H => lam < Phi K D R H t - (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t))).card
          ≤ _ := Finset.card_le_card hsub
        _ ≤ _ := Finset.card_biUnion_le
    have hstep3 : ∀ t ∈ Finset.Icc 1 (Fintype.card D),
        (∑ T ∈ Finset.univ.filter (fun T : Finset D => T.card = t),
          (Finset.univ.filter
            (fun H =>
              lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card : ℝ)
          ≤ (Fintype.card (Table K D R):ℝ) * Real.exp (-(t:ℝ) * u) := by
      intro t htmem
      rw [Finset.mem_Icc] at htmem
      obtain ⟨ht1, htD⟩ := htmem
      have hperT : ∀ T ∈ Finset.univ.filter (fun T : Finset D => T.card = t),
          ((Finset.univ.filter
            (fun H =>
              lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card : ℝ)
            ≤ (Fintype.card (Table K D R):ℝ) *
                Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) := by
        intro T hT
        rw [Finset.mem_filter] at hT
        have hbound :
            ((Finset.univ.filter
                (fun H : Table K D R =>
                  lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card : ℝ) /
              Fintype.card (Table K D R) ≤
              Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) :=
          Fdist_tail_bound T t hT.2 ht1 lam hlam_pos
        rw [div_le_iff₀ hcard_table_pos] at hbound
        calc ((Finset.univ.filter
              (fun H =>
                lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card : ℝ)
            ≤ Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) *
                (Fintype.card (Table K D R):ℝ) := hbound
          _ = (Fintype.card (Table K D R):ℝ) *
                Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) := mul_comm _ _
      calc (∑ T ∈ Finset.univ.filter (fun T : Finset D => T.card = t),
              ((Finset.univ.filter
                (fun H =>
                  lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card : ℝ))
          ≤ ∑ T ∈ Finset.univ.filter (fun T : Finset D => T.card = t),
              (Fintype.card (Table K D R):ℝ) *
                Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) :=
            Finset.sum_le_sum hperT
        _ = ((Finset.univ.filter (fun T : Finset D => T.card = t)).card : ℝ) *
              ((Fintype.card (Table K D R):ℝ) *
                Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t))) := by
            rw [Finset.sum_const, nsmul_eq_mul]
        _ = ((Fintype.card D).choose t : ℝ) *
              ((Fintype.card (Table K D R):ℝ) *
                Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t))) := by
            rw [card_filter_card_eq_choose t]
        _ ≤ Real.exp ((t:ℝ) * aConst D) *
              ((Fintype.card (Table K D R):ℝ) *
                Real.exp (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t))) := by
            apply mul_le_mul_of_nonneg_right (choose_exp_bound t ht1 htD)
            positivity
        _ = (Fintype.card (Table K D R):ℝ) * Real.exp (-(t:ℝ) * u) := by
            have hexp_key : (t:ℝ) * aConst D + (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) =
                -(t:ℝ) * u := by
              have hrw : (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) =
                  -(2 * lam ^ 2 * (Fintype.card K:ℝ)) * t := by ring
              rw [hrw, hlamsq2]
              ring
            rw [show -(t:ℝ) * u =
                  (t:ℝ) * aConst D + (-2 * lam ^ 2 * ((Fintype.card K:ℝ) * t)) from
                  hexp_key.symm, Real.exp_add]
            ring
    have hstep1R : ((Finset.univ.filter (fun H : Table K D R => lam < Y H)).card:ℝ) ≤
        ∑ t ∈ Finset.Icc 1 (Fintype.card D),
          ((Finset.univ.filter
            (fun H =>
              lam < Phi K D R H t - (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t))).card:ℝ) := by
      exact_mod_cast hstep1
    have hcombine1 : ((Finset.univ.filter (fun H : Table K D R => lam < Y H)).card:ℝ) ≤
        ∑ t ∈ Finset.Icc 1 (Fintype.card D),
          ∑ T ∈ Finset.univ.filter (fun T : Finset D => T.card = t),
            ((Finset.univ.filter
              (fun H =>
                lam + (1/2) * Real.sqrt ((Fintype.card R:ℝ) / t) < Fdist K D R H T)).card
              : ℝ) := by
      refine hstep1R.trans (Finset.sum_le_sum (fun t htmem => ?_))
      exact_mod_cast hstep2 t htmem
    have hcombine2 : ((Finset.univ.filter (fun H : Table K D R => lam < Y H)).card:ℝ) ≤
        ∑ t ∈ Finset.Icc 1 (Fintype.card D),
          (Fintype.card (Table K D R):ℝ) * Real.exp (-(t:ℝ) * u) :=
      hcombine1.trans (Finset.sum_le_sum hstep3)
    have hcombine3 : ((Finset.univ.filter (fun H : Table K D R => lam < Y H)).card:ℝ) ≤
        (Fintype.card (Table K D R):ℝ) *
          ∑ t ∈ Finset.Icc 1 (Fintype.card D), Real.exp (-(t:ℝ) * u) := by
      rw [Finset.mul_sum]
      exact hcombine2
    have hr0 : (0:ℝ) ≤ Real.exp (-u) := (Real.exp_pos _).le
    have hr1 : Real.exp (-u) < 1 := by
      rw [show (1:ℝ) = Real.exp 0 from Real.exp_zero.symm]
      exact Real.exp_lt_exp.mpr (by linarith)
    have hgeom : ∑ t ∈ Finset.Icc 1 (Fintype.card D), Real.exp (-(t:ℝ) * u) ≤
        Real.exp (-u) / (1 - Real.exp (-u)) := by
      have heqpow : ∀ t : ℕ, Real.exp (-(t:ℝ) * u) = (Real.exp (-u)) ^ t := by
        intro t
        rw [show -(t:ℝ) * u = (t:ℝ) * (-u) from by ring]
        exact Real.exp_nat_mul (-u) t
      simp_rw [heqpow]
      exact geom_sum_Icc_one_le hr0 hr1 (Fintype.card D)
    have hcombine4 : ((Finset.univ.filter (fun H : Table K D R => lam < Y H)).card:ℝ) ≤
        (Fintype.card (Table K D R):ℝ) * (Real.exp (-u) / (1 - Real.exp (-u))) :=
      hcombine3.trans (mul_le_mul_of_nonneg_left hgeom (by positivity))
    rw [div_le_iff₀ hcard_table_pos, mul_comm]
    exact hcombine4
  exact fact_tail_integrate Y hY0 hY1 (aConst D) (Fintype.card K : ℝ) ha1 hK1 htail

end Unif

section Assemble

/-- For `y ≥ 1`, `⌊y⌋₊ ≥ y/2` (the standard "floor loses at most half" bound). -/
theorem floor_half_le {y : ℝ} (hy : 1 ≤ y) : y / 2 ≤ (⌊y⌋₊ : ℝ) := by
  have h1 : (1 : ℝ) ≤ (⌊y⌋₊ : ℝ) := by
    have h1' : 1 ≤ ⌊y⌋₊ := Nat.le_floor (by exact_mod_cast hy)
    exact_mod_cast h1'
  have h2 : y - 1 < (⌊y⌋₊ : ℝ) := by
    have := Nat.lt_floor_add_one y
    linarith
  rcases le_total 2 y with hy2 | hy2
  · linarith
  · linarith

/-- The mode of `p^{H,z}` is at least the average `1/|D|` (pigeonhole): the sup of a nonnegative
family summing to `1` cannot sit below the mean. Needed only for the `D = 1` case of the final
corollary (an `ε`-unpredictable source forces `ε ≥ 1/D`, hence `ε = 1` when `D = 1`). -/
theorem epsHz_ge_inv_card (S : Source K D R) (H : Table K D R) (z : Aux)
    (hpos : 0 < margZ S H z) : (Fintype.card D : ℝ)⁻¹ ≤ epsHz S H z := by
  have hsum1 : ∑ x, condX S H z x = 1 := by
    unfold condX
    rw [← Finset.sum_div]
    exact div_self hpos.ne'
  by_contra hc
  push_neg at hc
  have hlt : ∀ x, condX S H z x < (Fintype.card D : ℝ)⁻¹ := fun x =>
    lt_of_le_of_lt (Finset.le_sup' (condX S H z) (Finset.mem_univ x)) hc
  have hsum_lt := Finset.sum_lt_sum_of_nonempty (Finset.univ_nonempty (α := D)) (fun x _ => hlt x)
  rw [hsum1] at hsum_lt
  have hDpos : (0 : ℝ) < Fintype.card D := by
    have := Fintype.card_pos (α := D); exact_mod_cast this
  rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_inv_cancel₀ hDpos.ne'] at hsum_lt
  exact absurd hsum_lt (lt_irrefl 1)

theorem margZ_nonneg (S : Source K D R) (H : Table K D R) (z : Aux) : 0 ≤ margZ S H z :=
  Finset.sum_nonneg (fun x _ => ENNReal.toReal_nonneg)

/-- Swapping a `tsum` with an inner `Finset.sum` (needed below since `margZ` is itself a `Finset`
sum over `x : D` inside a `tsum` over `z : Aux`) — not on Mathlib's shelf under this shape, but a
short induction on the finset via `Finset.cons_induction` and `Summable.tsum_add`. -/
theorem tsum_finset_sum_comm {ι β M : Type*} [AddCommMonoid M] [TopologicalSpace M] [T2Space M]
    [ContinuousAdd M] (s : Finset ι) (f : ι → β → M) (hf : ∀ i ∈ s, Summable (f i)) :
    ∑' b, ∑ i ∈ s, f i b = ∑ i ∈ s, ∑' b, f i b := by
  induction s using Finset.cons_induction with
  | empty => simp
  | cons a s ha ih =>
    simp_rw [Finset.sum_cons]
    have hfa : Summable (f a) := hf a (Finset.mem_cons_self a s)
    have hfs : Summable (fun b => ∑ i ∈ s, f i b) := by
      apply summable_sum
      intro i hi
      exact hf i (Finset.mem_cons.mpr (Or.inr hi))
    rw [hfa.tsum_add hfs, ih (fun i hi => hf i (Finset.mem_cons.mpr (Or.inr hi)))]

/-- `Pr[Z = z | H]` sums to exactly `1` over `z`, for *every* `H` (not just on average): the
source's output `(X,Z)` is a genuine `PMF`, so marginalizing out `X` (a `Finset.sum`, `D` being
finite) and summing over `Z` (a `tsum`, `Aux` being merely countable) recovers the whole mass. -/
theorem margZ_tsum_one (S : Source K D R) (H : Table K D R) : ∑' z : Aux, margZ S H z = 1 := by
  have h1 : ∑' p : D × Aux, S H p = 1 := PMF.tsum_coe (S H)
  have h2 : ∑' p : D × Aux, S H p = ∑' x : D, ∑' z : Aux, S H (x, z) := ENNReal.tsum_prod'
  have h3 : ∑' x : D, ∑' z : Aux, S H (x, z) = ∑ x : D, ∑' z : Aux, S H (x, z) := tsum_fintype _
  have h4 : (∑ x : D, ∑' z : Aux, S H (x, z)) = 1 := by rw [← h3, ← h2, h1]
  have h5 : ∀ x : D, ∑' z : Aux, S H (x, z) ≠ ⊤ := by
    intro x
    have hle : ∑' z : Aux, S H (x, z) ≤ ∑' p : D × Aux, S H p := by
      apply ENNReal.tsum_comp_le_tsum_of_injective (f := fun z => (x, z))
      intro a b hab
      exact (Prod.mk.injEq .. ▸ hab).2
    rw [h1] at hle
    exact ne_top_of_le_ne_top ENNReal.one_ne_top hle
  have h6 : (∑ x : D, ∑' z : Aux, S H (x, z)).toReal = 1 := by rw [h4]; simp
  rw [ENNReal.toReal_sum (fun x _ => h5 x)] at h6
  have h7 : ∀ x : D, (∑' z : Aux, S H (x, z)).toReal = ∑' z : Aux, (S H (x, z)).toReal := by
    intro x
    exact ENNReal.tsum_toReal_eq (fun z => (S H).apply_ne_top _)
  simp_rw [h7] at h6
  change ∑' z : Aux, ∑ x : D, sourceProb S H x z = 1
  rw [← h6]
  exact tsum_finset_sum_comm Finset.univ (fun x z => (S H (x, z)).toReal)
    (fun x _ => ENNReal.summable_toReal (h5 x))

theorem margZ_summable (S : Source K D R) (H : Table K D R) : Summable (margZ S H) := by
  by_contra hns
  have h1 := margZ_tsum_one S H
  rw [tsum_eq_zero_of_not_summable hns] at h1
  norm_num at h1

/-- `eq:main-plain`'s first inequality (the only one `Corollary cor:pub` uses), for a single fixed
source, distinguisher and unpredictability bound. -/
theorem main_ineq (S : Source K D R) (Dist : PubDistinguisher K D R) {ε : ℝ}
    (hε0 : 0 < ε) (hε1 : ε ≤ 1) (hU : IsUnpredictable S ε) :
    extPubAdv S Dist ≤
      (1 / Real.sqrt 2) * Real.sqrt (ε * Fintype.card R) +
        (6 / 5) * Real.sqrt (aConst D / Fintype.card K) := by
  -- Step 1: reduce to bounding the mean deficiency-plus-selection.
  have step1 := extPubAdv_le_mean S Dist
  refine step1.trans ?_
  -- Step 2: the pointwise (margZ-weighted) bound.
  have hpt : ∀ H z, margZ S H z * DeltaHz S H z ≤
      margZ S H z * ((1 / Real.sqrt 2) * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)
        + max (W1 K D R H) 0) := by
    intro H z
    rcases (margZ_nonneg S H z).lt_or_eq with hzpos | hz0
    · apply mul_le_mul_of_nonneg_left ?_ hzpos.le
      have hcx0 : ∀ x, 0 ≤ condX S H z x := fun x =>
        div_nonneg ENNReal.toReal_nonneg hzpos.le
      have hcx1 : ∑ x, condX S H z x = 1 := by
        unfold condX; rw [← Finset.sum_div]; exact div_self hzpos.ne'
      have heps_pos : 0 < epsHz S H z := by
        by_contra hc
        push_neg at hc
        have hle0 : ∀ x, condX S H z x ≤ 0 := fun x =>
          le_trans (Finset.le_sup' (condX S H z) (Finset.mem_univ x)) hc
        have hnp : ∑ x : D, condX S H z x ≤ 0 :=
          Finset.sum_nonpos (fun x _ => hle0 x)
        rw [hcx1] at hnp; linarith
      have heps_le1 : epsHz S H z ≤ 1 := by
        apply Finset.sup'_le
        intro x _
        have hle : condX S H z x ≤ ∑ x' : D, condX S H z x' :=
          Finset.single_le_sum (fun x' _ => hcx0 x') (Finset.mem_univ x)
        rwa [hcx1] at hle
      have hinv_ge1 : (1 : ℝ) ≤ (epsHz S H z)⁻¹ := by
        rw [le_inv_comm₀ (by norm_num) heps_pos]
        simpa using heps_le1
      set t := ⌊(epsHz S H z)⁻¹⌋₊ with htdef
      have ht1 : 1 ≤ t := Nat.le_floor (by exact_mod_cast hinv_ge1)
      have htpos : (0 : ℝ) < (t : ℝ) := by
        have : 0 < t := ht1; exact_mod_cast this
      have hfloor := floor_half_le hinv_ge1
      rw [← htdef] at hfloor
      have ht_inv_le : (t : ℝ)⁻¹ ≤ 2 * epsHz S H z := by
        rw [inv_le_iff_one_le_mul₀ htpos]
        have h2 : (epsHz S H z)⁻¹ ≤ 2 * (t : ℝ) := by linarith
        calc (1 : ℝ) = epsHz S H z * (epsHz S H z)⁻¹ := by
              rw [mul_inv_cancel₀ heps_pos.ne']
          _ ≤ epsHz S H z * (2 * (t : ℝ)) :=
              mul_le_mul_of_nonneg_left h2 heps_pos.le
          _ = 2 * epsHz S H z * t := by ring
      have htD : t ≤ Fintype.card D := by
        have hb : (epsHz S H z)⁻¹ ≤ (Fintype.card D : ℝ) := by
          have hge := epsHz_ge_inv_card S H z hzpos
          have hDpos : (0 : ℝ) < Fintype.card D := by
            have := Fintype.card_pos (α := D); exact_mod_cast this
          rw [inv_le_comm₀ heps_pos hDpos]
          simpa using hge
        calc t ≤ ⌊(Fintype.card D : ℝ)⌋₊ := Nat.floor_mono hb
          _ = Fintype.card D := Nat.floor_natCast _
      have hflat := lemma_flat S H z hzpos
      have hphi_mem : t ∈ Finset.Icc 1 (Fintype.card D) := Finset.mem_Icc.mpr ⟨ht1, htD⟩
      have hphi_le : Phi K D R H t - (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / (t : ℝ))
          ≤ W1 K D R H :=
        Finset.le_sup' (fun t' => Phi K D R H t' - (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / t'))
          hphi_mem
      have hW1max : W1 K D R H ≤ max (W1 K D R H) 0 := le_max_left _ _
      have hRt : Real.sqrt ((Fintype.card R : ℝ) / (t : ℝ)) ≤
          Real.sqrt (2 * ((Fintype.card R : ℝ) * epsHz S H z)) := by
        apply Real.sqrt_le_sqrt
        rw [div_le_iff₀ htpos]
        have hRnn : (0:ℝ) ≤ (Fintype.card R : ℝ) := by positivity
        calc (Fintype.card R : ℝ) = (Fintype.card R : ℝ) * ((t:ℝ)⁻¹ * (t:ℝ)) := by
              rw [inv_mul_cancel₀ htpos.ne', mul_one]
          _ ≤ (Fintype.card R : ℝ) * ((2 * epsHz S H z) * (t:ℝ)) :=
              mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right ht_inv_le htpos.le) hRnn
          _ = 2 * ((Fintype.card R : ℝ) * epsHz S H z) * t := by ring
      have hsqrt2 : Real.sqrt (2 * ((Fintype.card R : ℝ) * epsHz S H z)) =
          Real.sqrt 2 * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) :=
        Real.sqrt_mul (by norm_num) _
      rw [hsqrt2] at hRt
      have hcomb : (1 / 2) * Real.sqrt ((Fintype.card R : ℝ) / (t : ℝ)) ≤
          (1 / Real.sqrt 2) * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) := by
        have hs2 : (1 : ℝ) / Real.sqrt 2 = Real.sqrt 2 / 2 := by
          rw [eq_div_iff (by norm_num : (2:ℝ) ≠ 0), div_mul_eq_mul_div, eq_comm,
            eq_div_iff (Real.sqrt_pos.mpr (by norm_num : (0:ℝ) < 2)).ne']
          rw [Real.mul_self_sqrt (by norm_num : (0:ℝ) ≤ 2)]
          ring
        have hstep : (1:ℝ)/2 * Real.sqrt ((Fintype.card R : ℝ) / (t : ℝ)) ≤
            1/2 * (Real.sqrt 2 * Real.sqrt ((Fintype.card R:ℝ) * epsHz S H z)) :=
          mul_le_mul_of_nonneg_left hRt (by norm_num)
        rw [hs2]
        linarith [hstep]
      linarith [hflat, hphi_le, hW1max, hcomb]
    · rw [← hz0, zero_mul, zero_mul]
  -- Universal facts about `DeltaHz`/`epsHz` needed for the summability bookkeeping below.
  have hDeltaHz_nonneg : ∀ H z, 0 ≤ DeltaHz S H z := by
    intro H z
    unfold DeltaHz DeltaOf
    apply mul_nonneg (by positivity)
    apply Finset.sum_nonneg
    intro k _
    unfold SD
    positivity
  have hepsHz_nonneg : ∀ H z, 0 ≤ epsHz S H z := by
    intro H z
    obtain ⟨x0, hx0⟩ := (Finset.univ_nonempty : (Finset.univ : Finset D).Nonempty)
    exact le_trans (div_nonneg ENNReal.toReal_nonneg (margZ_nonneg S H z))
      (Finset.le_sup' (condX S H z) hx0)
  have hepsHz_le_one : ∀ H z, epsHz S H z ≤ 1 := by
    intro H z
    rcases (margZ_nonneg S H z).lt_or_eq with hzpos | hz0
    · apply Finset.sup'_le
      intro x _
      have hcx0 : ∀ x, 0 ≤ condX S H z x := fun x => div_nonneg ENNReal.toReal_nonneg hzpos.le
      have hcx1 : ∑ x, condX S H z x = 1 := by
        unfold condX; rw [← Finset.sum_div]; exact div_self hzpos.ne'
      have hle : condX S H z x ≤ ∑ x' : D, condX S H z x' :=
        Finset.single_le_sum (fun x' _ => hcx0 x') (Finset.mem_univ x)
      rwa [hcx1] at hle
    · apply Finset.sup'_le
      intro x _
      have hz : condX S H z x = 0 := by unfold condX; rw [← hz0, div_zero]
      rw [hz]; norm_num
  have hR_pos : (0 : ℝ) < (Fintype.card R : ℝ) := by exact_mod_cast Fintype.card_pos (α := R)
  have hcard_ne : (Fintype.card (Table K D R) : ℝ) ≠ 0 := by
    have h := Fintype.card_pos (α := Table K D R)
    exact_mod_cast h.ne'
  -- Per-`H` tsum-splitting identity for an affine (in `z`) function, the core piece of
  -- bookkeeping reused by both the `hpt`-averaging step and the AM-GM step.
  have tsum_margZ_affine : ∀ (H : Table K D R) (f : Aux → ℝ) (a b : ℝ),
      Summable (fun z => margZ S H z * f z) →
      ∑' z, margZ S H z * (a * f z + b) = a * (∑' z, margZ S H z * f z) + b := by
    intro H f a b hf
    have heq : ∀ z, margZ S H z * (a * f z + b)
        = a * (margZ S H z * f z) + margZ S H z * b := by intro z; ring
    simp_rw [heq]
    rw [(hf.mul_left a).tsum_add ((margZ_summable S H).mul_right b), tsum_mul_left, tsum_mul_right,
      margZ_tsum_one S H, one_mul]
  -- Generic monotonicity of `expectHZ`, given the per-`H` inequality at the `tsum` level.
  have expectHZ_mono : ∀ (f g : Table K D R → Aux → ℝ),
      (∀ H, ∑' z, margZ S H z * f H z ≤ ∑' z, margZ S H z * g H z) →
      expectHZ S f ≤ expectHZ S g := by
    intro f g hle
    unfold expectHZ
    exact mul_le_mul_of_nonneg_left (Finset.sum_le_sum (fun H _ => hle H)) (by positivity)
  -- `expectHZ` of a genuinely constant-affine transform of `f` (`a`, `b` independent of `H`).
  have expectHZ_affine : ∀ (f : Table K D R → Aux → ℝ) (a b : ℝ),
      (∀ H, Summable (fun z => margZ S H z * f H z)) →
      expectHZ S (fun H z => a * f H z + b) = a * expectHZ S f + b := by
    intro f a b hfS
    unfold expectHZ
    have hstep : ∀ H, ∑' z, margZ S H z * (a * f H z + b)
        = a * (∑' z, margZ S H z * f H z) + b := fun H => tsum_margZ_affine H (f H) a b (hfS H)
    simp_rw [hstep]
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    have hTnb : (Fintype.card (Table K D R) : ℝ)⁻¹ *
        ((Fintype.card (Table K D R) : ℝ) * b) = b := by
      rw [← mul_assoc, inv_mul_cancel₀ hcard_ne, one_mul]
    rw [mul_add, hTnb]
    ring
  -- `expectHZ` of a constant multiple.
  have expectHZ_const_mul : ∀ (f : Table K D R → Aux → ℝ) (a : ℝ),
      expectHZ S (fun H z => a * f H z) = a * expectHZ S f := by
    intro f a
    unfold expectHZ
    have hstep : ∀ H, ∑' z, margZ S H z * (a * f H z) = a * ∑' z, margZ S H z * f H z := by
      intro H
      simp_rw [show ∀ z, margZ S H z * (a * f H z) = a * (margZ S H z * f H z) from
        fun z => by ring]
      exact tsum_mul_left
    simp_rw [hstep]
    rw [← Finset.mul_sum]
    ring
  -- Summability facts needed for the `tsum`s appearing in `hpt`'s average.
  have hf1_summable : ∀ H, Summable
      (fun z => margZ S H z * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) := by
    intro H
    refine Summable.of_nonneg_of_le (fun z => mul_nonneg (margZ_nonneg S H z) (Real.sqrt_nonneg _))
      (fun z => ?_) ((margZ_summable S H).mul_right (Real.sqrt (Fintype.card R : ℝ)))
    apply mul_le_mul_of_nonneg_left _ (margZ_nonneg S H z)
    apply Real.sqrt_le_sqrt
    calc (Fintype.card R : ℝ) * epsHz S H z ≤ (Fintype.card R : ℝ) * 1 :=
          mul_le_mul_of_nonneg_left (hepsHz_le_one H z) (by positivity)
      _ = (Fintype.card R : ℝ) := mul_one _
  have hf2_summable : ∀ H, Summable (fun z => margZ S H z * max (W1 K D R H) 0) :=
    fun H => (margZ_summable S H).mul_right _
  have heps_summable : ∀ H, Summable (fun z => margZ S H z * epsHz S H z) := by
    intro H
    refine Summable.of_nonneg_of_le (fun z => mul_nonneg (margZ_nonneg S H z) (hepsHz_nonneg H z))
      (fun z => ?_) (margZ_summable S H)
    calc margZ S H z * epsHz S H z ≤ margZ S H z * 1 :=
          mul_le_mul_of_nonneg_left (hepsHz_le_one H z) (margZ_nonneg S H z)
      _ = margZ S H z := mul_one _
  have hg_summable : ∀ H, Summable (fun z => margZ S H z *
      ((1 / Real.sqrt 2) * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)
        + max (W1 K D R H) 0)) := by
    intro H
    have heq : ∀ z, margZ S H z *
        ((1 / Real.sqrt 2) * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)
          + max (W1 K D R H) 0)
        = (1 / Real.sqrt 2) * (margZ S H z * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
          + margZ S H z * max (W1 K D R H) 0 := by intro z; ring
    simp_rw [heq]
    exact ((hf1_summable H).mul_left _).add (hf2_summable H)
  have hf_summable : ∀ H, Summable (fun z => margZ S H z * DeltaHz S H z) := by
    intro H
    exact Summable.of_nonneg_of_le (fun z => mul_nonneg (margZ_nonneg S H z) (hDeltaHz_nonneg H z))
      (fun z => hpt H z) (hg_summable H)
  -- Step A/B: average `hpt` over `z` (tsum) and `H` (Finset sum), landing exactly on
  -- `expectHZ`'s own shape for the "mean-deficiency" term and `lemma_unif`'s shape for the rest.
  have hA1 : ∀ H, ∑' z, margZ S H z * DeltaHz S H z ≤
      ∑' z, margZ S H z * ((1 / Real.sqrt 2) * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)
        + max (W1 K D R H) 0) :=
    fun H => (hf_summable H).tsum_le_tsum (fun z => hpt H z) (hg_summable H)
  have hA2 : ∀ H, ∑' z, margZ S H z * ((1 / Real.sqrt 2) *
        Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) + max (W1 K D R H) 0)
      = (1 / Real.sqrt 2) * (∑' z, margZ S H z * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
        + max (W1 K D R H) 0 :=
    fun H => tsum_margZ_affine H (fun z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
      (1 / Real.sqrt 2) (max (W1 K D R H) 0) (hf1_summable H)
  have stepB : expectHZ S (DeltaHz S) ≤
      (1 / Real.sqrt 2) * expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
        + (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H, max (W1 K D R H) 0 := by
    have hmono : expectHZ S (DeltaHz S) ≤
        expectHZ S (fun H z => (1 / Real.sqrt 2) *
          Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) + max (W1 K D R H) 0) :=
      expectHZ_mono (DeltaHz S) _ hA1
    refine hmono.trans (le_of_eq ?_)
    unfold expectHZ
    simp_rw [hA2]
    rw [Finset.sum_add_distrib, ← Finset.mul_sum, mul_add]
    ring
  -- Step C: AM-GM bound on the mean-deficiency term (deliberately avoiding Jensen).
  set c : ℝ := Real.sqrt (ε * (Fintype.card R : ℝ)) with hc_def
  have hRε_pos : (0 : ℝ) < ε * (Fintype.card R : ℝ) := mul_pos hε0 hR_pos
  have hc_pos : 0 < c := by rw [hc_def]; exact Real.sqrt_pos.mpr hRε_pos
  have hc_sq : c ^ 2 = ε * (Fintype.card R : ℝ) := by rw [hc_def]; exact Real.sq_sqrt hRε_pos.le
  have h2c_pos : (0 : ℝ) < 2 * c := by linarith
  have hcore_pt : ∀ H z, 2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) ≤
      (Fintype.card R : ℝ) * epsHz S H z + c ^ 2 := by
    intro H z
    have hx0 : (0 : ℝ) ≤ (Fintype.card R : ℝ) * epsHz S H z :=
      mul_nonneg hR_pos.le (hepsHz_nonneg H z)
    have hsqx : Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) ^ 2
        = (Fintype.card R : ℝ) * epsHz S H z := Real.sq_sqrt hx0
    nlinarith [sq_nonneg (Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z) - c), hsqx]
  have hC1 : ∀ H, ∑' z, margZ S H z *
        (2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) ≤
      ∑' z, margZ S H z * ((Fintype.card R : ℝ) * epsHz S H z + c ^ 2) := by
    intro H
    have hL : Summable (fun z => margZ S H z *
        (2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))) := by
      have heq : ∀ z, margZ S H z * (2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
          = 2 * c * (margZ S H z * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) := by
        intro z; ring
      simp_rw [heq]
      exact (hf1_summable H).mul_left _
    have hRsum : Summable (fun z => margZ S H z *
        ((Fintype.card R : ℝ) * epsHz S H z + c ^ 2)) := by
      have heq : ∀ z, margZ S H z * ((Fintype.card R : ℝ) * epsHz S H z + c ^ 2)
          = (Fintype.card R : ℝ) * (margZ S H z * epsHz S H z) + margZ S H z * c ^ 2 := by
        intro z; ring
      simp_rw [heq]
      exact ((heps_summable H).mul_left _).add ((margZ_summable S H).mul_right _)
    exact hL.tsum_le_tsum (fun z => mul_le_mul_of_nonneg_left (hcore_pt H z) (margZ_nonneg S H z))
      hRsum
  have hCmono : expectHZ S (fun H z => 2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) ≤
      expectHZ S (fun H z => (Fintype.card R : ℝ) * epsHz S H z + c ^ 2) :=
    expectHZ_mono _ _ hC1
  have hCmono_lhs : expectHZ S (fun H z => 2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
      = 2 * c * expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) :=
    expectHZ_const_mul (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) (2 * c)
  have hCmono_rhs : expectHZ S (fun H z => (Fintype.card R : ℝ) * epsHz S H z + c ^ 2)
      = (Fintype.card R : ℝ) * expectHZ S (epsHz S) + c ^ 2 :=
    expectHZ_affine (epsHz S) (Fintype.card R : ℝ) (c ^ 2) heps_summable
  have stepC0 : 2 * c * expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) ≤
      (Fintype.card R : ℝ) * expectHZ S (epsHz S) + c ^ 2 := by
    calc 2 * c * expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
        = expectHZ S (fun H z => 2 * c * Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) :=
          hCmono_lhs.symm
      _ ≤ expectHZ S (fun H z => (Fintype.card R : ℝ) * epsHz S H z + c ^ 2) := hCmono
      _ = (Fintype.card R : ℝ) * expectHZ S (epsHz S) + c ^ 2 := hCmono_rhs
  have stepC1 : (Fintype.card R : ℝ) * expectHZ S (epsHz S) + c ^ 2 ≤
      (Fintype.card R : ℝ) * ε + c ^ 2 := by
    have := mul_le_mul_of_nonneg_left (expectHZ_epsHz_le S hU) hR_pos.le
    linarith [this]
  have stepC2 : 2 * c * expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
      ≤ (2 * c) * c := by
    have heq : (Fintype.card R : ℝ) * ε + c ^ 2 = (2 * c) * c := by
      have hexp : (2 * c) * c = 2 * c ^ 2 := by ring
      rw [hexp, hc_sq]; ring
    linarith [stepC0, stepC1, heq]
  have stepC : expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z)) ≤ c :=
    le_of_mul_le_mul_left stepC2 h2c_pos
  -- Combine: `stepB` bounds `expectHZ S (DeltaHz S)`, `stepC` handles its first summand via
  -- AM-GM, and `lemma_unif` handles its second summand directly.
  calc expectHZ S (DeltaHz S)
      ≤ (1 / Real.sqrt 2) * expectHZ S (fun H z => Real.sqrt ((Fintype.card R : ℝ) * epsHz S H z))
          + (Fintype.card (Table K D R) : ℝ)⁻¹ * ∑ H, max (W1 K D R H) 0 := stepB
    _ ≤ (1 / Real.sqrt 2) * c + (6 / 5) * Real.sqrt (aConst D / Fintype.card K) :=
        add_le_add (mul_le_mul_of_nonneg_left stepC (by positivity)) lemma_unif

/-- **Corollary (public-seed conjecture).** `PublicSeedConjecture` holds, via `main_ineq` and a
term-by-term real-analysis comparison against `publicBound` (case-split on `Fintype.card D = 1`
vs. `≥ 2`) — not necessarily with the paper's optimal constants, just some constant that falls out
simply, since `PublicSeedConjecture` only asks for *some* `c > 0`. -/
theorem publicSeedConjecture_holds : PublicSeedConjecture := by
  set c : ℝ := (1 / Real.sqrt 2 + 6 / 5) + (6 / 5) * Real.sqrt (1 + Real.log 2) with hc_def
  refine ⟨c, ?_, ?_⟩
  · rw [hc_def]; positivity
  · intro K D R _ _ _ _ _ _ _ _ ε S Dist hε0 hε1 hU
    refine (main_ineq S Dist hε0 hε1 hU).trans ?_
    change (1 / Real.sqrt 2) * Real.sqrt (ε * (Fintype.card R : ℝ)) +
          (6 / 5) * Real.sqrt ((1 + Real.log (Fintype.card D : ℝ)) / (Fintype.card K : ℝ)) ≤
        c * (Real.sqrt (ε * (Fintype.card R : ℝ)) +
          Real.sqrt (Real.logb 2 (Fintype.card D : ℝ) / (Fintype.card K : ℝ)))
    have hK₀pos : (0 : ℝ) < (Fintype.card K : ℝ) := by exact_mod_cast Fintype.card_pos (α := K)
    have hR₀pos : (0 : ℝ) < (Fintype.card R : ℝ) := by exact_mod_cast Fintype.card_pos (α := R)
    have hK1 : 1 ≤ Fintype.card K := by have h := Fintype.card_pos (α := K); omega
    have hR1 : 1 ≤ Fintype.card R := by have h := Fintype.card_pos (α := R); omega
    have hD1n' : 1 ≤ Fintype.card D := by have h := Fintype.card_pos (α := D); omega
    have hK₀ge1 : (1 : ℝ) ≤ (Fintype.card K : ℝ) := by exact_mod_cast hK1
    have hR₀ge1 : (1 : ℝ) ≤ (Fintype.card R : ℝ) := by exact_mod_cast hR1
    have hc1_le_c : (1 / Real.sqrt 2 + 6 / 5 : ℝ) ≤ c := by
      rw [hc_def]
      have h2 : (0 : ℝ) ≤ (6 / 5) * Real.sqrt (1 + Real.log 2) := by positivity
      linarith
    have hc2_le_c : ((6 / 5) * Real.sqrt (1 + Real.log 2) : ℝ) ≤ c := by
      rw [hc_def]
      have h1 : (0 : ℝ) ≤ 1 / Real.sqrt 2 + 6 / 5 := by positivity
      linarith
    rcases hD1n'.eq_or_lt with hD1 | hD2
    · -- Case: Fintype.card D = 1. Every predictor guesses right, so `ε ≥ 1`.
      have hD1' : Fintype.card D = 1 := hD1.symm
      have hD₀eq1 : (Fintype.card D : ℝ) = 1 := by exact_mod_cast hD1'
      obtain ⟨x₀, hx₀⟩ := Fintype.card_eq_one_iff.mp hD1'
      obtain ⟨P₀, hP₀_def⟩ : ∃ P₀ : Predictor K D R, ∀ H z, P₀ H z = PMF.pure x₀ :=
        ⟨fun _ _ => PMF.pure x₀, fun _ _ => rfl⟩
      have hcollapse : ∀ (H : Table K D R) (p : D × Aux),
          (P₀ H p.2).bind (fun x' => PMF.pure (decide (p.1 = x'))) = PMF.pure true := by
        intro H p
        rw [hP₀_def, PMF.pure_bind]
        congr 1
        simp [hx₀ p.1]
      have hbridge : predGame S P₀ = (PMF.uniformOfFintype (Table K D R)).bind (fun H =>
          (S H).bind (fun p => (P₀ H p.2).bind (fun x' => PMF.pure (decide (p.1 = x'))))) := rfl
      have hSbind : ∀ H : Table K D R,
          (S H).bind (fun p => (P₀ H p.2).bind (fun x' => PMF.pure (decide (p.1 = x')))) =
            PMF.pure true := by
        intro H
        simp_rw [hcollapse H]
        exact PMF.bind_const (S H) (PMF.pure true)
      have hfull : predGame S P₀ = PMF.pure true := by
        rw [hbridge]
        simp_rw [hSbind]
        exact PMF.bind_const _ (PMF.pure true)
      have hpredAdv1 : predAdv S P₀ = 1 := by
        unfold predAdv
        rw [hfull, PMF.pure_apply_self]
        simp
      have hge1 : (1 : ℝ) ≤ ε := by
        have h := hU P₀
        rwa [hpredAdv1] at h
      rw [hD₀eq1]
      simp only [Real.log_one, Real.logb_one, zero_div, add_zero, Real.sqrt_zero]
      have h1overK_le_one : (1 : ℝ) / (Fintype.card K : ℝ) ≤ 1 := by
        rw [div_le_one hK₀pos]; exact hK₀ge1
      have hab : (1 : ℝ) ≤ ε * (Fintype.card R : ℝ) := by
        nlinarith [mul_le_mul hge1 hR₀ge1 zero_le_one hε0.le]
      have hstep_arg : (1 : ℝ) / (Fintype.card K : ℝ) ≤ ε * (Fintype.card R : ℝ) :=
        le_trans h1overK_le_one hab
      have hstep : Real.sqrt ((1 : ℝ) / (Fintype.card K : ℝ)) ≤
          Real.sqrt (ε * (Fintype.card R : ℝ)) :=
        Real.sqrt_le_sqrt hstep_arg
      have hkey_case1 : (1 / Real.sqrt 2 + 6 / 5 : ℝ) * Real.sqrt (ε * (Fintype.card R : ℝ)) ≤
          c * Real.sqrt (ε * (Fintype.card R : ℝ)) :=
        mul_le_mul_of_nonneg_right hc1_le_c (Real.sqrt_nonneg _)
      nlinarith [hstep, hkey_case1]
    · -- Case: 2 ≤ Fintype.card D.
      have hD2n : 2 ≤ Fintype.card D := by omega
      have hD2R : (2 : ℝ) ≤ (Fintype.card D : ℝ) := by exact_mod_cast hD2n
      have hl2pos : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
      have hlog2_nonneg : (0 : ℝ) ≤ Real.log 2 := hl2pos.le
      have hLge : Real.log 2 ≤ Real.log (Fintype.card D : ℝ) :=
        Real.log_le_log (by norm_num) hD2R
      have hlogb_eq :
          Real.logb 2 (Fintype.card D : ℝ) = Real.log (Fintype.card D : ℝ) / Real.log 2 :=
        (Real.log_div_log).symm
      have hkey2 : (1 + Real.log (Fintype.card D : ℝ)) ≤
          (1 + Real.log 2) * Real.logb 2 (Fintype.card D : ℝ) := by
        rw [hlogb_eq, mul_div_assoc', le_div_iff₀ hl2pos]
        nlinarith [hLge]
      have hstepD : Real.sqrt (1 + Real.log (Fintype.card D : ℝ)) ≤
          Real.sqrt (1 + Real.log 2) * Real.sqrt (Real.logb 2 (Fintype.card D : ℝ)) := by
        rw [← Real.sqrt_mul (show (0 : ℝ) ≤ 1 + Real.log 2 by linarith [hlog2_nonneg])]
        exact Real.sqrt_le_sqrt hkey2
      have hstepDK : Real.sqrt ((1 + Real.log (Fintype.card D : ℝ)) / (Fintype.card K : ℝ)) ≤
          Real.sqrt (1 + Real.log 2) *
            Real.sqrt (Real.logb 2 (Fintype.card D : ℝ) / (Fintype.card K : ℝ)) := by
        rw [Real.sqrt_div' _ hK₀pos.le, Real.sqrt_div' _ hK₀pos.le, mul_div_assoc',
          div_le_div_iff_of_pos_right (Real.sqrt_pos.mpr hK₀pos)]
        exact hstepD
      have hc_ge_inv_sqrt2 : (1 / Real.sqrt 2 : ℝ) ≤ c := by linarith [hc1_le_c]
      have hfact1 : (1 / Real.sqrt 2 : ℝ) * Real.sqrt (ε * (Fintype.card R : ℝ)) ≤
          c * Real.sqrt (ε * (Fintype.card R : ℝ)) :=
        mul_le_mul_of_nonneg_right hc_ge_inv_sqrt2 (Real.sqrt_nonneg _)
      have hfact2 : ((6 / 5 : ℝ) * Real.sqrt (1 + Real.log 2)) *
          Real.sqrt (Real.logb 2 (Fintype.card D : ℝ) / (Fintype.card K : ℝ)) ≤
          c * Real.sqrt (Real.logb 2 (Fintype.card D : ℝ) / (Fintype.card K : ℝ)) :=
        mul_le_mul_of_nonneg_right hc2_le_c (Real.sqrt_nonneg _)
      nlinarith [hstepDK, hfact1, hfact2,
        Real.sqrt_nonneg (Real.logb 2 (Fintype.card D : ℝ) / (Fintype.card K : ℝ))]

end Assemble

end Lhl.PublicSeed


