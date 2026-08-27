id: 0023-prover-4-u2
agent: prover
model: claude-opus-5[1m]
cycle: 4
status: PARTIAL

# L4: a lower bound on the τ-window payment

Throughout, $(A,B)$ is cross-disjoint: $A,B\subseteq\{\pm1\}^N$ nonempty, disjoint,
$\deg 1_A=:d_A\le d$, $\deg 1_B=:d_B\le d$. Note $d_A,d_B\ge 1$: if $d_A=0$ then $A$
is $\emptyset$ or the whole cube, and the whole cube forces $B=\emptyset$. Hence
$M(A),M(B)\neq\emptyset$, $|M(A)|=d_A$, $|M(B)|=d_B$.

For $Z\subseteq[N]$ and $z\in\{\pm1\}^{[N]\setminus Z}$ write $A_z:=\{y\in\{\pm1\}^Z:(y,z)\in A\}$,
$a_z:=|A_z|/2^{|Z|}$, and likewise $B_z,b_z$; the ambient $Z$ is always named.

## Statement proved

**Theorem L4.** Let $z$ range over $\{\pm1\}^{[N]\setminus M(B)}$ (slices in the cube $\{\pm1\}^{M(B)}$)
and $z'$ over $\{\pm1\}^{[N]\setminus M(A)}$. Then
$$\pi_\tau(A,B)\;\ge\;\frac{\mathbb E_z[a_zb_z]}{\alpha}+\frac{\mathbb E_{z'}[a_{z'}b_{z'}]}{\beta}
\;\ge\;2^{-d_B}+2^{-d_A}\;\ge\;2^{1-d}.$$
The bound uses no property of $\tau$, so it holds for every threshold; in particular the payment
is never $0$, and the *monomial* part $M(A)\cup M(B)$ of the windows already pays for it.

So the honest constant is $p=2^{-d_A}+2^{-d_B}$: **exponential in $d$, not $1/\mathrm{poly}(d)$.**
Corollaries 2 and 3 below give $p=\Omega(1/\mathrm{poly}(d))$ and $p\ge 1/2$ under declared extra
hypotheses that isolate exactly the remaining case.

## Proof

**Lemma 0 (restriction identity; this verifies (N1)).**
Let $Z\subseteq[N]$, $i\in Z$, and let $z$ range over $\{\pm1\}^{[N]\setminus Z}$. Then
$\mathrm{Inf}_i(1_A)=\mathbb E_z\!\left[\mathrm{Inf}_i(1_{A_z})\right]$ and consequently
$$\mathrm{Inf}_i(f_A)=\frac{\mathbb E_z\!\left[a_z\,\mathrm{Inf}_i(f_{A_z})\right]}{\alpha}.$$

*Proof.* For a $\{0,1\}$-valued $g$, $\mathrm{Inf}_i(g)=\sum_{S\ni i}\hat g(S)^2=\tfrac14\mathbb E_x[(g(x)-g(x^{\oplus i}))^2]
=\tfrac14\Pr_x[g(x)\neq g(x^{\oplus i})]$. Writing $x=(y,z)$ with $y\in\{\pm1\}^Z$ and noting that for
$i\in Z$ the flip $x\mapsto x^{\oplus i}$ acts only on $y$,
$\tfrac14\Pr_{y,z}[1_A(y,z)\neq 1_A(y^{\oplus i},z)]=\mathbb E_z\big[\tfrac14\Pr_y[1_{A_z}(y)\neq 1_{A_z}(y^{\oplus i})]\big]
=\mathbb E_z[\mathrm{Inf}_i(1_{A_z})]$. Divide by $\alpha=\mathbb E_z[a_z]$ and use
$\mathrm{Inf}_i(1_{A_z})=a_z\mathrm{Inf}_i(f_{A_z})$ (with the convention that the term is $0$ when $a_z=0$). $\square$

So (N1) is correct as stated by the orchestrator, for any window, not just $W_\tau(A)\cup W_\tau(B)$.

**Lemma 1 (top-monomial surjectivity; the core of (L2), for the window $M(B)$ alone).**
For **every** $z\in\{\pm1\}^{[N]\setminus M(B)}$ the slice function $1_{B_z}:\{\pm1\}^{M(B)}\to\{0,1\}$ is
nonconstant; hence $B_z\neq\emptyset$ and $B_z\neq\{\pm1\}^{M(B)}$, so
$$2^{-d_B}\;\le\;b_z\;\le\;1-2^{-d_B}.$$

*Proof.* Expand $1_B=\sum_S\widehat{1_B}(S)\chi_S$ and restrict: for $T\subseteq M(B)$ the coefficient of
$\chi_T$ in $1_{B_z}$ is $\sum_{S:\,S\cap M(B)=T}\widehat{1_B}(S)\chi_{S\setminus M(B)}(z)$. For $T=M(B)$ the
sum runs over $S\supseteq M(B)$; since $|M(B)|=d_B=\deg 1_B$, the only such $S$ with $\widehat{1_B}(S)\neq0$
is $S=M(B)$ itself. So the top coefficient of $1_{B_z}$ equals $\widehat{1_B}(M(B))\neq0$ for every $z$,
and $1_{B_z}$ is nonconstant. A nonempty subset of the $d_B$-dimensional cube has density $\ge2^{-d_B}$;
a non-full one has density $\le 1-2^{-d_B}$. $\square$

**Lemma 2 (one-sided payment).** With $z$ over $\{\pm1\}^{[N]\setminus M(B)}$,
$$\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)\;\ge\;\frac{\mathbb E_z[a_z(1-a_z)]}{\alpha}\;\ge\;\frac{\mathbb E_z[a_zb_z]}{\alpha}\;\ge\;2^{-d_B}.$$

*Proof.* Fix $z$ with $a_z>0$ and normalise inside the slice cube $\{\pm1\}^{M(B)}$:
$f_{A_z}=1_{A_z}/\sqrt{a_z}$ has $\widehat{f_{A_z}}(\emptyset)=\sqrt{a_z}$ and unit $\ell_2$ norm, so by Parseval
$$\sum_{i\in M(B)}\mathrm{Inf}_i(f_{A_z})\;\ge\;\sum_{\emptyset\neq S\subseteq M(B)}\widehat{f_{A_z}}(S)^2\;=\;1-a_z .$$
(This is (L3) applied inside the slice.) Now $A_z$ and $B_z$ are disjoint subsets of the *same* slice cube
$\{\pm1\}^{M(B)}$, because they are slices of the disjoint sets $A,B$ at the same $z$. Hence
$1-a_z\ge b_z$, and $b_z\ge2^{-d_B}$ by Lemma 1 — *for every $z$*, with no exceptional set.
Summing Lemma 0 over $i\in M(B)$,
$$\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)=\frac{\mathbb E_z\big[a_z\sum_{i\in M(B)}\mathrm{Inf}_i(f_{A_z})\big]}{\alpha}
\ge\frac{\mathbb E_z[a_z(1-a_z)]}{\alpha}\ge\frac{\mathbb E_z[a_zb_z]}{\alpha}\ge 2^{-d_B}\frac{\mathbb E_z[a_z]}{\alpha}=2^{-d_B}. \square$$

