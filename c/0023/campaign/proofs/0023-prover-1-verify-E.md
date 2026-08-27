---
id: 0023-prover-1-verify-E
agent: verifier-b
model: claude-opus-5[1m]
cycle: 2
---

# Blind referee pass E on artifact `0023-prover-1` (rung I01)

Inputs read: `intermediates/I01-spread-junta.md`, `CONTRACT.md`,
`proofs/0023-prover-1.md`, `sources/S1-acc22-card.md`, `sources/S2-clm23-card.md`.
Nothing else in the repository was consulted; no prover reasoning trace, no prior
verdict.

## STEP 0 — COMPLETENESS

The artifact terminates with `### END OF ARTIFACT 0023-prover-1 ###` (line 526).
No unit stops mid-proof: §§3–8 each carry a lemma with a closed proof (`■`), §9
carries the theorem, §§10–12 carry the non-load-bearing remark, the gap register
and the dependency list. NOT TRUNCATED; proceeding to review.

## 1. FINAL VERDICT

CLEAN — the artifact proves exactly the I01 statement (all quantifiers, the class,
per-coordinate average influence, and the $N$-independence of $\delta$ matching),
every one of Lemmas 1–6 and the Theorem is derived inline from the Contract's
definitions with no gap I can find, and the two citation touches are correctly
labelled non-load-bearing context.

## 2. FINDINGS TABLE

| # | Quoted location | Class | Explanation |
|---|---|---|---|
| — | — | — | **No defect of class (A), (B), (C), (D) or (E) found.** |

Non-defect observations, recorded so Triage can see they were considered and
deliberately not raised as findings (each would be OVERRULED or PEDANTIC):

| # | Quoted location | Status | Note |
|---|---|---|---|
| N1 | §10, "This is the NegRow/PosCol pattern of [ACC22] Claim B.3 — card S1 — reproved inline; the card is context, not justification." | NOT a (D) | Card S1 item S1.c prints Claim B.3 for the *summed* polynomials $\mathrm{NegRow}=\sum_i \mathsf{AND}_m(x_{i,*})$, $\mathrm{PosCol}$, i.e. singleton-support distributions with `RelInf` **strictly** $<1/(2d)$; the artifact instead uses *uniform distributions over the $d$ row/column AND-indicators*, with average influence **exactly** $1/(2d)$. These are different objects. The artifact does not lean on the card: it reproves its own construction in full from Lemma 1, calls the citation "provenance context", and marks the whole remark NOT load-bearing (§0, §11). I01's own "Grid ceiling" bullet already restates B.3 in this distributional form, so the artifact is aligned with the rung file. No defect. |
| N2 | §0, "the result is within a factor $3/2$ of optimal" | NOT an (A) | Lemma 6 (6.2) in fact licenses *every* $\delta$ with $\delta(d)<1/(2d)$, so the artifact under-claims by choosing $1/(3d)$. Under-claiming is not drift: I01 asks only for the existence of one admissible inverse-polynomial $\delta$, and $c_1=1/3$, $c_2=1$ is admissible ($\delta(d)=1/(3d)\in(0,1/3]\subseteq(0,1]$, $\delta(d)\ge c_1d^{-c_2}$ with equality). |
| N3 | §1, "Real-valued functions suffice: every class member is real-valued" | NOT a (C) | The Contract's ambient space is $\mathbb{C}$-valued, but $\mathcal{C}^{\mathrm{junta}}_d$ consists of nonnegative real functions and for $\mathcal{Y}=\mathbb{Z}_2$ the dual characters are real, so the $\mathbb{C}$-Fourier expansion of a real function has real coefficients and coincides with the $\pm1$-monomial expansion; $|\hat f(\chi)|^2=\hat f(T)^2$. The Contract itself prints this specialization (`CONTRACT.md` §Definitions, last paragraph). Legitimate. |
| N4 | §8, "Remark 8.1 (generalization hypothesis: satisfied)" | NOT a finding | A meta-claim about I01's "Generalization hypothesis" section, not a mathematical step. I concur on the mathematics it asserts: no constant in Lemmas 1–6 depends on the number of patterns, and (6.1) is bilinear in $(p_a),(q_b)$. Recorded for the ledger, not as a defect. |

