# CAMPAIGN LEDGER: c/0023
## Polynomial Compatibility Conjecture (PCC), inverse-polynomial influence regime

**Campaign:** c/0023 — depth 0 — contract: `CONTRACT.md`  
**Cycle:** 4 (refutation and prover chain on R2) · **Cycle 4 closed:** 2026-08-28  
**Harness:** `prompts/solve.md` (this repository's HARNESS.md)  
**First screenful orientation:** Cycle 4 complete: **R1 FROZEN** (ε*_junta(d)=1/(2d), δ(d)=1/(3d)); **R2 ACTIVE + OPEN** (I02, degree-d set rung). **Lead payment route REFUTED at its final step:** yields only exponential thresholds unconditionally (refuter-6 G5: window size d + O(log d log log d) for uniform-point minimal selections, deterministic rule ratio exactly 2^-d), plus conditional result on dense pairs (prover-4: proven on assumption both densities ≥ 1/poly(d), sparse pairs untouched). Refuter-7: hub witness does not decay but every coordinate carries influence ≥ 2^(-1-d) (d ≥ 17 carries real content). Refuter-8: GAP-3 refuted in its branch with certificate at degree 120, dimension 188, verified three exact ways over 7004 instances; refuting family crosses threshold only from degree 53 (small-dimension search ruled out). Prover-4 cycle complete: L1–L3 proved unconditional (u1); L4 proved at payment 2^(1-d) exponential only (u2); monomial-only sub-route closed by tight Theta(d 2^-d) isoperimetric bound (u3); branch excludes certified witness, exact branch empty at zero (u4). All conditional on dense pairs (densities ≥ 1/poly(d)); sparse pairs remain open. Nothing passed five-pass acceptance into ESTABLISHED.

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
| 3 | A | agent verifier | claude-fable-5 | NOT CLEAN | NOT CLEAN | proofs/0023-prover-3-verify-A.md |
| 3 | B | agent verifier | claude-fable-5 | CLEAN | WRONG (post-triage ruled) | proofs/0023-prover-3-verify-B.md |
| 3 | C | agent verifier | claude-fable-5 | CLEAN | WRONG (post-triage ruled) | proofs/0023-prover-3-verify-C.md |
| 3 | D | agent verifier-b | claude-opus-5 | DEFECTS | DEFECTS | proofs/0023-prover-3-verify-D.md |
| 3 | E | agent verifier-b | claude-opus-5 | DEFECTS | DEFECTS | proofs/0023-prover-3-verify-E.md |
| 3 | Triage | triage | — | (10 upheld, 9 overruled, 6 pedantic, 0 needs-source, 0 unclear) | passes B,C ruled WRONG (each had cleared 4 upheld defects); four passes read LEDGER.md/PROGRESS.md outside blind view, self-disclosed; fixed in r2 | proofs/0023-prover-3-triage.md |
| 3 | F (r2) | agent verifier-b | claude-opus-5 | PENDING | PENDING | proofs/0023-prover-3-r2-verify-F.md |
| 3 | G (r2) | agent verifier | claude-fable-5 | PENDING | PENDING | proofs/0023-prover-3-r2-verify-G.md |

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

### Prover-2 partial results (cycle 3, PARTIAL artifact 0023-prover-2)
**CID:** `d4b2e9f3c1a` · **Source:** 0023-prover-2 (cycle 3, claude-opus-5, PARTIAL)  
**Statement (three components):** (1) **R2 proved at every delta < 2^-d/d by independent poly(d)-window route** (alternative to graph-embedding strategy; cost: d exponential window sizes but delivers inverse-exponential margin). (2) **Positivity lemma (first two-family consequence of Chang-Fang): every shattering window of A meets rel(B) for every cross-disjoint pair** (proves window structure must interlock, key for dimension counting). (3) **(PAY**)** recorded OPEN **with its consequence:** if true, every balanced degree-D Boolean function has a coordinate of influence ≥ 1/poly(D) — **powerful if the premise holds, yet premise falsified by refuter-3.**  
**Verification tally:** none (PARTIAL artifact; depends on prover-2 verification, not yet in loop).

### Prover-3-r2 CAP I and CAP II barrier claims (cycle 3, CONDITIONAL, one revision cycle, re-verification in flight)
**CID:** `e8f4d2c9b6a` · **Source:** 0023-prover-3-r2 (cycle 3, claude-opus-5, PARTIAL, revision cycle 1)  
**Statement (CAP I and CAP II, not yet accepted):** Two barrier claims on I02 submitted in r2 revision; post-triage ruled NOT CLEAN (B,C passes ruled wrong; triage outcome 10 upheld, 9 overruled). **Not accepted.** Two in-flight re-verification passes F/G pending (verifier-b and verifier); status: re-verification in flight.  
**Verification tally:** Cycle 3 raw: A NOT CLEAN, B CLEAN (post-triage WRONG), C CLEAN (post-triage WRONG), D DEFECTS, E DEFECTS; Triage: 10 upheld/9 overruled/6 pedantic. Re-verification F/G pending.

### Refuter-5 non-Boolean-group floor (cycle 3, searched-but-unproved)
**CID:** `a1c6e9f2d3b` · **Source:** 0023-refuter-5 §5 (cycle 3, claude-opus-5)  
**Statement:** Non-Boolean group floor conjectured tight by exhaustive search at small d, but **proof not found**; optimization landscapes consistent with optimality but no certificate. Status: **OPEN, searched-but-unproved.**  
**Verification tally:** none (search only, no formal proof); marked CONDITIONAL pending proof or refutation in later cycles.

### Prover-4 payment-hypothesis chain (cycle 4, claude-opus-5, conditional on dense pairs)
**CID:** `b2e3f4a5c6d` · **Source:** 0023-prover-4-u0.md through -u4.md (cycle 4, claude-opus-5, five units)  
**Statement (composite, by unit):**  
**(u0: Definition and setup)** Rung R2 degree-d set hypothesis, payment-conditional framework, and dense-pair constraint introduction: densities 𝐅 and 𝐆 both ≥ 1/poly(d).  
**(u1: Rungs L1–L3)** **Proved unconditionally, no gaps:** L1 (structural constraint), L2 (degree bound), L3 (local incompatibility necessary condition). All three hold for arbitrary densities.  
**(u2: Rung L4)** **Proved unconditionally but ONLY at payment 2^(1-d), exponential decay** with d. No polynomial improvement under the framework. This kills the main payment-hypothesis route.  
**(u3: Monomial-only sub-route)** Closed by **tight Θ(d 2^(-d)) isoperimetric bound:** the monomial-only payment sub-route cannot exceed this. The true payment on the counterexample family is carried by a coordinate outside both monomial supports (critical observation). Route is dead for universal payment claims.  
**(u4: Branch exclusion and emptiness)** Branch genuinely excludes the certified witness from refuter-8; exact branch is empty at zero (on the certificate family, no points satisfy the relaxed constraint). Sub-hypothesis space is nowhere.  
**Overall condition:** All r2 results hold **IF both densities are ≥ 1/poly(d)** (dense pairs). **Sparse pairs remain completely open** (the whole remaining difficulty). R2 is therefore CONDITIONAL on dense-pair assumption, with independent sparse-pair work still required.  
**Verification tally:** none (CONDITIONAL artifact; not entered verification loop until dense-pair claim stands independently or gets released).

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

### **Refuter-3: eps*_ind(2) = 1/4 for all N (cycle 3, proved, not searched)**
**Source:** 0023-refuter-3 (cycle 3, claude-opus-5, exact arithmetic)  
**Statement:** Over ℤ₂ at degree d=2, for every N, **eps*_ind(2) = 1/4** exactly. The degree-≤2 junta size is exactly M(2)=4 (confirmed exhaustively 10,000+ configs). **d=2 influence spectrum {1/6, 1/4, 1/2}** (all attainable). **Forcing-only families never beat 1/(2d) = 1/4 at d=2.** For any incompatible pair, **Pr[forcing] ≥ 1/2 implies max delta ≥ 1/(8d) = 1/16**, a key barrier for the δ-payment structure. All results proved (not searched), with degree-2 certificate algebra.

### **Refuter-4: eps*_ind(3) = 1/6 with bracket, cheap degree-3 sets (cycle 3, claude-opus-5)**
**Source:** 0023-refuter-4 (cycle 3, claude-opus-5, exhaustive enumeration)  
**Statement:** Over ℤ₂ at degree d=3, **eps*_ind(3) = 1/6** surviving **bracket 1/24 to 1/6** (extremal pairs uniquely characterized). Complete window-6 and window-7 enumerations: **16,750,860 and 126,113,920 patterns** respectively. **Singleton frontier 3/16 for windows ≤ 7.** **Existence of cheap degree-3 sets with all influences 1/8** (proof: explicit construction; key for testing π_Rel lower bounds). **kappa_d ≤ d certified for every N by two independent linear systems mod two primes** (proof: SDP certificates + rational verification).

### **Refuter-5: Proved relevance-payment floor min π_Rel = 1 exactly (cycle 3, claude-opus-5)**
**Source:** 0023-refuter-5 (cycle 3, claude-opus-5, rigorous case analysis)  
**Statement:** **min π_Rel = 1 exactly**, holding for **all N, all d, attained iff the two sides share exactly one relevant coordinate** (proved not searched). **|S| ≥ 2 branch infimum = 1 unattained** (limit of sequences; rigorous proof via cross-disjoint structure + forcing argument). **Surplus 1/(2^(d-1)-1)** as the asymptotic excess above the floor. Non-Boolean group floor: searched-but-unproved (no proof found despite exhaustive optimization at small d; conjectured tight but status OPEN).

### **Refuter-6: Gap G5 settled, minimal vs minimum selection window; envelope conjecture refuted (cycle 4, claude-opus-5)**
**Source:** 0023-refuter-6 (cycle 4, claude-opus-5, verified certificate)  
**Statement:** **Gap G5 positively settled for uniform-point minimal selections:** expected window size **d + O(log d log log d)**. Negative half: deterministic rule on minimal selections gives ratio exactly **2^(-d)** (selection must be over uniformly random point). **Affine class capped.** **Refuter refuted its own envelope conjecture** with verified certificate; this statement kills the payment-hypothesis route at its final step, yielding only exponential thresholds for universal window selection.
**Verification:** Certificate-backed; verifiable in all three independent modes (computational, combinatorial, isoperimetric).

### **Refuter-7: Hub witness and direct-sum analysis; coordinate-wise influence floor (cycle 4, claude-opus-5)**
**Source:** 0023-refuter-7 (cycle 4, claude-opus-5, blind test by construction)  
**Statement:** On hub witness and its direct sums, payment does NOT decay with d (would falsify the payment hypothesis at its root). **Test was blind by construction.** Real finding: **every relevant coordinate carries influence ≥ 2^(-1-d)**. For d ≤ 16, window is entire relevant set and payment ≥ 1 trivially; **all meaningful content at d ≥ 17** (window-scaling regime). Confirms refuter-6 threshold boundary.
**Verification:** Blind design; test-replication constraints prevent backfit.

### **Refuter-8: GAP-3 Refuted in its Branch; exhaustive certificate (cycle 4, claude-opus-5)**
**Source:** 0023-refuter-8 (cycle 4, claude-opus-5, exhaustive verification)  
**Statement:** **GAP-3 REFUTED IN BRANCH** with certificate at degree 120, dimension 188. Verified **three exact ways over 7004 instances.** Refuting family crosses threshold **only from degree 53 onward** (no small-dimension instances); exhaustive search at degrees ≤ 52 rules nothing out, rules full space in. Certificate is multiscale and portable.
**Verification:** Three independent verification channels (certificate algebra, combinatorial tallying, isoperimetric lower-bound matching). 7004 instances: each certified independently; no batch-arithmetic vulnerability.

---

## DEAD PLANS

### R1 falsification honeypot (cycle 2, 0023-refuter-2)
**Status:** DEAD. **Reason:** Exact exhaustive search (all 984,858 (pattern, window) pairs k≤4, 200,000 random k∈[5,12], 1,712 stochastic free-form families, all structured architectures) yields ε*_junta(d)=1/(2d) exactly, grid-attained, via the isoperimetry chain F1–F4→(M). No construction beats the grid constant; pattern richness cannot push the frontier below Θ(1/d). The search is terminated not by resource exhaustion but by a fully quantitative obstruction, eliminating falsity via five elementary counting steps verified in exact arithmetic at scale. Falsity would contradict Harper's hypercube edge-isoperimetric inequality.

### Scout-2 prior-art candidates (cycle 2, 0023-scout-2)
**Status:** DEAD. **Reason:** Micro-scout on rung R1 as a standalone combinatorial object found no literature match. Killed approaches: (i) ALWZ spreadness — low average influence does not imply low window membership; the rung's content is the gap between them (scout-2 §C2). (ii) Cross-intersecting families — the polarity is wrong; literature requires cross-MEETING families (agreement), not cross-DISJOINT (conflict); measure mismatch (counting vs influence) (scout-2 §B4). (iii) Subcube partitions — single-family partitioning only, no two-family cross structure, no influence hypothesis (scout-2 §B5). (iv) Conflict complexity — runs over query-process distributions on 0/1-inputs, not over certificate/pattern families with influence caps (scout-2 §B6). (v) AA-conjecture specialisations — proved cases are single-function only; no pair/cross-disjoint variant found; Boolean-valued statements are classical but exponential-influence only (scout-2 §B7). Verdict: NO PRIOR RESOLUTION FOUND stands.

### Scout-3 KKDWY26 possibility (cycle 2, 0023-scout-3)
**Status:** DEAD. **Reason:** Full read of arXiv:2601.08727v2 (deciding source identified in scout-2 §E) resolved whether KKDWY26 hides a distributional or influence-type statement about disjoint-support families. Outcome: no distributions over polynomials, no families (every result per-function or per-pair), no spread, no influence HYPOTHESIS in any theorem, and the only influence CONCLUSIONS are in the exponential regime (2^{-2·rdeg}), already covered by card S1 (ACC22 Thm 4.4). Theorem 4 confirms S3a's $16d^4$ constant; Theorem 10 (only pair statement) is unusable for I01 (fails the everywhere-promise). Scout-3 §E verdict: outcome (i) of scout-2 prediction (no distributional statement). Possibility killed: KKDWY26 does not settle or partially settle I01.

### Plan P1 key step (cycle 3, killed by 0023-prover-2)
**Status:** DEAD. **Reason:** Prover-2's hub family with payment d·2^(1-d), machine-verified to d=12, refutes the payment denominated in relevance/junta windows (PAY*), killed by refuter-3 killer (a): forcing-only families never beat 1/(2d). Min-form route needing min(Inf_i f, Inf_i g) large: killed by refuter-3 killer (b) and strengthened to sum-form (shown by prover-3). Junta-substitution route with explicit ceiling: killed entirely.

### Strategist milestone: find cross-disjoint pair with relevance payment < 1 (cycle 3)
**Status:** CLOSED NEGATIVELY. **Reason:** Refuter-5 proved the floor is exactly 1 (all N, all d, attained iff the two sides share exactly one relevant coordinate). **This milestone must not be re-run.** Recorded as CLOSED-NEGATIVE per campaign protocol.

### R2 per-coordinate influence budget (cycle 3, killed by 0023-prover-3)
**Status:** DEAD. **Reason:** Intermediate I02's own total-influence-budget suggestion in its per-coordinate form, killed by prover-3 before r2 revision; per-coordinate model provably insufficient; shifted to window-coordinate model.

### Singletons-are-protected claim (cycle 3, killed by 0023-refuter-4)
**Status:** DEAD. **Reason:** Claim that singletons are protected by Aaronson-Ambainis: refuter-4 produces cheap degree-3 sets with all influences 1/8 at all coordinates, contradicting the singleton protection. Barrier claim killed entirely.

### Whole-class barrier and "value = 0" claims (cycle 3, killed by 0023-prover-3-r2)
**Status:** DEAD. **Reason:** Prover-3 and revision r2 killed the whole-class barrier claim and all "value = 0" and "value ≥ " claims by explicit construction of counterexamples. These were the CAP I and CAP II barrier claims; not accepted on r2 re-verification.

## REFUTED / KILLED (cycle 4)

1. **Spread-or-subcube dichotomy (killed by prover-4-u3)** — exact family counterexample with payment carried outside monomial supports; dichotomy does not hold under the framework.

2. **GAP-3 as stated, in its branch (killed by refuter-8, certificate)** — refuted with exhaustive certificate at degree 120, dimension 188, verified three independent ways over 7004 instances.

3. **Monomial-only payment sub-route (killed by prover-4-u3, tight bound)** — closed by Θ(d 2^(-d)) isoperimetric bound; cannot exceed this asymptotically. Dead end on universal payment.

4. **Refutation shape requiring balanced degree-D Boolean function with all influences exponentially small (killed by scout-6)** — impossible by max-influence lower bound theorem (known 2005 result, ≥ Ω(Var/deg⁴)); scout-6 carding prevents the falsification attempt.

5. **Refuter-6's own envelope conjecture (killed by refuter-6)** — refuted with verified certificate; window-size envelope does not scale polynomial; kills payment-hypothesis route at its final step.

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
- **S6-junta-degree-card.md** (id: S6, carded 2026-08-27 cycle 3, [READ] blocks S6a–S6d): **Junta size bounds and Nisan–Szegedy theorem:** [READ] blocks S6a–S6d: junta size **bracketed** $3 \cdot 2^{d-1}-2 \le M(d) \le 4.394 \cdot 2^d$ (upper bound from Wellens' 1973 result, lower bound from Chiarelli–Hatami–Saks 2009). **Nisan–Szegedy's own 1994 print [RESTATED]** via two read intermediaries (cite by content, not theorem number); both sides' key lemmas restated with proof sketches. **Per-coordinate influence quantum:** $2^{-1-d}$ exactly attained by $\text{AND}_d$ and $\text{OR}_d$ (no function of max-influence < 1/2d can govern the full class at degree d). All values carded; one [MEMORY]-grade fact refuter-5 flagged for carding before any prover cites it: the edge-isoperimetric equality case (currently used in R1 proof, holds by induction).
- **S7b-changfang26-card.md (addendum block)** (id: S7b, carded 2026-08-27 cycle 3, [READ] addendum): **Chang-Fang Corollary 3.4, p. 7:** Group-uniform property for **every finite abelian group and every nonzero degree-≤d C-valued f**, there exists a window of size ≤ d whose complement's support projects onto a hyperplane (statement printed identical to the Contract's degree notion). [READ] verified independently against PDFs; one non-mathematical correction applied: the source is post-referee review, not unrefereed.
- **S8-max-influence-status-card.md** (id: S8, carded 2026-08-28 cycle 4, [READ]): **Max-influence lower bound as known theorem.** Single-function statement **max influence ≥ Ω(Var/deg⁴)**, a known 2005 result. Strictly **weaker than Aaronson-Ambainis** (exponential vs polynomial regime). **QUARANTINED ATTRIBUTION:** the cubic decision-tree bound must NOT be cited to Midrijanis (attribution error in secondary sources; originality flags under review). Card status: [READ], used to kill scout-6 falsification attempt.
- **S9-osss-card.md** (id: S9, carded 2026-08-28 cycle 4, [READ]): **OSSS inequality and tight window formulation.** Ostrowski-Schramm-Servedio-Szegedy family-influence theorem and its window specialisation. [READ]; used in plan P4 (bounded-support weakening) analysis.

**QUEUE (ranked by load-bearing impact):**
Two latent items only, needed nowhere yet: (i) **internals of KKDWY26** (Theorem 9 proof techniques), (ii) **Mid04** (quant-ph/0403168 internal proofs) — both below bar for prover work given current queue. **One [MEMORY]-grade fact refuter-5 flagged:** edge-isoperimetric equality case for carding before any prover cites it.

**DECLINED:** none.

**Unissued source ids (monotone-id note, §2.2):** **S4 was never issued** — the
R1 micro-scout (`0023-scout-2`) found nothing that cleared the card bar, so the
next card took id S5. S4 must never be reused.

---

## PROCESS NOTES (cycle 4, transcription of operational constraints and corrections)

*This section records process rather than mathematical content; it exists to preserve operational state for resume and accountability.*

1. **Prover output-cap overflow (cycle 4, Fixed):** Two prover runs (exploratory attempts u0-draft and u2-draft) died on the 64k per-response output ceiling and emitted nothing. Workaround: split into one small scoped run per unit (u0, u1, u2, u3, u4 as five separate messages). This worked; all five units emitted complete.

2. **Git checkout error in shared working tree (cycle 4, Resolved):** A repeated `git checkout main` in the campaign's shared working tree silently DELETED 21 merged campaign artifacts from disk (proofs/*cycle-2*.md, proofs/*cycle-3*.md, sources/*.md from prior commits). Local main could not fast-forward; checkout was cancellation under git-internal semantics. Subagent u4 (the branch-exclusion unit) had no access to the actual prover-3-r3 output and guessed a definition, then reported a SPURIOUS defect against u3's carry-forward from u2 (exact-branch emptiness). Files were restored from origin/main. **Future constraint: main is not to be checked out in this tree; keep work on feature branches.**

3. **u4's defect claim against u3 — OVERRULED (cycle 4, Adjudicated):** u4 claimed the monomial payment (u3's core result) is not a lower bound on the window payment (u2's output). **Ruling:** The window contains the monomial support by definition of the window. The inequality is immediate from set inclusion. Claim is retracted and does not stand. (The confusion arose from the missing context: u4's first read of u3 was a guess, not the actual artifact.) Marked as OVERRULED in this ledger rather than returned to u4 for revision.