**Proof of Theorem L4.** All summands of $\pi_\tau$ are nonnegative and $M(B)\subseteq W_\tau(B)$,
$M(A)\subseteq W_\tau(A)$ by definition of the windows, so
$$\pi_\tau(A,B)\;\ge\;\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)\;+\;\sum_{i\in M(A)}\mathrm{Inf}_i(f_B),$$
and Lemma 2, applied to $(A,B)$ and then with the roles of $A,B$ exchanged (using the window $M(A)$
and $\deg1_A=|M(A)|$), bounds the two terms by $2^{-d_B}$ and $2^{-d_A}$. $\square$

Note the payment stays a *sum over both sides*: Lemma 2 never asks for a single coordinate heavy for
both, so the codimension-$d$-subcube-versus-complement witness is not violated (there $d_B$-side pays
$\approx d\,2^{-d-1}$ and the $A$-side pays $d/2$).

## Corollaries

**Corollary 1 (small degree).** $\pi_\tau\ge 2^{-d_A}+2^{-d_B}$, so $\pi_\tau\ge1$ when $d_A=d_B=1$ and
$\pi_\tau\ge2^{-k+1}$ whenever both degrees are $\le k$. Independently, if
$W_\tau(A)=\mathrm{Rel}(A)$ and $W_\tau(B)=\mathrm{Rel}(B)$ — which by (F4) holds whenever
$\tau\le 2^{-1-d}/\max(\alpha,\beta)$, in particular for all $d\le16$ — then $\pi_\tau=\pi_{\mathrm{Rel}}\ge1$ by (F6).

