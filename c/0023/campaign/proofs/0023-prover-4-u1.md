id: 0023-prover-4-u1
agent: prover
model: claude-opus-5[1m] (Opus 5, 1M context)
cycle: 4
status: COMPLETE

## Conventions fixed

Cube `{±1}^N` with the uniform measure; `E` and all Fourier expansions are with
respect to it. For `g : {±1}^S → R` we write `g = Σ_{T⊆S} ĝ(T) χ_T`,
`Inf_i(g) = Σ_{T∋i} ĝ(T)²`, `Var[g] = Σ_{T≠∅} ĝ(T)² = ‖g‖₂² − ĝ(∅)²`.

**C1 (indicator convention).** `1_A` is **{0,1}-valued**. So `‖1_A‖₂² = E[1_A²] =
E[1_A] = α`, `1̂_A(∅) = α`, `Var[1_A] = α − α² = α(1−α)`.

**C2 (degree).** `deg(1_A)` is the degree of the unique multilinear
representation. `deg` is unchanged by a nonzero affine rescaling of the values.

**C3 (fibre normalisation).** For a fibre `A_w ⊆ {±1}^W` we normalise by the
**fibre density** `a_w = |A_w|/2^{|W|}`, *not* by the global density `α`:
`f_{A_w} := 1_{A_w}/√(a_w)`, viewed as a function on `{±1}^W` with the uniform
measure on `{±1}^W`. This is the normalisation that makes `‖f_{A_w}‖₂ = 1`;
normalising by `α` would give `‖·‖₂² = a_w/α ≠ 1` in general and would break L3.

Throughout `(A,B)` is cross-disjoint: `A,B ≠ ∅`, `A ∩ B = ∅`,
`deg(1_A), deg(1_B) ≤ d`. `τ = c/(2d⁴)`, `W = W_τ(A) ∪ W_τ(B) ⊇ M(A) ∪ M(B)`.

---

## Lemma 0 (affine transfer of (F5)) — resolves the {0,1}-vs-{±1} question

*Let `h : {±1}^N → R` and `g = s + t·h` with `t ≠ 0`. Then for every `i`,
`Inf_i(g) = t²·Inf_i(h)`, `Var[g] = t²·Var[h]`, and `deg(g) ≤ deg(h)`.*

**Proof.** By uniqueness of the multilinear expansion, `ĝ(∅) = s + t·ĥ(∅)` and
`ĝ(T) = t·ĥ(T)` for every `T ≠ ∅`. Every `T ∋ i` is nonempty, so
`Inf_i(g) = Σ_{T∋i} t²ĥ(T)² = t² Inf_i(h)`; likewise
`Var[g] = Σ_{T≠∅} t²ĥ(T)² = t² Var[h]`. The support of `ĝ` is contained in that
of `ĥ` together with `∅`, so `deg(g) ≤ deg(h)`. ∎

**Consequence.** The ratio `max_i Inf_i(·) / Var[·]` is *invariant* under nonzero
affine rescaling, and the degree does not increase. Hence (F5) holds for
`{0,1}`-valued indicators **whichever** convention its "Boolean" means: if (F5)
is stated for `{±1}`-valued `g`, apply it to `g := 1 − 2·1_A` (which is
`{±1}`-valued, has `deg(g) ≤ deg(1_A) ≤ d` by Lemma 0 with `s=1, t=−2`), obtaining
`max_i Inf_i(g) ≥ c·Var[g]/d⁴`; dividing both sides by `t² = 4` and using Lemma 0
gives `max_i Inf_i(1_A) ≥ c·Var[1_A]/d⁴`. If instead (F5) already means
`{0,1}`-valued, this is (F5) verbatim. **No gap.**

---

## L1 (Heaviness)

**Statement.** `A ∩ B = ∅` forces `α + β ≤ 1`, hence `min(α,β) ≤ 1/2`. If
`α ≤ 1/2` then `H_τ(A) ≠ ∅`; symmetrically for `B`.

