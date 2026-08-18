# Provenance: One-Shot Decryption Without Extractability

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Proactive Secret Sharing without Erasures**
- Authors: Alexandru Cojocaru, Aggelos Kiayias, Yu Shen, Petros Wallden
- Venue/archive: IACR Cryptology ePrint Archive 2026
- Identifier: 2026/1072
- Bibliographic detail: inferred
- File: `2026-1072.pdf` (35 pages)
- sha256: `47fdd83138952b6faf279c0d5d0bfc626b1500d4c6b93ef81000dac9a52cf15f`
- Read on 2026-08-18T16:36:20Z via the `cli` backend

## How the paper leaves it open

`paper-asks-question`. Open. With extractable witness encryption the primitive is constructed for every $f < 1/2$ (the paper's Theorem 2), and nothing at all is known if extractability is dropped --- the paper's reduction has no substitute, since the witness-encryption statement in the construction is a true statement, where indistinguishability security is vacuous. The single-receiver (non-threshold) variant is separately argued to be unachievable by a gentle-measurement rewinding attack, so the threshold structure is not negotiable.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| openness | 7 | 7 | exact (100%) | An important direction left open by our work is whether the extractability requirements underlying our constructions can be weakened or eliminated altogether, f... |
| statement | 20 | 20 | exact (100%) | Assuming one-shot signatures as defined in Definition 5 and post-quantum extractable witness encryption as defined in Definition 6, there is a threshold public-... |
| openness | 7 | 7 | exact (100%) | Even weakening extractability to more structured assumptions would already constitute meaningful progress. |
| definition | 16 | 16 | exact (100%) | We term this new primitive threshold PKE with one-shot decryption (Definition 10). In this scheme, there is a committee of (quantum) private-key holders, to whi... |
| progress | 20 | 20 | exact (100%) | Note that the extractable security of witness encryption implies that, if an adversary A has non-negligible distinguishing advantage, then given the statement, ... |
| progress | 7 | 7 | exact (100%) | Our primary goal is to demonstrate for the first time that proactive security without erasures is achievable, and to identify quantum cryptographic mechanisms t... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is real, is the paper's own, and genuinely stays open: p.7 says in the paper's own voice that whether extractability can be weakened or eliminated is \"left open by our work\", and every positive result (Theorems 2-5, pp.20/23/26/29) still assumes extractable witness encryption with nothing later retracting it. The single most important defect is that the paper contains no notion of indistinguishability-secure witness encryption at all - Definition 6 (p.12) defines only the extractable variant - so the draft's headline implication \"OSS + plain WE => threshold one-shot decryption for every f<1/2\", cross-referenced as if it came from the paper, is a harvester-built strengthening of an existential question the paper deliberately left disjunctive. That plus a quantifier-wrong negative-resolution clause, a silently patched OSS definition, and a corruption phase that matches neither Experiment 1 nor Experiment 2 as printed are all precisely repairable, so the draft is salvageable rather than irrecoverable.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 7 | The problem is in the paper. Page 7, "On the underlying cryptographic assumptions": "An important direction left open by our work is whether the extractability requirements underlying our constructions can be weakened or eliminated altogether, for example by relying on more structured or restricted knowledge assumptions, or by developing alternative realizations of one-shot decryption without extractability." The primitive itself is Definition 10 (p.17) and the positive result is Theorem 2 (p.20), both cited correctly. |
| Openness | pass | 20 | It stays open. Extractable witness encryption (Definition 6, p.12) is the only witness-encryption notion the paper ever defines, and every positive result assumes it: Theorem 2 (p.20), Theorem 3 (p.23), Corollary 1 (p.24), Theorem 4 (p.26), Theorem 5 (p.29, functional WE). Sections 5, 6 and Appendices A-B contain no result removing or weakening extractability, and the phrase "indistinguishability security" occurs nowhere in the paper. Nothing resolves the question. |
| Strength | fail | 7 | The paper poses a disjunctive, existential question - can extractability be "weakened or eliminated altogether", by "more structured or restricted knowledge assumptions" OR by "alternative realizations of one-shot decryption without extractability" (p.7). The draft replaces this with one specific implication: OSS + indistinguishability-secure WE => threshold one-shot decryption for every f<1/2. That is strictly stronger than the paper's question (proving it answers the paper; refuting it does not), and the paper never names plain witness encryption as the replacement assumption. |
| Quantifiers and parameters | fail | 19 | Two errors. (i) The draft's closing clause asserts that a negative resolution would be "an oracle relative to which ... no threshold public-key encryption scheme with one-shot decryption for any f<1/2 does [exist]"; the negation of "for any f<1/2 there is a scheme" (Theorem 2, p.20) is "for SOME f<1/2 there is none", so the stated separation is far stronger than the negation. (ii) The draft folds one corruption phase into both experiments, carrying the free-of-charge posterior-corruption rule into the security experiment; the paper's Experiment 1 (p.18, lines 10-15) aborts whenever \|J'\|+\|J\| > fn with no exemption, and Experiment 2's printed test is "\|J'\| + 1 > fn" (p.19, line 14), matching neither of the draft's formulations. Separately, the paper's Experiment 2 pseudocode (p.19, lines 13-18) hands the adversary nothing at all for an already-decrypted party, contradicting the draft's "A may end up holding the state of all n parties" - though the p.17 prose the draft follows does say posterior corruption is unbudgeted, so the paper is internally inconsistent here. Ranges f<1/2, \|J\| >= (1-f)n for correctness and \|J\| > fn for Dec all match Definition 10 (pp.17-18). |
| Attribution | pass | 7 | The paper claims the question as its own: "An important direction left open by OUR work" (p.7, emphasis added). It is not a problem attributed to another paper. FHAS24 and ACL+22 are cited on the same page only as examples of more structured assumptions, which is how the draft presents them. |
| Definitions | fail | 12 | Three divergences. (1) The paper contains no definition of indistinguishability-secure witness encryption. Definition 6 (p.12), despite being titled "Witness Encryption", defines an EXTRACTABLE scheme: correctness plus extractable security only. The draft's "Definition 2, item (i)" - on which the entire conjecture's hypothesis (ii) rests - is the harvester's own supplied notion presented with a cross-reference as if the paper had it. (2) The draft's OSS security adds the clause m_0 != m_1; the paper's Definition 5 (p.12) omits it entirely. (3) The draft fixes the OSS message space to {0,1}^*; Definition 5 leaves it an abstract M, and Algorithm 1 (p.20) signs only tags in {0,1}^lambda. |
| Fabrication | fail | - | Unsupported assertions: (a) GGHW14 appears nowhere in the paper's bibliography (pp.29-32) and the paper never says extractable WE with arbitrary auxiliary input is implausible - the draft's own bibliography honestly flags this entry as unverified; (b) the black-box-separation framing ("A resolution in the negative would be a black-box separation, i.e. an oracle relative to which...") appears nowhere - the paper never mentions oracle separations; (c) "nothing at all is known if extractability is dropped" and "the paper's reduction has no substitute" are the drafter's inferences, where the paper says only that satisfactory instantiations remain an open problem and that structured assumptions would be progress (p.7); (d) the parenthetical justifying the 1/2 bound over 1/4 is presented inside a definition attributed to the paper, which states the bound (p.18) with no such explanation. Everything else checks out: Theorem 1's classical impossibility for any f>0 (p.14), the rewinding attack on the single-receiver variant (pp.5, 16), the tag-and-witness-encryption construction and the 2(1-f)n > n argument (p.19), the extractor pulling out >= (1-f)n signatures (p.20), FWE equivalent to extractability obfuscation (p.14), FHAS24 in the AGM and ACL+22 as lattice inspiration (pp.7, 13). All bibliography entries except GGHW14 match the paper's reference list. |
| Self-containment | pass | - | The draft spells out all three primitives, both experiments and the corruption phase in full, so a reader who has never seen the paper knows what object to build and which three properties to prove. The only self-containment defect is cosmetic: hypothesis (ii) points at "Definition 2, item (i)", which is internally resolvable within the draft even though it corresponds to nothing in the paper. |

### Unsupported by the paper

- Citation [GGHW14] and the claim that extractable witness encryption for NP with arbitrary auxiliary input "is generally regarded as implausible": GGHW14 is absent from the paper's bibliography (pp.29-32) and the paper makes no implausibility claim about auxiliary-input extractable WE. (The draft's own bibliography flags the entry as unverified.)
- "A resolution in the negative would be a black-box separation, i.e. an oracle relative to which a one-shot signature scheme and an indistinguishability-secure witness encryption scheme for NP exist but no threshold public-key encryption scheme with one-shot decryption for any f<1/2 does." The paper never discusses oracle or black-box separations anywhere, and the quantifier does not match the negation of Theorem 2 (p.20).
- "[N]othing at all is known if extractability is dropped" and "the paper's reduction has no substitute" (status_note): the paper states only that satisfactory instantiations of post-quantum extractable WE remain open and that weakening to structured assumptions would be progress (p.7).
- Hypothesis (ii)'s cross-reference to an indistinguishability-security notion "(Definition 2, item (i))" as if the paper contained it: the paper's only witness-encryption definition (Definition 6, p.12) is the extractable one, and the phrase "indistinguishability security" appears nowhere in the paper.
- The clause "m_0 != m_1" in the one-shot-signature security experiment, absent from the paper's Definition 5 (p.12) - a necessary repair, but not the paper's text.
- The parenthetical "(The bound 1/2 rather than 1/4 is the right one: the honest committee does decrypt one of the two ciphertexts, so one bit is always learnable.)" presented inside a definition attributed to the paper; the paper gives the 1/2 bound (p.18) with no such rationale.
- Applying the free-of-charge posterior-corruption rule to the security experiment: the paper's Experiment 1 (p.18, lines 10-15) contains no such exemption.

