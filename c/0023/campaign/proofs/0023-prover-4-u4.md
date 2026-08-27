id: 0023-prover-4-u4
agent: prover
model: claude-opus-5[1m]
cycle: 4
status: PARTIAL

# [GAP-3]: the branch does exclude the witness, but $\pi_\tau\ge\pi_M$ is false, and the exact branch is empty

Notation as in `0023-prover-4-u3` (its `u2` predecessor is absent from the repo; all definitions used below are restated). $f_A:=1_A/\sqrt\alpha$, $\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(1_A)/\alpha$; $M(A)$ is *a* maximum-degree monomial support of $1_A$, $d_A:=|M(A)|=\deg 1_A$, $\theta_A:=\widehat{1_A}(M(A))\ne0$; $W_\tau(A):=\{i:\mathrm{Inf}_i(f_A)\ge\tau\}$, $\tau=c/(2d^4)$;
$\pi_M:=\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)+\sum_{i\in M(A)}\mathrm{Inf}_i(f_B)$, $\ \pi_\tau$ the same with $W_\tau$ in place of $M$. Write $\varepsilon_A,\varepsilon_B$ for the two summands of $\pi_M$.

**Verdict.** (i) The branch **does** genuinely exclude the certified witness: $\pi_M=\tfrac d2+d\,2^{-d-1}/(1-2^{-d})\ge d/2$, verified below from the definitions, and the exclusion survives the natural attempts to hide the witness behind decoy monomials. (ii) But u3's opening assertion **$\pi_\tau\ge\pi_M$ is FALSE**, and the certified witness refutes it: there $\pi_\tau\approx d2^{-d-1}$ while $\pi_M\approx d/2$. So branch 1 pays nothing, and the dichotomy as a whole does not close the rung even if [GAP-3] is proved. (iii) [GAP-3] is **true vacuously at $\varepsilon=0$** (Theorem C: the exact branch is empty), and I show this cannot be robustified past $2^{-\Theta(d)}$; for $\varepsilon=2^{-\Theta(d)}$ it is **open**, and I identify the exact extra hypothesis it needs.

## 1. The mandated check: does the branch exclude the certified witness?

Witness $\mathcal W_d$: $A=\{x\in\{\pm1\}^N:x_1=\dots=x_d=+1\}$, $B=\bar A$.

* $1_A=\prod_{i\le d}\frac{1+x_i}{2}=2^{-d}\sum_{S\subseteq[d]}x_S$. So $\deg 1_A=d$ and $[d]$ is the **unique** maximum-degree support: $M(A)=[d]$, $\theta_A=2^{-d}$. Since $1_B=1-1_A$, also $\deg1_B=d$, $M(B)=[d]$, $\theta_B=-2^{-d}$. $\alpha=2^{-d}$, $\beta=1-2^{-d}$.
* For $i\le d$: $x\in A\Rightarrow x^{\oplus i}\notin A$, so $\Pr[1_A(x)\ne1_A(x^{\oplus i})]=2\alpha=2^{1-d}$ and $\mathrm{Inf}_i(1_A)=\mathrm{Inf}_i(1_B)=2^{-d-1}$. Hence $\mathrm{Inf}_i(f_A)=\tfrac12$ and $\mathrm{Inf}_i(f_B)=2^{-d-1}/(1-2^{-d})$. Coordinates $i>d$ are irrelevant.
* Therefore $\displaystyle\pi_M(\mathcal W_d)=\underbrace{\textstyle\sum_{i\in M(B)}\mathrm{Inf}_i(f_A)}_{=d/2}+\underbrace{\textstyle\sum_{i\in M(A)}\mathrm{Inf}_i(f_B)}_{=d\,2^{-d-1}/(1-2^{-d})}\ \ge\ \tfrac d2 .$

