---
id: 0023-prover-3-u2
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: UNIT 2 of 6 (witness (a) + CAP I)
---

# Unit 2 — witness (a): the address pair, and CAP I (the relevance-denominated cap)

## L5 (the address pair, exact)

**Construction.** Fix $k\ge1$ and set $d:=k+1$. Coordinates: $k$ *address bits*
$a_1,\dots,a_k$ and $2^k$ *target bits* $y_j$, $j\in\{0,1\}^k$; so
$N=k+2^k$. For $a\in\{\pm1\}^k$ let $b(a)\in\{0,1\}^k$ be its bit pattern,
$b_t(a):=\tfrac{1-a_t}2$. Put
$$A_k:=\{x\in\{\pm1\}^N:\ y_{b(a)}=+1\},\qquad B_k:=A_k^{\,c}=\{x:\ y_{b(a)}=-1\}.$$

**Statement.** For every $k\ge1$ (so every $d\ge2$):

1. $\mathbf 1_{A_k}=\tfrac12+2^{-k-1}\sum_{j\in\{0,1\}^k}\sum_{T\subseteq[k]}
   \varepsilon_T(j)\,a_T\,y_j$, where $\varepsilon_t(j):=1-2j_t\in\{\pm1\}$,
   $\varepsilon_T(j):=\prod_{t\in T}\varepsilon_t(j)$, $a_T:=\prod_{t\in T}a_t$.
2. $\deg\mathbf 1_{A_k}=\deg\mathbf 1_{B_k}=k+1=d$; the maximum-degree monomial
   supports of $\mathbf 1_{A_k}$, and of $\mathbf 1_{B_k}$, are **exactly** the
   $2^k$ sets $\{a_1,\dots,a_k,y_j\}$, $j\in\{0,1\}^k$.
3. $\alpha_{A_k}=\alpha_{B_k}=\tfrac12$;
   $\mathrm{Rel}(A_k)=\mathrm{Rel}(B_k)=[N]$, so
   $|\mathrm{Rel}|=k+2^k=2^{d-1}+d-1$ on both sides and $S(A_k,B_k)=[N]$.
4. Influences of the normalised functions, on both sides:
   $\mathrm{Inf}_{a_t}(f)=\tfrac14$ ($t\in[k]$),
   $\mathrm{Inf}_{y_j}(f)=2^{-k-1}$ ($j\in\{0,1\}^k$); total influence
   $\sum_i\mathrm{Inf}_i(f)=\tfrac k4+\tfrac12\ (\le d)$.
5. $(A_k,B_k)\in\mathcal P_d$ and
   $$\pi_{\mathrm{Rel}}(A_k,B_k)=\tfrac k2+1=\tfrac{d+1}2,\qquad
   \frac{\pi_{\mathrm{Rel}}(A_k,B_k)}{|\mathrm{Rel}(A_k)|+|\mathrm{Rel}(B_k)|}
   =\frac{k+2}{4(k+2^k)}\ \le\ \frac{d+1}{2^{d+1}} .$$

**Proof.** (1) For each $j$, $\mathbf 1[b(a)=j]=\prod_{t=1}^k\mathbf
1[a_t=\varepsilon_t(j)]=\prod_{t=1}^k\frac{1+\varepsilon_t(j)a_t}2
=2^{-k}\sum_{T\subseteq[k]}\varepsilon_T(j)a_T$. Since exactly one $j$ satisfies
$b(a)=j$,
$$\mathbf 1_{A_k}(x)=\sum_j\mathbf 1[b(a)=j]\cdot\frac{1+y_j}2
=\tfrac12\sum_j\mathbf 1[b(a)=j]+\tfrac12\sum_j\mathbf 1[b(a)=j]\,y_j .$$
The first sum is $\equiv1$, giving $\tfrac12$. Expanding the second by the
display above gives $2^{-k-1}\sum_j\sum_T\varepsilon_T(j)a_Ty_j$, which is (1).
(One may double-check the constant term: $\sum_j\varepsilon_T(j)=
\prod_{t\in T}\bigl(\sum_{j_t\in\{0,1\}}(1-2j_t)\bigr)2^{k-|T|}=0$ for
$T\ne\emptyset$, so no $a_T$-only monomial appears, consistent with (1).)

