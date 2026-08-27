---
id: 0023-prover-3
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: PARTIAL
---

# An internal barrier for rung R2 (I02): per-coordinate window-payment arguments cannot beat $\mathrm{poly}(d)\,2^{-d}$ — and the two live plans escape it

Plan pursued: `0023-strategist-2` §3.6 (P6, class (f) BARRIER), only. Units with
full working: `0023-prover-3-u0 … u5`. Exact-arithmetic re-checks:
`0023-prover-3-code/check_witnesses.py`.

---

## VERDICT

**PARTIAL.** A barrier is **established** for two precisely delimited technique
sub-classes and is **refuted as a barrier for the whole window-payment class**.
No claim is made about R2's truth: a barrier is not a refutation, and **R2
remains open**.

1. **CLAUSE (iv) FIRST, since it is the campaign-critical finding: P1 and P5
   ESCAPE the barrier — YES, both, by exact computation.** The strategist's
   ruling (`0023-strategist-2` §0.6) is **confirmed**, with its stated reason
   corrected: the operative reason is not "sum rather than $\min$" (Remark 4.4
   below shows that is *insufficient*), but the conjunction **(α)** window size
   bounded by a theorem unrelated to relevance **and (β)** willingness to charge
   coordinates that are cheap for their own side. On the two certified witnesses,
   the shattering-window functional (P1) has value $\ge1/8$ and
   $>1/4$; the certificate functional (P5) has value $\ge1/(2(d+1))$ — none is
   $2^{-\Theta(d)}$, so neither cap touches them. The campaign's lead plan is
   **not** dead.
2. **BARRIER (proved).** Every *relevance-denominated* window functional is
   capped at $(d+1)2^{-d-1}$ (**CAP I**, §3); every *own-heavy* window functional
   at level $\theta\ge1/\mathrm{poly}(d)$ is capped at $\frac1{2(2^d-1)}$
   (**CAP II**, §4). Both are $2^{-\Theta(d)}$, hence within a $\mathrm{poly}(d)$
   factor of K1 and **not** inverse-polynomial. This closes I02's own flagged
   route ("re-base R1's payment argument on the influence budget") **in its
   per-coordinate / per-relevant-coordinate form**, negatively.
3. **SCOPE (proved).** Both witnesses are singleton pairs of normalised
   indicators, so both caps hold verbatim at **R2, R3, R4, R5 and R6′** (§5);
   at R4 the caps sit *below* the sub-exponential target $c\,e^{-d^{\alpha}}$, so
   the class cannot deliver R4 either. CAP II moreover generalises to **every
   finite abelian group** (§5.4); CAP I is established for $\mathbb Z_2$ and all
   even-order groups (odd-order: [GAP-2]).
4. **CALIBRATION (proved).** The barrier does **not** condemn frozen I01/R1, nor
   refuter-3 §5.1's $1/(8d)$ forcing bound, nor P4's variance route, nor K1 —
   each is located explicitly relative to the class boundary (§6), and both caps
   sit **above** K1's proved threshold, as a consistent barrier must.
5. **FRONTIER (proved, and it is the artifact's most reusable output).** The
   *whole* class — canonical or not, randomised or not, point-indexed or not — is
   capped by the single number
   $\eta^*(d)=\inf_{\text{pairs}}\sum_{i\in\mathrm{Rel}(A)\cap\mathrm{Rel}(B)}
   [\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)]\in[2^{-d},1]$, and P1's headline
   constant $p=1$ **forces $\eta^*(d)=1$ exactly** — a new, sharp, cheap,
   falsifiable milestone (§8).
6. **New objects recorded:** an equivariant survivor $W_{\max}$ (§7.3) that no
   plan proposes; and a precise drafting warning for P5 (§7.5): its per-point
   variant *is* capped at $2^{-\Theta(d)}$, only the averaged form escapes.

---

## 1. Setup and the technique class

Cube $\{\pm1\}^N$, uniform measure; $\hat h(S)$, $\deg h$,
$\mathrm{Inf}_i(h)=\sum_{S\ni i}\hat h(S)^2$ as in `CONTRACT.md`. For
$\emptyset\ne A\subseteq\{\pm1\}^N$: $\alpha_A=|A|/2^N$,
$f_A=\mathbf 1_A/\lVert\mathbf 1_A\rVert_2$, so $\lVert f_A\rVert_2=1$ and
$\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha_A$. Put
$\mathcal C^{\mathrm{ind}}_d=\{f_A:\deg\mathbf 1_A\le d\}$ (all $N$),
$\mathrm{Rel}(A)=\{i:\mathrm{Inf}_i(\mathbf 1_A)>0\}$, and
$$\mathcal P_d:=\{(A,B):A,B\subseteq\{\pm1\}^N\ \text{nonempty},\ \deg\mathbf 1_A,\deg\mathbf 1_B\le d,\ A\cap B=\emptyset\},\quad S(A,B):=\mathrm{Rel}(A)\cap\mathrm{Rel}(B).$$
$(\mathbf F,\mathbf G)$, finitely supported over $\mathcal
C^{\mathrm{ind}}_d(N)$, is **incompatible** if $fg\equiv0$ for all cross pairs
(equivalently every cross pair is in $\mathcal P_d$);
$\delta_{\mathbf F}:=\max_i\mathbb E_{\mathbf F}\mathrm{Inf}_i(f)$, likewise
$\delta_{\mathbf G}$.

**D1 (window functional).** A map $W$ sending each admissible $A$ (any $N$) to
$W(A)\subseteq[N]$. **Localised:** $W(A)\subseteq\mathrm{Rel}(A)$ always.
**Canonical:** $W(\sigma A)=\sigma W(A)$ for every cube automorphism $\sigma$
(signed permutation). *Only localisation is used in the caps.*

