# Source card S1 — Coretti, Dodis, Guo, Steinberger, *Random Oracles and Non-Uniformity*

ePrint 2017/937 (version dated 8 August 2022); EUROCRYPT 2018. Read from a local PDF copy.

## Definition 1 (p. 10, verbatim in substance)

An $(N,M)$-source is a random variable $X$ with range $[M]^{N}$. A source is called

- $(1-\delta)$-dense if for every subset $I\subseteq[N]$, $H_\infty(X_I)\ge(1-\delta)\cdot|I|\cdot\log M$;
- $(P,1-\delta)$-dense if it is fixed on at most $P$ coordinates and is $(1-\delta)$-dense on the rest;
- $P$-bit-fixing if it is fixed on at most $P$ coordinates and uniform on the rest.

## Claim 2 (p. 10; proof in Appendix A, p. 40)

*Let $X$ be uniform over $[M]^{N}$, $Z:=f(X)$ for arbitrary $f:[M]^N\to\{0,1\}^S$, $X_z$ the
law of $X$ conditioned on $f(X)=z$, and $S_z:=N\log M-H_\infty(X_z)$. For every $\delta>0$,
$X_z$ is $\gamma$-close to a convex combination of finitely many $(P',1-\delta)$-dense
sources, for $P'=(S_z+\log 1/\gamma)/(\delta\cdot\log M)$.*

**What the proof establishes, beyond the statement.** The proof takes $Y:=X_z$, picks the
largest $I$ admitting $y_I$ with $\Pr[Y_I=y_I]>2^{-(1-\delta)|I|\log M}$, splits off
$Y':=Y\mid Y_I=y_I$, and recurses on $Y\mid Y_I\neq y_I$ while
$\Pr[X\in\mathrm{supp}(Y)]>\gamma$. Three consequences are used in this campaign and are
visible in that argument:

1. **Only the min-entropy deficiency is used.** Claim 25 (density of $Y'_{\bar I}$) uses only
   maximality of $I$; Claim 26 ($|I|\le S/(\delta\log M)$) uses only $H_\infty(Y)\ge N\log M-S$;
   the recursion's invariant $H_\infty(Y)\ge N\log M-(S+\log1/\gamma)$ uses only
   $\Pr[Y=y]=\Pr[X=y\mid X\in\mathrm{supp}(Y)]$. Nowhere is it used that $X_z$ is a
   conditioning of a uniform variable by a deterministic function. The claim therefore holds
   for any distribution on $[M]^N$ of min-entropy deficiency $S_z$.
2. **The components have pairwise disjoint supports**, since each step removes
   $\mathrm{supp}(Y')$ from the current support before recursing. Hence the index of the
   component containing a sampled $x$ is a deterministic function of $x$.
3. **Fixed values are values the sample takes**: the component fixes $I$ to $y_I$ and is
   supported on $\{x:x_I=y_I\}$.

## Claim 3 (p. 10, proved p. 11)

*For any $(P',1-\delta)$-dense source $X'$ and its corresponding $P'$-bit-fixing source $Y'$
— fixed on the same coordinates to the same values — and for any (adaptive) distinguisher
$D$ that queries at most $T$ coordinates of its oracle,*
$$\bigl|\Pr[D^{X'}=1]-\Pr[D^{Y'}=1]\bigr|\ \le\ T\delta\cdot\log M,$$
*and $\Pr[D^{X'}=1]\le M^{T\delta}\cdot\Pr[D^{Y'}=1]$.*

The proof is an H-coefficient argument on transcripts: $p_{X'}(\tau)\le M^{-(1-\delta)T}$ and
$p_{Y'}(\tau)=M^{-T}$, whence the statistical distance of transcripts is at most
$1-M^{-T\delta}\le T\delta\log M$. It assumes without loss of generality that $D$ is
deterministic and does not query fixed positions.

## Lemma 1 (p. 10) — recorded for completeness, not used

*Let $X$ be uniform over $[M]^N$ and $Z:=f(X)$ with $f:[M]^N\to\{0,1\}^S$. For any $\gamma>0$
and $P\in\mathbb N$ there is a family $\{Y_z\}_{z\in\{0,1\}^S}$ of convex combinations of
$P$-bit-fixing $(N,M)$-sources such that for any distinguisher $D$ taking an $S$-bit input
and querying at most $T<P$ coordinates,*
$$\bigl|\Pr[D^{X}(f(X))=1]-\Pr[D^{Y_{f(X)}}(f(X))=1]\bigr|\ \le\ \frac{(S+\log1/\gamma)\cdot T}{P}+\gamma.$$

This packaged form is **not** what this campaign uses, for two reasons: its family is indexed
by the advice alone, so the decomposed oracle is drawn independently of the real one and is
not consistent with it; and its Claim 4, which bounds $\mathbb E_z[S_z]\le S$, relies on $Z$
being a deterministic function of $X$, which fails for randomised leakage. Claims 2 and 3 are
used directly instead.