### Corrections the checker asked for

- **formal_statement_latex (scope)** — The draft states the conjecture as the single implication "OSS + indistinguishability-secure WE => threshold one-shot decryption for every f<1/2", and calls this the paper's open question. The paper's question (p.7) is existential and disjunctive: whether extractability can be "weakened or eliminated altogether", either via "more structured or restricted knowledge assumptions" or via "alternative realizations of one-shot decryption without extractability". Plain witness encryption is never named as the replacement, and the paper's weaker reading (structured knowledge assumptions) is dropped.
  - suggested: Pose the conjecture as: for every constant f<1/2 there exists a threshold public-key encryption scheme with one-shot decryption (Definition 10) whose security does not rest on any extractability or knowledge assumption; and record explicitly that the harvester's chosen formalization of the strongest reading is OSS + indistinguishability-secure witness encryption, while the paper also counts weakening extractability to structured or restricted knowledge assumptions (its FHAS24 / ACL+22 examples, p.7) as progress on the same question.
- **formal_statement_latex (final sentence)** — "A resolution in the negative would be a black-box separation, i.e. an oracle relative to which a one-shot signature scheme and an indistinguishability-secure witness encryption scheme for NP exist but no threshold public-key encryption scheme with one-shot decryption for any f<1/2 does." Two faults: the paper never frames the question as a separation (no oracle or black-box discussion anywhere in 35 pages), and the quantifier is wrong - negating "for any f<1/2 there is a scheme" yields "for some f<1/2 there is none".
  - suggested: Delete the sentence. If a negative direction is wanted, write: "a negative resolution would exhibit some f<1/2 for which no such scheme exists under these assumptions (in particular, a black-box separation would suffice)" - and mark it as the harvester's framing, not the paper's.