**D2 (the two named properties).** $W$ is **relevance-denominated with density
$c$** on a family if $|W(A)|\ge c|\mathrm{Rel}(A)|$ there
($W_{\mathrm{rel}}(A):=\mathrm{Rel}(A)$ has $c=1$). $W$ is **own-heavy at level
$\theta$** if $W(A)\subseteq\{i:\mathrm{Inf}_i(f_A)\ge\theta\}$ for every $A$
(e.g. $W^\theta_{\mathrm{hvy}}$; and $W_{\mathrm{Forced}}$, $\theta=1/2$).

**D3 (payment).** $\displaystyle
\pi_W(A,B):=\sum_{i\in W(B)}\mathrm{Inf}_i(f_A)+\sum_{i\in W(A)}\mathrm{Inf}_i(f_B)$,
and $\pi_{\mathrm{Rel}}:=\pi_{W_{\mathrm{rel}}}$. A **sum** over the two sides,
never a $\min$.

**D4 (the class $\mathcal W$ — window-payment arguments).** An argument is in
$\mathcal W$ if it proceeds exactly by: **(T1)** fix a localised $W$ (each side's
window a function of its own function only); **(T2)** prove
$\pi_W(A,B)\ge\rho(|W(A)|,|W(B)|)$ for **all** $(A,B)\in\mathcal P_d$, $\rho$ any
function of the two window sizes; **(T3)** conclude by linearity of expectation
over independent $f\sim\mathbf F,g\sim\mathbf G$, using as its only quantitative
inputs $\delta_{\mathbf F},\delta_{\mathbf G}$ and the window sizes.
**This is a stipulation, not a theorem** — see [G1].

**D5 (value).**
$\Theta_W(d):=\inf\{\pi_W(A,B)/(|W(A)|+|W(B)|):(A,B)\in\mathcal P_d,\ |W(A)|+|W(B)|\ge1\}$
($:=0$ if the index set is empty), and $V_W(d):=0$ if some pair has both windows
empty, else $\Theta_W(d)$.

## 2. Framework

**T1 (master count).** *For incompatible $(\mathbf F,\mathbf G)$ and localised
$W$:* $\mathbb E[\pi_W(f,g)]\le\delta_{\mathbf F}\mathbb
E|W(g)|+\delta_{\mathbf G}\mathbb E|W(f)|$; *hence if
$\pi_W\ge\Lambda(|W(A)|+|W(B)|)$ on $\mathcal P_d$ and $\mathbb
E[|W(f)|+|W(g)|]>0$ then $\max(\delta_{\mathbf F},\delta_{\mathbf G})\ge\Lambda$.*

*Proof.* $\pi_W(f,g)=\sum_i\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)+\sum_i\mathbf
1\{i\in W(f)\}\mathrm{Inf}_i(g)$ (finite sums). By independence, for each $i$,
$\mathbb E[\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)]=\Pr[i\in W(g)]\,\mathbb
E_{\mathbf F}[\mathrm{Inf}_i(f)]\le\Pr[i\in W(g)]\delta_{\mathbf F}$; sum,
using $\sum_i\Pr[i\in W(g)]=\mathbb E|W(g)|$, and symmetrise. For the second
claim: every cross pair is in $\mathcal P_d$, so pointwise
$\pi_W\ge\Lambda(|W(f)|+|W(g)|)$; take expectations, bound the right side by
$\max(\delta_{\mathbf F},\delta_{\mathbf G})\mathbb E[|W(f)|+|W(g)|]$, divide.∎

*Remark 2.1.* Independence is used **only** in the factorisation, and only
requires each window to depend on its own function. A window depending on the
**pair** breaks T1 and is outside $\mathcal W$. (This is card S7's obstacle (ii)
in its only load-bearing form. Canonicity is *not* required.)

*Remark 2.2 (randomised / point-indexed windows).* If $W(A)\sim\mu_A$ with
$\mu_A$ depending only on $A$ and drawn independently of the other side, T1–T3
hold with $|W(A)|,\pi_W$ replaced by expectations (same proof, conditioning on
the draws). This is what places **P5** (windows $=$ certificates of a random
point of its own set) inside the framework.

**T2 (value theorem: $V_W$ is exactly what the class can prove).** *Under (T2)
with any $\rho$, the threshold $T$ established by (T1)–(T3) satisfies
$T\le V_W(d)$. In particular the frozen rung's variant "$\pi_W\ge p$,
$|W|\le m$, hence $\max\delta\ge p/(2m)$" yields at most $V_W(d)$.*

*Proof.* The count's output for a family is
$\Lambda(\mathbf F,\mathbf G)=\mathbb E[\rho]/\mathbb E[|W(f)|+|W(g)|]$ when the
denominator is positive, and nothing otherwise; $T=\inf_{(\mathbf F,\mathbf G)}
\Lambda$. If some $(A_0,B_0)\in\mathcal P_d$ has both windows empty, the point
masses at $f_{A_0},f_{B_0}$ form an incompatible family with zero denominator, so
$T\le0=V_W(d)$. Otherwise, for each $(A,B)\in\mathcal P_d$ the point masses give
$\Lambda=\rho(|W(A)|,|W(B)|)/(|W(A)|+|W(B)|)\le\pi_W(A,B)/(|W(A)|+|W(B)|)$ by
(T2); take the infimum. For the variant: $p\le\pi_W(A,B)$ and
$2m\ge|W(A)|+|W(B)|$ give $p/(2m)\le\Theta_W(d)$, and in the empty case
$p\le\pi_W(A_0,B_0)=0$. ∎

**T3 (localisation ceiling).** *For localised $W$ and any $(A,B)\in\mathcal P_d$,*
$$\pi_W(A,B)\ \le\ \pi_{\mathrm{Rel}}(A,B)=\sum_{i\in S(A,B)}\bigl[\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)\bigr];
\qquad\text{hence}\quad V_W(d)\le\eta^*(d):=\inf_{\mathcal P_d}\pi_{\mathrm{Rel}} .$$

