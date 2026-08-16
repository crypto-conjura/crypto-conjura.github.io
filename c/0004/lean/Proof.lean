/-
Toward a formal proof of `Conjura0004.lhl_public_seed`.

This file is a **partial** formalization. It is not the proof, and it does not
claim to be: `c/0004`'s `proof_formal` stays `open` until the main theorem
compiles with no `sorry` at all. See `LEDGER.md` for what is proved and what
is outstanding.

What is here is the bottom of the argument, proved rather than assumed. The
informal proof (`../latex/proof.tex`) opens by collecting seven "standard
facts" it borrows from outside itself. The first of those, Fact 2.1, is the
one everything else is phrased in terms of: the best advantage any unbounded
distinguisher can have between two distributions is their statistical
distance. Section 1 below proves it, in the finite setting, with no `sorry`.

Why this one first. `Statement.lean` defines the extraction advantage
operationally, as a game an adversary plays. Every later step of the informal
proof works with an analytic quantity instead, a sum over rows of a
statistical distance. Fact 2.1 is the bridge between the two, so nothing
above it can be formalized until it is.
-/
import Statement
import Mathlib.Analysis.MeanInequalities

namespace Conjura0004

open scoped ENNReal BigOperators

/-! ## 1. Statistical distance, and the optimal distinguisher

Everything is finite, so statistical distance is defined directly as half the
l1 distance between two mass functions, in `ℝ`, with no measure theory. -/

section SD

variable {Ω : Type} [Fintype Ω]

/-- The mass a `PMF` puts on a point, as a real number. Finite everywhere, so
nothing is lost against the `ℝ≥0∞`-valued `p ω`. -/
noncomputable def rmass (p : PMF Ω) (ω : Ω) : ℝ := (p ω).toReal

omit [Fintype Ω] in
lemma rmass_nonneg (p : PMF Ω) (ω : Ω) : 0 ≤ rmass p ω := ENNReal.toReal_nonneg

omit [Fintype Ω] in
lemma rmass_le_one (p : PMF Ω) (ω : Ω) : rmass p ω ≤ 1 := by
  show (p ω).toReal ≤ 1
  simpa using ENNReal.toReal_mono (by simp) (p.coe_le_one ω)

/-- A `PMF` on a finite type has total real mass one. -/
lemma sum_rmass (p : PMF Ω) : ∑ ω, rmass p ω = 1 := by
  have h : ∑ ω, p ω = 1 := by
    have := p.tsum_coe
    rwa [tsum_fintype] at this
  have := congrArg ENNReal.toReal h
  rwa [ENNReal.toReal_sum (fun ω _ => p.apply_ne_top ω), ENNReal.toReal_one] at this

/-- Statistical distance: half the l1 distance between the two mass
functions. -/
noncomputable def SD (P Q : PMF Ω) : ℝ := (1 / 2) * ∑ ω, |rmass P ω - rmass Q ω|

lemma SD_nonneg (P Q : PMF Ω) : 0 ≤ SD P Q := by
  apply mul_nonneg (by norm_num)
  exact Finset.sum_nonneg fun ω _ => abs_nonneg _

lemma SD_comm (P Q : PMF Ω) : SD P Q = SD Q P := by
  unfold SD
  congr 1
  exact Finset.sum_congr rfl fun ω _ => abs_sub_comm _ _

lemma SD_self (P : PMF Ω) : SD P P = 0 := by simp [SD]

lemma SD_le_one (P Q : PMF Ω) : SD P Q ≤ 1 := by
  have h : ∀ ω : Ω, |rmass P ω - rmass Q ω| ≤ rmass P ω + rmass Q ω := by
    intro ω
    rw [abs_sub_le_iff]
    constructor <;> linarith [rmass_nonneg P ω, rmass_nonneg Q ω]
  have := Finset.sum_le_sum (fun ω (_ : ω ∈ Finset.univ) => h ω)
  rw [Finset.sum_add_distrib, sum_rmass, sum_rmass] at this
  unfold SD
  linarith

/-- The positive part of the mass difference sums to the statistical distance.

This is the identity the optimal-distinguisher bound turns on: a
distinguisher can only collect the points where `Q` is heavier than `P`, and
because the two total masses agree, that half of the l1 distance is the whole
statistical distance. -/
lemma sum_pos_part_eq_SD (P Q : PMF Ω) :
    ∑ ω, max (rmass Q ω - rmass P ω) 0 = SD P Q := by
  have hzero : ∑ ω, (rmass Q ω - rmass P ω) = 0 := by
    rw [Finset.sum_sub_distrib, sum_rmass, sum_rmass, sub_self]
  have habs : ∀ ω : Ω,
      |rmass P ω - rmass Q ω|
        = max (rmass Q ω - rmass P ω) 0 + max (rmass P ω - rmass Q ω) 0 := by
    intro ω
    rcases le_total (rmass P ω) (rmass Q ω) with h | h
    · rw [abs_of_nonpos (by linarith), max_eq_left (by linarith),
        max_eq_right (by linarith)]
      ring
    · rw [abs_of_nonneg (by linarith), max_eq_right (by linarith),
        max_eq_left (by linarith)]
      ring
  -- pos and neg parts differ by the (zero) signed sum
  have hsplit : ∀ ω : Ω,
      max (rmass P ω - rmass Q ω) 0
        = max (rmass Q ω - rmass P ω) 0 - (rmass Q ω - rmass P ω) := by
    intro ω
    rcases le_total (rmass P ω) (rmass Q ω) with h | h
    · rw [max_eq_right (by linarith), max_eq_left (by linarith)]; ring
    · rw [max_eq_left (by linarith), max_eq_right (by linarith)]; ring
  unfold SD
  rw [Finset.sum_congr rfl (fun ω _ => habs ω), Finset.sum_add_distrib,
    Finset.sum_congr rfl (fun ω _ => hsplit ω), Finset.sum_sub_distrib, hzero]
  ring

