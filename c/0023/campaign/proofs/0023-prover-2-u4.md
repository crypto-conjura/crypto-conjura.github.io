---
id: 0023-prover-2-u4
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE (unit 4 of 5)
---

# Unit 4 — Lean statement skeleton (phase 1 only: statements, `sorry` bodies), type-checked

File: `campaign/lean/0023-prover-2-skeleton.lean`.
Checked with `lake env lean` against Mathlib in the repository's existing Lean
project (`/lean`, toolchain `leanprover/lean4:v4.33.0`). **Result: no errors;
the only diagnostics are the nine expected `declaration uses 'sorry'`
warnings.** This is HARNESS §3.8 *phase 1* (statement round-trip), not a
verification: compilation of a `sorry`-closed file is not proof (§3.8's audit
note), and the mathematics of record is units 1–3 plus the exact machine check
of u2.

## What is defined

`Point N := Fin N → Bool` (`false ↦ +1`, `true ↦ −1`); `val`, `chi S`
(the monomial $x^S$), `coeff f S` ($=\langle f,x^S\rangle$, computed as a sum
over the cube divided by $2^N$), `DegLE f d` ($\deg f\le d$ as "every $S$ with
a nonzero coefficient has $|S|\le d$"), `Infl f i` ($\sum_{S\ni i}\hat
f(S)^2$), `flp i` (coordinate flip), `Relevant A`, `dens A`, `ind A`,
`nrm A` ($\mathbf 1_A/\sqrt\alpha$), `IsWindow d A W` (shattering window:
$|W|\le d$ and every off-$W$ pattern is realised in $A$), and `pay A B WA WB`
(the payment, each side charged on the **partner's** window).

## Round-trip of the load-bearing statements (Lean → English, diffed against u1–u3)

| Lean declaration | English | matches |
|---|---|---|
| `L1_nonvanishing` | a nonzero multilinear $f$ of degree $\le k$ is nonzero on at least a $2^{-k}$ fraction of the cube | u1/L1 ✔ |
| `L2_quantum` | $A\ne\emptyset$, $\deg\mathbf 1_A\le d$, $i$ relevant $\Rightarrow$ $\mathrm{Inf}_i(\mathbf 1_A)\ge 2^{-(d+1)}$ | u1/L2 ✔ |
| `L4_positivity` | $B\ne\emptyset$, $A\cap B=\emptyset$, $W$ a shattering window of $A$ $\Rightarrow$ some $i\in W$ is relevant for $B$ | u1/L4 ✔ (note: no degree hypothesis on $A$ or $B$ appears, exactly as in u1) |
| `L5_count` | for pair-independent windows of size $\le\omega$ and per-coordinate average influences $\le\delta_F,\delta_G$, the *expected* payment under the product distribution is $\le(\delta_F+\delta_G)\omega$ | u1/L5 ✔ |
| `T1_reduction` | if every cross-disjoint pair in the two supports pays $\ge p$ on the pair-independent windows, and $2\delta\omega<p$, then some pair of sets is **not** disjoint (= the R2 conclusion for indicators) | u1/T1 ✔ |
| `T2_payment` | every cross-disjoint degree-$\le d$ pair pays $\ge 2^{1-d}$ on any pair of shattering windows | u1/T2(a) ✔ |
| `T3_deg`, `T3_window`, `T3_payment` | the family $\mathsf A_d,\mathsf B_d=\mathsf A_d^c$ on $d+1$ coordinates has degree $d$ on both sides, the block $U$ is a shattering window of both, and the payment there is exactly $d\,2^{1-d}$ | u2/L6,T3 ✔ |

Two conventions to note for a future formalizer, both deliberate: (i) the
distributions are modelled as weight vectors on finite index types
(`Fintype ιF`), which is I02's finitely-supported reading; (ii) the R2
conclusion is rendered as `¬ Disjoint (AF a) (AG b)`, which for normalized
indicators is *equivalent* to $\exists x,\ f(x)g(x)\ne0$ and avoids carrying
$\sqrt\alpha$ through the statement.

## What the skeleton did and did not buy

* **Did:** confirmed that every statement in units 1–3 is expressible with no
  hidden quantifier and that none of them is accidentally vacuous or
  ill-typed; in particular that `IsWindow` (card S7b's conclusion) and `pay`
  (the partner-window sum) can be stated without reference to the *pair*, which
  is the property L5 needs.
* **Did not:** prove anything. Nine `sorry`s; `#print axioms` was not run
  because no theorem is closed. No Lean-side check of T3's arithmetic — that is
  the Python certificate of u2.

EMITTED unit 4 of 5; NEXT UNIT: Final — assembled self-contained artifact
`0023-prover-2.md`, gap register, dependencies, STAGE HANDOFF.

### END OF ARTIFACT 0023-prover-2-u4 ###