*Proof.* $\mathrm{Inf}_i(f_A)=0$ off $\mathrm{Rel}(A)$ and all influences are
$\ge0$, so $\sum_{i\in W(B)}\mathrm{Inf}_i(f_A)
=\sum_{i\in W(B)\cap\mathrm{Rel}(A)}\mathrm{Inf}_i(f_A)\le\sum_{i\in
S}\mathrm{Inf}_i(f_A)$ using $W(B)\subseteq\mathrm{Rel}(B)$; symmetrise, and note
the displayed identity is the case $W=W_{\mathrm{rel}}$. For the ceiling: if some
pair has both windows empty, $V_W=0\le\eta^*$; else every pair has
$|W(A)|+|W(B)|\ge1$, so the ratio is $\le\pi_{\mathrm{Rel}}(A,B)$; take infima. ∎

**T4 (floor: the class is not vacuous).** *(a) Every nonzero multilinear real $p$
of degree $m$ on $\{\pm1\}^n$ has $\Pr[p\ne0]\ge2^{-m}$. (b) $S(A,B)\ne\emptyset$
for every $(A,B)\in\mathcal P_d$. (c) $\mathrm{Inf}_i(f_A)\ge2^{-d-1}$ for
$i\in\mathrm{Rel}(A)$. (d) $2^{-d}\le\eta^*(d)\le1$.*

*Proof.* (a) Take $T$, $|T|=m$, with coefficient $c_T\ne0$. Restricting the
coordinates off $T$ to any $w$, only $S\supseteq T$ can contribute to the
$x_T$-coefficient, and $S\supsetneq T$ is impossible ($\deg p=m$), so that
coefficient stays $c_T\ne0$ and the restriction is $\not\equiv0$; each of the
$2^{n-m}$ restrictions therefore contains a nonzero point.
(b) $\mathbf 1_A$ depends only on $\mathrm{Rel}(A)$; if
$\mathrm{Rel}(A)\cap\mathrm{Rel}(B)=\emptyset$, pick patterns realised by $A$ and
by $B$ on their disjoint relevant sets and combine them into a point of
$A\cap B$ — contradiction.
(c) $D_i:=\frac12(\mathbf 1_A(x^{i\to+1})-\mathbf 1_A(x^{i\to-1}))
=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)x_{S\setminus\{i\}}$ is a nonzero
multilinear polynomial of degree $\le d-1$ in the other $N-1$ variables, with
values in $\{0,\pm\frac12\}$; Parseval gives $\mathrm{Inf}_i(\mathbf
1_A)=\mathbb E[D_i^2]=\frac14\Pr[D_i\ne0]\ge\frac14 2^{-(d-1)}=2^{-d-1}$ by (a);
divide by $\alpha_A\le1$. *(This reproves card S6a's quantum inline; no
[RESTATED] item is load-bearing.)*
(d) Lower: pick $i\in S$ by (b) and use (c) twice. Upper: the $d\times d$ grid
pair (row-subcube vs column-subcube) has $S=\{$the crossing cell$\}$ and each
side forces it, so each contributes $\frac12$ (Remark 4.2(a)), giving
$\pi_{\mathrm{Rel}}=1$. ∎

## 3. Witness (a): the address pair, and CAP I

**Construction.** $k\ge1$, $d=k+1$, coordinates $a_1..a_k$ and $y_j$
($j\in\{0,1\}^k$), $N=k+2^k$; $b_t(a)=\frac{1-a_t}2$;
$A_k:=\{x:y_{b(a)}=+1\}$, $B_k:=A_k^c$.

**T5 (exact table).** *(i)* $\mathbf 1_{A_k}=\frac12+2^{-k-1}\sum_j\sum_{T\subseteq[k]}
\varepsilon_T(j)a_Ty_j$ with $\varepsilon_t(j)=1-2j_t$. *(ii)*
$\deg=d$ on both sides; the maximum-degree monomial supports of $\mathbf
1_{A_k}$, and of $\mathbf 1_{B_k}$, are exactly the $2^k$ sets
$\{a_1,\dots,a_k,y_j\}$. *(iii)* $\alpha=\frac12$,
$\mathrm{Rel}=[N]=S(A_k,B_k)$, $|\mathrm{Rel}|=k+2^k=2^{d-1}+d-1$. *(iv)*
$\mathrm{Inf}_{a_t}(f)=\frac14$, $\mathrm{Inf}_{y_j}(f)=2^{-k-1}$ on both sides;
$\sum_i\mathrm{Inf}_i(f)=\frac k4+\frac12$. *(v)*
$(A_k,B_k)\in\mathcal P_d$ and $\pi_{\mathrm{Rel}}(A_k,B_k)=\frac k2+1=\frac{d+1}2$.

*Proof.* (i) $\mathbf 1[b(a)=j]=\prod_t\frac{1+\varepsilon_t(j)a_t}2
=2^{-k}\sum_T\varepsilon_T(j)a_T$, and
$\mathbf 1_{A_k}=\sum_j\mathbf 1[b(a)=j]\frac{1+y_j}2$; the $y$-free part sums to
$\frac12$. (ii) The monomials $a_Ty_j$ have pairwise distinct supports and
coefficients $\pm2^{-k-1}\ne0$, so (i) is the multilinear expansion;
$\deg=\max(|T|+1)=k+1$ and the top supports are those with $T=[k]$.
$\mathbf 1_{B_k}=1-\mathbf 1_{A_k}$ negates non-constant coefficients.
(iii) Immediate from (i)–(ii). (iv) Monomials containing $y_j$: all $2^k$ choices
of $T$, so $\mathrm{Inf}_{y_j}(\mathbf 1)=2^k2^{-2k-2}=2^{-k-2}$; containing
$a_t$: $2^{k-1}2^k$ monomials, so $\mathrm{Inf}_{a_t}(\mathbf
1)=2^{2k-1}2^{-2k-2}=\frac18$; divide by $\alpha=\frac12$.
(v) Disjoint, nonempty, degree $d$; by T3's identity with $S=[N]$,
$\pi_{\mathrm{Rel}}=2\sum_i\mathrm{Inf}_i(f)=2(\frac k4+\frac12)$. ∎

