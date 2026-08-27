---
id: 0023-prover-1-verify-B
agent: verifier
model: claude-sonnet-5
cycle: 2
---

# Verification report: 0023-prover-1 (rung I01, ℤ₂ spread-junta indicators)

## 1. FINAL VERDICT

CLEAN PASS: the artifact proves exactly the I01 statement (word-for-word match
against the Contract/rung text), with explicit witnesses c₁=1/3, c₂=1,
δ(d)=1/(3d), N-independent; every one of Lemmas 1–6 and the Theorem was
re-derived by hand from the stated hypotheses and checks out arithmetically,
including the inline induction proof of the hypercube edge-isoperimetric
inequality (Lemma 3), the layer-cake/level-set argument (Lemma 4), and the
finite-sum weighted-counting aggregation (Lemma 6); no critical error, no
statement drift, no citation defect, and no unverifiable dependency were
found; two trivial PEDANTIC completeness remarks are noted below but do not
affect soundness.

## 2. FINDINGS TABLE

| Quoted location | Class | Explanation |
|---|---|---|
| §5, Lemma 3, "WLOG assume $a:=\|W_+\|\ge b:=\|W_-\|$" | PEDANTIC (not a formal class; would be C at most) | The induction implicitly needs $a\ge1$ (so that the induction hypothesis is applicable to $W_+$ in the $b=0$ case, and so `log_2 a` is defined). This holds automatically since $W\ne\emptyset$ and $a\ge b$ force $a\ge1$, but the one-line justification is left to the reader. A competent reader fills this without effort; does not affect correctness. |
| §6, Lemma 4 Step 1, "$\lvert V_u\triangle V_{u'}\rvert\ge\big\lvert\lvert V_u\rvert-\lvert V_{u'}\rvert\big\rvert$" | PEDANTIC | Standard fact about symmetric differences, stated without its (one-line) proof; true and routine. |
| §10, Remark 10.1 (mentions card S1) | tagged CARD by the artifact itself, non-load-bearing | Checked against card S1 (Claim B.3, NegRow/PosCol, $\mathbb Z_2$-only, threshold $1/(2d)$): the reproved inline construction matches the card's construction and stated influence level exactly; used only as provenance context, not as a justification step, so no citation defect. |

No (A) STATEMENT DRIFT, (B) CRITICAL ERROR, (D) CITATION DEFECT, or (E)
UNVERIFIABLE findings.

## 3. STEP-BY-STEP LOG

**STEP 0 (completeness).** File ends with `### END OF ARTIFACT 0023-prover-1 ###`
after a complete Dependencies section; no mid-sentence/mid-proof truncation.
PASS, not TRUNCATED.

**Class (A) check.** I01's Statement (rung file, lines 22–32) and the
artifact's restated Theorem (§0 and §9) are identical in every quantifier,
every hypothesis (finite support; unit-norm/degree automatic for the class;
per-coordinate *average* influence, for *every* $i\in[N]$, for *both* $\mathbf
F$ and $\mathbf G$; $\delta$ a function of $d$ alone, $N$-independent) and the
exact non-vanishing conclusion. No strengthened hypothesis, no weakened
conclusion, no reordered quantifier, no max-over-support substitution, no
asymptotic-for-exact substitution. Class (A): none.

**Lemma 1 (influence = edge count).** Re-derived: Parseval (Step 1, standard),
flip identity $\mathrm{Inf}_i(f)=\frac14\mathbb E[(f(x)-f(x^{\oplus i}))^2]$
(Step 2, standard), specialization to a normalized indicator giving
$\mathrm{Inf}_i(f)=|\partial_iA|/(2|A|)$ (Step 3 — I recomputed
$\mathbb E_x[(f-f^{\oplus i})^2]=2|\partial_iA|/|A|$ directly from
$\|\mathbf1_A\|_2^2=|A|/2^N$ and the edge count, matches), and the junta
lifting $|\partial_iA|=b_i(P)2^{N-|J|}$, $|A|=|P|2^{N-|J|}$ (Step 4) giving
$\mathrm{Inf}_i(f)=b_i(P)/(2|P|)$. All four steps verified by direct
computation; ACCEPTED. Tag: **MECH**.

**Lemma 2 (disjointness $\iff$ projection disjointness).** Both directions
re-derived from the definitions of $A,B$ as cylinder sets and $\pi_S$; the
$(\Rightarrow)$ direction's explicit witness point $x$ (defined piecewise on
the partition $J,\ K\setminus J,\ [N]\setminus(J\cup K)$) was checked to
satisfy $x_J=p\in P$ and $x_K=q\in Q$ coordinate-by-coordinate, using
$p_S=u=q_S$ on $S=J\cap K$. Degenerate case $S=\emptyset$ correctly forces
$A\cap B\ne\emptyset$ (one-point cube argument). ACCEPTED. Tag: **MECH**.

