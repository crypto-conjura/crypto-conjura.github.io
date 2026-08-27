---
id: 0023-prover-3-r2
agent: reviser
model: claude-opus-5[1m]
cycle: 3
status: PARTIAL
---

# An internal barrier for rung R2 (I02): **two** window-payment sub-classes — relevance-denominated and own-heavy — cannot beat $\mathrm{poly}(d)\,2^{-d}$; the class as a whole is **not** capped, and the two live plans escape both caps

Revision of `0023-prover-3` against the triage ruling `0023-prover-3-triage.md`
(10 upheld findings U1–U10, 6 pedantic P1–P6). Plan pursued:
`0023-strategist-2` §3.6 (P6, class (f) BARRIER), only. Units with full working:
`0023-prover-3-u0 … u5` (unrevised; where a unit conflicts with this file, this
file governs). Exact-arithmetic re-checks:
`0023-prover-3-code/check_witnesses.py` and, new in this revision,
`0023-prover-3-r2-code/check_min_certificates.py`. Changelog at the end.

Readable with no context beyond `intermediates/I02-degree-d-sets.md` and
`CONTRACT.md`; every rung class it names is restated in §5.3.

---

## VERDICT

**PARTIAL.** A barrier is **established for exactly two precisely delimited
technique sub-classes**, and is **refuted as a barrier for the whole
window-payment class $\mathcal W$** — refuted in the exact sense that *no cap
proved here applies to $\mathcal W$ as a whole*: §7 exhibits three localised
members that neither cap touches. That is not a claim that any of them succeeds.
No claim is made about R2's truth: a barrier is not a refutation, and **R2
remains open**.

**Two standing disclaimers, load-bearing for every clause below.**

* **(No lower bounds.)** $\Theta_W(d)$ (D5) is an *infimum* over all of
  $\mathcal P_d$. A ratio computed at one pair is an **upper** bound on it. This
  artifact computes ratios at two pairs and therefore proves **no lower bound on
  any $\Theta_W$ anywhere.** Every "escape" statement below is a statement that
  a cap's *hypotheses fail*, or that a *particular witness contributes no cap
  below* some number — never that a functional's value is at least anything.
* **(Class stipulation.)** $\mathcal W$ (D4) is a stipulated class, not a
  theorem about all possible arguments; see [G1], which lists concrete
  non-members, including the mass-denominated route of I02's own flagged
  question.

1. **CLAUSE (iv) FIRST, since it is the campaign-critical finding: P1 and P5
   ESCAPE both caps — YES, both, by exact computation.** The strategist's ruling
   (`0023-strategist-2` §0.6) is **confirmed**, with its stated reason corrected:
   the operative reason is not "sum rather than $\min$" (Remark 4.4 shows that
   move is *insufficient*), but the conjunction **(α)** a *sub-exponential
   (effectively $\mathrm{poly}(d)$) window size on the address family*, from a
   theorem unrelated to relevance, **and (β)** the window contains, at witness
   (b), a coordinate $i$ with $\mathrm{Inf}_i(f_D)\le\frac1{2(2^d-1)}$ — i.e.
   own-heaviness fails at every level strictly above $\frac1{2(2^d-1)}$.
   Precisely what is proved (§7): **at both certified witnesses the hypotheses of
   CAP I and of CAP II fail for the shattering window (P1), for the
   minimum-certificate window (P5), and for $W_{\max}$, and each witness
   contributes no cap below an explicit inverse-polynomial number** — so neither
   cap, and neither witness, touches them. **No lower bound on
   $\Theta_{W_{\mathrm{sh}}}$ or $\Theta_{\text{cert}}$ is claimed**; indeed
   $\Theta_{W_{\mathrm{sh}}}(d)\le\eta^*(d)\in[2^{-d},1]$ and the bracket for
   $\eta^*$ is **open** (§8.2). The campaign's lead plan is **not** dead; whether
   it succeeds is exactly the open milestone of §8.5.
2. **BARRIER (proved), with its three qualifiers stated.** Relative to the object
   class $\mathcal C^{\mathrm{ind}}_d$ of R2 **and to every larger class**
   (§5.1–5.2; the relativisation is essential — see §6.1, without it the
   sentence would falsely condemn frozen R1, whose class is *smaller*):
   *(i)* every window functional that is **relevance-denominated with density
   $c$** is capped at $\frac{d+1}{c\,2^{d+1}}$ (**CAP I**, T6(b)); at $c=1$ this
   is $(d+1)2^{-d-1}$ (T6(a)), and even a relevance-independent size
   $\ge2^{\varepsilon d}$ is capped at $(d+1)2^{-\varepsilon d}/2$ (T6(c));
   *(ii)* every functional that is **own-heavy at a level
   $\theta>\frac1{2(2^d-1)}$ (strictly) and nonempty at the subcube $C$** is
   capped at $\frac1{2(2^d-1)}$ (**CAP II**, T8) — for $\theta=1/\mathrm{poly}(d)$
   the strictness means "for all $d\ge d_0(\theta)$".
   Both ceilings are $2^{-\Theta(d)}$, hence within a $\mathrm{poly}(d)$ factor
   of K1 and **not** inverse-polynomial. This closes I02's flagged route
   ("re-base R1's payment argument on the influence budget") **only in its
   per-coordinate / per-relevant-coordinate / thresholded forms**. **It does NOT
   close the mass-denominated form** — charging payment against the influence
   *mass* $\sum_i\mathrm{Inf}_i\le d$ rather than against a bounded window is
   outside $\mathcal W$ by construction (D4(T3) admits only
   $\delta_{\mathbf F},\delta_{\mathbf G}$ and window *sizes*), so **it is capped
   by nothing in this artifact**; see [G1]. I02's central question is therefore
   **not closed by this artifact in either direction**.
3. **SCOPE (proved), with the ladder consequence stated exactly.** Both
   witnesses are singleton pairs of normalised indicators, so both caps hold
   verbatim in the object classes of **R2, R3, R4, R5, R6′ and R6($\mathbb Z_2$)**
   (§5), with the same numerical ceilings. The campaign may **not** record R4 (or
   R2, R3, R5, R6′) as condemned. What it may record is the conditional form:
   > *No relevance-denominated window-payment argument, and no
   > own-heavy-at-$\theta>\frac1{2(2^d-1)}$ window-payment argument, can
   > establish R4's target $c\,e^{-d^\alpha}$ — or any threshold above
   > $(d+1)2^{-d-1}$ resp. $\frac1{2(2^d-1)}$ — in the object class of R2, R3,
   > R4, R5, R6′ or R6($\mathbb Z_2$).*
   CAP II moreover generalises to **every finite abelian group** (§5.4); CAP I is
   established for $\mathbb Z_2$ and all even-order groups (odd order: **[G2]**).
4. **CALIBRATION (proved).** The barrier does **not** condemn frozen I01/R1, nor
   `0023-refuter-3` §5.1's $1/(8d)$ forcing bound, nor P4's variance route, nor
   K1 — each is located explicitly relative to the class boundary (§6), and both
   caps sit **above** K1's proved threshold, as a consistent barrier must.
5. **FRONTIER (proved, and it is the artifact's most reusable output).** Every
   localised window functional that is nonempty on the pairs approaching
   $\eta^*(d)$ — which includes every functional named in this artifact and both
   live plans' — is capped by the single number
   $\eta^*(d)=\inf_{\text{pairs}}\sum_{i\in\mathrm{Rel}(A)\cap\mathrm{Rel}(B)}
   [\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)]\in[2^{-d},1]$, whose bracket is
   **open**; and P1's headline constant $p=1$ **forces $\eta^*(d)=1$ exactly** —
   a new, sharp, cheap, falsifiable milestone (§8).
6. **New objects recorded:** an equivariant survivor $W_{\max}$ (§7.3) that no
   plan proposes; the non-canonicity theorem §7.2; and two precise drafting
   warnings for P5 (§7.4–7.5): its per-point variant *is* capped at
   $2^{-\Theta(d)}$ (only the averaged form escapes), and its certificate notion
   and selection rule must be declared, because the escape computation is
   selection-dependent.

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
(e.g. $W^\theta_{\mathrm{hvy}}(A):=\{i\in\mathrm{Rel}(A):\mathrm{Inf}_i(f_A)\ge\theta\}$;
and $W_{\mathrm{Forced}}$, $\theta=1/2$). These are **two sub-classes of
$\mathcal W$, not a partition of it**: §7 exhibits members of $\mathcal W$ with
neither property.

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
**This is a stipulation, not a theorem** — see [G1]. In particular a count whose
denominator is influence **mass** rather than a window size is *not* in
$\mathcal W$.

**D5 (value).**
$$\Theta_W(d):=\inf\Bigl\{\tfrac{\pi_W(A,B)}{|W(A)|+|W(B)|}\ :\ (A,B)\in\mathcal P_d,\ |W(A)|+|W(B)|\ge1\Bigr\},$$
with the convention $\Theta_W(d):=0$ in the degenerate case where **no** pair of
$\mathcal P_d$ has a nonempty combined window (then $W\equiv\emptyset$ on
$\mathcal P_d$, the count's denominator vanishes for *every* incompatible family,
and the argument establishes no positive threshold at all — this convention is
therefore sound as stated).

