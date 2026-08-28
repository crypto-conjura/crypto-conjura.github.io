id: 0023-analysis-1
agent: prover
model: claude-opus-5[1m]
cycle: 5

status: PARTIAL

# Are the two conditional routes complementary?

**Verdict: NO.** The projection fact *is* decisive — but it decides against
complementarity. It collapses $\kappa$ to $1/\alpha$, and route 2's exchange
rate then shows route 2 pays only when $\alpha\le\mathrm{poly}(d)2^{-d}$, not
when $\kappa\ge\mathrm{poly}(d)$. An exponentially wide density band escapes
both, and it is occupied by an elementary pair.

## 1. The window does contain both defect sets (Lemma 1)

**Lemma 1.** Let $A$ be nonempty with $\deg 1_A\le d$ and $W_A$ its
projection-defect set, $|W_A|\le d$ (S7b). Then for **any** $W\supseteq W_A$ and
every $w\in\{\pm1\}^{[N]\setminus W}$, $A_w\ne\emptyset$; hence $p_A=1$.

*Proof.* $[N]\setminus W\subseteq[N]\setminus W_A$. Given
$w\in\{\pm1\}^{[N]\setminus W}$, extend it arbitrarily to
$w'\in\{\pm1\}^{[N]\setminus W_A}$. By S7b there is $x\in A$ with
$x|_{[N]\setminus W_A}=w'$; then $x|_{[N]\setminus W}=w$. $\square$

Route 2 sets $W=W_A\cup W_B$ ($|W|\le 2d$ here; $4d$ in its degree-$2d$
setting — the constant is immaterial). So Lemma 1 applies to both sides:

$$p_A=p_B=1,\qquad \boxed{\kappa_A=1/\alpha,\quad \kappa_B=1/\beta}\ \text{exactly.}$$

Two consequences. (i) $\kappa_A\in[1,2^d]$ is exactly the density floor
$\alpha\ge2^{-d}$ restated; $\kappa_A=2^d$ on the codim-$d$ subcube ✓. (ii)
**`0023-prover-5-u0` §4's stated enemy is misidentified.** "Each $A$ dense
inside a $2^{-d}$-fraction of fibres, a junta on coordinates outside $W$" cannot
occur: Lemma 1 forbids it. $\kappa_A=O(1)$ means only $\alpha=\Omega(1)$ — a
dense set, which route 1 already claims. The fibre apparatus carries no
information beyond density; step 4 is literally

$$\max_i\mathrm{Inf}_i(f_A)\ \ge\ \frac{2^{-d-1}}{4d\,\alpha}. \tag{$\ast$}$$

I have re-derived $(\ast)$ and it is sound: $\mathrm{Inf}_i(1_A)=\mathbb
E_w[\mathrm{Inf}^{(w)}_i(1_{A_w})]$ for $i\in W$; Poincaré on $\{\pm1\}^W$ gives
$\sum_{i\in W}\mathrm{Inf}^{(w)}_i\ge\alpha_w(1-\alpha_w)\ge2^{-d-1}$ (steps 2–3
force $2^{-d}\le\alpha_w\le1-2^{-d}$); average, divide by $|W|$ and by $\alpha$.
Its real content is the $N$-free localisation $\sum_{i\in
W}\mathrm{Inf}_i(1_A)\ge2^{-d-1}$.

## 2. The exchange rate, and the escaping band

$(\ast)$ reaches $1/\mathrm{poly}(d)$ **iff** $\kappa_A\ge2^{d+1}\cdot
4d/\mathrm{poly}(d)$, i.e. $\alpha\le\mathrm{poly}(d)\,2^{-d}$ — route 2's own
§3 says "hands the rung whenever $\mathbb E_A[\kappa_A]\ge2^d/\mathrm{poly}(d)$"
and $\kappa\le2^d$ always. The question's hypothesis
"$\max(\kappa_A,\kappa_B)\ge\mathrm{poly}(d)$" therefore understates what route 2
needs by a factor $2^d$. Since $\max(\kappa_A,\kappa_B)=1/\min(\alpha,\beta)$:

