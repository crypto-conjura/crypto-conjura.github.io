---
id: 0023-prover-2-u2
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE (unit 2 of 5) — milestone M1b, adverse outcome
---

# Unit 2 — T3: (PAY★) as stated is FALSE, exponentially

This unit refutes the key step of plan P1 in the form the strategist states it
(artifact `0023-strategist-2`, **V3**: the inequality is quantified over
*every* choice of maximum-degree monomial supports $W_A,W_B$), and in the
weaker form quantified over every choice of *shattering* windows. It does
**not** refute the choice-map form (PAY$\star_{\mathcal W}$) of u1/T1, which is
what the reduction actually consumes; unit 3 handles that.

Notation as in u0 §0 and u1.

---

## The family

**Definition ($\mathsf H_d$).** Fix an integer $d\ge2$ and put $N=d+1$. Write a
point of $\{\pm1\}^N$ as $(u,w)$ with $u\in\{\pm1\}^d$ (the **block**,
coordinates $u_1,\dots,u_d$) and $w\in\{\pm1\}$ (the **hub**, one coordinate).
Let
$$p:=(+1,+1,\dots,+1)\in\{\pm1\}^d,\qquad q:=(-1,+1,\dots,+1)\in\{\pm1\}^d$$
(so $p,q$ differ in exactly the first block coordinate). Define
$$\boxed{\ \mathsf A_d:=\bigl\{(u,w):w=+1,\ u\ne p\bigr\}\ \cup\ \bigl\{(u,w):w=-1,\ u=q\bigr\},\qquad \mathsf B_d:=\{\pm1\}^N\setminus\mathsf A_d.\ }$$
Explicitly $\mathsf B_d=\{(u,w):w=+1,\ u=p\}\cup\{(u,w):w=-1,\ u\ne q\}$.
Both are nonempty and they are disjoint by construction.

## L6 (exact Fourier data of $\mathsf H_d$). PROVED-INLINE

**Statement.** With $h:=\tfrac{1+w}2=\mathbf 1\{w=+1\}$ and $U:=\{u_1,\dots,u_d\}$,
$$\mathbf 1_{\mathsf A_d}=\frac{1+w}{2}\ -\ 2^{-d}\sum_{\emptyset\ne T\ni 1}u^T\ -\ 2^{-d}\,w\!\!\sum_{T\subseteq\{2,\dots,d\}}\!\! u^T ,$$
i.e. the multilinear expansion of $\mathbf 1_{\mathsf A_d}$ has exactly the
following nonzero coefficients:
$$\widehat{\mathbf 1_{\mathsf A}}(\emptyset)=\tfrac12,\quad
\widehat{\mathbf 1_{\mathsf A}}(\{w\})=\tfrac12-2^{-d},\quad
\widehat{\mathbf 1_{\mathsf A}}(T)=-2^{-d}\ (T\subseteq U,\ u_1\in T),\quad
\widehat{\mathbf 1_{\mathsf A}}(T\cup\{w\})=-2^{-d}\ (\emptyset\ne T\subseteq U\setminus\{u_1\}).$$
Consequently:

1. $\deg\mathbf 1_{\mathsf A_d}=\deg\mathbf 1_{\mathsf B_d}=d$, so
   $f_{\mathsf A_d},f_{\mathsf B_d}\in\mathcal C^{\mathrm{ind}}_d$;
2. $\alpha=\beta=\tfrac12$;
3. $\mathrm{Inf}_{u_i}(\mathbf 1_{\mathsf A_d})=2^{-d-1}$ for every $i\in[d]$,
   and $\mathrm{Inf}_w(\mathbf 1_{\mathsf A_d})=(\tfrac12-2^{-d})^2+(2^{d-1}-1)2^{-2d}$;
   the same values hold for $\mathbf 1_{\mathsf B_d}$;
4. $U$ and $U':=\{u_2,\dots,u_d,w\}$ are both maximum-degree monomial supports
   of $\mathbf 1_{\mathsf A_d}$ and of $\mathbf 1_{\mathsf B_d}$; hence, by
   L3(2), $U,U'\in\mathcal S_d(\mathsf A_d)\cap\mathcal S_d(\mathsf B_d)$.

