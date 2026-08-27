id: S9-osss
agent: scout (source-carding errand 2, campaign c/0023, SOURCE GATE 1 for rung I02/R2)
model: claude-opus-5[1m]
cycle: 4; status: COMPLETE

# SOURCE CARD [S9] — the OSSS inequality ("Every decision tree has an influential variable")

Discharges the second errand of the cycle-4 scout gate: plan **P4** is gated on
this inequality and **P5** may use it. Also the engine of card **S8** (the
status of the single-function question (Q)); S8 cites this card, not the paper.

**Citation.** Ryan O'Donnell, Michael Saks, Oded Schramm, Rocco A. Servedio,
*Every decision tree has an influential variable*, **FOCS 2005**, pp. 31–39
(IEEE), DOI 10.1109/SFCS.2005.34. Preprint read: **arXiv:cs/0508071v1**
(16 Aug 2005), 11 pages, the version "posted by permission from the IEEE
Computer Society. To appear in FOCS 2005" (p. 1 footnote). All page numbers
below are the **arXiv v1** pages.

**Retrieval status. [READ]** — the full v1 PDF fetched from
`arxiv.org/pdf/cs/0508071` and **all 11 pages read as page images** on
2026-08-27 (pp. 1–9 body, 10–11 references). Rung 1 of the access ladder only;
no block. A mirror exists at `cs.columbia.edu/~rocco/Public/osss-focs_z.pdf`
(not used). ⚠ Theorem numbering verified for the arXiv/FOCS preprint; a later
journal reprint could renumber.

---

## Conventions fixed by the paper (get these wrong and the factor is wrong)

All printed on pp. 2 and 6, [READ]:

* **Domain.** `{-1,1}^n_{(p)}` is the cube with the *p*-biased product measure
  `mu_(p)(x) = p^{|{i : x_i = 1}|}(1-p)^{|{i : x_i = -1}|}`; writing
  `{-1,1}^n` alone means **uniform** `p = 1/2`. §3 generalises to an arbitrary
  finite *n*-wise product probability space `Omega = X_1 x ... x X_n`.
* **Variance.** `Var[f] = E[f^2] - E[f]^2 = 4 Pr[f = 1] Pr[f = -1]`; the paper
  says explicitly: "*if f is equally likely to be 1 as -1, then*
  `Var[f] = 1`". So for a **balanced ±1-valued** `f`, `Var[f] = 1` exactly.
* **Influence.** `Inf_i(f) = 2 Pr_{x, x^{(i)}}[f(x) != f(x^{(i)})]`, where
  `x^{(i)}` **rerandomizes** (not flips) coordinate `i`. The paper states
  (p. 2): "*Our definition agrees with the one introduced in [2] in the uniform
  measure case p = 1/2, which was* `Inf_i[f] = Pr[f(x) != f(x ⊕ i)]`", and
  differs from the p-biased notion of e.g. Friedgut–Kalai by a factor
  `4p(1-p)`. `Inf(f) := sum_i Inf_i(f)` is the total influence.
