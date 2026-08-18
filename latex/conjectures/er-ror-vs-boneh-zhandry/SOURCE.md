# Provenance: Erasing Real-or-Random Quantum IND-CPA Does Not Imply Boneh-Zhandry Security

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

`paper-conjectures`. The paper proves the reverse direction (the Boneh-Zhandry family does not imply the erasing real-or-random family) and proves that the erasing real-or-random family is strictly weaker than the erasing one-ciphertext family (which does imply Boneh-Zhandry). Whether erasing real-or-random security implies Boneh-Zhandry security is one of the 41 cells the paper's implication table leaves open, and it is one of the six non-implications the paper explicitly conjectures.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 44 | 44 | exact (100%) | Assuming P 4 6=⇒ P 6, since P 4 implies P 5, P 7, P 9, P 10, P 11, P 13, we can conclude that P 5, P 7, P 9, P 10, P 11, P 13 does not imply P 6. |
| openness | 36 | 36 | exact (100%) | The relation between P 4 and P 6 remains open question. |
| progress | 45 | 45 | exact (100%) | (P 4?P 6). To show the implication, we need to simulate ST queries with ER queries that is non-trivial due to no-cloning theorem (as discussed above as well). |
| definition | 6 | 6 | exact (100%) | We conclude that a notion P does not imply Q if there exists an encryption scheme that is secure with respect to the notion P and insecure with respect to the n... |
| parameter | 6 | 6 | exact (100%) | All of non-implications hold on the assumption of the existence of a quantum secure one-way function. |
| definition | 5 | 5 | exact (100%) | Note that this panel includes the security notion from [BZ13b]. |
| openness | 44 | 44 | exact (100%) | In Figure 1, we indicate six non-implications (with red dashed arrows) that if they hold, all the open questions will be resolved by the transitivity. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is real and stays open: Table 1 (p. 6) marks P4?P6 with \"?\", §7.1 says \"The relation between P 4 and P 6 remains open question\" (p. 36), and §9 — the paper's final technical section — still lists (P4?P6) as one of six conjectured non-implications with exactly the no-cloning rationale the draft gives (pp. 44–45); the panel instantiation, the theorem attributions (22, 24, 27, 28, 29), the one-b/one-k game, the fresh-per-query r and π, and every definition all check out symbol by symbol. The single substantive error is that the draft presents the already-proved reverse direction (P6 ⇏ P4) as unqualified, when p. 6 states it is the paper's one separation holding only in the quantum random oracle model, via Theorem 39. That is a status-note defect, precisely repairable, and does not touch the conjectured statement itself.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 36 | The problem is in the paper twice over. §7.1, Panel 4 paragraph (p. 36): "The relation between P 4 and P 6 remains open question." Table 1 (p. 6) carries "?" in row P4, column P6 — verified on the rendered page, not from the text layer. §9 (p. 44) opens "Assuming P 4 6=⇒ P 6, since P 4 implies P 5, P 7, P 9, P 10, P 11, P 13..." |
| Openness — stays open | pass | 44 | Read past the cited passages: §7.2–7.4 separations (pp. 36–43) never treat P4 vs P6; §8's all-notions-secure scheme (p. 44, Thm 44) proves a scheme secure in P1 and P2 and so implies nothing about panel relations; §9 (pp. 44–45) is the last technical section and still counts P4?P6 among the 41 open cells and the six conjectured non-implications. Figure 1 (p. 22) shows it as a red dashed arrow, i.e. unproved. No footnote, appendix, or later table resolves it. |
| Strength | pass | 5 | The paper's conjecture is at panel level (P4 ⇏ P6); the draft instantiates it as learn(*,ER)-chall(*,ER,ror) secure / learn(*,ST)-chall(*,CL,1ct) insecure. Both are listed members of Panel 4 (p. 4) and Panel 6 (p. 5) respectively, and intra-panel notions are proved equivalent (Thms 16, 17, 19), so the instantiation is neither a strengthening nor a weakening. The draft's added hypothesis "quantum-secure one-way functions exist" matches the paper's own blanket convention for non-implications (p. 6) and is needed for the claim to be non-vacuous. |
| Quantifiers and parameters | pass | 10 | Checked symbol by symbol. Def. 7 (p. 10): challenger draws k ← KGen() and one random bit b, both fixed for the whole game, with learning queries interleavable between challenge queries — matches the draft. §3.1 (p. 10): "A fresh randomness will be chosen for each query ... but, for a superposition query, all the messages in the query will be encrypted with the same randomness" — matches. chall(·,ER,ror) (p. 13): U = \|m⟩ ↦ Enc_k(π^b(m);r), π random on {0,1}^n, π^0 = id per the alternative circuit Û^{π^b} then Û^{Enc(·,r)}; Thm 23's proof (p. 34) confirms "each query uses a different random permutation π and uses it only once" — matches the draft's per-query resampling. The draft's negation of security (∃ polynomial p, advantage ≥ 1/p for infinitely many η) is the correct negation of Def. 7's "at most 1/2 + ε for some negligible ε". |
| Attribution | pass | 44 | This is the harvested paper's own open cell in its own Table 1, and its own conjecture: §9 (pp. 44–45) enumerates the six non-implications it argues are "more likely to be true" and gives (P4?P6) as item 3 with its own no-cloning argument. Not borrowed from a cited work — the open questions the paper credits to others ([MS16,GKS20], p. 6) concern P1 vs P2, which the paper resolves. Minor: the paper never uses the word "conjecture"; it says these are "more likely" to hold, so the draft's "explicitly conjectures" is a shade strong but substantively supported. |
| Definitions | pass | 13 | Every notion means what the paper means. ST oracle U_f: \|x,y⟩ ↦ \|x,y⊕f(x)⟩ (p. 8); ER oracle Û^f: \|x⟩ ↦ \|f(x)⟩, defined only for injective f, realizable when f and a left inverse are efficient (§2.1, p. 8, and p. 11 note); ST-learning and ER-learning queries (p. 11); chall(·,CL,1ct) returns Enc_k(m_b;r) for classical m_0,m_1 (p. 11); chall(·,ER,ror) (p. 13); (h,n,n',t,t')-encryption scheme with the draft's exact signatures and correctness (Def. 2, p. 9). Nothing swapped for a standard variant. |
| Fabrication | fail | 6 | The draft states flatly that the paper "proves the reverse direction (the Boneh-Zhandry family does not imply the erasing real-or-random family)" and that "it is already proved that (b) does not imply (a)", and that separations "are all conditional on quantum-secure one-way functions". P6 ⇏ P4 is derived on p. 36 from Theorem 39 (P2 ⇏ P10, p. 40) via P2 ⇒ P6 and P4 ⇒ P10, and p. 6 states: "They all hold in the standard model except the non-implication in the Theorem 39 that holds in the quantum random oracle model." So the reverse direction is the paper's one QROM-only separation; the draft presents it as unqualified. Separately, attributing P4 ⇏ P1 to "Corollary 29" is one transitivity step loose — Cor. 29 (p. 37) states P2, P4 ⇏ P8, and p. 36 derives P4 ⇏ P1 from it via P1 ⇒ P8 (the claim itself is stated outright on p. 6). No other unsupported assertion found: the 41 open cells (p. 44), the six transitively-implied panels P5,P7,P9,P10,P11,P13 (p. 44), Thms 22/24/27/28, the qPRP-from-OWF remark (Remark 5, p. 10; footnote 9, p. 38), and every bibliography entry all check out against the source. |
| Self-containment | pass | 13 | A reader who has never seen the paper could work from the draft alone: the two query models, both challenge types, the l-c-IND-CPA game, the encryption-scheme syntax, and the negation with its quantifiers are all spelled out, and the paper's own definition of non-implication (p. 6) is reproduced. The panel labels P1–P14 appear only as orienting context, not as load-bearing terms in the formal statement. |

