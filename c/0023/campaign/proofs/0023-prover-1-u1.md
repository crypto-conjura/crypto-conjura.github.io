---
id: 0023-prover-1-u1
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 1 of 8: Lemma 1)
---

# 0023-prover-1 — Unit 1: Lemma 1 (influence formula for normalized junta indicators)

Conventions as in Unit 0 (`0023-prover-1-u0.md`): uniform measure on
$\{\pm1\}^N$, $\chi_T(x)=\prod_{i\in T}x_i$ for $T\subseteq[N]$,
$\hat f(T)=\mathbb{E}_x[f(x)\chi_T(x)]$, $\mathrm{Inf}_i(f)=\sum_{T\ni i}\hat f(T)^2$;
for $\emptyset\ne P\subseteq\{\pm1\}^J$, $A=\{x\in\{\pm1\}^N:x_J\in P\}$,
$f_{J,P}=\mathbf 1_A/\|\mathbf 1_A\|_2$; $b_i(P)$ = number of $i$-edges of
$\{\pm1\}^J$ with exactly one endpoint in $P$ ($i\in J$); and for
$A\subseteq\{\pm1\}^N$, $\partial_i A$ = set of $i$-edges of $\{\pm1\}^N$ with
exactly one endpoint in $A$. For $x\in\{\pm1\}^N$, $x^{\oplus i}$ flips
coordinate $i$.

---

**Lemma 1 (influence formula).** Let $J\subseteq[N]$,
$\emptyset\ne P\subseteq\{\pm1\}^J$, and $f=f_{J,P}$. Then for every
$i\in[N]$:
$$\mathrm{Inf}_i(f)=\begin{cases}\dfrac{b_i(P)}{2|P|} & \text{if } i\in J,\\[4pt] 0 & \text{if } i\notin J.\end{cases}$$

*Proof.* The proof has four steps.

**Step 1 (well-definedness, orthonormality, Parseval).**
Since $P\ne\emptyset$, pick $u\in P$ and extend it arbitrarily to a point of
$\{\pm1\}^N$; that point lies in $A$, so $A\ne\emptyset$,
$\|\mathbf 1_A\|_2^2=|A|/2^N>0$, and $f$ is well defined (and
$\|f\|_2=1$ by construction).

