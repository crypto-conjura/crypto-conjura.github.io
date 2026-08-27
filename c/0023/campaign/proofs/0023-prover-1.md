---
id: 0023-prover-1
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE
---

# 0023-prover-1 — Proof of intermediate I01 (rung R1: spread-junta indicators, ℤ₂)

## VERDICT: COMPLETE

The I01 statement is proved in full, for all $d$ and $N$, with the explicit
witnesses $c_1=1/3$, $c_2=1$, $\delta(d)=1/(3d)$. Every step is proved inline
from the parent Contract's definitions (specialized to
$\mathcal{Y}=\mathbb{Z}_2$ as I01 fixes); **no external result is used**; the
gap register is empty. I01's binding generalization hypothesis is met: the
proof is a weighted-counting (union-bound replacement) argument with an
inline isoperimetric payment lemma, linear in the distributions, with no
pattern enumeration and no constants of the form $2^{2^d}$. A non-load-bearing
remark (Remark 10.1) reproves inline that no $\delta(d)\ge1/(2d)$ can
witness the rung, so the result is within a factor $3/2$ of optimal.

*Assembled from units `0023-prover-1-u0.md` … `-u6.md` (method sketch and one
lemma per unit); this file is self-contained and supersedes none of them.*

---

## 0. Statement proved

**Statement (I01, verbatim).** There exist $c_1\in(0,1]$, $c_2>0$, and
$\delta:\mathbb{N}\to(0,1]$ with $\delta(d)\ge c_1 d^{-c_2}$ for all
$d\ge 1$, such that for all $d,N\in\mathbb{N}$ and all finitely supported
distributions $\mathbf{F},\mathbf{G}$ over the class

$$\mathcal{C}^{\mathrm{junta}}_d:=\Bigl\{\tfrac{\mathbf{1}_A}{\|\mathbf{1}_A\|_2}\ :\ A=\{x\in\{\pm1\}^N: x_J\in P\},\ J\subseteq[N],\ |J|\le d,\ \emptyset\ne P\subseteq\{\pm1\}^J\Bigr\}$$

satisfying, for every $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf{F}}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb{E}_{g\sim\mathbf{G}}[\mathrm{Inf}_i(g)]\le\delta(d)$,
there exist $f\in\mathrm{supp}\,\mathbf{F}$, $g\in\mathrm{supp}\,\mathbf{G}$,
and $x\in\{\pm1\}^N$ with $f(x)\,g(x)\ne 0$.

**We prove this with the explicit witnesses $c_1=1/3$, $c_2=1$,
$\delta(d)=1/(3d)$** (Theorem, §9).

## 1. Conventions and definitions

All definitions follow the parent Contract (`CONTRACT.md`) specialized to
$\mathcal{Y}=\mathbb{Z}_2$ with $\{\pm1\}$-coordinates, as I01 fixes.

* $\mathbb{N}=\{1,2,3,\dots\}$. (Conventions with $0\in\mathbb{N}$: see
  Remark 9.1; both degenerate cases are trivial.)
* $\{\pm1\}^N$ carries the uniform probability measure;
  $\langle f,g\rangle=\mathbb{E}_x[f(x)g(x)]$,
  $\|f\|_2=(\mathbb{E}_x f(x)^2)^{1/2}$. Real-valued functions suffice: every
  class member is real-valued (the Contract's $|\hat f(\chi)|^2$ becomes
  $\hat f(T)^2$).
* Fourier: for $T\subseteq[N]$, $\chi_T(x)=\prod_{i\in T}x_i$; every
  $f:\{\pm1\}^N\to\mathbb{R}$ has a unique expansion
  $f=\sum_{T\subseteq[N]}\hat f(T)\chi_T$, $\hat f(T)=\mathbb{E}[f\chi_T]$
  (orthonormality is proved in Lemma 1, Step 1). The Contract's influence,
  specialized: $\mathrm{Inf}_i(f)=\sum_{T\ni i}\hat f(T)^2$ — applied AFTER
  normalization, i.e. to $\mathbf 1_A/\|\mathbf 1_A\|_2$. Influences are
  nonnegative (sums of squares).
* Points of $\{\pm1\}^J$ ($J\subseteq[N]$) are $\pm1$-strings indexed by $J$;
  $x_J$ is the restriction of $x$ to $J$; $\{\pm1\}^\emptyset$ is a one-point
  set. For $u\in\{\pm1\}^J$ and $i\in J$, $u^{\oplus i}$ flips coordinate
  $i$. An **$i$-edge** of $\{\pm1\}^J$ is an unordered pair
  $\{u,u^{\oplus i}\}$; an **edge** is an $i$-edge for some $i$.
* For $\emptyset\ne P\subseteq\{\pm1\}^J$ and $i\in J$:
  $b_i(P):=\#\{i$-edges of $\{\pm1\}^J$ with exactly one endpoint in $P\}$.
  For $A\subseteq\{\pm1\}^N$ and $i\in[N]$: $\partial_i A:=$ the set of
  $i$-edges of $\{\pm1\}^N$ with exactly one endpoint in $A$. For
  $W\subseteq\{\pm1\}^n$: $\partial_E W:=$ the set of edges (all directions)
  with exactly one endpoint in $W$.
