# A composite audit protocol for universally composable security proofs

Merges three inputs: the read-only `proofread-check` skill (anchored, non-inventive, LaTeX-safe reporting), the staged UC audit suite (extraction before judgement, adversarial framing, first-class `UNVERIFIABLE`), and the single-proof verifier (independent baseline, atomic step verdicts, unused-hypothesis check, one-line final verdict).

Section 1 is the prompt. Sections 2 to 8 are the modules you drop in when a stage returns thin results, plus staging, schema, rubric, adjudication, the LaTeX sidecar variant, and design notes.

---

## 0. How to use

**Scope per run.** One audit unit: one theorem with its proof, or one functionality, or one hybrid transition. Batching hybrids is where audits go shallow.

**The bundle.** Every run receives the unit plus a constant preamble: `index.md` (the S0 verbatim extract of labels, definitions, functionality pseudocode, and theorem statements), `inventory.md` (the Phase B table, frozen after S1), and the verbatim statements of every external result the unit cites. Split the evaluation unit, never the evidence.

**Where to cut.** On dependency closure, not on `\section` boundaries, which routinely sever a proof from the definitions it uses. Where the source is already `\input`-structured, mirror that structure and re-cut only when a unit exceeds roughly 1,500 words or bundles several independent obligations. Section 2 stage S0.5 computes the cut.

**Carry-forward.** Across runs carry only the Phase B inventory, the Phase D reification, and the open-obligations ledger, never the earlier verdicts. A confident early stage otherwise suppresses a later finding.

**The obligations ledger.** Splitting is safe only if each run logs what it deferred to material it could not see. S7 discharges every ledger entry against the real text or promotes it to a finding. Without the ledger, splitting silently converts gaps into assumptions, which is the failure mode hard rule 4 exists to prevent.

**Two runs then adjudicate.** Run the prompt twice with different section orderings, then run section 6. Categories where the two runs disagree are the categories where the audit itself is unreliable.

**Placeholders.** `{{FRAMEWORK}}`, `{{MATERIAL}}`, `{{THEOREM}}`, `{{DEFINITIONS}}`, `{{EXTERNAL RESULTS}}`.

---

## 1. The prompt

Copy from here to the closing marker.

~~~text
=== UC PROOF AUDIT: COMPOSITE PROTOCOL ===

ROLE
You are auditing a claimed security result in the {{FRAMEWORK: UC / GUC / UCGS / JUC / iUC / GNUC / IITM / SUC}} framework. Your task is to determine whether the stated result is established by the argument given. You are not assessing contribution, novelty, presentation, or writing.

MANDATE AND CALIBRATION
Two instructions pull against each other. Hold both.
(a) Search adversarially. Presume the material contains at least one substantive defect and allocate effort accordingly. "Construct an environment that distinguishes" finds errors that "check whether this step is correct" does not. An audit that finds nothing after a shallow pass has failed.
(b) Report calibrated. The presumption in (a) governs search effort, not conclusions. It is not a reporting quota. A SOUND verdict is a legitimate finding, but you must defend it obligation by obligation, as rigorously as you would defend an error.
Never report a concern you cannot anchor and witness. Distinguish a defect in the paper from a gap in your own knowledge: if a step is standard in a literature not provided here, mark it UNVERIFIABLE, never ERROR.

MATERIAL
Theorem or claim: {{THEOREM}}
Definitions, notation, functionality pseudocode: {{DEFINITIONS}}
Statements of cited external results, verbatim where available: {{EXTERNAL RESULTS}}
Proof or section under audit: {{MATERIAL}}

HARD RULES
1. Do not summarize. Do not praise. Do not comment on exposition. Those are handled in a separate pass.
2. Anchor every judgement: theorem, lemma, or definition label; equation or line number; or a quoted trigger clause of at most twelve words. Unanchored findings are discarded.
3. Verdict vocabulary.
   At step level (Phase E): VALID / UNJUSTIFIED / INVALID.
   At finding level (Phase I):
     ERROR        the stated inference does not follow, or the claim is false
     GAP          the inference may hold but a required step is absent
     CONVENTION   defensible under one reading of the framework, wrong under another, and the paper does not fix the reading
     UNVERIFIABLE cannot be settled from the material provided; name exactly what is missing
     QUESTION     a request to the authors that would resolve an ambiguity
4. No silent repair. If you supplied a lemma, hypothesis, convention, or missing case to make a step work, the step is UNJUSTIFIED and the finding is GAP or ERROR. Name what you supplied. If you believe the missing item exists in material not provided to you, do not assume it: log it in the open-obligations ledger (J4), mark the affected conclusions UNVERIFIABLE, and continue.
5. No appeal to standardness. Never write "this is standard" or "follows from known results" without naming the source and stating the exact form of the result invoked.
6. No approval by restatement. To mark a step VALID, name the obligation it discharges and why it is discharged. Paraphrasing the step is not verification. "Looks fine", "clearly", and "as expected" are not verdicts.
7. A correct conclusion is not evidence that the steps are valid. A proof can be wrong when the theorem is true. Audit the proof.
8. Budget honesty. If the material exceeds what you can analyze at the granularity Phase E requires, stop, say where you stopped, and report only what you covered. Do not skim.

