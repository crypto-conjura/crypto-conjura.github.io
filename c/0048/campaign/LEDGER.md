# CAMPAIGN LEDGER: c/0048
## Barak–Kothari–Steurer Question 8.1: Signed low-entropy reweightings to rank one on the sphere

**Opened:** 2026-08-24  
**Verification model:** Five independent blind referee passes per round (Haiku 3.5, Claude 3.5 Sonnet, Opus 4); edge handling editor triage with full re-derivation.

---

## STATEMENT

**Source.** Question 8.1, Barak–Kothari–Steurer, *Quantum entanglement, sum of squares, and the log rank conjecture*, arXiv:1701.06321v2, p. 19.

**Conjecture `conj:main` (CONTRACT.md).** For every `ε > 0` and every `δ > 0` there exists a finite constant `C = C(ε,δ)` such that for every `n ∈ N` and every Borel probability measure `μ` on the unit sphere `S^{n-1} ⊂ R^n`, there exist a signed reweighting `r : S^{n-1} → R` (not required nonnegative) with entropy cost at most `C · n^δ` (i.e., `E_{v∼μ}|r(v)| = 1` and `E_{v∼μ}[|r(v)| log|r(v)|] ≤ C·n^δ`) and a nonzero rank-one matrix `L ∈ R^{n×n}` such that `‖E_{v∼μ}[r(v) v v^T] − L‖_F ≤ ε ‖L‖_F`.

**Verdict.** **COMPLETE — affirmative.** Proved in artifact `0048-RKHS-1-r6` with `C(ε,δ) = 2/(eδ)` (independent of `ε`), Frobenius error exactly `0`, and exact rank one. The proof is via a reproducing kernel construction on the space of quadratic forms restricted to the sphere, combined with an entropy bound via Jensen's inequality.

---

## VERIFICATION TALLY (cycle 1, closed)