| route | covers |
|---|---|
| 1 (payment, `refuter-8` §5) | $\min(\alpha,\beta)\ge d^{-a}$ |
| 2 (fibre-wise, $(\ast)$) | $\min(\alpha,\beta)\le d^{b}2^{-d}$ |

**Escaping regime.** $d^{b}2^{-d}<\min(\alpha,\beta)<d^{-a}$. Nonempty for every
$d$ with $d^{a+b}<2^{d}$, i.e. all but finitely many $d$, whatever the
polynomials. In your terms: a pair escapes both iff each side is *sparse yet not
at the granularity floor* — and by Lemma 1 "meets few fibres" is impossible, so
$p$ contributes nothing and the escape is purely a statement about $\alpha$.

**Sharp exhibit (elementary).** $A=$ codimension-$k$ subcube, $B=\bar A$, with
$b\log_2 d<k<d-a\log_2 d$, e.g. $k=\lceil d/2\rceil$. Both have degree $k\le d$;
cross-disjoint; $W=K$, $|K|=k\le d$; $\alpha=2^{-k}$, $\beta=1-2^{-k}$;
$\kappa_A=2^{k}=2^{d/2}$, $\kappa_B\approx1$. Route 1 fails ($\alpha\ll
d^{-a}$); $(\ast)$ returns $2^{-d/2-1}/(4d)$. Neither regime applies.
`0023-refuter-8`'s certified V1/V2 witnesses sit in the same band (C1: $d=80$,
$\alpha=1.46\cdot10^{-11}\approx2^{-36}=2^{-0.45d}$), so the band is occupied by
a family already known to defeat route 1 unconditionally.

## 3. What a third argument must cover, and the likely repair

The residual target is: *every nonempty $A$ with $\deg 1_A\le d$ and
$2^{-d}\le\alpha\le1/2$ has $\max_i\mathrm{Inf}_i(f_A)\ge1/\mathrm{poly}(d)$*,
with the middle band $\mathrm{poly}(d)2^{-d}\le\alpha\le d^{-a}$ open.

The loss in $(\ast)$ is localised: step 3 replaces $\alpha_w(1-\alpha_w)$ by the
worst-case granularity floor $2^{-d-1}$. Keeping it gives the strictly stronger

$$\max_i\mathrm{Inf}_i(f_A)\ \ge\ \frac{\lambda_A}{8d},\qquad
\lambda_A:=\frac{\mathbb E_w\big[\min(\alpha_w,1-\alpha_w)\big]}{\alpha}, \tag{$\dagger$}$$

using $\alpha_w(1-\alpha_w)\ge\tfrac12\min(\alpha_w,1-\alpha_w)$ and
$|W|\le2d$. Here $\lambda_A\ge\kappa_A2^{-d}$, and $\lambda_A=1$ whenever
$\alpha_w\le\tfrac12$ for a.e. $w$. On the exhibit of §2 every fibre has
$\alpha_w=2^{-k}$, so $\lambda_A=1$ and $(\dagger)$ yields $1/(8d)$ — correct
(true value $1/2$). **So §2's escape family is not an escape family for
$\lambda$.** The right residual conjecture is $\lambda_A\ge1/\mathrm{poly}(d)$,
whose only enemy is $A$ nearly filling the fibres it is dense on while being
globally sparse. Whether such $A$ of degree $\le d$ exists is [GAP] — untested.

## 4. Status of the pieces

Nothing above proves the rung. Route 1's conditional (`0023-refuter-8` §5) is an
Aaronson–Ambainis-type max-influence statement, **unproved and uncited**. Route
2's chain (`0023-prover-5-u0` steps 1–4) is a SKETCH; §1 above confirms step 4's
arithmetic but its steps 1–3 rest on S7b and on the cross-disjointness argument
of step 2, neither re-verified here. This artifact is a **reduction and a
refutation of a claimed complementarity**, not a proof. Also unaddressed: whether
the rung needs a heavy coordinate on one side or both — on the §2 exhibit
$\max_i\mathrm{Inf}_i(f_B)\approx2^{-k-1}$, so under a two-sided reading that
pair refutes the rung outright and the two-sided reading must be wrong.

### END OF ARTIFACT 0023-analysis-1 ###