**Independent check.** `check_witnesses.py` (truth tables, integer
Walsh–Hadamard, exact `Fraction`s) reproduces for $k=1,2,3$: $\alpha=1/2$,
$\deg=k+1$, $|\mathrm{Rel}|=3,6,11$, influences $1/4$ and $1/4,1/8,1/16$,
$\pi_{\mathrm{Rel}}=3/2,2,5/2$, ratios $1/4,1/6,5/44$, and $2^k$ top supports each
containing all address bits and exactly one target — agreeing with T5 and with
`0023-refuter-3` §4.

*Remark 3.1.* $A_k$ has degree $d$ and $2^{d-1}+d-1$ relevant coordinates, so
this witness **re-proves inline** that the relevance window of a degree-$d$ set is
exponential; cards S6c/S6d are context only.

**T6 (CAP I).** *Let $d\ge2$, $k=d-1$, $W$ any localised window functional. Then
$V_W(d)=0$ if $W(A_k)=W(B_k)=\emptyset$, and otherwise*
$$V_W(d)\ \le\ \frac{d+1}{2\bigl(|W(A_k)|+|W(B_k)|\bigr)} .$$
*Hence: (a) if $W\supseteq\mathrm{Rel}$ (in particular $W=W_{\mathrm{rel}}$, the
junta-substitution route), $V_W(d)\le\frac{d+1}{4(2^{d-1}+d-1)}\le(d+1)2^{-d-1}$;
(b) with density $c$ on this family, $V_W(d)\le\frac{d+1}{c\,2^{d+1}}$, so
$c\ge1/\mathrm{poly}(d)$ still leaves $2^{-\Theta(d)}$; (c) $|W(A_k)|+|W(B_k)|
\ge2^{\varepsilon d}$ alone gives $V_W(d)\le(d+1)2^{-\varepsilon d}/2$.*

*Proof.* $\Theta_W$ is an infimum over $\mathcal P_d$, so it is at most the ratio
at the admissible pair $(A_k,B_k)$, which by T3 and T5(v) is at most
$\frac{(d+1)/2}{|W(A_k)|+|W(B_k)|}$; the empty case is D5. Then substitute
$|W(A_k)|+|W(B_k)|=2(2^{d-1}+d-1)$, $\ge2c(2^{d-1}+d-1)\ge c2^d$, or
$\ge2^{\varepsilon d}$. ∎

*Corollary 3.2 (what CAP I closes).* By T2, any argument in $\mathcal W$ with a
relevance-denominated window establishes at most $\mathrm{poly}(d)2^{-d}$ — i.e.
refuter-2's inequality (M) transplanted to $\mathcal C^{\mathrm{ind}}_d$, the R1
proof with the junta size substituted (I02's recorded non-solution, now with the
explicit ceiling $(d+1)2^{-d-1}$), and I02's own flagged
total-influence-budget route *in its per-coordinate form*, are all capped.

*Remark 3.3 (the kill is in the denominator).* $\pi_{\mathrm{Rel}}(A_k,B_k)=
\frac{d+1}2$ is **large**; CAP I bites only because the relevance count is
$\ge2^{d-1}$. A functional whose size is bounded by a theorem *independent of
relevance* is therefore untouched — the precise sense in which the shattering
($\le d$) and certificate ($O(d^4)$) windows sit outside CAP I (§7).

## 4. Witness (b): the codimension-$d$ subcube pair, and CAP II

**T7 (exact table).** *Let $C=\{x:x_1=\dots=x_d=+1\}\subseteq\{\pm1\}^N$,
$D=C^c$. Then $\mathbf 1_C=2^{-d}\sum_{S\subseteq[d]}x_S$;
$\deg\mathbf 1_C=\deg\mathbf 1_D=d$ with unique maximum-degree support $[d]$ each;
$\alpha_C=2^{-d}$, $\alpha_D=1-2^{-d}$;
$\mathrm{Rel}(C)=\mathrm{Rel}(D)=[d]=S$; and for $i\in[d]$*
$$\mathrm{Inf}_i(f_C)=\tfrac12,\qquad \mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)},\qquad
\pi_{\mathrm{Rel}}(C,D)=\frac d2+\frac d{2(2^d-1)} .$$

*Proof.* $\mathbf 1_C=\prod_{i\le d}\frac{1+x_i}2$ gives the expansion, the
degree and the unique top support; complementation preserves both.
$\mathrm{Inf}_i(\mathbf 1_C)=2^{d-1}4^{-d}=2^{-d-1}=\mathrm{Inf}_i(\mathbf 1_D)$;
divide by $\alpha_C,\alpha_D$. $C\cap D=\emptyset$, both nonempty. ∎
(Exact check, $d=2..6$: $\mathrm{Inf}(f_D)=1/6,1/14,1/30,1/62,1/126$;
$\pi_{\mathrm{Rel}}=4/3,12/7,32/15,80/31,64/21$ — agreeing with
`0023-refuter-3` §4.)

*Remark 4.2 (forced coordinates, inline).* Say $A$ *forces* $i$ if
$A\subseteq\{x:x_i=s\}$. **(a)** Then $\mathrm{Inf}_i(f_A)=\frac12$ exactly:
$\mathbf 1_A\frac{1-sx_i}2\equiv0$ gives $x_i\mathbf 1_A=s\mathbf 1_A$, so
$\widehat{\mathbf 1_A}(S\cup\{i\})=s\widehat{\mathbf 1_A}(S)$ for $S\not\ni i$,
whence $\mathrm{Inf}_i(\mathbf 1_A)=\frac12\lVert\mathbf
1_A\rVert^2_2=\frac{\alpha_A}2$. **(b)** A degree-$\le d$ set forces at most $d$
coordinates: forcing all of $F$ gives $\alpha_A\le2^{-|F|}$, while T4(a) gives
$\alpha_A=\Pr[\mathbf 1_A\ne0]\ge2^{-d}$. So $W_{\mathrm{Forced}}$ is localised,
own-heavy at $\theta=\frac12$, of size $\le d$; and
$\mathrm{Forced}(C)=[d]$, $\mathrm{Forced}(D)=\emptyset$.

