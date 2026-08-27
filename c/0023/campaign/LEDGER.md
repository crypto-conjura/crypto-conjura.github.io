# CAMPAIGN LEDGER: c/0023
## Polynomial Compatibility Conjecture (PCC), inverse-polynomial influence regime

**Campaign:** c/0023 — depth 0 — contract: `CONTRACT.md`  
**Cycle:** 2 (rung R1 reconnaissance) · **Cycle 2 closed:** 2026-08-27  
**Harness:** `prompts/solve.md` (this repository's HARNESS.md)  
**First screenful orientation:** Cycle 2 complete: **R1 FROZEN** (ε*_junta(d)=1/(2d), δ(d)=1/(3d), witnesses c₁=1/3, c₂=1; 5/5 blind passes post-triage-clean + blind gate CLEAN). Progress: one rung climbed (R0→R1), five remain (R2–R6). Prover (0023-prover-1) proved lemma chain F1–F4→(M) via Harper edge-isoperimetry; scout R1 micro-sweep killed prior-art candidates; scout deciding-source (KKDWY26) read complete; S5 card written; S3a residual [SOURCE-BLOCKED] lifted. Source queue empty; next gate: HUMAN GATE on frozen proof, then R2 scout→refuter→strategist→prover pipeline.

---

## ESTABLISHED

### I01 (rung R1): Junta incompatibility via indicator-pair payment chain **FROZEN**
**CID:** `6a7b5c2e3f1` · **Proof artifact:** 0023-prover-1 (evicted from active context; cited as black box per §2.4)  
**Statement:** For ℤ₂ and indicator junta families 𝒞^junta_d with max per-coordinate average influence δ(d), incompatibility forces **max(δ_F, δ_G) ≥ 1/(2d)**. Equivalently, every incompatible pair imposes a constraint **δ_F·E_𝐆|K| + δ_G·E_𝐅|J| ≥ 1** where |J|, |K| ≤ d are window sizes. The grid (d×d row-column construction) achieves equality and attains the frontier exactly; thus **ε*_junta(d) = 1/(2d)** and **δ(d) = 1/(3d) is a witnessing threshold** (or any θ/(2d) for 0 < θ < 1). Witnesses: c₁ = 1/3, c₂ = 1 (per-coordinate average influence bounds; tightness via grid ceiling).  
**Verification record (frozen, never re-verified per §2.4):** 5/5 blind passes post-triage-clean (passes A–E: agent verifier family, then agent verifier-b family) + final blind gate CLEAN, date 2026-08-27. Triage summary: 0 upheld, 3 overruled, 6 pedantic, 0 needs-source, 0 unclear defects; one false affirmative clearance corrected in pass B.  
**Load-bearing caveats (from triage, filed verbatim):**  
(i) The "generalization hypothesis met" claim is a passed detour test, not a verified statement that the indicator-specific engine lifts to signed classes.  
(ii) The tightness remark 10.1 is non-load-bearing.

## VERIFICATION TALLY

| Cycle | Pass | Agent | Model | RAW verdict | POST-TRIAGE verdict | Report |
|-------|------|-------|-------|-------------|---------------------|--------|
| 2 | A | agent verifier | claude-fable-5 | CLEAN | CLEAN | proofs/0023-prover-1-verify-A.md |
| 2 | B | agent verifier | claude-fable-5 | CLEAN | CLEAN | proofs/0023-prover-1-verify-B.md |
| 2 | C | agent verifier | claude-fable-5 | CLEAN | CLEAN | proofs/0023-prover-1-verify-C.md |
| 2 | D | agent verifier-b | claude-opus-4 | CLEAN | CLEAN | proofs/0023-prover-1-verify-D.md |
| 2 | E | agent verifier-b | claude-opus-4 | CLEAN | CLEAN | proofs/0023-prover-1-verify-E.md |
| 2 | Triage | triage | — | (3 overruled, 6 pedantic) | all passes upheld / 0 defects | proofs/0023-prover-1-triage.md |
| 2 | Blind Gate | final gate | — | CLEAN | CLEAN | proofs/0023-prover-1-blindgate.md |

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

### **Junta-class frontier (refuter-proved, exact, ε*_junta(d)=1/(2d); grid-attained; tightness via isoperimetry)**
**Source:** 0023-refuter-2 (cycle 2, exact arithmetic + exhaustive sweep)  
**Statement (CERTIFIED, NOT VERIFIED):** Over ℤ₂, for patterns on indicator junta supports:
- **(Table of exact frontier values, all certified rational.)** ε*_junta(2,2)=1/2; ε*_junta(2,3)=1/3; ε*_junta(2,4)=1/4 (grid-attained); ε*_junta(3,3)=1/4; ε*_junta(3,4)=1/4. No partition-rich configuration beats the grid constant.
- **(Per-pair payment law.)** Every cross-disjoint incompatible pair forces $\sum_{i\in S}[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)] \ge 1$ on the shared window $S$; minimum attained exactly 1 (verified on 20,000+ pairs). Payment-tight pairs are locally grid-like (all 10,494 sampled tight pairs reduce to single oppositely-forced coordinates with uniform fibers).
- **(Junta vs full-class divergence at d=2.)** Junta frontier $1/4$ vs full-class frontier $1/5$ (refuter-1 §4.1): sub-1/(2d) full-class records are essentially non-indicator sums-of-indicators.
**Proof method (candidate, F1–F4→(M)):** Formula (F1): influence formula; (F2): disjointness ≡ projection-disjointness; (F3): projection-density payment bound via hypercube edge-isoperimetry (verified exhaustively 984,858 (pattern, window) pairs k≤4, 200,000 random k∈[5,12]); (F4): per-pair payment from (F3); (M): master count via (F4) linearity over distributions → max(δ_F,δ_G)≥1/(2d). **Non-elementary link: hypercube edge-isoperimetry (Harper); verified only computationally on all reachable scales; general-k truth rests on the standard isoperimetric inequality.**
**Rigidity:** All intermediate quantities at every audit satisfy their inequality; grid meets every link with equality.

