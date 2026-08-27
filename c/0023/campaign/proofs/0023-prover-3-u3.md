---
id: 0023-prover-3-u3
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: UNIT 3 of 6 (witness (b) + CAP II)
---

# Unit 3 — witness (b): the codimension-$d$ subcube pair, and CAP II (the own-heavy cap)

## L7.1 (the subcube pair, exact)

**Construction.** Fix $d\ge1$ and $N\ge d$; let
$C:=\{x\in\{\pm1\}^N:\ x_1=\dots=x_d=+1\}$ and $D:=C^{\,c}$.

**Statement.**
1. $\mathbf 1_C=2^{-d}\sum_{S\subseteq[d]}x_S$ and $\mathbf 1_D=1-\mathbf 1_C$;
   $\deg\mathbf 1_C=\deg\mathbf 1_D=d$, and the unique maximum-degree monomial
   support of each is $[d]$.
2. $\alpha_C=2^{-d}$, $\alpha_D=1-2^{-d}$;
   $\mathrm{Rel}(C)=\mathrm{Rel}(D)=[d]=S(C,D)$.
3. $\mathrm{Inf}_i(f_C)=\tfrac12$ and
   $\mathrm{Inf}_i(f_D)=\dfrac1{2(2^d-1)}$ for every $i\in[d]$ (and $0$ for
   $i>d$).
4. $(C,D)\in\mathcal P_d$ and
   $$\pi_{\mathrm{Rel}}(C,D)=\frac d2+\frac d{2(2^d-1)},\qquad
   \frac{\pi_{\mathrm{Rel}}(C,D)}{|\mathrm{Rel}(C)|+|\mathrm{Rel}(D)|}=\frac14+\frac1{4(2^d-1)} .$$

**Proof.** (1) $\mathbf 1_C=\prod_{i=1}^d\frac{1+x_i}2=2^{-d}\sum_{S\subseteq[d]}
x_S$; the coefficient of $x_{[d]}$ is $2^{-d}\ne0$ and no monomial has larger
support, so $\deg=d$ with $[d]$ the unique maximum-degree support. Passing to
$\mathbf 1_D=1-\mathbf 1_C$ negates all non-constant coefficients, so the same
holds for $D$.
(2) $\alpha_C=\mathbb E[\mathbf 1_C]=2^{-d}$; the relevant sets are $[d]$ by (1).
(3) For $i\in[d]$: $\mathrm{Inf}_i(\mathbf 1_C)=\sum_{S\subseteq[d],S\ni
i}(2^{-d})^2=2^{d-1}\cdot4^{-d}=2^{-d-1}$, and
$\mathrm{Inf}_i(\mathbf 1_D)=\mathrm{Inf}_i(\mathbf 1_C)=2^{-d-1}$ (equal
non-constant coefficients up to sign). Dividing by $\alpha_C=2^{-d}$ and
$\alpha_D=(2^d-1)2^{-d}$:
$\mathrm{Inf}_i(f_C)=\tfrac12$, $\mathrm{Inf}_i(f_D)=\frac{2^{-d-1}2^{d}}{2^d-1}
=\frac1{2(2^d-1)}$.
(4) $C\cap D=\emptyset$; both are nonempty (for $d\ge1$, $|C|=2^{N-d}\ge1$ and
$|D|=2^N-2^{N-d}\ge1$); degrees are $d$. Then by L3.1's identity and $S=[d]$,
$\pi_{\mathrm{Rel}}(C,D)=d\bigl[\tfrac12+\frac1{2(2^d-1)}\bigr]$; divide by
$|\mathrm{Rel}(C)|+|\mathrm{Rel}(D)|=2d$. $\blacksquare$

**Independent check.** `check_witnesses.py` (truth tables, integer
Walsh–Hadamard, exact `Fraction`s) confirms for $d=2,\dots,6$:
$\mathrm{Inf}(f_C)=1/2$; $\mathrm{Inf}(f_D)=1/6,1/14,1/30,1/62,1/126
=\frac1{2(2^d-1)}$; $\pi_{\mathrm{Rel}}=4/3,12/7,32/15,80/31,64/21$; ratio
$1/3,2/7,4/15,8/31,16/63=\frac14+\frac1{4(2^d-1)}$; one maximum-degree support per
side, of size $d$. The influence values agree with `0023-refuter-3` §4.

