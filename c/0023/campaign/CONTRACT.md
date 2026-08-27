# PROBLEM CONTRACT — c/0023

## Polynomial Compatibility Conjecture (PCC), inverse-polynomial influence regime

**Depth:** 0 (original statement; no descent).
**Canonical source:** Conjecture stated by Austrin, Chung, Chung, Fu, Lin, Mahmoody, *On the Impossibility of Key Agreements from Quantum Random Oracles*, ePrint 2022/218 / CRYPTO 2022 [ACC22]; consumed in the inverse-polynomial regime by Chung, Lin, Mahmoody, *Black-Box Separations for Non-Interactive Commitments in a Quantum World*, ePrint 2023/570 [CLM23]. Statement below is verbatim from this repository's `c/0023/latex/main.tex` (AI-written from [CLM23], not yet checked by a human — treat exact correspondence with [ACC22]'s printed conjecture as a fact the Scout must confirm).

## Notation

* `𝒴` is a finite abelian group; `𝒴̂` its dual group, whose elements are the
  characters `χ : 𝒴 → ℂ^×`; the trivial character is `0̂`.
* `N ∈ ℕ` is the number of coordinates, `[N] = {1,…,N}`; an input is
  `x = (x_1,…,x_N) ∈ 𝒴^N`.
* For `χ = (χ_1,…,χ_N) ∈ 𝒴̂^N`, `χ(x) := ∏_{i=1}^N χ_i(x_i)`. These `|𝒴|^N`
  functions form an orthonormal basis of `{f : 𝒴^N → ℂ}` under
  `⟨f,g⟩ := E_{x←𝒴^N}[f(x) conj(g(x))]` (uniform `x`), so every `f` has a unique
  Fourier expansion `f = Σ_{χ∈𝒴̂^N} f̂(χ) χ` with `f̂(χ) ∈ ℂ`.
* `‖f‖_2 := (E_{x←𝒴^N} |f(x)|²)^{1/2}` — the `ℓ_2` norm under the uniform
  distribution on `𝒴^N` (normalized, not counting measure).
* `𝐅, 𝐆` denote probability distributions over functions `𝒴^N → ℂ`;
  `supp(𝐅)` is the set of functions to which `𝐅` assigns non-zero probability.

## Definitions (degree and influence over a finite abelian group)

For `f : 𝒴^N → ℂ` with Fourier expansion `f = Σ_χ f̂(χ) χ`:

* The **degree** of a character `χ = (χ_1,…,χ_N) ∈ 𝒴̂^N` is
  `deg(χ) := |{ i ∈ [N] : χ_i ≠ 0̂ }|`, and
  `deg(f) := max{ deg(χ) : f̂(χ) ≠ 0 }`, with `deg(f) := 0` for `f ≡ 0`.
* The **influence** of coordinate `i ∈ [N]` on `f` is
  `Inf_i(f) := Σ_{χ : χ_i ≠ 0̂} |f̂(χ)|²`.

For `𝒴 = ℤ_2` these specialise to the usual notions for multilinear
polynomials `f = Σ_{S⊆[N]} α_S ∏_{i∈S} x_i` over `x_i ∈ {±1}`:
`deg(f) = max_{α_S≠0} |S|` and `Inf_i(f) = Σ_{S∋i} α_S²`.

## THE STATEMENT TO BE PROVED OR REFUTED

Verbatim (LaTeX) from `c/0023/latex/main.tex`, Conjecture `conj:main`:

```latex
There exist a finite abelian group $\cY$, constants $c_1\in(0,1]$ and
$c_2>0$, and a function $\delta\colon\NN\to(0,1]$ satisfying
$\delta(d)\ge c_1\,d^{-c_2}$ for all $d\ge 1$ --- equivalently,
$\delta(d)\ge 1/p(d)$ for some polynomial $p$ --- such that for every
$d\in\NN$ and every $N\in\NN$ the following holds.

Let $\bF$ and $\bG$ be any two probability distributions over functions
$\cY^N\to\CC$ such that:
\begin{itemize}
  \item \emph{unit $\ell_2$ norm:} $\lVert f\rVert_2 = 1$ for every
  $f\in\operatorname{supp}(\bF)$ and $\lVert g\rVert_2 = 1$ for every
  $g\in\operatorname{supp}(\bG)$;
  \item \emph{degree at most $d$:} $\deg(f)\le d$ for every
  $f\in\operatorname{supp}(\bF)$ and $\deg(g)\le d$ for every
  $g\in\operatorname{supp}(\bG)$;
  \item \emph{$\delta$-influences on average:} for every $i\in[N]$,
  \[
    \mathop{\mathbb{E}}_{f\sample\bF}\bigl[\operatorname{Inf}_i(f)\bigr]
      \ \le\ \delta(d) \quad\text{and}\quad
    \mathop{\mathbb{E}}_{g\sample\bG}\bigl[\operatorname{Inf}_i(g)\bigr]
      \ \le\ \delta(d).
  \]
\end{itemize}
Then there exist $f\in\operatorname{supp}(\bF)$,
$g\in\operatorname{supp}(\bG)$, and $x\in\cY^N$ such that
\[ f(x)\cdot g(x)\ \ne\ 0. \]
```