### **The obstruction (refuter-diagnosed, not a theorem)**
**Source:** 0023-refuter-1 §5  
**Statement (diagnostic):** Three independent walls hit every construction searched:
1. **(O1) Conflict localization / union bound.** Within subcube-indicator distributions, every incompatible pair has max per-coordinate average influence ≥ 1/(2d); the grid is extremal. Proof: incompatibility means certain-conflict; two subcubes conflict iff some shared coordinate forced opposite; union bound gives 1≤2δ·E|T|≤2δ·d.
2. **(O2) The union/product asymmetry.** Sub-1/(2d) gains come from union side (quadratic per-coordinate influence decay), but partner forced into product-form (degree grows linearly, influence constant 1/(b+b²)). Balancing optimizes at small b, yielding plateau 2/5→4/11. Within all block architectures, ε·d bounded below by absolute constant; no choice reaches o(1/d).
3. **(O3) Boolean impossibility.** Boolean-derived pairs (1±σ)/√2 have value max_i Inf_i(σ)/2; OSSS + decision-tree-depth bounds give Var≤(max Inf)·poly(d), so Boolean pairs provably 1/poly-bounded — cannot certify falsity. Counterexample if it exists must be essentially non-Boolean (spiky nonnegative densities, the regime where AA-kin open since 2009).

Together: expected profile if ε*(d)=Θ(1/d) and **the conjecture is TRUE with c₂=1**.

---

## DEAD PLANS

### R1 falsification honeypot (cycle 2, 0023-refuter-2)
**Status:** DEAD. **Reason:** Exact exhaustive search (all 984,858 (pattern, window) pairs k≤4, 200,000 random k∈[5,12], 1,712 stochastic free-form families, all structured architectures) yields ε*_junta(d)=1/(2d) exactly, grid-attained, via the isoperimetry chain F1–F4→(M). No construction beats the grid constant; pattern richness cannot push the frontier below Θ(1/d). The search is terminated not by resource exhaustion but by a fully quantitative obstruction, eliminating falsity via five elementary counting steps verified in exact arithmetic at scale. Falsity would contradict Harper's hypercube edge-isoperimetric inequality.