**Remark L7.2 (two facts about forced coordinates, proved inline).** Say $A$
*forces* $i$ if $A\subseteq\{x:x_i=s\}$ for some $s\in\{\pm1\}$; write
$\mathrm{Forced}(A)$ for the set of such $i$.
*(a) A forced coordinate has $\mathrm{Inf}_i(f_A)=\tfrac12$ exactly.* Indeed
$\mathbf 1_A\cdot\frac{1-sx_i}2\equiv0$ gives $x_i\mathbf 1_A=s\mathbf 1_A$
pointwise, hence $\widehat{\mathbf 1_A}(S\cup\{i\})=s\,\widehat{\mathbf 1_A}(S)$
for every $S\not\ni i$ (multiplication by $x_i$ maps the coefficient at $S$ to
the coefficient at $S\triangle\{i\}$). So
$\mathrm{Inf}_i(\mathbf 1_A)=\sum_{S\not\ni i}\widehat{\mathbf 1_A}(S\cup\{i\})^2
=\sum_{S\not\ni i}\widehat{\mathbf 1_A}(S)^2=\tfrac12\lVert\mathbf 1_A\rVert_2^2
=\tfrac{\alpha_A}2$, i.e. $\mathrm{Inf}_i(f_A)=\tfrac12$.
*(b) A degree-$\le d$ set forces at most $d$ coordinates.* If $A$ forces every
$i\in F$ then $\alpha_A\le2^{-|F|}$, while L4.0 applied to $\mathbf 1_A$ gives
$\alpha_A=\Pr[\mathbf 1_A\ne0]\ge2^{-\deg\mathbf 1_A}\ge2^{-d}$; hence
$|F|\le d$.
(So $W_{\mathrm{Forced}}$ is a localised functional, own-heavy at
$\theta=\tfrac12$, with $|W_{\mathrm{Forced}}|\le d$ — a legitimate member of the
class, and the window used by refuter-3 §5.1. Note $\mathrm{Forced}(C)=[d]$ and
$\mathrm{Forced}(D)=\emptyset$.)

## L7.3 (CAP II — the own-heavy cap) and its dichotomy

**Definition (recalled).** $W$ is **own-heavy at level $\theta$** if
$W(A)\subseteq\{i:\mathrm{Inf}_i(f_A)\ge\theta\}$ for every admissible $A$.

**Theorem (CAP II).** Let $d\ge1$ and let $W$ be a localised window functional
that is own-heavy at some level $\theta>\dfrac1{2(2^d-1)}$. Then
$$V_W(d)\ \le\ \frac1{2(2^d-1)}\ =\ 2^{-\Theta(d)} .$$

**Proof.** By L7.1(3) every coordinate has $\mathrm{Inf}_i(f_D)\le
\frac1{2(2^d-1)}<\theta$ (coordinates $i>d$ have influence $0$), so own-heaviness
forces $W(D)=\emptyset$.
*Case $W(C)=\emptyset$:* then $(C,D)\in\mathcal P_d$ has both windows empty, so
$V_W(d)=0$ by D5.
*Case $W(C)\ne\emptyset$:* $W(C)\subseteq\mathrm{Rel}(C)=[d]$, and
$$\pi_W(C,D)=\underbrace{\sum_{i\in W(D)}\mathrm{Inf}_i(f_C)}_{=0}
+\sum_{i\in W(C)}\mathrm{Inf}_i(f_D)=\frac{|W(C)|}{2(2^d-1)},$$
so $V_W(d)\le\Theta_W(d)\le\dfrac{\pi_W(C,D)}{|W(C)|+|W(D)|}
=\dfrac{|W(C)|/(2(2^d-1))}{|W(C)|}=\dfrac1{2(2^d-1)}$. $\blacksquare$

