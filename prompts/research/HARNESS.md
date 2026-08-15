# A Multi-Agent Harness for Attacking an Open Conjecture

Roles are separated so errors decorrelate; verification is adversarial and blind; only agents that cannot see how progress was made are allowed to assert it. Architecture follows the generator/verifier/reviser designs of Aletheia (arXiv:2602.10177) and Huang & Yang (arXiv:2507.15855), with additions for literature grounding, refutation, formalization, persistence, and controlled retreat.

## 0. Calibration before you start

In the largest published sweep, a strong agent was run against 700 problems listed as open; of 200 that experts could grade, 68.5% were fundamentally flawed, 31.5% technically correct, and only **6.5% meaningfully correct**, i.e. correct and answering the intended question (arXiv:2602.10177 §5.2). Three consequences drive the design:

1. **The modal failure is a valid proof of a weaker or different statement**, because the model silently takes the easiest reading. Spend more effort pinning the statement than checking the algebra.
2. **Refusal is the most valuable output after success.** An agent that cannot say "no progress" hands you plausible garbage.
3. **A literature hit is a likely, good outcome**, but watch for a pretrained solution reproduced without attribution.

Aim this at self-contained combinatorial, probabilistic, or number-theoretic statements provable in a few pages. It is a poor fit for problems needing a genuinely new framework.

## 1. Architecture

| Agent | Sees | Must not see | Output |
|---|---|---|---|
| **Scout** | Contract, web | (none) | Prior-art report + source requests |
| **Strategist** | Contract, Scout report | (none) | *k* distinct attack plans |
| **Prover ᵢ** (×*k*, isolated) | Contract, plan *i*, Ledger, cards | Other provers' work | Proof or honest partial |
| **Refuter** (×1–2) | Contract, code exec | Provers' work | Counterexample or barrier |
| **Verifier** (×5) | Contract, cards, artifact only | Generator's trace, prior verdicts | Bug report |
| **Triage** | Contract, artifact, bug report | (none) | Filtered report + source queue |
| **Reviser** | Contract, artifact, filtered report | (none) | Patched artifact |
| **Formalizer** | Contract, accepted artifact, cards | (none) | Lean statement, then proof |
| **Weakener** | Contract, full Ledger, dead plans | (none) | Ranked weakenings, for the human |
| **Lifter** | Contract, proved weakening | (none) | What breaks on lifting the restriction |
| **Checkpointer / Resume** | Ledger, session artifacts / resume card | (none) | Checkpoint / next action |
| **Ledger / progress** | Everything | (none) | Machine state / human status files |

**Invariants.**
- *Isolation.* Provers run in separate contexts; only settled Ledger facts cross between them. Correlated errors defeat cross-checking.
- *Blindness.* The Verifier sees the finished artifact in a fresh context, never the reasoning that produced it. This is the highest-leverage detail: a long trace acts as misleading supporting context that inflates confidence in its own conclusion (arXiv:2602.10177 §2.2).
- *Grounding.* No agent cites a result it has not read; on a retrieval failure it stops and requests the document (§2.1).
- *Persistence.* No agent relies on the conversation; state lives in files (§2.2).
- *Freeze.* Each statement is verified once, then sealed and cited as a black box (§2.4).

Where possible, use **different base models** for Prover and Verifier.

## 2. The Problem Contract

Write once; paste verbatim as the header of every agent prompt. Ambiguity here is the leading cause of wasted compute.

```
### PROBLEM CONTRACT ###

STATEMENT (verbatim, LaTeX, as posed):
  [exact statement; do not paraphrase]
CANONICAL SOURCE: [paper / page]

DESCENT (only if this is a weakening of an earlier Contract):
  Depth: [0 for the original]   Parent: [statement it weakens]
  Axis of retreat / Given up / Obstruction evaded: [...]
  Does NOT establish: [one blunt line, carried into any write-up]

DEFINITIONS: [every non-standard symbol pinned]
QUANTIFIER ORDER, in words: [write it out; most misreadings live here]
ASYMPTOTIC CONVENTIONS: [what tends to infinity, in what order, what is fixed]

WHAT COUNTS AS A SOLUTION:
  [ ] full proof   [ ] disproof (explicit)   [ ] bound X -> Y
  [ ] proof under added hypothesis H, acceptable only if H is [...]
  NOT acceptable: [degenerate readings you can foresee]

KNOWN RESULTS citable without proof: [precise statements]
KNOWN BARRIERS: [failed approaches and why]
SOURCE LIBRARY: [uploaded so far] / DECLINED: [do not re-request]

INTERPRETATION RULE: if any part admits more than one reading, STOP and
report it. Do not resolve it yourself; do not pick the easiest reading.
```

## 2.1 The Source Access Protocol

Retrieval fails silently and expensively: an agent that cannot read a theorem reconstructs it from pretraining with the hypotheses slightly wrong. Reading capacity is finite, so requests are rationed. Paste alongside the Contract in every agent that touches the literature.

