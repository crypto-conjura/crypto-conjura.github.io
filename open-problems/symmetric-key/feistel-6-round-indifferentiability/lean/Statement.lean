/-
Exact Full Indifferentiability of 6-Round Feistel Networks.

This file states the conjecture only; it is not a machine-checked proof.
The full indifferentiability framework (Maurer et al. 2002) — the Feistel
construction Ψ^r[F], the ideal permutation P, simulators S^P, and
distinguishers D — is set out precisely in `../latex/main.tex`. Fully
formalizing that framework (simulators as stateful oracle-interactive
programs, distinguishing advantage as a probability over random F, P) is
its own project; here two opaque quantities abstract it:

* `SimQueryBound sim q` : the number of queries a candidate simulator
  `sim` makes to answer `q` distinguisher queries.
* `Advantage n q simQueries` : the best distinguishing advantage any
  distinguisher making `q` total queries can achieve against 6-round
  Feistel on `2n`-bit strings, given a simulator with the stated query
  behaviour.

The conjecture is that some simulator exists with polynomially many
queries whose advantage is negligible in the stated sense.

Self-contained (no Mathlib dependency): `Rat` (rationals, from Lean's
core library) stands in for the real-valued advantage/probability, since
the polynomial bound below only needs ordered-field arithmetic, not
Mathlib's asymptotic-notation or measure-theoretic probability library.
-/

/-- The number of oracle queries a candidate simulator `sim` makes to
answer `q` distinguisher queries; left opaque, since fully modelling
simulators as interactive programs is out of scope for this file. -/
opaque SimQueryBound (sim : Nat) (q : Nat) : Nat

/-- The best distinguishing advantage (as a rational, standing in for a
real-valued probability) any distinguisher making `q` total queries can
achieve against 6-round Feistel on `2n`-bit strings, relative to
simulator `sim`; left opaque for the same reason as `SimQueryBound`. -/
opaque Advantage (sim : Nat) (n q : Nat) : Rat

/-- Full Indifferentiability of 6-Round Feistel Conjecture.
There exists a simulator making only polynomially many queries in `q`
(for some fixed degree `k`) whose distinguishing advantage against
6-round Feistel is bounded by `c · q ^ k / 2 ^ n`, for every `n` and
every query budget `q`. -/
theorem feistel6_indifferentiability :
    ∃ (sim : Nat) (k : Nat), 2 ≤ k ∧
      (∃ c : Nat, 0 < c ∧ ∀ q : Nat, SimQueryBound sim q ≤ c * q ^ k) ∧
      (∃ c : Rat, 0 < c ∧ ∀ n q : Nat,
        Advantage sim n q ≤ c * (q : Rat) ^ k / (2 : Rat) ^ n) := by
  sorry
