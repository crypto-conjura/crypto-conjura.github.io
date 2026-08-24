# PROBLEM CONTRACT

## Notation

* `n ∈ N` is the ambient dimension; `S^{n-1} = { v ∈ R^n : ‖v‖₂ = 1 }` is the
  real unit sphere.
* For `A ∈ R^{n×n}`, `‖A‖_F = (Σ_{i,j} A_{i,j}²)^{1/2}` is the Frobenius norm.
* `L ∈ R^{n×n}` is *rank one* if `L = ab^T` for some `a,b ∈ R^n`; it is
  *nonzero* if `L ≠ 0`.
* `μ` denotes a Borel probability measure on `S^{n-1}`, and `r : S^{n-1} → R` a
  Borel measurable function that is **not** required to be nonnegative.
* `E_{v∼μ}[ r(v) v v^T ]` denotes the `n × n` matrix whose `(i,j)` entry is
  `E_{v∼μ}[ r(v) v_i v_j ]`.
* `ε > 0` is the accuracy parameter (relative Frobenius distance to rank one)
  and `δ > 0` is the entropy exponent.
* Throughout, `0 log 0 := 0`.

## Definition (signed reweighting and its entropy cost)

Let `μ` be a Borel probability measure on `S^{n-1}` and let `K ≥ 0`. A Borel
measurable function `r : S^{n-1} → R` is a *signed reweighting of `μ` with
entropy cost at most `K`* if `r` is `μ`-integrable and

    E_{v∼μ} |r(v)| = 1 ,
    E_{v∼μ} [ |r(v)| log |r(v)| ] ≤ K .

If in addition `r ≥ 0` holds `μ`-almost everywhere, then `r` is a *nonnegative*
reweighting; in that case `dμ' := r dμ` is a probability measure and the entropy
cost is exactly the Kullback–Leibler divergence `Δ_KL(μ' ‖ μ)`.

## THE STATEMENT TO BE PROVED OR REFUTED

For every `ε > 0` and every `δ > 0` there exists a finite constant
`C = C(ε,δ)` such that the following holds for every `n ∈ N` and every Borel
probability measure `μ` on `S^{n-1}`: there exist a signed reweighting `r` of
`μ` with entropy cost at most `C · n^δ` (in the sense of the Definition above)
and a **nonzero** rank one matrix `L ∈ R^{n×n}` such that

    ‖ E_{v∼μ}[ r(v) v v^T ] − L ‖_F  ≤  ε ‖L‖_F .

## Reading conventions fixed by this Contract

1. **Quantifier placement on the constant.** The entropy bound `O(n^δ)` hides a
   constant that may depend on `ε` and `δ` but *not* on `n` or `μ`. That
   constant is `C(ε,δ)` above. A solver should track the dependence of `C` on
   `ε` rather than treat it as free.
2. **Regularity.** `r` is required to be Borel measurable and `μ`-integrable.
   No further regularity is assumed, and none may be added.
3. **`L` is not required to be symmetric or PSD**, only rank one and nonzero.
   The accuracy requirement is *relative* to `‖L‖_F`.

## Known boundary

The statement restricted to nonnegative `r` is established for `δ ≥ 1/2`, and
is tight there: the exponent `1/2` cannot be improved while `r ≥ 0` is imposed.
The regime `δ < 1/2` is the content of the question, and requires cancellation.
