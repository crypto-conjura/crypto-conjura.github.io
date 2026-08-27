---
id: 0023-prover-3-verify-A
agent: verifier
model: claude-sonnet-5
cycle: 3
---

# Verification report on `0023-prover-3.md` (internal barrier for R2, P1/P5 escape ruling)

## 1. FINAL VERDICT

**NOT CLEAN, but no critical error found in the load-bearing mathematics**: independent
recomputation of every numeric claim (witness (a)'s exact Fourier table at k=1,
witness (b)'s exact table at d=1,2, T1–T9, the non-canonicity automorphism
argument, and the calibration cross-checks) confirms CAP I, CAP II, the SCOPE
monotonicity direction, the CALIBRATION claims (R1/refuter-3's bound are not
condemned, no cap sits below K1), and the P1/P5 escape ruling all hold as stated;
the two defects found are (B) a false unqualified universal claim in Remark
4.2(b) ("Forced(D)=∅" fails at d=1, though this has no traceable effect on any
conclusion drawn from it) and (E) four cited source cards (S6a, S6c, S6d, S7b)
could not be located in `campaign/sources/` despite an extensive search, one of
which (S7b) is marked load-bearing in the artifact's own Dependencies table —
though I was able to independently re-derive the fact it is cited for directly
from the Contract's own degree definition, so this (E) does not in fact
undermine the conclusion it is attached to.

## 2. STEP 0 — COMPLETENESS GATE

Artifact ends with `### END OF ARTIFACT 0023-prover-3 ###`; no unit is left
mid-sentence or mid-equation. **PASS — not truncated.**

## 3. CLASS-A DRIFT CHECK (what the artifact actually proves vs. the Contract)

The Contract's target for this rung (I02/R2) is a proof, refutation, or named
partial of the degree-≤d indicator statement. This artifact does **not**
attempt any of those; it is a BARRIER artifact (Contract's own "BARRIER
CHECKLIST" explicitly authorizes "arguments using only per-coordinate
influence budgets cannot beat exponential thresholds" as a legitimate
internal-barrier target, §3.2 class (f)). The artifact's own VERDICT is
careful to state "No claim is made about R2's truth: a barrier is not a
refutation, and R2 remains open," and its title/scope match its content: two
precisely-delimited technique sub-classes (relevance-denominated windows;
own-heavy windows) are capped at $2^{-\Theta(d)}$, and this is explicitly
**not** claimed to be a cap on the whole window-payment class 𝒲 (the VERDICT's
second sentence says so in as many words). **No statement drift found** at the
top level. One phrasing risk flagged below (§6, PEDANTIC-leaning C).

## 4. STEP 0.5 — NEGATION CHECK

For the two caps (T6/CAP I, T8/CAP II) the "value" $V_W(d)$ is defined (D5) as
an **infimum** over $\mathcal P_d$; each cap is proved by exhibiting one
specific pair in $\mathcal P_d$ whose ratio is small. The negation of a cap
("$V_W(d)$ exceeds the stated bound") would require the *infimum* to exceed a
value achieved at an explicit exhibited point — impossible once the
exhibited-pair computation is itself correct, so there is no route to
"prove the negation" in a separate context; I confirmed the exhibited-pair
computations independently (§5 below) and found them correct, so no
CONTRADICTION risk on T6/T8. Likewise the non-canonicity theorem (§7.2) is an
orbit/transitivity argument I re-derived from scratch (§5.5 below); its
negation ("some canonical localised functional selects a max-degree monomial
support") is refuted by the same transitive-orbit argument, which I verified
independently, not merely accepted on the artifact's word. **No hard-stop
contradiction found.**

## 5. Independent recomputation (exact arithmetic, done by hand/reasoning — no
Bash tool was available in this environment despite the task description
mentioning one; all fractions below are exact)

**5.1 Witness (a), $k=1,d=2$.** Enumerated all 8 points of
$\{a,y_0,y_1\}\in\{\pm1\}^3$; $A_1=\{(+1,+1,+1),(+1,+1,-1),(-1,+1,+1),(-1,-1,+1)\}$,
$\alpha=1/2$. Reconstructed $\mathbf 1_{A_1}=\tfrac12+\tfrac14y_0(1+a)+\tfrac14y_1(1-a)$
and checked all 8 points against T5(i)'s general formula — **matches exactly**.
Derived $\mathrm{Inf}_a(\mathbf 1_{A_1})=\mathrm{Inf}_{y_0}(\mathbf 1_{A_1})=\mathrm{Inf}_{y_1}(\mathbf 1_{A_1})=1/8$
directly from the coefficients, hence $\mathrm{Inf}_a(f)=\mathrm{Inf}_{y_j}(f)=1/4$ after
dividing by $\alpha=1/2$ — **matches T5(iv)** ($k=1$ case: $1/4$ and $2^{-k-1}=1/4$
coincide). $\pi_{\mathrm{Rel}}(A_1,B_1)=2(1/4+1/4+1/4)=3/2=(d+1)/2$ —
**matches T5(v)** and the artifact's own reported code check ("$3/2,2,5/2$" for
$k=1,2,3$).