*Remark 1.1 (what D5 deliberately does **not** do; escalated item E1 of the
triage).* Earlier drafts of this artifact also set the value to $0$ whenever
*some* single pair of $\mathcal P_d$ had both windows empty, and concluded from
such a pair that the argument "establishes nothing". **That inference is invalid
and has been removed.** A degenerate pair defeats an argument only if it is *in
scope*: an argument in $\mathcal W$ must prove "every incompatible family with
$\max(\delta_{\mathbf F},\delta_{\mathbf G})<\delta(d)$ is compatible", so a
family whose own $\max\delta$ exceeds the claimed threshold refutes nothing. (At
the point masses $(A_k,B_k)$ of §3, $\max\delta=1/4$; at $(C,D)$ of §4,
$\max\delta=1/2$; every threshold at issue here is $<1/(2d)\le1/4$ for $d\ge2$,
so both are out of scope.) The two candidate refinements of the ceiling —
$T\le\min\bigl(\Theta_W(d),\ \inf\{\max(\delta_{\mathbf F},\delta_{\mathbf G}):
\text{incompatible, all windows empty}\}\bigr)$, versus keeping no clause at all
and claiming nothing on such families — are **escalated to the human** and are
used by **no cap in this artifact**. Both caps below are stated with an explicit
nonemptiness hypothesis instead, and that hypothesis is verified for every
concrete functional they are applied to.

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
**pair** breaks T1 and is outside $\mathcal W$. (This is the only load-bearing
form of obstacle (ii) recorded in card S7, `sources/S7-changfang26-card.md`.
Canonicity is *not* required.)

*Remark 2.2 (randomised / point-indexed windows).* If $W(A)\sim\mu_A$ with
$\mu_A$ depending only on $A$ and drawn independently of the other side, T1–T3
hold with $|W(A)|,\pi_W$ replaced by expectations (same proof, conditioning on
the draws). This is what places **P5** (windows $=$ certificates of a random
point of its own set) inside the framework.

**T2 (value theorem: $\Theta_W$ bounds what the class can prove).** *Under (T2)
with any $\rho$, the threshold $T$ established by (T1)–(T3) satisfies
$T\le\Theta_W(d)$. In particular the frozen rung's variant "$\pi_W\ge p$,
$|W|\le m$, hence $\max\delta\ge p/(2m)$" yields at most $\Theta_W(d)$.*

*Proof.* The count's output for a family is
$\Lambda(\mathbf F,\mathbf G)=\mathbb E[\rho]/\mathbb E[|W(f)|+|W(g)|]$ when the
denominator is positive, and nothing otherwise; $T=\inf_{(\mathbf F,\mathbf G)}
\Lambda$ over the families for which the count concludes. If $W\equiv\emptyset$
on $\mathcal P_d$ the count concludes for no incompatible family, so no positive
$T$ is established and $T\le0=\Theta_W(d)$. Otherwise, for each
$(A,B)\in\mathcal P_d$ with $|W(A)|+|W(B)|\ge1$ the point masses at $f_A,f_B$
form an incompatible family with positive denominator, giving
$\Lambda=\rho(|W(A)|,|W(B)|)/(|W(A)|+|W(B)|)\le\pi_W(A,B)/(|W(A)|+|W(B)|)$ by
(T2); take the infimum over those pairs. For the variant: $p\le\pi_W(A,B)$ and
$2m\ge|W(A)|+|W(B)|$ give $p/(2m)\le\Theta_W(d)$. ∎

*(Pairs with both windows empty are simply not used: they contribute no
inequality here. See Remark 1.1.)*

**T3 (localisation ceiling).** *For localised $W$ and any $(A,B)\in\mathcal P_d$,*
$$\pi_W(A,B)\ \le\ \pi_{\mathrm{Rel}}(A,B)=\sum_{i\in S(A,B)}\bigl[\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)\bigr];$$
*hence $\Theta_W(d)\le\eta^*_W(d):=\inf\{\pi_{\mathrm{Rel}}(A,B):(A,B)\in\mathcal
P_d,\ |W(A)|+|W(B)|\ge1\}$ (and $\Theta_W=0$ in the degenerate case). In
particular*
$$\Theta_W(d)\ \le\ \eta^*(d):=\inf_{\mathcal P_d}\pi_{\mathrm{Rel}}
\qquad\text{for every localised }W\text{ with }W(A)\cup W(B)\ne\emptyset\text{ on all of }\mathcal P_d,$$
*which by T4(b) holds for $W_{\mathrm{rel}}$, $W_{\max}$, the shattering window
and the certificate windows — i.e. for every functional considered below.*

*Proof.* $\mathrm{Inf}_i(f_A)=0$ off $\mathrm{Rel}(A)$ and all influences are
$\ge0$, so $\sum_{i\in W(B)}\mathrm{Inf}_i(f_A)
=\sum_{i\in W(B)\cap\mathrm{Rel}(A)}\mathrm{Inf}_i(f_A)\le\sum_{i\in
S}\mathrm{Inf}_i(f_A)$ using $W(B)\subseteq\mathrm{Rel}(B)$; symmetrise, and note
the displayed identity is the case $W=W_{\mathrm{rel}}$. For the ceiling: at a
pair with $|W(A)|+|W(B)|\ge1$ the ratio is at most
$\pi_W(A,B)\le\pi_{\mathrm{Rel}}(A,B)$; take the infimum over exactly those
pairs, and note it is $\eta^*(d)$ when they are all of $\mathcal P_d$. ∎

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
$A\cap B$ — contradiction. (In particular $\mathrm{Rel}(A)\ne\emptyset$ on
$\mathcal P_d$.)
(c) $D_i:=\frac12(\mathbf 1_A(x^{i\to+1})-\mathbf 1_A(x^{i\to-1}))
=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)x_{S\setminus\{i\}}$ is a nonzero
multilinear polynomial of degree $\le d-1$ in the other $N-1$ variables, with
values in $\{0,\pm\frac12\}$; Parseval gives $\mathrm{Inf}_i(\mathbf
1_A)=\mathbb E[D_i^2]=\frac14\Pr[D_i\ne0]\ge\frac14 2^{-(d-1)}=2^{-d-1}$ by (a);
divide by $\alpha_A\le1$. *(This reproves block S6a of
`sources/S6-junta-degree-card.md` inline; no [RESTATED] item is load-bearing.)*
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

**Independent check.** `0023-prover-3-code/check_witnesses.py` (truth tables,
integer Walsh–Hadamard, exact `Fraction`s) reproduces for $k=1,2,3$:
$\alpha=1/2$, $\deg=k+1$, $|\mathrm{Rel}|=3,6,11$, influences $1/4$ and
$1/4,1/8,1/16$, $\pi_{\mathrm{Rel}}=3/2,2,5/2$, relevance-window ratios
$1/4,1/6,5/44$, and $2^k$ top supports each containing all address bits and
exactly one target — agreeing with T5 and with `proofs/0023-refuter-3.md` §4.

*Remark 3.1.* $A_k$ has degree $d$ and $2^{d-1}+d-1$ relevant coordinates, so
this witness **re-proves inline** that the relevance window of a degree-$d$ set is
exponential; blocks S6c/S6d of `sources/S6-junta-degree-card.md` are context
only.

**T6 (CAP I).** *Let $d\ge2$, $k=d-1$, $W$ any localised window functional with
$|W(A_k)|+|W(B_k)|\ge1$. Then*
$$\Theta_W(d)\ \le\ \frac{d+1}{2\bigl(|W(A_k)|+|W(B_k)|\bigr)} .$$
*Hence: (a) if $W\supseteq\mathrm{Rel}$ (in particular $W=W_{\mathrm{rel}}$, the
junta-substitution route), $\Theta_W(d)\le\frac{d+1}{4(2^{d-1}+d-1)}\le(d+1)2^{-d-1}$;
(b) with density $c>0$ on this family, $\Theta_W(d)\le\frac{d+1}{c\,2^{d+1}}$, so
$c\ge1/\mathrm{poly}(d)$ still leaves $2^{-\Theta(d)}$; (c) $|W(A_k)|+|W(B_k)|
\ge2^{\varepsilon d}$ alone gives $\Theta_W(d)\le(d+1)2^{-\varepsilon d}/2$.
In each of (a),(b),(c) the nonemptiness hypothesis is automatic
($\mathrm{Rel}(A_k)\ne\emptyset$; $c>0$ with $|\mathrm{Rel}|\ge1$;
$2^{\varepsilon d}\ge1$). If instead $W(A_k)=W(B_k)=\emptyset$, this pair
contributes no bound and no cap is claimed from it (Remark 1.1).*

*Proof.* $\Theta_W$ is an infimum over the pairs of $\mathcal P_d$ with nonempty
combined window, so it is at most the ratio at the admissible pair
$(A_k,B_k)$, which by T3 and T5(v) is at most
$\frac{(d+1)/2}{|W(A_k)|+|W(B_k)|}$. Then substitute
$|W(A_k)|+|W(B_k)|=2(2^{d-1}+d-1)$, $\ge2c(2^{d-1}+d-1)\ge c2^d$, or
$\ge2^{\varepsilon d}$. ∎