## 3. STEP-BY-STEP LOG

### 3.0 Class (A) check, done first: what the artifact actually proves

In my own words, the Theorem of §9 establishes: *fix once and for all $c_1=1/3$,
$c_2=1$, $\delta(d)=1/(3d)$. Then for every $d\in\mathbb{N}$, every
$N\in\mathbb{N}$, and every pair of finitely supported probability distributions
$\mathbf F,\mathbf G$ whose supports lie in $\mathcal{C}^{\mathrm{junta}}_d$ (over
$\{\pm1\}^N$) and which satisfy, for **every** coordinate $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\le 1/(3d)$ and the same for
$\mathbf G$, there are $f\in\mathrm{supp}\,\mathbf F$, $g\in\mathrm{supp}\,\mathbf
G$ and a point $x\in\{\pm1\}^N$ with $f(x)g(x)\ne0$.*

Diff against I01, item by item:

| Contract feature (I01 / CONTRACT.md) | Artifact | Verdict |
|---|---|---|
| Quantifier order: $\exists(c_1,c_2,\delta)$ **before** $\forall(d,N,\mathbf F,\mathbf G)$, then $\exists(f,g,x)$ | §9 fixes $c_1,c_2,\delta$ in the theorem statement, then says "Fix $d,N\in\mathbb{N}$ and $\mathbf F,\mathbf G$ as in the statement" | matches, no swap |
| $\delta$ may depend on $d$, **never on $N$** (CONTRACT.md "Consequences a solver must respect") | $\delta(d)=1/(3d)$; $N$ appears nowhere in $\delta$, and Lemma 6's bound $(δ_F+δ_G)d\ge1$ has no $N$ in it — the $2^{N-|J|}$ factors cancel identically in Lemma 1 (1.3)/(1.4) | matches; this is the crux and it is genuinely $N$-free |
| $\delta(d)\ge c_1d^{-c_2}$, $\delta:\mathbb{N}\to(0,1]$ | verified in §9 first paragraph | matches |
| Class: $\mathbf 1_A/\|\mathbf 1_A\|_2$, $A=\{x:x_J\in P\}$, $J\subseteq[N]$, $|J|\le d$, $\emptyset\ne P\subseteq\{\pm1\}^J$ | §0 reproduces the class verbatim; §1 fixes witnessing $(J,P)$ with $|J|\le d$ | matches |
| Influence hypothesis: **per-coordinate**, **on average over the distribution** ($\forall i$, $\mathbb{E}_{f}[\mathrm{Inf}_i(f)]\le\delta$); NOT $\max_{f\in\mathrm{supp}}$, NOT $\sum_i$, NOT "for some $i$" (CONTRACT.md reading convention 2; I01 "NOT acceptable") | Lemma 6 sets $\delta_F:=\max_{i\in[N]}\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]$ — max over *coordinates* of the *average* over the distribution, which is exactly the hypothesis form; the bound on $\Sigma_1$ sums $\sum_a p_a\mathrm{Inf}_i(f_a)$ **before** bounding by $\delta_F$, so it is genuinely an average argument, not a per-function one | matches; I specifically probed the max-vs-average pattern and the artifact is on the correct (harder) side |
| Conclusion: exact non-vanishing at a single common point, no approximate substitute (CONTRACT.md convention 4) | §9 works with the exact negation "for all $f,g,x$: $f(x)g(x)=0$" | matches |
| Unit norm and $\deg\le d$ pointwise on the support | automatic for the class; verified in Remark 3.1 | matches (and is not needed as a hypothesis, only as a consistency check) |
| Finitely supported distributions (convention 1) | Lemma 6 hypothesis, and used only to make the double sum finite | matches |
| I01 "Does NOT establish: neither PCC nor ℤ₂-PCC" | §12 states this explicitly | matches; no claim inflation |