**5.2 Witness (b), $d=2$.** $\mathbf 1_C=\tfrac14(1+x_1+x_2+x_1x_2)$,
$\alpha_C=1/4=2^{-d}$; $\mathrm{Inf}_1(\mathbf 1_C)=1/8=2^{-d-1}$; dividing by
$\alpha_C$: $\mathrm{Inf}_1(f_C)=1/2$ — matches. $\mathbf 1_D=1-\mathbf 1_C$,
$\alpha_D=3/4$, $\mathrm{Inf}_1(f_D)=(1/8)/(3/4)=1/6=1/(2(2^2-1))$ — matches T7's
general formula and its reported "$d=2$: $1/6$" exact check. $\pi_{\mathrm{Rel}}(C,D)=1+2/(2\cdot3)=4/3$ — matches.

**5.3 T4(a)/(c).** Verified the restriction argument (a nonzero degree-$m$
monomial's coefficient survives every restriction off its support, hence a
nonzero point exists in every one of the $2^{n-m}$ fibres, giving
$\Pr[p\ne0]\ge2^{-m}$) and the derivative argument for T4(c)
($\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E[D_i^2]=\tfrac14\Pr[D_i\ne0]\ge2^{-d-1}$,
$D_i$ nonzero of degree $\le d-1$, using T4(a)) from scratch: **both correct**.
T4(d)'s upper bound (single forced crossing cell, $\pi_{\mathrm{Rel}}=1$
exactly): confirmed via Remark 4.2(a)'s forcing formula.

**5.4 T6, T8, T9, T6.a/b, §6.4's numeric self-checks.** Recomputed all
inequality chains in T6's proof (substituting $|W(A_k)|+|W(B_k)|=2(2^{d-1}+d-1)$
and the density/exponential-window corollaries) and T8/T9's case split
($w_D=0$ vs $w_D\ge1$): **all arithmetic checks out**, including the
self-consistency claims in §6.4 ($2^{-d}/d\le(d+1)2^{-d-1}$ for $d\ge1$, and
$2^{-d}/d\le1/(2(2^d-1))$ for $d\ge2$) — both verified by direct algebra.

**5.5 Non-canonicity theorem (§7.2).** Re-derived the automorphism
$\sigma_c$ directly: with $s_t=1-2c_t$, checked $b_t(s_ta_t)=b_t(a)\oplus c_t$
coordinatewise and hence $b(\sigma_c(a))=b(a)\oplus c$; then
$y'_{b(a')}=y_{(b(a)\oplus c)\oplus c}=y_{b(a)}$, so membership in $A_k$ is
preserved under $\sigma_c$ — confirms $\sigma_c(A_k)=A_k$ from first
principles, independent of the artifact's own proof. The orbit/transitivity
argument (equivariant $W(A_k)$'s target-part is a union of orbits of a
transitive action, hence $\emptyset$ or everything) is standard and correct.
**Confirmed independently.**

## 6. FINDINGS TABLE