### Unsupported by the paper

- The reverse direction P6 ⇏ P4 is asserted as proved with no mention that the paper's proof route (Theorem 39, p. 40) holds only in the quantum random oracle model — explicitly singled out as the one exception on p. 6. Appears in status_note, in informal ("it is already proved that (b) does not imply (a)"), and by omission in setting_latex ("Separations of this kind in the paper are all conditional on quantum-secure one-way functions", which silently drops the QROM half of the same sentence on p. 6).

### Corrections the checker asked for

- **status_note** — "The paper proves the reverse direction (the Boneh-Zhandry family does not imply the erasing real-or-random family)" is presented without qualification. P6 ⇏ P4 is obtained on p. 36 from Theorem 39, and p. 6 flags Theorem 39 as the sole non-implication in the paper that holds only in the quantum random oracle model, not the standard model.
  - suggested: The paper establishes the reverse direction (P6 does not imply P4) in the quantum random oracle model: Theorem 39 shows P2 ⇏ P10 in the QROM, and P6 ⇏ P4 follows since P2 ⇒ P6 and P4 ⇒ P10. This is the paper's only separation that is not in the standard model (p. 6).
- **informal** — "it is already proved that (b) does not imply (a)" omits that the proof is in the quantum random oracle model.
  - suggested: "...and it is already proved, in the quantum random oracle model, that (b) does not imply (a)."