No statement drift. In particular the artifact does **not** silently restrict to
conjunction patterns (the "Rung 0 calibration" I01 forbids citing): Lemmas 4 and 5
are proved for arbitrary nonempty $P\subseteq\{\pm1\}^J$, and the payment comes
from projection density, not from pattern shape.

### 3.1 §1 conventions — ACCEPTED

* Well-definedness of $f_{J,P}$: $P\ne\emptyset\Rightarrow A\ne\emptyset\Rightarrow
  \|\mathbf 1_A\|_2>0$. Accepted.
* Non-injectivity of $(J,P)\mapsto f_{J,P}$ is flagged and handled by fixing one
  witnessing representation per support element. I checked the consequence the
  artifact asserts: $A=\{x:f(x)\ne0\}$ and $\mathrm{Inf}_i(f)$ are functions of
  $f$ alone, whereas $|J|$ is representation-dependent; the proof only ever needs
  $|J_a|\le d$ for the *chosen* witness (guaranteed by class membership) and the
  *same* chosen witness feeds Lemma 2 ($S_{ab}=J_a\cap K_b$), Lemma 5 and the
  $\Sigma_1,\Sigma_2$ bounds. Internally consistent. Accepted.

### 3.2 Lemma 1 (influence $=b_i(P)/(2|P|)$) — ACCEPTED, tag MECH

* Step 1: $\chi_T\chi_{T'}=\chi_{T\triangle T'}$ and
  $\mathbb{E}[\chi_U]=\mathbf 1[U=\emptyset]$; $2^N$ orthonormal vectors in a
  $2^N$-dimensional space form a basis; Parseval on finite sums. Accepted.
* Step 2: $f(x)-f(x^{\oplus i})=2\sum_{T\ni i}\hat f(T)\chi_T(x)$, hence
  $\mathrm{Inf}_i(f)=\tfrac14\mathbb{E}[(f(x)-f(x^{\oplus i}))^2]$. Recomputed
  independently: $\mathbb{E}[(2\sum_{T\ni i}\hat f(T)\chi_T)^2]=4\sum_{T\ni
  i}\hat f(T)^2$. Accepted.
* Step 3: the count of $x$ with exactly one of $x,x^{\oplus i}$ in $A$ is
  $2|\partial_iA|$ because $i$-edges partition $\{\pm1\}^N$ into $2^{N-1}$
  disjoint pairs. Then
  $\mathbb{E}[\cdot]=2^{-N}\cdot2|\partial_iA|\cdot2^N/|A|=2|\partial_iA|/|A|$ and
  $\mathrm{Inf}_i=|\partial_iA|/(2|A|)$. Recomputed, agrees with (1.2). Accepted.
* Step 4: $|A|=|P|2^{N-|J|}$, and for $i\in J$, $|\partial_iA|=b_i(P)2^{N-|J|}$
  (each boundary window-edge lifts over the $2^{N-|J|}$ choices of $x_{J^c}$, and
  every $i$-edge of the big cube arises exactly once this way). The $2^{N-|J|}$
  cancels — this is precisely where $N$-independence is bought. For $i\notin J$,
  $\mathbf 1_A(x^{\oplus i})=\mathbf 1_A(x)$, so $\mathrm{Inf}_i=0$. Accepted.
* Negation check: I independently computed the singleton case from the Fourier
  side. For $P$ a single point of a $k$-dimensional window, $f=2^{k/2}\mathbf
  1_A$ and $\hat f(T)=2^{-k/2}$ for all $T\subseteq J$, so
  $\mathrm{Inf}_i=2^{k-1}2^{-k}=1/2$, matching $b_i(P)/(2|P|)=1/2$. The full
  pattern gives $f\equiv1$, all influences $0$, matching $b_i=0$. Lemma 1's
  negation is refuted on both checkable extremes. **Tag: MECH.**