```
### SOURCE ACCESS PROTOCOL ###

You may ask me to upload sources you cannot reach. Requests are rationed; treat
pages as scarce.

ACCESS LADDER, exhaust before requesting (report which rungs you tried):
  1. arXiv / the field's preprint server (eprint.iacr.org, ECCC, HAL).
  2. Author homepage or institutional repository.
  3. Scholar "all versions", Semantic Scholar, OpenAlex, DBLP, DOI page.
  4. A later survey or citing paper that restates the result with full
     hypotheses. A faithful restatement with a citation costs nothing and
     resolves most requests.

WHAT EARNS AN UPLOAD (all four): load-bearing; hypothesis-sensitive (exact
statement matters); irreplaceable (cannot reprove in under a page or substitute
a card already held); not already in SOURCE LIBRARY or DECLINED. "For
completeness" and background reading never qualify.

REQUEST FORMAT (at most 3, ranked, end your response with this):
  ### SOURCE REQUEST ###
  Rank n: citation; identifier (DOI/arXiv); exactly what is needed (theorem +
  page range); which of our steps collapses without it; rungs tried; the
  fallback if unavailable.

WHILE WAITING: mark the step [SOURCE-BLOCKED: ref] inline. You may proceed under
an explicitly labelled assumed statement, flagged unverified; everything
downstream is then conditional. Never quietly cite a result you have not read;
if recalling from memory, say so.

ON RECEIPT, emit a SOURCE CARD before use, then evict the paper:
  ### SOURCE CARD [S_n] ###
  citation + page; verbatim statement (LaTeX); hypotheses itemised (flag any our
  objects may fail); conclusion in your words; what it does NOT say; where we use
  it.
The card, not the paper, enters the Ledger and is what downstream agents cite. A
campaign that keeps papers resident runs out of room by the third dependency;
one that keeps only cards accumulates dozens.
```

## 2.2 The Persistence Protocol

A campaign outlives your token allowance. Treat the conversation as disposable and the files as the campaign.

```
### PERSISTENCE PROTOCOL ###

OBLIGATION 1, end every response with a state delta, always, even on refusal:
  ### STATE DELTA ###
  Artifact: [id or none]; Status: [COMPLETE/PARTIAL/ABANDONED];
  Established / Conditional / Killed: [new, one clause each];
  New sources: [cards or requests];
  NEXT ACTION: [one, fully specified: agent, input ids, output id];
  If interrupted here, the campaign loses: [one line].

OBLIGATION 2, work in atomic units (one Scout sweep, one Prover attempt, one
Verifier pass, one Lean lemma, one Ledger update). Do not start a unit you
cannot finish AND record. Long proofs: emit each completed lemma separately.

BUDGET STATE (I tell you, or ask):
  GREEN normal; AMBER start no new prover waves, close verification loops,
  checkpoint at each boundary; RED finish the current unit, checkpoint, stop;
  RESERVE emergency checkpoint only (§3.12). Always keep enough to checkpoint.

NEVER REDO SETTLED WORK. Trust the Ledger's ESTABLISHED entries; do not
re-prove, re-verify, or re-search them. If you doubt one, say so; do not quietly
redo it.
```

**On-disk layout.** One directory per campaign; append-only except the status files. (CLAUDE.md carries the full annotated tree.)

```
_campaigns/C001-<slug>/
  conjecture.tex / .pdf        root conjecture, self-contained
  PROGRESS.md                  all progress + "What remains to be discharged"
  REPORT.md                    overall progress report (prose)
  LEDGER.md                    machine state / resume substrate
  SESSION-LOG.md               append-only
  intermediates/               frozen chain + active target, numbered I01...
    I0N-<slug>.tex/.pdf, I0N-audit-prompt.txt, I0N-audit-response.md,
    I0N-audit-package.zip, I0N-session.tar.gz
  sources/ (S0N-card.md, evictable PDFs)   proofs/ (A0xx-role-cN.md)   lean/
```

- **Numbers are monotone, never reused.** A revised proof is a new `A0xx`; a corrected lemma a new intermediate. The Ledger records the supersession.
- **Only LEDGER/PROGRESS/REPORT are rewritten**; everything else is append-only, so a corrupted Ledger rebuilds from the artifacts and log.
- Give each `proofs/` artifact a header (`id, agent, model, cycle, status`); record the model, since a tally may span model versions.

**Compaction.** Compact, don't truncate: proofs live in files, the Ledger holds statements plus ids; a dead plan collapses to one line one cycle after death; a paper drops once its card exists. Retreat log and weakening pool are never compacted.

## 2.3 Effort and Output Contracts

**Truncation** is a per-message output ceiling; lowering effort does not fix it (effort governs thinking, not visible length). Fix it with an output contract plus chunking. **Allowance exhaustion** is what effort is for: effort applies to all tokens including tool calls, so low effort also means fewer searches, which is why a search-heavy role must not run low. Set effort per role, once.

| Role | effort | Role | effort |
|---|---|---|---|
| Scout | high | Triage | medium |
| Strategist | max | Reviser | high |
| Prover | xhigh | Formalizer | xhigh |
| Refuter | xhigh | Weakener | max |
| Verifier | high (5×) | Lifter | high |
| Prospector | low | Ledger, Checkpointer | low |
| Portfolio Triage | medium | Resume, progress | medium |

Spend effort where the reasoning-to-output ratio is high (Strategist, Weakener), starve it on transcription (Ledger). Verification gets accuracy from five independent `high` passes, not one `max` pass; cut passes before effort, and the fifth before the first. Turn off web/tools for roles that do not use them (Prover, Triage, Reviser, Lifter, Ledger).

