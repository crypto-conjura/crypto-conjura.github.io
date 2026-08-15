/-
Generalized Mirror Theory Conjecture.

This file states the conjecture only; it is not a machine-checked proof.
The full setup — cycle-consistent affine equation systems E(G, λ) over
𝔽₂ⁿ on a multigraph G = (V, E), non-degenerate solutions, the maximum
component size ξ_max(G) — is set out precisely in `../latex/main.tex`.
Here, `N` stands for `2 ^ n`, `q` for `|V|`, `m` for `|E|`, `xiMax` for
ξ_max(G), and `h` for the number of non-degenerate solutions h(G, λ); the
graph itself and its cycle-consistency are left implicit (abstracted into
the hypothesis that such a `q`, `m`, `xiMax`, `h` arise from *some*
cycle-consistent system, via the opaque predicate `ArisesFromSystem`).

Self-contained (no Mathlib dependency): the falling factorial `(N)_q` is
defined directly by recursion on `q` rather than via `Finset.prod`, and
`Rat` stands in for the real-valued error term.
-/

/-- The falling factorial `(N)_q = N(N-1)...(N-q+1)`, defined directly by
recursion (no `Finset.prod`, to keep this file Mathlib-free). -/
def fallingFactorial (N : Nat) : Nat → Nat
  | 0 => 1
  | q + 1 => (N - q) * fallingFactorial N q

/-- Abstracts "`q`, `m`, `xiMax`, `h` are respectively the vertex count,
edge count, maximum component size, and non-degenerate solution count of
*some* cycle-consistent affine system E(G, λ)", per `../latex/main.tex`.
Left opaque: fully defining it needs the graph `G` and labelling `λ`
themselves, which this self-contained file doesn't set up. -/
opaque ArisesFromSystem (q m xiMax h : Nat) : Prop

/-- Generalized Mirror Theory Conjecture.
For a cycle-consistent affine system on a graph with `q` vertices, `m`
edges, and maximum component size `xiMax`, both sublinear in `o(√N)`, the
number of non-degenerate solutions `h` satisfies the tight lower bound
`h ≥ (N)_q / N ^ m · (1 - O(q · xiMax / N))`. -/
theorem generalized_mirror_theory
    (N q m xiMax h : Nat) (hN : 0 < N)
    (harises : ArisesFromSystem q m xiMax h) :
    ∃ c : Rat, 0 < c ∧
      (h : Rat) ≥ (fallingFactorial N q : Rat) / (N : Rat) ^ m *
        (1 - c * ((q : Rat) * xiMax / N)) := by
  sorry
