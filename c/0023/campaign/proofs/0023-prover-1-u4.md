---
id: 0023-prover-1-u4
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 4 of 8: Lemma 4)
---

# 0023-prover-1 — Unit 4: Lemma 4 (projection-density payment)

Conventions as in Unit 0. Recall: for $\emptyset\ne P\subseteq\{\pm1\}^J$ and
$S\subseteq J$, $\pi_S:\{\pm1\}^J\to\{\pm1\}^S$ is coordinate restriction and
$\nu_P(S)=|\pi_S(P)|/2^{|S|}\in(0,1]$ is the projection density. Uses
Lemma 1 (Unit 1: $\mathrm{Inf}_i(f_{J,P})=b_i(P)/(2|P|)$ for $i\in J$) and
Lemma 3 (Unit 3: $|\partial_E W|\ge|W|\log_2(2^n/|W|)$ for nonempty
$W\subseteq\{\pm1\}^n$).

---

**Lemma 4 (projection-density payment).** Let $J\subseteq[N]$,
$\emptyset\ne P\subseteq\{\pm1\}^J$, $f=f_{J,P}$, and $S\subseteq J$. Then
$$\sum_{i\in S}\mathrm{Inf}_i(f)\ \ge\ \frac12\,\log_2\frac{1}{\nu_P(S)}.$$

Equivalently (multiplying by $2|P|$ and using Lemma 1): with all quantities
integers,
$$\sum_{i\in S} b_i(P)\ \ge\ |P|\,\log_2\frac{2^{|S|}}{|\pi_S(P)|}.\tag{4.0}$$

*Proof.* If $S=\emptyset$: the left side is an empty sum $=0$, and
$\pi_\emptyset(P)$ is the one-point cube $\{\pm1\}^\emptyset$ itself
(nonempty image inside a one-point set), so $\nu_P(\emptyset)=1$ and the
right side is $0$. ✓ Assume from now on $S\ne\emptyset$; set $s=|S|\ge1$.

Identify $\{\pm1\}^J\cong\{\pm1\}^S\times\{\pm1\}^{J\setminus S}$, writing
window points as $(u,v)$, $u\in\{\pm1\}^S$, $v\in\{\pm1\}^{J\setminus S}$;
then $\pi_S(u,v)=u$. Define the **fiber-count function**
$$w:\{\pm1\}^S\to\mathbb{Z}_{\ge0},\qquad w(u):=\bigl|\{v\in\{\pm1\}^{J\setminus S}:(u,v)\in P\}\bigr| .$$
Three immediate properties:
$$\sum_{u\in\{\pm1\}^S}w(u)=|P|;\qquad w(u)\ge1\iff u\in\pi_S(P);\qquad w(u)\le 2^{|J\setminus S|}.\tag{4.1}$$