### Scout-2 prior-art candidates (cycle 2, 0023-scout-2)
**Status:** DEAD. **Reason:** Micro-scout on rung R1 as a standalone combinatorial object found no literature match. Killed approaches: (i) ALWZ spreadness — low average influence does not imply low window membership; the rung's content is the gap between them (scout-2 §C2). (ii) Cross-intersecting families — the polarity is wrong; literature requires cross-MEETING families (agreement), not cross-DISJOINT (conflict); measure mismatch (counting vs influence) (scout-2 §B4). (iii) Subcube partitions — single-family partitioning only, no two-family cross structure, no influence hypothesis (scout-2 §B5). (iv) Conflict complexity — runs over query-process distributions on 0/1-inputs, not over certificate/pattern families with influence caps (scout-2 §B6). (v) AA-conjecture specialisations — proved cases are single-function only; no pair/cross-disjoint variant found; Boolean-valued statements are classical but exponential-influence only (scout-2 §B7). Verdict: NO PRIOR RESOLUTION FOUND stands.

### Scout-3 KKDWY26 possibility (cycle 2, 0023-scout-3)
**Status:** DEAD. **Reason:** Full read of arXiv:2601.08727v2 (deciding source identified in scout-2 §E) resolved whether KKDWY26 hides a distributional or influence-type statement about disjoint-support families. Outcome: no distributions over polynomials, no families (every result per-function or per-pair), no spread, no influence HYPOTHESIS in any theorem, and the only influence CONCLUSIONS are in the exponential regime (2^{-2·rdeg}), already covered by card S1 (ACC22 Thm 4.4). Theorem 4 confirms S3a's $16d^4$ constant; Theorem 10 (only pair statement) is unusable for I01 (fails the everywhere-promise). Scout-3 §E verdict: outcome (i) of scout-2 prediction (no distributional statement). Possibility killed: KKDWY26 does not settle or partially settle I01.

## OPEN GAPS

1. **K1/K2/K3/K3′ source pins (CONTRACT.md, confirmed 2026-08-27):**
   - **K1** [CONFIRMED — source card S1]: [ACC22] Theorem 4.4 (p. 20) proves the conjecture's analogue with strict threshold δ < |𝒴|^{-d}/d for every finite abelian group; proof (§5.2) uses no influence bound on 𝐅 and no degree bound on 𝐆.
   - **K2** [CONFIRMED for ℤ₂ — source card S1]: [ACC22] Claim B.3 (p. 41): NegRow/PosCol pair on d×d Boolean variables has degree d, all relative influences ≤1/(2d), singleton supports, and f·g≡0. Printed for ℤ₂ only; any witnessing δ must satisfy δ(d)<1/(2d) over ℤ₂, hence effectively c₂≥1 for ℤ₂.
   - **K3** [CONFIRMED — source card S2]: [CLM23] Conjecture 2.8 + Definition 2.9 + Lemma 2.12, consumption at ε=δ(dκ)/10, strictly inverse-polynomial regime, ℤ₂-first.
   - **K3′** (provenance, from Scout 2026-08-27): Contract's verbatim statement is [CLM23] Conjecture 2.8 (ℂ-valued), not [ACC22] Conjecture 5.5 (ℝ-valued); equivalent up to factor 2 in δ ([ACC22] Thm 5.6 / App. A; [CLM23] fn. 8). "Finitely supported" convention (Reading convention 1) is Contract-added, benign.

## SOURCE LIBRARY