* **CONVERSION TO THIS CAMPAIGN'S CONTRACT (scout's own one-line check, not
  printed).** At `p = 1/2` and for **±1-valued** `f`,
  `Pr[f(x) != f(x ⊕ i)] = sum_{S ∋ i} fhat(S)^2`, so **OSSS's `Inf_i` is
  exactly the Contract's Fourier influence** and `Var[f] = sum_{S != ∅}
  fhat(S)^2`. ⚠ For `{0,1}`-valued indicators the two conventions differ by a
  factor 4 both in `Inf_i` and in `Var` (see card S6a's influence dictionary);
  the *ratio* `Var/Inf_max` used by Corollary 1.2 is scale-invariant, so the
  corollary transfers to `{0,1}`-valued functions unchanged, but a bare
  `Inf_i` number does not.
* **Cost measures.** For a deterministic decision tree (DDT) `T` computing `f`:
  `delta_i(T) = Pr_x[T queries x_i]`, and
  `Delta(T) = sum_i delta_i(T) = E_x[# coords T queries on x]`. `Delta(f)` is
  the minimum of `Delta(T)` over all DDTs computing `f` (equivalently over all
  randomized decision trees, RDTs); `D(f)` is the min-max **depth**, `R(f)` the
  zero-error randomized complexity. Printed: `Delta(f) <= R(f) <= D(f)`.

---

## Verbatim statements (LaTeX-ised transcriptions from the page images)

```latex
% Abstract, p. 1:
We prove that for any decision tree calculating a boolean function
f : \{-1,1\}^n \to \{-1,1\},
    \mathbf{Var}[f] \le \sum_{i=1}^n \delta_i \mathbf{Inf}_i(f),
where \delta_i is the probability that the ith input variable is read and
\mathbf{Inf}_i(f) is the influence of the ith variable on f. The variance,
influence and probability are taken with respect to an arbitrary product
measure on \{-1,1\}^n. It follows that the minimum depth of a decision tree
calculating a given balanced function is at least the reciprocal of the largest
influence of any input variable. Likewise, any balanced boolean function with a
decision tree of depth d has a variable with influence at least 1/d. The only
previous nontrivial lower bound known was \Omega(d 2^{-d}).

% Theorem 1.1, p. 3 (the main inequality for Boolean functions):
Let f : \{-1,1\}^n_{(p)} \to \{-1,1\} and let T be a DDT computing f. Then
    \mathbf{Var}[f] \le \sum_{i=1}^n \delta_i(T)\,\mathbf{Inf}_i(f).

% Corollary 1.2, p. 3:
For every f : \{-1,1\}^n_{(p)} \to \{-1,1\} we have
    \Delta(f) \ \ge\ \frac{\mathbf{Var}(f)}{\mathbf{Inf}_{\max}(f)} .

% Remark after Corollary 1.2, p. 3:
[If] d is an integer \ge \Delta(f), then the sum of the influences of the d
most influential variables is at least \mathbf{Var}[f].

% Section 1.2.1, p. 4 -- THE DEGREE COROLLARY, the sentence card S8 turns on:
For instance, Nisan and Szegedy [18] showed that if f : \{-1,1\}^n \to
\{-1,1\} is computed by a polynomial over \mathbb{R} of degree \deg(f), then
every coordinate i with nonzero influence has \mathbf{Inf}_i(f) \ge
2^{-\deg(f)}. Since D(f) \le O(\deg(f)^4) (by a result of Nisan and Smolensky
[8]), our Corollary 1.2 implies that the maximum influence in fact satisfies
    \mathbf{Inf}_{\max}(f) \ \ge\ \Omega\bigl(\mathbf{Var}[f]/\deg(f)^4\bigr).

% Section 1.2.1, p. 4 -- the APPROXIMATE-degree version:
... since D(f) \le O(\widetilde{\deg}(f)^6) by [1], our Corollary 1.2 implies
that the maximum influence in fact satisfies
    \mathbf{Inf}_{\max}(f)\ \ge\ \Omega\bigl(\mathbf{Var}[f]/
      \widetilde{\deg}(f)^6\bigr),
% where \widetilde{\deg}(f) is the least degree of a p with |p(x)-f(x)|<1/3
% for all x. (Contrast: Talagrand's route gives only
% \mathbf{Inf}_{\max}(f) \ge \exp(-O(\widetilde{\deg}(f)/\mathbf{Var}[f])).)

% Theorem 3.1, p. 6 (the general metric-space inequality):
Let f : \Omega \to (Z,d) be a function mapping a finite n-wise product
probability space into a metric space, and let T be a DDT computing f. Then
    \mathbf{Vr}[f] \le \sum_{i=1}^n \delta_i(T)\,\mathbf{Inf}_i(f),
% where \mathbf{Vr}^{\mu,d}[f] = E_{(x,y)}[d(f(x),f(y))] (the "variation") and
% \mathbf{Inf}_i^{\mu,d}(f) = E_{(x,x^{(i)})}[d(f(x),f(x^{(i)}))].

% Theorem 3.2, p. 7 (the TWO-FUNCTION version):
Let f, g : \Omega \to (Z,d) be functions mapping a finite n-wise product
probability space into a metric space, and let \mathcal{T} be an RDT computing
f. Then
    \bigl|\mathbf{CoVr}[f,g]\bigr| \le \sum_{i=1}^n
        \delta_i(\mathcal{T})\,\mathbf{Inf}_i(g),
% \mathbf{CoVr}[f,g] = E_{(x,y)}[d(f(x),g(y))] - E_x[d(f(x),g(x))];
% \mathbf{CoVr}[f,f] = \mathbf{Vr}[f].

% Consequence printed p. 8 (approximation form):
[F]or every \epsilon > 0 the expected number of queries required by a
randomized decision tree to calculate any approximation f of g satisfying
E[d(f(x),g(x))] \le \epsilon is at least
    \frac{\mathbf{Vr}[g] - 2\epsilon}{\mathbf{Inf}_{\max}(g)} .

% Equation (6), p. 8 (real-valued two-function version):
    \bigl|\mathbf{Cov}[f,g]\bigr| \le \sum_{i=1}^n
       \delta_i(\mathcal{T})\,\mathbf{Inf}_i^{\rho_1}[g],
% for f : \Omega \to [-1,1], g : \Omega \to \mathbb{R}, \mathcal{T} an RDT
% computing f, \rho_1(x,y) = |x-y|, \mathbf{Cov}[f,g] = E[f g] - E[f]E[g].

% Theorem 3.3, p. 8 (semimetric version) and Corollary 3.4, pp. 8-9:
Let f, g : \Omega \to (Z,\rho) be functions mapping an n-wise product
probability space into a semimetric space, and let \mathcal{T} be an RDT
computing f. Let k be the length of the longest path in any DDT in
\mathcal{T}'s support. Then |\mathbf{CoVr}[f,g]| \le \mathbf{Def}_k(\rho)
\sum_i \delta_i(\mathcal{T}) \mathbf{Inf}_i(g).
% Corollary 3.4 (the real-valued, \rho_2(z,z')=(z-z')^2/2 case, where
% \mathbf{Vr}^{\rho_2}[f] = \mathbf{Var}[f]):
Let f : \Omega \to (\mathbb{R},\rho_2) ... and let \mathcal{T} be an RDT
computing f. Let k be the length of the longest path in any DDT in
\mathcal{T}'s support. Then
    \mathbf{Var}[f] \le k \sum_{i=1}^n \delta_i(\mathcal{T})
        \mathbf{Inf}_i^{\rho_2}(f),
and f has a coordinate with \rho_2-influence at least \mathbf{Var}[f]/k^2.
```

**Proof mechanism (one line, from pp. 6–7, so a prover knows what is being
used).** Couple `x` and `y` independent, walk the tree on `x` and define the
hybrid `u[t]` agreeing with `x` on the first `t` queried coordinates and with
`y` elsewhere; `Vr[f] = E[d(f(u[0]), f(u[s]))]` telescopes along the path by
the **triangle inequality**, and each step is `Inf_{i_t}` in expectation. The
triangle inequality is the only place metricity is used; that is exactly what
fails for `rho_2` (see "does NOT say").

---

## Hypotheses itemised (with a ✔/⚠ against this campaign's objects)

1. **`f` is TOTAL and `{-1,1}`-valued** on the whole cube (Theorem 1.1 /
   Corollary 1.2). ✔ for the campaign's balanced `g : {±1}^m -> {±1}`;
   ✔ for `{0,1}`-valued indicators `1_A` after the affine change of value
   (S6a shared convention 2), noting the factor-4 caveat above.
   ⚠ **NOT satisfied** by the normalized members `1_A/||1_A||_2` of
   `C^ind_d` as *real-valued* functions unless one uses the general
   Theorem 3.1/3.3 versions with their own losses.
2. **There is a decision tree computing `f` exactly**, and `delta_i`,
   `Delta`, `D` refer to that tree. ✔ automatic for any total Boolean `f`
   (the trivial tree gives `D(f) <= n`); the content is in choosing a *good*
   tree. ⚠ For a general real-valued function of degree `d` **no exact
   decision tree of small depth need exist at all** — this is the hypothesis
   that fails in the bounded/real case, and it is the reason OSSS does not
   settle Aaronson–Ambainis (card S8).
3. **Product measure.** Any product measure on the cube (p-biased), or any
   finite `n`-wise product probability space (§3). ✔ uniform is the case
   the campaign needs.
4. **No monotonicity, no balance, no degree hypothesis** anywhere in
   Theorem 1.1 or Corollary 1.2. ✔ (Monotonicity appears only in §2's
   *application* to graph properties, Theorem 2.1, via the external
   inequality (3) from [19].)
5. **`n`-free / dimension-free.** Nothing is assumed about `n`; the bound is
   in terms of `Var`, `Inf`, and the tree's query profile only. ✔ — this is
   why it is usable in a Contract whose thresholds may not depend on `N`.

---

## Conclusion in my own words

For any total Boolean function and **any** decision tree that computes it, the
function's variance is at most the query-probability-weighted sum of its
influences. Hence the *expected* number of queries of the best (even
randomized) tree is at least `Var(f)/Inf_max(f)`: a function that is hard to
compute with few queries cannot have all its influences small. Specialised:
a balanced Boolean function computable by a depth-`d` tree has a coordinate of
influence `>= 1/d`, and — combining with degree-vs-depth — a Boolean function
of real degree `deg(f)` has a coordinate of influence
`>= Omega(Var[f]/deg(f)^4)`, printed by the authors themselves.

## What it does NOT say

* **It is not a statement about bounded real-valued functions.** The clean
  inequality is false in the real-valued `rho_2` (variance) setting with an
  absolute constant: the paper's **Figure 1** (p. 10) exhibits `f : {-1,1}^3
  -> R` computed by an explicit DDT with `Var[f] = 3/2` but
  `sum_i delta_i(T) Inf_i^{rho_2}(f) = 23/16 < 3/2` [READ]. §3.4 quantifies
  the failure by a "defect" `Def_k(rho) <= k`, and Corollary 3.4 pays for it
  with `Var[f]/k^2` instead of `Var[f]/k`. The §4 open question asks whether
  the factor `k` can be replaced by a constant; Figure 1 shows it must be
  `> 1`. **Consequence for us: no OSSS variant applies to a real-valued
  degree-`d` function unless an exact decision tree for it is exhibited.**
* Nothing about **distributions over functions**, nothing about pairs of
  *cross-disjoint* sets, nothing about `ell_2`-normalized functions, nothing
  about groups other than `Z_2`. The only two-function statement is
  Theorem 3.2 / eq. (6), which bounds a **covariance** of `f` with `g` by the
  influences **of `g` alone**, weighted by the query profile of a tree
  computing **`f`** — it is not a symmetric statement and it is not an
  intersection statement.
* It gives **no upper bound** on `Inf_max`, no structure theorem, and no
  junta conclusion.
* It says nothing about `delta_i` versus `Inf_i` (the separate OSSS conjecture
  for monotone functions is not in this paper's statements above).
* The degree corollary is stated for **exact** real degree and for
  **approximate** degree of a *Boolean* `f`; it says nothing about a
  nonnegative real degree-`d` function (rung R3's setting).

## Where the campaign uses it

1. **Card S8 / question (Q).** §1.2.1's printed corollary
   `Inf_max(f) >= Omega(Var[f]/deg(f)^4)` **is** the campaign's (Q), for
   ±1-valued `f`. See S8 for the exact fit and the sharper exponent.
2. **Plan P4** (gated on this inequality): the usable form is Corollary 1.2,
   `Inf_max(f) >= Var(f)/Delta(f)` with `Delta(f) <= R(f) <= D(f)`, plus a
   degree-vs-depth bound. Hypothesis 1 is the binding one: it applies to a
   *Boolean-valued* side of a pair, not to normalized indicators as real
   functions and not to R3's level-set functions.
3. **Plan P5** may use the two-function Theorem 3.2 / eq. (6) — flagged as the
   only pair-form in the paper, with the asymmetry noted above.

### END OF CARD S9 ###
