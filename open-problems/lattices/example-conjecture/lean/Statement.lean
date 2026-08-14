/-
Example Conjecture — Lean statement template.

Replace this file with a Lean formalization of the actual conjecture
statement (not a proof — state it as a `theorem`/`example` ending in
`sorry`, since these are open conjectures). This file is a
self-contained, dependency-free starting point:

* Use `Nat`, `Int`, or `Rat` for parameters and bounds — all three are
  available without any `import`. Avoid the unicode `ℕ`/`ℤ`/`ℚ`
  notation; it requires Mathlib, which this repo does not depend on.
* If the real statement needs an object this file can't fully define
  from scratch (an adversary model, a graph, a probability space, ...),
  introduce it as an `opaque` predicate/definition, exactly as the three
  real conjecture statements in this repo do (see e.g.
  `../../symmetric-key/k-collisions-auxiliary-input/lean/Statement.lean`),
  and say so in a comment — don't silently assume something the file
  doesn't actually formalize.
* End the conjecture itself with `:= by sorry`. Lean will still
  typecheck the file (with a "declaration uses `sorry`" warning) — that
  warning is the honest signal that this is a *stated*, not *proved*,
  conjecture.

Check this file with `lake env lean Statement.lean` (or plain
`lean Statement.lean`, since it needs no project dependencies) before
committing it — a `.lean` file that fails to parse is worse than no
formal artifact at all.
-/

/-- Replace with the conjecture's actual statement. -/
theorem example_conjecture (n : Nat) : n + 0 = n := by
  sorry
