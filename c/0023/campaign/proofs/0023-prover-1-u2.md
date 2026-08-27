---
id: 0023-prover-1-u2
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 2 of 8: Lemma 2)
---

# 0023-prover-1 — Unit 2: Lemma 2 (disjointness = projection disjointness on the shared window)

Conventions as in Unit 0. In particular, for $S\subseteq J$,
$\pi_S:\{\pm1\}^J\to\{\pm1\}^S$ denotes coordinate restriction ($u\mapsto
u_S$); the same symbol is used for the restriction map $\{\pm1\}^K\to\{\pm1\}^S$
when $S\subseteq K$ (the domains are clear from the argument). Recall
$\{\pm1\}^\emptyset$ is a one-point set (the empty string), and the
restriction of anything to $\emptyset$ is that point.

---

**Lemma 2 (disjointness criterion).** Let $J,K\subseteq[N]$,
$\emptyset\ne P\subseteq\{\pm1\}^J$, $\emptyset\ne Q\subseteq\{\pm1\}^K$, and
put
$$A=\{x\in\{\pm1\}^N:x_J\in P\},\qquad B=\{x\in\{\pm1\}^N:x_K\in Q\},\qquad S=J\cap K.$$
Then
$$A\cap B=\emptyset\quad\Longleftrightarrow\quad \pi_S(P)\cap\pi_S(Q)=\emptyset.$$
Moreover, if $S=\emptyset$ then $A\cap B\ne\emptyset$; consequently
$A\cap B=\emptyset$ forces $S\ne\emptyset$.

*Proof.*

**($\Leftarrow$, contrapositive form: a common point forces intersecting
projections.)** Suppose $x\in A\cap B$. Then $x_J\in P$ and $x_K\in Q$.
Restricting further to $S\subseteq J$ and $S\subseteq K$:
$$x_S=(x_J)_S\in\pi_S(P)\qquad\text{and}\qquad x_S=(x_K)_S\in\pi_S(Q),$$
so $x_S\in\pi_S(P)\cap\pi_S(Q)\ne\emptyset$. Hence
$\pi_S(P)\cap\pi_S(Q)=\emptyset$ implies $A\cap B=\emptyset$.

**($\Rightarrow$, contrapositive form: intersecting projections force a
common point.)** Suppose $u\in\pi_S(P)\cap\pi_S(Q)$. Choose $p\in P$ with
$p_S=u$ and $q\in Q$ with $q_S=u$. Define $x\in\{\pm1\}^N$ coordinatewise:
$$x_i=\begin{cases} p_i & i\in J,\\ q_i & i\in K\setminus J,\\ +1 & i\notin J\cup K.\end{cases}$$
This is well defined: the three index sets $J$, $K\setminus J$,
$[N]\setminus(J\cup K)$ partition $[N]$, so each coordinate receives exactly
one value. We check $x\in A\cap B$:

* $x_J=p\in P$: for $i\in J$, $x_i=p_i$ by definition. Hence $x\in A$.
* $x_K=q\in Q$: for $i\in K\setminus J$, $x_i=q_i$ by definition. For
  $i\in K\cap J=S$, $x_i=p_i=(p_S)_i=u_i=(q_S)_i=q_i$, using $p_S=u=q_S$.
  So $x_i=q_i$ for all $i\in K$, i.e. $x_K=q\in Q$. Hence $x\in B$.

So $A\cap B\ne\emptyset$. This proves: $A\cap B=\emptyset$ implies
$\pi_S(P)\cap\pi_S(Q)=\emptyset$.

**(Degenerate case $S=\emptyset$.)** $\{\pm1\}^\emptyset$ is a one-point
set, and $\pi_\emptyset(P)$, $\pi_\emptyset(Q)$ are nonempty subsets of it
(images of the nonempty sets $P,Q$), hence both equal the whole one-point
set and intersect. By the direction just proved (its contrapositive),
$A\cap B\ne\emptyset$. In particular this covers the case where one window
is empty (a constant function $f\equiv1$): it meets everything. Therefore
$A\cap B=\emptyset$ can only occur with $S\ne\emptyset$. $\blacksquare$

---

**Remark 2.1.** The lemma is representation-dependent in its statement
($S,P,Q$ refer to chosen representations) but is applied downstream only to
the fixed witnessing representations of Unit 0; both sides of the equivalence
are then unambiguous. The sets $A,B$ themselves are intrinsic (they are the
supports of $f_{J,P}$, $f_{K,Q}$).

**Sanity check (evidence only).** $J=K=\{1\}$, $P=\{-1\}$, $Q=\{+1\}$:
$S=\{1\}$, projections $\{-1\},\{+1\}$ disjoint, and indeed
$A=\{x:x_1=-1\}$, $B=\{x:x_1=+1\}$ are disjoint. $J=\{1\},K=\{2\}$: $S=\emptyset$,
and any nonempty patterns co-occur at some $x$ — consistent with the
degenerate case.

EMITTED unit 2 of 8; NEXT UNIT u3 (Lemma 3, edge-isoperimetry); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u2 ###
