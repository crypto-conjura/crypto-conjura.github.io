/-
  Campaign c/0023, artifact 0023-prover-2 (prover, plan P1), unit 4.
  STATEMENT-ONLY Lean skeleton: definitions + the boundary signatures of
  L2, L4, L5, T1, T2, T3.  All proof bodies are `sorry`; this file is a
  type-check of the STATEMENTS, per HARNESS 3.8 phase 1.
  Type-checked with: lake env lean <this file>  (Mathlib, lean4 v4.33.0).
-/
import Mathlib

namespace C0023

/-! ### The cube, the multilinear expansion, degree, influence -/

/-- A point of `{±1}^N`, encoded as a Boolean vector: `false ↦ +1`, `true ↦ -1`. -/
abbrev Point (N : ℕ) := Fin N → Bool

variable {N : ℕ}

/-- The `±1` value of coordinate `i` at `x`. -/
def val (x : Point N) (i : Fin N) : ℝ := if x i then -1 else 1

/-- The monomial `x^S = ∏_{i ∈ S} x_i`. -/
def chi (S : Finset (Fin N)) (x : Point N) : ℝ := ∏ i ∈ S, val x i

/-- The multilinear (Fourier) coefficient of `f` at `S`, i.e. `⟨f, x^S⟩`. -/
noncomputable def coeff (f : Point N → ℝ) (S : Finset (Fin N)) : ℝ :=
  (∑ x : Point N, f x * chi S x) / 2 ^ N

/-- `deg f ≤ d`. -/
def DegLE (f : Point N → ℝ) (d : ℕ) : Prop :=
  ∀ S : Finset (Fin N), coeff f S ≠ 0 → S.card ≤ d

/-- The Contract's influence `Inf_i(f) = Σ_{S ∋ i} f̂(S)²`. -/
noncomputable def Infl (f : Point N → ℝ) (i : Fin N) : ℝ :=
  ∑ S ∈ Finset.univ.filter (fun S : Finset (Fin N) => i ∈ S), coeff f S ^ 2

/-- Flip coordinate `i` of `x`. -/
def flp (i : Fin N) (x : Point N) : Point N := Function.update x i (! x i)

/-- The relevant coordinates of a set. -/
def Relevant (A : Finset (Point N)) : Set (Fin N) :=
  {i | ∃ x : Point N, x ∈ A ∧ flp i x ∉ A}

/-- Density `α = |A|/2^N`. -/
noncomputable def dens (A : Finset (Point N)) : ℝ := (A.card : ℝ) / 2 ^ N

/-- The `{0,1}`-valued indicator of `A`. -/
def ind (A : Finset (Point N)) : Point N → ℝ := fun x => if x ∈ A then 1 else 0

/-- The unit-norm member of the class: `1_A / ‖1_A‖₂`. -/
noncomputable def nrm (A : Finset (Point N)) : Point N → ℝ :=
  fun x => ind A x / Real.sqrt (dens A)

/-- `W` is a *shattering window* for `A` at degree `d`: `|W| ≤ d` and `A`
projects onto `{±1}^{[N] \ W}` (card S7b). -/
def IsWindow (d : ℕ) (A : Finset (Point N)) (W : Finset (Fin N)) : Prop :=
  W.card ≤ d ∧ ∀ y : Point N, ∃ a ∈ A, ∀ i, i ∉ W → a i = y i

/-- The payment: each side charged on the *partner's* window; a sum, never a min. -/
noncomputable def pay (A B : Finset (Point N)) (WA WB : Finset (Fin N)) : ℝ :=
  (∑ i ∈ WB, Infl (nrm A) i) + (∑ i ∈ WA, Infl (nrm B) i)

/-! ### L1, L2: the nonvanishing lemma and the influence quantum -/

theorem L1_nonvanishing (k : ℕ) (f : Point N → ℝ) (hf : f ≠ 0) (hdeg : DegLE f k) :
    (1 : ℝ) / 2 ^ k ≤
      ((Finset.univ.filter (fun x : Point N => f x ≠ 0)).card : ℝ) / 2 ^ N := by
  sorry

theorem L2_quantum (d : ℕ) (hd : 1 ≤ d) (A : Finset (Point N)) (hA : A.Nonempty)
    (hdeg : DegLE (ind A) d) {i : Fin N} (hi : i ∈ Relevant A) :
    (1 : ℝ) / 2 ^ (d + 1) ≤ Infl (ind A) i := by
  sorry

/-! ### L4 = G1: positivity (the first two-family consequence of card S7b) -/

theorem L4_positivity (d : ℕ) (A B : Finset (Point N)) (hB : B.Nonempty)
    (hdisj : Disjoint A B) {W : Finset (Fin N)} (hW : IsWindow d A W) :
    ∃ i ∈ W, i ∈ Relevant B := by
  sorry

/-! ### L5: the master count with pair-independent windows -/

variable {ιF ιG : Type*} [Fintype ιF] [Fintype ιG]