Produce the phases below in order. Do not state an overall verdict before Phase J.

--- PHASE A. INDEPENDENT BASELINE (write before engaging with the author's argument) ---
Using only the theorem statement, definitions, and functionality code:
A1. State precisely what must be exhibited, and the quantifier structure you expect the emulation claim to have (for all adversaries there exists a simulator, or the dummy-adversary form, or the specialized-simulator form).
A2. Sketch the simulator you would build. Name its state variables and say at which activation each is first set.
A3. List the obligations you expect to be hard: every point where the simulator must extract a value, every point where it must equivocate, every place a real party's view constrains it. Predict where the argument will be thin.
A4. List the modelling choices your sketch depends on: local or global setup, programmable or observable random oracle, erasures, static or adaptive corruption, synchrony, who chooses the CRS.
This is one possible route, not the author's. Do not assume the author follows it. Its purpose is a baseline: any difficulty you predicted that the author's argument never confronts is a candidate finding, and you must record whether the author's route legitimately avoids it or silently steps around it.

--- PHASE B. FORMAL INVENTORY (extraction precedes judgement) ---
Fill this table before evaluating anything. Write ABSENT where the paper does not say, and treat every ABSENT as a candidate finding.
B1  Framework, exact reference, and which revision or version.
B2  Every ideal functionality: name, interfaces (input, output, network, corruption), leakage, delayed-output convention.
B3  Every protocol and its subroutines; which functionalities are hybrid setups.
B4  Corruption model: static, adaptive, or mobile; at what granularity corruption may occur (between activations only, or mid-activation and mid-subroutine); erasures assumed and of what; who is told of a corruption and when; whether corrupting a party corrupts the subroutine instances it spawned; whether corruption is permitted after outputs are delivered; any threshold on the corrupted set and when it is enforced.
B5  Setup: CRS, PKI, random oracle, clock; local or global; does the simulator choose or program it.
B6  The simulator: its state, its inputs, what it learns and at which activation.
B7  The hybrid or game sequence: every hybrid, the single change, the claimed distance (perfect, statistical with epsilon, computational with the assumption named).
B8  Runtime convention: how polynomial time is defined for protocol, adversary, environment, simulator; the import mechanism.
B9  Which composition theorem is invoked, from which source, and what its hypotheses are.
B10 Session and party identifier discipline: how SIDs are generated, whether global uniqueness is assumed, who checks.
B11 The exact emulation statement, with quantifier order as written.
B12 Concrete or asymptotic: is the claim a concrete bound or a negligibility statement, and what is the security parameter's role in every quantity.

--- PHASE C. NOTATION, CONVENTIONS, AND SILENT ASSUMPTIONS ---
C1. Restate every nonstandard definition and notation the argument relies on, and confirm each is used consistently across code, definitions, and theorem statements. Flag non-identical technical terms used interchangeably (simulator and adversary, protocol and functionality, reduction and hybrid); flag them rather than unifying them, since the distinction may be intentional.
C2. List every convention the argument relies on but does not state, and for each say whether a different common reading would break the argument. Check at minimum: immediate versus delayed output, and public versus private delayed output; whether corruption is delivered to the party or announced to the environment; whether a claim proved for the dummy adversary is used for arbitrary adversaries; balanced environments; identifier and SID discipline; the polynomial-time convention and how it is imported; negligible in which parameter; whether "session" means a single instance or the multi-session extension; erasures, and whether an erasure is atomic within an activation or can be interrupted by a corruption; whether a corruption exposes the state of subroutine instances; whether the corrupted set is fixed once chosen; whether the random oracle is local or global, programmable or observable; who samples the CRS.
Any such convention that the paper leaves open and under which the argument changes truth value is a CONVENTION finding.
C3. Assume standard structural macros, template commands, and global definitions are bound outside the provided material. Do not flag a symbol merely because its definition is not shown. Flag a symbol only when it is used inconsistently within the provided text, contradicts a definition given here, or escapes a local binding scope.

--- PHASE D. REIFICATION (before step analysis) ---
D1. Rewrite the simulator as explicit pseudocode: named state variables, one handler per activation, explicit branches for every message it may receive and every corruption transition. Include one corruption handler per party per protocol phase, covering corruption before the party's first activation, between any two of its activations, after it sent a message but before delivery, and after its output was delivered. Then audit the rewrite against the paper's prose. List every field you had to invent, every branch the prose leaves undefined, and every ordering you had to choose. Each such item is a finding, not a convenience.
D2. For each ideal functionality, produce a table with columns: message, precondition and state, state change, output and to whom, leakage to the adversary. Mark every cell the paper does not determine, including out-of-order, duplicate, and post-abort messages.
D3. List every hybrid as a triple: the single change from its predecessor, the claimed distance, and the justification cited. Any hybrid whose change is not single is a finding.

--- PHASE E. STEP-LEVEL ANALYSIS ---
Decompose the argument into atomic inference steps. For each: a verdict (VALID / UNJUSTIFIED / INVALID) and one line naming the obligation the step discharges and why it is or is not discharged. Merge consecutive steps only when they are routine and share one justification; never merge across a step that introduces an assumption, invokes an external result, changes the corruption model, or moves between games. Identify the earliest failing step and state explicitly which later steps are contingent on it.

--- PHASE F. OBLIGATION CHECKLIST ---
Answer every item with a verdict and an anchor. If an item does not apply, say so in one line with the reason. Do not skip items.

F1 SIMULATOR
  a. Is simulation straight-line? Search for re-running, rewinding, or repeated sampling of the adversary or environment. Flag phrases such as "runs A again", "repeats until", "by an averaging argument over A's coins".
  b. Extraction. At the exact activation where the simulator must know a value, state where that value comes from. If it comes from a later activation, the proof is out of order.
  c. Equivocation under adaptive corruption. List every field of internal state the simulator must produce when a party is corrupted mid-protocol, and for each give its source. Any field it cannot produce is a commitment-problem failure. If the corruption model is adaptive or mobile, F6 replaces this item with a full ledger; complete F6 before reporting F1c.
  d. Quantifier order. Is the simulator constructed using knowledge of the environment? If so the result is the specialized-simulator relaxation, not UC emulation.
  e. Dummy adversary. Is a claim proved only for the dummy adversary and then used for arbitrary adversaries, or the reverse, without invoking the equivalence?
  f. Complexity. Strict or expected polynomial time? Does the simulator's runtime depend on the environment's, and is that consistent with B8?
  g. Free-resource audit. List everything the simulator may do that a real party may not: choosing the CRS, programming the random oracle, learning corruption status early, aborting, rewinding a subroutine. For each, state what breaks if that resource is global or non-programmable.

F2 FUNCTIONALITY DESIGN
  a. Realizability: hidden message lengths, guaranteed termination in an asynchronous model, fairness, instantaneous delivery.
  b. Vacuity: state one concrete attack the functionality forbids. If you cannot, the specification may be too weak to be worth proving.
  c. Totality: is behaviour defined for every message in every corruption state, including out-of-order, duplicate, and post-abort messages?
  d. Responsiveness: does the functionality or protocol send a modelling-related message to the adversary and then depend on a reply? What happens if no reply comes, or if control returns by another path? Check unintended state changes, race conditions, and reentrance.
  e. Corruption interface: exactly what leaks on corruption, and does the informal description match the code?
  f. Identifier hygiene: does the argument rely on SID uniqueness or unforgeability that no functionality provides?

F3 COMPOSITION
  a. Are the hypotheses of the invoked composition theorem checked item by item? Quote where.
  b. Subroutine-respecting: does any subroutine communicate with entities outside the calling instance? Is any state shared across sessions (a signing key, a counter, a ledger, an oracle)?
  c. If state is shared, does the paper use joint-state, GUC, or UCGS machinery, and is the theorem invoked the one that matches the machinery used?
  d. Is a single-session result promoted to multi-session, and is the promotion licensed?
  e. Is the composition theorem applied to a protocol that fails the framework's well-formedness or polynomial-time conditions?

F4 TIME, SYNCHRONY, NETWORK
  a. Is a round structure assumed that the underlying asynchronous model does not provide?
  b. Is a clock or bounded-delay channel used, and is its functionality specified and realizable?
  c. Is rushing assumed in a form that constrains the order of send and receive within a round?
  d. Does any argument rely on an activation order the framework does not guarantee?

F5 PROBABILITY AND REDUCTIONS
  a. Expectation versus realized value. For every bound, state whether the quantity sits inside or outside the probability the theorem quantifies over. Flag any substitution of an expected cost for the cost of a specific run, any use of E[f(X)] where f(E[X]) was bounded, and the reverse.
  b. Worst case versus average case. Does the theorem require a per-run or worst-case guarantee while the proof supplies an average or a bound in expectation? If so, is there a tail bound, and is it stated?
  c. Identical-until-bad. For each hybrid pair claimed to differ only on a bad event, verify the two games are syntactically identical until the flag is set, and that the flag's probability does not depend on choices the adversary makes after the fork.
  d. Conditioning. After conditioning on a bad event or its complement, does the argument still treat other variables as independent or uniform?
  e. Union bounds over adaptively chosen index sets, or over sets whose size depends on adversarial behaviour.
  f. Loss factors. Collect every multiplicative and additive loss: session count, hybrid count, index guessing, rewinding. Does the final bound account for all of them? Is anything absorbed into an asymptotic that the concrete claim needs?
  g. Hybrid arguments: is the per-step gap negligible AND the number of hybrids polynomial? Both, separately.
  h. Is any reduction's adversary given inputs it cannot compute, or required to answer queries it cannot answer?

F6 ADAPTIVE CORRUPTION AND ERASURES
  Apply this whole block whenever B4 is anything other than static. If B4 is static, answer only F6a, and additionally state in one line whether any claim, abstract, or informal remark in the paper suggests adaptive security; a static proof described as adaptive is a finding.
  a. Schedule granularity. At what instants may the adversary corrupt: only between activations, or also mid-activation, mid-local-computation, and while a subroutine call is outstanding? Name the earliest and latest corruption instants the argument's case analysis covers, then exhibit one admissible instant it does not cover.
  b. Commensurability with the ideal world. For every real-world corruption the simulator must effect a corresponding ideal-world corruption. State for each: whether the functionality's corruption interface admits corruption at that instant; exactly what the functionality returns to the simulator then; and whether that suffices to produce the state the environment expects. A functionality that retains a party's input only until output delivery cannot support corruption after delivery.
  c. Equivocation ledger, field by field. For every message the simulator sent on behalf of a party while that party was honest, list the coins, keys, plaintexts, and intermediate values it must later exhibit to explain that message, with the source of each. A missing entry is the commitment problem, and it is a failure of this ledger rather than a property of any one primitive (Nielsen 2002).
  d. Erasure semantics. If erasures are assumed: is an erasure atomic within an activation, or can the adversary corrupt between computing a value and erasing it? Exactly which values are erased, and is the randomness that produced an already-sent message among them? Does any subroutine or global setup retain state the caller believes erased? "We assume erasures" does not state an erasure model, and the amount of state exposed on corruption is what determines the power of the adaptive adversary (Canetti, Feige, Goldreich, Naor 1996).
  e. Subsidiaries. Corrupting a party normally exposes the state of the machines it spawned. Does the argument account for subroutine state revealed by a corruption, including a joint-state or global subroutine shared with other sessions? Does corrupting one caller expose a key that other sessions depend on?
  f. Messages in flight. A party corrupted after sending a message but before its delivery: may the adversary now drop or replace it, and does the ideal world admit the corresponding late change of input? Verify that the channel functionality actually grants what the proof uses, in both directions.
  g. Post-output corruption. The environment may corrupt at any point until it halts, including after every output has been delivered. Does the case analysis extend past protocol termination, and what state must the simulator produce there?
  h. Static machinery inside an adaptive proof. Flag any reduction, hybrid, invoked lemma, or assumption that fixes the corrupted set in advance and is then used against an adaptive adversary. If the corruption pattern is guessed, write the loss factor explicitly and check it against F5f: a guess over subsets of parties is exponential unless the set is bounded, and complexity leveraging must be stated, not absorbed. Adaptive security does not follow from static security in general (Canetti, Damgård, Dziembowski, Ishai, Malkin 2004).
  i. Hybrids that fix behaviour. For every hybrid in which a party's behaviour is replaced, simulated, or fixed, say what happens if that party is corrupted while the hybrid is in force. A hybrid defined only for parties that remain honest is a finding, and the indistinguishability claim for that transition is UNJUSTIFIED until the corrupted case is given.
  j. Late-determined programming. If the simulator programs an oracle, a CRS, or a key at corruption time, the programmed point is chosen late. Bound the probability that the environment already queried or constrained it, and say why the programming stays consistent with every answer already given. Under a global or non-programmable setup this route is unavailable; check F1g.
  k. Corruption knowledge as a free resource. Does any step use the corruption pattern before the adversary fixes it, including implicitly through a quantity that depends on the final corrupted set (an index chosen "for the party that stays honest", a hybrid indexed by the honest set)?
  l. Mobile or proactive corruption. If parties may be released from corruption, specify the state at recovery, who resets it, whether the functionality models recovery at all, and whether the security claim is per-period or global.
  m. Threshold discipline. If at most t corruptions are assumed, is the bound enforced at every instant rather than only at the end? Does any step assume the honest set is fixed, where the model only guarantees that its size stays at least n minus t?

F7 COUNTERFACTUAL SENSITIVITY
  For each modelling choice recorded in B4, B5, B8, and C2, name the first step of the argument that breaks if the choice is reversed. Include at least: static in place of adaptive, adaptive in place of static, erasures removed, and erasures made non-atomic. A result whose proof is insensitive to a choice the paper emphasizes, or hypersensitive to one it does not mention, is a finding either way.

--- PHASE G. HYPOTHESES, EDGE CASES, EXTERNAL DEPENDENCIES ---
G1. For each stated hypothesis, name where it is used. A hypothesis never used is a finding: either the statement is weaker than it needs to be, or the hypothesis is doing hidden work elsewhere.
G2. List every assumption the argument uses that the statement does not contain: implicit finiteness, well-definedness, non-degeneracy, side conditions, independence, unique decodability, honest majority.
G3. Audit the statement itself: quantifier order and scope, implicit domains, and degenerate cases. Check at minimum: no corruptions, all parties corrupted, corruption before the first message, corruption between a send and its delivery, corruption after every output has been delivered but before the environment halts, corruption of the last remaining honest party, empty input, duplicate SIDs, an adversary that never delivers, an environment that halts immediately.
G4. External dependencies. List every cited lemma or theorem the argument invokes. For each, state marked [UNVERIFIED] what you are assuming it says. Where the statement was not provided, say explicitly that your verification is conditional on it, and name every conclusion that inherits the condition.

--- PHASE H. ADVERSARIAL SYNTHESIS ---
Select the three weakest points found so far. For each, attempt to construct an explicit distinguishing environment or attack: the environment's inputs to parties, its interaction with the adversary, its output rule, and its advantage computed or bounded. Report ATTACK (it works), FAILED (name the blocker), or INCONCLUSIVE (name what you would need). An honest FAILED with a stated blocker is more valuable than a vague suspicion.

--- PHASE I. FINDINGS ---
Emit findings sorted by severity: FATAL, MAJOR, MINOR, EDITORIAL, with editorial last so it never dilutes the technical findings. One record per finding, in the schema supplied to you. For each ERROR additionally state:
  - the invalid inference as "the paper infers X from Y, which does not follow because Z";
  - whether the theorem is false or merely unproven;
  - the minimal counterexample, or the exact missing hypothesis;
  - one or two candidate repairs, each with its cost: weaker bound, stronger assumption, restricted corruption model, changed metric, additional functionality.
Every reported error carries a concrete witness: a counterexample, or the exact invalid inference. Vague concerns and stylistic preferences are not findings.

--- PHASE J. SELF-AUDIT AND VERDICT ---
J1. Coverage table: every Phase F item, marked done, not applicable, or not performed, with a reason for anything not performed.
J2. Every place you relied on a convention rather than on text in the material.
J3. Everything you supplied that the material does not state.
J4. Open-obligations ledger. One entry per item you deferred to material not provided in this bundle, in the ledger schema supplied to you: what you assumed it says, which unit or label you believe holds it, and every step and finding that inherits the assumption. An empty ledger is an assertion that the bundle was closed; make it explicitly.
J5. Confidence for each ERROR as HIGH, MEDIUM, or LOW, with a one-line reason. Do not inflate.
J6. A single final line, exactly:
VERDICT: SOUND | HAS GAPS | INVALID
An argument that is internally valid but depends on an [UNVERIFIED] external result is HAS GAPS, not SOUND. Name the result on the same line.

=== END OF PROMPT ===
~~~

---

## 2. Staged pipeline

Run stages separately for a full paper. Carry forward only the artifacts named.

| Stage | Input | Prompt core | Artifact |
|---|---|---|---|
| S0 Normalize | full paper | extract labels, definitions, functionality pseudocode, theorem statements verbatim into a numbered index; change nothing | `index.md` |
| S0.5 Partition | S0 index, full source | the non-evaluative partition prompt below; emits units, bundles, and audit order | `units.md` |
| S1 Model | S0 index, framework sections | Phases B and C, plus F4 | `model-audit.md` |
| S2 Functionalities | functionality pseudocode only | D2 and F2 | `func-audit.md` |
| S3 Simulator | simulator description, main proof | D1 then F1 | `sim-audit.md` |
| S4 Hybrids | one hybrid pair per call | D3 and F5, per transition | `hybrid-audit.md` |
| S5 Composition | theorem statements and invocation sites | F3, with the cited theorem's hypotheses quoted from its source | `comp-audit.md` |
| S6 Attack | the three to five weakest findings | Phase H only, one point per call, with permission to fail | `attack-log.md` |
| S7 Consolidate | all artifacts | deduplicate, resolve contradictions, discharge every ledger entry against the source, run the global-only checks reserved in P6, triage | `report.md` |

S3's rewrite is the highest-yield single instruction here. Forcing the simulator into explicit code with named state exposes missing fields, out-of-order extraction, and unhandled corruption transitions that prose conceals. S4 must run once per transition.

Audit in the order S0.5 computes: leaves first, in reverse topological order, so that a unit's dependencies carry verdicts rather than `[UNVERIFIED]` tags by the time the theorem consuming them is reached.

### S0.5, the partition prompt

Emits structure only. Any sentence evaluating the argument is a violation; an early impression of soundness formed here propagates into every downstream stage.

~~~text
=== S0.5 PARTITION (non-evaluative) ===
From the normalized index and the full source, produce the audit unit list. Emit no
verdicts, no assessment of correctness, and no impression of quality. Any sentence
evaluating the argument is a violation.

P1. Dependency graph. One node per numbered object (definition, functionality,
    lemma, theorem, hybrid). One edge U -> V when U's statement or proof uses V.
    Edges come from explicit references AND from symbol use: any symbol occurring in
    U but bound outside U is an edge to wherever it is bound. State where each is
    bound. Standard template and package macros are not nodes.
P2. Candidate units. A minimal set of nodes you would audit together. Nodes joined
    by a shared invariant, a shared simulator, or a shared state variable belong to
    one unit. Splitting them destroys the evidence the audit needs.
P3. Closure test. Unit U is SELF-CONTAINED relative to bundle B only if every
    symbol, definition, hypothesis, corruption convention, and cited result used in
    U appears verbatim in B. Otherwise list each missing item as MATERIALIZE (paste
    its statement into B) or UNAVAILABLE (to be marked [UNVERIFIED] at audit time).
    Do not call a unit self-contained on the ground that you could reconstruct a
    missing item yourself.
P4. Criticality. For each leaf, name every theorem that fails if this node is false.
    Rank units by number of dependents, then by proof depth. Keep this reading
    structural: which result is invoked where, never whether the invocation is sound.
P5. Audit order. Reverse topological, leaves first. Break any cycle by naming the
    mutual dependency as a finding candidate for Phase G4.
P6. Global-only checks. List the checks no single unit can perform: notation drift
    across sections, hypotheses stated in one section and used in none, state shared
    across sessions, corruption model commensurability, total loss factor across the
    whole reduction chain. These are reserved for S7 and must not be attempted here.

Output units.md: per unit, its node list, its bundle manifest (MATERIALIZE and
UNAVAILABLE items separated), its dependents, and its rank.
~~~

---

## 3. Probe bank

Insert verbatim when a stage returns thin results. Each is phrased to be unanswerable by paraphrase.

1. At which activation, precisely, does the simulator first learn the value it must commit to? Quote the line.
2. Party P is corrupted immediately after message 3. Enumerate every field of P's internal state the environment now sees, and for each name where the simulator obtains a consistent value.
3. Name one behaviour permitted by the real protocol and forbidden by the ideal functionality. If you cannot, explain why the functionality is not vacuous.
4. Rewrite the functionality so every message in every state has defined behaviour. List the cases you had to invent.
5. Suppose the random oracle is global and non-programmable. Which steps fail, and at which line?
6. Suppose the CRS is chosen by an external party the simulator cannot influence. Which steps fail?
7. Give the concrete bound with all loss factors written out: no asymptotic notation, no absorbed constants.
8. Every place the paper writes an expectation: is it inside or outside the probability the theorem quantifies over? Tabulate.
9. Does the conclusion hold for every execution, or only on average over the coins? Quote the quantifier in the theorem and the quantifier the proof establishes.
10. Quote the hypotheses of the composition theorem invoked, from its original source, and point to where each is verified.
11. Does the proof anywhere rely on knowing the corruption pattern before it happens?
12. Is any subroutine instance shared between two sessions? Trace one shared object end to end.
13. Which steps break if the adversary never responds to a network-interface query?
14. Construct an environment that distinguishes by timing or activation order alone.
15. Which lemma in the appendix, if false, would invalidate the main theorem? Audit that lemma first.
16. Which hypothesis of the theorem is never used in the proof? If none, name the step that uses each.
17. Name one modelling choice the paper makes whose reversal would leave every step intact. Why is it stated?
18. Corrupt the sender one activation after it sent its message and one activation before delivery. Write out the state the environment now sees, entry by entry, and the simulator's source for each entry.
19. The environment corrupts every party after all outputs are delivered, then halts. Which line of the proof covers this, and what does the functionality return to the simulator at that point?
20. Erasures are assumed. Name the exact instruction after which the value is gone, and say what the adversary sees if it corrupts one instruction earlier.
21. In hybrid H_i a party's messages are simulated. That party is corrupted while H_i is in force. Is H_i still well defined, and does the claimed distance to H_{i+1} still hold?
22. Does any quantity in the proof, including a hybrid index or a challenge position, depend on which parties end up corrupted? If so, when is it fixed relative to the adversary's choice?

Probe 15 is the right opener for any appendix audit. Probes 8, 9, and 16 catch the two failure modes that survive refereeing most often: substituting an expected value for a realized one, and a hypothesis that appears in the statement but does no work in the proof. Probes 18 to 22 are the adaptive-corruption battery; each is a specific corruption instant, because "is the proof adaptively secure" is answerable by paraphrase and "corrupt the sender here, now enumerate the state" is not.

---

## 4. Output schema

One record per finding, emitted as a machine-readable sidecar so consolidation and cross-run deduplication stay mechanical.

```yaml
- id: F-014
  stage: S4
  anchor:
    label: "thm:main / hybrid H_3 -> H_4"
    page_or_line: "p. 27, eq. (14)"
    trigger: "by linearity of expectation"
  verdict: ERROR            # ERROR | GAP | CONVENTION | UNVERIFIABLE | QUESTION
  category: F5a             # checklist item
  severity: FATAL           # FATAL | MAJOR | MINOR | EDITORIAL
  confidence: HIGH          # HIGH | MEDIUM | LOW
  earliest_failing_step: "E.17"
  claim: "The paper infers X from Y."
  why_invalid: "Y bounds the expected value; X requires the value for the run in which the bad event occurs. These differ because the event is positively correlated with the cost."
  counterexample: "Take the distribution ..., where E[C] = k but C = 0 on the conditioned event."
  repairs:
    - "Replace the metric by its worst-case variant; costs a factor of ... in the bound."
    - "Add a tail bound via ...; requires assumption ... ."
  affects: ["thm:main", "cor:2", "sec:6"]
  supplied_by_auditor: "none"
  conditional_on: []        # ledger ids this finding depends on
```

Ledger records are emitted separately, one per item deferred to material outside the bundle. S7 must close every one of them.

```yaml
- id: OB-003
  unit: "S4 / hybrid H_3 -> H_4"
  assumed: "Lemma 4.2 gives a per-run bound on C, not a bound in expectation."
  believed_location: "lem:4.2, appendix B (not in this bundle)"
  why_needed: "Step E.17 substitutes the bound into a per-run quantity."
  inherits: ["E.17", "E.18-E.24", "F-014"]
  if_false: "F-014 upgrades from GAP to FATAL; thm:main is unproven as stated."
  status: OPEN             # OPEN | DISCHARGED | PROMOTED_TO_FINDING
```

---

## 5. Severity rubric

- **FATAL.** The theorem as stated is false, or the central inference is invalid with no visible route to repair inside the paper's framework. Test: can the abstract's claim survive?
- **MAJOR.** The theorem is plausibly true but not proved. Repair needs new argument, a weaker bound, or a stronger assumption. Includes invoking the wrong composition theorem, and unspecified functionality behaviour the proof relies on.
- **MINOR.** Local slip, recoverable by a reader: wrong constant, mislabelled hybrid, omitted case that is genuinely symmetric.
- **EDITORIAL.** Notation, references, exposition. Reported last and separately.

Include the calibration line in every stage prompt: *distinguish a defect in the paper from a gap in your own knowledge; if a step is standard in a literature you cannot access, mark it UNVERIFIABLE, not ERROR.* Without it, audits generate a long tail of false positives on framework conventions, which trains the reader to ignore the report.

---

## 6. Adjudication and defense passes

Two independent runs disagree usefully. Adjudicate rather than average.

~~~text
You are adjudicating two independent audits of the same UC result. For each finding:
- Classify as CONFIRMED (both runs, compatible reasoning), CONTESTED (one run only, or incompatible reasoning), or SPURIOUS (rests on a misreading you can identify by quoting the material).
- For every CONTESTED finding, state the single question whose answer would settle it.
- Produce a merged list ordered by severity, then confidence.
- Report the disagreement rate, and name the checklist categories the two runs disagreed on most; those are the categories where the audit itself is unreliable.
Do not resolve a disagreement by averaging. Pick a side and give the reason, or leave it CONTESTED.
~~~

For your own paper, add a third pass in which the auditor defends the paper against the audit, and must, for each finding, either concede, refute with a quotation, or propose the cheapest repair. Findings that survive all three passes are the ones worth a week.

---

## 7. LaTeX sidecar variant

To feed the existing `proofread-check` pipeline, append this to Phase I. It keeps the audit read-only and machine-consumable.

~~~text
DELIVERABLES (do not modify the source files)
1. NAME-uc-audit.tex, in the same directory: the complete original source with findings inserted inline as \aicomment{[cat] one-line issue} followed where applicable by \aifix{concrete suggestion}. Full source, nothing elided. Category is one of sim, func, comp, prob, model, def, thm, proof, notation, ref.
2. NAME-uc-audit-report.tex and its compiled PDF: self-contained, using only \documentclass[11pt]{article} with geometry, xcolor, hyperref, enumitem, and nothing from the paper's own preamble. One subsection per section of the source, in document order, each finding an item with category tag, one-line description, location, and suggested fix. Clean sections are listed "No issues found". Global findings go under a final "Cross-file notes".

LATEX SAFETY
Everything inside \aicomment{...} and \aifix{...} becomes part of the source. Escape text-mode specials: % & # _ $ as \% \& \# \_ \$. Avoid bare backslashes and unmatched braces. An unescaped % comments out the closing brace and breaks compilation. Name symbols in math mode ($x_i$, $\Adv$) rather than as text. Never execute the paper's macros in the report: refer to them as literal text, for example \texttt{\textbackslash FAC}, and paraphrase math rather than pasting it.

PLACEMENT
Code and algorithm environments are protected: comment only, never redline inside them. For a float, place the comment inside the float but outside the inner code or algorithmic block, just after \caption, so it travels with the float. For a non-floating verbatim-style listing, place the comment immediately before or after the environment, since macros are not interpreted inside.
~~~

---

## 8. Design notes

**What each source contributes.** The staged suite supplies extraction before judgement (Phase B), the adversarial framing (Phase H), and `UNVERIFIABLE` as a first-class verdict. The single-proof verifier supplies the independent baseline (Phase A), atomic step verdicts with an earliest failing step (Phase E), and the unused-hypothesis check (G1), all of which the suite lacks. The `proofread-check` skill supplies anchoring discipline, the injunction against inventing problems, and the external-context caution now in C3.

**The one conflict, resolved explicitly.** The suite says an audit that finds nothing has failed; the verifier says a sound proof is a valid finding. The prompt resolves this in the mandate: the presumption of defect is a search heuristic that governs effort, and calibrated reporting governs output. Left unresolved, the model either manufactures findings to satisfy the quota or approves the proof to satisfy the calibration note.

**Two additions not in any source.** Phase D makes reification mandatory rather than a stage-three aside: rewriting the simulator as code with named state, and each functionality as a message-by-state table, converts prose ambiguity into an enumerable list of invented fields. Phase F6 asks, for each modelling choice, which step breaks if the choice is reversed. This catches both directions of mismatch: a proof insensitive to a choice the paper emphasizes, and a proof hypersensitive to one it never mentions.

**Why the protocol partitions rather than reading the whole paper.** Local checks degrade with irrelevant context: performance is highest when the relevant material sits at the start or end of the input and drops significantly when it must be retrieved from the middle, even in models built for long contexts (Liu et al., TACL 2024). Phase E step verdicts and the field-by-field equivocation check in F1c are exactly the checks that suffer. The countervailing pressure is that subroutine-respecting, shared state across sessions, and corruption-model commensurability are global properties by construction, and an unused hypothesis is only visible to a reader who saw both the statement and the whole proof. The resolution is the module-and-linker structure: per-unit runs with an explicit bundle manifest, a ledger of unresolved externals, and one consolidation pass that sees every artifact but none of the raw text.

**Why adaptive corruption gets its own block.** The defects are not local to any one step, which is why a step-by-step reader misses them. They live in the cases the case analysis never enumerates: a corruption instant nobody considered, a hybrid well defined only while a party stays honest, a functionality whose corruption interface cannot answer the query the simulator must make, an erasure that the model permits the adversary to interrupt. F6 is therefore written as an enumeration of instants and of state, not as a question about the corruption model, and it demands a ledger with a named source per field. The three items most likely to be missed entirely are F6b (the ideal-world side of a corruption, since the functionality's corruption interface is usually the least specified part of the paper), F6g (corruption after outputs are delivered, since informal reasoning stops at protocol termination), and F6h (statically fixed machinery reused adaptively, since the resulting loss factor is easy to absorb into an asymptotic).

**Why anchoring is a hard rule.** An anchored finding can be checked against the source in seconds. An unanchored one costs the same to refute as to produce, which is how audit reports become unreadable.

---

## 9. References

Checks in the prompt draw on the following. All bibliographic details verified.

- Canetti, R. 'Universally Composable Security'. Journal of the ACM 67(5), Article 28, 94 pages, 2020. doi:10.1145/3402457. Full version, Cryptology ePrint Archive 2000/067, revised repeatedly, which is why B1 asks for the revision. Source for the dummy-adversary equivalence (F1e) and for the quantifier order that separates UC emulation from the specialized-simulator relaxation (F1d).
- Canetti, R., Dodis, Y., Pass, R., Walfish, S. 'Universally Composable Security with Global Setup'. TCC 2007. Global setup, hence F1g and F3c.
- Badertscher, C., Canetti, R., Hesse, J., Tackmann, B., Zikas, V. 'Universal Composition with Global Subroutines: Capturing Global Setup within plain UC'. TCC 2020; Cryptology ePrint Archive 2020/1209. The machinery F3c asks the paper to match.
- Canetti, R., Rabin, T. 'Universal Composition with Joint State'. CRYPTO 2003, LNCS 2729, pp. 265-281. Shared state across sessions, hence F3b and F3c.
- Hofheinz, D., Shoup, V. 'GNUC: A New Universal Composability Framework'. Journal of Cryptology 28(3), pp. 423-508, 2015; ePrint 2011/303. Differs from UC on protocol structure, polynomial time, and corruption, which is why B1 and B8 are separate inventory items.
- Küsters, R., Tuengerthal, M., Rausch, D. 'The IITM Model: A Simple and Expressive Model for Universal Composability'. Journal of Cryptology 33(4), pp. 1461-1584, 2020; ePrint 2013/025.
- Camenisch, J., Krenn, S., Küsters, R., Rausch, D. 'iUC: Flexible Universal Composability Made Simple'. ASIACRYPT 2019, LNCS 11923; ePrint 2019/1073.
- Camenisch, J., Enderlein, R.R., Krenn, S., Küsters, R., Rausch, D. 'Universal Composition with Responsive Environments'. ASIACRYPT 2016, part II, pp. 807-840. The source of the non-responsiveness artifacts checked in F2d.
- Hofheinz, D., Unruh, D., Müller-Quade, J. 'Polynomial Runtime and Composability'. Journal of Cryptology 26(3), pp. 375-441, 2013. Why B8 and F1f are asked separately from everything else.
- Nielsen, J.B. 'Separating Random Oracle Proofs from Complexity Theoretic Proofs: The Non-Committing Encryption Case'. CRYPTO 2002, LNCS 2442, pp. 111-126. The commitment problem behind F1c and F6c.
- Canetti, R., Feige, U., Goldreich, O., Naor, M. 'Adaptively Secure Multi-Party Computation'. STOC 1996, pp. 639-648. doi:10.1145/237814.238015. Establishes that the power of an adaptive adversary is governed by how much state a corruption exposes, which is why F6d asks what is erased rather than whether erasures are assumed.
- Canetti, R., Damgård, I., Dziembowski, S., Ishai, Y., Malkin, T. 'Adaptive versus Non-Adaptive Security of Multi-Party Protocols'. Journal of Cryptology 17(3), pp. 153-207, 2004. The separation invoked in F6h: for Byzantine adversaries adaptive security is strictly stronger than non-adaptive security, for any number of parties.
- Canetti, R., Lindell, Y., Ostrovsky, R., Sahai, A. 'Universally Composable Two-Party and Multi-Party Secure Computation'. STOC 2002, pp. 494-503. The reference point for what adaptive UC realization costs in setup and assumptions.
- Bellare, M., Rogaway, P. 'The Security of Triple Encryption and a Framework for Code-Based Game-Playing Proofs'. EUROCRYPT 2006, LNCS 4004, pp. 409-426; ePrint 2004/331. The identical-until-bad discipline in F5c.
- Canetti, R., Cohen, A., Lindell, Y. 'A Simpler Variant of Universally Composable Security for Standard Multiparty Computation'. CRYPTO 2015, LNCS 9216, pp. 3-22.
- Rausch, D., Küsters, R., Chevalier, C. 'Embedding the UC Model into the IITM Model'. EUROCRYPT 2022; ePrint 2022/224. Relevant when a result proved in one model is cited inside another.
- Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., Liang, P. 'Lost in the Middle: How Language Models Use Long Contexts'. Transactions of the Association for Computational Linguistics 12, pp. 157-173, 2024. doi:10.1162/tacl_a_00638. The empirical basis for partitioning rather than auditing a whole paper in one pass.