- **definitions_latex, Definition 2 (witness encryption)** — Item (i), indistinguishability security, is cross-referenced as though it were in the paper. The paper's Definition 6 (p.12) defines only extractable witness encryption; no indistinguishability notion for WE appears anywhere in the paper. Item (ii) also adds |m_0| = |m_1|, which the paper's Definition 6 does not require.
  - suggested: Keep item (i) but label it explicitly as the standard GGSW13 notion supplied by the harvester, noting that the source paper defines only the extractable variant (Definition 6, p.12). Drop the added |m_0| = |m_1| from item (ii), or flag it as a harvester-side restriction.
- **definitions_latex, Definition 1 (one-shot signatures)** — The security experiment includes "m_0 != m_1", which the paper's Definition 5 (p.12) omits, and the message space is fixed to {0,1}^*, where Definition 5 leaves it an abstract M and Algorithm 1 (p.20) signs only tags in {0,1}^lambda.
  - suggested: Keep m_0 != m_1 but state that it repairs Definition 5 as printed (which without the clause is unsatisfiable, since honest KeyGen-then-Sign already yields two verifying pairs) and matches AGKZ20. Replace {0,1}^* with an abstract message space M containing {0,1}^lambda.
- **definitions_latex, Definition 3 (corruption phase)** — One corruption phase is defined for both properties, with posterior corruption free of charge and abort condition |J| + |J''| > fn. The paper's Experiment 1 (p.18, lines 10-15) has no exemption and aborts on |J'| + |J| > fn; Experiment 2 (p.19, lines 13-18) exempts already-decrypted parties but its printed abort test is |J'| + 1 > fn, and its pseudocode delivers nothing at all for an exempted party even though the p.17 prose says the adversary "can corrupt all parties after decryption".
  - suggested: Give the two experiments separate corruption sub-procedures, following Experiment 1 (no exemption, abort if |J'| + |J| > fn) and Experiment 2 respectively, and note in a remark that the paper's Experiment 2 pseudocode is inconsistent with its p.17 prose about what an exempted party hands over.
- **definitions_latex, Definition 3 (closing parenthetical)** — "(The bound 1/2 rather than 1/4 is the right one: the honest committee does decrypt one of the two ciphertexts, so one bit is always learnable.)" is presented as part of a definition attributed to the paper. The paper states the 1/2 bound (Definition 10, p.18; also Definition 9, p.16) with no such justification.
  - suggested: Move it out of the definition into a harvester's remark, or delete it.
- **setting_latex and status_note** — "generally regarded as implausible [GGHW14]" cites a work absent from the paper's bibliography (pp.29-32) for a claim the paper never makes; and "nothing at all is known if extractability is dropped" / "the paper's reduction has no substitute" are inferences attributed to the paper's status.
  - suggested: Drop the GGHW14 sentence or mark it plainly as external context outside the source paper. Replace the status claims with what the paper says: post-quantum extractable witness encryption "is only understood from strong knowledge-type assumptions, and obtaining satisfactory instantiations remains an important open problem" (p.7), and the paper reports no progress toward removing extractability.
- **progress_note** — "builds three proactive secret sharing protocols and a secret-usability extension on top of it (Theorems 3-5)" reads as four artifacts across three theorems; the paper's three protocols are Protocols 1-3, and Protocol 3 (Theorem 5, p.29) IS the secret-usability one. Also unstated: Theorem 3 (p.23) holds for any f<1 (passive), while Theorems 4 and 5 need f<1/2 (active).
  - suggested: "builds three proactive secret sharing protocols (Protocols 1-3, Theorems 3-5, pp.23/26/29), the third of which adds secret usability via functional witness encryption; Theorem 3 tolerates any f<1 against a passive mobile adversary, Theorems 4 and 5 require f<1/2 against an active one."

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `GGHW14` — Sanjam Garg, Craig Gentry, Shai Halevi, and Daniel Wichs, *On the implausibility of differing-inputs obfuscation and extractable witness encryption with auxiliary input*, CRYPTO 2014 (recalled from memory; not cited by the source paper -- verify before use) 2014

## Build

- pdflatex: ok
- chktex: 4 warnings
- lacheck: 0 warnings

## What to check hardest

Check the formalisation hardest. The paper poses one question spanning three routes (structured knowledge assumptions, restricted knowledge assumptions, or eliminating extractability entirely); this statement fixes the last reading and keeps the paper's own two ingredients, one-shot signatures plus witness encryption, dropping only extractability. A reviewer may prefer a version quantified over "any falsifiable assumption", which is harder to state precisely. Second, an implication between primitives can only be refuted by a separation, which I have stated explicitly rather than left implicit. Third, two definitional details: the paper's Experiment 2 as literally printed (page 19, lines 11-19) does not hand the adversary the state of a party whose key has already answered a partial-decryption query, while its prose says "the adversary can corrupt all parties after decryption" -- Definition 3 above follows the prose, which is the notion the application needs; and the paper's Definition 5 security game does not print the condition $m_0 \neq m_1$, which I have added as clearly intended. Finally, I am not aware of any follow-up giving threshold one-shot decryption without extractability, but the one-shot-signature literature is moving fast, and a recent simpler one-shot-signature construction is cited by the paper, so a reviewer should check whether anything has since built one-shot decryption from non-extractable assumptions.