end SD

/-! ## 2. The distinguishing game

`Fact 2.1` of `../latex/proof.tex`: an unbounded distinguisher's advantage
between `P₀` and `P₁` is at most `SD P₀ P₁`. -/

section Distinguishing

variable {Ω : Type} [Fintype Ω]

/-- Sample a uniform bit `b`, then a point from `P₀` or `P₁` accordingly, hand
the point to `A`, and ask whether `A` recovered `b`. `A` is an arbitrary
function into `PMF Bool`: randomized, and subject to no complexity bound. -/
noncomputable def distGame (P₀ P₁ : PMF Ω) (A : Ω → PMF Bool) : PMF Bool :=
  (PMF.uniformOfFintype Bool).bind fun b =>
    (cond b P₁ P₀).bind fun ω =>
      (A ω).bind fun b' => PMF.pure (decide (b' = b))

/-- `2 Pr[A wins] - 1`, the same normalization `extAdv` uses. -/
noncomputable def distAdv (P₀ P₁ : PMF Ω) (A : Ω → PMF Bool) : ℝ :=
  2 * (distGame P₀ P₁ A true).toReal - 1

/-- The winning probability of the distinguishing game, written out.

Half the chance of calling a `P₀` sample "0", plus half the chance of calling
a `P₁` sample "1". -/
lemma distGame_apply_true (P₀ P₁ : PMF Ω) (A : Ω → PMF Bool) :
    distGame P₀ P₁ A true
      = (1 / 2) * (∑ ω, P₀ ω * (A ω) false) + (1 / 2) * (∑ ω, P₁ ω * (A ω) true) := by
  have inner : ∀ (b : Bool) (ω : Ω),
      ((A ω).bind fun b' => PMF.pure (decide (b' = b))) true = (A ω) b := by
    intro b ω
    rw [PMF.bind_apply, tsum_bool]
    cases b <;> simp [PMF.pure_apply]
  have mid : ∀ b : Bool,
      ((cond b P₁ P₀).bind fun ω => (A ω).bind fun b' => PMF.pure (decide (b' = b))) true
        = ∑ ω, (cond b P₁ P₀) ω * (A ω) b := by
    intro b
    rw [PMF.bind_apply, tsum_fintype]
    exact Finset.sum_congr rfl fun ω _ => by rw [inner b ω]
  have hu : ∀ b : Bool, PMF.uniformOfFintype Bool b = 1 / 2 := by
    intro b; rw [PMF.uniformOfFintype_apply]; simp
  rw [distGame, PMF.bind_apply, tsum_bool, mid, mid, hu, hu]
  simp

end Distinguishing

section DistinguishingBound

variable {Ω : Type} [Fintype Ω]

private lemma ne_top_mul (a b : ℝ≥0∞) (ha : a ≠ ⊤) (hb : b ≠ ⊤) : a * b ≠ ⊤ :=
  ENNReal.mul_ne_top ha hb

/-- The same winning probability, in `ℝ`. -/
lemma distGame_toReal (P₀ P₁ : PMF Ω) (A : Ω → PMF Bool) :
    (distGame P₀ P₁ A true).toReal
      = (1 / 2) * (∑ ω, rmass P₀ ω * rmass (A ω) false)
        + (1 / 2) * (∑ ω, rmass P₁ ω * rmass (A ω) true) := by
  have hfin : ∀ (P : PMF Ω) (f : Ω → PMF Bool) (b : Bool) (ω : Ω),
      P ω * (f ω) b ≠ ⊤ := fun P f b ω =>
    ne_top_mul _ _ (P.apply_ne_top ω) ((f ω).apply_ne_top b)
  rw [distGame_apply_true]
  rw [ENNReal.toReal_add (by
        refine ENNReal.mul_ne_top (by norm_num) ?_
        exact (ENNReal.sum_ne_top).2 fun ω _ => hfin P₀ A false ω) (by
        refine ENNReal.mul_ne_top (by norm_num) ?_
        exact (ENNReal.sum_ne_top).2 fun ω _ => hfin P₁ A true ω)]
  rw [ENNReal.toReal_mul, ENNReal.toReal_mul,
    ENNReal.toReal_sum (fun ω _ => hfin P₀ A false ω),
    ENNReal.toReal_sum (fun ω _ => hfin P₁ A true ω)]
  simp only [ENNReal.toReal_mul, rmass]
  norm_num