theorem L5_count (ω : ℕ) (δF δG : ℝ)
    (AF : ιF → Finset (Point N)) (AG : ιG → Finset (Point N))
    (pF : ιF → ℝ) (pG : ιG → ℝ)
    (hpF0 : ∀ a, 0 ≤ pF a) (hpF1 : ∑ a, pF a = 1)
    (hpG0 : ∀ b, 0 ≤ pG b) (hpG1 : ∑ b, pG b = 1)
    (W : Finset (Point N) → Finset (Fin N)) (hW : ∀ A, (W A).card ≤ ω)
    (hF : ∀ i : Fin N, (∑ a, pF a * Infl (nrm (AF a)) i) ≤ δF)
    (hG : ∀ i : Fin N, (∑ b, pG b * Infl (nrm (AG b)) i) ≤ δG) :
    (∑ a, ∑ b, pF a * pG b * pay (AF a) (AG b) (W (AF a)) (W (AG b)))
      ≤ (δF + δG) * ω := by
  sorry

/-! ### T1: the reduction (PAY⋆) ⟹ R2 -/

theorem T1_reduction (d ω : ℕ) (p δ : ℝ)
    (W : Finset (Point N) → Finset (Fin N)) (hW : ∀ A, (W A).card ≤ ω)
    (AF : ιF → Finset (Point N)) (AG : ιG → Finset (Point N))
    (hAF : ∀ a, (AF a).Nonempty) (hAG : ∀ b, (AG b).Nonempty)
    (hdegF : ∀ a, DegLE (ind (AF a)) d) (hdegG : ∀ b, DegLE (ind (AG b)) d)
    (pF : ιF → ℝ) (pG : ιG → ℝ)
    (hpF0 : ∀ a, 0 ≤ pF a) (hpF1 : ∑ a, pF a = 1)
    (hpG0 : ∀ b, 0 ≤ pG b) (hpG1 : ∑ b, pG b = 1)
    (hinfF : ∀ i : Fin N, (∑ a, pF a * Infl (nrm (AF a)) i) ≤ δ)
    (hinfG : ∀ i : Fin N, (∑ b, pG b * Infl (nrm (AG b)) i) ≤ δ)
    (hpay : ∀ a b, Disjoint (AF a) (AG b) →
              p ≤ pay (AF a) (AG b) (W (AF a)) (W (AG b)))
    (hsmall : 2 * δ * ω < p) :
    ∃ a b, ¬ Disjoint (AF a) (AG b) := by
  sorry

/-! ### T2: the unconditional payment bound and the threshold it yields -/

theorem T2_payment (d : ℕ) (hd : 1 ≤ d) (A B : Finset (Point N))
    (hA : A.Nonempty) (hB : B.Nonempty) (hdisj : Disjoint A B)
    (hdegA : DegLE (ind A) d) (hdegB : DegLE (ind B) d)
    {WA WB : Finset (Fin N)} (hWA : IsWindow d A WA) (hWB : IsWindow d B WB) :
    (2 : ℝ) / 2 ^ d ≤ pay A B WA WB := by
  sorry

/-! ### T3: the family refuting (PAY⋆) in its all-maximum-degree-windows form -/

/-- The block window `U = {u_1,…,u_d}` inside `Fin (d+1)`. -/
def blockWindow (d : ℕ) : Finset (Fin (d + 1)) :=
  Finset.univ.filter (fun j => j ≠ Fin.last d)

/-- `𝖠_d = {(u,w) : w = +1, u ≠ p} ∪ {(u,w) : w = -1, u = q}` with
`p = (+1,…,+1)` and `q = p` flipped in the first block coordinate. -/
def Afam (d : ℕ) : Finset (Point (d + 1)) :=
  Finset.univ.filter (fun x =>
    if x (Fin.last d) = false
      then ∃ i : Fin d, x (Fin.castSucc i) = true
      else ∀ i : Fin d, x (Fin.castSucc i) = decide (i.val = 0))

/-- `𝖡_d = 𝖠_d^c`. -/
def Bfam (d : ℕ) : Finset (Point (d + 1)) := (Afam d)ᶜ

theorem T3_deg (d : ℕ) (hd : 2 ≤ d) :
    DegLE (ind (Afam d)) d ∧ DegLE (ind (Bfam d)) d := by
  sorry

theorem T3_window (d : ℕ) (hd : 2 ≤ d) :
    IsWindow d (Afam d) (blockWindow d) ∧ IsWindow d (Bfam d) (blockWindow d) := by
  sorry

/-- The certificate: the payment on the block window is `d·2^{1-d}`, which is
`2^{-Θ(d)}`, so (PAY⋆) quantified over all maximum-degree windows is false. -/
theorem T3_payment (d : ℕ) (hd : 2 ≤ d) :
    pay (Afam d) (Bfam d) (blockWindow d) (blockWindow d) = (d : ℝ) * 2 / 2 ^ d := by
  sorry

end C0023