## Quantifier order, in words

Existentials first, chosen once and for all: a finite abelian group `𝒴`, constants
`c_1 ∈ (0,1]`, `c_2 > 0`, and a function `δ : ℕ → (0,1]` with `δ(d) ≥ c_1 d^{-c_2}`
for all `d ≥ 1`. Then universals: **every** `d ∈ ℕ`, **every** `N ∈ ℕ`, and
**every** pair `(𝐅, 𝐆)` of distributions satisfying the three hypotheses, where
the influence hypothesis uses the bound `δ(d)`. Then existentials again: **some**
`f ∈ supp(𝐅)`, **some** `g ∈ supp(𝐆)`, **some** `x ∈ 𝒴^N` with `f(x)·g(x) ≠ 0`.

Consequences a solver must respect:

* `δ` may depend on `d` but **never on `N`**. An `N`-dependent threshold proves
  a different (weaker) statement. This is the crux of the difficulty.
* The group is **existentially** quantified: a proof for any one finite abelian
  group (e.g. `ℤ_2`) settles the conjecture affirmatively.
* A refutation must therefore rule out **every** finite abelian group and
  **every** admissible `δ` (every `c_1, c_2`): for each `(𝒴, c_1, c_2, δ)` it
  must exhibit some `(d, N, 𝐅, 𝐆)` satisfying all hypotheses at bound `δ(d)`
  with `f(x)·g(x) = 0` for **all** `f ∈ supp(𝐅)`, `g ∈ supp(𝐆)`, `x ∈ 𝒴^N`.

## Asymptotic conventions

None. Nothing tends to infinity; the statement is exact, for every `d` and `N`.
`δ` is a single function of `d` fixed before `d`, `N`, `𝐅`, `𝐆` are chosen.

## Reading conventions fixed by this Contract

1. **Distributions are finitely supported**, and `supp(𝐅)` is the set of
   functions of positive probability. (In the source application the supports
   are finite; a continuous-measure reading under which every point has
   probability zero and `supp` is empty is a degenerate misreading and is
   excluded.) Resolved by the Scout 2026-08-27: neither [ACC22] nor [CLM23]
   prints a support restriction; this convention is Contract-added and benign
   (see K3′ below).
2. **The influence hypothesis is per-coordinate, on average over the
   distribution:** for every `i ∈ [N]`, `E_{f←𝐅}[Inf_i(f)] ≤ δ(d)`. It is NOT
   a bound on `max_{f∈supp} Inf_i(f)`, NOT a bound on `Σ_i`, and NOT "for some
   `i`".
3. **Unit norm and the degree bound hold pointwise on the support** (every
   function in either support, exactly).
4. `f(x)·g(x) ≠ 0` is exact non-vanishing at a single common point; no
   approximate or high-probability substitute counts.

## What counts as a solution

- [x] **Full proof:** exhibit one finite abelian group and one admissible
      inverse-polynomial `δ`, and prove the implication for all `d, N, 𝐅, 𝐆`.
- [x] **Disproof:** as pinned under "Quantifier order" above. A sufficient
      scheme: for every finite abelian group, a family of incompatible pairs
      `(𝐅_d, 𝐆_d)` whose maximal per-coordinate average influence `ε(d)` is
      smaller than every inverse polynomial along an infinite sequence of `d`
      (then every admissible `δ` is violated at some `d`).
- [x] **Named partials (valuable, but settle nothing):** raising the proved
      threshold for some group from exponentially small to, e.g.,
      `exp(-d^α)` (`α < 1`) or `exp(-polylog d)`; or lowering the refutation
      frontier (incompatible pairs with influence `o(1/d)`); or a proof for a
      declared restricted class (fixed small `d`; Boolean-valued functions;
      singleton or bounded-size supports; product-structured distributions) —
      each admissible only as an explicitly declared ladder rung with its own
      Contract, never reported against this one.

