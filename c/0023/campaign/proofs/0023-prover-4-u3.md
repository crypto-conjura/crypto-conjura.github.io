id: 0023-prover-4-u3
agent: prover
model: claude-opus-5[1m]
cycle: 4
status: COMPLETE

# The dichotomy (D) fails, and the monomial-only route is now closed at $\Theta(d\,2^{-d})$

Notation as in `0023-prover-4-u2`. Write $\pi_M(A,B):=\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)+\sum_{i\in M(A)}\mathrm{Inf}_i(f_B)$ for the **monomial payment**, the quantity Theorem L4 bounds; $\pi_\tau\ge\pi_M$.

**Summary.** (D) **fails**. In the family $\mathcal E_d$ of §3 *both* branches' hypotheses fail at once: neither side's max-degree slices are $1/\mathrm{poly}(d)$-dense, and neither side is a subcube, graph, or near-subcube. Moreover $\pi_M(\mathcal E_d)=d\,2^{1-d}$, so no argument using only $M(A),M(B)$ can certify more than $2^{-\Theta(d)}$. I also prove (§2) that $\pi_M\ge\frac{d_B}{2}2^{-d_B}+\frac{d_A}{2}2^{-d_A}$, which is tight within a factor $2$ on $\mathcal E_d$: the monomial sub-route is now closed from both sides. **But the route as a whole does not cap at exponential**: in $\mathcal E_d$ the true payment is $\pi_\tau\approx1$, carried by a coordinate *outside* $M(A)\cup M(B)$ that is heavy for both sides (§4). The correct dichotomy is on the window, not on the monomial.

## 1. Two slicewise ingredients

**Fact I (edge isoperimetry).** For $S\subseteq\{\pm1\}^m$ of density $s\in(0,1)$,
$\ \sum_{i\in[m]}\mathrm{Inf}_i(f_S)\ \ge\ \tfrac12\log_2(1/s)$.

*Proof.* Harper–Bernstein–Hart: $e(S)\le\frac12|S|\log_2|S|$ edges inside $S$, so the edge boundary is $\partial S=|S|m-2e(S)\ge|S|\log_2(2^m/|S|)$. With $\mathrm{Inf}_i(1_S)=\frac14\Pr_x[1_S(x)\ne1_S(x^{\oplus i})]$ we get $\sum_i\mathrm{Inf}_i(1_S)=\frac14\cdot\frac{2\partial S}{2^m}\ge\frac{s\log_2(1/s)}{2}$; divide by $s$. $\square$
(Tight: $S$ a codimension-$k$ subcube has $\sum_i\mathrm{Inf}_i(f_S)=k/2=\frac12\log_2(1/s)$.)

**Fact I′ (dense form).** $\mathrm{Inf}_i(1_S)=\mathrm{Inf}_i(1_{\bar S})$, so $\sum_i\mathrm{Inf}_i(f_S)=\frac{1-s}{s}\sum_i\mathrm{Inf}_i(f_{\bar S})\ \ge\ \frac{1-s}{s}\cdot\frac{\log_2\frac{1}{1-s}}{2}$.

**Fact II (singleton slices are maximally influential).** If $B_z$ is a singleton for every $z\in\{\pm1\}^{[N]\setminus M(B)}$ (i.e. $B$ is the graph of a map $\{\pm1\}^{\overline{M(B)}}\to\{\pm1\}^{M(B)}$), then $\mathrm{Inf}_j(f_B)=\tfrac12$ for **every** $j\in M(B)$.

*Proof.* For $j\in M(B)$, $x\in B\Rightarrow x^{\oplus j}\notin B$ (one point per fibre), so $\Pr[1_B(x)\ne1_B(x^{\oplus j})]=2\beta$, giving $\mathrm{Inf}_j(1_B)=\beta/2$. $\square$

Fact II **discharges GAP‑1**: Corollary 3 of u2 needed "$B$ is a subcube" only to know $\mathrm{Inf}_j(f_B)=1/2$ on $M(B)$; Fact II gives that for every graph set, with no structure theorem. (The fixed-point step producing $M(A)\cap M(B)\ne\emptyset$ is still only proved for subcubes — that remains GAP‑2.)

## 2. Theorem A: the sharp monomial bound

**Theorem A.** For every cross-disjoint pair, with $z$ over $\{\pm1\}^{[N]\setminus M(B)}$,
$$\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)\ \ge\ \mathbb E_{\mu_A}\!\big[g(a_z)\big]\ \ge\ \max\!\big(1,\tfrac{d_B}{2}\big)\,2^{-d_B},\qquad
g(a):=\max\Big(1-a,\ \tfrac{1-a}{a}\cdot\tfrac{\log_2\frac{1}{1-a}}{2}\Big),$$
where $\mu_A(z)\propto a_z$. Hence $\pi_\tau\ \ge\ \pi_M\ \ge\ \max(1,\tfrac{d_A}{2})2^{-d_A}+\max(1,\tfrac{d_B}{2})2^{-d_B}$.