```
### OUTPUT CONTRACT ###   (append to every role, with the target length)
Target length: [N] words, a budget not a minimum.
OMIT: restating the request; recapping the plan; process narration; a closing
summary; self-caveats; offers of further help. The Ledger is the memory.
NEVER TRUNCATE MID-ARTIFACT: stop at the last complete unit, say so, name the
next. Every complete artifact ends with:  ### END OF ARTIFACT [id] ###
Its absence signals truncation; downstream agents rely on that.
```

```
### EMISSION ORDER ###   (append to Prover and Formalizer)
Do not attempt the whole output in one response. Emit one unit per message,
STOP after each, wait for "next":
  Unit 0: METHOD SKETCH only (skeleton + full lemma statements + case split).
  Unit k: proof of Lemma k only.
  Final: assembly + gap register + dependencies.
End each with: EMITTED unit k of n; NEXT UNIT ...; ARTIFACT [id]. Plus the state
delta. This makes truncation structurally impossible and each unit checkpointable.
```

```
### STAGE HANDOFF ###   (emit at the end of every stage: a rung proved, or an advance)
A stage is one rung (one intermediate). End it with three things and nothing after:
  1. GOAL, self-contained: the statement just proved, stated with its own
     hypotheses and the givens it may assume by name, so it reads without any
     chat history. Point to the file I0N-<slug>.tex.
  2. PROOF: the completed proof as that self-contained artifact, ending with
     ### END OF ARTIFACT I0N ###. If not yet proved, say so and stop here.
  3. AUDIT, the exact command and steps to check it:
       bash blind-package.sh <campaign> I0N
     then open a CLEAN session (fresh chat / `claude` in an empty dir / web),
     drag in I0N-audit-files/, paste I0N-audit-prompt.txt, and save the verdict
     to I0N-audit-response.md.
  Freeze only on a clean audit; then name the next stage's GOAL (I0(N+1)) and stop.
```

**Ledger patch mode.** Rewrite the whole Ledger only at session end or every third cycle; otherwise emit `LEDGER PATCH, cycle n, sections: [...]`. A Ledger truncated mid-file is worse than no update.

## 2.4 One Statement at a Time: the Frozen Chain

The Weakener hands you a simpler statement S1; a Prover proves it; you verify S1 once; S1 is then FROZEN, a black box you cite and never re-verify. Only then take up S2 (the next rung, or the next lemma), which may cite S1 freely. And so on up the chain, one statement in flight at a time.

The rule: **each statement is verified exactly once, and the moment it is ESTABLISHED it is FROZEN and leaves the active workload.** This is the defence against re-verifying settled results every session, which is the fastest way to exhaust an allowance. A frozen statement is carried as its statement plus verification record; its proof lives in a file, out of context. The active context holds one target plus the black-box statements it cites, never their proofs.

Freezing suspends re-verification, not scrutiny. Do not re-open a frozen statement on a hunch. But if a downstream step reveals it does not give what is needed, that is a *mismatch*: flag it and, if it stands, open a NEW corrected statement with its own once-only verification. The chain is append-only. Within one target you may still run parallel plans; the one-at-a-time rule governs the vertical chain, not the horizontal plans for the current statement.

## 3. The prompts

### 3.1 Scout: prior art

Run first, alone. If it succeeds you are done, cheaply.

```
[PROBLEM CONTRACT] [SOURCE ACCESS PROTOCOL]

You are a research librarian in [field]. Determine whether this statement, or
something implying it, is already in the literature. Do not attempt a proof.

Search: direct keywords; at least three oblique reformulations (search each);
generalizations whose specialization gives the statement; offhand remarks
(search the key quantity, not the problem name); negative results dating the
problem as open.

For every claim: citation, theorem/page, the result in your OWN words, and a
retrieval status: [READ] (with URL) / [RESTATED] (cite both original and the
intermediary you read) / [BLOCKED] (rungs tried) / [MEMORY] (say so; never dress
as READ). An honest [BLOCKED] is worth more than a confident paraphrase.

OUTPUT:
  A. VERDICT: SETTLED / PARTIALLY SETTLED / NO PRIOR RESOLUTION FOUND / UNCLEAR.
  B. Nearest known results, each with the exact gap, each status-tagged.
  C. Standard techniques on this family and what obstructs each.
  D. Confidence, and what you could not check.
  E. THE DECIDING SOURCE: the one document that would most change A, and what
     each possible content implies. The most valuable line in the report.
  F. SOURCE REQUEST, or "none needed".
```

Resolve E before running the Strategist. A [MEMORY] tag on a load-bearing citation is a stop condition.

### 3.2 Strategist: generate divergent attacks

Force divergence; the point is different ideas, not more votes.

```
[PROBLEM CONTRACT] [SCOUT REPORT]

Plan an assault; do not prove. Produce EXACTLY 6 plans, mutually independent (no
two fail for the same reason). Cover, and label, these classes:
  (a) REDUCTION to a known theorem or solved case
  (b) DIRECT CONSTRUCTION (probabilistic or explicit)
  (c) REFUTATION (assume false, hunt the counterexample)
  (d) WEAKENING (strongest special case you believe provable)
  (e) TRANSFER (import machinery from another field; name it)
  (f) BARRIER (argue a class of techniques cannot resolve it)

Per plan: one-sentence thesis; the key step everything turns on; a FALSIFIABLE
MILESTONE provable or refutable in under two pages; prior probability of a full
proof, with reasoning; what it yields even if it fails. Rank by
(information gained)/(effort), not by probability of success.
```

