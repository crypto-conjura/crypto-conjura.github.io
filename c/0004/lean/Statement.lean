/-
Leftover Hash Lemma extraction bound for unpredictable random-oracle sources,
public seed.  Conjura statement c/0004.

This file states the conjecture.  It does not prove it: `lhl_public_seed`
below is the one `sorry` in the file.

What is different here from c/0001 through c/0003 is that nothing is
`opaque`.  Those files abstract the object under study behind an opaque
constant, which makes the statement compile but pins nothing: any two
readers can disagree about what was said and the kernel will not arbitrate.
c/0004 is fully concrete -- finite seed, input and output sets, a uniform
function table handed to everyone, two explicit games -- so it can be
written out, and every quantifier below corresponds to one in the
`## Statement` tab of `c/0004/index.qmd`.  See `MATCH.md` for the
element-by-element correspondence.

Design notes.

* Everything in sight is finite, so the randomness is `PMF` (finitely
  supported probability mass functions) rather than measure theory.  A
  probability is then just the mass a `PMF Bool` puts on `true`.
* "Computationally unbounded, and receives the entire function table of `H`
  as an explicit input" is modelled by letting the source, the predictor and
  the distinguisher be *arbitrary functions* of the table.  There is no
  complexity class to name: an arbitrary function is exactly an unbounded
  algorithm.
* The auxiliary-information alphabet `Z` carries no `Fintype` and no
  `DecidableEq`.  The informal statement puts no constraint on `z` beyond
  the source producing it, and none is needed here either, so `Z` stays an
  arbitrary type.  This is deliberate: requiring `Fintype Z` would be a
  restriction the informal statement does not make.
-/
import Mathlib.Probability.ProbabilityMassFunction.Constructions
import Mathlib.Probability.Distributions.Uniform
import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.Analysis.Real.Sqrt

namespace Conjura0004

open scoped ENNReal

/-! ## The objects -/

/-- The function table of the random oracle: every map `𝒦 × 𝒟 → ℛ`.
`H ←$ Fun(𝒦 × 𝒟, ℛ)` below is the uniform distribution on this type. -/
abbrev Table (K D R : Type) := K × D → R

/-- A source.  Unbounded, and handed the entire table, so: an arbitrary
function of the table, returning a distribution on (sample, auxiliary
information) pairs. -/
abbrev Source (K D R Z : Type) := Table K D R → PMF (D × Z)

/-- A predictor.  Sees the table and the auxiliary information, and guesses
the source's sample.  It does *not* see the sample. -/
abbrev Predictor (K D R Z : Type) := Table K D R → Z → PMF D

/-- A distinguisher for the public-seed game.  Sees the table, the seed (this
is what "public seed" means), the challenge, and the auxiliary information. -/
abbrev Distinguisher (K D R Z : Type) := Table K D R → K → R → Z → PMF Bool

section Games

variable {K D R Z : Type}
  [Fintype K] [Fintype D] [Fintype R]
  [DecidableEq K] [DecidableEq D]
  [Nonempty K] [Nonempty D] [Nonempty R]