**Corollary L7.4.** Any argument in $\mathcal W$ whose window is selected by an
own-influence threshold $\theta(d)\ge1/\mathrm{poly}(d)$ — for instance
$W^{\theta}_{\mathrm{hvy}}$, or $W_{\mathrm{Forced}}$ ($\theta=\tfrac12$), or
"the coordinates carrying at least a $1/\mathrm{poly}(d)$ share of the total
influence budget $\sum_i\mathrm{Inf}_i\le d$" — establishes at most
$\max(\delta_{\mathbf F},\delta_{\mathbf G})\ge\frac1{2(2^d-1)}$, for every $d$
with $\theta(d)>\frac1{2(2^d-1)}$ (i.e. all $d\ge d_0(\theta)$). For
$W_{\mathrm{Forced}}$ the value is in fact $V=0$: the pair $(C,D)$ has
$W_{\mathrm{Forced}}(C)=[d]$ but the *bound* is $\frac1{2(2^d-1)}$; and the pair
of two disjoint sets neither of which forces anything (e.g. the $d=2$
signed-4-cycle pairs of `0023-refuter-3` §2, or $(A_k,B_k)$ of L5, which force
nothing) has both windows empty, so the route establishes **nothing at all**
there.

**L7.5 (dichotomy: exactly which windows witness (b) kills).** For any localised
$W$, put $w_C=|W(C)|$, $w_D=|W(D)|$. Then
$$\frac{\pi_W(C,D)}{w_C+w_D}=\frac{\tfrac12 w_D+\tfrac{w_C}{2(2^d-1)}}{w_C+w_D}
\begin{cases}=\dfrac1{2(2^d-1)}=2^{-\Theta(d)},&w_D=0<w_C,\\[2mm]
\ \ge\ \dfrac1{2(w_C+w_D)}\ \ge\ \dfrac1{4d},&w_D\ge1 .\end{cases}$$
(The second line uses $w_C,w_D\le|\mathrm{Rel}|=d$.) **So witness (b) caps $W$
exponentially if and only if $W$ omits the cheap side's window entirely.** The
decisive question a plan must answer is therefore not "is my payment a sum rather
than a $\min$?" but:

> *does my window ever contain a coordinate that is cheap for its own function
> and expensive for the partner?*

If yes, witness (b) is powerless; if no, witness (b) kills the route at
$\frac1{2(2^d-1)}$.

**Remark L7.6 (this strictly strengthens refuter-3's killer (b)).** refuter-3
§4–5.2 shows
$\theta^*(d)=\min_{\text{pairs}}\max_{i\in S}\min(\mathrm{Inf}_if,\mathrm{Inf}_ig)
\le\frac1{2(2^d-1)}$, which refutes the **$\min$-form** route (HEAVY$_\theta$);
`0023-strategist-2` §0.4/IG3 correctly observes that this does not bind
**sum-form** payments, since on $(C,D)$ the sum payment is $\ge d/2$. CAP II
closes that gap in the *other* direction: the sum payment is large only because
$W(C)=[d]$ contains coordinates *cheap for $C$'s partner but expensive for $C$*;
as soon as the window rule refuses to select coordinates cheap for their own
function, the sum-form count collapses to the same exponential value. Hence the
min-to-sum move recommended by IG3 is **necessary but not sufficient**, and the
sufficient condition is exactly the italicised question of L7.5. This is new
relative to `0023-refuter-3` and is the part of the barrier that most changes how
a plan should be drafted.

**Remark L7.7 (the two caps are dual).** CAP I kills through the **denominator**
(window size forced to $2^{\Theta(d)}$ while the payment stays $\Theta(d)$); CAP
II kills through the **numerator** (window size stays $\le d$ but the payment
collapses to $2^{-\Theta(d)}$). A window functional therefore needs *both*
properties to survive: windows bounded by something other than relevance, **and**
willingness to charge coordinates that are cheap for their own side. Unit 5 shows
the shattering and certificate windows have both.

EMITTED unit 3 of 6. NEXT UNIT: 4 — the SCOPE LEMMA (the caps at R2–R6) and the
CALIBRATION lemma (why frozen I01, refuter-3 §5.1's $1/(8d)$ bound, and P4 are
not condemned).
ARTIFACT 0023-prover-3.

### END OF ARTIFACT 0023-prover-3-u3 ###