The model's roadmap can be its strongest contribution; do not assume this is the cheap role.

### 3.2.1 Case Planner: the climbing ladder (default path)

The default is bottom-up: prove the simplest nontrivial special case first, verify and freeze it, then climb toward the full conjecture, each rung a numbered intermediate. A special case is a weakening chosen proactively, so this reuses the frozen chain (§2.4), the verify loop (§3.5), and, when a rung resists, the Weakener (§3.10). Climbing up is the normal mode; weakening down is the fallback. Run this after the Scout.

```
[PROBLEM CONTRACT] [SCOUT REPORT]

Do not prove. Produce an ordered LADDER of special cases climbing from the
simplest nontrivial one to the full conjecture. Each rung must be:
  - IMPLIED by the conjecture (a genuine special case) and STRICTLY more general
    or harder than the rung below;
  - NONTRIVIAL (not vacuous, not in ESTABLISHED, not settled by the Scout);
  - statable and provable in a few pages, self-contained.
Use the restriction axes: fix the smallest parameter (e.g. k=2), small or fixed
n, a structured subclass, low dimension, and so on. Rung 1 is the simplest case
whose proof is not immediate; the top rung is the full conjecture (or the
strongest rung you believe reachable).

OUTPUT: a numbered ladder; per rung the statement (LaTeX), what new difficulty it
adds over the rung below, and whether the Scout already settles it (skip those).
Mark where you expect difficulty to jump. Then STOP; the human approves or
reorders. Do not begin proving.
```

