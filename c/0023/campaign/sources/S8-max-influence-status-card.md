id: S8-max-influence-status
agent: scout (deciding-source errand, campaign c/0023, SOURCE GATE 1 for rung I02/R2)
model: claude-opus-5[1m]
cycle: 4; status: COMPLETE

# SOURCE CARD [S8] — status of the single-function question (Q): **KNOWN (a theorem)**

Discharges the deciding question of the cycle-4 gate. The question, as posed to
this scout (call it **(Q)**):

> There is a polynomial `p` such that every **balanced** Boolean function
> `f : {±1}^N -> {±1}` of degree at most `D` has some coordinate with
> `Inf_i(f) >= 1/p(D)`.

**VERDICT: (Q) IS KNOWN — proved, and printed as an explicit corollary in
[OSSS05] itself.** It is *not* open, and it is *not* the Aaronson–Ambainis
conjecture; it is the **Boolean-valued (±1-valued) case** of AA, which is the
case AA's literature repeatedly records as already settled. The open AA
conjecture is about **bounded real-valued** functions, where the proof below
provably breaks (card S9's Figure 1 and hypothesis 2).

Four blocks:

| block | content | retrieval |
|---|---|---|
| **S8a** | the theorem that settles (Q), with its exact printed form | [READ] (via card S9) |
| **S8b** | the best printed exponent, and the exponent's known bracket | [READ] + one scout computation |
| **S8c** | the AA conjecture: exact variants, which is which, and status | [READ] x3 sources |
| **S8d** | the junta + Poincaré fallback the errand asked me to verify | [READ] card S6 + scout's own arithmetic |

---

### SOURCE CARD [S8a] ### — the theorem

**Citation.** O'Donnell–Saks–Schramm–Servedio, *Every decision tree has an
influential variable*, FOCS 2005 / **arXiv:cs/0508071v1, §1.2.1, p. 4**.
Full statement, hypotheses, conventions and conversions: **card S9** — cite S9,
not this block, for the inequality itself.

**Verbatim (arXiv v1, p. 4) [READ]:**

```latex
Since D(f) \le O(\deg(f)^4) (by a result of Nisan and Smolensky [8]), our
Corollary 1.2 implies that the maximum influence in fact satisfies
    \mathbf{Inf}_{\max}(f) \ \ge\ \Omega\bigl(\mathbf{Var}[f]/\deg(f)^4\bigr).
```

Here (S9's conventions, all printed) `f : {-1,1}^n -> {-1,1}` is total and
±1-valued, `deg(f)` is the degree of its real multilinear representation,
`Inf_i(f) = Pr[f(x) != f(x ⊕ i)] = sum_{S ∋ i} fhat(S)^2`, and
`Var[f] = 4 Pr[f=1]Pr[f=-1] = sum_{S != ∅} fhat(S)^2`, which equals **1**
exactly when `f` is balanced. `[8] = Buhrman–de Wolf, Complexity measures and
decision tree complexity: a survey, TCS 288(1):21–43, 2002` (bibliography read,
p. 10).

**(Q) as a corollary, in one line.** For balanced `f`, `Var[f] = 1`, so

```latex
\max_i \mathrm{Inf}_i(f)\ \ge\ \Omega\bigl(1/\deg(f)^4\bigr)
\qquad\text{i.e. (Q) holds with } p(D)=O(D^4).
```

Nothing else is needed: the polynomial is **printed in the same sentence as
the inequality**, so no unread depth-vs-degree source is load-bearing for the
existence of *some* polynomial.

**Also printed there, and stronger than (Q) [READ]:** the same corollary with
**approximate** degree, `Inf_max(f) >= Omega(Var[f] / degtilde(f)^6)`, where
`degtilde(f)` is the least degree of a real `p` with `|p(x)-f(x)| < 1/3`
everywhere (via `D(f) <= O(degtilde(f)^6)`, credited to Beals–Buhrman–Cleve–
Mosca–de Wolf, JACM 48(4), 2001). So (Q) survives replacing "degree `<= D`" by
"*approximated to error 1/3* by a degree-`D` polynomial", at exponent 6.

**A second, independent printed attestation that (Q)-type statements are known
[READ].** Shachar Lovett, Jiapeng Zhang, *Fractional certificates for bounded
functions*, **ECCC TR22-107 (20 Jul 2022) / ITCS 2023, p. 2**:

```
The AA conjecture is known to be true for Boolean functions. Specifically, the
seminal work of Nisan and Szegedy [17] showed that for every Boolean function
f : {0,1}^n -> {0,1}, its decision tree complexity and its polynomial degree
are equivalent, up to polynomial factors. However, their proof technique does
not extend to bounded functions. In fact, many techniques used to study Boolean
functions seem to fail when attempting to extend them to bounded functions.
```

⚠ Note the *form* of AA that Lovett–Zhang call known is their Conjecture 1.1
(decision-tree **approximation**), not the influence form; the influence form
for Boolean `f` is S8a's OSSS corollary. The two forms are equivalent — see
S8c.

### END OF CARD S8a ###

---

### SOURCE CARD [S8b] ### — the best printed exponent, and the bracket

**Upper route, best printed: `p(D) = O(D^3)`.** [READ] Rahul Chugh, Supartha
Podder, Swagato Sanyal, *Decision Tree Complexity versus Block Sensitivity and
Degree*, **arXiv:2209.08042v1, p. 2** (journal version: FSTTCS 2023, LIPIcs
284:27):

```
It is known (see Table 1 in [ABDK+21]; also follows from Proposition A.16 parts
(2), (3), (4) and (5)) that for all Boolean functions f, D(f) = O(bs(f)^3) and
D(f) = O(deg(f)^3). It is also known that there exist Boolean functions g, h
such that D(g) = Omega(bs(g)^2) and D(h) = Omega(deg(h)^2).
```

Combined with card S9's Corollary 1.2 (`Inf_max(f) >= Var(f)/Delta(f)` and
`Delta(f) <= R(f) <= D(f)`): **every balanced ±1-valued `f` of degree `D` has
`Inf_max(f) >= Omega(1/D^3)`.** `[ABDK+21]` = Aaronson, Ben-David, Kothari,
Rao, Tal, *Degree vs. approximate degree and quantum implications of Huang's
sensitivity theorem*, STOC 2021, DOI 10.1145/3406325.3451047 — existence and
authorship confirmed via ACM/DBLP search results, **its Table 1 itself
[RESTATED via Chugh–Podder–Sanyal, not read]**. `D(f) = O(deg(f)^3)` is also
widely attributed to **Midrijānis 2004** — that attribution is
**[MEMORY/RESTATED via search snippets only]**; I fetched
`arXiv:quant-ph/0403168` and its abstract states a *quantum* result
(`T`-query exact quantum ⇒ `O(T^3)` deterministic), **not** the degree bound,
so **do not cite Midrijānis for `D <= 6 deg^3`** without reading it. Use
Chugh–Podder–Sanyal p. 2 (or OSSS's own `deg^4`) instead.

**Ceiling of this route: exponent 2.** The same sentence records Boolean `h`
with `D(h) = Omega(deg(h)^2)`, so `Inf_max >= Var/D(f)` cannot yield better
than `1/deg^2` in general.

**Lower bound on the truth of (Q) (SCOUT'S OWN ELEMENTARY COMPUTATION — not a
citation, verify before use).** `k`-fold read-once composition of
`MAJ_3 : {±1}^3 -> {±1}`: `MAJ_3` has `deg = 3`, `Inf_i = 1/2` for each `i`;
read-once composition multiplies both, so the composed function `f_k` on
`n = 3^k` variables is balanced, has `deg(f_k) = 3^k = D` and
`Inf_i(f_k) = 2^{-k} = D^{-log_3 2} = D^{-0.6309...}` for every `i`. Hence

```latex
\text{the true exponent in (Q) lies in } [\,\log_3 2,\ 3\,]\approx[0.631,\ 3].
```

So (Q) is a theorem, but its *exponent* is not pinned down in print; a campaign
step needing a specific exponent must use `3` (or `4`, self-contained in OSSS)
and can never hope for better than `0.631` by this family.

### END OF CARD S8b ###

---

### SOURCE CARD [S8c] ### — the Aaronson–Ambainis conjecture: which variant is which

The distinction the errand was commissioned for. **Three statements, printed
verbatim below, with status:**

```latex
% (AA-inf) THE Aaronson-Ambainis conjecture, influence form. OPEN.
% [READ] S. K. Bhattacharya, Random Restrictions of Bounded Low Degree
% Polynomials Are Juntas, ITCS 2025, LIPIcs 325:17, p. 17:3, Conjecture 4:
Conjecture 4 (Aaronson-Ambainis conjecture). Let f : \{\pm1\}^n \to [0,1] be a
degree d polynomial. Then, there exists a coordinate j such that
\mathsf{Inf}_j[f] \ge \mathsf{poly}(1/d, \mathsf{Var}[f]).

% (AA-dt) The decision-tree-approximation form. OPEN, and EQUIVALENT to AA-inf.
% [READ] same paper, p. 17:2, Conjecture 3:
Conjecture 3. Let P : \{\pm1\}^n \to [0,1] be a degree d polynomial. For any
\epsilon > 0, there exists a classical decision tree T of depth at most
\mathsf{poly}(d,1/\epsilon) such that \mathbb{E}[(P(x)-T(x))^2] \le \epsilon.

% (Q) the campaign's question. A THEOREM (card S8a).
% Every balanced f : \{\pm1\}^N \to \{\pm1\} with \deg f \le D has
% \max_i \mathrm{Inf}_i(f) \ge 1/p(D), p(D) = O(D^3).
```

**The equivalence of the two AA forms is printed [READ]** (Bhattacharya,
p. 17:3): "*As a side remark, we mention that O'Donnell et al. [18] had shown
previously that functions which can be approximated by decision trees have a
coordinate with high influence. So conjectures 3 and 4 are equivalent.*"
([18] = OSSS; the relevant OSSS statement is card S9's Theorem 3.2 /
approximation consequence on p. 8.)

**Exact logical relation of (Q) to AA.**

* **AA ⇒ (Q)** — SCOUT'S OWN ONE-LINE CHECK, elementary, not printed: given
  balanced ±1-valued `g` of degree `D`, put `f = (1+g)/2 : {±1}^N -> {0,1}
  ⊂ [0,1]`, still degree `D`, with `Var[f] = Var[g]/4 = 1/4` and
  `Inf_j[f] = Inf_j[g]/4`; (AA-inf) then gives
  `Inf_j[g] = 4 Inf_j[f] >= 4 poly(1/D, 1/4) = 1/poly(D)`.
* **(Q) does NOT imply AA**, and (Q)'s being a theorem is *no* evidence that
  AA is close: AA has been open since 2008/2009 *with* (Q) known throughout.
  So **(Q) is STRICTLY WEAKER than AA**: it is AA's Boolean-valued,
  variance-1 special case.
* Therefore the campaign's earlier framing (`0023-scout-1` §B4, Contract K4)
  is refined, not contradicted: *AA is open in the bounded real-valued regime;
  its ±1-valued case is a 2005 theorem.* The kinship marker "open since 2009"
  applies to AA, **not** to (Q).

**Status of AA itself, re-confirmed this sweep (all [READ]).**
* Open. Bhattacharya, p. 17:3, surveys: DFKO06 gives the conjecture with
  `poly(d)` replaced by `exp(d)`; Montanaro 2012, equal-magnitude
  block-multilinear forms; O'Donnell–Zhao 2016, reduction to one-block
  decoupled polynomials; **"In 2020, Keller and Klein claimed to have found a
  proof for the conjecture but their paper had a subtle flaw and turned out to
  be wrong"**; Lovett–Zhang, fractional block sensitivity / fractional
  certificate complexity; Bansal–Sinha–de Wolf 2022, completely bounded
  block-multilinear forms. Bhattacharya's own Theorem 5 is the random-
  restriction (for-most-restrictions) result.
* Aaronson's own statement of AA is for `p` with `p(x) ∈ [0,1]` on the cube
  ("*there must be some variable i such that `Inf_i(p) >= poly(Var(p)/d)`*"),
  and the post records the Keller–Klein retraction "*because of what currently
  looks like a fatal flaw in Lemma 5.3, uncovered by Paata Ivanishvili*"
  — [READ] `scottaaronson.blog/?p=4414` (rendered text via fetch; a blog, so
  citable only as provenance for the retraction, not as a theorem source).
* Lovett–Zhang, ECCC TR22-107 p. 2, Conjecture 1.1, is the `{0,1}^n -> [0,1]`,
  `E|f - T|`-error variant of (AA-dt). [READ]

**⚠ Two traps a downstream artifact must not fall into.**
1. **The variance factor.** AA's conclusion degrades with `Var[f]`; (Q) has no
   variance factor because balanced ±1-valued means `Var = 1` exactly. A
   claim "(Q) with `Var(f)` in the numerator, for real-valued `f`" is AA, i.e.
   **open**, not S8a.
2. **Value range is the whole difficulty.** ±1-valued (or `{0,1}`-valued) is
   settled; `[0,1]`-valued is open. Card S9's Figure 1 shows the OSSS
   inequality *itself* fails (with constant 1) for real-valued functions in
   the variance semimetric, and S9 hypothesis 2 (an exact decision tree must
   exist) is what a bounded real degree-`d` function need not satisfy. Any
   campaign step that "lifts" S8a to real-valued functions is attacking AA.

### END OF CARD S8c ###

---

### SOURCE CARD [S8d] ### — the junta + Poincaré fallback: CORRECT, but superseded

The errand asked me to verify or correct the expected fallback bound. **The
reasoning is correct and gives `2^{-D-O(1)}`; it is simply far weaker than
S8a.** Assembly (arithmetic is the scout's own; both inputs are carded):

1. Balanced ±1-valued `g` ⇒ `sum_{S != ∅} ghat(S)^2 = Var(g) = 1`, and
   `sum_i Inf_i(g) = sum_S |S| ghat(S)^2 >= sum_{S != ∅} ghat(S)^2 = 1`
   (Poincaré; also `<= D` by I02's free fact).
2. `g` depends on at most `4.394 * 2^D` coordinates — **card S6c** [READ]
   (Wellens, Discrete Analysis 2022:19, Thm 1.1 (1.3)).
3. Averaging: `max_i Inf_i(g) >= 1/(4.394 * 2^D) = 2^{-D-2.14...}`.

So the *junta* route caps at `2^{-Theta(D)}` — as card S6's "deeper barrier"
paragraph already predicted — and the prover's remark in
`0023-prover-2.md` T5(c) that "the object the refutation needs sits within a
constant factor of the junta bound's extreme" is correct **but the object does
not exist**, because S8a rules it out at `1/poly(D)`, exponentially above
`2^{-D}`. **Gap between the two printed bounds: `2^{-D}` (junta route) versus
`Omega(D^{-3})` (OSSS route) — a full exponential.** Any future artifact
reaching only `2^{-Theta(D)}` on a single-function max-influence question is
not at the state of the art.

### END OF CARD S8d ###

---

## Where the campaign uses this card

Cited against `0023-prover-2.md` §T5 and gap register G-1/G-2, and against
plans P1/P4/P5.

1. **The prover's refutation shape T5(c) is DEAD (as a *shape*).** T5(c) is
   conditional on: "for infinitely many `D` there is a balanced
   `g : {±1}^m -> {±1}` with `deg g = D` and
   `mu(g) = max_j Inf_j(g) <= 2^{-cD}`". By **S8a** no such `g` exists for any
   `c > 0` once `D` is large (`mu(g) >= Omega(D^{-3})`). So the hypothesis of
   T5(c) is **unsatisfiable**: (PAY★★) cannot be refuted this way.
2. **T5(c′)'s necessary condition is discharged.** T5(c′) proves
   `(PAY★★) ⇒ (Q)`. Since (Q) is a theorem, T5(c′) exposes **no**
   obstruction to (PAY★★): the campaign was gated on a statement that is
   *true and printed*. ⚠ This does **not** prove (PAY★★) — the implication
   runs the wrong way, exactly as the prover's G-2 declares.
3. **On the `H(k,g,Delta)` family shape, the payment is inverse-polynomial**
   — ORCHESTRATOR-FACING CONSEQUENCE, elementary but **NOT verified here; a
   prover must redo it**. The prover's dichotomy (i) says: if
   `mu(g) >= 4 tau` then `pi >= 2 tau`. By S8b, `mu(g) >= c/D^3 >= c/d^3`
   (using `D <= d` in that construction), so choosing
   `tau(d) := c/(4 d^3)` puts every instance of the shape in branch (i), with
   payment `pi >= c/(2 d^3) = 1/poly(d)`. Branch (ii) (all coordinates
   `tau`-light with `mu(g)` exponentially small) is now **empty**.
4. **Plan P4** is unblocked: its gating inequality is card **S9**, now held,
   with its binding hypothesis identified (Boolean-valued side, exact decision
   tree). **Plan P5** may use S9's two-function Theorem 3.2 / eq. (6).
5. **R3 warning (I02's generalization hypothesis).** S8a is a *Boolean-valued*
   theorem and the value range is precisely where AA is open; a technique
   built on S8a/S9 does **not** automatically survive to R3's nonnegative
   real-valued level-set functions. Flag any such step as an AA-adjacent step.

## What this card does NOT say

* It does not say (PAY★★) holds, nor that R2 holds.
* It does not give a bound for **average-over-a-distribution** influence
  (R2's hypothesis is `E_{f~F}[Inf_i(f)] <= delta(d)`); S8a is per-function.
* It does not apply to `{0,1}`-valued *indicators viewed as real functions*
  after `ell_2` normalization: the ±1-valued hypothesis is on the function's
  *value set*, and `1_A/||1_A||_2` is `{0, alpha^{-1/2}}`-valued (two values,
  so affinely equivalent to ±1-valued — ✔ — but the *balanced* hypothesis then
  means `alpha = 1/2`; for sparse `A` use `Var(1_A) = alpha(1-alpha)`, giving
  `Inf_max(1_A) >= Omega(alpha(1-alpha)/D^3)` in `{0,1}` normalization).
  This last inequality is the scout's own transcription of S8a and is
  **unverified**.
* It settles nothing about AA, and nothing about non-`Z_2` groups.
* It does not pin the exponent (S8b: bracket `[0.631, 3]`).

### END OF CARD S8 ###