**Corollary 2 (non-degenerate slices $\Rightarrow$ $1/\mathrm{poly}(d)$).** Declare hypothesis
$$\mathbf{H}_\gamma:\qquad b_z\ge\gamma\ \text{ for all } z\in\{\pm1\}^{[N]\setminus M(B)}\ \text{with } a_z>0,
\quad\text{and symmetrically } a_{z'}\ge\gamma .$$
Then $\pi_\tau\ge2\gamma$. In particular $\mathbf H_{1/\mathrm{poly}(d)}$ gives $p=\Omega(1/\mathrm{poly}(d))$, which
suffices for the rung. $\mathbf H_\gamma$ fails only when one side's max-degree slices are
*maximally degenerate*: $b_z\approx2^{-d_B}$, i.e. $B$ meets the $M(B)$-cube in (essentially) one point
above the relevant $z$'s.

**Corollary 3 (the degenerate side is captured when it is a subcube).** Suppose $B$ is a subcube of
codimension $d_B$, $B=\{x:x_C=c\}$ with $|C|=d_B$ (so $\beta=2^{-d_B}$, $M(B)=C$, $\mathrm{Inf}_i(f_B)=1/2$
for $i\in C$). Then $M(A)\cap C\neq\emptyset$ and hence $\pi_\tau\ge1/2$.

*Proof.* If $M(A)\cap C=\emptyset$, then $C\subseteq[N]\setminus M(A)$, so we may choose
$z'\in\{\pm1\}^{[N]\setminus M(A)}$ with $z'_C=c$. By Lemma 1 applied to $A$ (window $M(A)$), the slice
$A_{z'}$ is nonempty; any $x\in A$ above $z'$ has $x_C=c$, i.e. $x\in A\cap B$ — contradiction. Then
$\pi_\tau\ge\sum_{i\in M(A)\cap C}\mathrm{Inf}_i(f_B)\ge1/2$. $\square$

The same argument covers any $B$ whose $M(B)$-slices are singletons *not depending on the coordinates
of $M(A)\setminus M(B)$*; a fixed-point obstruction is all that blocks the general singleton case.

## GAP REGISTER

- **No gap in Theorem L4, Lemmas 0–2, or Corollaries 1–3 as stated.** Lemma 1 is proved here rather
  than imported, so the theorem depends only on Parseval, disjointness, and the definition of $M(\cdot)$.
- **[SHORTFALL, not a gap]** The unconditional constant is $p=2^{-d_A}+2^{-d_B}\ge2^{1-d}$,
  exponentially small, *below* the $\Omega(1/\mathrm{poly}(d))$ target. The loss is entirely in
  $b_z\ge2^{-d_B}$ (Lemma 1): everything else is an identity or Parseval. Closing to $1/\mathrm{poly}(d)$
  needs exactly $\mathbf H_\gamma$ of Corollary 2 with $\gamma=1/\mathrm{poly}(d)$, or a structure theorem
  for the complementary "rigid slice" case.
- **[GAP-1]** *Not used in any claim above, recorded because it is the natural bridge to Corollary 3.*
  The folklore fact "a degree-$d$ Boolean set of density exactly $2^{-d}$ is a codimension-$d$ subcube"
  is **unverified here**. Corollary 3 is therefore stated with "$B$ is a subcube" as a hypothesis, not
  derived from $\beta=2^{-d_B}$. Anyone using GAP-1 to discharge that hypothesis must verify it first.
- **[GAP-2]** The generalisation after Corollary 3 (singleton slices depending on $M(A)\setminus M(B)$)
  is **not proved**; it is flagged as the open fixed-point obstruction and used nowhere.
- (F6), (F1), (F4), (L1) are cited only in Corollary 1 and the remarks; the main line uses none of them.

### END OF ARTIFACT 0023-prover-4-u2 ###
