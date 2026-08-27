id: 0023-refuter-8
agent: refuter
model: claude-opus-5[1m]
cycle: 4
status: COMPLETE

# VERDICT: **GAP-3 REFUTED IN BRANCH**

The branch restriction *does* exclude the literal certified witness — u3 is right about that — but the exclusion is not robust. A one-parameter deformation of the witness satisfies every hypothesis u3 states for branch 2 and drives $\max_i\min(\mathrm{Inf}_i(f_A),\mathrm{Inf}_i(f_B))$ to $2^{-\Theta(d)}$. **The localisation in §4 of `0023-prover-4-u3` is wrong as stated**; §5 below gives the missing hypothesis.

Notation as in the assignment; $Q(A,B):=\max_i\min(\mathrm{Inf}_i(f_A),\mathrm{Inf}_i(f_B))$, $\tau=1/(2d^4)$ ($c=1$). Code: `0023-refuter-8-code/` (`lib8.py`, `fam8.py`, `h1`–`h6`, `.out` files). All arithmetic exact (`Fraction` + integer fast Walsh–Hadamard). *`HARNESS.md` is not present in this repository; §3.4/§2 were taken from the launch brief.*

## 1. Baselines (exact, `h1.out`)

| pair | $Q$ | $\pi_M$ | in branch 2? |
|---|---|---|---|
| **W**: $A=$ codim-$d$ subcube, $B=\bar A$ | $\dfrac{1}{2(2^d-1)}$ | $\dfrac d2+\dfrac{d}{2(2^d-1)}\ \ge\ \tfrac12$ | **no** |
| $\mathcal E_d$ | $\tfrac12(1-2^{1-d})$ | $d\,2^{1-d}$ (min over the two max-degree supports) | yes |

Closed forms asserted against exhaustive brute force for $2\le d\le10$, tabulated to $d=12$. So u3's calibration note is confirmed: **W** has $\pi_M\ge1/2$ and never enters branch 2. $\mathcal E_d$ enters and satisfies GAP-3 with room to spare.

## 2. What flagged the falsity (the derived consequence)

For any complementary pair, $\mathrm{Inf}_i(f_B)=\tfrac{\alpha}{1-\alpha}\mathrm{Inf}_i(f_A)$, and $\sum_i\mathrm{Inf}_i(f_A)\le d$. Hence
$$Q(A,\bar A)\ \le\ \max_i\mathrm{Inf}_i(f_B)\ \le\ \frac{\alpha d}{1-\alpha}.$$
So **every** complementary pair of density $2^{-\Theta(d)}$ has $Q=2^{-\Theta(d)}$ for free; GAP-3 therefore asserts that no sparse degree-$d$ set reaches branch 2 — a claim about $\pi_M$ alone, which Theorem A's floor $\max(1,\tfrac{d_B}{2})2^{-d_B}$ does not support.

## 3. The deformation (proved by hand; verified on 7004 exact instances, `h6.out`)

**Deformation Lemma.** Let $Z,K$ be disjoint, $|K|=d$. Let $R\subseteq\{\pm1\}^Z$ be *any* nonempty set of density $\rho$ with $\deg 1_R=d_R$. Pick $1\le w\le d-1-d_R$, $K_1\subseteq K$ with $|K_1|=w$, and set
$$U=\{x_K: x_{K_1}\ne(+1)^w\},\qquad T=\{x_K=(+1)^d\},\qquad A=(R\times U)\ \sqcup\ (\{\pm1\}^Z\times T),\quad B=\bar A .$$
Then $1_A=1_R1_U+1_T$; since $\deg(1_R1_U)\le d_R+w\le d-1$ and $\deg 1_T=d$, **$x_K$ is the unique degree-$d$ monomial**, so $M(A)=M(B)=K$ is forced (no choice of supports exists). With $t=2^{-d}$, $u=1-2^{-w}$:
$$\alpha=\rho u+t;\quad \mathrm{Inf}_i(1_A)=u\,\mathrm{Inf}_i(1_R)\ (i\in Z),\ \ \rho2^{-w-1}+(1-2\rho)2^{-d-1}\ (i\in K_1),\ \ 2^{-d-1}\ (i\in K\setminus K_1),$$
$$Q=\frac{\max_i\mathrm{Inf}_i(1_A)}{\max(\alpha,\beta)},\qquad \pi_M=\Big(\sum_{i\in K}\mathrm{Inf}_i(1_A)\Big)\Big(\tfrac1\alpha+\tfrac1\beta\Big).$$

**The mechanism.** $T$ is a *degree booster*: a codimension-$d$ subcube of measure $2^{-d}$ that fixes the degree at $d$ and supplies the unique top monomial, while contributing influence $O(2^{-d})$. $A$ is otherwise the cylinder $R\times\{\pm1\}^K$, whose heavy coordinates lie in $Z$ — disjoint from $M(A)=K$. Exactly what **W** cannot do: for **W** the top monomial *is* the heavy set.

**Instances.** V1: $R=$ codim-$k$ subcube, $w=d-k-1$, $N=k+d$. V2: $R=R_1\cup R_2$ on disjoint blocks of size $k$, $w=d-2k-1$, $N=2k+d$.

