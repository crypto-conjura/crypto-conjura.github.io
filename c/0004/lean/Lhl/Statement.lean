import Mathlib

/-!
# Randomness extraction from unpredictable random-oracle sources

Statement of the two leftover-hash-lemma conjectures of `statement.tex`
(*Randomness Extraction from Unpredictable Random-Oracle Sources: Two
Leftover-Hash-Lemma Conjectures*).

Everything here is information-theoretic: the source, the predictor and the
distinguisher are arbitrary (computationally unbounded) randomized functions of
the *entire* function table of `H`, modelled as `PMF`-valued functions of that
table.

## Main definitions

* `Lhl.predGame`, `Lhl.extGame`, `Lhl.extPubGame`: the prediction game and the
  two extraction games (secret seed / public seed) of Figure 1.
* `Lhl.predAdv`, `Lhl.extAdv`, `Lhl.extPubAdv`, `Lhl.IsUnpredictable`:
  Definition 1.
* `Lhl.SecretSeedConjecture` (Conjecture 1, the main statement) and
  `Lhl.PublicSeedConjecture` (Conjecture 2).
-/

namespace Lhl

/-- The auxiliary output `z ∈ {0,1}^*` of a source. -/
abbrev Aux : Type := List Bool

/-- The full function table of `H : 𝒦 × 𝒟 → ℛ`, handed to every party. -/
abbrev Table (K D R : Type) : Type := K × D → R

/-- A source: given the table of `H`, it outputs an input `x ∈ 𝒟` together with
auxiliary information `z`. -/
abbrev Source (K D R : Type) : Type := Table K D R → PMF (D × Aux)

/-- A predictor: given the table of `H` and the auxiliary output `z`, it guesses
the source's input `x`. -/
abbrev Predictor (K D R : Type) : Type := Table K D R → Aux → PMF D

/-- A distinguisher in the secret-seed game: it sees the table of `H`, the
challenge `y` and the auxiliary output `z`, but not the seed. -/
abbrev Distinguisher (K D R : Type) : Type := Table K D R → R → Aux → PMF Bool

/-- A distinguisher in the public-seed game: as `Distinguisher`, but it also
sees the seed `sd`. -/
abbrev PubDistinguisher (K D R : Type) : Type := Table K D R → K → R → Aux → PMF Bool

section Games

variable {K D R : Type} [Fintype K] [Fintype D] [Fintype R]
  [Nonempty K] [Nonempty D] [Nonempty R] [DecidableEq K] [DecidableEq D]

