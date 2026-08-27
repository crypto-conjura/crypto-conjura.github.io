---
id: 0023-prover-1-u5
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 5 of 8: Lemma 5)
---

# 0023-prover-1 — Unit 5: Lemma 5 (per-pair payment ≥ 1)

Conventions as in Unit 0. Uses Lemma 2 (Unit 2) and Lemma 4 (Unit 4).

---

**Lemma 5 (per-pair payment).** Let $J,K\subseteq[N]$,
$\emptyset\ne P\subseteq\{\pm1\}^J$, $\emptyset\ne Q\subseteq\{\pm1\}^K$, and
let $f=f_{J,P}$, $g=f_{K,Q}$ with supports $A$, $B$. If $A\cap B=\emptyset$,
then with $S:=J\cap K$:
$$\sum_{i\in S}\bigl[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)\bigr]\ \ge\ 1 .$$

*Proof.* By Lemma 2, $A\cap B=\emptyset$ implies
$$\pi_S(P)\cap\pi_S(Q)=\emptyset,$$
and (also by Lemma 2) forces $S\ne\emptyset$. The sets $\pi_S(P)$ and
$\pi_S(Q)$ are nonempty (images of nonempty sets) and disjoint subsets of
$\{\pm1\}^S$, so
$$|\pi_S(P)|+|\pi_S(Q)|\ \le\ 2^{|S|},\qquad\text{i.e.}\qquad \nu_P(S)+\nu_Q(S)\ \le\ 1 .$$
Both densities are in $(0,1)$; by AM–GM,
$$\nu_P(S)\,\nu_Q(S)\ \le\ \Bigl(\frac{\nu_P(S)+\nu_Q(S)}{2}\Bigr)^{2}\ \le\ \frac14 .\tag{5.1}$$
Apply Lemma 4 to $(J,P,S)$ and to $(K,Q,S)$ — legitimate since
$S\subseteq J$ and $S\subseteq K$ — and add:
$$\sum_{i\in S}\bigl[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)\bigr]
\ \ge\ \frac12\log_2\frac1{\nu_P(S)}+\frac12\log_2\frac1{\nu_Q(S)}
\ =\ \frac12\log_2\frac{1}{\nu_P(S)\,\nu_Q(S)}
\ \ge\ \frac12\log_2 4\ =\ 1,$$
the last inequality by (5.1) and monotonicity of $\log_2$. $\blacksquare$

---

**Remark 5.1 (tight).** The bound is attained: $J=K=\{1\}$, $P=\{-1\}$,
$Q=\{+1\}$ gives disjoint supports, $S=\{1\}$,
$\mathrm{Inf}_1(f)=\mathrm{Inf}_1(g)=1/2$ (Lemma 1 with $b=1$, $|P|=1$), sum
$=1$. Every link is equality: $\nu_P=\nu_Q=1/2$, densities equal (AM–GM
tight), projections partition the shared cube, Lemma 4 tight on both sides.

**Remark 5.2 (mechanism).** Conflict certification is *paid for on the
shared window*: two patterns can only exclude each other by projecting to
disjoint — hence jointly sparse — subsets of $\{\pm1\}^{J\cap K}$, and
Lemma 4 converts that joint sparsity into total influence $\ge1$ on the
shared window. Coordinates of tiny influence live in nearly-full
projections (Lemma 1: $b_i\ll|P|$) and can never carry a conflict on their
own; this is the quantitative content behind the rung's "money question"
(sub-inverse-polynomial influences cannot certify incompatibility in this
class).

EMITTED unit 5 of 8; NEXT UNIT u6 (Lemma 6 + Theorem + tightness remark); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u5 ###
