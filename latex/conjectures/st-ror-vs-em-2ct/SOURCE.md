# Provenance: One Standard-Oracle Real-or-Random Challenge Query Does Not Imply One Embedding Two-Ciphertext Challenge Query

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Relationships between quantum IND-CPA notions**
- Authors: Tore Vincent Carstens, Ehsan Ebrahimi, Gelo Tabia, Dominique Unruh
- Venue/archive: IACR Cryptology ePrint Archive (preprint, 47 pages) 2020
- Identifier: IACR ePrint 2020/596
- Bibliographic detail: inferred
- File: `2020-596.pdf` (47 pages)
- sha256: `6bf24750709898e73eba224f90196b7146e936a1c643ffc28cb65417b9c86ead`
- Read on 2026-08-18T12:58:12Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Both notions are singleton equivalence classes in the paper's classification. The paper settles the relation of the real-or-random standard-oracle notion to five other panels and settles that the embedding two-ciphertext notion is not implied by the Boneh-Zhandry family or by the erasing-learning-query family, but leaves open whether it is implied by the real-or-random standard-oracle notion. This is one of the six non-implications the paper explicitly conjectures.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 45 | 45 | exact (100%) | Assuming P 12 6=⇒ P 7, since P 2, P 5 =⇒ P 7, then P 12 6=⇒ P 2, P 5. |
| openness | 36 | 36 | exact (100%) | The relation between P 12 and P 2, P 5, P 6, P 7, P 9, P 11 remain open. |
| progress | 45 | 45 | exact (100%) | Here, the adversary that attacks (EM , 2ct) expects to receive back four quantum registers that are the evaluation of the encryption oracle on two quantum input... |
| definition | 45 | 45 | exact (100%) | These notions have classical learning queries and one challenge query of type (ST , ror) and (EM , 2ct), respectively. |
| progress | 44 | 44 | exact (100%) | No natural mode of operation is secure in the sense of learn(∗, CL)-chall(1, ST , ror) notion. |
| parameter | 6 | 6 | exact (100%) | All of non-implications hold on the assumption of the existence of a quantum secure one-way function. |
| progress | 30 | 30 | exact (100%) | A less general version of this theorem (when there is only one challenge query) is used to show the equivalences of the notions in Panel 5. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's own and genuinely open: it is item 6 of Section 9's six conjectured non-implications (p. 45), cell (P12, P7) of Table 1 is a question mark (p. 6), Panel 12's discussion leaves P7 open (p. 36), and I confirmed no result in Sections 7 or 8 resolves it and that pages 45-47 are bibliography with no appendix. The two challenge-query unitaries, the direction of the separation, the negation of security, and the quantum-one-way-function hypothesis all transcribe correctly, and all seven quotes are verbatim on the pages claimed. The single most important defect is not in the formal statement but in the surrounding apparatus: Corollary 43 is paraphrased with only one of its two conjoined conditions, so the draft credits the paper with ruling out a materially larger class of modes of operation than it actually does — repairable, alongside the unsupported post-challenge learning queries in Definition 7.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 45 | Section 9 poses it explicitly as item 6: "(P 12?P 7). These notions have classical learning queries and one challenge query of type (ST , ror) and (EM , 2ct), respectively." Table 1 (p. 6) carries "?" at cell (P12, P7); Figure 1 labels P12 = learn(*,CL)-chall(1,ST,ror), and p. 5 gives Panel 7 = learn(*,CL)-chall(1,EM,2ct). Both are singleton panels, as the draft says. |
| Openness | pass | 36 | Panel 12 discussion: "The relation between P 12 and P 2, P 5, P 6, P 7, P 9, P 11 remain open." I read past the cited passage: I enumerated every result in Sections 7 and 8 (Thms 27, 28, Cor 29, Thms 33, 34, 39, 40, 41, 42, Cor 43, Thm 44) and none addresses P12 => P7. Pages 45-47 are the bibliography; the paper has no appendix. Section 9 (p. 44) frames it as one of six conjectured non-implications that would close all 41 open cells. |
| Strength | pass | 6 | The paper fixes the meaning of non-implication: "a notion P does not imply Q if there exists an encryption scheme that is secure with respect to the notion P and insecure with respect to the notion Q." The draft's clause 1 (Pi is P12-secure) and clause 2 (Pi is not P7-secure) instantiate exactly this for P12 ⇏ P7 — no strengthening, no weakening, no generalization to other panels. |
| Quantifiers and parameters | pass | 12 | Symbol-by-symbol match. Paper: U_{EM,2ct,r0\|\|r1,b} : \|m0,m1,0,0> -> \|m0,m1,Enc_k(m_b;r0),Enc_k(m_bbar;r1)>, with r0,r1 sampled independently from {0,1}^t and Q_out0,Q_out1 prepared by the challenger in \|0>^{n'} — the draft reproduces this including the two distinct randomnesses. Paper p. 13: chall(.,ST,ror) applies U_{Enc_k o pi^b} to the adversary's own Q_in, Q_out for a random permutation pi on {0,1}^n — draft matches. "1" means exactly one challenge query (p. 14); learn(*,CL) is polynomially many classical queries for a QPT adversary. The negation of Definition 7's "at most 1/2 + eps for some negligible eps" as ">= 1/2 + 1/p for infinitely many eta" is the correct negation. Definition 2's signatures for KGen/Enc/Dec and the correctness condition are reproduced exactly (p. 9). |
| Attribution | pass | 44 | This is the harvested paper's own conjecture, not a problem it credits to someone else: "In Figure 1, we indicate six non-implications (with red dashed arrows) that if they hold, all the open questions will be resolved by the transitivity... then argue why these six non-implications are more likely to be true." The draft's openness_kind of "paper-conjectures" is right, and the count of six is right (P2?P9, P8?P7, P4?P6, P3?P11, P12?P11, P12?P7). |
| Definitions | fail | 10 | Definition 7 sequences the game Key Gen -> Learning Queries -> Challenge Queries -> Guess, and the only interleaving it grants is the parenthetical "the adversary is allowed to submit some learning queries between the challenge queries as well." With chall(1,...) there is exactly one challenge query, so "between" is vacuous and the paper's game affords no post-challenge learning phase. The draft's "in any order (learning queries may be made both before and after the challenge query)" adds adversarial freedom the paper does not grant, and it perturbs both clauses at once — strengthening the security demanded in clause 1 while enlarging the attacker in clause 2. Every other definition in the draft matches the paper exactly. |
| Fabrication | fail | 44 | Corollary 43 defines a "natural" mode of operation by two conjoined conditions: "there exists an input block i and an output block j such that output block j does not depend on i, but, ranging over all possible input messages, output block j can take any value." The draft's progress_note and setting_latex both state only the first condition, which makes the corollary rule out a strictly larger class of modes than it does. Separately, "the paper's separating constructions plant structure recoverable by Simon's algorithm [Sim97] from superposition queries only" holds for Section 7.3 (titled "Separations by Simon's Algorithm", using the sigma-periodic F_{s,sigma} of Definition 30), but not for the constructions actually relevant to this conjecture — Theorem 40, Theorem 42 and Corollary 43 all attack with a single-query Hadamard interference test, not Simon's algorithm. |
| Self-containment | pass | 12 | The notation and definitions blocks carry the encryption-scheme syntax, U_f, pi^b, the two challenge-query unitaries and the game, so a reader who has never opened the paper knows what object to build and what two properties to prove. The panel names P12/P7 appear only as orienting labels in the status and setting, not as load-bearing terms in the formal statement. |

### Unsupported by the paper

- progress_note and setting_latex: Corollary 43's "natural mode of operation" is reduced to a single condition (an output block independent of some input block), dropping the paper's second, conjoined requirement that "ranging over all possible input messages, output block j can take any value" (p. 44). As written the draft attributes to the paper a strictly stronger impossibility than it proves.
- definitions_latex: "learning queries may be made both before and after the challenge query" — Definition 7 (p. 10) grants learning queries only before the challenge phase and, by its parenthetical, between challenge queries; with chall(1,...) there is no post-challenge learning phase in the paper's game.
- setting_latex: "the paper's separating constructions plant structure recoverable by Simon's algorithm \cite{Sim97} from superposition queries only" — this describes Section 7.3 (Definition 30's sigma-periodic F_{s,sigma}, p. 37) but not the constructions relevant to P12 and P7: Theorem 40's r||PRF_k(r) XOR m, Theorem 42's qPRP-based scheme, and Corollary 43 all break with a single-query Hadamard interference test rather than Simon's algorithm (pp. 42-44).
- status_note: "The paper settles the relation of the real-or-random standard-oracle notion to five other panels" understates the record — p. 36 also settles P12 => P13 and P12 => P14 as implications, so seven relations are settled, five of them non-implications.

### Corrections the checker asked for

- **definitions_latex** — The clause "in any order (learning queries may be made both before and after the challenge query)" is not supported by Definition 7 (p. 10), which orders Learning Queries before Challenge Queries and permits learning queries only "between the challenge queries" — vacuous when there is exactly one challenge query.
  - suggested: Strike the parenthetical and the phrase "in any order": "a QPT adversary A makes polynomially many CL-learning queries followed by exactly one challenge query of type (Y, rt), all answered with this same k and this same b; finally A outputs a bit b' and wins iff b' = b."
- **progress_note** — Corollary 43 (p. 44) is paraphrased with only the first of its two conjoined conditions, overstating the class of modes it rules out. The paper's definition of a "natural" mode additionally requires that, ranging over all possible input messages, the independent output block can take any value.
  - suggested: "...the paper's Corollary 43 shows that no mode of operation is secure for it if, for some message length, there is an input block i and an output block j such that j does not depend on i and yet j can take any value as the input message ranges over the whole message space — a class the paper notes includes CBC (with i the second and j the first block)."
- **setting_latex** — Same omission of Corollary 43's second condition ("no mode of operation with an output block independent of some input block is secure for $P12$"), plus the unsupported generalization that "the paper's separating constructions plant structure recoverable by Simon's algorithm" — true of Section 7.3 only, whereas Theorems 40 and 42 and Corollary 43 attack with a single-query Hadamard interference test.
  - suggested: State Corollary 43 with both of its conditions as above, and narrow the Simon claim to: "the paper's Section 7.3 separations plant a sigma-periodic structure recoverable by Simon's algorithm \cite{Sim97} from superposition queries only, while the separations bearing on these two panels (Theorems 40 and 42, Corollary 43) instead use a single-query Hadamard interference test."

## Build

- pdflatex: ok
- chktex: 3 warnings
- lacheck: 0 warnings

## What to check hardest

(1) The hypothesis that quantum-secure one-way functions exist is mine, following the paper's convention for its proved separations; some assumption of this kind is unavoidable, since with no such function no scheme is secure in either notion and the implication holds vacuously. (2) The paper is a 2020 ePrint; a later version of this work or follow-up work may have closed this cell, and I have not checked against the newest version. (3) My reading that Theorem 20's derivation of the two-ciphertext format from the real-or-random format fails here specifically because it consumes embedding-model learning queries is a reading of that proof, not a sentence the paper states about this cell; the paper's own stated obstruction is the register-counting one I quote. (4) The paper's per-panel bookkeeping should be checked independently: the boxed panel lists on pages 4-5 contain at least one error (the Panel 11 box repeats Panel 10), although the two singleton panels used here are stated consistently in the boxes, in Figure 1 and in Corollary 43.

