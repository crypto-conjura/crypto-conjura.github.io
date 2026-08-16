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
      (A ω).bind fun b' => PMF.pure (decide (b = b'))

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
      ((A ω).bind fun b' => PMF.pure (decide (b = b'))) true = (A ω) b := by
    intro b ω
    rw [PMF.bind_apply, tsum_bool]
    cases b <;> simp [PMF.pure_apply]
  have mid : ∀ b : Bool,
      ((cond b P₁ P₀).bind fun ω => (A ω).bind fun b' => PMF.pure (decide (b = b'))) true
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

/-! ## 3. Bridging the game to the analytic quantity

`Statement.lean` defines `extAdv` operationally. The informal proof works with
statistical distances instead. The bridge is that the extraction game *is* a
distinguishing game, between the two distributions the distinguisher's view
has under `b = 0` and `b = 1`.

The one restriction here that the conjecture does not make is `[Fintype Z]`:
`SD` above is defined by a `Finset` sum, so the view type has to be finite,
and the view carries `z`. Lifting it means redoing section 1 with `tsum`,
which is possible (a `PMF` is countably supported) and is recorded as
outstanding in `LEDGER.md`. -/

section Bridge

variable {K D R Z : Type}
  [Fintype K] [Fintype D] [Fintype R] [Fintype Z]
  [DecidableEq K] [DecidableEq D]
  [Nonempty K] [Nonempty D] [Nonempty R]

/-- Everything the distinguisher is handed: the table, the seed, the
challenge, the auxiliary information. -/
abbrev View (K D R Z : Type) := Table K D R × K × R × Z

/-- The law of the distinguisher's view under challenge bit `b`. -/
noncomputable def viewDist (S : Source K D R Z) (b : Bool) : PMF (View K D R Z) :=
  (PMF.uniformOfFintype (Table K D R)).bind fun H =>
    (S H).bind fun xz =>
      (PMF.uniformOfFintype K).bind fun sd =>
        (PMF.uniformOfFintype R).bind fun y₁ =>
          PMF.pure (H, sd, (if b then y₁ else H (sd, xz.1)), xz.2)

/-- The distinguisher, reading its four arguments off one view. -/
def onView (Dist : Distinguisher K D R Z) : View K D R Z → PMF Bool :=
  fun v => Dist v.1 v.2.1 v.2.2.1 v.2.2.2