*Corollary 3.2 (what CAP I closes).* By T2, any argument in $\mathcal W$ with a
relevance-denominated window (density $\ge1/\mathrm{poly}(d)$) establishes at most
$\mathrm{poly}(d)2^{-d}$ — i.e. refuter-2's inequality (M) transplanted to
$\mathcal C^{\mathrm{ind}}_d$, the R1 proof with the junta size substituted
(I02's recorded non-solution, now with the explicit ceiling $(d+1)2^{-d-1}$), and
I02's flagged total-influence-budget route *in its per-coordinate form*, are all
capped. This is a statement about these sub-classes only.

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
`proofs/0023-refuter-3.md` §4.)

*Remark 4.2 (forced coordinates, inline).* Say $A$ *forces* $i$ if
$A\subseteq\{x:x_i=s\}$. **(a)** Then $\mathrm{Inf}_i(f_A)=\frac12$ exactly:
$\mathbf 1_A\frac{1-sx_i}2\equiv0$ gives $x_i\mathbf 1_A=s\mathbf 1_A$, so
$\widehat{\mathbf 1_A}(S\cup\{i\})=s\widehat{\mathbf 1_A}(S)$ for $S\not\ni i$,
whence $\mathrm{Inf}_i(\mathbf 1_A)=\frac12\lVert\mathbf
1_A\rVert^2_2=\frac{\alpha_A}2$. **(b)** A degree-$\le d$ set forces at most $d$
coordinates: forcing all of $F$ gives $\alpha_A\le2^{-|F|}$, while T4(a) gives
$\alpha_A=\Pr[\mathbf 1_A\ne0]\ge2^{-d}$. So $W_{\mathrm{Forced}}$ is localised,
own-heavy at $\theta=\frac12$, of size $\le d$; and $\mathrm{Forced}(C)=[d]$,
while $\mathrm{Forced}(D)=\emptyset$ **for $d\ge2$** (at $d=1$, $D=\{x_1=-1\}$
forces $x_1$; every use of this clause below is at $d\ge2$).

**T8 (CAP II).** *If $W$ is localised, own-heavy at some level
$\theta>\frac1{2(2^d-1)}$, and $W(C)\ne\emptyset$, then
$\Theta_W(d)\le\frac1{2(2^d-1)}$.*

*Proof.* By T7 every coordinate has $\mathrm{Inf}_i(f_D)\le\frac1{2(2^d-1)}
<\theta$, so $W(D)=\emptyset$; and $W(C)\ne\emptyset$ by hypothesis, so the pair
$(C,D)$ has a nonempty combined window and is admissible in D5's infimum. Then
$\pi_W(C,D)=0+\sum_{i\in W(C)}\mathrm{Inf}_i(f_D)=\frac{|W(C)|}{2(2^d-1)}$, and
$\Theta_W(d)\le\pi_W(C,D)/|W(C)|=\frac1{2(2^d-1)}$. ∎

*Remark 4.2$'$ (the nonemptiness hypothesis is satisfied by every concrete
own-heavy rule at issue).* For $W^\theta_{\mathrm{hvy}}$ with
$\theta\le\frac12$ one has $W^\theta_{\mathrm{hvy}}(C)=[d]$ (T7:
$\mathrm{Inf}_i(f_C)=\frac12$ for $i\in[d]$); likewise
$W_{\mathrm{Forced}}(C)=\mathrm{Forced}(C)=[d]$. So for every own-heavy rule
named in this artifact, T8 applies unconditionally whenever
$\frac1{2(2^d-1)}<\theta\le\frac12$. If a hypothetical own-heavy $W$ had
$W(C)=\emptyset$ as well, witness (b) would contribute no bound, and this
artifact would claim no cap for it (Remark 1.1).

**T9 (dichotomy: exactly which windows witness (b) kills).** *With
$w_C=|W(C)|,w_D=|W(D)|$ ($\le d$), $w_C+w_D\ge1$,*
$$\frac{\pi_W(C,D)}{w_C+w_D}=\frac{\frac12w_D+\frac{w_C}{2(2^d-1)}}{w_C+w_D}
=\frac1{2(2^d-1)}\ \text{if } w_D=0<w_C,\qquad \ge\frac1{2(w_C+w_D)}\ge\frac1{4d}\ \text{if } w_D\ge1 .$$
*So witness (b) caps a functional exponentially **iff** the functional omits the
cheap side's window entirely.* Hence the decisive question **for escaping witness
(b)** is not "$\min$ or sum?" but: **does my window ever contain a coordinate
cheap for its own function and expensive for the partner?** *That test is
necessary and sufficient for witness (b) alone.* It is **not** sufficient for
escaping the barrier as a whole: §8.1's $\eta^*$ ceiling binds every localised
window functional regardless of the answer, and CAP I bites through a different
mechanism (Remark 4.5), so a plan must also pass CAP I's size test.

*Remark 4.3 (corollaries).* Any window selected by an own-influence threshold
$\theta\ge1/\mathrm{poly}(d)$, or "the coordinates carrying a
$1/\mathrm{poly}(d)$ share of the budget $\sum_i\mathrm{Inf}_i\le d$" read as a
*threshold* rule, or $W_{\mathrm{Forced}}$, is capped at $\frac1{2(2^d-1)}$ for
all $d\ge d_0(\theta)$ (the strictness $\theta>\frac1{2(2^d-1)}$ in T8 is what
forces the $d_0$), the nonemptiness hypothesis being discharged by Remark 4.2$'$.
In particular **$W_{\mathrm{Forced}}$ is capped at $\frac1{2(2^d-1)}$**. Note
that the *address* pair contributes nothing here: it forces no coordinate on
either side, so both of $W_{\mathrm{Forced}}$'s windows are empty there and that
pair yields no bound (Remark 1.1) — the cap on $W_{\mathrm{Forced}}$ comes from
witness (b) alone. **No claim that $W_{\mathrm{Forced}}$ "establishes nothing at
all" is made**; what is proved is the exponential cap.
*Mass-denominated reading, not covered:* a count that charges payment against
$\sum_i\mathrm{Inf}_i$ itself, rather than against a window of bounded size, is
outside D4(T3) by construction and is **capped by nothing in this artifact**
([G1]).