/-- The prediction game `Pred^S_P`:
`H ←$ Fun(𝒦 × 𝒟, ℛ)`, `(x, z) ←$ S(H)`, `x' ←$ P(H, z)`, return `x = x'`. -/
noncomputable def predGame (S : Source K D R) (P : Predictor K D R) : PMF Bool := do
  let H ← PMF.uniformOfFintype (Table K D R)
  let (x, z) ← S H
  let x' ← P H z
  return decide (x = x')

/-- The secret-seed extraction game `Ext^S_D`: the seed `sd` is drawn after the
source has terminated and is *not* given to the distinguisher. -/
noncomputable def extGame (S : Source K D R) (Dist : Distinguisher K D R) : PMF Bool := do
  let H ← PMF.uniformOfFintype (Table K D R)
  let (x, z) ← S H
  let sd ← PMF.uniformOfFintype K
  let y₁ ← PMF.uniformOfFintype R
  let b ← PMF.uniformOfFintype Bool
  let b' ← Dist H (if b then y₁ else H (sd, x)) z
  return decide (b = b')

/-- The public-seed extraction game `Ext-pub^S_D`: as `extGame`, except that the
seed `sd` is given to the distinguisher. -/
noncomputable def extPubGame (S : Source K D R) (Dist : PubDistinguisher K D R) : PMF Bool := do
  let H ← PMF.uniformOfFintype (Table K D R)
  let (x, z) ← S H
  let sd ← PMF.uniformOfFintype K
  let y₁ ← PMF.uniformOfFintype R
  let b ← PMF.uniformOfFintype Bool
  let b' ← Dist H sd (if b then y₁ else H (sd, x)) z
  return decide (b = b')

/-- `Adv^pred_{𝒦,𝒟,ℛ,S}(P) = Pr[Pred^S_P ⇒ 1]`. -/
noncomputable def predAdv (S : Source K D R) (P : Predictor K D R) : ℝ :=
  (predGame S P true).toReal

/-- `Adv^ext_{𝒦,𝒟,ℛ}(S, D) = 2 Pr[Ext^S_D ⇒ 1] - 1`. -/
noncomputable def extAdv (S : Source K D R) (Dist : Distinguisher K D R) : ℝ :=
  2 * (extGame S Dist true).toReal - 1

/-- `Adv^ext-pub_{𝒦,𝒟,ℛ}(S, D) = 2 Pr[Ext-pub^S_D ⇒ 1] - 1`. -/
noncomputable def extPubAdv (S : Source K D R) (Dist : PubDistinguisher K D R) : ℝ :=
  2 * (extPubGame S Dist true).toReal - 1

/-- A source is `ε`-unpredictable if no unbounded predictor wins the prediction
game with probability more than `ε`. -/
def IsUnpredictable (S : Source K D R) (ε : ℝ) : Prop :=
  ∀ P : Predictor K D R, predAdv S P ≤ ε

end Games

/-- The conjectured secret-seed bound
`δ(ε, K, D, R) = c √((ε R + log₂ D) / K)`. -/
noncomputable def secretBound (c ε : ℝ) (K D R : ℕ) : ℝ :=
  c * Real.sqrt ((ε * R + Real.logb 2 D) / K)

/-- The conjectured public-seed bound
`δ_pub(ε, K, D, R) = c (√(ε R) + √(log₂ D / K))`. -/
noncomputable def publicBound (c ε : ℝ) (K D R : ℕ) : ℝ :=
  c * (Real.sqrt (ε * R) + Real.sqrt (Real.logb 2 D / K))

/-- **Conjecture 1 (secret seed), the main statement.** There is a universal
constant `c > 0`, independent of `𝒦`, `𝒟`, `ℛ` and `ε`, such that for all
nonempty finite `𝒦`, `𝒟`, `ℛ`, all `ε ∈ (0, 1]`, every `ε`-unpredictable source
`S` and every unbounded distinguisher `D`,
`Adv^ext_{𝒦,𝒟,ℛ}(S, D) ≤ c √((ε R + log₂ D) / K)`. -/
def SecretSeedConjecture : Prop :=
  ∃ c : ℝ, 0 < c ∧
    ∀ (K D R : Type) [Fintype K] [Fintype D] [Fintype R]
      [Nonempty K] [Nonempty D] [Nonempty R] [DecidableEq K] [DecidableEq D]
      (ε : ℝ) (S : Source K D R) (Dist : Distinguisher K D R),
      0 < ε → ε ≤ 1 → IsUnpredictable S ε →
      extAdv S Dist ≤
        secretBound c ε (Fintype.card K) (Fintype.card D) (Fintype.card R)

/-- **Conjecture 2 (public seed).** As `SecretSeedConjecture`, for the game in
which the distinguisher is given the seed, with the bound
`c (√(ε R) + √(log₂ D / K))`. -/
def PublicSeedConjecture : Prop :=
  ∃ c : ℝ, 0 < c ∧
    ∀ (K D R : Type) [Fintype K] [Fintype D] [Fintype R]
      [Nonempty K] [Nonempty D] [Nonempty R] [DecidableEq K] [DecidableEq D]
      (ε : ℝ) (S : Source K D R) (Dist : PubDistinguisher K D R),
      0 < ε → ε ≤ 1 → IsUnpredictable S ε →
      extPubAdv S Dist ≤
        publicBound c ε (Fintype.card K) (Fintype.card D) (Fintype.card R)

end Lhl