omit [Fintype Z] [Nonempty D] in
/-- `distGame` on the two view laws, with the binds flattened out. -/
lemma distGame_viewDist (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    distGame (viewDist S false) (viewDist S true) (onView Dist)
      = (PMF.uniformOfFintype Bool).bind fun b =>
          (PMF.uniformOfFintype (Table K D R)).bind fun H =>
            (S H).bind fun xz =>
              (PMF.uniformOfFintype K).bind fun sd =>
                (PMF.uniformOfFintype R).bind fun y₁ =>
                  (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
                    PMF.pure (decide (b = b')) := by
  rw [distGame]
  refine congrArg _ (funext fun b => ?_)
  have hc : cond b (viewDist S true) (viewDist S false) = viewDist S b := by
    cases b <;> rfl
  rw [hc, viewDist]
  simp only [PMF.bind_bind, PMF.pure_bind, onView]

omit [Fintype Z] [Nonempty D] in
/-- The extraction game **is** a distinguishing game between the two view laws.

The only work is moving the challenge bit from where the game samples it
(last, after the table, the source, the seed and the uniform challenge) to
where a distinguishing game samples it (first): four applications of
`PMF.bind_comm`. -/
theorem extGame_eq_distGame (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    extGame S Dist = distGame (viewDist S false) (viewDist S true) (onView Dist) := by
  rw [distGame_viewDist, extGame]
  have c1 : ∀ (H : Table K D R) (xz : D × Z) (sd : K),
      ((PMF.uniformOfFintype R).bind fun y₁ =>
          (PMF.uniformOfFintype Bool).bind fun b =>
            (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
              PMF.pure (decide (b = b')))
        = ((PMF.uniformOfFintype Bool).bind fun b =>
          (PMF.uniformOfFintype R).bind fun y₁ =>
            (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
              PMF.pure (decide (b = b'))) := fun _ _ _ => PMF.bind_comm _ _ _
  simp only [c1]
  have c2 : ∀ (H : Table K D R) (xz : D × Z),
      ((PMF.uniformOfFintype K).bind fun sd =>
          (PMF.uniformOfFintype Bool).bind fun b =>
            (PMF.uniformOfFintype R).bind fun y₁ =>
              (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
                PMF.pure (decide (b = b')))
        = ((PMF.uniformOfFintype Bool).bind fun b =>
          (PMF.uniformOfFintype K).bind fun sd =>
            (PMF.uniformOfFintype R).bind fun y₁ =>
              (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
                PMF.pure (decide (b = b'))) := fun _ _ => PMF.bind_comm _ _ _
  simp only [c2]
  have c3 : ∀ H : Table K D R,
      ((S H).bind fun xz =>
          (PMF.uniformOfFintype Bool).bind fun b =>
            (PMF.uniformOfFintype K).bind fun sd =>
              (PMF.uniformOfFintype R).bind fun y₁ =>
                (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
                  PMF.pure (decide (b = b')))
        = ((PMF.uniformOfFintype Bool).bind fun b =>
          (S H).bind fun xz =>
            (PMF.uniformOfFintype K).bind fun sd =>
              (PMF.uniformOfFintype R).bind fun y₁ =>
                (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
                  PMF.pure (decide (b = b'))) := fun _ => PMF.bind_comm _ _ _
  simp only [c3]
  exact PMF.bind_comm _ _ _

omit [Nonempty D] in
/-- **The bridge.**  No unbounded distinguisher does better against the
extraction game than the statistical distance between the two view laws.

This is what lets every later step of `../latex/proof.tex` work with an
analytic quantity instead of a game. -/
theorem extAdv_le_SD_views (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    extAdv S Dist ≤ SD (viewDist S false) (viewDist S true) := by
  have : extAdv S Dist = distAdv (viewDist S false) (viewDist S true) (onView Dist) := by
    unfold extAdv distAdv
    rw [extGame_eq_distGame]
  rw [this]
  exact distAdv_le_SD _ _ _

open scoped Classical in
/-- The MAP test on views, curried back into a `Distinguisher`. Unbounded, so
this is a legal adversary in the game as stated. -/
noncomputable def mapDist (S : Source K D R Z) : Distinguisher K D R Z :=
  fun H sd y z => mapTest (viewDist S false) (viewDist S true) (H, sd, y, z)

omit [Nonempty D] in
open scoped Classical in
/-- The bridge is tight: `mapDist` attains the view distance. -/
theorem extAdv_mapDist (S : Source K D R Z) :
    extAdv S (mapDist S) = SD (viewDist S false) (viewDist S true) := by
  have honView : onView (mapDist S) = mapTest (viewDist S false) (viewDist S true) := rfl
  have : extAdv S (mapDist S)
      = distAdv (viewDist S false) (viewDist S true) (onView (mapDist S)) := by
    unfold extAdv distAdv
    rw [extGame_eq_distGame]
  rw [this, honView, distAdv_mapTest]

omit [Nonempty D] in
/-- **Lemma 3.1 of `../latex/proof.tex`, first half.**  The best extraction
advantage any unbounded distinguisher achieves is exactly the statistical
distance between the two view laws.

The informal proof states this with a maximum and notes in passing that the
maximum is attained. Here that is `IsGreatest`, with `mapDist` as the witness. -/
theorem isGreatest_extAdv (S : Source K D R Z) :
    IsGreatest {r : ℝ | ∃ Dist : Distinguisher K D R Z, extAdv S Dist = r}
      (SD (viewDist S false) (viewDist S true)) :=
  ⟨⟨mapDist S, extAdv_mapDist S⟩,
   by rintro r ⟨Dist, rfl⟩; exact extAdv_le_SD_views S Dist⟩

/-! ### The predictor side

`Lemma 3.1` also identifies the best prediction advantage with an analytic
quantity: the expected largest conditional mass. With everything finite that
quantity can be written without any conditioning, as `∑ z, max_x p(x, z)`,
because `p(z) · max_x p(x | z) = max_x p(x, z)`. -/

/-- `∑ z, max_x Pr[(x, z)]`, the analytic form of the best prediction
advantage on a fixed table. Equal to `𝔼_Z[ε_{H,Z}]` of `../latex/proof.tex`. -/
noncomputable def maxMass (S : Source K D R Z) (H : Table K D R) : ℝ :=
  ∑ z : Z, Finset.univ.sup' Finset.univ_nonempty fun x : D => rmass (S H) (x, z)

omit [Nonempty K] [Nonempty D] in
lemma predGame_toReal (S : Source K D R Z) (P : Predictor K D R Z) :
    (predGame S P true).toReal
      = ∑ H : Table K D R, rmass (PMF.uniformOfFintype (Table K D R)) H
          * ∑ xz : D × Z, rmass (S H) xz * rmass (P H xz.2) xz.1 := by
  have inner : ∀ (H : Table K D R) (xz : D × Z),
      ((P H xz.2).bind fun x' => PMF.pure (decide (xz.1 = x'))) true
        = (P H xz.2) xz.1 := by
    intro H xz
    rw [PMF.bind_apply, tsum_fintype]
    rw [Finset.sum_eq_single xz.1]
    · simp [PMF.pure_apply]
    · intro x' _ hx
      simp [PMF.pure_apply, Ne.symm hx]
    · intro h; exact absurd (Finset.mem_univ _) h
  have mid : ∀ H : Table K D R,
      ((S H).bind fun xz => (P H xz.2).bind fun x' => PMF.pure (decide (xz.1 = x'))) true
        = ∑ xz : D × Z, (S H) xz * (P H xz.2) xz.1 := by
    intro H
    rw [PMF.bind_apply, tsum_fintype]
    exact Finset.sum_congr rfl fun xz _ => by rw [inner H xz]
  have hne : ∀ (H : Table K D R) (xz : D × Z), (S H) xz * (P H xz.2) xz.1 ≠ ⊤ :=
    fun H xz => ENNReal.mul_ne_top ((S H).apply_ne_top xz) ((P H xz.2).apply_ne_top xz.1)
  rw [predGame, PMF.bind_apply, tsum_fintype,
    ENNReal.toReal_sum (fun H _ => ENNReal.mul_ne_top
      ((PMF.uniformOfFintype (Table K D R)).apply_ne_top H)
      (by rw [mid H]; exact (ENNReal.sum_ne_top).2 fun xz _ => hne H xz))]
  refine Finset.sum_congr rfl fun H _ => ?_
  rw [mid H, ENNReal.toReal_mul, ENNReal.toReal_sum (fun xz _ => hne H xz)]
  simp only [ENNReal.toReal_mul, rmass]

omit [Nonempty K] in
/-- **Lemma 3.1, predictor half (bound).**  No unbounded predictor beats the
expected largest mass. -/
theorem predAdv_le_maxMass (S : Source K D R Z) (P : Predictor K D R Z) :
    predAdv S P
      ≤ ∑ H : Table K D R, rmass (PMF.uniformOfFintype (Table K D R)) H * maxMass S H := by
  rw [predAdv, predGame_toReal]
  refine Finset.sum_le_sum fun H _ => ?_
  refine mul_le_mul_of_nonneg_left ?_ (rmass_nonneg _ _)
  rw [Fintype.sum_prod_type_right]
  refine Finset.sum_le_sum fun z _ => ?_
  set M := Finset.univ.sup' Finset.univ_nonempty fun x : D => rmass (S H) (x, z) with hM
  have hbound : ∀ x : D, rmass (S H) (x, z) * rmass (P H z) x ≤ M * rmass (P H z) x := by
    intro x
    exact mul_le_mul_of_nonneg_right
      (Finset.le_sup' (fun x : D => rmass (S H) (x, z)) (Finset.mem_univ x))
      (rmass_nonneg _ _)
  calc ∑ x : D, rmass (S H) (x, z) * rmass (P H z) x
      ≤ ∑ x : D, M * rmass (P H z) x := Finset.sum_le_sum fun x _ => hbound x
    _ = M * ∑ x : D, rmass (P H z) x := by rw [Finset.mul_sum]
    _ = M := by rw [sum_rmass, mul_one]

end Bridge

end Conjura0004