**Lemma 3 (edge-isoperimetry, entropy form), the flagged non-elementary
ingredient.** Checked with full attention as instructed:
- Base case $n=0$: trivial, correct.
- Exact boundary decomposition $|\partial_EW|=|\partial_EW_+|+|\partial_EW_-|+|W_+\triangle W_-|$:
  re-derived (facet edges vs. direction-$n$ edges partition all edges of the
  $n$-cube); correct, and the bound $|W_+\triangle W_-|\ge a-b$ from
  $W_+\triangle W_-\supseteq W_+\setminus W_-$, $|W_+\setminus W_-|\ge a-b$
  checked correct.
- Case $b=0$: I recomputed $a\log_2(2^{n-1}/a)+a = a\log_2(2^n/a)$
  algebraically (using $\log_2(2^{n-1}/a)+1=\log_2(2\cdot2^{n-1}/a)$); matches
  the claim exactly.
- Case $b\ge1$: I independently expanded
  $g(a)=(a+b)\log_2(a+b)-a\log_2a-b\log_2b-2b$ from RHS(3.3) minus the target
  and got the identical expression to the artifact's; verified $g(b)=0$ by
  direct substitution, and $g'(a)=\log_2\frac{a+b}{a}>0$ by direct
  differentiation of $a\log_2a$ (using $\frac{d}{da}[a\log_2a]=\log_2a+1/\ln2$);
  hence $g\ge0$ on $[b,\infty)$, closing the induction.
This is a genuine, correct, from-scratch inline proof of a real (well-known)
inequality; ACCEPTED with full arithmetic re-verification. Tag: **MECH**.

**Lemma 4 (projection-density payment).** $S=\emptyset$ case trivial and
correct. For $S\ne\emptyset$: (4.2) [$\sum_ib_i(P)\ge\mathrm{TV}_S(w)$]
re-derived from the fiber decomposition and $|V_u\triangle V_{u'}|\ge|w(u)-w(u')|$;
(4.3) [layer-cake identity $\mathrm{TV}_S(w)=\sum_t|\partial_EL_t|$] re-derived
from $|c-c'|=\sum_{t\ge1}|\mathbf1[c\ge t]-\mathbf1[c'\ge t]|$, valid for
nonnegative integers, and the finite-sum exchange is licensed by finiteness;
(4.4) [level-set isoperimetry summed, using Lemma 3 on each nonempty $L_t$ and
monotonicity of $\log_2(2^s/\cdot)$ in the *denominator* direction, i.e.
$|L_t|\le|\pi_S(P)|\Rightarrow\log_2(2^s/|L_t|)\ge\log_2(2^s/|\pi_S(P)|)$] —
direction of the monotonicity step checked and correct; chained with
$\sum_t|L_t|=|P|$. Assembly and division by $2|P|$, substitution of Lemma 1,
correct. ACCEPTED. Tag: **MECH**.

**Lemma 5 (per-pair payment $\ge1$).** $\pi_S(P)\cap\pi_S(Q)=\emptyset$ forced
by Lemma 2; disjoint subsets of $\{\pm1\}^S$ give $\nu_P(S)+\nu_Q(S)\le1$,
AM–GM gives $\nu_P(S)\nu_Q(S)\le1/4$ — checked. Summing two instances of
Lemma 4 and using monotonicity of $\log_2$ to reach $\ge\frac12\log_24=1$ —
checked. ACCEPTED. Tag: **MECH**.

**Lemma 6 (master count), the linearity/counting step singled out for
scrutiny.** Re-verified the exact identity: weighting Lemma 5's per-pair
inequality by $p_aq_b\ge0$ and summing over the finite index set $(a,b)$ gives
$\Sigma_1+\Sigma_2\ge1$ exactly (no union bound, no loss over the — possibly
$N$- or support-size-dependent — number of pairs, since the weights sum to
$1$: this is a genuine weighted-average argument, matching the artifact's own
"generalization hypothesis" claim). Independently re-derived the bound
$\Sigma_1\le\delta_F\sum_bq_b|K_b|$ using $S_{ab}\subseteq K_b$, nonnegativity
of influences, and $\mathbb E_{\mathbf F}[\mathrm{Inf}_i]\le\delta_F$ for every
$i$ (by definition of $\delta_F$ as the max over $i$); symmetric bound for
$\Sigma_2$. Checked that combining these two *upper* bounds with the *lower*
bound $\Sigma_1+\Sigma_2\ge1$ correctly yields (6.1)
$\delta_F\sum_bq_b|K_b|+\delta_G\sum_ap_a|J_a|\ge1$ (valid: sum of upper bounds
$\ge$ sum of the actual quantities $\ge1$). Then $|J_a|,|K_b|\le d$ and
$\delta_F,\delta_G\ge0$ give $(\delta_F+\delta_G)d\ge$ LHS of (6.1) $\ge1$, and
$\delta_F+\delta_G\le2\max(\delta_F,\delta_G)$ gives (6.2). All steps
independently re-derived and correct; finiteness of $m,n,N$ (hence licit sum
reordering) explicitly and correctly invoked. ACCEPTED. Tag: **MECH**.