/-- Game `Pred^S_P`:
`H ←$ Fun(𝒦 × 𝒟, ℛ)`; `(x, z) ←$ S(H)`; `x' ←$ P(H, z)`; return `x = x'`. -/
noncomputable def predGame (S : Source K D R Z) (P : Predictor K D R Z) :
    PMF Bool :=
  (PMF.uniformOfFintype (Table K D R)).bind fun H =>
    (S H).bind fun xz =>
      (P H xz.2).bind fun x' =>
        PMF.pure (decide (xz.1 = x'))

/-- Game `Ext-pub^S_D` (public seed):
`H ←$ Fun(𝒦 × 𝒟, ℛ)`; `(x, z) ←$ S(H)`; `sd ←$ 𝒦`;
`y₀ ← H(sd, x)`; `y₁ ←$ ℛ`; `b ←$ {0,1}`; `b' ←$ D(H, sd, y_b, z)`;
return `b = b'`.

`b = false` selects the real challenge `y₀ = H(sd, x)` and `b = true` the
uniform one `y₁`, matching `y₀`/`y₁` in the informal game. -/
noncomputable def extGame (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    PMF Bool :=
  (PMF.uniformOfFintype (Table K D R)).bind fun H =>
    (S H).bind fun xz =>
      (PMF.uniformOfFintype K).bind fun sd =>
        (PMF.uniformOfFintype R).bind fun y₁ =>
          (PMF.uniformOfFintype Bool).bind fun b =>
            (Dist H sd (if b then y₁ else H (sd, xz.1)) xz.2).bind fun b' =>
              PMF.pure (decide (b = b'))

/-- `Adv^pred_{𝒦,𝒟,ℛ,S}(P) := Pr[Pred^S_P ⇒ 1]`. -/
noncomputable def predAdv (S : Source K D R Z) (P : Predictor K D R Z) : ℝ :=
  (predGame S P true).toReal

/-- `Adv^{ext-pub}_{𝒦,𝒟,ℛ}(S, D) := 2 Pr[Ext-pub^S_D ⇒ 1] - 1`. -/
noncomputable def extAdv (S : Source K D R Z) (Dist : Distinguisher K D R Z) : ℝ :=
  2 * (extGame S Dist true).toReal - 1

/-- `S` is ε-unpredictable: no unbounded predictor beats ε. -/
def Unpredictable (ε : ℝ) (S : Source K D R Z) : Prop :=
  ∀ P : Predictor K D R Z, predAdv S P ≤ ε

end Games

/-! ## The conjecture -/

/-- **Conjecture (public seed).**  There is a universal constant `c > 0`,
independent of `𝒦`, `𝒟`, `ℛ` and `ε`, such that for all nonempty finite
`𝒦, 𝒟, ℛ`, all `ε ∈ (0, 1]`, every ε-unpredictable source `S` and every
unbounded distinguisher `D`,

`Adv^{ext-pub}(S, D) ≤ c · (√(ε R) + √(log₂ D / K))`.

The constant is existentially quantified *outside* every other quantifier,
which is what "universal constant" means and is the whole content of the
conjecture: a `c` allowed to depend on `𝒦`, `𝒟`, `ℛ` or `ε` would make the
statement trivial. -/
theorem lhl_public_seed :
    ∃ c : ℝ, 0 < c ∧
      ∀ (K D R Z : Type)
        [Fintype K] [Fintype D] [Fintype R]
        [DecidableEq K] [DecidableEq D]
        [Nonempty K] [Nonempty D] [Nonempty R]
        (ε : ℝ), 0 < ε → ε ≤ 1 →
        ∀ S : Source K D R Z, Unpredictable ε S →
        ∀ Dist : Distinguisher K D R Z,
          extAdv S Dist ≤
            c * (Real.sqrt (ε * Fintype.card R)
                 + Real.sqrt (Real.logb 2 (Fintype.card D) / Fintype.card K)) := by
  sorry

/-! ## Sanity lemmas

These are `sorry`-free.  They exist because a definition that nothing has
been proved about is a definition nobody has checked: an advantage that
could fall outside `[0, 1]`, or a degenerate case that does not come out to
the obvious answer, is how a misformalization announces itself. -/

section Sanity

variable {K D R Z : Type}
  [Fintype K] [Fintype D] [Fintype R]
  [DecidableEq K] [DecidableEq D]
  [Nonempty K] [Nonempty D] [Nonempty R]

/-- A probability read off a `PMF Bool` is at most one. -/
private lemma toReal_le_one (p : PMF Bool) (b : Bool) : (p b).toReal ≤ 1 := by
  have h := p.coe_le_one b
  simpa using ENNReal.toReal_mono (by simp) h

omit [Nonempty K] [Nonempty D] in
theorem predAdv_nonneg (S : Source K D R Z) (P : Predictor K D R Z) :
    0 ≤ predAdv S P :=
  ENNReal.toReal_nonneg

omit [Nonempty K] [Nonempty D] in
theorem predAdv_le_one (S : Source K D R Z) (P : Predictor K D R Z) :
    predAdv S P ≤ 1 :=
  toReal_le_one _ _

omit [Nonempty K] [Nonempty D] in
/-- The prediction advantage is a probability. -/
theorem predAdv_mem_unitInterval (S : Source K D R Z) (P : Predictor K D R Z) :
    predAdv S P ∈ Set.Icc (0 : ℝ) 1 :=
  ⟨predAdv_nonneg S P, predAdv_le_one S P⟩

omit [Nonempty D] in
theorem extAdv_le_one (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    extAdv S Dist ≤ 1 := by
  have := toReal_le_one (extGame S Dist) true
  unfold extAdv
  linarith

omit [Nonempty D] in
theorem neg_one_le_extAdv (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    -1 ≤ extAdv S Dist := by
  have : (0 : ℝ) ≤ (extGame S Dist true).toReal := ENNReal.toReal_nonneg
  unfold extAdv
  linarith

/-- If every branch of a bind is a fair coin on `true`, so is the bind. -/
private lemma bind_half {α : Type} (p : PMF α) (f : α → PMF Bool)
    (hf : ∀ a, f a true = 1 / 2) : (p.bind f) true = 1 / 2 := by
  rw [PMF.bind_apply]
  simp only [hf]
  rw [ENNReal.tsum_mul_right, PMF.tsum_coe, one_mul]

/-- Guessing a uniform bit that nothing observed depends on succeeds with
probability exactly one half. -/
private lemma guess_half (q : PMF Bool) :
    ((PMF.uniformOfFintype Bool).bind fun b =>
      q.bind fun b' => PMF.pure (decide (b = b'))) true = 1 / 2 := by
  have inner : ∀ b : Bool,
      (q.bind fun b' => PMF.pure (decide (b = b'))) true = q b := by
    intro b
    rw [PMF.bind_apply]
    rw [tsum_bool]
    cases b <;> simp [PMF.pure_apply]
  rw [PMF.bind_apply, tsum_bool, inner, inner]
  have hu : ∀ b : Bool, PMF.uniformOfFintype Bool b = 1 / 2 := by
    intro b
    rw [PMF.uniformOfFintype_apply]
    simp
  rw [hu, hu]
  have hsum : q false + q true = 1 := by
    have := q.tsum_coe
    rwa [tsum_bool] at this
  rw [← mul_add, hsum, mul_one]

omit [Nonempty D] in
/-- **Degenerate case.**  When the output set has a single element the
challenge carries no information at all: `y₀` and `y₁` are equal whatever
the seed and the sample, so the distinguisher's view does not depend on the
hidden bit and its advantage is exactly zero.

This is the sanity check that the two games were wired up the right way
round.  A formalization that accidentally leaked `b` into the
distinguisher's input, or that compared the wrong pair of bits, would give
something other than `0` here. -/
theorem extAdv_eq_zero_of_subsingleton
    [Subsingleton R] (S : Source K D R Z) (Dist : Distinguisher K D R Z) :
    extAdv S Dist = 0 := by
  have key : extGame S Dist true = 1 / 2 := by
    refine bind_half _ _ fun H => bind_half _ _ fun xz => bind_half _ _ fun sd =>
      bind_half _ _ fun y₁ => ?_
    -- With `R` a subsingleton the challenge is the same value either way, so
    -- the distinguisher's input no longer mentions `b`.
    have hcond : ∀ b : Bool,
        (if b then y₁ else H (sd, xz.1)) = H (sd, xz.1) := by
      intro b; cases b <;> simp [Subsingleton.elim y₁ (H (sd, xz.1))]
    simp only [hcond]
    exact guess_half _
  unfold extAdv
  rw [key]
  simp

end Sanity

end Conjura0004