(2) The monomials in (1) are $a_Ty_j$ with supports $T\cup\{y_j\}$, pairwise
distinct as $(T,j)$ ranges over $2^{[k]}\times\{0,1\}^k$, each with coefficient
$\pm2^{-k-1}\ne0$. So (1) *is* the multilinear expansion, $\deg=\max(|T|+1)=k+1$,
and the maximum-degree supports are those with $|T|=k$, i.e. $T=[k]$: the sets
$\{a_1,\dots,a_k,y_j\}$, one for each $j$, and there are $2^k$ of them. Since
$\mathbf 1_{B_k}=1-\mathbf 1_{A_k}$, its expansion has the same monomials with
negated coefficients (and constant $\tfrac12$), so it has the same degree and the
same maximum-degree supports.

(3) $\alpha_{A_k}=\mathbb E[\mathbf 1_{A_k}]=\tfrac12$ by (1);
$\alpha_{B_k}=1-\tfrac12$. Every $a_t$ occurs (e.g. in $a_{\{t\}}y_j$) and every
$y_j$ occurs, so $\mathrm{Rel}(A_k)=[N]$, and likewise for $B_k$.

(4) By (1) every coefficient has $|\widehat{\mathbf 1_{A_k}}(S)|=2^{-k-1}$ on the
$2^k\cdot2^k$ monomial supports. Monomials containing $y_j$: all $2^k$ choices of
$T$, so $\mathrm{Inf}_{y_j}(\mathbf 1_{A_k})=2^k\cdot2^{-2k-2}=2^{-k-2}$.
Monomials containing $a_t$: $T\ni t$ ($2^{k-1}$ choices) and any $j$ ($2^k$
choices), so
$\mathrm{Inf}_{a_t}(\mathbf 1_{A_k})=2^{2k-1}\cdot2^{-2k-2}=\tfrac18$.
Dividing by $\alpha=\tfrac12$ gives $\tfrac14$ and $2^{-k-1}$. The same holds for
$B_k$ (same $|$coefficients$|$, same $\alpha$). Total:
$k\cdot\tfrac14+2^k\cdot2^{-k-1}=\tfrac k4+\tfrac12$.

(5) $A_k\cap B_k=\emptyset$, both nonempty, both of degree $d$: so
$(A_k,B_k)\in\mathcal P_d$. By L3.1's identity and $S=[N]$,
$$\pi_{\mathrm{Rel}}(A_k,B_k)=\sum_{i\in[N]}\bigl[\mathrm{Inf}_i(f_{A_k})+\mathrm{Inf}_i(f_{B_k})\bigr]
=2\Bigl(\tfrac k4+\tfrac12\Bigr)=\tfrac k2+1 .$$
Dividing by $2(k+2^k)$ gives $\frac{k+2}{4(k+2^k)}$, and since
$k+2^k\ge2^k=2^{d-1}$ and $k+2=d+1$, this is $\le\frac{d+1}{4\cdot2^{d-1}}
=\frac{d+1}{2^{d+1}}$. $\blacksquare$

**Independent check.** `0023-prover-3-code/check_witnesses.py` builds $A_k,B_k$
as truth tables on $\{\pm1\}^N$ (no formula), computes the Fourier transform by
integer fast Walsh–Hadamard and all influences as exact `Fraction`s, for
$k=1,2,3$: it reproduces $\alpha=1/2$; $\deg=k+1$; $|\mathrm{Rel}|=k+2^k$
($3,6,11$); address influences $1/4$; target influences $1/4,1/8,1/16$;
$\sum_i\mathrm{Inf}_i=3/4,1,5/4$; $\pi_{\mathrm{Rel}}=3/2,2,5/2$; ratios
$1/4,1/6,5/44$; and that the maximum-degree supports are exactly $2^k$ sets, each
containing all address bits and exactly one target. All agree with L5 and with
`0023-refuter-3` §4's table ($k=3$: $|J|=11$, $\pi=5/2$, ratio $1/8.8=5/44$).

**Remark L5.1 (this witness re-proves the junta blow-up inline).** $A_k$ has
degree $d=k+1$ and depends on $k+2^k=2^{d-1}+d-1$ coordinates, so
$M(d)\ge2^{d-1}+d-1$: the relevance window of a degree-$d$ set is *unavoidably*
exponential in $d$. Cards S6c/S6d are therefore not needed anywhere in this
artifact except as context (they sharpen the constant to $\Theta(2^d)$).

## L6 (CAP I — the relevance-denominated cap)

**Statement.** Let $d\ge2$, $k=d-1$, and let $W$ be **any** localised window
functional at degree $d$ (canonical or not). Then

$$\textbf{(i)}\quad V_W(d)\ \le\ \frac{d+1}{2\bigl(|W(A_k)|+|W(B_k)|\bigr)}
\qquad\text{if }|W(A_k)|+|W(B_k)|\ge1,$$
$$\textbf{(ii)}\quad V_W(d)=0\qquad\text{if }W(A_k)=W(B_k)=\emptyset .$$