**Proof.** First, `α + β = |A|/2^N + |B|/2^N = |A ∪ B|/2^N ≤ 1` by disjointness,
so `min(α,β) ≤ 1/2`.

Assume `α ≤ 1/2`. Since `A ≠ ∅` we have `α > 0`, and `α ≤ 1/2 < 1` forces
`N ≥ 1` (for `N = 0` the cube is a single point and every nonempty `A` has
`α = 1`). So the index set is nonempty and `Var[1_A] = α(1−α) > 0`.

By the Consequence of Lemma 0, `max_i Inf_i(1_A) ≥ c·α(1−α)/d⁴`.

Since `α > 0`, `f_A = 1_A/√α` is the case `s = 0, t = α^{−1/2}` of Lemma 0, so
`Inf_i(f_A) = Inf_i(1_A)/α` for every `i`. Therefore

  `max_i Inf_i(f_A) = (1/α)·max_i Inf_i(1_A) ≥ c·(1−α)/d⁴ ≥ c·(1/2)/d⁴ = c/(2d⁴) = τ`,

using `1 − α ≥ 1/2`. Any maximising `i` satisfies `Inf_i(f_A) ≥ τ`, i.e.
`H_τ(A) ≠ ∅`. ∎

(Note `α` cancels exactly, as intended: the `α` from `Var[1_A]` against the `α`
in the normalisation of `f_A`.)

---

## Sub-fact S (density floor for a degree-≤d set)

*Let `n ≥ 0` and let `∅ ≠ C ⊆ {±1}^n` have `deg(1_C) ≤ d`. Then
`|C|/2^n ≥ 2^{−deg(1_C)} ≥ 2^{−d}`.*

**Proof.** Put `D = deg(1_C) ≤ d` and let `M(C)`, `|M(C)| = D`, be the support of
a maximum-degree monomial of `1_C`. By (F2), `C` projects **onto**
`{±1}^{[n]\M(C)}`: every one of the `2^{n−D}` patterns off `M(C)` is realised by
some point of `C`. Distinct patterns come from distinct points, so
`|C| ≥ 2^{n−D}` and `|C|/2^n ≥ 2^{−D} ≥ 2^{−d}`. ∎

---

## L2 (Uniform fibre floor)

**Statement.** For every `w ∈ {±1}^{[N]\W}`: `A_w ≠ ∅`, `a_w ≥ 2^{−d}`;
`B_w ≠ ∅`, `b_w ≥ 2^{−d}`; and `A_w ∩ B_w = ∅`. Consequently
`2^{−d} ≤ a_w ≤ 1 − 2^{−d}` and likewise for `b_w`.

**Proof.** Fix `w`. (If `W = [N]` the only `w` is the empty pattern, `A_w = A`,
and every claim below reads correctly.)

*(i) `A_w ≠ ∅`.* By definition `M(A) ⊆ W_τ(A) ⊆ W`, hence
`[N]\W ⊆ [N]\M(A)`. By (F2) applied to `A`, the projection
`π : A → {±1}^{[N]\M(A)}` is surjective. Let `u ∈ {±1}^{[N]\M(A)}` be any pattern
whose restriction to `[N]\W` equals `w` (one exists: extend `w` arbitrarily on
`W\M(A)`). Surjectivity gives `x ∈ A` with `x|_{[N]\M(A)} = u`, hence
`x|_{[N]\W} = w`. So `x|_W ∈ A_w`.

*(ii) `a_w ≥ 2^{−d}`.* Consider `g_w : {±1}^W → R`, `g_w(y) := 1_A(y, w)`, the
restriction of the multilinear polynomial `1_A` obtained by substituting the
constants `w` for the variables indexed by `[N]\W`. Substituting constants into a
multilinear polynomial and re-expanding yields a multilinear polynomial in the
remaining variables in which every monomial is a sub-monomial of an original one;
hence `deg(g_w) ≤ deg(1_A) ≤ d`. Also `g_w(y) = 1` iff `(y,w) ∈ A` iff
`y ∈ A_w`, so `g_w = 1_{A_w}` and `deg(1_{A_w}) ≤ d` as a function on `{±1}^W`.
By (i) `A_w ≠ ∅`, so Sub-fact S in dimension `n = |W|` gives `a_w ≥ 2^{−d}`.