**T8 (CAP II).** *If $W$ is localised and own-heavy at some level
$\theta>\frac1{2(2^d-1)}$ then $V_W(d)\le\frac1{2(2^d-1)}$.*

*Proof.* By T7 every coordinate has $\mathrm{Inf}_i(f_D)\le\frac1{2(2^d-1)}
<\theta$, so $W(D)=\emptyset$. If also $W(C)=\emptyset$, the pair $(C,D)$ has both
windows empty and $V_W=0$. Otherwise
$\pi_W(C,D)=0+\sum_{i\in W(C)}\mathrm{Inf}_i(f_D)=\frac{|W(C)|}{2(2^d-1)}$, and
$V_W\le\pi_W(C,D)/|W(C)|=\frac1{2(2^d-1)}$. ∎

**T9 (dichotomy: exactly which windows witness (b) kills).** *With
$w_C=|W(C)|,w_D=|W(D)|$ ($\le d$),*
$$\frac{\pi_W(C,D)}{w_C+w_D}=\frac{\frac12w_D+\frac{w_C}{2(2^d-1)}}{w_C+w_D}
=\frac1{2(2^d-1)}\ \text{if } w_D=0<w_C,\qquad \ge\frac1{2(w_C+w_D)}\ge\frac1{4d}\ \text{if } w_D\ge1 .$$
*So witness (b) caps a functional exponentially **iff** the functional omits the
cheap side's window entirely.* The decisive question for a plan is therefore not
"$\min$ or sum?" but: **does my window ever contain a coordinate cheap for its
own function and expensive for the partner?**

*Remark 4.3 (corollaries).* Any window selected by an own-influence threshold
$\ge1/\mathrm{poly}(d)$, or "the coordinates carrying a $1/\mathrm{poly}(d)$
share of the budget $\sum_i\mathrm{Inf}_i\le d$", or $W_{\mathrm{Forced}}$, is
capped at $\frac1{2(2^d-1)}$ for all $d\ge d_0(\theta)$; for
$W_{\mathrm{Forced}}$ in fact $V=0$, since the address pair forces nothing on
either side, so both windows are empty there.

*Remark 4.4 (this strictly strengthens refuter-3's killer (b)).* refuter-3
refutes the **$\min$-form** route (HEAVY$_\theta$) via
$\theta^*(d)\le\frac1{2(2^d-1)}$, and `0023-strategist-2` IG3 correctly notes
that this does not bind **sum-form** payments (on $(C,D)$ the sum payment is
$\ge d/2$). T8 closes that gap from the other side: the sum payment is large only
because $W(C)=[d]$ contains coordinates cheap for $C$'s partner; a rule that
refuses own-cheap coordinates collapses to the same exponential value. **The
min$\to$sum move is necessary but not sufficient**; the sufficient condition is
T9's italicised question.

*Remark 4.5 (duality).* CAP I kills through the denominator (exponential window,
$\Theta(d)$ payment); CAP II through the numerator ($\le d$ window,
$2^{-\Theta(d)}$ payment). A surviving functional needs **both** (α) a
relevance-independent size bound and (β) own-cheap charging.

## 5. SCOPE: the caps hold at R2–R6

**5.1 Class-genericity.** For any family $\mathcal C$ of unit-norm degree-$\le d$
functions, with $\mathrm{Rel}(h)=\{i:\mathrm{Inf}_i(h)>0\}$, $\mathcal
P_d(\mathcal C)=\{(h_1,h_2):h_1h_2\equiv0\}$ and D1–D5 unchanged, the proofs of
T1, T2, T3 hold verbatim (they use only: incompatibility $=$ all cross pairs in
$\mathcal P_d(\mathcal C)$; independence; $\mathrm{Inf}\ge0$; admissibility of
point masses; vanishing off $\mathrm{Rel}$). T4's *floor* is indicator-specific
and is used in no cap.

**5.2 Monotonicity.** If $\mathcal C\subseteq\mathcal C'$ and $W=W'|_{\mathcal
C}$ then $V^{\mathcal C'}_{W'}(d)\le V^{\mathcal C}_{W}(d)$: $\mathcal
P_d(\mathcal C)\subseteq\mathcal P_d(\mathcal C')$, so the infimum is over a
superset (and the empty-window clause transfers). **Caps proved by exhibiting a
witness inside $\mathcal C^{\mathrm{ind}}_d$ therefore hold over every larger
class, and never transfer downward.**

**5.3 The witnesses are singleton indicator pairs.** $f_{A_k},f_{B_k},f_C,f_D$
are unit-norm, nonnegative, $\{0,\text{const}\}$-valued, degree $\le d$;
$(A_k,B_k)$ and $(C,D)$ are cross-disjoint; as point masses they satisfy each
rung's hypotheses with $\delta=\max_i\mathrm{Inf}_i$. Hence they lie in
$$\mathcal C^{\mathrm{ind}}_d\ \subset\ \mathcal C^{+}_d\ \subset\ \{\mathbb R\text{-valued},\lVert\cdot\rVert_2=1,\deg\le d\}\ \subset\ \{\mathbb C\text{-valued},\dots\},$$
i.e. in the classes of **R2 ⊂ R3 ⊂ R4/R5/R6′ ⊂ R6($\mathbb Z_2$)**
(`PROGRESS.md`). With 5.2: **CAP I and CAP II hold at every one of R2, R3, R4,
R5, R6′ and R6($\mathbb Z_2$)**, with the same numerical ceilings. R5 needs no
distributional part (T2 already evaluates at point masses). At R4, whose target
is $c\,e^{-d^\alpha}$ ($\alpha<1$), we have $(d+1)2^{-d-1}<c\,e^{-d^\alpha}$ for
all large $d$, so **the class cannot deliver R4's sub-exponential target either**.

**5.4 Groups.** *CAP II generalises to every finite abelian group $\mathcal Y$*:
with $C_{\mathcal Y}=\{x:x_1=\dots=x_d=y_0\}$,
$\widehat{\mathbf 1_{C_{\mathcal Y}}}(\chi)$ is nonzero exactly on the
$|\mathcal Y|^d$ characters supported in $[d]$, each of modulus
$|\mathcal Y|^{-d}$; so $\deg=d$, $\alpha=|\mathcal Y|^{-d}$,
$\mathrm{Inf}_i(f_{C_{\mathcal Y}})=1-|\mathcal Y|^{-1}$ and
$\mathrm{Inf}_i(f_{D_{\mathcal Y}})=\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^d-1}$,
and T8's proof runs verbatim with cap
$\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^{d}-1}$. *CAP I* holds for $\mathbb Z_2$
and, by pullback along a surjection $\varphi:\mathcal Y\to\mathbb Z_2$ (which
preserves degree, all coefficients, all influences, $\alpha$ and disjointness),
for every **even-order** group; for odd order see [GAP-2].