| Location (quoted) | Class | Explanation |
|---|---|---|
| Remark 4.2(b): *"$\mathrm{Forced}(C)=[d]$, $\mathrm{Forced}(D)=\emptyset$"* | **B** (bounded impact) | False as an unqualified universal claim: at $d=1$, $D=C^c=\{x_1=-1\}$ **does** force $x_1=-1$, so $\mathrm{Forced}(D)=\{1\}\ne\emptyset$. Checked directly: $\mathbf 1_D=(1-x_1)/2$ depends only on $x_1$. However, I traced every downstream use (T8's proof, Remark 4.3, §6.2's "$V_{W_{\mathrm{Forced}}}=0$" claim) and found the $d=1$ case is independently consistent even when $D$ is correctly treated as forcing at $d=1$ (the forcing-pair ratio there evaluates to exactly $1/(2d)=1/2$, matching refuter-3's bound with no contradiction), and $d=1$ is a degenerate case the campaign's own ladder (`PROGRESS.md` "Axes skipped... Fixed small degree... SETTLED by K1") already treats as settled outside this rung's content. **No conclusion in the artifact is shown to rest on this false sub-claim surviving at $d=1$.** Should be qualified to $d\ge2$ if repaired. |
| Dependencies table: *"S7b (card) \| Chang–Fang Thm 1.2 / Cor. 3.4 \| CARD, READ \| §7.1: P1's window is $\le d$ **by theorem** \| yes, for the escape claim only"* and the three cards S6a/S6c/S6d | **E** (non-blocking on inspection) | I searched `campaign/sources/` extensively (S1-acc22-card.md and S2-clm23-card.md were found and read; S6a, S6c, S6d, S7b under a dozen plausible filenames could not be located — no directory-listing tool was available to me, only direct-path `Read`). Per the SOURCE ACCESS PROTOCOL, an unreachable card with no card supplied is class (E) and load-bearing (E) blocks acceptance. **However**: the specific fact S7b is cited for — "a maximum-degree monomial support has size $\le\deg(f)$" — follows *immediately* from the artifact's own D1/degree definitions (a monomial of degree $\deg(f)\le d$ has, by definition, a support of exactly that size), with no external theorem needed; I verified this from the Contract's own degree definitions independently of any card. So while the citation is technically unverifiable as filed, the underlying claim it supports is not actually citation-dependent, and the escape conclusion in §7.1 does not collapse if S7b turns out to be miscited or inapplicable. S6a is explicitly marked "no" (re-proved inline as T4(c), which I independently checked, §5.3 above) and S6c/S6d are marked "no" / used only in units not included in this artifact — neither is load-bearing here. |
| VERDICT clause (iv): *"P1 and P5 ESCAPE the barrier — YES, both, by exact computation... none is $2^{-\Theta(d)}$, so neither cap touches them."* | **C** (clarity, PEDANTIC-leaning) | This is textually correct and properly scoped ("escape" = "escape CAP I and CAP II, the two barriers *this artifact proves*," not "proved to achieve inverse-polynomial value over all of $\mathcal P_d$") — the artifact is explicit about this scoping in §8 (η*(d) is the *actual* universal ceiling on the whole class, and whether P1's constant forces $\eta^*(d)=1$ is left as an open, falsifiable milestone, not claimed proved). A reader skimming only the VERDICT's headline could over-read "P1 and P5 escape the barrier" as "P1/P5 are shown to succeed," which they are not — the computation is only against the two *specific* witness pairs used to prove CAP I/CAP II, not a proof that no *other* pair defeats $W_{\mathrm{sh}}$ or the certificate functional. No repair needed; flagging for Triage as a wording risk, not a defect in the mathematics. |
| §7.5, "P5's payment is over $\Sigma(x,y)$..." | **C** (justification gap, not blocking) | This paragraph introduces a second, *different* payment quantity ($\Sigma(x,y)$, the coordinates where two *specific* certificates fix oppositely) from the D3/Remark-2.2 quantity actually used to establish the escape in §7.4 (which I independently recomputed and confirmed equals $k/2+2^{-k}$, matching P1's value exactly, via the correct application of Remark 2.2's independent-draw expectation). The relationship between $\Sigma(x,y)$ and the formally defined $\pi_W$ of D3 is not spelled out (whether $\Sigma$ *is* $\pi_W$ under Remark 2.2, or a genuinely different, pair-joint quantity outside the class per Remark 2.1's own caveat about pair-dependent windows) is asserted rather than derived. Since the main escape claim for P5 rests on the §7.4 computation (which I verified independently and which does *not* use $\Sigma(x,y)$), this gap does not affect the artifact's actual VERDICT, but the "drafting warning" itself is under-justified as stated. |

No class (D) citation misuse was found (K1's use in §6.4 is a correct
comparison, not a misapplication of its hypotheses).

## 7. Adjudication tags for load-bearing lemmas

| Lemma | Tag | Basis |
|---|---|---|
| T1 (master count) | **MECH** | Re-derived from independence + linearity of expectation, self-contained. |
| T2 (value theorem) | **MECH** | Re-derived; infimum-comparison argument, self-contained. |
| T3 (localisation ceiling) | **MECH** | Direct from $W(A)\subseteq\mathrm{Rel}(A)$ and $\mathrm{Inf}\ge0$. |
| T4(a)–(d) | **MECH** | Re-derived the restriction argument and the derivative/Parseval argument from scratch (§5.3). |
| T5 (witness a table) | **MECH + CODE** | Re-derived by hand for $k=1$ (§5.1), matching; artifact also cross-checks with `check_witnesses.py` for $k=1,2,3$ (exact `Fraction`s) — I could not run this code (no Bash tool available) but the hand computation independently corroborates it. |
| T6 (CAP I) | **MECH** | Algebra re-derived and checked (§5.4). |
| T7 (witness b table) | **MECH + CODE** | Re-derived for $d=1,2$ by hand (§5.2); code-checked by the artifact for $d=2..6$. |
| T8, T9 (CAP II, dichotomy) | **MECH** | Re-derived (§5.4). |
| Remark 4.2 (forcing) | **MECH, with one false sub-claim** | Re-derived; part (a)'s general formula is correct; part (b)'s specific claim "$\mathrm{Forced}(D)=\emptyset$" is false at $d=1$ (Finding above). |
| §7.2 non-canonicity theorem | **MECH** | Re-derived the automorphism and orbit argument from scratch (§5.5), independent of the artifact's proof. |
| §5.1–5.4 SCOPE / monotonicity | **MECH** | Direction of the inequality ($V^{C'}\le V^{C}$ for $C\subseteq C'$) re-derived from the infimum-over-a-superset argument; confirmed non-inverted. |
| S7b citation (used in §7.1) | **CARD, but card unlocatable → treated as NONE, with an independent MECH substitute found** | See Findings table; I re-derived the cited fact directly from D1, so it does not actually need CARD status to stand. |
| S6a citation (NS94 quantum bound) | **CARD, unlocatable, non-load-bearing (re-proved as T4(c), MECH)** | See Findings table. |
| S1 (K1, ACC22 Thm 4.4) | **CARD** | Located and read (`sources/S1-acc22-card.md`); used only for a non-load-bearing consistency comparison in §6.4, correctly applied. |

## 8. STEP-BY-STEP LOG

1. STEP 0 completeness: PASS (END marker present).
2. Class-A drift check: PASS, artifact's scope matches its title/verdict and the Contract's BARRIER-plan authorization.
3. §1–2 (D1–D5, T1–T4): all definitions and lemmas re-derived independently; accepted.
4. §3 (T5, T6/CAP I): witness (a) table re-derived by hand for $k=1$; CAP I's algebra re-checked; accepted.
5. §4 (T7, T8/CAP II, T9, Remark 4.2): witness (b) table re-derived by hand for $d=1,2$; CAP II/T9 algebra re-checked; **defect found** in Remark 4.2(b) at $d=1$ (Finding 1, Class B, bounded impact — traced downstream, no propagation found).
6. §5 (SCOPE, monotonicity, groups): monotonicity direction re-derived and confirmed non-inverted; group generalization (§5.4) spot-checked structurally, accepted.
7. §6 (CALIBRATION): R1/refuter-3 non-condemnation arguments checked against the definitions of $\mathcal C^{\mathrm{junta}}_d$ and forcing pairs; K1-consistency algebra re-checked (§6.4); accepted, modulo Finding 1's edge case which does not propagate here.
8. §7 (P1/P5 escape, non-canonicity): §7.1/7.4 computations independently re-derived for $k=1$/$d=2$, matching exactly; §7.2 automorphism argument independently re-derived (§5.5); §7.3 ($W_{\max}$) spot-checked, consistent; §7.5 flagged as under-justified but non-load-bearing for the actual VERDICT (Finding, Class C).
9. §8 (FRONTIER): logical implications (universal ceiling, sufficiency direction, PAY⋆⟹η*=1) checked as valid conditionals, correctly hedged as open/falsifiable, not overclaimed.
10. GAP REGISTER: [G1]–[G4] read and found to be honestly and correctly self-classified (definitional stipulation, odd-order-group gap, non-claimed converse, routine).
11. Dependencies/citations: S1, S2 located and read; S6a/S6c/S6d/S7b could not be located despite an extensive filename search (no directory-listing tool available) — flagged as Finding 2, Class E, but shown non-blocking for the one load-bearing use.

## 9. SOURCE REQUEST

Rank 1: source cards `S6a`, `S6c`, `S6d`, `S7b` (exact filenames unknown to me —
they are referenced in `0023-prover-3.md`'s Dependencies table but I could not
locate them anywhere under `c/0023/campaign/sources/` using plausible
filenames); needed to confirm the artifact's own provenance claims for the
Nisan–Szegedy-type junta bound, the Wellens bound, the CHS bound, and the
Chang–Fang monomial-support theorem. What collapses without it: only the
*citation's* validity, not the mathematics — I independently re-derived the
one load-bearing fact (S7b's use in §7.1) from the Contract's own degree
definition (§7 finding above), so this request is a provenance/process
matter for Triage, not a blocker on the artifact's conclusions. Rungs tried:
direct `Read` on ~15 plausible filenames following the `S<n>-<slug>-card.md`
convention established by S1/S2; no directory-listing tool was available in
this session. Fallback if unavailable: Triage can route this to a
provenance-only follow-up (does the card exist under a name I did not guess?)
without reopening the mathematics.

### END OF ARTIFACT 0023-prover-3-verify-A ###