**Proof.** Since $\mathbf 1_p(u)=\prod_{i=1}^d\frac{1+u_i}2=2^{-d}\sum_{T\subseteq
U}u^T$ and $\mathbf 1_q(u)=2^{-d}\sum_{T}\varepsilon^Tu^T$ with
$\varepsilon^T=(-1)^{\mathbf 1\{u_1\in T\}}$, and since by definition
$$\mathbf 1_{\mathsf A}=h\,(1-\mathbf 1_p)+(1-h)\,\mathbf 1_q
= h+2^{-d}\sum_{T\subseteq U}u^T\bigl[(1-h)\varepsilon^T-h\bigr],$$
we evaluate the bracket. If $u_1\in T$ then $\varepsilon^T=-1$ and the bracket
is $-(1-h)-h=-1$. If $u_1\notin T$ then $\varepsilon^T=+1$ and the bracket is
$(1-h)-h=1-2h=-w$. Substituting $h=\frac{1+w}2$ and separating the $T=\emptyset$
term (which lies in the second case, contributing $-2^{-d}w$) gives the
displayed expansion, and the coefficient list is read off from it; the
monomials listed are pairwise distinct, so no cancellation occurs and each
listed coefficient is exact. In particular $\frac12-2^{-d}\ne0$ (as $d\ge2$)
and $-2^{-d}\ne0$.

(1) The monomials present have degrees $|T|\le d$ (first family; $T=U$ occurs,
with $u_1\in U$, so degree $d$ is attained) and $|T|+1\le d$ (second family,
since $T\subseteq U\setminus\{u_1\}$ has $|T|\le d-1$). So
$\deg\mathbf 1_{\mathsf A}=d$. As $\mathbf 1_{\mathsf B}=1-\mathbf
1_{\mathsf A}$, the two functions have the same nonzero coefficients off
$\emptyset$ up to sign, so $\deg\mathbf 1_{\mathsf B}=d$ too. Both sets are
nonempty, so their normalisations lie in $\mathcal C^{\mathrm{ind}}_d$.

(2) $\alpha=\widehat{\mathbf 1_{\mathsf A}}(\emptyset)=\frac12$ and
$\beta=1-\alpha=\frac12$.

(3) Fix $i\in[d]$ and count the monomials containing $u_i$; each has
coefficient $\pm2^{-d}$, so
$\mathrm{Inf}_{u_i}=2^{-2d}\cdot\#\{\text{such monomials}\}$.
*If $i=1$:* only the first family qualifies, giving the $T\subseteq U$ with
$u_1\in T$, i.e. $2^{d-1}$ monomials.
*If $i\ge2$:* the first family gives $T\ni u_1,u_i$, i.e. $2^{d-2}$ monomials;
the second gives $T\subseteq U\setminus\{u_1\}$ with $u_i\in T$, i.e. $2^{d-2}$
monomials; total $2^{d-1}$.
Either way $\mathrm{Inf}_{u_i}(\mathbf 1_{\mathsf A})=2^{d-1}2^{-2d}=2^{-d-1}$.
For the hub, the monomials containing $w$ are $\{w\}$ (coefficient
$\frac12-2^{-d}$) and $T\cup\{w\}$ for the $2^{d-1}-1$ nonempty
$T\subseteq U\setminus\{u_1\}$ (coefficient $-2^{-d}$), giving the stated
value. Since $\mathbf 1_{\mathsf B}=1-\mathbf 1_{\mathsf A}$, all influences
agree.

(4) $|U|=|U'|=d=\deg$, and the coefficients at $u^U$ (namely $-2^{-d}$, first
family with $T=U\ni u_1$) and at $u^{U\setminus\{u_1\}}w$ (namely $-2^{-d}$,
second family with $T=U\setminus\{u_1\}\ne\emptyset$ as $d\ge2$) are nonzero;
for $\mathbf 1_{\mathsf B}$ they are $+2^{-d}$. L3(2) then puts both sets in
$\mathcal S_d$ of both windows. $\square$

*(Direct check of the shattering property, independent of L3(2): off $U$ the
only remaining coordinate is $w$, and both values of $w$ occur in
$\mathsf A_d$ and in $\mathsf B_d$; off $U'$ the only remaining coordinate is
$u_1$, and both values occur in each set — e.g. $(q,-1)\in\mathsf A_d$ has
$u_1=-1$ and $(u,+1)$ with $u=(+1,-1,\dots)\in\mathsf A_d$ has $u_1=+1$.)*

---

## T3 (refutation of (PAY★) in its stated form). PROVED-INLINE

**Statement.** For every $d\ge2$, the pair $(\mathsf A_d,\mathsf B_d)$ is a
cross-disjoint pair in $\mathcal C^{\mathrm{ind}}_d$, and for the
maximum-degree monomial supports $W_{\mathsf A}=W_{\mathsf B}=U$,
$$\pi\bigl((\mathsf A_d,U),(\mathsf B_d,U)\bigr)\ =\ \sum_{i\in U}\mathrm{Inf}_i(f_{\mathsf A_d})+\sum_{i\in U}\mathrm{Inf}_i(f_{\mathsf B_d})\ =\ d\,2^{1-d} .$$
Consequently:

* **(PAY★) is false at every inverse-polynomial $p$:** for any $p$ with
  $p(d)\ge c_1d^{-c_2}$ there is $d$ with $d\,2^{1-d}<p(d)$, so the inequality
  of strategist V3 fails at that $d$. The decay is exponential:
  $\min_{W_{\mathsf A},W_{\mathsf B}}\pi\le d2^{1-d}=2^{-\Theta(d)}$.