## 6. CALIBRATION: what the barrier does NOT condemn

**6.1 Frozen I01 / R1 — not condemned.** R1's engine *is* a window-payment
argument with $W\supseteq\mathrm{Rel}$ (CAP I's technique sub-class), payment
$\ge1$, $|W|\le d$, assembled by T1. But its object class is
$\mathcal C^{\mathrm{junta}}_d$, which **does not contain witness (a)**
($|\mathrm{Rel}(A_k)|=2^{d-1}+d-1>d$), and by 5.2 caps never transfer downward.
Witness (b) *is* in that class, but R1's window is not own-heavy (on $D$ it is
$[d]$, all of whose coordinates are cheap for $D$), and T9 gives
$\ge\frac14$ there — consistent with R1's proved $\frac1{2d}$.
**One-sentence diagnosis of the R1→R2 jump:** *R1 is provable by a
relevance-denominated payment because its class caps the relevance window at $d$
by fiat; R2 is not, because its class contains a degree-$d$ set with $2^{d-1}$
relevant coordinates and only $\Theta(d)$ units of payment to spread over them.*

**6.2 refuter-3 §5.1's $1/(8d)$ forcing bound — not condemned.** It is the
window-payment argument with $W=W_{\mathrm{Forced}}$ **restricted to forcing
pairs**, where $\pi_W\ge\frac12+\frac12=1$ and $|W|\le d$ (Remark 4.2), giving
$\ge\frac1{2d}$ on that sub-class — a genuine $\mathrm{poly}(d)$ result, exactly
as declared. CAP II speaks only of the route to **all** of R2 and says precisely
refuter-3's own caveat: witness (b) is not a forcing pair
($\mathrm{Forced}(D)=\emptyset$), so the inequality fails there, and over
$\mathcal P_d$ one has $V_{W_{\mathrm{Forced}}}=0$.

**6.3 P4, K1, P2 — outside the class.** P4 (OSSS + depth-vs-degree, variance vs
max influence) has no window and no per-pair payment; K1's proof is a
Cauchy–Schwarz over the $|\mathcal Y|^d-1$ non-constant blocks; P2 exhibits a
common point. None is in $\mathcal W$ (D4), so no cap applies.

**6.4 Consistency with proved thresholds (a self-check).** A cap below a proved
threshold would refute the barrier. Both caps sit above K1's
$2^{-d}/d$: $\frac{2^{-d}}d\le(d+1)2^{-d-1}$ for $d\ge1$, and
$\frac{2^{-d}}d\le\frac1{2(2^d-1)}$ for $d\ge2$ (as $d2^d\ge2(2^d-1)$). Both are
far below the grid ceiling $\frac1{2d}$ (IG1) and below R2's target, as a barrier
must be.

## 7. CLAUSE (iv): P1 and P5 escape