/-- The advantage, with the constant cleared away: what a distinguisher
collects is the mass difference, weighted by how often it says "1". -/
lemma distAdv_eq (P₀ P₁ : PMF Ω) (A : Ω → PMF Bool) :
    distAdv P₀ P₁ A = ∑ ω, rmass (A ω) true * (rmass P₁ ω - rmass P₀ ω) := by
  have hbool : ∀ ω : Ω, rmass (A ω) false + rmass (A ω) true = 1 := by
    intro ω
    have h := sum_rmass (A ω)
    rw [Fintype.sum_bool] at h
    linarith
  have hsplit : ∀ ω : Ω,
      rmass P₀ ω * rmass (A ω) false
        = rmass P₀ ω - rmass P₀ ω * rmass (A ω) true := by
    intro ω
    have h : rmass (A ω) false = 1 - rmass (A ω) true := by linarith [hbool ω]
    rw [h]; ring
  unfold distAdv
  rw [distGame_toReal, Finset.sum_congr rfl (fun ω _ => hsplit ω),
    Finset.sum_sub_distrib, sum_rmass]
  rw [Finset.sum_congr rfl (fun ω _ => mul_comm (rmass P₁ ω) (rmass (A ω) true))]
  rw [Finset.sum_congr rfl (fun ω (_ : ω ∈ Finset.univ) =>
    (mul_sub (rmass (A ω) true) (rmass P₁ ω) (rmass P₀ ω)))]
  rw [Finset.sum_sub_distrib]
  rw [Finset.sum_congr rfl (fun ω (_ : ω ∈ Finset.univ) =>
    mul_comm (rmass (A ω) true) (rmass P₀ ω))]
  ring

/-- **Fact 2.1 of `../latex/proof.tex`.**  No unbounded distinguisher, however
it randomizes, beats the statistical distance. -/
theorem distAdv_le_SD (P₀ P₁ : PMF Ω) (A : Ω → PMF Bool) :
    distAdv P₀ P₁ A ≤ SD P₀ P₁ := by
  rw [distAdv_eq, ← sum_pos_part_eq_SD]
  refine Finset.sum_le_sum fun ω _ => ?_
  have h0 : 0 ≤ rmass (A ω) true := rmass_nonneg _ _
  have h1 : rmass (A ω) true ≤ 1 := rmass_le_one _ _
  rcases le_total 0 (rmass P₁ ω - rmass P₀ ω) with h | h
  · rw [max_eq_left h]; nlinarith
  · rw [max_eq_right h]; nlinarith

open scoped Classical in
/-- The maximum-a-posteriori test: answer "1" exactly where `P₁` outweighs
`P₀`. Unbounded, and deterministic, so it needs no randomness either. -/
noncomputable def mapTest (P₀ P₁ : PMF Ω) : Ω → PMF Bool :=
  fun ω => PMF.pure (decide (rmass P₀ ω < rmass P₁ ω))

open scoped Classical in
/-- **Fact 2.1, attainment.**  The MAP test achieves the statistical distance,
so the bound above is tight and the supremum over distinguishers is attained. -/
theorem distAdv_mapTest (P₀ P₁ : PMF Ω) :
    distAdv P₀ P₁ (mapTest P₀ P₁) = SD P₀ P₁ := by
  rw [distAdv_eq, ← sum_pos_part_eq_SD]
  refine Finset.sum_congr rfl fun ω _ => ?_
  by_cases h : rmass P₀ ω < rmass P₁ ω
  · have hd : decide (rmass P₀ ω < rmass P₁ ω) = true := decide_eq_true h
    have hm : rmass (mapTest P₀ P₁ ω) true = 1 := by
      unfold mapTest; rw [hd]; simp [rmass, PMF.pure_apply]
    rw [hm, one_mul, max_eq_left (by linarith)]
  · have hd : decide (rmass P₀ ω < rmass P₁ ω) = false := decide_eq_false h
    have hm : rmass (mapTest P₀ P₁ ω) true = 0 := by
      unfold mapTest; rw [hd]; simp [rmass, PMF.pure_apply]
    rw [hm, zero_mul, max_eq_right (by linarith [not_lt.mp h])]

/-- The optimal distinguishing advantage *is* the statistical distance: the
set of achievable advantages has `SD P₀ P₁` as its greatest element. -/
theorem isGreatest_distAdv (P₀ P₁ : PMF Ω) :
    IsGreatest {r : ℝ | ∃ A : Ω → PMF Bool, distAdv P₀ P₁ A = r} (SD P₀ P₁) :=
  ⟨⟨mapTest P₀ P₁, distAdv_mapTest P₀ P₁⟩,
   by rintro r ⟨A, rfl⟩; exact distAdv_le_SD P₀ P₁ A⟩

end DistinguishingBound

end Conjura0004