## RETREAT LOG

**Cycle 3 note:** No retreat. R2 is OPEN, not stalled. Stall criteria not met: (i) plans P2/P4/P5 untried, (ii) source queue empty, (iii) only one cycle on this rung.

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
| I02-degree-d-sets | intermediates/I02-degree-d-sets.md | case-planner | claude-opus-5 | 3 | ACTIVE TARGET / OPEN | rung R2; proved at d=2 with optimal constant 1/4 and every delta below exponential threshold; content window open; CAP I/II barrier claims submitted post-triage (NOT accepted), re-verification in flight |
| 0023-scout-4 | proofs/0023-scout-4.md | scout | claude-opus-5 | 3 | COMPLETE | rung R2 micro-scout; verdict NO PRIOR RESOLUTION FOUND; literature on degree-d sets and influence asymptotics scanned; no degree-d junta-payment theorem found matching Contract structure |
| 0023-scout-5 | proofs/0023-scout-5.md | scout | claude-opus-5 | 3 | COMPLETE | rung R2 extended scout on related degree-d constructions; verdict: PARTIALLY SETTLED (Chang-Fang bounds the core structure; Nisan-Szegedy carded as S6); no complete prior theorem |
| 0023-refuter-3 | proofs/0023-refuter-3.md | refuter | claude-opus-5 | 3 | COMPLETE | degree d=2: eps*_ind(2)=1/4 all N (proved, not searched); M(2)=4 confirmed; influence spectrum {1/6,1/4,1/2}; forcing-only barrier; delta payment structure constraints; two killers (a) forcing-only, (b) sum-form strengthening |
| 0023-refuter-3-code | proofs/0023-refuter-3-code/ | refuter | — | 3 | COMPLETE | reproducible code: junta_d2_lib.py + analysis scripts; d=2 exhaustive proofs with certificate algebra |
| 0023-refuter-4 | proofs/0023-refuter-4.md | refuter | claude-opus-5 | 3 | COMPLETE | degree d=3: eps*_ind(3)=1/6 bracket 1/24–1/6; 16.75M and 126M pattern enumerations (windows 6,7); singleton frontier 3/16; cheap degree-3 sets (all influences 1/8); kappa_d <= d certified by two linear systems mod primes |
| 0023-refuter-4-code | proofs/0023-refuter-4-code/ | refuter | — | 3 | COMPLETE | reproducible code: junta_d3_lib.py + window enumerations; full rational arithmetic |
| 0023-refuter-5 | proofs/0023-refuter-5.md | refuter | claude-opus-5 | 3 | COMPLETE | Proved: min π_Rel=1 exactly (all N, all d; attained iff one relevant coordinate shared); |S|≥2 infimum 1 unattained; surplus 1/(2^(d-1)-1). Non-Boolean floor: searched-but-unproved (status OPEN) |
| 0023-refuter-5-code | proofs/0023-refuter-5-code/ | refuter | — | 3 | COMPLETE | reproducible code: relevance_payment_lib.py + proofs of floor exactness |
| 0023-strategist-2 | proofs/0023-strategist-2.md | strategist | claude-opus-5 | 3 | COMPLETE | six re-ranked plans P1–P6 for I02 rung (R2); P1 key step killed by refuter-3; P6 delivered barrier (same obstruction as R1); P2/P4/P5 remain untried; strategic implication: one ascent direction exhausted, three lateral routes available |
| 0023-prover-2 | proofs/0023-prover-2.md | prover | claude-opus-5 | 3 | PARTIAL | independent poly(d)-window route for R2 at every delta < 2^-d/d; positivity lemma (shattering window structure); (PAY**) recorded OPEN (would imply every balanced Boolean function has high-influence coordinate, but premise falsified by refuter-3) |
| campaign/lean/0023-prover-2-skeleton.lean | campaign/lean/0023-prover-2-skeleton.lean | prover | — | 3 | PARTIAL FORMALIZATION | Lean statement skeleton for prover-2 results; proof status INCOMPLETE |
| 0023-prover-3 | proofs/0023-prover-3.md | prover | claude-opus-5 | 3 | SUPERSEDED-BY 0023-prover-3-r2 | initial cycle-3 attempt on I02; five blind passes (A-E: two verifiers); RAW: NOT CLEAN, CLEAN, CLEAN, DEFECTS, DEFECTS; POST-TRIAGE: passes B,C ruled WRONG (cleared 4 upheld defects each); triage outcome 10 upheld/9 overruled/6 pedantic; four passes self-disclosed ledger/progress-read outside blind gate; CAP I/II barrier claims NOT ACCEPTED |
| 0023-prover-3-verify-A | proofs/0023-prover-3-verify-A.md | verifier | claude-fable-5 | 3 | COMPLETE | blind pass A on prover-3: agent verifier family; RAW NOT CLEAN; POST-TRIAGE NOT CLEAN |
| 0023-prover-3-verify-B | proofs/0023-prover-3-verify-B.md | verifier | claude-fable-5 | 3 | COMPLETE | blind pass B on prover-3: agent verifier family; RAW CLEAN; POST-TRIAGE RULED WRONG (cleared 4 upheld defects) |
| 0023-prover-3-verify-C | proofs/0023-prover-3-verify-C.md | verifier | claude-fable-5 | 3 | COMPLETE | blind pass C on prover-3: agent verifier family; RAW CLEAN; POST-TRIAGE RULED WRONG (cleared 4 upheld defects) |
| 0023-prover-3-verify-D | proofs/0023-prover-3-verify-D.md | verifier | claude-opus-5 | 3 | COMPLETE | blind pass D on prover-3: agent verifier-b family; RAW DEFECTS; POST-TRIAGE DEFECTS |
| 0023-prover-3-verify-E | proofs/0023-prover-3-verify-E.md | verifier | claude-opus-5 | 3 | COMPLETE | blind pass E on prover-3: agent verifier-b family; RAW DEFECTS; POST-TRIAGE DEFECTS |
| 0023-prover-3-triage | proofs/0023-prover-3-triage.md | triage | — | 3 | COMPLETE | triage ruling: 10 upheld, 9 overruled, 6 pedantic, 0 needs-source, 0 unclear; passes B,C ruled WRONG; process note: four passes read LEDGER.md or PROGRESS.md outside blind view, all self-disclosed; root cause fixed in r2 |
| 0023-prover-3-r2 | proofs/0023-prover-3-r2.md | reviser | claude-opus-5 | 3 | PARTIAL / REVISION CYCLE 1 | revised prover-3 addressing upheld defects; CAP I and CAP II barrier claims resubmitted; re-verification in flight (passes F/G pending); NOT YET ACCEPTED |
| 0023-prover-3-r2-code | proofs/0023-prover-3-r2-code/ | reviser | — | 3 | PARTIAL | reproducible code for r2 revisions |
| 0023-prover-3-r2-verify-F | proofs/0023-prover-3-r2-verify-F.md | verifier-b | claude-opus-5 | 3 | PENDING | re-verification pass F on prover-3-r2; status PENDING |
| 0023-prover-3-r2-verify-G | proofs/0023-prover-3-r2-verify-G.md | verifier | claude-fable-5 | 3 | PENDING | re-verification pass G on prover-3-r2; status PENDING |
| S6-junta-degree-card | sources/S6-junta-degree-card.md | scout | — | 3 | IN LIBRARY ([READ]) | Junta size bounds (Wellens upper, Chiarelli–Hatami–Saks lower), Nisan–Szegedy theorem (restated via intermediaries), influence quantum 2^(-1-d) attained by AND_d/OR_d; [MEMORY] flag on edge-isoperimetric equality case |
| S7-changfang26-card (S7b addendum) | sources/S7-changfang26-card.md | scout | — | 3 | IN LIBRARY ([READ]) | S7b addendum: Chang-Fang Cor. 3.4, group-uniform window property for degree-≤d, post-referee source, one non-math correction applied |
| 0023-scout-6 | proofs/0023-scout-6.md | scout | claude-opus-5 | 4 | COMPLETE | falsification attempt: seek balanced degree-D Boolean function with exponentially small influences; killed by S8 max-influence theorem (known result, strictly weaker bound) |
| S8-max-influence-status-card | sources/S8-max-influence-status-card.md | scout | — | 4 | IN LIBRARY ([READ]) | Max-influence lower bound ≥ Ω(Var/deg⁴), known 2005 theorem, strictly weaker than Aaronson-Ambainis; quarantined attribution (cubic decision-tree bound not to be cited to Midrijanis) |
| S9-osss-card | sources/S9-osss-card.md | scout | — | 4 | IN LIBRARY ([READ]) | OSSS inequality and tight window formulation; used in plan P4 analysis |
| 0023-refuter-6 | proofs/0023-refuter-6.md | refuter | claude-opus-5 | 4 | COMPLETE | Gap G5 settled: minimal-point selection window size d + O(log d log log d), deterministic rule 2^(-d), affine class capped; refuter's envelope conjecture refuted with certificate |
| 0023-refuter-6-code | proofs/0023-refuter-6-code/ | refuter | — | 4 | COMPLETE | reproducible code for G5 settlement and envelope refutation |
| 0023-refuter-7 | proofs/0023-refuter-7.md | refuter | claude-opus-5 | 4 | COMPLETE | Hub witness and direct-sum payment analysis; every relevant coordinate carries influence ≥ 2^(-1-d); meaningful content only at d ≥ 17; test was blind by construction |
| 0023-refuter-7-code | proofs/0023-refuter-7-code/ | refuter | — | 4 | COMPLETE | reproducible code for hub-witness analysis and coordinate-wise floor |
| 0023-refuter-8 | proofs/0023-refuter-8.md | refuter | claude-opus-5 | 4 | COMPLETE | GAP-3 refuted in branch: certificate at degree 120, dimension 188, verified three ways over 7004 instances; refuting family crosses threshold only from degree 53 |
| 0023-refuter-8-code | proofs/0023-refuter-8-code/ | refuter | — | 4 | COMPLETE | reproducible code for GAP-3 branch refutation and multiscale certificate verification |
| 0023-prover-4-u0 | proofs/0023-prover-4-u0.md | prover | claude-opus-5 | 4 | COMPLETE | Unit 0: setup and framework; dense-pair constraint introduction |
| 0023-prover-4-u1 | proofs/0023-prover-4-u1.md | prover | claude-opus-5 | 4 | COMPLETE | Unit 1: rungs L1–L3 proved unconditionally with no gaps |
| 0023-prover-4-u2 | proofs/0023-prover-4-u2.md | prover | claude-opus-5 | 4 | COMPLETE | Unit 2: rung L4 proved unconditionally but only at payment 2^(1-d), exponential; kills main payment route |
| 0023-prover-4-u3 | proofs/0023-prover-4-u3.md | prover | claude-opus-5 | 4 | COMPLETE | Unit 3: monomial-only sub-route closed by Θ(d 2^(-d)) tight bound; true payment outside monomial supports |
| 0023-prover-4-u4 | proofs/0023-prover-4-u4.md | prover | claude-opus-5 | 4 | COMPLETE | Unit 4: branch excludes certified witness; exact branch empty at zero; sub-hypothesis nowhere |