**Step 1 (boundary edges dominate the total variation of $w$).** Let
$E(\{\pm1\}^S)$ denote the edge set of the $S$-cube and define
$$\mathrm{TV}_S(w):=\sum_{\{u,u'\}\in E(\{\pm1\}^S)}\bigl|w(u)-w(u')\bigr| .$$
Claim:
$$\sum_{i\in S}b_i(P)\ \ge\ \mathrm{TV}_S(w).\tag{4.2}$$
Fix $i\in S$. Every $i$-edge of the window cube $\{\pm1\}^J$ has the form
$\{(u,v),(u^{\oplus i},v)\}$ for a unique $i$-edge $\{u,u^{\oplus i}\}$ of the
$S$-cube and a unique $v\in\{\pm1\}^{J\setminus S}$ (flipping $i\in S$ changes
only the $S$-part). Hence, grouping the boundary $i$-edges of $P$ by their
$S$-projection,
$$b_i(P)=\sum_{\{u,u'\}\ i\text{-edge of }\{\pm1\}^S}\ \bigl|\{v:\ \mathbf 1[(u,v)\in P]\ne\mathbf 1[(u',v)\in P]\}\bigr| .$$
For a fixed $i$-edge $\{u,u'\}$, the sets $V_u=\{v:(u,v)\in P\}$ and
$V_{u'}=\{v:(u',v)\in P\}$ have sizes $w(u)$, $w(u')$, and the inner count is
$|V_u\triangle V_{u'}|\ge\bigl||V_u|-|V_{u'}|\bigr|=|w(u)-w(u')|$. Summing
over the $i$-edges of the $S$-cube and then over $i\in S$ gives (4.2)
(every edge of the $S$-cube is an $i$-edge for exactly one $i\in S$).

**Step 2 (layer cake).** For $t\in\mathbb{Z}_{\ge1}$ define the level sets
$$L_t:=\{u\in\{\pm1\}^S:\ w(u)\ge t\},\qquad
L_1=\pi_S(P)\supseteq L_2\supseteq\cdots,\qquad L_t=\emptyset\ \text{for}\ t>t_{\max}:=\max_u w(u).$$
For any integers $c,c'\ge0$:
$|c-c'|=\sum_{t\ge1}\bigl|\mathbf 1[c\ge t]-\mathbf 1[c'\ge t]\bigr|$
(the summand is $1$ exactly when $\min(c,c')<t\le\max(c,c')$, which happens
for exactly $|c-c'|$ values of $t$). Applying this to
each edge and exchanging the two finite sums:
$$\mathrm{TV}_S(w)=\sum_{\{u,u'\}\in E}\sum_{t\ge1}\bigl|\mathbf 1_{L_t}(u)-\mathbf 1_{L_t}(u')\bigr|
=\sum_{t=1}^{t_{\max}}\ \sum_{\{u,u'\}\in E}\bigl|\mathbf 1_{L_t}(u)-\mathbf 1_{L_t}(u')\bigr|
=\sum_{t=1}^{t_{\max}}\bigl|\partial_E L_t\bigr|,\tag{4.3}$$
since an edge contributes $1$ to the $t$-th inner sum iff exactly one endpoint
lies in $L_t$. ($t_{\max}\ge1$ because $P\ne\emptyset$; all sums are finite.)

**Step 3 (isoperimetry on each level set).** For $1\le t\le t_{\max}$ the set
$L_t$ is nonempty (any $u$ attaining $w(u)=t_{\max}\ge t$ lies in it), so
Lemma 3 applies in the $s$-dimensional cube:
$$|\partial_E L_t|\ \ge\ |L_t|\log_2\frac{2^{s}}{|L_t|}\ \ge\ |L_t|\log_2\frac{2^{s}}{|\pi_S(P)|},$$
the second step because $L_t\subseteq L_1=\pi_S(P)$ gives
$|L_t|\le|\pi_S(P)|$, and $\log_2$ is monotone (this holds regardless of the
sign of either logarithm, and the prefactor $|L_t|\ge0$). Summing over $t$
and using $\sum_{t=1}^{t_{\max}}|L_t|=\sum_{t\ge1}\sum_u\mathbf 1[w(u)\ge t]
=\sum_u w(u)=|P|$ (by (4.1)):
$$\sum_{t=1}^{t_{\max}}|\partial_E L_t|\ \ge\ |P|\,\log_2\frac{2^{s}}{|\pi_S(P)|}.\tag{4.4}$$

**Assembly.** Chaining (4.2), (4.3), (4.4):
$$\sum_{i\in S}b_i(P)\ \ge\ \mathrm{TV}_S(w)\ =\ \sum_{t=1}^{t_{\max}}|\partial_E L_t|\ \ge\ |P|\,\log_2\frac{2^{s}}{|\pi_S(P)|},$$
which is (4.0). Dividing by $2|P|>0$ and substituting Lemma 1
($\mathrm{Inf}_i(f)=b_i(P)/(2|P|)$ for $i\in S\subseteq J$):
$$\sum_{i\in S}\mathrm{Inf}_i(f)\ \ge\ \frac12\log_2\frac{2^{s}}{|\pi_S(P)|}=\frac12\log_2\frac1{\nu_P(S)}. \qquad\blacksquare$$

---

**Remark 4.1 (why this is the right "payment").** The inequality converts
projection *sparsity* on a window $S$ into a lower bound on total influence
on $S$: a pattern whose $S$-projection covers only a $\nu$-fraction of
$\{\pm1\}^S$ pays total influence $\ge\frac12\log_2(1/\nu)$ there. It is
tight for subcube patterns (Remark 3.1 equality propagates: e.g. $P$ a single
point, $S=J$: LHS $=|J|/2$, RHS $=\frac12\log_2 2^{|J|}=|J|/2$).

**Sanity checks (evidence only).** (i) $P$ full, any $S$: LHS $\ge0=$ RHS ✓.
(ii) $J=\{1,2\}$, $P=\{(+,+),(-,-)\}$, $S=\{1\}$: $\pi_S(P)$ full, RHS $=0$;
LHS $=b_1(P)/(2|P|)=2/4=1/2\ge0$ ✓ (strict slack — diagonal/parity patterns
overpay).
(iii) $P=\{(+,+)\}$, $S=\{1\}$: $\nu=1/2$, RHS $=1/2\cdot1=1/2$;
LHS $=b_1/(2|P|)=1/2$ ✓ equality.

EMITTED unit 4 of 8; NEXT UNIT u5 (Lemma 5, per-pair payment ≥ 1); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u4 ###