**NOT acceptable:**

* Any `δ` depending on `N`, however mildly.
* Replacing the average-influence hypothesis by a per-function
  (max-over-support) influence bound and calling the result the conjecture:
  that strengthens the hypothesis, hence proves a weaker statement.
* The vacuous continuous-support reading (convention 1).
* An infinite or non-abelian group.
* Restricting `d`, `N`, the value range of the functions, or the support
  sizes, unless declared as a ladder rung / weakening with its own Contract.

## Known results citable without proof

All of these enter proofs only through the source cards in `sources/`
(`S1-acc22-card.md`, `S2-clm23-card.md`); cite the cards, not this summary.
Confirmed by the Scout on 2026-08-27 (artifact `0023-scout-1`).

* **K1 [CONFIRMED — card S1]:** [ACC22] Theorem 4.4 (p. 20) proves the
  conjecture's analogue with the **strict** threshold `δ < |𝒴|^{-d}/d`, for
  **every** finite abelian group. Its proof (§5.2 there) uses no influence
  bound on `𝐅` and no degree bound on `𝐆` — an asymmetry a prover may
  exploit; see the card for the exact hypotheses.
* **K2 [CONFIRMED for ℤ_2 — card S1]:** [ACC22] Claim B.3 (p. 41): the
  NegRow/PosCol pair on `d×d` Boolean variables has degree `d`, all relative
  influences `≤ 1/(2d)`, singleton supports, and `f·g ≡ 0`. So over `ℤ_2` any
  witnessing `δ` must satisfy `δ(d) < 1/(2d)` for all `d` where this
  construction lives, and effectively `c_2 ≥ 1` for `ℤ_2`. **Printed for
  `ℤ_2` only** — the analogous window for other groups is not in print.
* **K3 [CONFIRMED — card S2]:** [CLM23] consumes the conjecture as its
  Conjecture 2.8 plus Definition 2.9 ((𝒴,δ,d,N)-quantum states) and the
  conversion Lemma 2.12, at `ε = δ(dκ)/10` — strictly the inverse-polynomial
  regime, `ℤ_2`-first.
* **K3′ (provenance, from the Scout):** the verbatim statement above is
  [CLM23] Conjecture 2.8 (ℂ-valued functions), not [ACC22]'s printed
  Conjecture 5.5 (ℝ-valued); the two are equivalent up to a factor 2 in `δ`
  ([ACC22] Thm 5.6 / App. A; [CLM23] fn. 8). The "finitely supported"
  convention (Reading convention 1) is Contract-added and benign — printed in
  neither source.
* **K4 (context only, not citable):** the Aaronson–Ambainis conjecture
  (arXiv:0911.0996) is the named kin and is **still open** (the Keller–Klein
  proof was retracted; Bhattacharya's ITCS 2025 random-restrictions variant,
  arXiv:2402.13952, is a for-some not a for-all statement). Three 2026 works
  (arXiv:2504.05710v2, 2608.03824, 2608.17610) *bypass* PCC in downstream
  applications — notably 2608.03824's unconditional O(q⁵) attack on perfectly
  complete QCCC key agreement — reducing PCC's downstream load without
  resolving it; [CLM23] and ePrint 2023/1720 still consume it.

## Known barriers / failed approaches

None formalized. The kinship with Aaronson–Ambainis (open since 2009 in the
regime analogous to this one) is the empirical difficulty marker. The
techniques behind K1 (if confirmed: per-character mass accounting compatible
with union bounds at exponential scale) reportedly do not survive at
inverse-polynomial scale; diagnosing exactly why is a Strategist deliverable,
not an assumption.

## BARRIER CHECKLIST (for the Strategist / Case Planner pre-check)

* Relativization / algebrization / natural proofs: **not applicable** — the
  statement is an unconditional Fourier-analytic claim about finite function
  spaces, not a complexity-class separation.
* Black-box / meta-reduction barriers: **not applicable to the statement
  itself**; they live in the downstream application ([CLM23]'s separations).
* No known barrier constrains proof techniques here. BARRIER-class plans
  (§3.2 class f) should target technique classes internal to the problem
  (e.g. "arguments using only per-coordinate influence budgets cannot beat
  exponential thresholds"), not the classical complexity barriers.

## Source library

Library: (empty — no cards yet). DECLINED: none.

## INTERPRETATION RULE

If any part of this Contract admits more than one reading, STOP and report it.
Do not resolve it yourself; do not pick the easiest reading.