* For $S\subseteq J$: $\pi_S:\{\pm1\}^J\to\{\pm1\}^S$ is coordinate
  restriction ($u\mapsto u_S$); the **projection density** is
  $\nu_P(S):=|\pi_S(P)|/2^{|S|}$.
* For $J\subseteq[N]$ and $\emptyset\ne P\subseteq\{\pm1\}^J$ write
  $A=\{x\in\{\pm1\}^N:x_J\in P\}$ and
  $f_{J,P}:=\mathbf 1_A/\|\mathbf 1_A\|_2$. Since $P\ne\emptyset$,
  $A\ne\emptyset$ (extend any $u\in P$ arbitrarily), so
  $\|\mathbf 1_A\|_2>0$ and $f_{J,P}$ is well defined, with $\|f_{J,P}\|_2=1$.
* **Witnessing representations.** The map $(J,P)\mapsto f_{J,P}$ is not
  injective (e.g. $P=\{\pm1\}^J$ gives $f\equiv1$ for every $J$).
  Distributions are over *functions*; for each function in a support we fix
  one witnessing representation $(J,P)$ with $|J|\le d$,
  $\emptyset\ne P\subseteq\{\pm1\}^J$ (class membership guarantees one).
  Influences and supports are intrinsic to the function; Lemmas 2, 4, 5 are
  proved for arbitrary valid representations; the final count (Lemma 6) uses
  only $|J|\le d$ of the chosen witness. No step depends on which witness is
  chosen.
* Notation guard: $T$ = Fourier index sets; $J,K$ = windows; $S$ = shared
  window; $P,Q$ = patterns; $W$ = set in the isoperimetric lemma; $L_t$ =
  level sets.

## 2. Method overview

Six lemmas, then the theorem. Lemma 1: the influence of a normalized junta
indicator is an exact boundary-edge count, $b_i(P)/(2|P|)$. Lemma 2: two
cylinder sets are disjoint iff their patterns' projections to the shared
window are disjoint (so disjoint windows force intersection). Lemma 3
(standalone, proved inline by induction): the entropy-form edge-isoperimetric
inequality on the hypercube. Lemma 4: total influence on any $S\subseteq J$
is at least $\frac12\log_2(1/\nu_P(S))$ — projection sparsity must be paid
for in influence. Lemma 5: a disjoint pair pays total influence $\ge1$ on its
shared window (disjoint projections have density product $\le1/4$). Lemma 6:
weighting Lemma 5 by the product distribution and routing each side's payment
through the partner's window budget $\le d$ gives
$\delta_F\,\mathbb{E}|K|+\delta_G\,\mathbb{E}|J|\ge1$, hence
$\max(\delta_F,\delta_G)\ge1/(2d)$. The theorem follows by contraposition at
$\delta(d)=1/(3d)<1/(2d)$.

```
Lemma 1 (influence = edge count)   Lemma 2 (projection criterion)   Lemma 3 (isoperimetry, standalone)
      \                                  |                              /
       \                                 |                   Lemma 4 (uses 1, 3)
        \                                |                      /
         \                               Lemma 5 (uses 2, 4)
          \                              |
           \                       Lemma 6 (uses 5, nonneg. influences)
            \                            |
             Theorem (uses 6)      + Remark 10.1 (uses 1; NOT load-bearing)
```

Case-split ledger (each discharged where it arises): shared window
$S=\emptyset$, incl. constant functions (Lemma 2 and Lemma 4); empty half in
the isoperimetric induction (Lemma 3, case $b=0$); empty level sets (Lemma 4,
sum truncated at $t_{\max}$); non-unique representations (§1, witnesses);
$d=0$/$N=0$ under a $0\in\mathbb{N}$ convention (Remark 9.1).

## 3. Lemma 1: influence formula

**Lemma 1.** Let $J\subseteq[N]$, $\emptyset\ne P\subseteq\{\pm1\}^J$, and
$f=f_{J,P}$. Then for every $i\in[N]$:
$$\mathrm{Inf}_i(f)=\begin{cases}\dfrac{b_i(P)}{2|P|} & \text{if } i\in J,\\[4pt] 0 & \text{if } i\notin J.\end{cases}$$

*Proof.*