### 3.3 Lemma 2 (disjointness $\iff$ projection disjointness) — ACCEPTED, tag MECH

Both directions are contrapositives and both are constructive. The gluing in
($\Rightarrow$) is well defined because $J$, $K\setminus J$,
$[N]\setminus(J\cup K)$ partition $[N]$, and the verification $x_K=q$ splits
correctly into $i\in K\setminus J$ (by fiat) and $i\in S$ (using $p_S=u=q_S$).
The degenerate branch $S=\emptyset$ is discharged explicitly ($\{\pm1\}^\emptyset$
is a one-point set, both projections are nonempty subsets of it hence equal to
it), which is the case that would otherwise silently sink Lemma 5 — the artifact
gets it right and also records it in §2's case-split ledger. **Tag: MECH.**

### 3.4 Lemma 3 (edge isoperimetry, entropy form) — ACCEPTED, tag MECH

This is the lemma the review brief singles out; I checked base case, step,
applicability of the induction hypothesis, and the equality claim separately.

* **Base case present and correct.** $n=0$: the unique nonempty $W$ is the
  one-point cube, $|\partial_EW|=0=1\cdot\log_2(2^0/1)$. The induction at $n=1$
  therefore invokes the statement at $n=0$, which *is* established. No missing
  base case, no invocation at an unestablished value.
* **Boundary decomposition (3.2).** I re-derived it: every edge of $\{\pm1\}^n$
  is either a facet edge (fixed last coordinate $\epsilon$, an edge of the
  $(n-1)$-cube in the first $n-1$) or a direction-$n$ edge; the two kinds are
  disjoint and exhaust; a facet edge at level $\epsilon$ is a boundary edge of
  $W$ iff it is a boundary edge of $W_\epsilon$; a direction-$n$ edge at $u$ is
  boundary iff $u\in W_+\triangle W_-$. So the displayed identity is an equality,
  and the artifact then relaxes $|W_+\triangle W_-|\ge|W_+\setminus W_-|\ge a-b$.
  Accepted. The WLOG $a\ge b$ is legitimate: the decomposition is symmetric under
  $\epsilon\mapsto-\epsilon$.
* **Case $b=0$.** Requires $W_+\ne\emptyset$, which holds since $|W|\ge1$ and
  $b=0$. $a\log_2(2^{n-1}/a)+a=a\log_2(2^n/a)$ — checked. Accepted.
* **Case $b\ge1$.** Both halves nonempty so the induction hypothesis applies to
  each. I recomputed the algebra of the reduction independently:
  RHS(3.3)$-(a+b)\log_2\frac{2^n}{a+b}
  =(a+b)(n-1)-a\log_2a-b\log_2b+a-b-(a+b)n+(a+b)\log_2(a+b)
  =(a+b)\log_2(a+b)-a\log_2a-b\log_2b-2b$, which is exactly the artifact's
  $g(a)$. Accepted.
* **The claim $g\ge0$.** $g(b)=2b\log_2(2b)-2b\log_2b-2b=2b(1+\log_2b)-2b\log_2
  b-2b=0$ — checked. $g'(a)=\log_2(a+b)+\tfrac1{\ln2}-\log_2a-\tfrac1{\ln2}
  =\log_2\frac{a+b}{a}>0$ for $b>0$ — checked (the two $1/\ln2$ terms from
  $\frac{d}{da}[a\log_2a]$ genuinely cancel). Hence $g$ increases on
  $[b,\infty)$ and $g(a)\ge g(b)=0$; evaluating at the integers $a=|W_+|$,
  $b=|W_-|$ is legitimate since the claim is proved for all reals $a\ge b>0$.
  Accepted.
* **Equality cases.** Remark 5.1's subcube computation is correct
  ($|\partial_EW|=|W|\,|I|$, each boundary edge counted once at its $W$-endpoint,
  and $\log_2(2^n/|W|)=|I|$), and the artifact correctly notes that no
  extremizer structure is used downstream — only the inequality. So no hidden
  dependence on an unproved uniqueness-of-extremizer claim.