**In collection (cards evict originals):**
- **S1-acc22-card.md** (id: S1-acc22, retrieved 2026-08-27 by Scout): [ACC22] full theorem statements, proof mechanism, counterexamples B.1–B.5, context. **Marginal annotation (triage, cycle 2, 2026-08-27):** Claim B.2's strict inequality is equality at n=1 — filed as card annotation, not a defect.
- **S2-clm23-card.md** (id: S2-clm23, retrieved 2026-08-27 by Scout): [CLM23] Conjecture 2.8, state formulation, conversion lemma, consumption regime, uncertainty-principle ingredient.
- **S3-2026-bypass-lemmas-card.md** (ids: S3a, S3b, first carded 2026-08-27 by Scout at [RESTATED] grade, **upgraded to [READ] the same day** from the human-uploaded PDFs `2608.03824v1.pdf` and `2504.05710v2.pdf`): S3a = arXiv:2608.03824 Lemma 3.5 "Disjoint-support separator", §3.4 pp. 7–8 (depth-O(d⁴) decision tree deciding which of two everywhere-disjoint degree-≤d real multilinear polynomials is nonzero, under a promise; per-pair, algorithmic, no influence/norm/distribution content) — statement AND proof now carded, including the recursion and the explicit constant assembly (b ≤ 8D² disjoint maximum monomials per stage via the KKDWY26 rational-degree lemma, ≤ 8d³ queries per stage, ≤ 2d stages, depth ≤ 16d⁴); S3b = arXiv:2504.05710v2 Lemma 3.4, §3.2 pp. 13–14 (win-win partial assignments for a single nonzero degree-d polynomial) — statement AND proof carded (≤ d rounds of maximal-disjoint-maximum-monomial fixing, |μ| ≤ md², case (b) via Mid04). PCC-mismatch flags unchanged on the card. **S3a residual [SOURCE-BLOCKED: KKDWY26] on internal Lemma 2.3 uses is LIFTED by S5 item C1 (Corollary 1 now READ at source).** Residual one-level-deeper block: [Mid04] (quant-ph/0403168) — statement printed in the read paper, its own proof not read.
- **S5-kkdwy26-card.md** (id: S5, carded 2026-08-27 cycle 2 by Scout, [READ] — arXiv:2601.08727v2 full PDF, all 26 pages read): [READ] Kothari–Kovacs-Deak–Wang–Yang, *Rational degree is polynomially related to degree*, main result $\deg(f) \le \widetilde O(\mathrm{rdeg}(f)^3)$. Four items: (C1) **Corollary 1 (discrete-Markov lemma, p. 4), statement and proof**, verbatim: $p$ real, $|p(x)|\le h$ on cube, $|p(0^n)|=h$, $p(x)p(0^n)\le 0$ at |x|=1 ⟹ $\deg(p)\ge\sqrt{n/2}$ — **confirms S3a's constant exactly, lifts S3a residual block**; (T4) **Theorem 4 (p. 7), verbatim: $D(f)\le 4\deg_\pm(f)^2\,\mathrm{rdeg}(f)^2\le 16\,\mathrm{rdeg}(f)^4$**, the form S3a cites for the total-function template (P2 adapts); (T10+F7) **Theorem 10 (Effective Hypercube Nullstellensatz, p. 18)** — the paper's only pair-of-disjoint-support statement, requires EVERYWHERE-promise (no common zeros on entire cube), **unusable for I01 objects** (incompatible indicators have common zeros on $(A\cup B)^c$, same flag as S3a hyp 4); Fact 7 (p. 18) **barrier evidence: dropping $g_1g_2\equiv 0$ kills any poly(d) partition-of-unity bound even at degree 1**, supporting evidence that R1 proof must exploit disjointness itself; (T9/R3) **Theorem 9 + Remark 3 (p. 16)**: influence content is exponential regime only ($2^{-2\,\mathrm{rdeg}}$), already covered by S1; delimitless. **Does NOT contain:** distributions over polynomials (only over decision trees), families (every result per-function or per-pair), spread, influence HYPOTHESIS, or $1/\mathrm{poly}(d)$ influence CONCLUSION. Deciding source outcome: confirmed scout-2 §E outcome (i).