For $T,T'\subseteq[N]$ we have $\chi_T\chi_{T'}=\chi_{T\triangle T'}$
(coordinates in $T\cap T'$ contribute $x_i^2=1$), and for any
$U\subseteq[N]$,
$\mathbb{E}_x[\chi_U(x)]=\prod_{i\in U}\mathbb{E}[x_i]=\mathbf 1[U=\emptyset]$
by independence of the coordinates and $\mathbb{E}[x_i]=0$. Hence
$\mathbb{E}[\chi_T\chi_{T'}]=\mathbf 1[T=T']$: the $2^N$ functions $\chi_T$
are orthonormal. Since they are $2^N$ orthonormal (hence linearly
independent) elements of the $2^N$-dimensional space of real functions on
$\{\pm1\}^N$, they form an orthonormal basis; every real $f$ has a unique
expansion $f=\sum_{T\subseteq[N]}\hat f(T)\chi_T$ with
$\hat f(T)=\mathbb{E}[f\chi_T]\in\mathbb{R}$, and for any real coefficients
$(c_T)$, Parseval holds:
$\mathbb{E}_x[(\sum_T c_T\chi_T(x))^2]=\sum_T c_T^2$ (expand and use
orthonormality; all sums are finite).

**Step 2 (flip identity).** Fix $i\in[N]$. For every $T\subseteq[N]$,
$\chi_T(x^{\oplus i})=\chi_T(x)$ if $i\notin T$ and
$\chi_T(x^{\oplus i})=-\chi_T(x)$ if $i\in T$ (flipping $x_i$ negates exactly
the factors with $i\in T$). Therefore
$$f(x)-f(x^{\oplus i})=\sum_T \hat f(T)\bigl(\chi_T(x)-\chi_T(x^{\oplus i})\bigr)=2\sum_{T\ni i}\hat f(T)\chi_T(x).$$
By Parseval (Step 1) applied to the right-hand side,
$$\mathbb{E}_x\bigl[(f(x)-f(x^{\oplus i}))^2\bigr]=4\sum_{T\ni i}\hat f(T)^2=4\,\mathrm{Inf}_i(f),$$
i.e.
$$\mathrm{Inf}_i(f)=\tfrac14\,\mathbb{E}_x\bigl[(f(x)-f(x^{\oplus i}))^2\bigr].\tag{1.1}$$

**Step 3 (edge count for a normalized indicator).** For $f=\mathbf
1_A/\|\mathbf 1_A\|_2$,
$$(f(x)-f(x^{\oplus i}))^2=\frac{(\mathbf 1_A(x)-\mathbf 1_A(x^{\oplus i}))^2}{\|\mathbf 1_A\|_2^2}
=\begin{cases}\|\mathbf 1_A\|_2^{-2} & \text{if exactly one of }x,x^{\oplus i}\in A,\\ 0 & \text{otherwise.}\end{cases}$$
The set of $x$ such that exactly one of $x,x^{\oplus i}$ lies in $A$ is
exactly the set of endpoints of edges in $\partial_i A$; distinct edges are
disjoint (each point lies on exactly one $i$-edge), so this set has size
$2|\partial_i A|$. Hence
$$\mathbb{E}_x\bigl[(f(x)-f(x^{\oplus i}))^2\bigr]=\frac{1}{\|\mathbf 1_A\|_2^{2}}\cdot\frac{2|\partial_i A|}{2^N}
=\frac{2^N}{|A|}\cdot\frac{2|\partial_i A|}{2^N}=\frac{2|\partial_i A|}{|A|},$$
and with (1.1),
$$\mathrm{Inf}_i(f)=\frac{|\partial_i A|}{2|A|}.\tag{1.2}$$

**Step 4 (junta structure).** Identify $x\in\{\pm1\}^N$ with the pair
$(x_J,x_{J^c})\in\{\pm1\}^J\times\{\pm1\}^{[N]\setminus J}$; then
$A=\{x:x_J\in P\}$ corresponds to $P\times\{\pm1\}^{[N]\setminus J}$, so
$$|A|=|P|\cdot 2^{N-|J|}.\tag{1.3}$$

*Case $i\notin J$.* Then $(x^{\oplus i})_J=x_J$, so
$\mathbf 1_A(x^{\oplus i})=\mathbf 1_A(x)$ for all $x$; no $i$-edge has
exactly one endpoint in $A$, i.e. $|\partial_i A|=0$, and (1.2) gives
$\mathrm{Inf}_i(f)=0$.

*Case $i\in J$.* An $i$-edge of $\{\pm1\}^N$ is $\{x,x^{\oplus i}\}$ with
$x=(u,v)$, $x^{\oplus i}=(u^{\oplus i},v)$, where $u=x_J\in\{\pm1\}^J$ and
$v=x_{J^c}$; membership in $A$ depends only on the first component. So
$\{x,x^{\oplus i}\}\in\partial_i A$ iff exactly one of $u,u^{\oplus i}$ lies
in $P$, i.e. iff $\{u,u^{\oplus i}\}$ is one of the $b_i(P)$ boundary
$i$-edges of the window cube — and for each such window edge there are
exactly $2^{N-|J|}$ choices of $v$, each giving a distinct $i$-edge of
$\{\pm1\}^N$. Hence
$$|\partial_i A|=b_i(P)\cdot 2^{N-|J|}.\tag{1.4}$$
Substituting (1.3) and (1.4) into (1.2):
$$\mathrm{Inf}_i(f)=\frac{b_i(P)\,2^{N-|J|}}{2\,|P|\,2^{N-|J|}}=\frac{b_i(P)}{2|P|}. \qquad\blacksquare$$

---

**Remark 1.1 (non-load-bearing; I01's "automatic" clauses).**
(i) $\|f_{J,P}\|_2=1$ by construction (Step 1).
(ii) $\deg f_{J,P}\le|J|$: for $T\not\subseteq J$ pick $i\in T\setminus J$;
pairing each $x$ with $x^{\oplus i}$ leaves $f$ unchanged (Step 4, first
case) and negates $\chi_T$, so
$\hat f(T)=\mathbb{E}[f\chi_T]=-\mathbb{E}[f\chi_T]=0$. Hence the Fourier
support lies in subsets of $J$ and $\deg f\le |J|\le d$.
(iii) Consequently $\mathrm{Inf}_i(f)\ge0$ always (sum of squares), and
$\mathrm{Inf}_i(f)=0$ for $i\notin J$ also follows from (ii) — Step 4 proved
it directly.

**Sanity checks (evidence only, not proof).** Singleton pattern in a
$k$-dimensional window: $b_i=1$, $|P|=1$, so $\mathrm{Inf}_i=1/2$ for every
$i\in J$ — the classical relative influence of AND. Full pattern
$P=\{\pm1\}^J$: $b_i=0$, $f\equiv1$, all influences $0$. Consistent.

EMITTED unit 1 of 8; NEXT UNIT u2 (Lemma 2); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u1 ###