*Proof.* Inside the slice cube $\{\pm1\}^{M(B)}$ (dimension $d_B$), Parseval gives $\sum_{i\in M(B)}\mathrm{Inf}_i(f_{A_z})\ge1-a_z$ (u2, Lemma 2) and Fact I′ gives $\sum_{i\in M(B)}\mathrm{Inf}_i(f_{A_z})\ge\frac{1-a_z}{a_z}\cdot\frac{\log_2\frac1{1-a_z}}{2}$; so the slice sum is $\ge g(a_z)$. Lemma 0 of u2 is an identity, so averaging loses nothing:
$\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)=\mathbb E_z[a_z\sum_{i}\mathrm{Inf}_i(f_{A_z})]/\alpha\ge\mathbb E_z[a_zg(a_z)]/\alpha=\mathbb E_{\mu_A}[g(a_z)]$.
By Lemma 1 of u2 plus $A_z\cap B_z=\emptyset$ we have $c:=1-a_z\ge b_z\ge2^{-d_B}$ for every $z$. Now $g\ge c\max(1,\frac{\log_2(1/c)}{2})$, and $c\mapsto c\log_2(1/c)$ increases on $(0,1/e)$ while $c\max(1,\cdot)\ge c\ge\frac14$ for $c\ge\frac14$; so the minimum over $c\in[2^{-d_B},1]$ is attained at $c=2^{-d_B}$, with value $\max(1,\frac{d_B}{2})2^{-d_B}$. Exchange $A,B$ for the second term. $\square$

This gains a factor $d/2$ on Theorem L4 and, crucially, **handles mixtures**: the bound is a pointwise bound on $g(a_z)$ averaged under $\mu_A$, so sparse-but-structured and dense slices may be freely interleaved; nothing assumes the slices behave alike. §3 shows the constant cannot be improved beyond a factor $2$.

## 3. The family $\mathcal E_d$: (D) is false

Let $N\ge d+1$, $K=\{1,\dots,d\}$, $t=d+1$, $u=(+1,\dots,+1)$, $v=(-1,+1,\dots,+1)\in\{\pm1\}^K$, and
$$A:=\{x:x_t=+1,\ x_K\ne u\}\ \cup\ \{x:x_t=-1,\ x_K=v\},\qquad B:=\overline A .$$

**Disjointness/nonemptiness.** $B=\bar A$ and $0<|A|<2^N$. ✓

**Degrees.** With $\Pi_w=\prod_{i\in K}\frac{1+w_ix_i}{2}=2^{-d}\sum_{T\subseteq K}w_Tx_T$ and $u_T\equiv1$, $v_T=(-1)^{[1\in T]}$:
$$1_A=\tfrac{1+x_t}{2}\big(1-\Pi_u\big)+\tfrac{1-x_t}{2}\Pi_v
=\tfrac{1+x_t}{2}-2^{-d}\!\!\sum_{T\ni 1}x_T-2^{-d}\!\!\sum_{T\subseteq K\setminus\{1\}}\!\!x_Tx_t .$$
(The bracket multiplying $x_T$ is $\frac{v_T-1}{2}-x_t\frac{1+v_T}{2}$, which is $-1$ when $1\in T$ and $-x_t$ otherwise.) Every monomial has degree $\le d$, and degree $d$ is attained by $x_K$ (coefficient $-2^{-d}$) and by $x_{K\setminus\{1\}}x_t$ (coefficient $-2^{-d}$). So $\deg1_A=d$ and $K$ is a legitimate choice of $M(A)$. Since $1_B=1-1_A$, likewise $\deg 1_B=d$ and $M(B)=K$ is legitimate. ✓

**Densities.** $\alpha=\frac12(1-2^{-d})+\frac12 2^{-d}=\frac12=\beta$. ✓

**Slice densities over $K$.** For $z\in\{\pm1\}^{[N]\setminus K}$: $a_z=1-2^{-d}$ if $z_t=+1$, $a_z=2^{-d}$ if $z_t=-1$; $b_z=1-a_z$. So **on each side the max-degree slice densities take the value $2^{-d}$ on half the fibres**: $\mathbf H_\gamma$ fails for every $\gamma>2^{-d}$, on both sides simultaneously. ✓

**Influences.** $\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(f_B)$ (complements, equal densities). For $i\in K$: conditioned on either value of $x_t$, membership flips iff exactly one of $x_K,x_K^{\oplus i}$ hits the single distinguished point, probability $2^{1-d}$; so $\mathrm{Inf}_i(f_A)=\frac12\cdot2^{1-d}=2^{-d}$. For $i=t$: membership agrees exactly when $x_K\in\{u,v\}$, so $\mathrm{Inf}_t(f_A)=\frac12(1-2^{1-d})$. All other coordinates are irrelevant. ✓