**Theorem (§9).** Admissibility of $c_1,c_2,\delta$ checked directly.
Proof-by-contradiction: negation of the I01 conclusion is checked to be
*exactly* Lemma 6's "incompatible" hypothesis (via
$f(x)g(x)=\mathbf1_{A\cap B}(x)/(\|\mathbf1_A\|_2\|\mathbf1_B\|_2)$, an exact
identity), giving $\max(\delta_F,\delta_G)\ge1/(2d)$; combined with the
influence hypothesis giving $\delta_F,\delta_G\le\delta(d)=1/(3d)$, i.e.
$\max(\delta_F,\delta_G)\le1/(3d)$; and $1/(2d)>1/(3d)$ for every $d\ge1$ is a
genuine, checked contradiction. ACCEPTED. Tag: **MECH**.

**Remark 10.1 (non-load-bearing tightness).** Independently recomputed:
NegRow/PosCol-style row/column grid on $[d]\times[d]$; verified no common
nonvanishing point (position $(r,c)$ would need to be simultaneously $-1$ and
$+1$); verified via Lemma 1 that $b_i(P_r)=1$ for a singleton pattern, giving
$\mathrm{Inf}_i(f_r)=1/2$ on its window, hence
$\mathbb E_{\mathbf F}[\mathrm{Inf}_{(r',c')}]=1/(2d)$ exactly. Matches card
S1's Claim B.3 construction and stated $1/(2d)$ threshold. Correct and
consistent; explicitly non-load-bearing, does not gate the main result. Tag:
**CARD** (context only) / **MECH** (the reproof itself).

## STEP 0.5 — NEGATION CHECK

For each load-bearing lemma (1–6, Theorem) I attempted to construct or
motivate the negation using the same style of argument, to test whether my
own scrutiny would equally "accept" the opposite claim:
- Lemma 3's negation would require a set $W$ beating the entropy bound; the
  induction's algebra (re-derived independently above, matching exactly) rules
  this out for every $n$ by strong induction — I could not construct a
  step where the inequality direction could be flipped without breaking the
  arithmetic identities (e.g. $a\log_2(2^{n-1}/a)+a=a\log_2(2^n/a)$ is an
  identity, not an inequality, so there is no slack to exploit for a
  counter-derivation).
- Lemma 6 / Theorem's negation would require $\Sigma_1+\Sigma_2<1$ to coexist
  with the per-pair Lemma-5 bound $\ge1$ weighted by a probability
  distribution summing to 1 — impossible by linearity (a weighted average of
  quantities each $\ge1$, with weights summing to 1, is itself $\ge1$; no
  alternative weighting or index-set choice was found that evades this).
No lemma admits a parallel derivation of its negation; no CONTRADICTION
(both-accepted) condition triggered. Hard-stop condition not reached.

## ADJUDICATION TAGS

Lemma 1: **MECH**. Lemma 2: **MECH**. Lemma 3: **MECH**. Lemma 4: **MECH**.
Lemma 5: **MECH**. Lemma 6: **MECH**. Theorem (§9): **MECH**. Remark 10.1:
**CARD** (provenance mention of S1) + **MECH** (self-contained reproof). No
lemma in the load-bearing chain (Lemmas 1–6, Theorem) is tagged CODE (no
executed computation was used or needed — all claims are finite closed-form
algebra) or NONE (nothing was left unchecked) or CARD (no load-bearing step
borrows from a source card; S1 appears only in the explicitly non-load-bearing
Remark 10.1).

## 4. SOURCE REQUEST

None. No external result is used in the load-bearing proof chain (Lemmas 1–6,
Theorem); the one mention of card S1 is non-load-bearing provenance and was
checked directly against the card's content (matches).

### END OF ARTIFACT 0023-prover-1-verify-B ###