**QUEUE (ranked by load-bearing impact):**
(empty — both strategist requests resolved at [READ] grade on 2026-08-27, and KKDWY26 (the deciding source) fully read on 2026-08-27 cycle 2, resulting in S5 card and S3a residual block lift. Latent, below bar, only if a proof step comes to depend on internal proofs of [Mid04] (quant-ph/0403168) — currently needed only as a single-function lemma cite for S3b.)

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
| S3-2026-bypass-lemmas-card | sources/S3-2026-bypass-lemmas-card.md | scout + orchestrator | claude-fable-5 | 1–2 | IN LIBRARY ([READ]) | S3a = 2608.03824 Lem 3.5 (statement + proof, pp. 7–8), S3b = 2504.05710v2 Lem 3.4 (statement + proof, pp. 13–14); upgraded from [RESTATED] via human-uploaded PDFs 2026-08-27; S3a residual [SOURCE-BLOCKED: KKDWY26] lifted by S5 cycle 2 |
| I01-spread-junta | intermediates/I01-spread-junta.md | case-planner | claude-fable-5 | 2 | ESTABLISHED+FROZEN | rung R1; verified via prover 0023-prover-1 lemma chain; 5/5 blind passes post-triage-clean; final blind gate CLEAN; proof frozen, cited as black box per §2.4 |
| 0023-prover-1-verify-A | proofs/0023-prover-1-verify-A.md | verifier | claude-fable-5 | 2 | COMPLETE | blind pass A: agent verifier family; RAW CLEAN; POST-TRIAGE CLEAN |
| 0023-prover-1-verify-B | proofs/0023-prover-1-verify-B.md | verifier | claude-fable-5 | 2 | COMPLETE | blind pass B: agent verifier family; RAW CLEAN; POST-TRIAGE CLEAN; corrected one false affirmative clearance in triage |
| 0023-prover-1-verify-C | proofs/0023-prover-1-verify-C.md | verifier | claude-fable-5 | 2 | COMPLETE | blind pass C: agent verifier family; RAW CLEAN; POST-TRIAGE CLEAN |
| 0023-prover-1-verify-D | proofs/0023-prover-1-verify-D.md | verifier | claude-opus-4 | 2 | COMPLETE | blind pass D: agent verifier-b family; RAW CLEAN; POST-TRIAGE CLEAN |
| 0023-prover-1-verify-E | proofs/0023-prover-1-verify-E.md | verifier | claude-opus-4 | 2 | COMPLETE | blind pass E: agent verifier-b family; RAW CLEAN; POST-TRIAGE CLEAN |
| 0023-prover-1-triage | proofs/0023-prover-1-triage.md | triage | — | 2 | COMPLETE | triage ruling: 0 upheld, 3 overruled, 6 pedantic, 0 needs-source, 0 unclear; all five passes post-triage-clean; filed marginal annotation on S1 Claim B.2 |
| 0023-prover-1-blindgate | proofs/0023-prover-1-blindgate.md | final gate | — | 2 | COMPLETE | final blind gate: CLEAN |
| 0023-scout-2 | proofs/0023-scout-2.md | scout | claude-fable-5 | 2 | COMPLETE | rung-start micro-scout on I01 standalone; verdict NO PRIOR RESOLUTION FOUND; kills ALWZ spreadness, cross-intersecting families, subcube partitions, conflict complexity, AA specialisations; identifies KKDWY26 as deciding source |
| 0023-scout-3 | proofs/0023-scout-3.md | scout | claude-fable-5 | 2 | COMPLETE | bounded full read of deciding source arXiv:2601.08727v2 (KKDWY26); resolves scout-2 §E; outcome (i) confirmed: no distributional/influence theorem for I01 in KKDWY26; S5 card written; S3a residual block lifted |
| 0023-refuter-2 | proofs/0023-refuter-2.md | refuter | claude-fable-5 | 2 | COMPLETE | rung R1 exact exhaustive search (all 984,858 (pattern,window) pairs k≤4, 200,000 random k≤12, 1,712 stochastic free-form families, all structured architectures); ε*_junta(d)=1/(2d) exactly, grid-attained; candidate theorem F1–F4→(M) with isoperimetry as non-elementary link; falsity ruled out via five elementary counting steps |
| 0023-refuter-2-code | proofs/0023-refuter-2-code/ | refuter | — | 2 | COMPLETE | reproducible code: junta_lib.py + 5 scripts (t1–t5); ~2.5 min wall clock; python 3.14, numpy 2.5.2, scipy 1.18.1 (all load-bearing arithmetic in exact rationals/integers) |
| S5-kkdwy26-card | sources/S5-kkdwy26-card.md | scout | — | 2 | IN LIBRARY ([READ]) | KKDWY26 source card [READ]: Corollary 1 (discrete-Markov, statement+proof, lifts S3a residual block), Theorem 4 (constant confirmation), Theorem 10 (pair statement, unusable for I01, everywhere-promise fails), Fact 7 (barrier evidence), T9/R3 (influence content exponential only, already in S1). Global: no distributions, no families, no spread, no influence hypothesis. |
| 0023-prover-1 | proofs/0023-prover-1.md | prover | claude-fable-5 | 2 | COMPLETE/FROZEN-PROOF | assigned plan: refuter-2 §8 lemma chain (F1–F4→(M)); proved statement: ε*_junta(d)=1/(2d), δ(d)=1/(3d) witnessing; Harper edge-isoperimetry proved inline; proof frozen, proof evicted from context per §2.4 |