**Theorem B.** For $\mathcal E_d$ with $M(A)=M(B)=K$: $\ \pi_M=2\,d\,2^{-d}=d\,2^{1-d}$.

So Theorem A ($\ge d\,2^{-d}$ here) is tight within a factor $2$, and:

> **No bound derived from $M(A)$ and $M(B)$ alone can exceed $O(d\,2^{-d})$.** The monomial sub-route is closed.

**Why (D) is refuted.** In $\mathcal E_d$: branch 1 fails ($\gamma\le 2^{-d}$); and branch 2 has nothing to bite on — $A$ and $B$ are neither subcubes, nor graphs (Fact II does not apply: $b_z=1-2^{-d}$ on half the fibres), nor near-subcubes; each is a *union* of a co-singleton cylinder and a singleton cylinder. Both alternatives of (D) are false of the same pair.

## 4. What the second branch must say

$\mathcal E_d$ is **not** a counterexample to the rung. Its true payment is large: $t$ is heavy for *both* sides, $\mathrm{Inf}_t(f_A)=\mathrm{Inf}_t(f_B)=\frac12(1-2^{1-d})$, so for any $\tau\le\frac12(1-2^{1-d})$ — in particular any $\tau=1/\mathrm{poly}(d)$ with $d\ge17$ — we have $t\in W_\tau(A)\cap W_\tau(B)$ and
$$\pi_\tau(\mathcal E_d)\ \ge\ \mathrm{Inf}_t(f_A)+\mathrm{Inf}_t(f_B)=1-2^{1-d}.$$
(Equivalently: $t$ lies in the *other* maximum-degree monomial $x_{K\setminus\{1\}}x_t$, so a version of the route that puts every maximum-degree support into the window also pays. Within this family that is forced: the max-degree supports are $K$ and $(K\setminus\{j\})\cup\{t\}$ for $j$ in the disagreement set of $u,v$, which is nonempty.)

**Rigidity lemma (what "$\pi_M$ small" forces).** If $\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)\le\epsilon$ then $\mathbb E_{\mu_A}[1-a_z]\le\epsilon$, so with $R:=\{z:a_z\ge1-\sqrt\epsilon\}$ and $\rho=\Pr[R]$: $A$ carries $\ge(1-\sqrt\epsilon)$ of its mass on $R$, $(1-\sqrt\epsilon)\rho\le\alpha\le\rho+\sqrt\epsilon\,\alpha$, and $\beta\le\sqrt\epsilon\rho+(1-\rho)$. Symmetrically $B$ concentrates on a cylinder $R'\subseteq\{\pm1\}^{\overline{M(A)}}$ with $\Pr[R']\approx\beta$. These are mutually consistent (no contradiction is available from densities — $\mathcal E_d$ realises them with $\rho=\rho'=\frac12$), and they say exactly this:

> **The second branch must be:** when $\pi_M$ is exponentially small, both sets are, up to $\sqrt{\pi_M}$, co-sparse parts of cylinders over *complementary* base sets $R,R'$ living off the monomials; the payment is then carried by $\mathrm{Inf}$ mass on the **boundary coordinates of $R$**, which lie outside $M(A)\cup M(B)$ and are heavy for $A$ and $B$ simultaneously (in $\mathcal E_d$, $R=\{z_t=1\}$, boundary coordinate $t$).

This does not contradict the calibration note: the subcube-versus-complement witness has $\pi_M\ge\frac12$, so it never enters this branch. A proof of the rung along these lines needs: *from the cylinder structure, extract a coordinate $i^\ast$ with $\mathrm{Inf}_{i^\ast}(f_A)\ge1/\mathrm{poly}(d)$ and $\mathrm{Inf}_{i^\ast}(f_B)\ge\tau$* (or vice versa). **[GAP-3]** — not proved here; it is the whole remaining content, and it is now correctly localised.

## GAP REGISTER

- **No gap** in Facts I, I′, II, Theorem A, or the verification of $\mathcal E_d$ (degrees, disjointness, densities, influences are computed from the definitions above).
- **GAP‑1 of u2 is discharged** by Fact II (for the purpose it was needed).
- **GAP‑2 of u2 stands**: $M(A)\cap M(B)\ne\emptyset$ is proved only for subcube $B$.
- **[GAP-3]** The second branch (§4) is identified and its hypotheses are proved (rigidity lemma), but the extraction of a coordinate heavy on one side and windowed on the other is not proved.
- **Scope caveat.** Theorem B refutes the $M$-only route under the reading of u2 in which $M(\cdot)$ is *a* maximum-degree support. If the window is defined to contain *all* maximum-degree supports, $\mathcal E_d$ is not a counterexample to that variant — but Theorem A's tightness still shows any bound proved from one such support alone caps at $O(d2^{-d})$.

### END OF ARTIFACT 0023-prover-4-u3 ###