*Remark 4.4 (this strictly strengthens refuter-3's killer (b)).*
`proofs/0023-refuter-3.md` §5.2 refutes the **$\min$-form** route
(HEAVY$_\theta$) via $\theta^*(d)\le\frac1{2(2^d-1)}$, and
`proofs/0023-strategist-2.md` IG3 correctly notes that this does not bind
**sum-form** payments (on $(C,D)$ the sum payment is $\ge d/2$). T8 closes that
gap from the other side: the sum payment is large only because $W(C)=[d]$
contains coordinates cheap for $C$'s partner; a rule that refuses own-cheap
coordinates collapses to the same exponential value. **The min$\to$sum move is
necessary but not sufficient — the necessity is inherited from
`0023-refuter-3` §5.2 (CERTIFIED, not verified), the insufficiency is T8**; the
sufficient condition for witness (b) is T9's italicised question.

*Remark 4.5 (duality).* CAP I kills through the denominator (exponential window,
$\Theta(d)$ payment); CAP II through the numerator ($\le d$ window,
$2^{-\Theta(d)}$ payment). A functional escaping **both caps** needs **both**:
**(α)** a **sub-exponential — effectively $\mathrm{poly}(d)$ — window size on the
address family** (not merely a relevance-independent bound: by T6(c) even a
relevance-independent size $2^{\varepsilon d}$ is still capped at
$(d+1)2^{-\varepsilon d}/2$, so what is needed is $|W(A_k)|+|W(B_k)|
\le\mathrm{poly}(d)$, or at least $2^{o(d)}$); and **(β)** the quantitative
negation of own-heaviness at witness (b): **$W(D)$ must contain a coordinate $i$
with $\mathrm{Inf}_i(f_D)\le\frac1{2(2^d-1)}$**, i.e. $W$ is not own-heavy at any
level strictly above $\frac1{2(2^d-1)}$. (α) and (β) are necessary to escape
these two caps; they are **not** claimed sufficient for anything — §8.1's ceiling
applies regardless.

## 5. SCOPE: the caps hold in the object classes of R2–R6

**5.1 Class-genericity.** For any family $\mathcal C$ of unit-norm degree-$\le d$
functions, with $\mathrm{Rel}(h)=\{i:\mathrm{Inf}_i(h)>0\}$, $\mathcal
P_d(\mathcal C)=\{(h_1,h_2):h_1h_2\equiv0\}$ and D1–D5 unchanged, the proofs of
T1, T2, T3 hold verbatim (they use only: incompatibility $=$ all cross pairs in
$\mathcal P_d(\mathcal C)$; independence; $\mathrm{Inf}\ge0$; admissibility of
point masses; vanishing off $\mathrm{Rel}$). T4's *floor* is indicator-specific
and is used in no cap.

**5.2 Monotonicity.** If $\mathcal C\subseteq\mathcal C'$ and $W=W'|_{\mathcal
C}$ then $\Theta^{\mathcal C'}_{W'}(d)\le\Theta^{\mathcal C}_{W}(d)$: $\mathcal
P_d(\mathcal C)\subseteq\mathcal P_d(\mathcal C')$, so the infimum is over a
superset. **Caps proved by exhibiting a witness inside $\mathcal
C^{\mathrm{ind}}_d$ therefore hold over every larger class, and provably never
transfer downward.**

**5.3 The witnesses are singleton indicator pairs.** $f_{A_k},f_{B_k},f_C,f_D$
are unit-norm, nonnegative, $\{0,\text{const}\}$-valued, of degree $\le d$;
$(A_k,B_k)$ and $(C,D)$ are cross-disjoint; as point masses they satisfy each
rung's hypotheses with $\delta=\max_i\mathrm{Inf}_i$. Hence they lie in
$$\mathcal C^{\mathrm{ind}}_d\ \subset\ \mathcal C^{+}_d\ \subset\ \{\mathbb R\text{-valued},\lVert\cdot\rVert_2=1,\deg\le d\}\ \subset\ \{\mathbb C\text{-valued},\dots\},$$
i.e. in the object classes of **R2 ⊂ R3 ⊂ R4/R5/R6′ ⊂ R6($\mathbb Z_2$)**. The
rung classes, restated so that this file needs no other campaign document
(source: `PROGRESS.md`, ladder R1–R6 and "Declared route"): **R2** normalised
indicators of degree-$\le d$ sets over $\mathbb Z_2$ (this rung, I02); **R3**
arbitrary nonnegative unit-norm degree-$\le d$ functions; **R4** the full signed
$\mathbb R$-valued class with the weaker target $c\,e^{-d^\alpha}$, $\alpha<1$;
**R5** the full signed class at the inverse-polynomial frontier but only for
point-mass distributions; **R6′** the $\mathbb Z_2$, $\mathbb R$-valued,
arbitrary-finite-support instantiation at inverse-polynomial $\delta$;
**R6($\mathbb Z_2$)** the top rung's $\mathbb Z_2$ instantiation.

With 5.2: **CAP I and CAP II hold in the object class of every one of R2, R3,
R4, R5, R6′ and R6($\mathbb Z_2$)**, with the same numerical ceilings. R5 needs
no distributional part (T2 already evaluates at point masses).

*Consequence for R4, stated with the correct quantifier (U1).* R4's target is
$c\,e^{-d^\alpha}$ with $\alpha<1$, and $(d+1)2^{-d-1}<c\,e^{-d^\alpha}$ for all
$d\ge d_0(c,\alpha)$ — explicitly, for every $d$ with
$(d+1)\ln2-\ln(d+1)-d^\alpha\ge\ln(1/c)$, and such a $d_0$ exists and is
computable since the left side is eventually increasing to $+\infty$ (as
$\alpha<1$); likewise $\frac1{2(2^d-1)}<c\,e^{-d^\alpha}$ for all large $d$.
Therefore:
> **no relevance-denominated window-payment argument, and no
> own-heavy-at-$\theta>\frac1{2(2^d-1)}$ window-payment argument, can establish
> R4's target $c\,e^{-d^\alpha}$ — or any threshold above $(d+1)2^{-d-1}$ resp.
> $\frac1{2(2^d-1)}$ — in the object class of R2, R3, R4, R5, R6′ or
> R6($\mathbb Z_2$).**

**This does *not* say that "the class $\mathcal W$ cannot deliver R4", and R4 is
NOT condemned by this artifact.** $\mathcal W$ contains members that no cap here
touches (§7: the shattering window, the minimum-certificate window, $W_{\max}$,
and by the same token any per-function case-split window with a
$\mathrm{poly}(d)$ size bound on the address family and an own-cheap coordinate
at witness (b)), and $\eta^*(d)\in[2^{-d},1]$ is open (§8.2). The ladder record
must carry the displayed conditional sentence, not a summary of it.

**5.4 Groups.** *CAP II generalises to every finite abelian group $\mathcal Y$*:
with $C_{\mathcal Y}=\{x:x_1=\dots=x_d=y_0\}$,
$\widehat{\mathbf 1_{C_{\mathcal Y}}}(\chi)$ is nonzero exactly on the
$|\mathcal Y|^d$ characters supported in $[d]$, each of modulus
$|\mathcal Y|^{-d}$; so $\deg=d$, $\alpha=|\mathcal Y|^{-d}$,
$\mathrm{Inf}_i(f_{C_{\mathcal Y}})=1-|\mathcal Y|^{-1}$ and
$\mathrm{Inf}_i(f_{D_{\mathcal Y}})=\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^d-1}$,
and T8's proof runs verbatim with cap
$\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^{d}-1}$. *CAP I* holds for $\mathbb Z_2$
and, by pullback along a surjective homomorphism $\varphi:\mathcal Y\to\mathbb
Z_2$, for every **even-order** group: the dual map $\hat\varphi$ is injective, so
$h\mapsto h\circ\varphi^{N}$ preserves each Fourier coefficient, hence degree,
all influences and $\alpha$ (each fibre of $\varphi$ has the same size, so
$\varphi^N$ is measure-preserving), and it preserves disjointness of supports;
and a finite abelian group admits a $\mathbb Z_2$ quotient iff its order is even.
For odd order see **[G2]**.

## 6. CALIBRATION: what the barrier does NOT condemn

**6.1 Frozen I01 / R1 — not condemned.** R1's engine *is* a window-payment
argument with $W\supseteq\mathrm{Rel}$ (CAP I's technique sub-class), payment
$\ge1$, $|W|\le d$, assembled by T1. But its object class is
$\mathcal C^{\mathrm{junta}}_d$ (normalised indicators of $\le d$-window
cylinder-*pattern* sets $\{x:x_J\in P\}$, $|J|\le d$, $\emptyset\ne
P\subseteq\{\pm1\}^J$), which **does not contain witness (a)**
($|\mathrm{Rel}(A_k)|=2^{d-1}+d-1>d$), and by 5.2 caps never transfer downward.
Witness (b) *is* in that class ($D=C^c$ is the pattern set with $P$ all patterns
but one), but R1's window is not own-heavy (on $D$ it is $[d]$, all of whose
coordinates are cheap for $D$), and T9 gives $\ge\frac14$ there — consistent with
R1's proved $\frac1{2d}$. **This is exactly why the caps of §5.3 must be stated
relative to an object class:** dropping that relativisation would falsely condemn
frozen R1.
**One-sentence diagnosis of the R1→R2 jump:** *R1 is provable by a
relevance-denominated payment because its class caps the relevance window at $d$
by fiat; R2 is not, because its class contains a degree-$d$ set with $2^{d-1}$
relevant coordinates and only $\Theta(d)$ units of payment to spread over them.*

**6.2 refuter-3 §5.1's $1/(8d)$ forcing bound — not condemned.** It is the
window-payment argument with $W=W_{\mathrm{Forced}}$ **restricted to forcing
pairs**, where $\pi_W\ge\frac12+\frac12=1$ and $|W|\le d$ (Remark 4.2), giving
$\ge\frac1{2d}$ on that sub-class — a genuine $\mathrm{poly}(d)$ result, exactly
as declared, and the same computation as `proofs/0023-refuter-3.md` §5.1 (which
also proves that any family with $\Pr[\text{forcing}]\ge\frac12$ has
$\max\delta\ge1/(8d)$). CAP II speaks only of the route to **all** of R2 and says
precisely refuter-3's own caveat: witness (b) is not a forcing pair
($\mathrm{Forced}(D)=\emptyset$ for $d\ge2$), so the inequality $\pi_W\ge1$ fails
there, and over all of $\mathcal P_d$ the functional $W_{\mathrm{Forced}}$ is
capped, $\Theta_{W_{\mathrm{Forced}}}(d)\le\frac1{2(2^d-1)}$ (Remark 4.3). *No
claim that $W_{\mathrm{Forced}}$ establishes nothing at all is made.*

**6.3 P4, K1, P2 — outside the class.** P4 (OSSS + depth-vs-degree, variance vs
max influence) has no window and no per-pair payment; K1's proof (card S1,
`sources/S1-acc22-card.md`) is a Cauchy–Schwarz over the
$|\mathcal Y|^d-1$ non-constant blocks; P2 exhibits a common point. None is in
$\mathcal W$ (D4), so no cap applies. Nor is the mass-denominated count of
Remark 4.3 in $\mathcal W$.

**6.4 Consistency with proved thresholds (a self-check; used nowhere).** A cap
below a proved threshold would refute the barrier. Both caps sit above K1's
$2^{-d}/d$: $\frac{2^{-d}}d\le(d+1)2^{-d-1}$ for $d\ge1$, and
$\frac{2^{-d}}d\le\frac1{2(2^d-1)}$ for $d\ge2$ (as $d2^d\ge2(2^d-1)$) — this is
the consequential direction. In the other direction, comparison with the grid
ceiling $\frac1{2d}$ (card S1 Claim B.3, restated in I02) is **not** uniform in
$d$: exactly, $(d+1)2^{-d-1}=\frac12,\frac38,\frac14,\frac5{32}$ against
$\frac1{2d}=\frac12,\frac14,\frac16,\frac18$ at $d=1,2,3,4$ — equal at $d=1$ and
strictly **larger** at $d=2,3,4$, with the first strict inequality
$(d+1)2^{-d-1}<\frac1{2d}$ at $d=5$ ($\frac3{32}<\frac1{10}$). So **CAP I lies
below the grid ceiling only for $d\ge5$**; CAP II's $\frac1{2(2^d-1)}$ lies below
it for all $d\ge2$. Nothing in this artifact uses the comparison.

## 7. CLAUSE (iv): P1 and P5 escape both caps