Per rung, climbing: materialise it as the next intermediate (`new-intermediate.sh`); **first sanity-check it computationally** (run the Refuter's bounded search on the rung: small cases, exact arithmetic, mod checks) so you do not spend a proving budget on a false statement, and if the check fails the rung is false, so stop and refute rather than prove; then attempt it (one prover usually suffices for low rungs, the full Strategist only where difficulty jumps); run the verify loop; on five clean passes freeze it and advance. If verification fails, revise (bounded to three cycles), then try at most two fresh proof attempts on different plans; if it still resists, the rung is too hard, so invoke the Weakener to insert an easier rung below it or weaken the target. End each rung with the STAGE HANDOFF (§2.3): the self-contained goal, its proof artifact, and the command to audit it, then the next rung's goal. This bounded budget per rung keeps every stage small and progress legible as a sequence of frozen files.

### 3.3 Prover: one per plan, isolated

```
[PROBLEM CONTRACT] [SOURCE ACCESS PROTOCOL] [PERSISTENCE PROTOCOL]
[OUTPUT CONTRACT + EMISSION ORDER] [ASSIGNED PLAN i] [LEDGER: lemmas + cards]

Pursue this plan only; another team covers the others; do not read their work.

* Rigour dominates: a correct conclusion via an unjustified step is a FAILURE.
  Mark every unjustifiable step [GAP] inline.
* Honesty: if you cannot close it, do not produce something that looks complete.
  Report only what you can prove. A key lemma, one discharged case, a one-sided
  bound, a structural fact, or a refuted milestone are all valuable. "This plan
  does not work, and here is exactly where it breaks" is a real result.
* If a step needs a source whose exact statement you have not read, mark it
  [SOURCE-BLOCKED: ref] and issue a SOURCE REQUEST. Never reconstruct a borrowed
  theorem from memory.
* Prefer a plan needing no inaccessible source; if yours turns on one, say so in
  the VERDICT.

OUTPUT (emission order): VERDICT (COMPLETE/PARTIAL/PLAN REFUTED/NO PROGRESS);
METHOD SKETCH (auditable skeleton + full lemma statements + case split); DETAILED
ARGUMENT (only the proof you claim); GAP REGISTER ([GAP] and [SOURCE-BLOCKED],
each routine or load-bearing); DEPENDENCIES (external results, exact statements,
tagged READ/RESTATED/CARD/SOURCE-BLOCKED/MEMORY; a load-bearing SOURCE-BLOCKED
or MEMORY makes the result PARTIAL, not COMPLETE); SOURCE REQUEST or "none". On the Final unit, also emit the STAGE HANDOFF (§2.3):
the self-contained GOAL, its PROOF artifact, and the exact AUDIT command.
```

### 3.4 Refuter: run in parallel, always

Counterexamples are cheap to verify and expensive to overlook. Run even when you believe the conjecture.

```
[PROBLEM CONTRACT]

The conjecture is FALSE; find the counterexample. Argue for falsity as strongly
as the evidence allows.

1. Identify the fragile regimes (boundary, degenerate, extremal, small cases,
   high-dimension limits).
2. Write and RUN code to search them, exhaustively where feasible, stochastically
   otherwise. Report the exact space covered; state what a null result rules out.
3. If infeasible, set up an optimization whose objective is positive exactly when
   the conjecture fails; report the best value and configuration.
4. A near-miss: characterise precisely what blocks it. That obstruction is
   usually the heart of the proof.
5. A counterexample: verify by two independent methods, one exact/symbolic.

OUTPUT: FALSIFIED (certificate) / NEAR-MISS (obstruction) / NO COUNTEREXAMPLE IN
REGIME [specified] / SEARCH INFEASIBLE (reasons).
```

LLM-guided evolutionary search over object-constructing programs is the strongest known method for this half (arXiv:2511.02864); it excels at combining standard ideas nobody had the patience to search, and is the wrong tool where genuinely new insight is needed.

### 3.5 Verifier: blind, adversarial, ×5

Paste the artifact into a fresh context: no history, no reasoning trace, no indication of who produced it.

```
[PROBLEM CONTRACT] [SOURCE CARDS for cited results, if any]

### ARTIFACT UNDER REVIEW ###
[paste the proof verbatim, nothing else]

You are a referee for a top journal. Find and report defects. You are a
VERIFIER, NOT A SOLVER: do not repair, fill gaps, or supply the intended
argument. A correct conclusion via an unjustified step is incorrect.

STEP 0 COMPLETENESS: if the artifact lacks its ### END OF ARTIFACT id ### line
or stops mid-proof, return the single verdict TRUNCATED, name the last complete
unit, and STOP. Do not verify a partial artifact.

Then classify every defect:
  (A) STATEMENT DRIFT, proves something other than the Contract (strengthened
      hypothesis, weakened conclusion, reordered quantifiers, asymptotic for
      exact, ambiguous term read the easy/vacuous way). CHECK THIS FIRST: state
      what the artifact actually proves, in your words, and diff vs the Contract.
      Highest-frequency defect.
  (B) CRITICAL ERROR, a broken step. Explain, note it invalidates this line,
      then scan on and verify logically independent parts (other cases).
  (C) JUSTIFICATION GAP, conclusion may hold but the argument is incomplete.
      Explain the gap, ASSUME the conclusion, continue downstream.
  (D) CITATION DEFECT, external result misused. Check against the source card,
      hypothesis by hypothesis; confirm our objects satisfy each.
  (E) UNVERIFIABLE, cannot reach a cited source and no card covers it. Do NOT
      guess or wave through; record it, say what the proof needs it to say.
      A load-bearing (E) blocks acceptance.

OUTPUT: 1. FINAL VERDICT, one sentence. 2. FINDINGS TABLE: quoted location,
class, explanation. 3. STEP-BY-STEP LOG: one line per accepted step, detail per
defect. 4. SOURCE REQUEST for (D)/(E), or "none".

COMMON FAILURE PATTERNS to probe for actively (a starting checklist; extend per
domain), on top of the A-E classes:
  - quantifier order swapped, or "for all sufficiently large n" silently dropped;
  - a union or probability bound summed over an n-dependent or unbounded index
    without control;
  - worst-case vs expected vs high-probability conflated;
  - an asymptotic claim standing in for the explicit constant the result needs;
  - a reduction or hybrid whose lost factor or step count is not accounted for;
  - an adversary/oracle given access it should not have, or a simulation only
    claimed, not shown, statistically close;
  - independence assumed between events or variables not shown independent;
  - a limit / sum-integral / expectation interchange used without justification;
  - a negligible or measure-zero exception treated as empty;
  - induction with a missing base case, or a step invoking the statement at a
    value not yet established;
  - an object constructed but not shown to satisfy every required property.
```

Acceptance: run five times independently; accept only on five clean passes. Critical errors are rarely missed, but reported critical errors are often not critical (high recall, low precision), which is why Triage exists. Class (E) findings are gaps in your library, not the proof: one upload clears them for every later cycle. Fast refute: if two independent passes report the *same* genuine critical error (Triage upholds it), stop revising at once and treat the approach as refuted, rather than grinding the three-cycle budget; route to a fresh plan or the Weakener.

#### 3.5.1 External blind review, the strongest form

A subagent verifier is isolated but not blank: it still loads the workspace framing. For the passes that certify a result, and for anything high-stakes, hand the proof to a session with no context at all, ideally a different model. Produce the package with `blind-package.sh <campaign> <intermediate>` (or `/blind-package`): a zip of the Contract, the artifact with provenance stripped, and the source cards, plus a self-contained referee prompt beside it. It omits the ledger, plans, dead ends, prover reasoning, and prior verdicts. Run it in a brand-new chat (or `claude` in an empty dir, or the web interface); the verdict returns as a file you feed to Triage and counts toward the five-pass tally. This is the higher bar you clear before calling a result proved, not a replacement for the in-loop passes.

### 3.6 Triage: referee the referee

Skip this and the loop is unstable: the Reviser will mangle a correct proof to satisfy a spurious objection.

```
[PROBLEM CONTRACT] [ARTIFACT] [BUG REPORT]

You are the handling editor. Rule each finding, on the mathematics alone (the
referee's confidence is not evidence):
  UPHELD    real defect; the artifact must change.
  OVERRULED referee mistaken; explain the error precisely.
  PEDANTIC  a gap a competent reader fills without effort; note, don't require a
            rewrite. STATEMENT DRIFT (A) is never PEDANTIC.
  NEEDS SOURCE cannot settle without an unreachable source; route to the source
            queue, NOT the reviser.
  UNCLEAR   cannot adjudicate; escalate to the human.

OUTPUT: filtered report (UPHELD + PEDANTIC only); escalation list; consolidated
SOURCE REQUEST (merge duplicates; that document is the bottleneck).
```

### 3.7 Reviser

```
[PROBLEM CONTRACT] [ARTIFACT] [FILTERED BUG REPORT]

Repair the artifact.
* Address every UPHELD finding; change nothing unflagged.
* You may NOT close a gap by weakening the theorem. If the only repair weakens
  it, STOP and report that; weakening goes through the Weakener gate (3.10),
  human-chosen. The original claim then reverts to unproved.
* Any [SOURCE-BLOCKED] marker stays; you have no more literature access than
  before. If you can route around it entirely, do so and say so.
* Do not paper over a gap with prose; supply the argument or leave [GAP] marked.

Return the full revised artifact as a NEW file (monotone id, never overwrite),
END-OF-ARTIFACT marker, plus a changelog mapping each finding to its resolution.
```

Loop 3.5, 3.6, 3.7 until five clean passes, or the same defect survives three revision cycles (a real difficulty: stop and look there yourself). Beware the *cognitive well*: iterative refinement can converge to a confident but wrong fixed point that the solver and its own grader both accept (arXiv:2602.16793). The defences are already in place, use them: fresh independent verifiers each round (never the same grader), different model families, and an external blind review (§3.5.1) before you call anything proved.

### 3.8 Formalizer: the only unforgeable check

Two phases, never merged.

**Phase 1, statement only**, from the Contract (not the proof, which would bias it). Round-trip the Lean statement back to English and diff against the Contract before any proof work.

**Phase 2, proof**, only after the statement round-trips. Beyond a couple of pages use a blueprint / proof-DAG (arXiv:2606.05400). A borrowed theorem must be in Mathlib (hypotheses checked to match), or a named local hypothesis from a source card, or a named `axiom` with a citation comment that appears in `#print axioms`. Never invent a Mathlib lemma name. Emit one lemma per message.

**Audit.** Lean accepts declarations closed by `sorry`; compilation is not proof (arXiv:2605.20120).
```bash
grep -rn "sorry\|admit\|native_decide" .    # trust holes
grep -rn "^axiom" .                          # extra axioms
```
`#print axioms MainTheorem` should return only `propext, Classical.choice, Quot.sound`; justify anything else.

### 3.9 Ledger

One file, updated every cycle, the sole channel between isolated provers and the only thing a cold session needs. Write it self-contained.

```
[CURRENT LEDGER] [NEW OUTPUTS THIS CYCLE]

Maintain the record; assume the reader has no context. OUTPUT MODE: PATCH
(changed sections only) except a full rewrite at session end / every third
cycle. Never spend deep reasoning here; it is transcription.

  HEADER: campaign, depth, contract file, cycle, session, date, budget, NEXT
    ACTION. First, one screenful; this is read on resume.
  ESTABLISHED: proved+verified. Statement, proof artifact id, tally, date.
    On becoming ESTABLISHED, mark FROZEN: keep statement + tally, note the
    proof file, evict the proof. FROZEN = cited as a black box, never
    re-verified (2.4).
  VERIFICATION TALLY: per pass (number, verdict, model, report id). Spans
    sessions; never restart the count.
  CONDITIONAL (with dependency); REFUTED (with counterexample).
  DEAD PLANS: killed plans + precise reason; compact to one line after a cycle.
  OPEN GAPS (ranked); DEPENDENCY GRAPH (flag any cycle); PROVENANCE (agent,
    model, cycle; whether an argument may derive from a Scout source).
  RETREAT LOG: one row per attempted statement (depth, statement, parent, axis,
    outcome, obstruction). Never delete; this is the output when the conjecture
    survives.
  WEAKENING POOL: every candidate ever generated, UNTRIED/ATTEMPTED/PROVED/
    REFUTED/DISCARDED, with the implication order. Carry passed-over candidates.
  SOURCE LIBRARY / SOURCE QUEUE / DECLINED / BLOCKED CLAIMS.
  MANIFEST: one line per artifact (id, path, agent, model, cycle, status,
    superseded-by). NEXT ACTION: exactly one, fully specified. Never empty or
    plural.

A claim resting on a [SOURCE-BLOCKED] dependency stays CONDITIONAL however many
passes it survives. A claim proved at depth d is recorded against its own
Contract, never the depth-0 statement. Before returning: could a fresh session
continue from this alone? If not, add what is missing.
```

### 3.10 Weakener: controlled retreat

The Reviser may not weaken a proof; this is the only legitimate gate for weakening, when the *campaign* stalls: a deliberate step down on a named axis, with the original left open, chosen by the human.

**Declare a STALL only when all four hold:** every top plan is dead or has a gap surviving three cycles; the Refuter reports no near-miss suggesting falsity; the Source Queue is empty or written off (**check this first**, a campaign blocked on an unread paper is not stalled); two cycles are done under review.

```
[PROBLEM CONTRACT] [LEDGER: dead plans, gaps, refuter reports, weakening pool]

The campaign has stalled. Do not prove; do not retry a dead plan.

STEP 1 DIAGNOSE: name the single obstruction that killed the dead plans, at fine
resolution ("the union bound loses a factor k and k is unbounded", not "the
combinatorics got hard"). Are the failures the same obstruction in disguise? You
retreat from the obstruction, not the statement.

STEP 2 CANDIDATES: 5 to 7 weakenings. Each must be: IMPLIED by the original
(verify the direction); EVADE the diagnosed obstruction (state why, THE BINDING
CONSTRAINT: a weaker statement hitting the same wall buys nothing);
NON-DEGENERATE; ABOVE the Level-0 significance floor. Draw from and label with
these axes, prefer untried ones: (a) domain restriction (b) quantifier
relaxation (c) conclusion relaxation (d) added named hypothesis (e) model
restriction (f) average case (g) approximation (h) DUALISE to a barrier.

STEP 3 ORDER: give the implication order; mark SIBLINGS (incomparable, equal
strength, different axis, more valuable than descents) vs strictly BELOW.

STEP 4 PRESENT AND STOP. Output the menu, nothing after it. Do not start any
candidate.
  ### WEAKENING MENU ###
  Diagnosed obstruction: [one sentence]
  W1: statement (LaTeX); axis; gives up; evades because; level; already known?;
      lift prospect ("nothing obvious" is a warning); cost.
  ... implication order; your ranking with reasons; discarded and why.
  YOUR CHOICE: which to attack? (or reject and ask for another axis)
```

Recommend AGAINST retreat if the obstruction is identical across all candidates (a barrier, axis h, is the honest output), if near-misses suggest falsity, or if everything left is Level 0.

**Re-entry.** A chosen candidate becomes a **new Contract** and the single active target (2.4): one weakening proved, verified once, and FROZEN before the next is considered. Fill the DESCENT block, set depth+1, run from the top. Two mandatory parts: **re-run the Scout** (weakenings are far likelier to be in the literature already), and **re-plan fresh** (a revived parent plan must say why the obstruction no longer applies). Keep the parent Ledger; the parent stays OPEN with its diagnosed obstruction.

**Repeat stalls:** prefer, in order, an untried SIBLING at the same strength; then an earlier menu's candidate reconsidered; then a descent to depth+1. Never re-attempt a failed statement. Past depth 3, stop and ask the human whether the target is still worth proving.

### 3.11 Lifter: climb back up

Run immediately on a proved weakening, before write-up.

```
[PROBLEM CONTRACT for the weakening] [THE VERIFIED PROOF] [PARENT CONTRACT]

The weakening is proved. Do not attempt the parent yet. The proved weakening is
now FROZEN: a black box the next target cites, never re-verified.

1. LOCATE every step that uses the restriction; quote each. If a step does not
   use it, say so, and state the weakest restriction the proof actually needs.
2. CLASSIFY each use: REMOVABLE (sketch the general argument) / COSTLY (state the
   price) / ESSENTIAL (false without it; give the step-level counterexample).
3. RESTATE the strongest statement this proof establishes (maybe stronger than
   the Contract).
4. REPORT the remaining gap as a precise new conjecture, the next single active
   target, with the ESSENTIAL uses as its stated difficulty. Emit it as the next
   STAGE HANDOFF (§2.3): the self-contained next GOAL and the AUDIT command it
   will use once proved.
5. Compare the ESSENTIAL uses to the parent's diagnosed obstruction. If they
   coincide, you have isolated the true difficulty of the original problem: a
   reportable finding independent of any proof.
```

### 3.12 Checkpointer: end a session cleanly

Run at every session boundary, at RED, and before any expensive step. Cheap; run it often.

```
[CURRENT LEDGER] [ARTIFACTS THIS SESSION]

Write the checkpoint; do no mathematics. Produce three things:
1. UPDATED LEDGER, complete and self-contained (apply compaction; verify it has
   every ESTABLISHED claim with its tally, retreat log, weakening pool, source
   library/queue, dependency graph, and exactly one NEXT ACTION).
2. SESSION LOG ENTRY (appended): session n, date, model, budget spent; started
   at; did (<=3 lines); result; SURPRISED ME (be specific, the field worth
   reading in six weeks); did NOT do; NEXT ACTION (verbatim).
3. RESUME CARD: campaign; depth + contract file; cycle; files to load (smallest
   sufficient set, in order); do NOT reload (superseded artifacts, evicted
   PDFs); NEXT ACTION; the one thing a fresh session tends to get wrong here.
Then stop; name the file paths.
```

Emergency (RESERVE): output only the bare LaTeX statements of unrecorded results, where each proof lives (or "in this conversation only, unrecorded", flag loudly), and one NEXT ACTION. Nothing else.

### 3.13 Resume: start a session cold

```
[RESUME CARD] [LEDGER] [CONTRACT] [SOURCE ACCESS + PERSISTENCE PROTOCOLS]
[only the artifacts the next action names]

You are resuming with no memory. The Ledger is authoritative and complete; treat
it as fact, not a summary to double-check.

STEP 1 COHERENCE CHECK before any work: exactly one NEXT ACTION, understood;
every claim it depends on is ESTABLISHED/CONDITIONAL with dependencies recorded;
no referenced artifact id is missing; no dependency cycle; no queued source is
needed by the next action. Report any discrepancy and STOP; do not repair on your
own initiative.
STEP 2 STATE what you will do, in two sentences, and its cost; wait if material.
STEP 3 EXECUTE the next action, only that. Do not tidy elsewhere, re-verify
settled claims, revisit dead plans, or open a second front.
STEP 4 emit the STATE DELTA.
```

## 4. Orchestration

```
Scout -> if SETTLED, stop (literature identification)
      -> SOURCE GATE 1: resolve the deciding source (upload or write off) first
Case Planner -> ordered LADDER of special cases, simplest nontrivial -> full
             conjecture (top rung). == HUMAN APPROVES / REORDERS ==

CLIMB the ladder, one rung at a time (rung 1 = simplest):
  materialise rung as intermediate I0N (new-intermediate.sh)
  attempt it: one Prover for low rungs; full Strategist -> Provers x k + Refuter
              where difficulty jumps
  SOURCE GATE 2 if a wave raised requests (merge, rank, fill top 2-3)
  /verify-loop: Verifier x5 (blind) -> Triage -> Reviser -> back to Verifier
    stop: 5/5 clean; OR same defect survives 3 cycles; OR blocked on a source
      |- verified -> mark ESTABLISHED + FROZEN, evict proof (2.4)
      |            -> (Formalizer if wanted) -> Human reads it
      |            -> emit STAGE HANDOFF (goal + proof + audit cmd), then ADVANCE
      |- resists (3 revise cycles + <=2 fresh proof attempts all failed)
      |            -> Weakener: insert an easier rung BELOW, or weaken the target
      |            -> == HUMAN CHOOSES == -> new intermediate, re-run Scout on it
  ... climb until the top rung (the full conjecture) is frozen.
Ledger update (+ /progress for PROGRESS.md, REPORT.md) at every boundary
```

(You can also go straight at the top rung and only weaken on stall; the ladder is the safer default because every stage is small and each frozen rung is durable progress.)

**Discipline.** Verification is where compute buys the most; fewer, better-checked candidates beat more candidates. Batch uploads at the gate (separate provers often want the same paper). Two cycles, then a human reads everything. Retreat is a walk on a partial order: move sideways before down, and check each step actually evades the obstruction. Frozen-chain: resolve one statement, verify once, freeze, then advance, so the active verification workload stays the size of one statement however long the chain grows. Spend a nearly-exhausted allowance on a verifier pass or a Ledger update, never on starting a prover or formalization.

## 5. What this is not

It is not a debate. Symmetric multi-agent debate does not reliably beat self-consistency at matched compute; much of its apparent benefit is answer aggregation, and confident agents dominate regardless of correctness (arXiv:2310.01798). What works is asymmetric role separation plus an external grounding signal (code, retrieved literature, a proof assistant) at every point a claim could otherwise be settled by rhetoric. Every agent here either has such a signal or has a role that forbids asserting anything new.

## 6. Failure modes

| Failure | Countermeasure |
|---|---|
| Statement drift | Contract quantifier order; Verifier class (A) first |
| Specification gaming | Contract INTERPRETATION RULE: report, don't resolve |
| Citation fabrication / misattribution | Scout retrieves + paraphrases; Verifier (D) checks the card |
| Silent memory substitution | retrieval tags; [SOURCE-BLOCKED]; class (E) blocks acceptance |
| Correlated errors | isolated contexts; different models per role |
| Verifier false positives | Triage; never skip it |
| `sorry` in the build | grep + `#print axioms` |
| Lost work / budget spent unrecorded | atomic units; state delta; reserve-checkpoint rule |
| Re-verification thrash | 2.4 freeze: verify once, cite as black box, evict proof |
| Truncated artifact verified | END marker; Verifier step 0 returns TRUNCATED |
| Premature / futile retreat | stall criterion 3 (queue clear); Weakener (ii) EVADES |
| Claim inflation | DESCENT "does NOT establish"; recorded against own Contract |

## 7. If it works

Re-run the Scout with the *proof technique* as the search key: independent rediscovery is the most common outcome that looks like a breakthrough, and the odds rise at each depth. Report only what you proved: if it was a depth-2 weakening, the "does NOT establish" line goes near the theorem. Document provenance honestly: the prompts, the outputs, and which insights came from which side, with transcripts for anything load-bearing, in the spirit of the reflections in Feng et al. (2602.10177). Only a human can carry accountability for correctness and attribution.

## 8. If it does not work

The retreat log plus the diagnosed obstructions is a legitimate output. A short note stating the conjecture, the natural approaches, and precisely why each fails, with the Lifter's isolation of the essential difficulty, saves the next person a month. Publish the barrier, keep the source cards, leave the conjecture open in the record.

## References

- Feng et al. (2026), *Towards Autonomous Mathematics Research*, arXiv:2602.10177. Aletheia; generator/verifier/reviser; Erdos base rates; hallucination taxonomy; HAI cards.
- Feng et al. (2026), *Semi-Autonomous Mathematics Discovery with Gemini*, arXiv:2601.22401. The 700-problem sweep.
- Huang & Yang (2025), *Winning Gold at IMO 2025*, arXiv:2507.15855; github.com/lyang36/IMO25. Model-agnostic verify-and-refine (solver/verifier/corrector); 5/6 at IMO 2025. The five-pass acceptance and the A-E defect classes here are this harness's conventions, not theirs.
- *Escaping the Cognitive Well*, arXiv:2602.16793. Names the failure where refinement converges to a confident-wrong fixed point accepted by solver and grader alike.
- Huang et al. (2023), *LLMs Cannot Self-Correct Reasoning Yet*, arXiv:2310.01798. Limits of debate.
- Georgiev, Gomez-Serrano, Tao, Wagner (2025), *Mathematical Exploration and Discovery at Scale*, arXiv:2511.02864. AlphaEvolve; scope of construction search.
- LeanMarathon (2026), arXiv:2606.05400. Blueprint / proof-DAG for long-horizon autoformalization.
- Lau (2026), arXiv:2605.20120. The `sorry` trap in AI-generated Lean.