---

## NEXT ACTION (exactly one)

**HUMAN GATE — Read the frozen proof proofs/0023-prover-1.md per HARNESS §4. On go-ahead, proceed to intermediate I02 (rung R2, degree-d set rung) or optionally formalizer on I01.**

**Cycle 2 SUMMARY (CLOSED 2026-08-27):** 
- **Rung R1 reconnaissance completed.** Micro-scout (0023-scout-2): NO PRIOR RESOLUTION FOUND on I01 standalone; all prior-art candidates (ALWZ, cross-intersecting families, subcube partitions, conflict complexity, AA specialisations) killed. Deciding-source full read (0023-scout-3): KKDWY26 outcome (i) confirmed (no distributional/influence theorem); S5 card written; S3a residual [SOURCE-BLOCKED: KKDWY26] lifted.
- **Exact frontier discovered.** Refuter (0023-refuter-2): ε*_junta(d)=1/(2d) exactly, grid-attained. Candidate proof chain F1–F4→(M) verified exhaustively; Harper edge-isoperimetry (non-elementary link) verified computationally; falsity ruled out via five elementary counting steps.
- **Prover completed.** 0023-prover-1: lemma chain F1–F4→(M) proved; I01 statement (incompatibility forces max(δ_F,δ_G)≥1/(2d), witnessed δ(d)=1/(3d), tightness via grid) verified **FROZEN** per §2.4.
- **Verification loop closed.** Five blind passes (A–E, two verifier families), triage (0 upheld, 3 overruled, 6 pedantic, all post-triage-clean), final blind gate CLEAN; cycle 2 all gates CLEAR; one rung climbed; five remain.

**On HUMAN GATE approval:**
1. **Materialise rung R2 (degree-d set rung) as intermediate I02.** R2 prerequisite: the Nisan–Szegedy-type junta theorem must be carded before I02 cites it. **First step is a source-card errand** (no prover work on I02 until card is available).
2. **Optional:** Formalizer on I01 if wanted (per §4, non-blocking; one external lemma [Mid04] remains unread, does not block Lean statement but may block Lean proof).

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
- **Verified intermediate I01 (rung R1), frozen:** ε*_junta(d)=1/(2d), δ(d)=1/(3d), witnesses c₁=1/3, c₂=1; proof artifact 0023-prover-1 (evicted from context); 5/5 blind passes post-triage-clean + blind gate CLEAN; verification tally complete (cycle 2, all verdicts recorded).
- Cycle 1 Scout verdict (NO PRIOR RESOLUTION FOUND).
- Cycle 2 Scout-2 micro-verdict on R1 (NO PRIOR RESOLUTION FOUND, killed prior-art routes).
- Cycle 2 Scout-3 deciding-source verdict (KKDWY26 fully read; outcome (i) confirmed; S3a residual lifted).
- Cycle 2 Refuter verdict (exact frontier search complete; falsity ruled out via Harper isoperimetry chain).
- Cycle 2 Prover verdict (I01 proved; lemma chain F1–F4→(M) complete with inline Harper proof).
- Cycle 2 Verification loop complete (5 blind passes, triage, final blind gate all CLEAN).
- Six independent attack plans (cycle 1 Strategist).
- Complete case ladder R0–R6 (PROGRESS.md, approved cycle 1).
- Five source cards (S1, S2, S3a/S3b, S5) with marginal annotation on S1 from cycle 2 triage.
- **Next action fully specified:** HUMAN GATE — read frozen proof 0023-prover-1.md; on approval, materialise R2 (I02) with Nisan–Szegedy junta theorem as source-card prerequisite.

---

---

### END OF LEDGER PATCH, c/0023, cycle 2 closed, sections: HEADER, ESTABLISHED (I01 FROZEN), VERIFICATION TALLY, CONDITIONAL (I01 removed), MANIFEST (0023-prover-1 COMPLETE/FROZEN-PROOF, +5 verify reports, +triage, +blindgate, I01-spread-junta ESTABLISHED+FROZEN), SOURCE LIBRARY (S1 marginal annotation appended), NEXT ACTION (HUMAN GATE), Resume test — date 2026-08-27 ###