*Standing reading for this whole section (U3).* Each displayed ratio is the value
of $\pi_W/(|W(A)|+|W(B)|)$ **at one pair**, hence an **upper** bound on
$\Theta_W(d)$. What such a computation establishes is that *this witness
contributes no cap below that number* — equivalently, the cap that this witness
would impose is inverse-polynomial, not $2^{-\Theta(d)}$. Together with the
verified failure of each cap's hypotheses, that is the escape. **No lower bound
on $\Theta_{W_{\mathrm{sh}}}$, $\Theta_{\text{cert}}$ or
$\Theta_{W_{\max}}$ is claimed, and none follows**: by T3 each is
$\le\eta^*(d)\in[2^{-d},1]$, and pinning $\eta^*$ is the open problem of §8.2.

**7.1 P1 (shattering window).** $W_{\mathrm{sh}}(A):=$ any maximum-degree
monomial support of $\mathbf 1_A$ — i.e. the plan's window in the sense of
`proofs/0023-strategist-2.md` §2, table V1 ("*shattering window $W(A)$ | any
maximum-degree monomial support*"), whose surjectivity ("shattering") property is
used elsewhere in P1 but **not here**. Its size bound is **definitional, not a
citation**: a maximum-degree monomial support is a set $S$ with
$\widehat{\mathbf 1_A}(S)\ne0$ and $|S|=\deg\mathbf 1_A$, so
$|W_{\mathrm{sh}}(A)|=\deg\mathbf 1_A\le d$ by the Contract's definition of
degree. It is nonempty on $\mathcal P_d$ (both sides have $\deg\ge1$ there, since
$\deg\mathbf 1_A=0$ forces $A=\{\pm1\}^N$ and then $B=\emptyset$). Localised.
Exact values:
* **On witness (a)** (T5(ii)): $W_{\mathrm{sh}}(A_k)=\{a_1..a_k,y_j\}$,
  $W_{\mathrm{sh}}(B_k)=\{a_1..a_k,y_{j'}\}$ for some targets $j,j'$, so
  $\pi=\bigl(\frac k4+2^{-k-1}\bigr)\cdot2=\frac k2+2^{-k}$ and
  $$\frac{\pi}{2d}=\frac{k/2+2^{-k}}{2(k+1)}\ \ge\ \frac k{4(k+1)}\ \ge\ \frac18\quad(k\ge1),$$
  **for every choice of the two supports** (exact: $1/4,5/24,13/64$ for
  $k=1,2,3$). So witness (a) contributes no cap below $1/8$.
* **On witness (b)** (T7): $W_{\mathrm{sh}}(C)=W_{\mathrm{sh}}(D)=[d]$ (unique
  top support each), $\pi=\frac d2+\frac d{2(2^d-1)}$, ratio
  $=\frac14+\frac1{4(2^d-1)}>\frac14$. So witness (b) contributes no cap below
  $\frac14$.

Both caps' hypotheses fail *quantitatively*: the density on witness (a) is
$d/(2^{d-1}+d-1)=2^{-\Theta(d)}$, so CAP I(b)'s own ceiling degrades to
$(d+1)/(4d)\approx\frac14$, vacuous against the $\frac1{2d}$ grid ceiling; and
$W_{\mathrm{sh}}(D)=[d]$ is own-cheap, so CAP II's own-heaviness hypothesis fails
at every level $>\frac1{2(2^d-1)}$ and T9's second branch applies
($\ge\frac1{4d}$). **P1 is therefore not capped by CAP I, by CAP II, or by either
certified witness.** Whether P1 succeeds is §8.5's open milestone.

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
(iii),(iv) immediate (for (iv), $|W(A_k)|+|W(B_k)|\ge2^{k}\ge1$ in T6, so T6's
nonemptiness hypothesis holds). ∎

*Reading.* P1's escape is purchased **exactly** by non-canonicity — obstacle (ii)
of card S7 (`sources/S7-changfang26-card.md`). It is legitimate: T1 requires only
per-function dependence (Remark 2.1), and P1's (PAY$\star$) is quantified over
*all* selections, which is stronger than the count needs. Its price: within the
canonical world, a functional must be exponentially large on the address family
(capped) or confine itself to the address hub; a canonical route cannot choose
among $2^{d-1}$ symmetric targets.

**7.3 A new canonical survivor: $W_{\max}(A):=\{i:\mathrm{Inf}_i(f_A)=
\max_j\mathrm{Inf}_j(f_A)\}$**, with the convention
$W_{\max}(A):=\emptyset$ when $\mathrm{Rel}(A)=\emptyset$ (which never occurs on
$\mathcal P_d$, by T4(b), so $W_{\max}$ is nonempty there). Canonical and
localised. On witness (a), $k\ge2$: $W_{\max}=\{a_1..a_k\}$ on both sides,
$\pi=k/2$, ratio $\frac14$. On witness (b): $W_{\max}=[d]$ on both sides, ratio
$\frac14+\frac1{4(2^d-1)}$. Hypothesis check: its density on witness (a) is
$(d-1)/(2^{d-1}+d-1)=2^{-\Theta(d)}$, so CAP I(b) degrades to a vacuous
$\approx\frac14$; and it is **not own-heavy at any level strictly above
$\frac1{2(2^d-1)}$**, since by T7 witness (b)'s $D$ has $W_{\max}(D)=[d]$ with
$\mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)}$ *exactly*, so the inclusion required at
any $\theta>\frac1{2(2^d-1)}$ fails — and that strict form is precisely what
CAP II requires. **So $W_{\max}$ escapes both caps and is canonical** — a live
functional no plan proposes. Caveats: no payment inequality is known for it (so
nothing is claimed about its value); and its size is
$\le d/\max_i\mathrm{Inf}_i(f_A)$, hence $\mathrm{poly}(d)$ exactly when the
sparser side has $\max_i\mathrm{Inf}_i\ge1/\mathrm{poly}(d)$ — P4's uncarded gate
(**[MEMORY: OSSS + depth-vs-degree]**; flagged, used in no claim).

**7.4 P5 (certificate window).** *Certificate notions, declared (U4).* For
$x\in A$, a **certificate** is a set $S\subseteq[N]$ such that every $y$ agreeing
with $x$ on $S$ lies in $A$; it is **minimal** if no proper subset is one, and a
**minimum** certificate if it has the least size among all certificates of $x$.
Every minimum certificate is minimal; the converse fails. **P5's plan uses
*minimal* certificates with an averaged inequality over
$x\sim\mathrm{Unif}(A),y\sim\mathrm{Unif}(B)$; §7.4 evaluates *minimum*-size
certificates**, and a *selection* means a choice, for each $x$, of one such
certificate. Both notions give localised windows (a minimal certificate's
coordinates are relevant, [G4]) and are randomised in the sense of Remark 2.2
when $x\sim\mathrm{Unif}(A)$. P5's generic size bound $O(d^4)$ (block S6c of
`sources/S6-junta-degree-card.md` plus the textbook $C\le\mathrm{bs}\cdot s$) is
**not needed**: on the witnesses the certificates are explicit.

* **Witness (a), minimum certificates, computed over all selections.** Let
  $x\in A_k$ ($d=k+1$) and let $U\subseteq[k]$ be the address bits a certificate
  leaves free, $u=|U|$. Every certificate must fix the $k-u$ remaining address
  bits and, since the free bits realise all addresses $b(a)\oplus v$
  ($v\subseteq U$), must also fix all $2^u$ targets $y_{b(a)\oplus v}$ — each to
  $+1$, which requires those targets to be $+1$ at $x$. Hence every certificate
  has size $k-u+2^u\ge\min_{0\le u\le k}(k-u+2^u)=k+1=d$, with the minimum
  attained **exactly at $u\in\{0,1\}$**; the same count holds for $x\in B_k$ with
  $-1$ in place of $+1$. Consequently the **minimum certificate is of size $d$
  but is NOT unique**: the $u=0$ choice always works, and each $t\in[k]$ with
  $y_{b(a)\oplus e_t}$ of the correct sign at $x$ gives a further one, so the
  number of minimum certificates of a point is between $1$ and $k+1$ and depends
  on $x$ (exhaustive enumeration of **all** minimum certificates of **all** points
  of both sides, exact `Fraction`s, $k=1,2,3$, in
  `proofs/0023-prover-3-r2-code/check_min_certificates.py`: sizes all $=d$,
  observed multiplicities $1$–$2$, $1$–$3$, $1$–$4$. The earlier script
  `0023-prover-3-code/check_witnesses.py` returned only *one* minimum certificate
  per point, which is why the false uniqueness claim survived it.)
  Payment, for a selection using $u_A$ free address bits on the $A$-side and
  $u_B$ on the $B$-side (windows of size $d$ each, so denominator $2d$):
  $$\pi=\Bigl[\tfrac{k-u_B}4+2^{u_B}2^{-k-1}\Bigr]+\Bigl[\tfrac{k-u_A}4+2^{u_A}2^{-k-1}\Bigr],$$
  which is minimised over admissible selections at $u_A=u_B=1$ (the $u=0$ value
  exceeds the $u=1$ value by $\frac12-2^{-k}\ge0$). Hence **for every selection**
  $$\frac{\pi}{2d}\ \ge\ \frac{\frac{k-1}2+2^{1-k}}{2(k+1)}\ \ge\ \frac18
  \qquad(k\ge1),$$
  the last inequality being equivalent to $k\ge3-2^{3-k}$, true for all $k\ge1$.
  The minimum over $k$ of the worst-selection ratio is $\frac5{32}$, at $k=3$
  (values $\frac14,\frac16,\frac5{32},\frac{13}{80},\dots$ for $k=1,2,3,4$;
  exhaustively confirmed for $k\le3$ by the enumeration cited above, which
  returns exactly $\frac14,\frac16,\frac5{32}$ as the minima over all points and
  all selections on both sides).
  **For the declared $u=0$ selection only**, the payment is exactly P1's,
  $\frac k2+2^{-k}$, with ratio $\frac14,\frac5{24},\frac{13}{64}$ at
  $k=1,2,3$. Either way, **witness (a) contributes no cap below
  $\frac5{32}>\frac18$.**
  *Selection warning.* The bound above is for **minimum**-size certificates. The
  plan's *minimal* certificates can be much larger here: at a point of $A_k$
  whose $2^k$ targets are all $+1$, the set of all $2^k=2^{d-1}$ targets is a
  minimal certificate. Whether an arbitrary minimal-certificate selection has
  $\mathrm{poly}(d)$ *expected* window size on witness (a) — which is what
  Remark 2.2 and CAP I(b) would test — is **not settled here** ([G5]). P5 must
  therefore declare its selection rule; a minimum-size rule is what §7.4
  evaluates and what escapes.