---

## NEXT ACTION (exactly one)

**HUMAN GATE — select the next plan for rung R2 (I02), given that the lead payment route is refuted at its final step.** See candidates below. Harness stall criteria are NOT met: three plans untried, source queue empty, cycle 4 complete (plan gate open).

### Gate state, 2026-08-28 (cycle 4 fully closed)

**Lead payment route REFUTED.** Refuter-6 settled G5: minimal selections yield window size d + O(log d log log d), but deterministic rule is exactly 2^(-d). Refuter-7 confirms: on hub witnesses, every coordinate carries influence ≥ 2^(-1-d), so content only at d ≥ 17. Refuter-8 refutes GAP-3 in its own branch with multiscale certificate. Prover-4 proved L1–L3 unconditionally but L4 only at exponential payment 2^(1-d). Monomial sub-route closed by tight Theta(d 2^(-d)) bound. R2 conditional on both densities ≥ 1/poly(d); sparse pairs untouched and now the whole remaining difficulty.

### Candidates for next plan on R2

### Plan candidates (cycle 4, decision point)

Rung R2 (I02) is ACTIVE and OPEN. The payment-hypothesis route is DEAD (refuter-6 settled G5 to exponential, refuter-7 confirms on hub witnesses, refuter-8 refutes GAP-3 in branch, prover-4 proved only at payment 2^(1-d)). Prover-4 results hold **conditionally** on both densities ≥ 1/poly(d). Sparse pairs remain the whole remaining difficulty. Strategist plan set is `0023-strategist-2`; P1 key step refuted; P6 discharged (payment barrier). Three plans remain untried:

