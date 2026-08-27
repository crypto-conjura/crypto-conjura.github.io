---
id: 0023-prover-1-u3
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 3 of 8: Lemma 3)
---

# 0023-prover-1 — Unit 3: Lemma 3 (hypercube edge-isoperimetry, entropy form, proved inline)

Conventions as in Unit 0. For $W\subseteq\{\pm1\}^n$, $\partial_E W$ is the
set of edges of $\{\pm1\}^n$ (unordered pairs $\{u,u^{\oplus i}\}$, any
$i\in[n]$) with exactly one endpoint in $W$. This unit is fully
self-contained: it is the one ingredient the plan flags as non-elementary,
and it is proved here from scratch by induction (the weak "entropy form" of
edge-isoperimetry — not Harper's exact theorem, which is not needed).

---

**Lemma 3 (edge-isoperimetry, entropy form).** For every integer $n\ge0$ and
every nonempty $W\subseteq\{\pm1\}^n$:
$$|\partial_E W|\ \ge\ |W|\,\log_2\frac{2^n}{|W|}.$$

*Proof.* Induction on $n$.

**Base case $n=0$.** $\{\pm1\}^0$ is a one-point set; the only nonempty $W$
is that point, $|W|=1=2^0$, and the right-hand side is
$1\cdot\log_2 1=0\le0=|\partial_E W|$ (there are no edges). ✓

**Inductive step.** Let $n\ge1$ and assume the lemma for $n-1$. Write points
of $\{\pm1\}^n$ as $(u,\epsilon)$ with $u\in\{\pm1\}^{n-1}$,
$\epsilon\in\{\pm1\}$, and set
$$W_+=\{u:(u,+1)\in W\},\qquad W_-=\{u:(u,-1)\in W\},$$
subsets of $\{\pm1\}^{n-1}$ with $|W_+|+|W_-|=|W|$. By symmetry (relabeling
$\epsilon\mapsto-\epsilon$ changes neither side) assume
$a:=|W_+|\ \ge\ b:=|W_-|$.

*Exact boundary decomposition.* Edges of $\{\pm1\}^n$ come in two kinds.
(i) Edges inside a facet: $\{(u,\epsilon),(u',\epsilon)\}$ with $\{u,u'\}$ an
edge of $\{\pm1\}^{n-1}$; such an edge has exactly one endpoint in $W$ iff
exactly one of $u,u'$ lies in $W_\epsilon$, i.e. iff $\{u,u'\}\in\partial_E
W_\epsilon$ (boundary in the $(n-1)$-cube). (ii) Direction-$n$ edges:
$\{(u,+1),(u,-1)\}$; such an edge has exactly one endpoint in $W$ iff
$u\in W_+\triangle W_-$. These kinds are disjoint and exhaust all edges, so
$$|\partial_E W|=|\partial_E W_+|+|\partial_E W_-|+|W_+\triangle W_-|.\tag{3.1}$$
Moreover $W_+\triangle W_-\supseteq W_+\setminus W_-$ and
$|W_+\setminus W_-|\ge|W_+|-|W_-|=a-b$, so
$$|\partial_E W|\ \ge\ |\partial_E W_+|+|\partial_E W_-|+(a-b).\tag{3.2}$$

*Case $b=0$.* Then $|W|=a\ge1$ (as $W\ne\emptyset$), $\partial_E W_-=\emptyset$,
and (3.2) with the induction hypothesis on $W_+$ ($\ne\emptyset$) gives
$$|\partial_E W|\ \ge\ a\log_2\frac{2^{n-1}}{a}+a\ =\ a\Bigl(\log_2\frac{2^{n-1}}{a}+\log_2 2\Bigr)=a\log_2\frac{2^{n}}{a}=|W|\log_2\frac{2^n}{|W|}. ✓$$

*Case $b\ge1$.* Both halves are nonempty; the induction hypothesis applies to
each, and (3.2) gives
$$|\partial_E W|\ \ge\ a\log_2\frac{2^{n-1}}{a}+b\log_2\frac{2^{n-1}}{b}+(a-b).\tag{3.3}$$
It remains to show that the right-hand side of (3.3) is at least
$(a+b)\log_2\dfrac{2^n}{a+b}$. Expanding both sides
($\log_2\frac{2^{m}}{c}=m-\log_2 c$):
$$\text{RHS(3.3)}-(a+b)\log_2\frac{2^n}{a+b}
=\Bigl[(a+b)(n-1)-a\log_2a-b\log_2b+a-b\Bigr]-\Bigl[(a+b)n-(a+b)\log_2(a+b)\Bigr]$$
$$=(a+b)\log_2(a+b)-a\log_2 a-b\log_2 b-2b\ =:\ g(a),$$
viewed as a function of a real variable $a\in[b,\infty)$ with $b>0$ fixed. We
claim $g(a)\ge0$ for all real $a\ge b>0$; applying this at the integers
$a=|W_+|$, $b=|W_-|$ finishes the case.

*Claim: $g(a)\ge0$ for real $a\ge b>0$.* First, at $a=b$:
$$g(b)=2b\log_2(2b)-2b\log_2 b-2b=2b\bigl(\log_2(2b)-\log_2 b\bigr)-2b=2b\cdot1-2b=0.$$
Second, $g$ is differentiable on $(0,\infty)$ with, using
$\tfrac{d}{da}\bigl[a\log_2 a\bigr]=\log_2 a+\tfrac1{\ln 2}$:
$$g'(a)=\Bigl(\log_2(a+b)+\tfrac1{\ln2}\Bigr)-\Bigl(\log_2 a+\tfrac1{\ln2}\Bigr)-0=\log_2\frac{a+b}{a}\ >\ 0\quad(b>0).$$
So $g$ is (strictly) increasing on $[b,\infty)$ and $g(a)\ge g(b)=0$ for all
$a\ge b$. This proves the claim, hence the case $b\ge1$, hence the inductive
step, hence the lemma. $\blacksquare$

---

**Remark 3.1 (equality/edge cases).** Equality holds e.g. for subcubes
$W=\{u:u_i=\sigma_i\ \forall i\in I\}$: each of the $|I|$ fixed directions
contributes $|W|$ boundary edges and the free directions none, giving
$|\partial_E W|=|W|\,|I|=|W|\log_2(2^n/|W|)$. For $W$ the full cube both
sides are $0$. The empty set is excluded from the statement (and never needed
downstream; empty level sets are dropped before Lemma 3 is invoked).

**Remark 3.2 (what is and is not used).** Only the displayed inequality is
used downstream (in Lemma 4). No structure theorem for extremizers, no
Harper/Bernstein-order machinery, no source. The real-variable claim uses one
elementary derivative; the inequality $|W_+\triangle W_-|\ge a-b$ and the
decomposition (3.1) are exact set combinatorics.

**Sanity checks (evidence only).** $n=2$: $|W|=1$: boundary $=2=1\cdot\log_2 4$ ✓
(equality, subcube). $|W|=2$ diagonal $\{(+,+),(-,-)\}$: boundary $=4\ge2\cdot\log_2 2=2$ ✓
(strict). $|W|=3$: the complement is a single vertex, whose $2$ incident
edges are exactly the boundary, so $|\partial_E W|=2$; bound:
$3\log_2(4/3)=3(2-\log_23)\approx1.245$ ✓ ($2\ge1.245$, strict).

EMITTED unit 3 of 8; NEXT UNIT u4 (Lemma 4, projection-density payment); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u3 ###