- **setting_latex** — "Separations of this kind in the paper are all conditional on quantum-secure one-way functions" reproduces p. 6's first sentence but drops its second: the paper adds that they all hold in the standard model except Theorem 39, which needs a quantum random oracle.
  - suggested: Add: "All non-implications in the paper assume quantum-secure one-way functions, and all hold in the standard model except Theorem 39, which holds in the quantum random oracle model and is what yields $P6 \not\Rightarrow P4$."
- **progress_note** — "the erasing real-or-random family does not imply the erasing one-ciphertext family (Corollary 29 ...)" attributes P4 ⇏ P1 directly to Corollary 29, which states P2, P4 ⇏ P8 (P8 = learn(*,CL)-chall(1,ER,1ct)).
  - suggested: Corollary 29 (p. 37) states P2, P4 ⇏ P8; the paper then deduces P4 ⇏ P1, P3 on p. 36 because P1, P3 ⇒ P8. The bare claim that Panel 1 is strictly stronger than Panel 4 is also stated outright on p. 6.

## Build

- pdflatex: ok
- chktex: 9 warnings
- lacheck: 0 warnings

## What to check hardest

(1) I supply the hypothesis "assuming quantum-secure one-way functions exist". The paper states this hypothesis for all of its proved separations (page 6) but does not restate it for the six conjectured ones; some assumption is in fact necessary, since if no quantum-secure one-way function exists then no scheme is secure in either notion and the implication holds vacuously. A reviewer should check that this is the intended reading and not a change of strength. (2) The paper is a 2020 ePrint; a later revision or the peer-reviewed version of this work, or follow-up work, may have closed some of these cells. I am not aware of a resolution, but this should be checked against the newest version. (3) Panel membership must be read off Figure 1 and Section 6, not off the boxed lists on pages 4-5: the Panel 11 box on page 5 duplicates the contents of the Panel 10 box, which is plainly a typo. This does not affect the two notions in this conjecture, but it affects panel bookkeeping generally. (4) I have fixed one representative notion from each panel; this is faithful only because the paper proves all notions inside a panel equivalent, so a reviewer should confirm that $\mathrm{learn}(*,ER)$-$\mathrm{chall}(*,ER,\mathrm{ror})$ is in Panel 4 and $\mathrm{learn}(*,ST)$-$\mathrm{chall}(*,CL,1\mathrm{ct})$ is in Panel 6.