Branch 2 is entered only when $\pi_M<1/\mathrm{poly}(d)$; $d/2\ge 1/\mathrm{poly}(d)$ for all $d\ge1$. **The exclusion holds, with room $d/2$, and it is not an accident of the choice of $M$: here $M(A)=M(B)=[d]$ is forced.** u3's assertion is correct. (Calibration check: $\min_i\mathrm{Inf}_i$ over $\mathcal W_d$ is $2^{-d-1}/(1-2^{-d})$, which drops below $\tau=c/(2d^4)$ exactly from $d=17$ on when $c=1$ — the stated threshold.)

**Robustness of the exclusion.** The way to smuggle the witness into branch 2 would be to hide the heavy block $Y$ (the subcube's defining coordinates) *outside* the chosen $M$, using an E$_d$-style decoy block $K$, $|K|=q$, and top-degree cancellation. Take $R=\{y_Y=+1\}$ of codimension $k$, $u,v\in\{\pm1\}^K$ with $u_K=-v_K$, and $A=(R\times(\{\pm1\}^K\setminus\{u\}))\cup(R^c\times\{v\})$, $B=\bar A$ — the family of u3 §3 with $k$ free. Then $1_A=\Pi_R+\Pi_v-\Pi_R(\Pi_u+\Pi_v)$; the monomial $x_Yx_K$ cancels, $x_K$ survives with coefficient $2^{-q}v_K\ne0$ (degree $q$), and $x_Yx_{K\setminus\{1\}}$ survives with coefficient $-2^{1-k-q}\ne0$ (degree $k+q-1$). For $k\ge2$ the *unique* top support is $Y\cup(K\setminus\{1\})\supseteq Y$; and there $\alpha=2^{-k}(1-2^{-q})+(1-2^{-k})2^{-q}$, so $\mathrm{Inf}_i(f_A)=2^{-q-1}/\alpha\to\tfrac12$ for $i\in K$, giving $\varepsilon_A\ge(q-1)/2$. Excluded again. Only $k=1$ — where the base "jump set" is a codimension-1 subcube, whose single boundary coordinate is heavy for **both** sides — evades this, and that is $\mathcal E_d$ itself, which satisfies [GAP-3]. So the branch restriction is genuine, not a technicality.

## 2. DEFECT in u3: $\pi_\tau\ge\pi_M$ is false

$\pi_\tau\ge\pi_M$ requires $M(A)\subseteq W_\tau(A)$ and $M(B)\subseteq W_\tau(B)$. On $\mathcal W_d$ with $d\ge17$: $W_\tau(A)=[d]$ but $W_\tau(B)=\emptyset$ (every $\mathrm{Inf}_i(f_B)=2^{-d-1}/(1-2^{-d})<\tau$), so
$$\pi_\tau(\mathcal W_d)=0+\sum_{i\in W_\tau(A)}\mathrm{Inf}_i(f_B)=d\,2^{-d-1}/(1-2^{-d})\ \ll\ \tfrac d2\le\pi_M(\mathcal W_d).$$
On $\mathcal E_d$ the same containment fails ($\mathrm{Inf}_i(f_A)=2^{-d}<\tau$ on $M(A)=K$), though there $\pi_\tau>\pi_M$ numerically for an unrelated reason. **Consequence for the route:** branch 1 ("$\pi_M\ge1/\mathrm{poly}(d)$, hence done") is void — $\pi_M$ large does not certify $\pi_\tau$ large, and $\mathcal W_d$ is the counterexample. The dichotomy must be re-cut on $W_\tau$ from the start, and $\pi_M$ retained only as the *branch selector*, never as a payment.

## 3. Fact III, and the exact branch is empty

**Fact III (fibre non-degeneracy).** Let $\deg1_A=d_A\ge1$, $P:=M(A)$, $\chi_P:=\prod_{i\in P}x_i$. For $y\in\{\pm1\}^{[N]\setminus P}$ put $\varphi(y):=\mathbb E_{x_P}[1_A(y,x_P)\chi_P(x_P)]$. Then $\varphi\equiv\theta_A$. Consequently **every** fibre $A_y\subseteq\{\pm1\}^P$ satisfies $\emptyset\ne A_y\subsetneq\{\pm1\}^P$, and its density obeys $a'_y\in[2^{-d_A},1-2^{-d_A}]$.

*Proof.* For $S\subseteq[N]\setminus P$, $\widehat\varphi(S)=\mathbb E_x[1_A(x)\chi_{S\cup P}(x)]=\widehat{1_A}(S\cup P)$, which vanishes for $S\ne\emptyset$ because $|S\cup P|>d_A=\deg1_A$. So $\varphi\equiv\widehat\varphi(\emptyset)=\theta_A\ne0$. If $A_y=\emptyset$ then $\varphi(y)=0$; if $A_y$ is all of $\{\pm1\}^P$ then $\varphi(y)=\mathbb E[\chi_P]=0$ (as $d_A\ge1$). Finally $\varphi(y)=2^{-d_A}\sum_{x_P\in A_y}\chi_P(x_P)\in2^{-d_A}\mathbb Z$ and $|\varphi(y)|\le\min(a'_y,1-a'_y)$. $\square$

Fact III is unconditional and one line; it subsumes "Lemma 1 of u2" ($b_z\ge2^{-d_B}$, whence u3's Theorem A) and adds $|\theta_A|\ge2^{-d_A}$ and the upper bound $a'_y\le1-2^{-d_A}$.

**Theorem C (the exact branch is empty).** Let $A,B$ be cross-disjoint with $\deg1_A,\deg1_B\ge1$. If $\varepsilon_A=\varepsilon_B=0$ then $A\cap B\ne\emptyset$ — a contradiction. Hence no admissible pair has $\pi_M=0$.

*Proof.* $\varepsilon_A=0$ gives $\mathrm{Inf}_i(1_A)=0$ for all $i\in Q:=M(B)$, so $\widehat{1_A}(S)=0$ whenever $S\cap Q\ne\emptyset$: $1_A$ does not depend on $x_Q$. Symmetrically $1_B$ does not depend on $x_P$, $P:=M(A)$. Since $\widehat{1_B}(Q)=\theta_B\ne0$ and $1_B$ is independent of $P$, we get $P\cap Q=\emptyset$. Put $C:=[N]\setminus(P\cup Q)$. Independence means $A$ is determined by $(x_C,x_P)$ and $B$ by $(x_C,x_Q)$: $A=\{(x_C,x_P,x_Q):x_P\in A'_{x_C}\}$, $B=\{\cdot:x_Q\in B'_{x_C}\}$. Fact III applied to $A$ (fibres over $[N]\setminus P$, which are exactly the $A'_{x_C}$) gives $A'_{x_C}\ne\emptyset$ for every $x_C$; applied to $B$ it gives $B'_{x_C}\ne\emptyset$. Choosing $p\in A'_{x_C}$, $q\in B'_{x_C}$ puts $(x_C,p,q)\in A\cap B$. $\square$

So **[GAP-3] holds vacuously at $\varepsilon=0$**: there is nothing in the branch to extract from.

## 4. Why Theorem C does not robustify, and what [GAP-3] still needs

$\mathcal E_d$ has $\varepsilon_A=\varepsilon_B=d\,2^{-d}$ and is admissible, so **Theorem C is sharp up to $2^{-\Theta(d)}$**: the branch is non-empty exactly at the exponential scale, and by u3's Theorem A ($\pi_M\ge\max(1,\tfrac{d}{2})2^{-d}$ termwise) no argument of Theorem C's type can push the emptiness threshold to $1/\mathrm{poly}(d)$. The residual dependence that saves $\mathcal E_d$ is a *single point per fibre*, of measure $2^{-d}$ — precisely the quantum Fact III forbids going below.

What survives of Theorem C's mechanism in the robust regime is a reduction, and it is a **fixed point, not a descent**. Over the base $Z=\{\pm1\}^{[N]\setminus M(B)}$ set $a(z),b(z)$ = densities of $A_z,B_z$. Then (i) $\widehat a(S)=\widehat{1_A}(S)$ for $S\subseteq\overline{M(B)}$, so $\mathrm{Inf}_i(1_A)\ge\mathrm{Inf}_i(a)$ and likewise for $b$; (ii) $\deg a,\deg b\le d$; (iii) $a+b\le1$ pointwise; (iv) $b\ge2^{-d_B}$ everywhere (Fact III); (v) $\mathbb E[a(1-a)]\le\varepsilon_A\alpha$. Items (i)–(iii) say the pair $(a,b)$ is again a cross-disjoint bounded degree-$d$ pair on $Z$ — i.e. **branch 2's content is an instance of the R3-level rung on the base**, which is why no purely structural extraction closes it.

**The precise extra hypothesis.** In the *balanced complementary* sub-case — $\alpha+\beta\ge1-1/\mathrm{poly}(d)$ and $\min(\alpha,\beta)\ge1/\mathrm{poly}(d)$ — one has $b\approx1-a$, hence $\mathrm{Inf}_i(f_B)\gtrsim\mathrm{Inf}_i(a)/\beta$ and $\mathrm{Inf}_i(f_A)\gtrsim\mathrm{Inf}_i(a)/\alpha$ simultaneously, so a *single* coordinate serves both sides and
$$\textbf{[GAP-3] holds}\quad\Longleftarrow\quad \textbf{(H}_{\max}\textbf{)}:\ \max_i\mathrm{Inf}_i(f_R)\ \ge\ 1/\mathrm{poly}(d)\ \text{ for every degree-}{\le}d\text{ set }R\text{ with }\mathrm{Var}(1_R)\ge1/\mathrm{poly}(d).$$
$(\mathrm H_{\max})$ is exactly a max-influence theorem for bounded-degree Boolean functions of Aaronson–Ambainis type; the junta bounds available (Nisan–Szegedy, Chiarelli–Hatami–Saks: $O(2^d)$ relevant coordinates) give only $\max_i\mathrm{Inf}_i(f_R)\ge2^{-O(d)}$, which is worthless at this calibration. **[GAP-4]:** $(\mathrm H_{\max})$ is asserted, not proved, and I did not verify its literature status (no web access in this run). Outside the balanced complementary sub-case, [GAP-3] additionally needs the case $\alpha+\beta\ll1$, where $R$ and $R'$ are disjoint but not complementary and no single coordinate is forced — **[GAP-5]**, untouched.

## 5. Payment certified for the rung

Nothing new above $2^{-\Theta(d)}$. Unconditionally I can certify only $\pi_M\ge\max(1,\tfrac{d_A}{2})2^{-d_A}+\max(1,\tfrac{d_B}{2})2^{-d_B}$ (u3 Theorem A, unaffected), and by §2 that is **not** a lower bound on $\pi_\tau$, so it does not convert into a threshold at all. Under $(\mathrm H_{\max})$ plus the balanced-complementary hypothesis, branch 2 yields $\pi_\tau\ge1/\mathrm{poly}(d)$ and hence $\delta(d)\ge1/\mathrm{poly}(d)$ by the window-size accounting ($|W_\tau|\le d/\tau=O(d^5)$).

## GAP REGISTER

* **No gap** in §1 (the exclusion computation), §2 (the refutation of $\pi_\tau\ge\pi_M$), Fact III, or Theorem C.
* **DEFECT in u3 §0**, upheld: "$\pi_\tau\ge\pi_M$" is false; witness $\mathcal W_d$, $d\ge17$. Branch 1 of the dichotomy pays nothing.
* **[GAP-3]** remains open in the robust regime $\varepsilon=2^{-\Theta(d)}$; it is *not* an instance of the certified-false global statement (§1 verifies the exclusion), and it is *not* refuted — but §4 shows it is self-similar to the rung, so it is not strictly easier.
* **[GAP-4]** $(\mathrm H_{\max})$ unproved and unsourced. **[GAP-5]** the non-complementary case $\alpha+\beta\ll1$ untouched.
* **Scope note.** All of §1 and §3 assume $M(\cdot)$ is *a* maximum-degree support. Under the "all maximum-degree supports" reading, §1's exclusion only strengthens (more coordinates in $M$), and Theorem C is unchanged.

### END OF ARTIFACT 0023-prover-4-u4 ###