* **Negation check (exhaustive on small $n$).** $n=1$: $|W|=1\Rightarrow1\ge1$
  (eq), $|W|=2\Rightarrow0\ge0$ (eq). $n=2$: $|W|=1\Rightarrow2\ge2$ (eq);
  $|W|=2$ adjacent $\Rightarrow2\ge2$ (eq); $|W|=2$ diagonal $\Rightarrow4\ge2$;
  $|W|=3\Rightarrow2\ge3\log_2(4/3)\approx1.245$; $|W|=4\Rightarrow0\ge0$. $n=3$
  (representative shapes): $|W|=3$ path $\Rightarrow5\ge3\log_2(8/3)\approx4.25$;
  $|W|=5\Rightarrow5\ge5\log_2(8/5)\approx3.39$;
  $|W|=6\Rightarrow4\ge6\log_2(4/3)\approx2.49$;
  $|W|=7\Rightarrow3\ge7\log_2(8/7)\approx1.35$. No violation; the tightest
  configurations are exactly the subcubes, as Remark 5.1 predicts.
  **Tag: MECH** (proved inline; nothing borrowed, so no CARD dependency arises —
  and this is what lets §11's empty gap register and §12's "External results:
  none" stand).

### 3.5 Lemma 4 (projection-density payment) — ACCEPTED, tag MECH

* $S=\emptyset$ branch: empty sum $=0$ on the left, $\nu_P(\emptyset)=1$ so $0$
  on the right. Discharged explicitly. Accepted.
* **Step 1, (4.2).** For $i\in S$, every $i$-edge of the $J$-cube is
  $\{(u,v),(u^{\oplus i},v)\}$ for a unique $S$-cube $i$-edge and a unique
  $v\in\{\pm1\}^{J\setminus S}$; grouping gives
  $b_i(P)=\sum_{\{u,u'\}}|V_u\triangle V_{u'}|\ge\sum_{\{u,u'\}}\bigl||V_u|-|V_{u'}|\bigr|
  =\sum_{\{u,u'\}}|w(u)-w(u')|$. Summing over $i\in S$ counts each $S$-cube edge
  exactly once (an edge is an $i$-edge for exactly one $i$), yielding
  $\sum_{i\in S}b_i(P)\ge\mathrm{TV}_S(w)$. **Counting step audited specifically**
  (the brief asks for this): the index set on the left is $\{i\in S\}$ times
  $\{i\text{-edges of the }J\text{-cube}\}$; on the right it is
  $\{$edges of the $S$-cube$\}$; the map (window $i$-edge) $\mapsto$ ($S$-cube
  $i$-edge, fiber point $v$) is a bijection, so nothing is double-counted and
  nothing is dropped. Accepted.
* **Step 2, layer cake (4.3).** $|c-c'|=\sum_{t\ge1}|\mathbf1[c\ge t]-\mathbf
  1[c'\ge t]|$ for nonnegative integers (the summand is $1$ exactly for the
  $|c-c'|$ values of $t$ in $(\min,\max]$). The interchange of summation is over
  two finite index sets (edges of a finite cube $\times$ $t\le t_{\max}$), so no
  interchange justification is missing — I probed this against the "sum/integral
  interchange without justification" failure pattern and it is clean. The
  truncation at $t_{\max}=\max_uw(u)\ge1$ ($\ge1$ because $P\ne\emptyset$) is
  correct since $L_t=\emptyset$ for $t>t_{\max}$. Accepted.
* **Step 3.** For $1\le t\le t_{\max}$, $L_t\ne\emptyset$ (any maximizer of $w$
  lies in it), so Lemma 3 applies in the $s$-cube — the hypothesis of Lemma 3
  (nonempty) is checked at the point of use, not assumed. Then
  $L_t\subseteq L_1=\pi_S(P)$ gives $|L_t|\le|\pi_S(P)|$ and hence
  $\log_2\frac{2^s}{|L_t|}\ge\log_2\frac{2^s}{|\pi_S(P)|}$, multiplied by
  $|L_t|\ge0$ (sign of the prefactor checked). The identity
  $\sum_{t=1}^{t_{\max}}|L_t|=\sum_uw(u)=|P|$ is correct. Accepted.
* Assembly: dividing (4.0) by $2|P|>0$ and substituting Lemma 1 is valid because
  $S\subseteq J$, which is where Lemma 1's $i\in J$ branch is needed. Accepted.
* **Negation check.** (i) $P=\pi_S^{-1}(U)$, i.e. $P=U\times\{\pm1\}^{J\setminus
  S}$: then $\sum_{i\in S}b_i(P)=|\partial_EU|\,2^{|J\setminus S|}$ and (4.0)
  reduces *exactly* to Lemma 3 for $U$ — so Lemma 4 is tight precisely when
  Lemma 3 is, and a counterexample to Lemma 4 in this family would be one to
  Lemma 3. (ii) $P$ a singleton, $S=J$: both sides $|J|/2$, equality. (iii)
  $J=\{1,2\}$, $S=\{1\}$, $P=\{(+,+)\}$: LHS $b_1=1$, RHS $|P|\log_22=1$,
  equality. (iv) diagonal $P=\{(+,+),(-,-)\}$, $S=J$: LHS $=b_1+b_2=4$, RHS
  $=2\log_2(4/2)=2$, slack — matching the artifact's own "parity-like patterns
  overpay" note. No violation. **Tag: MECH.**

### 3.6 Lemma 5 (per-pair payment $\ge1$) — ACCEPTED, tag MECH

Lemma 2 supplies both $\pi_S(P)\cap\pi_S(Q)=\emptyset$ **and** $S\ne\emptyset$
(the latter is needed for the statement to be non-vacuous and is imported, not
assumed). Disjoint nonempty subsets of $\{\pm1\}^S$ give
$\nu_P(S)+\nu_Q(S)\le1$; AM–GM gives $\nu_P\nu_Q\le1/4$; both densities are
$>0$ so the logarithms are finite; adding the two Lemma 4 instances (legitimate:
$S\subseteq J$ and $S\subseteq K$) yields
$\frac12\log_2\frac1{\nu_P\nu_Q}\ge\frac12\log_24=1$. Negation check: Remark 7.1's
$J=K=\{1\}$, $P=\{-1\}$, $Q=\{+1\}$ attains exactly $1$, so the constant cannot be
improved and is not accidentally off by a factor. **Tag: MECH.**

### 3.7 Lemma 6 (master count) — ACCEPTED, tag MECH

This is the linearity-of-expectation/counting step the brief asks me to audit; I
re-derived it from scratch.

* Finiteness: $m,n,N<\infty$, so all interchanges in (6.3) and after are
  unconditional. There is **no union bound over an unbounded index** anywhere —
  the probability weights $p_aq_b$ sum to $1$, so the pairwise payments are
  *averaged*, not *summed*. I probed the "union bound over an $n$-dependent
  index" pattern specifically: the number of pairs $mn$ never appears in the
  final bound, which is what makes the argument survive at inverse-polynomial
  scale. Accepted.
* (6.3): Lemma 5 holds for **every** pair $(a,b)$ (incompatibility is a
  for-all-pairs hypothesis), so multiplying by $p_aq_b\ge0$ and summing is a
  convex combination of statements each $\ge1$, hence $\ge1$. No independence
  between $\mathbf F$ and $\mathbf G$ is assumed or needed — the product weight
  $p_aq_b$ is just the weight in the double average, not a claim that anything is
  independent. I probed the "unshown independence" pattern; it does not arise.
  Accepted.
* $\Sigma_1$ bound: $S_{ab}=J_a\cap K_b\subseteq K_b$ and influences are
  nonnegative, so enlarging the inner index set to $K_b$ can only increase; then
  $\sum_{a,b}p_aq_b\sum_{i\in K_b}\mathrm{Inf}_i(f_a)
  =\sum_bq_b\sum_{i\in K_b}\mathbb{E}_{\mathbf F}[\mathrm{Inf}_i]
  \le\delta_F\sum_bq_b|K_b|$. The order of operations is the load-bearing detail
  and it is right: the $a$-sum (i.e. the average over $\mathbf F$) is taken
  **first**, and only the resulting per-coordinate *average* is bounded by
  $\delta_F$. A max-over-support argument would have bounded $\mathrm{Inf}_i(f_a)$
  individually; this does not. Accepted. (Remark: by Lemma 1 the enlargement is
  in fact an equality, since $\mathrm{Inf}_i(f_a)=0$ for $i\notin J_a$; harmless.)
* $\Sigma_2$ bound: the symmetric routing $S_{ab}\subseteq J_a$, then the $b$-sum
  first: $\sum_ap_a\sum_{i\in J_a}\mathbb{E}_{\mathbf G}[\mathrm{Inf}_i]
  \le\delta_G\sum_ap_a|J_a|$. I verified the "cross" structure is not swapped:
  $\mathbf F$'s influence budget is spent over $\mathbf G$'s windows and vice
  versa. Accepted.
* (6.2): $\sum_bq_b|K_b|\le d$ and $\sum_ap_a|J_a|\le d$ (each $|J_a|,|K_b|\le d$
  and the $p,q$ are probability vectors), $\delta_F,\delta_G\ge0$, so
  $(\delta_F+\delta_G)d\ge1$; then $\delta_F+\delta_G\le2\max$ gives
  $\max\ge1/(2d)$. Accepted.
* **Negation check.** Instantiate (6.1) at the $d\times d$ grid of Remark 10.1:
  $\delta_F=\delta_G=1/(2d)$, $\sum_bq_b|K_b|=\sum_ap_a|J_a|=d$, LHS
  $=\tfrac12+\tfrac12=1$ — the inequality is attained with equality, so Lemma 6's
  constant is exactly right and cannot be an artifact of a slack step. I also
  tried to construct a violating configuration by hand at $d=2$: cross-disjointness
  forces every $J_a$ to meet every $K_b$; if $|S_{ab}|=1$ then Lemma 2 forces both
  patterns to *fix* that coordinate, driving that coordinate's influence to $1/2$
  in both functions (recovering the grid); if $|S_{ab}|\ge2$ the payment can be
  spread (e.g. $\pi_S(P)=\{(+,+),(-,-)\}$ vs $\pi_S(Q)=\{(+,-),(-,+)\}$, densities
  $1/2$ each), but then the shared windows consume window budget and $|K_b|\le d$
  reabsorbs the gain — consistent with (6.1) being tight at $1$. No violation
  found. **Tag: MECH.**

### 3.8 Theorem §9 — ACCEPTED, tag MECH

* Admissibility of the witnesses re-checked above (see N2).
* Nonemptiness of both supports: correct, and needed for (6.3) to be a nonempty
  convex combination.
* Negation of the conclusion $\Rightarrow$ pairwise disjoint supports: correct
  because class members are nonnegative, so $f(x)g(x)>0\iff x\in A\cap B$ and
  $=0$ otherwise; there is no cancellation possibility (this is exactly where the
  restriction to *indicators* rather than signed functions is used, and the
  artifact uses it openly — this is the rung's declared restriction, not smuggled
  generality).
* Contradiction $1/(2d)\le\max(\delta_F,\delta_G)\le1/(3d)$ with
  $1/(2d)>1/(3d)$ for all $d\ge1$. Accepted.
* Remark 9.1 ($0\in\mathbb{N}$): at $d=0$ the class is $\{f\equiv1\}$ ($J=\emptyset$
  forced, $P$ the one-point set) and the conclusion is immediate; at $N=0$ the
  cube is a point, $[N]=\emptyset$ makes the hypothesis vacuous and $J=\emptyset$
  is forced. Both branches check out; $\delta(0):=1\in(0,1]$ is consistent with
  the constraint being imposed only for $d\ge1$ (as I01 prints it). Accepted as a
  correct handling of a convention ambiguity — and note the artifact *reports*
  the ambiguity rather than silently picking a reading, as the Interpretation Rule
  requires.

### 3.9 §10 Remark 10.1 (tightness) — ACCEPTED as non-load-bearing, tag CARD (context only)

Verified anyway: the $2d$ functions lie in $\mathcal{C}^{\mathrm{junta}}_d$
(windows of size exactly $d$, singleton patterns), the $f_r$ are pairwise distinct
and likewise the $g_c$ (checked at $d=1$ too, where the grid degenerates to a
single coordinate and the two functions are still distinct and disjoint), no
common non-vanishing point since cell $(r,c)$ would need both signs, and
$\mathbb{E}_{\mathbf F}[\mathrm{Inf}_{(r',c')}]=\frac1d\cdot\frac12=\frac1{2d}$ for
*every* coordinate because exactly one row function is supported on each cell.
Conclusion "no witnessing $\delta$ can have $\delta(d)\ge1/(2d)$" follows. Its
relation to card S1 is discussed at N1; the citation is context, the mathematics
is self-contained, so no (D) and no (E) arises. **Tag: CARD (non-load-bearing);
the load-bearing chain's tag set is MECH throughout.**

### 3.10 §§11–12 registers — ACCEPTED

The empty gap register is *earned*: I found no step that borrows an unproved
external statement. The only two external touches (card S1 in Remark 10.1;
refuter artifact `0023-refuter-2` as plan provenance in §12) are both declared
non-justificatory, and neither is reachable from the Theorem through the
dependency graph of §2. §12's scope notes ($\delta$ $N$-free; average not max;
windows $\le d$; exact non-vanishing; establishes R1 only) are all accurate as
verified above. No class (E) finding: nothing in the load-bearing chain requires a
source I cannot reach.

### 3.11 Common-failure-pattern sweep (explicit results)

| Pattern | Result |
|---|---|
| quantifier order swapped / "sufficiently large $n$" dropped | not present; §3.0 diff |
| union/probability bound over an unbounded or $N$-dependent index | not present; Lemma 6 averages with weights summing to $1$, and $m,n,N$ never enter the bound |
| worst-case vs expected vs high-probability conflated | probed hardest (this is the rung's stated trap); Lemma 6 keeps the average-over-distribution form throughout |
| asymptotic standing in for an explicit constant | not present; $c_1=1/3$, $c_2=1$ explicit, no $o(1)$ anywhere in the chain |
| reduction/hybrid with an unaccounted lost factor | no reduction or hybrid is used |
| adversary/oracle over-empowered; simulation only claimed | n/a (not a crypto reduction) |
| independence assumed but not shown | not present; see §3.7 |
| limit / sum interchange unjustified | all sums finite; §3.5 Step 2 and §3.7 |
| negligible/measure-zero exception treated as empty | not present; every degenerate branch ($S=\emptyset$, $b=0$, $L_t=\emptyset$, $d=0$, $N=0$, $J=\emptyset$) is discharged in the text and listed in §2's case-split ledger |
| induction with missing base case / step at an unestablished value | Lemma 3 has $n=0$ and steps only from $n-1$ to $n$; checked |
| object constructed but not shown to satisfy every property | Remark 10.1's $2d$ functions: class membership, distinctness, disjointness and influence level are each verified; Remark 3.1 verifies unit norm and $\deg\le d$ for the class |

## 4. SOURCE REQUEST

none. No class (D) or (E) finding; the two cards already in `sources/` cover every
external mention, and the load-bearing chain cites nothing external.

### END OF ARTIFACT 0023-prover-1-verify-E ###