**7.1 P1 (shattering window).** $W_{\mathrm{sh}}(A)$ $=$ any maximum-degree
monomial support ($|W_{\mathrm{sh}}|\le d$ **by theorem**, card S7b; the
projection property is not used). Localised. Exact values:
* **On witness (a)** (T5(ii)): $W_{\mathrm{sh}}(A_k)=\{a_*,y_j\}$,
  $W_{\mathrm{sh}}(B_k)=\{a_*,y_{j'}\}$, so
  $\pi=\bigl(\frac k4+2^{-k-1}\bigr)\cdot2=\frac k2+2^{-k}$ and
  $$\frac{\pi}{2d}=\frac{k/2+2^{-k}}{2(k+1)}\ \ge\ \frac k{4(k+1)}\ \ge\ \frac18\quad(k\ge1),$$
  independently of the choices (exact: $1/4,5/24,13/64$ for $k=1,2,3$).
* **On witness (b)** (T7): $W_{\mathrm{sh}}(C)=W_{\mathrm{sh}}(D)=[d]$,
  $\pi=\frac d2+\frac d{2(2^d-1)}$, ratio $=\frac14+\frac1{4(2^d-1)}>\frac14$.

Both class hypotheses fail *quantitatively*: the density on witness (a) is
$d/(2^{d-1}+d-1)=2^{-\Theta(d)}$, so CAP I(b)'s own bound degrades to
$(d+1)/(4d)\approx\frac14$ (vacuous); and $W_{\mathrm{sh}}(D)=[d]$ is own-cheap,
so CAP II's hypothesis fails and T9 gives $\ge\frac1{4d}$. **P1 escapes.**

**7.2 Non-canonicity theorem (why the escape is real, and its price).** *(i) For
$c\in\{0,1\}^k$ the map $\sigma_c$: $a_t\mapsto(1-2c_t)a_t$,
$y'_j:=y_{j\oplus c}$, is a cube automorphism with $\sigma_c(A_k)=A_k$,
$\sigma_c(B_k)=B_k$, acting transitively on the $2^k$ targets. (ii) Hence for
canonical localised $W$, $W(A_k)\cap\{\text{targets}\}\in\{\emptyset,\text{all}\}$.
(iii) Hence **no canonical localised functional is a shattering-window
selection** (every top support has exactly one target, and $1\notin\{0,2^k\}$).
(iv) Every canonical localised $W$ either has $|W(A_k)|\ge2^{d-1}$ — capped by
CAP I at $(d+1)2^{-d}$ — or satisfies $W(A_k)\subseteq\{a_1,\dots,a_k\}$.*

*Proof.* (i) $\sigma_c$ flips signs of some address coordinates and permutes
targets by the involution $j\mapsto j\oplus c$. With $s_t=1-2c_t$,
$b_t(s_ta_t)=b_t(a)$ if $c_t=0$ and $1-b_t(a)$ if $c_t=1$, so
$b(a')=b(a)\oplus c$ and $y'_{b(a')}=y_{b(a)}$; thus membership is preserved.
Transitivity: given $j,j'$ take $c=j\oplus j'$. (ii) Equivariance gives
$W(A_k)=\sigma_cW(A_k)$ for all $c$, so the target part is a union of orbits.
(iii),(iv) immediate (for (iv), $|W(A_k)|+|W(B_k)|\ge2^{k}$ in T6). ∎

*Reading.* P1's escape is purchased **exactly** by non-canonicity — card S7's
obstacle (ii). It is legitimate: T1 requires only per-function dependence
(Remark 2.1), and P1's (PAY$\star$) is quantified over *all* selections, which is
stronger than the count needs. Its price: within the canonical world, a
functional must be exponentially large on the address family (capped) or confine
itself to the address hub; a canonical route cannot choose among $2^{d-1}$
symmetric targets.

**7.3 A new canonical survivor: $W_{\max}(A):=\{i:\mathrm{Inf}_i(f_A)=
\max_j\mathrm{Inf}_j(f_A)\}$.** Canonical and localised (both sides of a
cross-disjoint pair have $\mathrm{Rel}\ne\emptyset$, T4(b)). On witness (a),
$k\ge2$: $W_{\max}=\{a_1..a_k\}$ both sides, $\pi=k/2$, ratio $\frac14$. On
witness (b): $W_{\max}=[d]$ both sides, ratio $\frac14+\frac1{4(2^d-1)}$. Neither
relevance-denominated nor own-heavy at level $\ge\frac1{2(2^d-1)}$. **So
$W_{\max}$ escapes both caps and is canonical** — a live functional no plan
proposes. Caveats: no payment inequality is known for it; and its size is
$\le d/\max_i\mathrm{Inf}_i(f_A)$, hence $\mathrm{poly}(d)$ exactly when the
sparser side has $\max_i\mathrm{Inf}_i\ge1/\mathrm{poly}(d)$ — P4's uncarded gate
(**[MEMORY: OSSS + depth-vs-degree]**; flagged, used in no claim).

**7.4 P5 (certificate window).** Minimum-size certificates $T_A(x)$; localised
(a minimal certificate's coordinates are relevant) and randomised in the sense of
Remark 2.2 when $x\sim\mathrm{Unif}(A)$. P5's size bound $O(d^4)$ (card S6c +
textbook $C\le\mathrm{bs}\cdot s$) is **not needed**: on the witnesses the
certificates are explicit.
* **Witness (a):** the unique minimum certificate of $x\in A_k$ is
  $\{a_1..a_k,y_{b(a)}\}$ (size $d$): freeing an address bit moves the read,
  freeing the target lets it flip. So the payment equals P1's,
  $\frac k2+2^{-k}$, over windows summing to $2d$: ratio $\ge\frac18$.
* **Witness (b):** $T_C(x)=[d]$; $T_D(y)=\{i\}$ for any $i\le d$ with $y_i=-1$.
  So $\pi=\frac12+\frac d{2(2^d-1)}\ge\frac12$ over windows summing to $d+1$:
  ratio $\ge\frac1{2(d+1)}$ (exact: $5/18,5/28,19/150$ at $d=2,3,4$).

Both hypotheses fail as in 7.1 (size bounded by a block-sensitivity theorem, not
by relevance; $T_D(y)$ own-cheap). **P5 escapes.**

**7.5 A precise drafting warning for P5 (new).** P5's payment is over
$\Sigma(x,y)$, the coordinates the two certificates fix *oppositely*. On witness
(a), $i\in\Sigma$ iff ($i=a_t$, $a_t\ne a'_t$) or ($i=y_{b(a)}$ and $a=a'$),
hence
$$\sum_{i\in\Sigma(x,y)}\bigl[\mathrm{Inf}_i(f_{A_k})+\mathrm{Inf}_i(f_{B_k})\bigr]
=\tfrac12\bigl|\{t:a_t\ne a'_t\}\bigr|+2^{-k}\mathbf 1\{a=a'\},$$
which is $2^{-k}=2^{-\Theta(d)}$ in the **worst case** over points but has
**average** $\frac k4+2^{-2k}\ge\frac{d-1}4$ (addresses are independent uniform
under $x\sim\mathrm{Unif}(A_k)$, $y\sim\mathrm{Unif}(B_k)$); exact-arithmetic
check for $k\le4$: worst $2^{-k}$, average $\frac k4+4^{-k}$. On witness (b)
every point pair pays $\ge\frac12$. **So P5's averaged inequality escapes, but any
per-point ($\forall x,y$) variant is capped at $2^{-\Theta(d)}$ by witness (a).**
P5 must therefore stay averaged, and must use Remark 2.2's randomised count.

## 8. FRONTIER: one number caps the whole method

1. **(Universal ceiling)** For every localised $W$ — canonical or not,
   deterministic or randomised, point-indexed or not —
   $V_W(d)\le\eta^*(d)=\inf_{\mathcal P_d}\sum_{i\in S(A,B)}[\mathrm{Inf}_i(f_A)
   +\mathrm{Inf}_i(f_B)]$ (T3, Remark 2.2).
2. **(Bracket)** $2^{-d}\le\eta^*(d)\le1$, the upper bound attained by the grid
   pair (T4(d)).
3. **(Sufficiency, one direction only)** If $\eta^*(d)=2^{-\Theta(d)}$ — i.e. if
   some cross-disjoint pair has *all* shared relevant coordinates cheap for
   **both** sides (each contributes $\ge2^{-d}$ by T4(c), so such a pair also has
   $|S|\le2^{\Theta(d)}$) — then **the whole class dies, P1, P5 and $W_{\max}$
   included**. The converse is **not** claimed: CAP II caps a sub-class while
   $\pi_{\mathrm{Rel}}(C,D)=\Theta(d)$ is large. What $\eta^*\ge1/\mathrm{poly}(d)$
   does establish is that no further cap can come from the localisation ceiling
   alone; it must exploit the window selection rule, as CAP II does.
4. **(The certified witnesses cannot supply it)**
   $\pi_{\mathrm{Rel}}(A_k,B_k)=\frac{d+1}2$ and
   $\pi_{\mathrm{Rel}}(C,D)=\frac d2+\frac d{2(2^d-1)}$ — both $\Theta(d)$.
5. **(New necessary condition for P1)** (PAY$\star$) at constant $p$ implies
   $\eta^*(d)\ge p$ (since $\pi_{W_{\mathrm{sh}}}\le\pi_{\mathrm{Rel}}$, T3).
   With 2, **(PAY$\star$) at $p=1$ forces $\eta^*(d)=1$ exactly**, the grid being
   extremal. Falsifiable milestone, strictly easier than (PAY$\star$) itself (no
   window choices are quantified): **search for a cross-disjoint degree-$\le d$
   pair with $\pi_{\mathrm{Rel}}<1$.** A hit refutes $p=1$ (not R2); a hit at
   $2^{-\Theta(d)}$ kills the entire window-payment class.

---

## GAP REGISTER

* **[G1] LOAD-BEARING, DEFINITIONAL (not a gap in a proof).** D4's stipulation —
  that a member of $\mathcal W$ uses *only* (T2) per-pair and *only*
  $\delta_{\mathbf F},\delta_{\mathbf G}$ plus window sizes in (T3) — is what
  "the class" means. T2 then bounds the class's output. Any argument that uses
  more (level weights, hypercontractivity, coordinate correlations, pair-dependent
  windows, fibre renormalisation, variance identities, constructive witnesses) is
  **not** constrained by anything here. **The class is not exhaustive and is not
  claimed to be**; §6.3 and §7 name concrete non-members.
* **[G2] GAP (scope limitation, not attempted).** CAP I is not established for
  finite abelian groups of **odd** order (no $\mathbb Z_2$ quotient, no native
  address witness given). Affects only CAP I, only odd-order groups, only at the
  top rung; the ladder's declared route is $\mathbb Z_2$.
* **[G3] Routine.** §8.3's non-claimed converse is explicitly not proved; the
  one-directional statement is what is used.
* **[G4] Routine.** §7.4's claim that minimal-certificate coordinates are relevant
  is proved in one line in the unit file (`u5`, L11) and used only to check
  localisation, which is also evident from the explicit certificates.
* **[MEMORY, flagged, unused]** refuter-3 §5.3's "Boolean case of
  Aaronson–Ambainis" remark and the OSSS + depth-vs-degree chain are cited
  **nowhere** in any claim; they appear only in §7.3's caveat about $W_{\max}$'s
  window size, explicitly as an open conditional.
* No [SOURCE-BLOCKED] item is load-bearing.

## DEPENDENCIES

| ref | statement used | status | where | load-bearing? |
|---|---|---|---|---|
| **S1** (card) | K1: ACC22 Thm 4.4, compatibility for $\delta<|\mathcal Y|^{-d}/d$ | CARD, READ | §6.4 consistency check; "no better than K1" | no (comparative) |
| **S7b** (card) | Chang–Fang Thm 1.2 / Cor. 3.4: a maximum-degree monomial support has size $\le\deg$ | CARD, READ | §7.1: P1's window is $\le d$ **by theorem** | yes, for the *escape* claim only |
| **S6c** (card) | Wellens: $n(f)\le4.394\cdot2^{\deg f}$ | CARD, READ | Remark in `u1` (L4.4) only | no |
| **S6d** (card) | CHS: $M(d)\ge3\cdot2^{d-1}-2$ | CARD, READ | context; superseded inline by Remark 3.1 | no |
| **S6a** (card) | NS94 influence quantum $\ge2^{-1-d}$ | CARD, RESTATED | **re-proved inline** as T4(c) | no |
| `0023-refuter-3` §4 | the two witness families and their influence tables | CERTIFIED (not verified) | supplied the *leads*; every number re-derived here (T5, T7) and re-checked exactly | no |
| `0023-prover-1` (I01) | frozen R1 statement | FROZEN | §6.1 calibration only; **not re-derived** | no |
| own code | `0023-prover-3-code/check_witnesses.py` | exact `Fraction` re-check | T5, T7, §7.1, §7.4, §7.5 | corroborative |

Everything else is proved inline (T4(a) non-vanishing, T4(b) relevance
intersection, T4(c) quantum, Remark 4.2 forced coordinates, §5.4 group Fourier,
§7.2 automorphisms).

## SOURCE REQUEST

None. This artifact needs no unread source; its two [MEMORY] items are unused.

### END OF ARTIFACT 0023-prover-3 ###