**Certificates (`h5.out`).**

| | $N$ | $\rho=\alpha$ | $\pi_M$ | $Q=\max_i\mathrm{Inf}_i(f_B)$ | $\tau$ |
|---|---|---|---|---|---|
| **C1** V1, $d{=}80,k{=}36$ | 116 | $1.46\cdot10^{-11}$ | $4.72\cdot10^{-12}$ | $7.28\cdot10^{-12}$ | $1.22\cdot10^{-8}$ |
| **C2** V2, $d{=}120,k{=}34$ | 188 | $1.16\cdot10^{-10}$ | $1.13\cdot10^{-14}$ | $2.91\cdot10^{-11}$ | $2.41\cdot10^{-9}$ |

Both clauses of GAP-3 require some $i^\ast$ with $\mathrm{Inf}_{i^\ast}(f_B)\ge\tau$; but $\max_i\mathrm{Inf}_i(f_B)<\tau$, so $W_\tau(B)=\emptyset$ and **GAP-3 fails outright** (also $\pi_\tau\le N\max_i\mathrm{Inf}_i(f_B)<6\cdot10^{-9}$). Asymptotically $\max(\pi_M,Q)=2^{-d/2+O(\log d)}$ (V1) — beating *every* inverse polynomial. Crossovers: V1 first beats $1/(2d^4)$ at $d=53$, and $1/d^{10}$ at $d=152$; V2 at $d=84$ and $d=244$.

The pairs sit in branch 2 by *every* criterion u3 offers: $\pi_M$ exponentially small; rigidity satisfied ($1-\Pr_A[R\times\text{cube}]$ and $1-\Pr_B[\bar R\times\text{cube}]$ both $\ll\sqrt{\pi_M}$); max-degree slice profile $\{\approx1$ on a $\rho$-fraction, $2^{-d}$ elsewhere$\}$ on both sides — the same shape as $\mathcal E_d$, so branch 1 ($\mathbf H_\gamma$) fails identically; not a graph (Fact II inapplicable). V1's $A$ *is* a near-subcube (relative distance $3\cdot2^{k-d}$), so **C2/V2 is the load-bearing witness**: its $A$ is at relative distance $\approx\tfrac12$ from every subcube (exactly $53/86$, $7/15$, $10/19$, … at small $d$, `h5.out`).

## 4. Verification (three exact routes, `h2`,`h3`,`h6`)

(a) boundary route $\mathrm{Inf}_i(f_A)=b_i(A)/(2|A|)$; (b) integer FWHT Fourier route $\sum_{S\ni i}c_S^2/(2^N|A|)$, which also yields the degree and *all* max-degree supports; (c) the hand-derived Lemma. `lib8.card` asserts (a)$=$(b) on every pair. (c) matched (a)+(b) on **7004** instances: all 255 base sets $R\subseteq\{\pm1\}^3$ and 400 random $R\subseteq\{\pm1\}^4$, crossed with every admissible $(d,w)$ up to $N\le12$; plus the 28 named V1/V2 instances, $4\le d\le9$.

## 5. The obstruction, and the repair

$\mathcal E_d$ pays because its cylinder base is **balanced**: $\rho=\tfrac12$, so the boundary coordinate $t$ of $R$ has $\mathrm{Inf}_t\approx\tfrac12$ for *both* sides. The deformation keeps everything else and only moves $\rho$ to $2^{-\Theta(d)}$; then the boundary coordinates of $R$ are heavy for $A$ ($\approx\tfrac12$, resp. $\tfrac14$) and carry only $\approx\rho/2$ for $B$. u3's rigidity lemma pins $\rho\approx\alpha$ but leaves $\alpha$ free — that is the hole.

> **Repair.** Branch 2 must carry the extra hypothesis $\min(\alpha,\beta)\ge1/\mathrm{poly}(d)$ (equivalently $\rho,1-\rho\ge1/\mathrm{poly}(d)$). Under it the payment reduces to: *every degree-$\le d$ set of density in $[1/\mathrm{poly}(d),1-1/\mathrm{poly}(d)]$ has a coordinate of influence $\ge1/\mathrm{poly}(d)$.* I neither prove nor cite this; it is an Aaronson–Ambainis-type max-influence statement and must be treated as unresolved. **Sparse pairs are now known to be outside every branch of the route** — they need a separate argument, and W plus C1/C2 show the window payment there is genuinely $2^{-\Theta(d)}$.

## 6. Search space covered, and what it does not settle

Exhaustive, exact, over **every** cross-disjoint pair of nonempty sets at $N=3$ (6 050 pairs) and $N=4$ (42 915 650 pairs), `h4.out`: $\min\max(\pi_M,Q)=1,1,3/4,27/28$ at $d=1,2,3,4$. **Null result, ruling out nothing:** the deformation needs $2^{-d}\ll\rho\ll1$, impossible for $d\le4$; the family drops below $\tau$ only at $d\ge53$. The refutation rests on the Lemma evaluated in exact rationals at $d=80,120$, not on small-$d$ extrapolation. Not covered: non-complementary pairs at large $d$; groups $\ne\mathbb Z_2$; whether §5's repaired branch is true.

### END OF ARTIFACT 0023-refuter-8 ###