*(iii) `B`.* Identical, using `M(B) ⊆ W_τ(B) ⊆ W`: `B_w ≠ ∅`, `b_w ≥ 2^{−d}`.

*(iv) Disjointness.* If `y ∈ A_w ∩ B_w` then `(y,w) ∈ A` and `(y,w) ∈ B`,
contradicting `A ∩ B = ∅`. So `A_w ∩ B_w = ∅`, whence `a_w + b_w ≤ 1` and
therefore `a_w ≤ 1 − b_w ≤ 1 − 2^{−d}` (and symmetrically for `b_w`). ∎

---

## L3 (Fibre total)

**Statement.** For every `w ∈ {±1}^{[N]\W}`, with `f_{A_w} = 1_{A_w}/√(a_w)` as
in C3,

  `Σ_{i∈W} Inf_i(f_{A_w}) ≥ 1 − a_w ≥ 1 − (1 − 2^{−d}) = 2^{−d}`.

**Proof.** By L2, `a_w > 0`, so `f_{A_w}` is defined. It is a function on
`{±1}^W`, so its Fourier expansion is supported on subsets `T ⊆ W`.

Norm and mean: `‖1_{A_w}‖₂² = E_{y∈{±1}^W}[1_{A_w}(y)²] = E[1_{A_w}] = a_w`, and
`1̂_{A_w}(∅) = E[1_{A_w}] = a_w`. Hence `‖f_{A_w}‖₂² = a_w/a_w = 1` and
`f̂_{A_w}(∅) = a_w/√(a_w) = √(a_w)`, so `f̂_{A_w}(∅)² = a_w`. By Parseval the
total non-constant weight is
`Σ_{∅≠T⊆W} f̂_{A_w}(T)² = ‖f_{A_w}‖₂² − f̂_{A_w}(∅)² = 1 − a_w`.

Now exchange sums (all terms nonnegative):

  `Σ_{i∈W} Inf_i(f_{A_w}) = Σ_{i∈W} Σ_{T∋i} f̂_{A_w}(T)² = Σ_{∅≠T⊆W} |T|·f̂_{A_w}(T)² ≥ Σ_{∅≠T⊆W} f̂_{A_w}(T)² = 1 − a_w`,

using `|T| ≥ 1` for `T ≠ ∅`. Finally L2(iv) gives `a_w ≤ 1 − 2^{−d}`, so
`1 − a_w ≥ 2^{−d}`. ∎

**Exact bound obtained.** `Σ_{i∈W} Inf_i(f_{A_w}) ≥ 1 − a_w ≥ 2^{−d}`, and the
same for `B` with `b_w`. The `2^{−d}` floor uses the *cross-disjointness*
(through `b_w ≥ 2^{−d}`), not just `A`.

---

## GAP REGISTER

None. All three lemmas are proved in full for all `d ≥ 0` and all `N ≥ 0`.

Two points that were live risks and are now closed:

1. **(F5) convention.** Closed by Lemma 0: `max_i Inf_i/Var` is affine-invariant
   and degree does not increase, so (F5) transfers between the `{0,1}` and `{±1}`
   conventions with no loss of constant. L1 is therefore unconditional in `c`.
2. **Fibre normalisation.** L3 normalises by `a_w` (C3), the only choice making
   `f_{A_w}` unit-`ℓ₂`; normalising by the global `α` would give
   `‖·‖₂² = a_w/α` and the displayed identity would fail.

Facts used: (F2) in Sub-fact S and L2(i); (F5) in L1. (F1) is used only for the
cited bound `|W_τ(·)| = O(d⁵)`, which is not needed in L1–L3. (F4) unused.

### END OF ARTIFACT 0023-prover-4-u1 ###