* **(PAY★) at $p=1$ is false from $d=3$ on:** $\pi=3/4<1$ at $d=3$, $1/2$ at
  $d=4$, $5/16$ at $d=5$. (At $d=2$ the value is exactly $1$, which is why the
  strategist's $d\le2$ calibration V4 did not see this.)
* The same computation refutes the a-priori-weaker statement quantified over
  all **shattering** windows (by L6(4) $U$ is one), and refutes the claim of
  strategist §0.3 that the S7b-window payment is bounded below by a constant.

**Proof.** By L6(1),(4) the pair is admissible and $U$ is an admissible window
for both sides. By L6(2),(3),
$$\pi=\frac{1}{\alpha}\sum_{i\in U}\mathrm{Inf}_i(\mathbf 1_{\mathsf A})+\frac{1}{\beta}\sum_{i\in U}\mathrm{Inf}_i(\mathbf 1_{\mathsf B})
=2\cdot d\,2^{-d-1}+2\cdot d\,2^{-d-1}=d\,2^{1-d}. \qquad\square$$

**Machine confirmation (exact, second independent method).**
`proofs/0023-prover-2-code/check_family.py` builds $\mathsf A_d,\mathsf B_d$
from the set definition (not from the expansion), computes the multilinear
expansion by an integer Walsh–Hadamard transform in `fractions.Fraction`
arithmetic, and asserts, for $d=2,\dots,12$: $\deg=d$ on both sides;
$\alpha=\beta=1/2$; $\mathrm{Inf}_{u_i}=2^{-d-1}$; the stated hub influence;
that $U$ and $U'$ are maximum-degree monomial supports of both sides; that
both sets surject off $U$ and off $U'$ (shattering, checked by enumeration);
$\pi(U,U)=d2^{1-d}$; and $\pi(U',U')=1+(d-2)2^{1-d}$. All assertions pass; no
floating point enters any assertion. Printed values:
$d=2:1$, $3:\tfrac34$, $4:\tfrac12$, $5:\tfrac5{16}$, $6:\tfrac3{16}$,
$7:\tfrac7{64}$, $8:\tfrac1{16}$, $9:\tfrac9{256}$, $10:\tfrac5{256}$,
$11:\tfrac{11}{1024}$, $12:\tfrac3{512}$.

---

## What T3 does and does not kill

**It does NOT refute R2, and no reading of it may be sold as progress toward a
refutation.** $(\mathsf A_d,\mathsf B_d)$ is a *singleton-supported* pair whose
hub influence is large: $\mathrm{Inf}_w(f_{\mathsf A_d})=2\bigl[(\tfrac12-2^{-d})^2+(2^{d-1}-1)2^{-2d}\bigr]\to\tfrac12$,
so the pair violates R2's influence hypothesis at every inverse-polynomial
$\delta$ by a wide margin. It is a counterexample to a *proof technique*, not
to the rung.

**It does kill:** the inequality (PAY★) of strategist V3 as stated (all
maximum-degree supports, or all shattering windows), hence P1's advertised key
step and its headline constant $p=1$; and it falsifies the strategist's
inference (§0.2–§0.3) that immunity to refuter-3's two certified killers makes
the S7b-window payment route safe. The family is immune to both killers'
diagnostics for the same reasons the strategist gives — its windows have size
$d$, not $2^{\Theta(d)}$ (indeed $\mathsf A_d$ has only $d+1$ relevant
coordinates, so even the *junta* denominator is $\Theta(d)$ here), and no
$\min$ over the two sides appears — and it is nevertheless exponentially
cheap. So it is a **third, independent obstruction**, orthogonal to killers
(a) and (b), and it lives inside the smallest possible object: a single pair of
complementary sets on $d+1$ coordinates.

**The mechanism, stated for the record.** The Chang–Fang window is a *degree*
object; the payment is an *influence* object; cards S7 and S7b certify (over
the paper's complete text) that the source says nothing about influence, and
$\mathsf H_d$ shows the two can be decoupled: all of $\mathsf A_d$'s influence
mass sits on the hub $w$, which the maximum-degree support $U$ misses entirely,
while every coordinate of $U$ carries only the influence *quantum* $2^{-d-1}$
of L2 — the minimum permitted by degree $d$. In other words, T2 is not merely
the best bound this route currently gives; on the window $U$ it is *tight*, up
to the factor $d$, for a genuine pair.

EMITTED unit 2 of 5; NEXT UNIT: u3 = T4 (anatomy: the two-parameter family, and
what a choice map must do) and T5 (the repaired window functional, its
verification table, and the exact object that would refute it);
ARTIFACT 0023-prover-2.

### END OF ARTIFACT 0023-prover-2-u2 ###
