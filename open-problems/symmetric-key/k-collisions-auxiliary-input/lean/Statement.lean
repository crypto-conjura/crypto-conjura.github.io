/-
Tight Time-Space Tradeoffs for k-Collisions with Auxiliary Input.

This file states the conjecture only; it is not a machine-checked proof.
The full two-stage auxiliary-input random-oracle (AI-ROM) adversary model
(offline advice phase, online query phase, random oracle H : [N] → [N]) is
described precisely in `../latex/main.tex`. Formalizing that full
adversarial model (probability over random oracles, PPT-style query
bounds) is its own project; here we abstract it behind
`FindsKCollision`, an opaque predicate meant to capture:

  "some adversary using S bits of advice and T online oracle queries
   finds a k-collision in a random oracle H : [N] → [N] with success
   probability at least 1/2."

and state the conjectured lower bound on `S`, `T` that any such adversary
must pay, for every k ≥ 3.

This is a self-contained file (no Mathlib dependency): natural numbers
suffice for the parameters S, T, k, N, and a plain existential constant
`c` stands in for the Ω(·) notation used in the write-up.
-/

/-- Abstracts "there is an (S, T)-adversary with k-collision success
probability ≥ 1/2 against a random oracle on `[N]`", per the AI-ROM model
in `../latex/main.tex`. Left opaque: fully defining it needs a probability
space over random oracles, which this self-contained file doesn't set up. -/
opaque FindsKCollision (S T k N : Nat) : Prop

/-- Generalized k-Collision Time-Space Tradeoff Conjecture.
For every k ≥ 3, any adversary that finds a k-collision (with advice
length `S` and `T` online queries) against a random oracle on `[N]` must
satisfy `Sᵏ⁻¹ · Tᵏ = Ω(Nᵏ⁻¹)`. -/
theorem k_collision_time_space_tradeoff
    (S T k N : Nat) (hk : 3 ≤ k) (h : FindsKCollision S T k N) :
    ∃ c : Nat, 0 < c ∧ c * N ^ (k - 1) ≤ S ^ (k - 1) * T ^ k := by
  sorry