**Consequences.**
* **(a) Relevance-complete windows.** If $W(A)\supseteq\mathrm{Rel}(A)$ for all
  $A$ (in particular $W=W_{\mathrm{rel}}$, and in particular the
  "junta-substitution" route that replaces R1's window by the junta set), then
  $$V_W(d)\ \le\ \frac{d+1}{4(2^{d-1}+d-1)}\ \le\ \frac{d+1}{2^{d+1}}\ =\ 2^{-\Theta(d)} .$$
* **(b) Density-$c$ windows.** If $|W(A_k)|\ge c|\mathrm{Rel}(A_k)|$ and
  $|W(B_k)|\ge c|\mathrm{Rel}(B_k)|$ for some $c=c(d)>0$, then
  $V_W(d)\le\frac{d+1}{c\,2^{d+1}}$. So even $c(d)=1/\mathrm{poly}(d)$ leaves
  $V_W(d)=2^{-\Theta(d)}$.
* **(c) Any sub-exponential window suffices to kill.** If merely
  $|W(A_k)|+|W(B_k)|\ge2^{\varepsilon d}$ for some $\varepsilon>0$, then
  $V_W(d)\le(d+1)2^{-\varepsilon d}/2=2^{-\Theta(d)}$.

**Proof.** (ii) is D5's first clause, since $(A_k,B_k)\in\mathcal P_d$ by L5(5).
For (i): by D5, $V_W(d)\le\Theta_W(d)$, and $\Theta_W(d)$ is an infimum over
$\mathcal P_d$ of ratios, so it is bounded by the ratio at the single admissible
pair $(A_k,B_k)$:
$$V_W(d)\ \le\ \frac{\pi_W(A_k,B_k)}{|W(A_k)|+|W(B_k)|}
\ \overset{\text{L3.1}}{\le}\ \frac{\pi_{\mathrm{Rel}}(A_k,B_k)}{|W(A_k)|+|W(B_k)|}
\ \overset{\text{L5(5)}}{=}\ \frac{(d+1)/2}{|W(A_k)|+|W(B_k)|}.$$
For (a): $|W(A_k)|+|W(B_k)|=2(k+2^k)=2(2^{d-1}+d-1)$, giving the first bound, and
$2^{d-1}+d-1\ge2^{d-1}$ the second. (b): substitute
$|W(A_k)|+|W(B_k)|\ge2c(k+2^k)\ge c\,2^{d}$. (c): substitute directly.
$\blacksquare$

**Corollary L6.1 (what this closes).** By L2, *any* argument in $\mathcal W$
whose window functional is relevance-denominated in the sense of L6(a)–(c)
establishes at most $\max(\delta_{\mathbf F},\delta_{\mathbf
G})\ge(d+1)2^{-\varepsilon d}$, i.e. a threshold that is
$2^{-\Theta(d)}$ — hence **not inverse-polynomial**, and within a
$\mathrm{poly}(d)$ factor of the already-known K1 threshold $2^{-d}/d$ (card
S1). In I02's terms such an artifact is a **PARTIAL, not a proof of R2**, and
this is now a theorem about the technique rather than an observation about one
attempt. In particular:
* refuter-2's per-pair inequality (M) transplanted to $\mathcal
  C^{\mathrm{ind}}_d$ — capped;
* the R1 proof with the junta size $M(d)$ substituted for the window size (I02's
  recorded non-solution) — capped, with the explicit numerical ceiling
  $(d+1)2^{-d-1}$;
* I02's own flagged route ("re-base R1's payment on the total-influence budget")
  **in its per-coordinate/per-relevant-coordinate form** — capped: charging a
  conflict against the partner's used-coordinate count is exactly L6(a).

**Remark L6.2 (what CAP I does *not* say).** It does not say the payment is
small: $\pi_{\mathrm{Rel}}(A_k,B_k)=\frac{d+1}2$ is *large*. The kill is caused
entirely by the **denominator** — the number of relevant coordinates, which L5.1
shows is $\ge2^{d-1}$. Hence a functional whose window size is bounded by a
theorem *independent of relevance* is untouched by CAP I; that is the precise
sense in which the shattering window (card S7b, $|W|\le d$) and the certificate
window ($|W|\le O(d^4)$) sit outside it, quantified in Unit 5.

EMITTED unit 2 of 6. NEXT UNIT: 3 — witness (b), the codimension-$d$ subcube
pair, and CAP II (the own-heavy cap), including the promotion of refuter-3's
$\min$-form killer to the sum-form payment.
ARTIFACT 0023-prover-3.

### END OF ARTIFACT 0023-prover-3-u2 ###
