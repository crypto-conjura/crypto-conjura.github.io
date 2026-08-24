# SOURCE CARD S1 — Barak, Kothari, Steurer, arXiv:1701.06321v2

*Quantum entanglement, sum of squares, and the log rank conjecture*, STOC 2017;
arXiv:1701.06321v2, 9 July 2017. Quotations below are verbatim from the text
layer of the published PDF (`pdftotext -layout`), with the page as printed.

## Q1 — Question 8.1, p. 19 (verbatim)

> Is it the case that for every distribution `µ` over `S^{n−1}` and every
> `ε, δ > 0` there is a (not necessarily positive) function `r : S^{n−1} → R`
> such that `E_{v∼µ}|r(v)| = 1`, `E_{v∼µ}|r(v)| log |r(v)| ⩽ O(n^δ)` and a
> nonzero rank one `L` such that `‖E_{v∼µ}[r(v)vv^⊤] − L‖_F ⩽ ε‖L‖_F` ?

Immediately following, p. 19 (verbatim):

> A positive solution for Question 8.1 for any `δ < 1/2` would be very
> interesting. It may improve the best known bound for the log rank conjecture
> to `Õ(n^δ)` and if appropriately extended to pseudo-distributions, improve our
> algorithm's running time to `exp(Õ(n^δ))` as well. We do know that the answer
> to this question is No if one does not allow negative reweighting functions.

## Q2 — Theorem 2.3 ("Rank one reweighting"), p. 5 (verbatim)

> Let `µ` be any distribution over rank one `n × n` matrices and `ε > 0`. Then
> there exists an `√n poly(1/ε)`-deficient reweighting `µ′` of `µ` and a rank one
> matrix `L` such that `‖L − Ẽ_{µ′} X‖_F ⩽ ε‖L‖_F`

## Q3 — Theorem 2.4 (dual formulation), p. 5 (verbatim)

> Let `A` be any `N × N` matrix of rank at most `n`. Then there exists a subset
> `I ⊆ [N]` with `|I| ⩾ exp(−√n poly(1/ε))N` and a rank one matrix `L` such that
> `‖L − A_{I,I}‖_F ⩽ ε‖L‖_F` where `A_{I,I}` is the submatrix corresponding to
> restricting the rows and columns of `A` to the set `I`.

## Q4 — the flatness dictionary, §2.2, p. 5 (verbatim)

> a flat distribution `µ′` with `Δ_KL(µ′‖µ) ⩽ k` corresponds to the uniform
> distribution over `{u_i v_i^⊤}_{i∈I}` where `I ⊆ [N]` satisfies `|I| ⩾ 2^{−k}N`

## Q5 — tightness remark, p. 6 (verbatim)

> It can be shown that as stated, Theorem 2.3 is tight. However there are
> different notions of being "close to rank one" that could be useful in both
> the log-rank and the quantum separability setting, for which there is hope to
> obtain substantially improved quantitative bounds.

## Q6 — footnote 7, p. 6 (verbatim)

> We note a caveat that this depends on the notion of "approximate" used.
> Gavinsky and Lovett [GL14] showed that to prove the log rank conjecture it
> suffices to find a in a rank `n` Boolean matrix a rectangle of measure
> `exp(− polylog(n))` that is nearly monochromatic in the sense of having a
> `1 − 1/O(n)` fraction of its entries equal. In this paper we are more concerned
> with rectangles whose distance to being rank one (or monochromatic) is some
> `ε > 0` that is only a small constant or `1/ polylog(n)`.

## Q7 — footnote 8, p. 19 (verbatim)

> As mentioned in Footnote 7, improving the bounds on the log rank conjecture
> might require better control of the dependence of the bound on `ε` than we
> need for our setting.

## Q8 — normalisation of the columns, §2.3, p. 6 (verbatim)

> We will restrict our attention to the case that all the columns of `U` and `V`
> are of unit norm. (This restriction is easy to lift and anyway holds
> automatically in our intended application.)

## Q9 — Definition 2.2 ("k-deficient reweighting"), p. 5 (verbatim)

> Let `µ` be a probability distribution. We say that a probability distribution
> `µ′` is a `k`-deficient reweighting of `µ` if `∆_KL(µ′‖µ) ⩽ k` where
> `∆_KL(µ′‖µ)` denotes the Kullback-Leibler divergence of `µ′` and `µ`, defined
> as `E_{X∼µ′} log(µ′(X)/µ(X))`.

Note for anyone using Q2: "deficient" is defined here only for a *probability
distribution* `µ′`, so a `k`-deficient reweighting is by definition nonnegative
(it is a probability distribution) and normalised. This is the definition the
term in Theorem 2.3 (Q2) carries. It is distinct from "flat" (Q4).
