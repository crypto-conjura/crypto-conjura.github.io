# CAMPAIGN LEDGER: c/0023
## Polynomial Compatibility Conjecture (PCC), inverse-polynomial influence regime

**Campaign:** c/0023 — depth 0 — contract: `CONTRACT.md`  
**Cycle:** 1 (scaffold + reconnaissance) · **Closed:** 2026-08-27  
**Harness:** `prompts/solve.md` (this repository's HARNESS.md)  
**First screenful orientation:** This ledger captures cycle 1's complete scaffold: Scout verdict (NO PRIOR RESOLUTION FOUND, 2026-08-27), six strategist plans P1–P6 ranked by information-per-effort, case ladder R0–R6 ready for human approval, and computationally verified refutation boundaries. No proof attempted; all inputs to first materalised rung I01 (R1, spread-junta indicator) await approval.

---

## ESTABLISHED

(none — no artifact has entered the verification loop)

## VERIFICATION TALLY

| Cycle | Pass | RAW verdict | POST-TRIAGE verdict |
|-------|------|-------------|---------------------|
| (none) | — | — | — |

## CONDITIONAL

### R1: Strategist occupancy-density reformulation (unverified, strategist-level)
**CID:** `e6e7c2a9a8f` · **Source:** 0023-strategist-1 §0, R1  
**Statement:** For finitely supported 𝐅 put μ_𝐅(x) := E_{f←𝐅}[|f(x)|²]. Then μ_𝐅 ≥ 0, E μ_𝐅 = 1, deg μ_𝐅 ≤ 2d, and ∪_{f∈supp 𝐅} supp(f) = supp(μ_𝐅). Hence **(𝐅,𝐆) incompatible ⟺ μ_𝐅 · μ_𝐆 ≡ 0** (disjoint union-supports).  
**Verification tally:** none (strategist-level; requires prover validation before load-bearing use).

### R2: Strategist coefficient-lightness reformulation (unverified, strategist-level)
**CID:** `f7b8d3c0a9e` · **Source:** 0023-strategist-1 §0, R2  
**Statement:** For every χ ≠ 0 with live coordinate i, |μ̂_𝐅(χ)| ≤ 2·E_f[√(Inf_i(f))] ≤ 2√δ. Incompatible families are densities with **individually tiny** nonconstant Fourier coefficients — but their Fourier ℓ¹ mass is uncontrolled.  
**Verification tally:** none (strategist-level; reformulation only).

### R3: Strategist density-operator reformulation (unverified, strategist-level)
**CID:** `a2d1e5f4b9c` · **Source:** 0023-strategist-1 §0, R3  
**Statement:** A distribution 𝐅 enters hypotheses and conclusion only through M_𝐅 := E_f[|f⟩⟨f|], a PSD unit-trace operator on V_d. **PCC ⟺ for every pair M, M′ of PSD unit-trace operators on V_d with Tr(M L_i), Tr(M′ L_i) ≤ δ(d) for all i, the point-basis diagonals have intersecting supports.** Corollaries: supports of size ≤ dim V_d ≤ (N|𝒴|)^d are WLOG; the problem is a finite SDP-feasibility question for each (d, N); this is precisely ACC22 Conjecture 4.3's state form made finite-dimensional-explicit.  
**Verification tally:** none (strategist-level; reformulation only).

---

## COMPUTATIONALLY CERTIFIED (unverified as proofs)

All results below are computational artifacts from 0023-refuter-1 (cycle 1, Claude-fable-5, exact rational arithmetic where certificates are noted). These are **certified** algorithmic discoveries, not yet **verified** as theorems; they become ESTABLISHED only after passing the verify loop (§3.5, five clean passes). They are cited here as factual statements about the refutation frontier: what must be true of any counterexample if PCC is false. Record them to decouple refuter discovery from proof verification.

### **Theorem R-1 (refuter-proved, exact, ε*(1,N;ℤ₂) = 1/2 for every N)**
**Source:** 0023-refuter-1 §2, Computation C1  
**Statement:** Over ℤ₂, at degree d=1, for every N the exact value ε*(1,N) (the minimum of the maximum per-coordinate average influence over all incompatible pairs) equals **1/2, independent of N**. No N-decay at the bottom rung.  
**Proof method:** Theorem (four-part argument: classification of degree-≤1 functions with exactly-half zero sets; for incompatible pairs, both sides forced to one-dimensional form; every such unit function has some Inf_i = 1/2). Exhaustive verification over N=1,2,3,4 (all partitions, cube-symmetry orbits). ℤ₃ probe: ε*(ℤ₃,1,1)=2/3, ε*(ℤ₃,1,2)=0.500... also showing no group advantage at d=1.  
**Rigidity:** All feasible partitions at each N match the theorem; the mechanism (one-dimensional supports forced) admits no exceptions.

### **Grid-pair construction confirmed (exact, ε*(𝒴,d) = (1−1/|𝒴|)/d)**
**Source:** 0023-refuter-1 §3  
**Statement:** For any finite abelian group 𝒴 and any d, the d×d grid/row-column construction (f_r = ⊗_c (1+x_{r,c})/2^{d/2}, g_c = ⊗_r (1−x_{r,c})/2^{d/2}, distributions uniform over rows/columns) achieves per-coordinate average influence exactly **1/(2d)** on both sides over ℤ₂, and **((1−1/|𝒴|)/d)** over general 𝒴.  
**Verification:** Two independent exact methods for ℤ₂: pointwise enumeration + Walsh–Hadamard (d≤4), combinatorial coefficient argument (d≤8). ℤ₃ verified to 1e−12. Consequence: any witnessing δ must satisfy **c₂ ≥ 1** (every group).

### **The 1/5 frontier at d=2, N=4 (exact, ε*(2,4)=1/5)**
**Source:** 0023-refuter-1 §4.1  
**Statement:** Exhaustive SDP over all 221 partition orbits of {±1}⁴ at d=2 reveals a minimum influence value of exactly **1/5** (rational certificate). The extremal pair is singleton-supported:  
```
f = (2 + x₁ + x₂ + x₃ + x₄ + x₂x₃ + x₁x₄)/√10
g = −(x₁ + x₄ − 2)(x₂ + x₃ − 2)/6
```
Both have degree 2, unit norms, f·g≡0 at all 16 points, Inf_i(f)=1/5, Inf_i(g)=1/6 for all i. Dual PSD certificates prove no distribution on either side beats 1/5. **K2's printed ceiling 1/(2d) is not tight; the refutation frontier lies strictly below it.**

### **Block-family record 4/11 (exact, asymptotic ε*(d) ≤ (4/11+o(1))/d)**
**Source:** 0023-refuter-1 §4.2  
**Statement:** Family: m blocks of b coordinates, f = Σⱼ 1_{marked_j} (degree b), g = ∏ⱼ (Σ_block x − b)/√(b+b²) (degree m), d=max(b,m). Exact influences: Inf_i(f) = 1/(2m(1+(m−1)2^{−b})), Inf_i(g) = 1/(b+b²), value V(b,m) = max of the two.

| seed (b,m) | d | N | value | d·value |
|---|---|---|---|---|
| (1,1) | 1 | 1 | 1/2 | 1/2 |
| (2,2) | 2 | 4 | 1/5 | 2/5 |
| (3,3) | 3 | 9 | 2/15 | 2/5 |
| (3,4) | 4 | 12 | 1/11 | **4/11** |

Sweep over (b,m) with b≤7, m≤24: minimum ratio **4/11≈0.3636** at (3,4) and (4,7); for large d drifts back toward ~0.43. SDP probes with degree slack: union side (3,4) partition averages down to 0.0908688 (float); product side pinned exactly at 1/12. **Composition preserves ε·d exactly — cannot improve the rate.**

### **Transport ceiling (exact, ε*(ℤ₂,4D) ≤ 1/(11D))**
**Source:** 0023-refuter-1 §4.3  
**Statement:** Transport lemma. Given an incompatible pair (f,g) on ℤ₂^n, deg≤d₀, influences≤(a,b), on a D×D grid of n-coordinate blocks: f_R = ⊗_C f, g_C = ⊗_R g with 𝐅,𝐆 uniform over rows/columns. Norms stay 1, degrees→D·d₀, per-coordinate influence→(a/D, b/D) (conflict preserved in block (R,C)). Corollary: **ε*(ℤ₂,4D)≤1/(11D)**, i.e., ε*(d)≤(4/11+o(1))/d. Every even-order group inherits via pullback; every group has ε*=O(1/d) by grid.  
**Verification:** Exact at D=2 with 1/5 seed (d=4, N=16, influences 1/10, 1/12).

### **The obstruction (refuter-diagnosed, not a theorem)**
**Source:** 0023-refuter-1 §5  
**Statement (diagnostic):** Three independent walls hit every construction searched:
1. **(O1) Conflict localization / union bound.** Within subcube-indicator distributions, every incompatible pair has max per-coordinate average influence ≥ 1/(2d); the grid is extremal. Proof: incompatibility means certain-conflict; two subcubes conflict iff some shared coordinate forced opposite; union bound gives 1≤2δ·E|T|≤2δ·d.
2. **(O2) The union/product asymmetry.** Sub-1/(2d) gains come from union side (quadratic per-coordinate influence decay), but partner forced into product-form (degree grows linearly, influence constant 1/(b+b²)). Balancing optimizes at small b, yielding plateau 2/5→4/11. Within all block architectures, ε·d bounded below by absolute constant; no choice reaches o(1/d).
3. **(O3) Boolean impossibility.** Boolean-derived pairs (1±σ)/√2 have value max_i Inf_i(σ)/2; OSSS + decision-tree-depth bounds give Var≤(max Inf)·poly(d), so Boolean pairs provably 1/poly-bounded — cannot certify falsity. Counterexample if it exists must be essentially non-Boolean (spiky nonnegative densities, the regime where AA-kin open since 2009).

Together: expected profile if ε*(d)=Θ(1/d) and **the conjecture is TRUE with c₂=1**.

---

## DEAD PLANS

(none)

## OPEN GAPS

1. **K1/K2/K3/K3′ source pins (CONTRACT.md, confirmed 2026-08-27):**
   - **K1** [CONFIRMED — source card S1]: [ACC22] Theorem 4.4 (p. 20) proves the conjecture's analogue with strict threshold δ < |𝒴|^{-d}/d for every finite abelian group; proof (§5.2) uses no influence bound on 𝐅 and no degree bound on 𝐆.
   - **K2** [CONFIRMED for ℤ₂ — source card S1]: [ACC22] Claim B.3 (p. 41): NegRow/PosCol pair on d×d Boolean variables has degree d, all relative influences ≤1/(2d), singleton supports, and f·g≡0. Printed for ℤ₂ only; any witnessing δ must satisfy δ(d)<1/(2d) over ℤ₂, hence effectively c₂≥1 for ℤ₂.
   - **K3** [CONFIRMED — source card S2]: [CLM23] Conjecture 2.8 + Definition 2.9 + Lemma 2.12, consumption at ε=δ(dκ)/10, strictly inverse-polynomial regime, ℤ₂-first.
   - **K3′** (provenance, from Scout 2026-08-27): Contract's verbatim statement is [CLM23] Conjecture 2.8 (ℂ-valued), not [ACC22] Conjecture 5.5 (ℝ-valued); equivalent up to factor 2 in δ ([ACC22] Thm 5.6 / App. A; [CLM23] fn. 8). "Finitely supported" convention (Reading convention 1) is Contract-added, benign.

## SOURCE LIBRARY

**In collection (cards evict originals):**
- **S1-acc22-card.md** (id: S1-acc22, retrieved 2026-08-27 by Scout): [ACC22] full theorem statements, proof mechanism, counterexamples B.1–B.5, context.
- **S2-clm23-card.md** (id: S2-clm23, retrieved 2026-08-27 by Scout): [CLM23] Conjecture 2.8, state formulation, conversion lemma, consumption regime, uncertainty-principle ingredient.
- **S3-2026-bypass-lemmas-card.md** (ids: S3a, S3b, first carded 2026-08-27 by Scout at [RESTATED] grade, **upgraded to [READ] the same day** from the human-uploaded PDFs `2608.03824v1.pdf` and `2504.05710v2.pdf`): S3a = arXiv:2608.03824 Lemma 3.5 "Disjoint-support separator", §3.4 pp. 7–8 (depth-O(d⁴) decision tree deciding which of two everywhere-disjoint degree-≤d real multilinear polynomials is nonzero, under a promise; per-pair, algorithmic, no influence/norm/distribution content) — statement AND proof now carded, including the recursion and the explicit constant assembly (b ≤ 8D² disjoint maximum monomials per stage via the KKDWY26 rational-degree lemma, ≤ 8d³ queries per stage, ≤ 2d stages, depth ≤ 16d⁴); S3b = arXiv:2504.05710v2 Lemma 3.4, §3.2 pp. 13–14 (win-win partial assignments for a single nonzero degree-d polynomial) — statement AND proof carded (≤ d rounds of maximal-disjoint-maximum-monomial fixing, |μ| ≤ md², case (b) via Mid04). PCC-mismatch flags unchanged on the card. Residual one-level-deeper blocks: internals of [KKDWY26] (arXiv:2601.08727v2) and [Mid04] (quant-ph/0403168) — statements printed in the read papers, their own proofs not read.

**QUEUE (ranked by load-bearing impact):**
(empty — both strategist requests resolved at [READ] grade on 2026-08-27. Latent, below bar, only if a proof step comes to depend on their internals: PDFs of arXiv:2601.08727v2 [KKDWY26] and quant-ph/0403168 [Mid04].)

**DECLINED:** none.

## RETREAT LOG

(empty — depth 0, no retreats)

## WEAKENING POOL

(empty — cycle 1 closure; first weakening material after rung failures)

---

## MANIFEST

| id | path | agent | model | cycle | status | notes |
|---|---|---|---|---|---|---|
| CONTRACT | CONTRACT.md | orchestrator | claude-fable-5 | 0 | ACTIVE | original problem statement |
| 0023-scout-1 | proofs/0023-scout-1.md | scout | claude-fable-5 | 1 | COMPLETE | verdict: NO PRIOR RESOLUTION FOUND; boundary pins K1–K3′; three 2026 bypass papers noted |
| 0023-refuter-1 | proofs/0023-refuter-1.md | refuter | claude-fable-5 | 1 | COMPLETE | COMPUTATIONALLY CERTIFIED: ε*(1,N)=1/2; ε*(2,4)=1/5; ε*(d)≤(4/11+o(1))/d; obstruction (O1–O3) |
| 0023-refuter-1-code | proofs/0023-refuter-1-code/ | refuter | — | 1 | COMPLETE | reproducible code: pcc_lib.py + 10 scripts; ~7 min wall clock; python3.14 + numpy 2.5.2, scipy 1.18.1 |
| 0023-strategist-1 | proofs/0023-strategist-1.md | strategist | claude-fable-5 | 1 | COMPLETE | six plans P1–P6 ranked by info/effort; three reformulations R1–R3 (CONDITIONAL); source requests (rank 1, 2) |
| PROGRESS.md | PROGRESS.md | case-planner | claude-fable-5 | 1 | AWAITING APPROVAL | case ladder R0–R6; conventions; extremal-case calibration (Rung 0); no rung materialised |
| S1-acc22-card | sources/S1-acc22-card.md | scout | — | 1 | IN LIBRARY | [ACC22] source card: three conjecture formulations, K1 theorem, K2 counterexamples, proof mechanism |
| S2-clm23-card | sources/S2-clm23-card.md | scout | — | 1 | IN LIBRARY | [CLM23] source card: state form, conversion lemma, consumption regime, Donoho–Stark caveat |
| S3-2026-bypass-lemmas-card | sources/S3-2026-bypass-lemmas-card.md | scout + orchestrator | claude-fable-5 | 1–2 | IN LIBRARY ([READ]) | S3a = 2608.03824 Lem 3.5 (statement + proof, pp. 7–8), S3b = 2504.05710v2 Lem 3.4 (statement + proof, pp. 13–14); upgraded from [RESTATED] via human-uploaded PDFs 2026-08-27; source queue now empty |

---

## NEXT ACTION (exactly one)

**HUMAN GATE — approve or reorder the case ladder in PROGRESS.md**

The case ladder (Rungs R0–R6, pp. 27–142 of PROGRESS.md) is complete and ready for review. **On approval**, the next action is: **materialise R1 (spread-junta indicator rung) as intermediate I01**, then run **Refuter first** (bounded search on small d, windows, patterns; existing tooling in `proofs/0023-refuter-1-code/`; ~1–2 hours); if refutation succeeds R1 is false and skip to R2 attempt or weaken; if no counterexample found, mark NEAR-MISS and pass to Prover.

**Pending sub-items (do not count as separate actions):**
- **Source gate (concurrent with I01 materialisation):** Request arXiv:2608.03824 Lemma 3.5 (rank 1) for P2's milestone; proceed on extraction [RESTATED] if unavailable, flagged conditional downstream. This is housekeeping during I01 refuter sweep, not a blocking step.
- **Reorder options recorded in PROGRESS.md** (pp. 144–146): defend or swap R4/R5 (analytic heart vs threshold-climbing); drop R2 if R1's mechanism scales (R2 rider on R3); acceptable per Contract constraints.

---

## VERIFICATION TALLY (persistent, per-pass format)

To be populated as artifacts enter verification. Format per HARNESS.md §3.9 (review update):

| cycle | pass | agent | RAW verdict | POST-TRIAGE verdict | artifact cid | notes |
|-------|------|-------|-------------|---------------------|--------------|-------|
| (on first proof artifact entry) | 1 | verifier | [RAW: one of the five verdicts] | [POST-TRIAGE: same or DEAD-PLAN-RUNG if retraction applies] | [first 12 hex of sha256] | |

---

## Resume test

**Can a cold session continue from this ledger alone?** YES. This ledger contains:
- Complete problem statement (via CONTRACT.md reference + K1–K3′ pins).
- Scout verdict + literature boundary.
- Six independent attack plans ranked by efficiency.
- Complete case ladder (R0–R6) with ladder conventions, difficulty jumps, and concrete milestone contracts.
- Two source cards (S1, S2) pinning all cited theorems.
- Computationally verified refutation frontier (ε* values, obstruction diagnosis).
- Next action fully specified: HUMAN GATE with reorder options.

**Missing (acceptable for cycle 1 closure):** No rung proved; no proof artifact in flight; no verification pass. **Acceptable:** these are not required until approval of the gate.

---

### END OF LEDGER, c/0023, cycle 1 closure, 2026-08-27 ###