**Step 1 (orthonormality, Parseval).** For $T,T'\subseteq[N]$,
$\chi_T\chi_{T'}=\chi_{T\triangle T'}$ (coordinates in $T\cap T'$ contribute
$x_i^2=1$), and for any $U\subseteq[N]$,
$\mathbb{E}_x[\chi_U(x)]=\prod_{i\in U}\mathbb{E}[x_i]=\mathbf 1[U=\emptyset]$
by independence of the coordinates and $\mathbb{E}[x_i]=0$. Hence
$\mathbb{E}[\chi_T\chi_{T'}]=\mathbf 1[T=T']$: the $2^N$ functions $\chi_T$
are orthonormal, hence linearly independent, hence an orthonormal basis of
the $2^N$-dimensional space of real functions on $\{\pm1\}^N$. Every real
$f$ has a unique expansion $f=\sum_T\hat f(T)\chi_T$ with
$\hat f(T)=\mathbb{E}[f\chi_T]\in\mathbb{R}$, and for any real
coefficients $(c_T)$, Parseval holds:
$\mathbb{E}_x[(\sum_Tc_T\chi_T(x))^2]=\sum_Tc_T^2$ (expand; use
orthonormality; all sums finite).

**Step 2 (flip identity).** Fix $i\in[N]$. For every $T$,
$\chi_T(x^{\oplus i})=\chi_T(x)$ if $i\notin T$ and $=-\chi_T(x)$ if
$i\in T$. Therefore
$$f(x)-f(x^{\oplus i})=\sum_T\hat f(T)\bigl(\chi_T(x)-\chi_T(x^{\oplus i})\bigr)=2\sum_{T\ni i}\hat f(T)\chi_T(x),$$
and by Parseval,
$$\mathrm{Inf}_i(f)=\sum_{T\ni i}\hat f(T)^2=\tfrac14\,\mathbb{E}_x\bigl[(f(x)-f(x^{\oplus i}))^2\bigr].\tag{1.1}$$

**Step 3 (edge count for a normalized indicator).** For
$f=\mathbf 1_A/\|\mathbf 1_A\|_2$,
$$(f(x)-f(x^{\oplus i}))^2=\begin{cases}\|\mathbf 1_A\|_2^{-2} & \text{if exactly one of }x,x^{\oplus i}\in A,\\ 0 & \text{otherwise.}\end{cases}$$
The set of $x$ with exactly one of $x,x^{\oplus i}$ in $A$ is exactly the set
of endpoints of edges in $\partial_i A$; distinct $i$-edges are disjoint
(each point lies on exactly one $i$-edge), so this set has size
$2|\partial_i A|$. With $\|\mathbf 1_A\|_2^2=|A|/2^N$:
$$\mathbb{E}_x\bigl[(f(x)-f(x^{\oplus i}))^2\bigr]=\frac{2^N}{|A|}\cdot\frac{2|\partial_i A|}{2^N}=\frac{2|\partial_i A|}{|A|},
\qquad\text{so by (1.1)}\qquad \mathrm{Inf}_i(f)=\frac{|\partial_i A|}{2|A|}.\tag{1.2}$$

**Step 4 (junta structure).** Identify $x\leftrightarrow(x_J,x_{J^c})\in
\{\pm1\}^J\times\{\pm1\}^{[N]\setminus J}$; then
$A\leftrightarrow P\times\{\pm1\}^{[N]\setminus J}$, so
$$|A|=|P|\cdot2^{N-|J|}.\tag{1.3}$$
*Case $i\notin J$:* $(x^{\oplus i})_J=x_J$, so
$\mathbf 1_A(x^{\oplus i})=\mathbf 1_A(x)$ for all $x$, $|\partial_iA|=0$,
and (1.2) gives $\mathrm{Inf}_i(f)=0$.
*Case $i\in J$:* every $i$-edge of $\{\pm1\}^N$ is
$\{(u,v),(u^{\oplus i},v)\}$ for a unique $u=x_J$ and $v=x_{J^c}$ (flipping
$i\in J$ changes only the $J$-part); membership in $A$ depends only on the
$J$-part, so the edge is in $\partial_iA$ iff $\{u,u^{\oplus i}\}$ is one of
the $b_i(P)$ boundary $i$-edges of the window cube, and each such window edge
lifts to exactly $2^{N-|J|}$ distinct $i$-edges (choices of $v$). Hence
$$|\partial_iA|=b_i(P)\cdot2^{N-|J|}.\tag{1.4}$$
Substituting (1.3), (1.4) into (1.2):
$\mathrm{Inf}_i(f)=\dfrac{b_i(P)2^{N-|J|}}{2|P|2^{N-|J|}}=\dfrac{b_i(P)}{2|P|}$. $\blacksquare$

**Remark 3.1 (I01's "automatic" clauses; non-load-bearing).**
(i) $\|f_{J,P}\|_2=1$ by construction. (ii) $\deg f_{J,P}\le|J|\le d$: for
$T\not\subseteq J$ pick $i\in T\setminus J$; pairing $x$ with $x^{\oplus i}$
leaves $f$ unchanged and negates $\chi_T$, so
$\hat f(T)=\mathbb{E}[f\chi_T]=-\mathbb{E}[f\chi_T]=0$.

*Sanity checks (evidence only).* Singleton pattern in a $k$-dim window:
$\mathrm{Inf}_i=1/2$ for $i\in J$ (the classical relative influence of AND).
Full pattern: $f\equiv1$, all influences $0$.

## 4. Lemma 2: disjointness = projection disjointness

**Lemma 2.** Let $J,K\subseteq[N]$, $\emptyset\ne P\subseteq\{\pm1\}^J$,
$\emptyset\ne Q\subseteq\{\pm1\}^K$, and put
$$A=\{x:x_J\in P\},\qquad B=\{x:x_K\in Q\},\qquad S=J\cap K.$$
Then $A\cap B=\emptyset\iff\pi_S(P)\cap\pi_S(Q)=\emptyset$. Moreover, if
$S=\emptyset$ then $A\cap B\ne\emptyset$; consequently $A\cap B=\emptyset$
forces $S\ne\emptyset$.

*Proof.* **($\Leftarrow$, via contrapositive.)** If $x\in A\cap B$ then
$x_J\in P$ and $x_K\in Q$; restricting to $S\subseteq J$ and $S\subseteq K$,
$x_S=(x_J)_S\in\pi_S(P)$ and $x_S=(x_K)_S\in\pi_S(Q)$, so the projections
intersect. Hence disjoint projections imply $A\cap B=\emptyset$.

**($\Rightarrow$, via contrapositive.)** Suppose
$u\in\pi_S(P)\cap\pi_S(Q)$; choose $p\in P$ with $p_S=u$ and $q\in Q$ with
$q_S=u$. Define $x\in\{\pm1\}^N$ by
$$x_i=\begin{cases}p_i & i\in J,\\ q_i & i\in K\setminus J,\\ +1 & i\notin J\cup K,\end{cases}$$
well defined since $J$, $K\setminus J$, $[N]\setminus(J\cup K)$ partition
$[N]$. Then $x_J=p\in P$, so $x\in A$. And $x_K=q$: for $i\in K\setminus J$,
$x_i=q_i$ by definition; for $i\in K\cap J=S$,
$x_i=p_i=u_i=q_i$ using $p_S=u=q_S$. So $x\in B$, and
$A\cap B\ne\emptyset$. Hence $A\cap B=\emptyset$ implies disjoint
projections.

**(Degenerate case $S=\emptyset$.)** $\{\pm1\}^\emptyset$ is a one-point
set, and $\pi_\emptyset(P),\pi_\emptyset(Q)$ are nonempty subsets of it,
hence both equal it and intersect; by the first direction,
$A\cap B\ne\emptyset$. This covers constant functions ($J=\emptyset$): they
meet everything. So disjointness can only occur with $S\ne\emptyset$.
$\blacksquare$

## 5. Lemma 3: hypercube edge-isoperimetry (entropy form), proved inline

This is the one ingredient the plan flags as non-elementary; it is proved
here from scratch (the weak "entropy form", which is all the payment lemma
needs — not Harper's exact theorem).

**Lemma 3.** For every integer $n\ge0$ and every nonempty
$W\subseteq\{\pm1\}^n$:
$$|\partial_E W|\ \ge\ |W|\,\log_2\frac{2^n}{|W|}.$$

*Proof.* Induction on $n$.

**Base case $n=0$.** The only nonempty $W$ is the one-point cube itself;
$|W|=1=2^0$, the right side is $0$, the left side is $0$ (no edges). ✓

**Inductive step.** Let $n\ge1$; assume the lemma for $n-1$. Write points as
$(u,\epsilon)$, $u\in\{\pm1\}^{n-1}$, $\epsilon\in\{\pm1\}$, and set
$W_\pm=\{u:(u,\pm1)\in W\}$, so $|W_+|+|W_-|=|W|$. By the symmetry
$\epsilon\mapsto-\epsilon$ assume $a:=|W_+|\ge b:=|W_-|$.

*Exact boundary decomposition.* Edges of $\{\pm1\}^n$ are of two kinds:
(i) facet edges $\{(u,\epsilon),(u',\epsilon)\}$ with $\{u,u'\}$ an edge of
$\{\pm1\}^{n-1}$ — such an edge has exactly one endpoint in $W$ iff
$\{u,u'\}\in\partial_EW_\epsilon$ (boundary in the $(n-1)$-cube); and
(ii) direction-$n$ edges $\{(u,+1),(u,-1)\}$ — boundary iff
$u\in W_+\triangle W_-$. The kinds are disjoint and exhaust all edges, so
$$|\partial_EW|=|\partial_EW_+|+|\partial_EW_-|+|W_+\triangle W_-|
\ \ge\ |\partial_EW_+|+|\partial_EW_-|+(a-b),\tag{3.2}$$
using $W_+\triangle W_-\supseteq W_+\setminus W_-$ and
$|W_+\setminus W_-|\ge a-b$.

*Case $b=0$.* Then $|W|=a\ge1$, $\partial_EW_-=\emptyset$, and (3.2) with
the induction hypothesis on $W_+\ne\emptyset$ gives
$$|\partial_EW|\ \ge\ a\log_2\frac{2^{n-1}}{a}+a\ =\ a\log_2\frac{2^n}{a}\ =\ |W|\log_2\frac{2^n}{|W|}. ✓$$

*Case $b\ge1$.* Both halves are nonempty; the induction hypothesis gives
$$|\partial_EW|\ \ge\ a\log_2\frac{2^{n-1}}{a}+b\log_2\frac{2^{n-1}}{b}+(a-b).\tag{3.3}$$
It remains to show RHS(3.3) $\ge(a+b)\log_2\frac{2^n}{a+b}$. Expanding with
$\log_2\frac{2^m}{c}=m-\log_2c$:
$$\text{RHS(3.3)}-(a+b)\log_2\frac{2^n}{a+b}
=(a+b)\log_2(a+b)-a\log_2a-b\log_2b-2b\ =:\ g(a),$$
a function of the real variable $a\in[b,\infty)$, $b>0$ fixed.

*Claim: $g(a)\ge0$ for all real $a\ge b>0$.* At $a=b$:
$g(b)=2b\log_2(2b)-2b\log_2b-2b=2b\cdot1-2b=0$. And with
$\frac{d}{da}[a\log_2a]=\log_2a+\frac1{\ln2}$:
$$g'(a)=\log_2(a+b)+\tfrac1{\ln2}-\log_2a-\tfrac1{\ln2}=\log_2\frac{a+b}{a}>0\quad(b>0),$$
so $g$ is increasing on $[b,\infty)$ and $g(a)\ge g(b)=0$. Applying the claim
at the integers $a=|W_+|,b=|W_-|$ completes the case, the induction, and the
lemma. $\blacksquare$

**Remark 5.1.** Equality holds for subcubes
$W=\{u:u_i=\sigma_i\ \forall i\in I\}$: each fixed direction contributes
$|W|$ boundary edges, free directions none, so
$|\partial_EW|=|W||I|=|W|\log_2(2^n/|W|)$. Only the displayed inequality is
used downstream; no extremizer structure is needed.

*Sanity checks (evidence only), $n=2$:* $|W|=1$: $2=1\cdot\log_24$ ✓
(equality). Diagonal $|W|=2$: $4\ge2$ ✓. $|W|=3$: boundary is the $2$ edges
at the complementary vertex; $2\ge3\log_2(4/3)\approx1.245$ ✓.

## 6. Lemma 4: projection-density payment

**Lemma 4.** Let $J\subseteq[N]$, $\emptyset\ne P\subseteq\{\pm1\}^J$,
$f=f_{J,P}$, and $S\subseteq J$. Then
$$\sum_{i\in S}\mathrm{Inf}_i(f)\ \ge\ \frac12\,\log_2\frac{1}{\nu_P(S)},$$
equivalently (multiplying by $2|P|$ and using Lemma 1)
$\ \sum_{i\in S}b_i(P)\ \ge\ |P|\log_2\bigl(2^{|S|}/|\pi_S(P)|\bigr)$. (4.0)

*Proof.* If $S=\emptyset$: the left side is an empty sum $=0$;
$\pi_\emptyset(P)$ is the whole one-point cube, so $\nu_P(\emptyset)=1$ and
the right side is $0$. ✓ Assume $S\ne\emptyset$; set $s=|S|\ge1$. Identify
$\{\pm1\}^J\cong\{\pm1\}^S\times\{\pm1\}^{J\setminus S}$, writing window
points as $(u,v)$; then $\pi_S(u,v)=u$. Define the fiber-count function
$$w:\{\pm1\}^S\to\mathbb{Z}_{\ge0},\qquad w(u):=\bigl|\{v:(u,v)\in P\}\bigr|,$$
so that
$$\sum_uw(u)=|P|;\qquad w(u)\ge1\iff u\in\pi_S(P);\qquad w\le2^{|J\setminus S|}.\tag{4.1}$$

**Step 1 (boundary edges dominate the total variation of $w$).** Let
$E(\{\pm1\}^S)$ be the edge set of the $S$-cube and
$\mathrm{TV}_S(w):=\sum_{\{u,u'\}\in E(\{\pm1\}^S)}|w(u)-w(u')|$. Claim:
$$\sum_{i\in S}b_i(P)\ \ge\ \mathrm{TV}_S(w).\tag{4.2}$$
Fix $i\in S$. Every $i$-edge of the window cube has the form
$\{(u,v),(u^{\oplus i},v)\}$ for a unique $i$-edge $\{u,u^{\oplus i}\}$ of
the $S$-cube and a unique $v$ (flipping $i\in S$ changes only the $S$-part).
Grouping the boundary $i$-edges of $P$ by their $S$-projection:
$$b_i(P)=\sum_{\{u,u'\}\ i\text{-edge of }\{\pm1\}^S}\bigl|\{v:\mathbf 1[(u,v)\in P]\ne\mathbf 1[(u',v)\in P]\}\bigr|,$$
and for fixed $\{u,u'\}$ the inner count is $|V_u\triangle V_{u'}|$ for
$V_u=\{v:(u,v)\in P\}$, $|V_u|=w(u)$; so it is
$\ge\bigl||V_u|-|V_{u'}|\bigr|=|w(u)-w(u')|$. Summing over the $i$-edges of
the $S$-cube and over $i\in S$ (every edge of the $S$-cube is an $i$-edge
for exactly one $i\in S$) gives (4.2).

**Step 2 (layer cake).** For $t\ge1$ let $L_t:=\{u:w(u)\ge t\}$; then
$L_1=\pi_S(P)\supseteq L_2\supseteq\cdots$ and $L_t=\emptyset$ for
$t>t_{\max}:=\max_uw(u)\ge1$. For integers $c,c'\ge0$,
$|c-c'|=\sum_{t\ge1}|\mathbf 1[c\ge t]-\mathbf 1[c'\ge t]|$ (the summand is
$1$ exactly when $\min(c,c')<t\le\max(c,c')$: exactly $|c-c'|$ values).
Applying this on each edge and exchanging the two finite sums:
$$\mathrm{TV}_S(w)=\sum_{t=1}^{t_{\max}}\ \sum_{\{u,u'\}\in E}\bigl|\mathbf 1_{L_t}(u)-\mathbf 1_{L_t}(u')\bigr|=\sum_{t=1}^{t_{\max}}\bigl|\partial_EL_t\bigr|,\tag{4.3}$$
since an edge contributes $1$ to the $t$-th inner sum iff exactly one
endpoint lies in $L_t$.

**Step 3 (isoperimetry on each level set).** For $1\le t\le t_{\max}$, $L_t$
is nonempty (any $u$ with $w(u)=t_{\max}$ lies in it), so Lemma 3 applies in
the $s$-cube; then $L_t\subseteq\pi_S(P)$ and monotonicity of $\log_2$ (with
prefactor $|L_t|\ge0$) give
$$|\partial_EL_t|\ \ge\ |L_t|\log_2\frac{2^s}{|L_t|}\ \ge\ |L_t|\log_2\frac{2^s}{|\pi_S(P)|}.$$
Summing over $t$ and using
$\sum_{t=1}^{t_{\max}}|L_t|=\sum_t\sum_u\mathbf 1[w(u)\ge t]=\sum_uw(u)=|P|$
(by (4.1)):
$$\sum_{t=1}^{t_{\max}}|\partial_EL_t|\ \ge\ |P|\log_2\frac{2^s}{|\pi_S(P)|}.\tag{4.4}$$

**Assembly.** Chaining (4.2), (4.3), (4.4):
$\sum_{i\in S}b_i(P)\ge|P|\log_2\bigl(2^s/|\pi_S(P)|\bigr)$, which is (4.0).
Dividing by $2|P|>0$ and substituting Lemma 1
($\mathrm{Inf}_i(f)=b_i(P)/(2|P|)$ for $i\in S\subseteq J$) gives the
influence form. $\blacksquare$

*Sanity checks (evidence only).* $P$ a single point, $S=J$: both sides
$=|J|/2$ (equality). Diagonal $P=\{(+,+),(-,-)\}$, $S=\{1\}$: LHS $=1/2$,
RHS $=0$ (strict slack: parity-like patterns overpay).

## 7. Lemma 5: per-pair payment ≥ 1

**Lemma 5.** Let $f=f_{J,P}$, $g=f_{K,Q}$ (patterns nonempty, as always)
with supports $A$, $B$. If $A\cap B=\emptyset$, then with $S:=J\cap K$:
$$\sum_{i\in S}\bigl[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)\bigr]\ \ge\ 1 .$$

*Proof.* By Lemma 2, disjointness gives $\pi_S(P)\cap\pi_S(Q)=\emptyset$ and
forces $S\ne\emptyset$. The projections are nonempty and disjoint in
$\{\pm1\}^S$, so $|\pi_S(P)|+|\pi_S(Q)|\le2^{|S|}$, i.e.
$\nu_P(S)+\nu_Q(S)\le1$; by AM–GM,
$$\nu_P(S)\,\nu_Q(S)\ \le\ \Bigl(\tfrac{\nu_P(S)+\nu_Q(S)}2\Bigr)^2\ \le\ \tfrac14.\tag{5.1}$$
Lemma 4 applies to $(J,P,S)$ and $(K,Q,S)$ since $S\subseteq J$ and
$S\subseteq K$; adding the two instances,
$$\sum_{i\in S}\bigl[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)\bigr]
\ \ge\ \frac12\log_2\frac1{\nu_P(S)\nu_Q(S)}\ \ge\ \frac12\log_24\ =\ 1,$$
by (5.1) and monotonicity of $\log_2$. $\blacksquare$

**Remark 7.1 (tight).** $J=K=\{1\}$, $P=\{-1\}$, $Q=\{+1\}$: disjoint
supports, $\mathrm{Inf}_1(f)=\mathrm{Inf}_1(g)=1/2$ (Lemma 1), sum exactly
$1$.

## 8. Lemma 6: master count

**Lemma 6.** Let $d,N\in\mathbb{N}$ and let $\mathbf F,\mathbf G$ be finitely
supported probability distributions over $\mathcal{C}^{\mathrm{junta}}_d$
(on $\{\pm1\}^N$), with fixed witnessing representations:
$\mathrm{supp}\,\mathbf F=\{f_1,\dots,f_m\}$, probabilities $p_a>0$,
$\sum_ap_a=1$, $f_a=f_{J_a,P_a}$, $|J_a|\le d$; and
$\mathrm{supp}\,\mathbf G=\{g_1,\dots,g_n\}$, $q_b>0$, $\sum_bq_b=1$,
$g_b=f_{K_b,Q_b}$, $|K_b|\le d$. Suppose $(\mathbf F,\mathbf G)$ is
**incompatible**: for every $a,b$ the supports $A_a$, $B_b$ are disjoint.
Put $\delta_F:=\max_{i\in[N]}\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]$
and $\delta_G:=\max_{i\in[N]}\mathbb{E}_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]$.
Then
$$\delta_F\cdot\Bigl(\textstyle\sum_bq_b|K_b|\Bigr)+\delta_G\cdot\Bigl(\textstyle\sum_ap_a|J_a|\Bigr)\ \ge\ 1;\tag{6.1}$$
in particular, since $|J_a|,|K_b|\le d$,
$$(\delta_F+\delta_G)\,d\ \ge\ 1\qquad\text{and}\qquad\max(\delta_F,\delta_G)\ \ge\ \frac1{2d}.\tag{6.2}$$

*Proof.* All sums are finite ($m,n,N<\infty$); exchanging their order is
unconditionally valid.

For each pair $(a,b)$ set $S_{ab}:=J_a\cap K_b$. Since
$A_a\cap B_b=\emptyset$, Lemma 5 gives
$\sum_{i\in S_{ab}}[\mathrm{Inf}_i(f_a)+\mathrm{Inf}_i(g_b)]\ge1$. Multiply
by $p_aq_b\ge0$, sum over $a,b$, and use $\sum_{a,b}p_aq_b=1$:
$$\underbrace{\sum_{a,b}p_aq_b\sum_{i\in S_{ab}}\mathrm{Inf}_i(f_a)}_{=:\Sigma_1}
+\underbrace{\sum_{a,b}p_aq_b\sum_{i\in S_{ab}}\mathrm{Inf}_i(g_b)}_{=:\Sigma_2}\ \ge\ 1.\tag{6.3}$$
Since $S_{ab}\subseteq K_b$ and influences are nonnegative, enlarging the
index set can only increase the inner sum:
$$\Sigma_1\ \le\ \sum_{a,b}p_aq_b\sum_{i\in K_b}\mathrm{Inf}_i(f_a)
=\sum_bq_b\sum_{i\in K_b}\underbrace{\sum_ap_a\mathrm{Inf}_i(f_a)}_{=\mathbb{E}_{\mathbf F}[\mathrm{Inf}_i]\le\delta_F}
\ \le\ \delta_F\sum_bq_b|K_b| .$$
Symmetrically ($S_{ab}\subseteq J_a$):
$\Sigma_2\le\delta_G\sum_ap_a|J_a|$. Substituting into (6.3) gives (6.1);
then $\sum_bq_b|K_b|\le d$, $\sum_ap_a|J_a|\le d$ give
$(\delta_F+\delta_G)d\ge1$, and $\delta_F+\delta_G\le2\max(\delta_F,\delta_G)$
gives (6.2). $\blacksquare$

**Remark 8.1 (generalization hypothesis: satisfied).** The count is linear
in each distribution, uses only per-coordinate *average* influences and the
window budgets $|J|,|K|\le d$, and never enumerates patterns: no constant
depends on the number of possible patterns (nothing like $2^{2^d}$). It is a
union-bound replacement: instead of a union over conflict coordinates, each
cross pair is charged a unit isoperimetric payment (Lemma 5) which the
average-influence budget must fund through the partner's window. This is the
engine I01's binding generalization hypothesis demands.

## 9. Theorem: I01 holds with $c_1=1/3$, $c_2=1$, $\delta(d)=1/(3d)$

**Theorem.** There exist $c_1\in(0,1]$, $c_2>0$, and
$\delta:\mathbb{N}\to(0,1]$ with $\delta(d)\ge c_1d^{-c_2}$ for all $d\ge1$,
such that for all $d,N\in\mathbb{N}$ and all finitely supported distributions
$\mathbf F,\mathbf G$ over $\mathcal{C}^{\mathrm{junta}}_d$ satisfying, for
every $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb{E}_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]\le\delta(d)$, there exist
$f\in\mathrm{supp}\,\mathbf F$, $g\in\mathrm{supp}\,\mathbf G$, and
$x\in\{\pm1\}^N$ with $f(x)\,g(x)\ne0$. Explicit witnesses:
$$c_1=\tfrac13,\qquad c_2=1,\qquad \delta(d)=\tfrac1{3d}.$$

*Proof.* Admissibility: $c_1=1/3\in(0,1]$, $c_2=1>0$; for $d\ge1$,
$\delta(d)=1/(3d)\in(0,1/3]\subseteq(0,1]$ and
$\delta(d)\ge c_1d^{-c_2}$ holds with equality.

Fix $d,N\in\mathbb{N}$ and $\mathbf F,\mathbf G$ as in the statement. Fix a
witnessing representation for each support element (§1). Both supports are
nonempty: a finitely supported probability distribution carries total mass
$1$ on finitely many points, at least one of positive probability.

Suppose for contradiction the conclusion fails: for **all**
$f\in\mathrm{supp}\,\mathbf F$, $g\in\mathrm{supp}\,\mathbf G$, and **all**
$x\in\{\pm1\}^N$, $f(x)g(x)=0$. For normalized indicators
$f=\mathbf 1_A/\|\mathbf 1_A\|_2$, $g=\mathbf 1_B/\|\mathbf 1_B\|_2$,
$$f(x)g(x)=\frac{\mathbf 1_A(x)\,\mathbf 1_B(x)}{\|\mathbf 1_A\|_2\,\|\mathbf 1_B\|_2}
\ \begin{cases}>0 & x\in A\cap B,\\ =0 & \text{otherwise,}\end{cases}$$
so the failure of the conclusion says precisely that every pair of supports
is disjoint: $(\mathbf F,\mathbf G)$ is incompatible in the sense of
Lemma 6. By Lemma 6 (6.2), $\max(\delta_F,\delta_G)\ge1/(2d)$. But the
influence hypothesis gives $\delta_F\le\delta(d)=1/(3d)$ and
$\delta_G\le1/(3d)$, hence
$$\frac1{2d}\ \le\ \max(\delta_F,\delta_G)\ \le\ \frac1{3d},$$
a contradiction, since $1/(2d)>1/(3d)$ for every $d\ge1$. $\blacksquare$

**Remark 9.1 (conventions with $0\in\mathbb{N}$).** If the reader's
$\mathbb{N}$ contains $0$: extend $\delta$ by $\delta(0):=1$ (the constraint
$\delta(d)\ge c_1d^{-c_2}$ is imposed only for $d\ge1$). At $d=0$ the class
is $\{f\equiv1\}$ ($J=\emptyset$, $P$ the unique nonempty pattern) and
$f(x)g(x)=1\ne0$ everywhere. At $N=0$ the cube is a single point, the
influence hypothesis is vacuous ($[N]=\emptyset$), the class is again
$\{f\equiv1\}$, and the conclusion holds at the unique point.

## 10. Tightness (remark; NOT load-bearing)

**Remark 10.1.** No witnessing $\delta$ for I01 can satisfy
$\delta(d)\ge1/(2d)$ for any $d\ge1$. Hence Lemma 6's constant is exact and
$\delta(d)=1/(3d)$ is within a factor $3/2$ of optimal.

*Proof (self-contained, via Lemma 1).* Fix $d\ge1$, $N=d^2$, coordinates
indexed by $(r,c)\in[d]\times[d]$. For $r\in[d]$: $J_r=\{(r,c):c\in[d]\}$
(row $r$), $P_r=\{(-1,\dots,-1)\}$, $f_r=f_{J_r,P_r}$. For $c\in[d]$:
$K_c=\{(r,c):r\in[d]\}$ (column $c$), $Q_c=\{(+1,\dots,+1)\}$,
$g_c=f_{K_c,Q_c}$. All windows have size $d$ and all patterns are nonempty,
so all $2d$ functions lie in $\mathcal{C}^{\mathrm{junta}}_d$; the $f_r$ are
pairwise distinct (the point with row $r$ all $-1$, rest $+1$, is in the
support of $f_r$ only), likewise the $g_c$. Let $\mathbf F,\mathbf G$ be
uniform on $\{f_r\}_r$, $\{g_c\}_c$.

*No common nonvanishing point:* $f_r(x)g_c(x)\ne0$ would force
$x_{(r,c)}=-1$ (row pattern) and $x_{(r,c)}=+1$ (column pattern) —
impossible. So the I01 conclusion fails for $(\mathbf F,\mathbf G)$.

*Influences:* $P_r$ is a single point of a $d$-cube, so $b_i(P_r)=1$ for
each $i\in J_r$, and Lemma 1 gives $\mathrm{Inf}_i(f_r)=1/2$ on $J_r$, else
$0$. Hence for every coordinate $(r',c')$:
$\mathbb{E}_{\mathbf F}[\mathrm{Inf}_{(r',c')}]=\frac1d\cdot\frac12=\frac1{2d}$
(only the term $r=r'$ contributes); symmetrically for $\mathbf G$. So all
I01 hypotheses hold at influence level exactly $1/(2d)$ while the conclusion
fails; any $\delta$ with $\delta(d)\ge1/(2d)$ is contradicted at this
$(d,N)$. (This is the NegRow/PosCol pattern of [ACC22] Claim B.3 — card S1 —
reproved inline; the card is context, not justification.) $\square$

## 11. Gap register

**Empty.** No [GAP], no [SOURCE-BLOCKED], no [MEMORY] on any step. The one
ingredient the plan flagged as potentially non-elementary (edge-isoperimetry)
is proved inline as Lemma 3 in the exact weak form used, so nothing in this
artifact is borrowed.

Deliberate scope notes (not gaps): Remarks 3.1, 5.1, 7.1, 8.1, 9.1, 10.1 and
all "sanity check (evidence only)" lines are non-load-bearing; the proof
chain is Lemmas 1–6 and the Theorem, exactly as drawn in §2's dependency
graph.

## 12. Dependencies

* **External results: none.** Everything is proved inline from the parent
  Contract's definitions (specialized to $\mathcal{Y}=\mathbb{Z}_2$,
  $\{\pm1\}$-coordinates, as fixed by I01): the Fourier basis and Parseval
  are re-derived in Lemma 1 Step 1; the isoperimetric inequality is Lemma 3.
* **Source cards:** S1 (ACC22) is *mentioned* in Remark 10.1 only as
  provenance context for the reproved grid construction — tagged CARD,
  non-load-bearing. No other card is referenced.
* **Refuter artifacts:** the plan (0023-refuter-2 §8) guided the lemma
  decomposition; none of its computations is cited as justification
  anywhere in this artifact.
* **I01 scope notes respected:** $\delta$ depends only on $d$ (never $N$);
  the influence hypothesis is per-coordinate average over the distribution
  (Lemma 6 is genuinely linear in the distributions — it is not a
  max-over-support argument); windows have size $\le d$; the conclusion is
  exact non-vanishing at a common point. Per I01's Descent block, this
  artifact establishes rung R1 only — **not** ℤ₂-PCC and **not** PCC.

### END OF ARTIFACT 0023-prover-1 ###