* **Witness (b).** $T_C(x)=[d]$ is the unique minimum certificate of any
  $x\in C$; $T_D(y)=\{i\}$ for any $i\le d$ with $y_i=-1$, a minimum certificate
  of size $1$ (multiplicity $=\#\{i\le d:y_i=-1\}\in[1,d]$, so again not unique,
  but the payment does not depend on which is chosen). So
  $\pi=\frac12+\frac d{2(2^d-1)}\ge\frac12$ over windows summing to $d+1$, and
  the ratio is $\frac{\frac12+\frac d{2(2^d-1)}}{d+1}\ge\frac1{2(d+1)}$
  (exact: $5/18,5/28,19/150$ at $d=2,3,4$) — **for every selection**. So
  witness (b) contributes no cap below $\frac1{2(d+1)}$.

Both caps' hypotheses fail as in §7.1 (size bounded by a block-sensitivity
theorem, not by relevance; $T_D(y)$ own-cheap, so own-heaviness fails at every
level $>\frac1{2(2^d-1)}$). **P5 is therefore not capped by CAP I, by CAP II, or
by either certified witness** — for minimum-size selections; see [G5] for the
unrestricted minimal-certificate variant. No lower bound on
$\Theta_{\text{cert}}$ is claimed.

**7.5 A precise drafting warning for P5 (new).** P5's payment is over
$\Sigma(x,y)$, the coordinates the two certificates fix *oppositely*, and
$\Sigma(x,y)\subseteq T_A(x)\cap T_B(y)\subseteq W(A)\cap W(B)$, so
$\pi_\Sigma\le\pi_W$ (influences are $\ge0$) — which is why the caps bind P5's
actual averaged inequality. **For the declared $u=0$ minimum-certificate
selection** on witness (a), $i\in\Sigma$ iff ($i=a_t$ and $a_t\ne a'_t$) or
($i=y_{b(a)}$ and $a=a'$), hence
$$\sum_{i\in\Sigma(x,y)}\bigl[\mathrm{Inf}_i(f_{A_k})+\mathrm{Inf}_i(f_{B_k})\bigr]
=\tfrac12\bigl|\{t:a_t\ne a'_t\}\bigr|+2^{-k}\mathbf 1\{a=a'\},$$
which is $2^{-k}=2^{-\Theta(d)}$ in the **worst case** over points but has
**average** $\frac k4+4^{-k}\ge\frac{d-1}4$ (addresses are independent uniform
under $x\sim\mathrm{Unif}(A_k)$, $y\sim\mathrm{Unif}(B_k)$); exact-arithmetic
check for $k\le4$: worst $2^{-k}$, average $\frac k4+4^{-k}$. (For other
selections the $\Sigma$-characterisation changes; the worst-case value $2^{-k}$
is what matters below and is attained already at $u=0$.) On witness (b) every
point pair pays $\ge\frac12$. **So P5's averaged inequality is not capped by
witness (a), but any per-point ($\forall x,y$) variant IS capped at
$2^{-\Theta(d)}$ by witness (a).** P5 must therefore stay averaged, and must use
Remark 2.2's randomised count.

## 8. FRONTIER: one number caps the whole method

1. **(Universal ceiling)** For every localised $W$ — canonical or not,
   deterministic or randomised, point-indexed or not — that is nonempty on the
   pairs approaching the infimum below (in particular for $W_{\mathrm{rel}}$,
   $W_{\mathrm{sh}}$, $W_{\max}$ and the certificate windows, all nonempty on all
   of $\mathcal P_d$ by T4(b) and §7.1),
   $$\Theta_W(d)\le\eta^*(d)=\inf_{\mathcal P_d}\sum_{i\in S(A,B)}[\mathrm{Inf}_i(f_A)
   +\mathrm{Inf}_i(f_B)]$$
   (T3, Remark 2.2). A $W$ that is empty at some pairs is bounded by the
   restricted infimum $\eta^*_W(d)$ of T3 instead; nothing further is claimed
   about it (Remark 1.1).
2. **(Bracket, open)** $2^{-d}\le\eta^*(d)\le1$, the upper bound attained by the
   grid pair (T4(d)). **Where $\eta^*$ sits in this bracket is not determined by
   this artifact**, and no result here may be read as pinning it.
3. **(Sufficiency, one direction only)** If some pair $(A,B)\in\mathcal P_d$ has
   $\pi_{\mathrm{Rel}}(A,B)=2^{-\Theta(d)}$ — i.e. *all* its shared relevant
   coordinates are cheap for **both** sides (each contributes $\ge2^{-d}$ by
   T4(c), so such a pair also has $|S|\le2^{\Theta(d)}$) — then **every localised
   $W$ with a nonempty combined window at that pair is capped at
   $2^{-\Theta(d)}$, which includes P1, P5 and $W_{\max}$**, and the whole method
   dies. The converse is **not** claimed ([G3]): CAP II caps a sub-class while
   $\pi_{\mathrm{Rel}}(C,D)=\Theta(d)$ is large. What
   $\eta^*\ge1/\mathrm{poly}(d)$ would establish is that no further cap can come
   from the localisation ceiling alone; it must exploit the window selection
   rule, as CAP II does.
4. **(The certified witnesses cannot supply it)**
   $\pi_{\mathrm{Rel}}(A_k,B_k)=\frac{d+1}2$ and
   $\pi_{\mathrm{Rel}}(C,D)=\frac d2+\frac d{2(2^d-1)}$ — both $\Theta(d)$.
5. **(New necessary condition for P1)** (PAY$\star$) at constant $p$ — i.e.
   $\pi_{W_{\mathrm{sh}}}\ge p$ at every pair and every selection — implies
   $\eta^*(d)\ge p$ (since $\pi_{W_{\mathrm{sh}}}\le\pi_{\mathrm{Rel}}$, T3).
   With 2, **(PAY$\star$) at $p=1$ forces $\eta^*(d)=1$ exactly**, the grid being
   extremal. Falsifiable milestone, strictly easier than (PAY$\star$) itself (no
   window choices are quantified): **search for a cross-disjoint degree-$\le d$
   pair with $\pi_{\mathrm{Rel}}<1$.** A hit refutes $p=1$ (not R2); a hit at
   $2^{-\Theta(d)}$ kills the entire window-payment class in the sense of item 3.

---

## GAP REGISTER

* **[G1] LOAD-BEARING, DEFINITIONAL (not a gap in a proof).** D4's stipulation —
  that a member of $\mathcal W$ uses *only* (T2) per-pair and *only*
  $\delta_{\mathbf F},\delta_{\mathbf G}$ plus window **sizes** in (T3) — is what
  "the class" means. T2 then bounds the class's output. Any argument that uses
  more is **not** constrained by anything here. Named non-members, each capped by
  nothing in this artifact: level weights; hypercontractivity; coordinate
  correlations; **pair-dependent windows** (they break T1's factorisation,
  Remark 2.1 — the substantive exclusion, not a convenience); fibre
  renormalisation; variance identities; constructive witnesses; **and, at the
  rung's own central question, the mass-denominated count** — charging payment
  against the influence *mass* $\sum_i\mathrm{Inf}_i\le d$ (I02, "charging
  payment against influence mass rather than against a bounded window") instead
  of against a window size. D4(T3) admits only window sizes as the denominator,
  so the mass-denominated form is outside $\mathcal W$ **by construction** and is
  **not capped here in either direction**; only its *thresholded* reading ("the
  coordinates carrying a $1/\mathrm{poly}(d)$ share of the budget") is covered,
  via CAP II (Remark 4.3). **The class is not exhaustive and is not claimed to
  be**; §6.3 and §7 name concrete non-members and concrete uncapped members.
* **[G2] GAP (scope limitation, not attempted).** CAP I is not established for
  finite abelian groups of **odd** order (no $\mathbb Z_2$ quotient, no native
  address witness given). Affects only CAP I, only odd-order groups, only at the
  top rung; the ladder's declared route is $\mathbb Z_2$.
* **[G3] Routine.** §8.3's converse is explicitly not proved; the one-directional
  statement is what is used.
* **[G4] Routine.** The claim that minimal-certificate coordinates are relevant
  is proved in one line in the unit file (`0023-prover-3-u5`, L11) and used only
  to check localisation, which is also evident from the explicit certificates.
* **[G5] GAP (new, from the U4 repair; load-bearing only for the *minimal*
  variant of P5).** §7.4 evaluates **minimum**-size certificate selections. For
  an unrestricted **minimal** (irredundant) selection, witness (a) admits minimal
  certificates of size $2^{d-1}$ (the all-targets certificate at a point whose
  targets are all $+1$), so whether such a selection keeps
  $\mathbb E|W(A_k)|=\mathrm{poly}(d)$ — the quantity CAP I(b) tests under
  Remark 2.2 — is not determined here. The escape claim of §7.4 is asserted for
  minimum-size selections only. The *hypothesis-failure* half (own-cheap $T_D$ at
  witness (b), so CAP II does not apply) holds for both notions.
* **[MEMORY, flagged, unused]** `0023-refuter-3` §5.3's "Boolean case of
  Aaronson–Ambainis" remark and the OSSS + depth-vs-degree chain are cited in
  **no** claim; they appear only in §7.3's caveat about $W_{\max}$'s window size,
  explicitly as an open conditional.
* **[ESCALATED E1, human]** the empty-window convention of D5 / Remark 1.1: which
  of the two candidate refinements the class model should adopt. No cap here uses
  either; both caps carry explicit nonemptiness hypotheses instead.
* No [SOURCE-BLOCKED] item exists in this artifact, and none is load-bearing.

## DEPENDENCIES

Each row cites the **file path** and the **internal block id** inside it.

| ref (block) | file | statement used | status | where | load-bearing? |
|---|---|---|---|---|---|
| **S1** | `sources/S1-acc22-card.md` | K1: ACC22 Thm 4.4, compatibility for $\delta<\|\mathcal Y\|^{-d}/d$; Claim B.3 grid ceiling $1/(2d)$ | CARD, READ | §6.3, §6.4 consistency checks | no (comparative) |
| **S7** (obstacle (ii)) | `sources/S7-changfang26-card.md` | that a *pair-dependent* window is the obstacle to per-function factorisation | CARD, READ | Remark 2.1, §7.2 *Reading* | no (framing) |
| **S7b** (items T1.2 / Cor. 3.4) | `sources/S7-changfang26-card.md` (S7b addendum, inline) | Chang–Fang support-shattering: $\mathrm{supp}(f)$ shatters $S^c$; $\dim_\pi(\mathrm{supp}f)+\deg_{\hat G}(f)\ge n$ | CARD, READ | **not used in §7.1** — the size bound $\|W_{\mathrm{sh}}(A)\|=\deg\mathbf 1_A\le d$ is definitional (see §7.1); the shattering/projection property is used only in P1's own positivity lemma, elsewhere | **no** |
| **S6c** | `sources/S6-junta-degree-card.md` | Wellens: $M(d)\le4.394\cdot2^{d}$; and, with the textbook $C\le\mathrm{bs}\cdot s$, P5's $O(d^4)$ certificate bound | CARD, READ | §7.4 (explicitly *not needed*); remark in `0023-prover-3-u1` (L4.4) | no |
| **S6d** | `sources/S6-junta-degree-card.md` | CHS lower bound $M(d)\ge3\cdot2^{d-1}-2$ | CARD, READ | context; superseded inline by Remark 3.1 | no |
| **S6a** | `sources/S6-junta-degree-card.md` | NS94 influence quantum $\ge2^{-1-d}$ | CARD, RESTATED | **re-proved inline** as T4(c) | no |
| — | `proofs/0023-refuter-3.md` §4 | the two witness families and their influence tables | CERTIFIED (not verified) | supplied the *leads*; every number re-derived here (T5, T7) and re-checked exactly | no |
| — | `proofs/0023-refuter-3.md` §5.1 | forcing-only families never beat $1/(2d)$; $\Pr[\text{forcing}]\ge\frac12\Rightarrow\max\delta\ge1/(8d)$ | CERTIFIED (not verified) | §6.2 calibration | no |
| — | `proofs/0023-refuter-3.md` §5.2 | refutation of the $\min$-form (HEAVY$_\theta$) route, $\theta^*(d)\le\frac1{2(2^d-1)}$ | CERTIFIED (not verified) | Remark 4.4's *necessity* half, attributed there | no (attributed, not re-proved) |
| — | `proofs/0023-refuter-3.md` §5.3 | the "two killers are not counterexamples" rigidity, incl. the Aaronson–Ambainis remark | CERTIFIED (not verified) | [MEMORY] item only; no claim | no |
| — | `proofs/0023-strategist-2.md` §2 table V1, §3.1 (PAY$\star$), §0.6, IG3 | P1's window ("any maximum-degree monomial support", size $\le d$) and P5's window; the ruling that P1/P5 are live; the min$\to$sum observation | CAMPAIGN ARTIFACT, READ | §7.1, §7.4, Remark 4.4, VERDICT 1 | no (fidelity of the objects evaluated) |
| — | `proofs/0023-prover-1.md` (I01) | frozen R1 statement and the class $\mathcal C^{\mathrm{junta}}_d$ (cylinder-*pattern* sets, $\le d$-windows) | FROZEN | §6.1 calibration only; **not re-derived** | no |
| — | `PROGRESS.md`, ladder R1–R6 and "Declared route" | the rung classes R2, R3, R4, R5, R6′, R6($\mathbb Z_2$) and R4's target $c\,e^{-d^\alpha}$ | CAMPAIGN FILE, READ; restated in §5.3 | §5.3 scope chain, VERDICT 3 | yes, for the *scope* clause only (and restated inline so this file is self-contained) |
| — | `intermediates/I02-degree-d-sets.md` | the rung statement; its flagged influence-budget route; the grid ceiling | CONTRACT-LEVEL | throughout; §6.4, Remark 4.3, [G1] | yes |
| own code | `proofs/0023-prover-3-code/check_witnesses.py` | exact `Fraction` re-check of the two witness tables, the shattering-window minima and the $\Sigma$-payment (**one** minimum certificate per point only — see §7.4) | own computation | T5, T7, §7.1, §7.5 | corroborative |
| own code (new) | `proofs/0023-prover-3-r2-code/check_min_certificates.py` | exhaustive enumeration of **all** minimum certificates of **all** points on both sides, $k\le3$: sizes $=d$, multiplicities $1..k+1$, worst-selection ratios $\frac14,\frac16,\frac5{32}$, best-selection ratios $\frac14,\frac5{24},\frac{13}{64}$ | own computation, run 2026-08-27 | §7.4 (the U4 repair) | corroborative (the algebra of §7.4 is self-contained) |

Everything else is proved inline (T4(a) non-vanishing, T4(b) relevance
intersection, T4(c) quantum, Remark 4.2 forced coordinates, §5.4 group Fourier
and the even-order pullback, §7.2 automorphisms, §7.4 the certificate-size
minimisation).

## SOURCE REQUEST

None. This artifact needs no unread source; both [MEMORY] items are unused, and
every card and campaign artifact it cites is in the repository at the path given
above.

---

## CHANGELOG (each triage finding → what changed)

**U1 (class A, scope overclaim — highest priority).** Retitled: the title now
names the **two** sub-classes (relevance-denominated, own-heavy) and states that
the class as a whole is **not** capped. §5.3's R4 sentence was deleted and
replaced by the displayed **conditional** form (quantified over the two
sub-classes, over the two numerical ceilings, and over the object classes of R2,
R3, R4, R5, R6′, R6($\mathbb Z_2$)), followed by an explicit "**R4 is NOT
condemned**" paragraph naming the four uncapped members (including the
per-function case-split window). VERDICT 3 was rewritten to carry the same
conditional sentence verbatim and the same non-condemnation. VERDICT's opening
kept the triage-endorsed "refuted as a barrier for the whole window-payment
class" and now glosses it precisely so it cannot be read as a success claim.
D2 now says explicitly that the two properties are sub-classes, not a partition.

**U2 (class B, invalid empty-window branch; five "$V=0$" claims).** D5 no longer
defines $V_W$: it defines $\Theta_W$ only, with the *sound* degenerate convention
$\Theta_W:=0$ when $W\equiv\emptyset$ on **all** of $\mathcal P_d$ (there the
count concludes for no family — this branch is valid, and is the only zero clause
retained). New Remark 1.1 states the invalid inference, deletes it, gives the
quantitative reason ($\max\delta=1/4$ and $1/2$ at the two witnesses, above every
threshold at issue), and records the two candidate refinements as **[ESCALATED
E1]**, used by no cap. The five casualties: (i) D5's zero clause — replaced;
(ii) T6's "$V_W=0$ if $W(A_k)=W(B_k)=\emptyset$" — deleted, replaced by an
explicit nonemptiness hypothesis plus "this pair contributes no bound", with the
hypothesis discharged for (a),(b),(c); (iii) T8's "if also $W(C)=\emptyset$ …
$V_W=0$" — deleted; T8 now carries the hypothesis $W(C)\ne\emptyset$, and new
Remark 4.2$'$ discharges it for every own-heavy rule named
($W^\theta_{\mathrm{hvy}}(C)=W_{\mathrm{Forced}}(C)=[d]$); (iv) Remark 4.3's "for
$W_{\mathrm{Forced}}$ in fact $V=0$" — deleted and replaced by "**capped at
$\frac1{2(2^d-1)}$**" via witness (b), with a note that the address pair
contributes nothing for that functional; (v) §6.2's "over $\mathcal P_d$ one has
$V_{W_{\mathrm{Forced}}}=0$" — replaced by the cap. T2's and T3's proofs were
corrected in the same way (T2 now infimises over the nonempty-window pairs; T3
now states $\Theta_W\le\eta^*_W$ in general and $\Theta_W\le\eta^*$ for the
everywhere-nonempty windows, which are the only ones used). §8.1 and §8.3 carry
the matching qualifier. CAP I(a)–(c) and CAP II with $W(C)\ne\emptyset$ are
preserved with their constants unchanged.

**U3 (class B, "value $\ge$" is unproved).** VERDICT 1 no longer says "value
$\ge1/8$ / $>1/4$ / $\ge1/(2(d+1))$". It now says the caps' hypotheses fail at
both certified witnesses and that each witness contributes no cap below the
stated inverse-polynomial number, and adds explicitly that **no lower bound on
any $\Theta_W$ is claimed** and that
$\Theta_{W_{\mathrm{sh}}}\le\eta^*\in[2^{-d},1]$ is open. Two standing
disclaimers were added at the top of the VERDICT, and §7 opens with a "standing
reading" paragraph making the upper-bound direction explicit for every ratio in
the section. Every escape sentence in §7.1, §7.3, §7.4 was reworded to
"contributes no cap below …" / "hypotheses fail". §8.2 is now labelled **open**.
The section's object is unchanged (per the triage's overruling of the
"wrong-window" suggestion): $W_{\mathrm{sh}}$ is still *any maximum-degree
monomial support*, now with the half-line attribution to
`0023-strategist-2` §2 table V1.

**U4 (class B, minimum certificates are not unique).** §7.4 now (i) defines
*certificate*, *minimal* and *minimum*, and declares that P5's plan uses minimal
while §7.4 evaluates minimum-size selections; (ii) performs the
$k-u+2^u$ minimisation, so minimality **of size** is proved rather than assumed;
(iii) deletes "unique" and states the correct multiplicity ($1$ to $k+1$,
$x$-dependent), backed by a **new** exhaustive enumeration of *all* minimum
certificates of *all* points on both sides,
`proofs/0023-prover-3-r2-code/check_min_certificates.py` (the old script returned
one certificate per point, which is why the false claim survived it);
(iv) replaces the exact
payment identity by the **min-over-selections** bound
$\bigl[\frac{k-1}2+2^{1-k}\bigr]/(2(k+1))\ge\frac18$ for all $k\ge1$, with the
worst selection identified ($u=1$ on both sides) and the least value over $k$
recorded as $\frac5{32}$ at $k=3$; the printed $\frac14,\frac5{24},\frac{13}{64}$
survive, now scoped to the declared $u=0$ selection; (v) records the
witness-(b) multiplicity and that the payment there is selection-independent;
(vi) scopes §7.5's $\Sigma$-characterisation and the $\frac k4+4^{-k}$ average to
the $u=0$ selection, keeping the worst-case $2^{-k}$ and the "P5 must stay
averaged" warning. New **[G5]** flags the one thing the repair opened: an
unrestricted *minimal* selection can pick a size-$2^{d-1}$ certificate at witness
(a), so P5 must declare its selection rule.

**U5 (class B, non-load-bearing: grid-ceiling sentence).** §6.4 no longer says
both caps sit far below $\frac1{2d}$. It now prints the exact comparison
($(d+1)2^{-d-1}=\frac12,\frac38,\frac14,\frac5{32}$ vs
$\frac1{2d}=\frac12,\frac14,\frac16,\frac18$), states equality at $d=1$, strict
*excess* at $d=2,3,4$, first strict inequality at $d=5$, restricts CAP I's
comparison to $d\ge5$, keeps CAP II's for $d\ge2$, and notes the comparison is
used nowhere. The consequential direction (both caps above K1's $2^{-d}/d$) is
unchanged.

**U6 (class D, citation defect + incomplete register).** §7.1's "$\le d$ **by
theorem**, card S7b" is deleted; the size bound is now derived in one line from
the Contract's definition of degree. The S7b row states what the card actually
says (Thm 1.2 shattering / Cor. 3.4), records that §7.1 does **not** use it, and
is marked **non-load-bearing**. Every row now carries the file **path** and the
internal block id; added rows for S7 obstacle (ii), `0023-refuter-3` §5.1, §5.2
and §5.3 (previously only §4), `0023-strategist-2`, `PROGRESS.md` and
`I02-degree-d-sets.md`. Card block ids are cited with their filenames throughout
the body as well (`sources/S6-junta-degree-card.md`,
`sources/S7-changfang26-card.md`, `sources/S1-acc22-card.md`). §5.3 additionally
restates the rung classes inline so a blind reader never needs `PROGRESS.md`.

**U7 (class C, VERDICT 2 dropped three qualifiers).** VERDICT 2 now states:
$(d+1)2^{-d-1}$ is T6(a) at density $c=1$ and the density-$c$ ceiling is T6(b)'s
$\frac{d+1}{c2^{d+1}}$ (with T6(c) for relevance-independent exponential sizes);
CAP II requires the **strict** $\theta>\frac1{2(2^d-1)}$, hence "for all $d\ge
d_0(\theta)$" at $\theta=1/\mathrm{poly}(d)$; and the caps are bounds on
$\Theta_W$ **relative to the object class $\mathcal C^{\mathrm{ind}}_d$ and
larger** — with a pointer to §6.1 explaining that dropping the relativisation
would falsely condemn frozen R1. §6.1 says the same in one added sentence.

**U8 (class C, the (α)/(β) glosses).** Remark 4.5's (α) is now "a
sub-exponential — effectively $\mathrm{poly}(d)$ — window size on the address
family", with T6(c) cited to show a merely relevance-independent bound is not
enough; (β) is now the quantitative "$W(D)$ contains an $i$ with
$\mathrm{Inf}_i(f_D)\le\frac1{2(2^d-1)}$", i.e. failure of own-heaviness strictly
above that level. VERDICT 1's conjunction was rewritten to match. T9's "decisive
question" is now scoped: necessary and sufficient for **witness (b) only**, with
the explicit note that §8.1's $\eta^*$ ceiling binds regardless and CAP I bites
through a different mechanism.

**U9 (class C, undeclared scope hole: the mass-denominated route).** Named in
three places: VERDICT 2 (next to the existing hedge, with the conclusion that
I02's central question is **not closed in either direction**), Remark 4.3 (a
"mass-denominated reading, not covered" clause), and **[G1]**, where it is listed
among the non-members with the reason (D4(T3) admits only window sizes as the
denominator) and the note that only the *thresholded* reading is covered by
CAP II. D4 itself now states this exclusion.

**U10 (class C, own-heaviness strictness in §7.3).** "Neither relevance-denominated
nor own-heavy at level $\ge\frac1{2(2^d-1)}$" is replaced by the provable form:
$W_{\max}$ is **not own-heavy at any level strictly above $\frac1{2(2^d-1)}$**,
justified from T7 (witness (b)'s $D$ attains the level exactly), with the note
that the strict form is precisely what CAP II requires; and the
relevance-denomination clause is replaced by the quantitative density computation
$(d-1)/(2^{d-1}+d-1)=2^{-\Theta(d)}$.

**P1–P6 (pedantic, folded in while touching those lines).** P1: Remark 4.2(b) now
says $\mathrm{Forced}(D)=\emptyset$ **for $d\ge2$**, with the $d=1$ exception
named, and §6.2 carries the qualifier. P2: §7.5 now states
$\Sigma\subseteq T_A\cap T_B\subseteq W(A)\cap W(B)$ and hence
$\pi_\Sigma\le\pi_W$. P3: §5.4's even-order pullback now gives the argument
(injective dual map, measure-preserving $\varphi^N$, $\mathbb Z_2$ quotient iff
even order). P4: $W_{\max}(A):=\emptyset$ when $\mathrm{Rel}(A)=\emptyset$ is now
part of the definition, with the note that this never occurs on $\mathcal P_d$.
P5: Remark 4.4's bolded sentence now carries "inherited from `0023-refuter-3`
§5.2" inline. P6: §5.3 gives an explicit computable $d_0(c,\alpha)$ criterion.

**Preserved unchanged (confirmed by the five passes and re-derived in triage; not
touched):** T1, T2's non-empty case, T3's inequality, T4, T5, T7, T9's arithmetic,
CAP I's and CAP II's constants, both witness influence tables, the quantifier
order of T1 (each window a function of its own set, fixed before the functional
count), the scope direction of §5.2 (caps propagate up, provably not down),
Remark 4.4's insufficiency of "sum rather than $\min$", the substantive exclusion
of pair-dependent windows (Remark 2.1, [G1]), §7.2's non-canonicity theorem,
§8.4, §8.5's milestone, and the honest self-assessment (status PARTIAL, the class
model a stipulation, [G2]'s odd-order gap, [G3]'s non-claimed converse).

### END OF ARTIFACT 0023-prover-3-r2 ###
