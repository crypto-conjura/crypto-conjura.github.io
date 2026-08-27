id: 0023-prover-4-u0
agent: prover
model: claude-opus-5[1m]
cycle: 4
status: SKETCH

# Method sketch for (PAY★★)

**Verdict.** Plausible; the risk is the word *absolute* in "absolute constant $p$". R2 does not need it: a payment $p$ over windows of size $w$ yields $\delta\approx p/(2w)$, so $p=1/\mathrm{poly}(d)$ with $w=O(d^5)$ already gives an inverse-polynomial $\delta$. The plan below is written for $p$ absolute and degrades gracefully.

## 1. Choice of τ

$\tau:=c/(2d^4)$ with $c$ from (F5); then $|W_\tau(A)|\le d+d/\tau=d+2d^5/c=O(d^5)$.

## 2. Lemma chain (statements only)

**L1 (Heaviness, density-free).** Since $A\cap B=\emptyset$, $\min(\alpha,\beta)\le 1/2$; if $\alpha\le 1/2$ then $\max_i\mathrm{Inf}_i(f_A)=\max_i\mathrm{Inf}_i(\mathbf 1_A)/\alpha\ge c\,\alpha(1-\alpha)/(\alpha d^4)\ge\tau$, so $H_\tau(A)\ne\emptyset$ — the normalisation cancels, handing L4 a sensitive coordinate at a scale independent of density.

**L2 (Uniform fibre floor).** With $W:=W_\tau(A)\cup W_\tau(B)$, $|W|=O(d^5)$: by (F2), for *every* $w\in\{\pm1\}^{[N]\setminus W}$ the fibres satisfy $a_w\ge 2^{-|M(A)|}\ge 2^{-d}$, $b_w\ge 2^{-d}$, $A_w\cap B_w=\emptyset$ — no fibre is empty, so L3 receives a cross-disjoint pair in dimension $O(d^5)$ in every fibre, with weights $a_w/\alpha,\,b_w/\beta$ of mean exactly $1$.

**L3 (Fibre total).** In each fibre $\sum_{i\in W}\mathrm{Inf}_i(f_{A_w})\ge 1-a_w\ge 1/2$, since all non-constant Fourier mass of $\mathbf 1_{A_w}$ lies on $W$; what remains is *localisation* — what fraction of that mass sits on $W_\tau(B)$ rather than on $W_\tau(A)\setminus W_\tau(B)$.

**L4 (Exchange/localisation).** If $\sum_{i\in W_\tau(B)}\mathrm{Inf}_i(f_A)<p$ then $\mathbf 1_A$ is $L^2$-$p$-close to a function ignoring $W_\tau(B)\supseteq M(B)$, and symmetrically for $B$; the two near-independences together with L2's every-fibre nonemptiness contradict $A\cap B=\emptyset$ for $p$ a small absolute constant.

**L5 (Assembly).** L1 supplies the branch hypothesis, L2 the fibre floor, L3 the mass, L4 its location; $\pi_\tau(A,B)\ge p$ in both branches of §3.

## 3. Case split

Split on where (F6)'s unit of payment sits. (a) A constant fraction of $\sum_{i\in\mathrm{Rel}(B)}\mathrm{Inf}_i(f_A)$ is carried by $i$ with $\mathrm{Inf}_i(f_B)\ge\tau$; those $i$ lie in $W_\tau(B)$, so the payment term captures it verbatim and we are done. (b) Otherwise that mass sits on $B$-light relevant coordinates; then (F4) forces $\mathrm{Inf}_i(\mathbf 1_B)\ge 2^{-1-d}$ for each, hence $\beta\ge 2^{-1-d}/\tau$, and one runs L4 on the $B$-side using L1's heavy coordinate for $A$.

## 4. Hardest step

L4. It is **not** the fibre-balance obstruction — L2 and L3 are one-sided and never form the weight $\mathbb E_w[\min(a_w/\alpha,\,b_w/\beta)]$ — it is the $\Omega(1)$-versus-$\Omega(\tau)$ gap: every mechanism I can see for locating $A$'s influence mass on $W_\tau(B)$ delivers $\tau$, not an absolute constant.

## 5. Falsifiable check

Take the hub witness (complementary pair on $d+1$ coordinates) and form its $k$-fold direct sum; brute-force $\pi_\tau$ at $\tau=c/(2d^4)$ for $d\le 4$, $k\le 3$ ($N\le 15$). If $\pi_\tau\to 0$ as $k$ grows, absolute $p$ is dead; if it stalls at $\Theta(1/\mathrm{poly}(d))$, the plan survives in the graceful form of the opening remark.

### END OF ARTIFACT 0023-prover-4-u0 ###