- **P2 (direct construction, fibre-wise).** Aims at FIBRE BALANCE obstruction: influence identity holds fibre-wise, but fibre normalisation differs from hypothesis, leaving exponential floor in the weight. Best R3-liftability prospect of the set. Strategist rank: second among untried.

- **P4 (weakening: bounded support).** Would establish R2 at every fixed support size, proving R2's content is pure dilution by rescaling. Declared an R3 detour. **Now un-gated: S9 (OSSS card) now cached.** Strategist rank: third.

- **Continuing payment route under dense-pair assumption.** Separate argument for sparse pairs; keep prover-4's conditional result independent; later unify if dense-pair case breaks. Orchestrator's recommended primary path.

Also available, not a plan: **Formalizer on frozen I01** (per §2.4 formalization protocol, non-blocking).

**Cycle 4 SUMMARY (CLOSED 2026-08-28):**
- **Scout cycle closed.** 0023-scout-6: falsification attempt on balance; killed by S8 (max-influence lower bound, known 2005 theorem, strictly weaker than AA). S8 and S9 cards cached.
- **Refuter cycle closed.** 0023-refuter-6: G5 settled (minimal window d + O(log d log log d), deterministic 2^(-d), affine capped); envelope conjecture refuted. 0023-refuter-7: hub witnesses; every coordinate influence ≥ 2^(-1-d), d ≥ 17 meaningful content. 0023-refuter-8: GAP-3 refuted in branch (certificate degree 120, dim 188, three-way verified over 7004 instances; threshold from degree 53).
- **Prover cycle closed.** 0023-prover-4 (five units u0–u4): L1–L3 proved unconditional (u1); L4 proved only at exponential 2^(1-d) (u2); monomial sub-route Theta(d 2^(-d)) closed (u3); branch excludes witness, exact branch empty (u4). R2 CONDITIONAL on densities ≥ 1/poly(d).
- **Nothing entered ESTABLISHED.** Five-pass acceptance gate remains unmet; prover-4 is CONDITIONAL pending dense-pair proof.
- **Five items KILLED/REFUTED.** Spread-or-subcube dichotomy; GAP-3 branch; monomial-only sub-route; falsification shape; refuter-6 envelope conjecture.
- **Process notes recorded:** output-cap workaround (five units), git-checkout file deletion (restored), u4 defect claim overruled.

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
- **Verified intermediate I01 (rung R1), FROZEN:** ε*_junta(d)=1/(2d), δ(d)=1/(3d), witnesses c₁=1/3, c₂=1; proof artifact 0023-prover-1 (evicted from context); 5/5 blind passes post-triage-clean + blind gate CLEAN; cycle 2 all verdicts recorded.
- **Active target I02 (rung R2), OPEN + CONDITIONAL:** degree-d set rung; proved at d=2 with optimal constant 1/4 and every delta below exponential threshold. **Cycle 4 refutation:** lead payment route dead (G5 exponential, GAP-3 refuted, L4 only 2^(1-d)). **Cycle 4 prover results:** L1–L3 unconditional; L4 and monomial sub-route exponential only; R2 conditional on both densities ≥ 1/poly(d); sparse pairs untouched (whole remaining difficulty). Nothing entered ESTABLISHED.
- Cycles 1–3 Scout verdicts (NO PRIOR RESOLUTION FOUND; prior-art routes killed). Cycle 4 scout-6: falsification attempt killed by S8.
- Cycle 2 KKDWY26 full read and S5 card; S3a residual lifted.
- Cycle 2 Refuter (exact frontier ε*_junta=1/(2d); Harper isoperimetry; falsity ruled out).
- Cycle 2 Prover (I01 proved; lemma chain F1–F4→(M); proof FROZEN).
- Cycle 2 Verification (5 blind, triage, blind gate all CLEAN → FROZEN).
- Cycle 3 Computationally certified (refuter-3/4/5 results on d=2,3 frontiers; relevance-payment floor; CAP I/II NOT ACCEPTED).
- Cycle 3 Conditional (prover-2 partial; refuter-5 non-Boolean floor OPEN).
- Cycle 4 Computationally certified (refuter-6/7/8: G5 settled, hub witness analysis, GAP-3 refuted in branch).
- Cycle 4 Conditional (prover-4 five units: L1–L3 unconditional, L4 and sub-routes exponential, dense-pair constraint).
- Killed/Refuted (spread-or-subcube, GAP-3 branch, monomial sub-route, falsification shape, envelope conjecture; five items cycle 4).
- Cycle 3 Killed plans (P1, (PAY*), (PAY**), min-form route, junta-substitution, singleton protection, barrier claims).
- Six independent attack plans P1–P6 (cycle 1 Strategist); cycle 3 Strategist re-ranked; cycle 4: P2/P4 un-gated, P1 dead.
- Complete case ladder R0–R6 (PROGRESS.md, approved cycle 1).
- Nine source cards (S1, S2, S3a/S3b, S5, S6, S7b, S8, S9) with annotations on S1 (cycle 2), S7b (cycle 3), S8 quarantine (cycle 4).
- Process notes recorded (cycle 4): output-cap workaround, git-checkout deletion incident, u4 defect overruled.
- **Next action fully specified:** HUMAN GATE — choose next plan for R2 given payment route refuted. Three candidates: P2 (fibre-wise direct), P4 (bounded-support weakening, un-gated), or continue payment route separately on dense pairs. Harness stall criteria NOT met.

---

---

### LEDGER PATCH, cycle 4, sections: HEADER (cycle 4 closed 2026-08-28, R1 FROZEN, R2 ACTIVE+OPEN, payment route REFUTED), COMPUTATIONALLY CERTIFIED (+refuter-6/7/8 cycle-4 results), CONDITIONAL (+prover-4 five-unit chain, dense-pair constraint), REFUTED/KILLED (+five items: spread-or-subcube, GAP-3 branch, monomial sub-route, falsification shape, envelope conjecture), SOURCE LIBRARY (+S8 max-influence card, S9 OSSS card), MANIFEST (+15 cycle-4 artifact rows), PROCESS NOTES (new: output-cap workaround, git-checkout incident, u4 defect ruling), NEXT ACTION (HUMAN GATE, three plan candidates: P2/P4/dense-pairs), Resume test — date 2026-08-28 ###
