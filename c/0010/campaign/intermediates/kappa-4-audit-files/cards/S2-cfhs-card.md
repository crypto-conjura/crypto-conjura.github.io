# Source card S2 — Coretti, Farshim, Harasser, Southern, *Multi-Source Randomness Extraction and Generation in the Random-Oracle Model*

ePrint 2025/1258; ITC 2025, LIPIcs 343, art. 10. Read from a local PDF copy.

## Setting (pp. 9–10)

$\mathrm{Fun}(N^{\ell},M)$; a source $S$ returns $(x,z)\in[N]\times\{0,1\}^{*}$; all parties
are unbounded and have oracle access to $H$. $S$ is $(q,\delta)$-unpredictable if every
predictor making at most $q$ oracle calls, on input the source's own leakage $z$, guesses
$x$ with probability at most $\delta$. The multi-source-extraction game draws
$H\gets_{\$}\mathrm{Fun}(N^{\ell},M)$, runs each $S_i$ to get $(x_i,z_i)$, sets
$y_0\gets_{\$}[M]$ and $y_1\gets H(x)$, and returns whether $D^{H}(y_b,z)$ guesses $b$;
$\mathsf{Adv}^{\mathrm{mse}}=2\Pr[\cdot]-1$. With $\ell=2$ this is exactly the Contract's
$\kappa$, up to the factor-of-two convention.

## Lemma 3, flat decomposition (p. 8)

*Let $k\in\mathbb R_{>0}$ with $2^{k}\in\mathbb N$. Then every $k$-source $X$ is a convex
combination of flat $k$-sources: $X=\sum p_iX_i$ with $p_i\ge0$, $\sum p_i=1$, each $X_i$
uniform on a subset of size $2^{k}$.* Here a $k$-source satisfies $\Pr[X=x]\le2^{-k}$ for
every $x$, and a flat $k$-source is uniform on a set of size exactly $2^{k}$. Attributed
there to reference [33].

## Lemma 4.3, binomial bounds (p. 8)

*For $k,n\in\mathbb N$ with $0<k\le n$, $(n/k)^{k}\le\binom nk\le(en/k)^{k}$.*

## Theorem 3, MSE (p. 28)

*Let $\ell,M,N,q_D\in\mathbb N$ and $k\in\mathbb R_{>0}$. For every tuple
$S=(S_1,\dots,S_\ell)$ of sources, each $(N^{\ell},2^{-k})$-unpredictable and with unbounded
oracle access, and every distinguisher $D$ making at most $q_D$ oracle calls,*
$$\mathsf{Adv}^{\mathrm{mse}}_{S,D}=O\Bigl(\ell\log M\ \sqrt[\ell+1]{\tfrac{q_D}{2^{k\ell}}\,(\sigma+\ell N)}\Bigr),$$
*where $\sigma\ge\sum_i\sigma_i$ bounds the total leakage length.*

Obtained by compression: Yao's equivalence turns a distinguisher into a next-bit predictor,
which is split according to whether it queries the challenge point, the first case going
through their Theorem 2 (unrecoverability) and the second through an incompressibility
argument; the sources' oracle-dependence is handled by decomposing them into flat sources.

**Two observations recorded against this statement.** Its right-hand side vanishes at
$q_D=0$, whereas the query-free extraction advantage is nonzero in general; it is therefore
read here as intended for $q_D\ge1$. And the constant hidden in the $O(\cdot)$ is not
extracted in the paper, so any bound quoting it is asymptotic.

## Section 1.4, the decomposition question (pp. 6–7)

The paper states that compression does not transfer to non-monolithic constructions such as
Merkle–Damgård or Sponge, and asks whether CDGS or Unruh decomposition can be run in the
multi-source setting. It rules out the naive route — running CDGS in parallel on $z_1$ and
$z_2$ and fixing the union — with the example $z_1:=\sum_{1\neq x\in[N]}H(x)$,
$z_2:=\sum_{x\in[N]}H(x)$: jointly the pair reveals $H(1)$, while individually neither leaks
anything about any particular point, so parallel decomposition fixes nothing. It conjectures
that parallel decomposition is possible under appropriate restrictions and leaves it open.