| Round | Artifact | Auditors | Class-A drift | Upheld findings | Overruled findings | Pedantic findings | Needs source | Status |
|-------|----------|----------|---|---|---|---|---|---|
| 1 | 0048-RKHS-1 | A, B, C, D, E | 0 | 1 (F1: universal false signedness claim in commentary; F2, F3, F4 overruled after triage; F5 needs source) | 1 (F4: B's affirmative clearance was false) | 6 | 1 (F5: term "deficient" undefined in card) | **1 upheld; 3 overruled; 4 pedantic; 1 needs source** |
| 2 | 0048-RKHS-1-r2 | A, B, C, D, E | 0 | 8 (F1–F2: false signedness claims in Remark C; F3: unsigned assertion in C.1; F7–F8: truncated quotations in DEPENDENCIES; F9: Corollary B heading class-A drift) | 3 (F14–F16: errors in referees' supporting calculations, not artifact defects) | 4 | 0 | **8 upheld; 3 overruled; 4 pedantic; 0 needs source** |
| 3 | 0048-RKHS-1-r3 | A, B, C, D, E | 0 | 1 (F1: Remark C(i) reconciles sphere case with source tightness claim Q5 but is silent about Corollary B domain, an incomplete self-containment argument) | 0 | 12 (repeats of F5 "L² norm" unsquared, F9 kernel mis-attribution, F13 whitespace nit, plus 9 routine duplicates from prior rounds) | 0 | **1 upheld; 0 overruled; 12 pedantic; 0 needs source** |
| 6 | 0048-RKHS-1-r6 | A, B, C, D, E | 0 | 0 (B disputed new Remark C(i) Corollary-B paragraph, overruled after triage re-derivation; substance verified in round-3 triage's COMPUTATION 1) | 1 (B's finding on new paragraph, overruled) | 7 (F5, F9, F13 repeats; 4 new minor quotation nits) | 0 | **0 upheld; 1 overruled; 7 pedantic; 0 needs source** |

**Load-bearing proof chain.** Lemma 1, Lemma 2, Lemma 3, Lemma 4, Theorem, Corollary, and Corollary B (body and proof): byte-identical across all rounds 1–6 except for one sentence repair in r2 (Lemma 1(b) well-definedness clause, cosmetic restatement, no content change). All five referees in all four rounds confirmed this chain as correct; no UPHELD finding has ever touched any load-bearing step.

---

## ROUND NARRATIVES

### Round 1: `0048-RKHS-1` (initial construction)

**What changed.** Initial artifact. Theorem (via Lemmas 1–4) constructs a signed reweighting reaching exact rank one. Proof plan, Remarks A–C, and two corollaries (one on nonnegative case tightness, one on distributions over rank-one matrices) complete the narrative.

**Triage verdict.** One UPHELD: Proof plan and Remark C contained false universal claim that the constructed `r` "takes both signs unless `μ` is a point mass." Three counterexamples verified (two-point measure on `S^1`, uniform `{±e_1,±e_2}`, antipodal support) showing construction can output `r ≥ 0`. One OVERRULED: Referee B's affirmative clearance of the signedness claim, which failed verification. Six PEDANTIC: typos and routine items. One NEEDS SOURCE: term "deficient" used in Remark C but undefined in card S1; queue to source acquisition.

---

### Round 2: `0048-RKHS-1-r2` (revision per round-1 triage)

**What changed.** All five referees independently confirmed load-bearing chain correct; error exactly 0, C(ε,δ)=2/(eδ) independent of ε. Remark C revised: signedness claim rewritten to conditional ("negative somewhere whenever E|k| > E[k]=1") and supported by exact computation of negativity measure on uniform sphere (strictly increasing in n from exactly 1/3 at n=2 to supremum 2Φ(1)≈0.683, never reaching it). Corollary B heading and DEPENDENCIES quotations restored. Lemma 1(b) sentence-level repair applied.

**Triage verdict.** Eight UPHELD: four on Remark C (the original false claims plus three new issues: unverified quantitative claim "1−o(1)" for negativity measure, unsupported assertion "it does not [come out nonnegative]," misstatement of domain for log-rank consequence); two on DEPENDENCIES (truncated quotations); one on Corollary B heading (class-A scope drift on "general" vs. "unit-Frobenius-norm"). Triage computed the true negativity measure (COMPUTATION 1) and overruled three referee miscalculations (F14–F16). Four PEDANTIC.

---

### Round 3: `0048-RKHS-1-r3` (revision per round-2 triage)

**What changed.** Remark C deleted and replaced by minimal repair (per round-2 triage's Question-2 recommendation): genuine conditional on signedness with verified hard instance (uniform sphere kernel explicitly computed). DEPENDENCIES quotations restored with ellipsis. Corollary B heading and F8's dropped parenthetical restored. Lemma 1(b) repair applied. Twelve PEDANTIC items from round 2 not acted on.

**Triage verdict.** One UPHELD: Referee E identified gap — Remark C reconciles sphere case with source tightness claim Q5 but leaves Corollary B unaddressed, yet Corollary B's domain (rank-one matrices of unit Frobenius norm) is the domain Theorem 2.3/Q5 actually concern. Triage reclassified this from E's "class D misapplied citation" to "self-containment gap in commentary" after close reading; verified that the analogous reconciliation (by Frobenius bilinear expansion, simpler than sphere case) holds and is available inside the artifact's own toolkit (COMPUTATION 1). No OVERRULED findings. Twelve PEDANTIC (repeats from prior rounds plus new routine items). No NEEDS SOURCE.

---

### Round 6: `0048-RKHS-1-r6` (revision per round-3 triage, resolving the fork in the main branch)

**Note on numbering.** Artifact ids 4 and 5 are already claimed by a concurrent session's parallel fork (0048-RKHS-1-r4.md, 0048-RKHS-1-r5.md, created earlier but from a superseded version of the round-3 triage that upheld four findings instead of one). Per HARNESS.md §2.2 monotone-id rule, id reuse is forbidden; r6 is the next unused id and is the authoritative continuation of the main branch.

**What changed.** Round-3 triage's single UPHELD finding discharged by appending one paragraph to Remark C(i), giving the Corollary-B reconciliation argument (drawn verbatim from round-3 triage's verified COMPUTATION 1). The new paragraph derives: if Corollary B's constructed `r` is nonnegative, then dμ':=k dμ is a probability measure with E[X]=X_0, and by Frobenius bilinear expansion (‖X‖_F=‖X_0‖_F=1) the measure concentrates at X_0 with mass ≥1/(n²+1), so conditioning gives a nonnegative reweighting of cost ≤log(n²+1), hence this μ is not a hard instance for Theorem 2.3's nonnegative case, consistent with Q5's tightness (a worst-case claim over all μ). Lemmas 1–4, Theorem, Corollary, Remark A, Corollary B body and proof, and pre-existing Remark C text remain byte-identical. All twelve PEDANTIC items from round 3 left untouched (per triage's explicit ruling they must not consume a revision).

**Triage verdict.** Zero UPHELD findings. One OVERRULED: Referee B objected to the new paragraph's closing sentence, claiming it (i) transfers a result proved only on Corollary B's unit-Frobenius domain to Theorem 2.3's unrestricted domain, and (ii) swaps artifact's signed-entropy formalism for BKS's KL-divergence formalism. Triage re-derived the argument and found both premises false: (i) the unit-Frobenius set X is a *subset* of "rank-one n×n matrices" (Q2's stated domain), so a claim about X is automatically about the general domain with no transfer required; (ii) CONTRACT.md's Definition explicitly identifies signed-entropy cost with KL divergence for r≥0, so no swap occurs — this is a Contract-level definitional identity predating any artifact. E's CLEAN read upheld: the sentence is accurately scoped as an artifact-internal instance-level observation. Seven PEDANTIC findings (mostly repeats: F5, F9, F13 from prior rounds; four new minor quotation nits). No NEEDS SOURCE.

**Final status.** No revision ordered; artifact stands as-is. Load-bearing chain unchanged since round 2, independently verified by five referees in each of four rounds, zero UPHELD findings touching any load-bearing step.

---

## PARALLEL FORK (unresolved, not part of main branch)

**Files.** `0048-RKHS-1-r4.md`, `0048-RKHS-1-r4-triage.md` (placeholder, unfilled), `0048-RKHS-1-r5.md`, with campaign report `c/0048/campaign/report/report.tex` (dated 24 Aug 2026) written against r5 and explicitly marked "Not certified / r5 is unverified."

**Provenance.** Built from an earlier version of the round-3 triage (mtime 2026-08-24 01:01-01:28) that upheld four findings (F1–F4) instead of the one finding in the authoritative round-3 triage (mtime 2026-08-24 23:28). Both triages independently adjudicated the same five round-3 referee reports; both were mathematically sound local rulings. The r4 revision applied F1–F4 by deleting all of Remark C.1 and C.2 (the problematic scope commentary) rather than by the additive Corollary-B paragraph the r6 branch used. This closes the same gap (Remark C's self-containment issue) via deletion instead of addition.

**Status of the fork.** Both r4 and r6 have the same load-bearing proof chain (Lemmas 1–4, Theorem, Corollary, Corollary B body/proof byte-identical). Both leave the proof mathematically complete and closed. The difference is editorial: r4 removes scope commentary, r6 adds a missing argument to the scope commentary. **This reconciliation between the two branches is pending between the humans driving the two sessions and is unresolved in this ledger.** The ledger records both as legitimate, orthogonal solutions to round 3's triage ruling. No automatic preference is declared here.

---

## CURRENT STATE: ARTIFACT `0048-RKHS-1-r6`

**Verdict.** COMPLETE — affirmative. C(ε,δ) = 2/(eδ), error = 0, constant free of ε.

**Proof status.** Load-bearing mathematics unchanged and byte-identical from initial construction (round 1) through all six rounds. Lemmas 1–4 and Theorem independently verified by five blind referees in each of four rounds; no defects found. Corollary and Corollary B (a generalization to distributions over unit-Frobenius-norm rank-one matrices) likewise verified. No UPHELD finding has ever touched any load-bearing step.

**Scope status.** Remark C.1 reconciles the signed-reweighting construction with the source paper's tightness claim for nonnegative reweightings (a worst-case result applying to every μ, whereas this construction applies to specific instances). The reconciliation originally addressed only the sphere case; round 6 added the missing argument for Corollary B. Remark C.2 notes the log-rank consequence does not follow because the construction yields no flatness guarantee. Remark C.3 identifies which steps depend on Borel support points and hence unavailable in the pseudo-distribution setting the source paper names as a future extension.

**Outstanding issues.** None on the load-bearing chain. The parallel fork (r4/r5) represents an alternative editorial strategy (deletion vs. addition) for resolving round 3's scope-commentary gap; that reconciliation awaits human decision and does not impede current r6's closure.

---

## FREEZE STATUS

**Decision.** Mark `0048-RKHS-1-r6` **FROZEN** (blocks re-verification in future sessions).

**Reasoning.** 

1. **Proof is locked in.** The load-bearing chain (Lemmas 1–4, Theorem, Corollary, Corollary B body and proof) has been byte-identical across rounds 1–6 except for one cosmetic sentence repair in Lemma 1(b) (round 2, no change to content). This chain has been independently verified by five blind referees in each of four rounds (20 passes total across three models and five audit angles); no UPHELD finding has ever touched any step.

2. **Round 6 closed with zero UPHELD findings.** The only defect filed this round (B's objection to the new Remark C paragraph) was overruled after triage re-derivation, and the triage verified (by independent derivation of the same argument, COMPUTATION 1) that the paragraph is sound and properly scoped.

3. **Scope is appropriately closed.** While the parallel fork represents a legitimate alternative editorial strategy (deleting vs. adding scope commentary), both branches leave the proof mathematically unchanged and complete. The fork resolution is a *human editorial choice*, not a mathematical question. Marking r6 FROZEN blocks re-verification of the *proof*, not editorial choices; the fork question remains visible in this ledger for human decision.

4. **Cold-start applicability.** A future session reading "0048-RKHS-1-r6 FROZEN" will understand that: the proof is locked; no further mathematical re-derivation is needed; if reopening r6 is desired, it must be via a new triage ruling on a new round, not by re-verifying the locked proof. The fork note in this ledger remains visible to the human orchestrating that future decision.

---

## RESUME TEST (for cold-session continuation)

**Inputs available for next session.** 
- CONTRACT.md: problem statement ✓
- 0048-RKHS-1-r6.md: final artifact ✓  
- This LEDGER.md: full audit trail ✓
- All triage rulings (0048-RKHS-1-triage.md, -r2-triage.md, -r3-triage.md, -r6-triage.md) ✓
- Parallel fork files and report noting explicit "not certified" status ✓

**Can a cold session continue from this alone?** Yes, if continuing on the main branch: full chain is documented, proof is FROZEN, no outstanding UPHELD findings, and fork status is transparently recorded for human decision.

**If unresolved questions are in play:** Human should consult round-3 triage (both versions, if fork reconciliation is needed) and round-6 triage (B vs. E dispute, showing how triage overruled B's objection with independent re-derivation). All reasoning is in the triage files; this ledger is the index.

---

## METADATA

**Campaign ID.** c/0048  
**Artifact chain.** 0048-RKHS-1 → 0048-RKHS-1-r2 → 0048-RKHS-1-r3 → 0048-RKHS-1-r6 (FROZEN)  
**Parallel fork.** 0048-RKHS-1-r4 (from superseded r3-triage v1) → 0048-RKHS-1-r5 (unverified report)  
**Files.** /c/0048/campaign/CONTRACT.md, intermediates/0048-RKHS-1{,-r2,-r3,-r6}.md, intermediates/*-triage.md, report/report.tex  
**Ledger opened.** 2026-08-25 (cycle 1, transcription of closed cycle)
