# Provenance: One Erasing Challenge Query Does Not Buy Security Against Many Embedding Learning Queries

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

`paper-conjectures`. The paper proves that the notion with a single erasing two-ciphertext challenge query implies four other panels, and separates it from two more, but leaves its relation to six panels open, among them the family with many embedding-model superposition learning queries and classical challenge queries. That non-implication is one of the six the paper explicitly conjectures, and by the paper's own bookkeeping it is the one whose resolution would settle the largest number of the remaining open cells.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 44 | 44 | exact (100%) | Assuming P 3 6=⇒ P 11, since P 3 =⇒ P 7, P 8, P 9, P 13, we can obtain P 7, P 8, P 9, P 13 6=⇒ P 11. |
| openness | 36 | 36 | exact (100%) | The relationships between P 3 and P 1, P 4, P 5, P 6, P 10, P 11 remain open questions. |
| progress | 45 | 45 | exact (100%) | The notions in P 11 have many quantum learning queries but P 3, have classical learning queries and only one quantum challenge query. It is unlikely that a redu... |
| definition | 6 | 6 | exact (100%) | We conclude that a notion P does not imply Q if there exists an encryption scheme that is secure with respect to the notion P and insecure with respect to the n... |
| parameter | 6 | 6 | exact (100%) | All of non-implications hold on the assumption of the existence of a quantum secure one-way function. |
| openness | 6 | 6 | exact (100%) | The cells with question marks remain open problems. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is real, is the paper's own conjecture (Section 9, item 4, p. 44-45), and stays open through the final section; the formal statement matches the paper clause by clause, including the (ER,2ct) isometry's per-ciphertext randomness and the correct negation of the security bound. The single most important thing I found is that the draft correctly resisted a typesetting trap: the Panel 11 box printed on p. 5 duplicates Panel 10's erasing-learning entries, and had the draft trusted it the whole conjecture would have collapsed into P10 — but Figure 1 (p. 22), the panel-equivalence list (p. 24), and Theorem 33 confirm P11 is the embedding-learning family the draft used. What fails is the surrounding bookkeeping: the status note says P3 implies four other panels where p. 36 says five, and the progress note's enumeration shows the fifth (P13) was simply dropped, along with a conflation of the paper's two established non-implications into one.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 44 | Section 9 lists six conjectured non-implications; item 4 is "(P3?P11). The notions in P11 have many quantum learning queries but P3, have classical learning queries and only one quantum challenge query." Table 1 (p. 6) carries a question mark at row P3, column P11, and Figure 1 (p. 22) draws it as a red dashed arrow. |
| Openness | pass | 36 | Section 7.1, Panel 3: "The relationships between P3 and P1, P4, P5, P6, P10, P11 remain open questions." Nothing later closes it — Section 8 (p. 44) constructs a scheme secure in all notions (irrelevant to separations), and Section 9 (p. 44), the final section, still lists P3?P11 as open. Read past the citation: Theorems 33, 34, 39, 40, 41, 42 and Corollary 29 are the only P11-related separations and none has P3 as its source. |
| Strength | pass | 22 | Paper conjectures P3 ⇏ P11 with the p. 6 convention that P ⇏ Q means a scheme secure for P and insecure for Q. Draft instantiates P3 as its unique member learn(*,CL)-chall(1,ER,2ct) (p. 22) and P11 as learn(*,EM)-chall(*,CL,1ct), a member of the six proved equivalent (p. 24). Neither strengthened nor weakened; picking one P11 member is legitimate since all six are equivalent. |
| Quantifiers and parameters | pass | 13 | Checked symbol by symbol. (ER,2ct) on p. 13 is U_{ER,2ct,r0\|\|r1,b}: \|m0,m1> -> \|Enc_k(m_b;r0),Enc_k(m_bbar;r1)> with r0,r1 <- {0,1}^t fresh — the draft's isometry is identical, including which randomness goes with which ciphertext. Learning queries polynomially many, challenge queries c_nb in {1,*} (p. 14, sec. 3.3). Fresh r per query but one r shared across a superposition (p. 10). Win probability <= 1/2 + eps for some negligible eps (Def. 7, p. 10); the draft's negation (exists polynomial p, at least 1/2 + 1/p for infinitely many eta) is the correct dual. Interleaving allowed (Def. 7, p. 10). Quantum-secure OWF assumption matches the paper's blanket convention for non-implications (p. 6). |
| Attribution | pass | 44 | This is the harvested paper's own conjecture, not a cited one: Section 9 says "In Figure 1, we indicate six non-implications (with red dashed arrows) that if they hold, all the open questions will be resolved" and then argues why each is likely, including (P3?P11). The draft's openness_kind "paper-conjectures" is correct. Cited works (BDJR97, BZ13b, GHS16, MS16, KKVB02, Zha16, Sim97) appear in the draft only as background, and each is in the paper's bibliography (pp. 45-47). |
| Definitions | pass | 11 | CL-learning, EM-learning (challenger supplies \|0>^{n'} output register, both registers returned), (CL,1ct) and (ER,2ct) challenge all match pp. 11 and 13. (h,n,n',t,t')-encryption scheme matches Definition 2 (p. 9); U_f and hat-U^g match p. 7 and sec. 2.1 (p. 8). Note a trap the draft correctly avoided: the Panel 11 box printed on p. 5 is a typesetting error duplicating Panel 10's learn(*,ER)-chall(.,CL,.) entries, but Figure 1 (p. 22), the six-notion equivalence list (p. 24), and Theorem 33 all give Panel 11 as learn(*,EM)-chall(c_nb,CL,c_rt). The draft used the correct definition. |
| Fabrication | fail | 36 | status_note says P3 "implies four other panels"; p. 36 states "P3 ==> P7, P8, P9, P13, P14" — five. The progress_note's "Established around the cell" list shows the loss: it names P8 (single erasing 1ct), P9 (single erasing ror), P7 (single embedding 2ct) and P14 (fully classical), omitting P13 = learn(*,CL)-chall(1,EM,ror). Same sentence describes the established non-implications as "the standard-query real-or-random family" (singular) where p. 36 gives two, P3 ⇏ P2 and P3 ⇏ P12. Separately, progress_note calls the Theorem-18-route-is-blocked argument "the paper's stated reason"; the paper's stated reason (p. 45) is only that one quantum query cannot simulate many, and it never invokes Theorem 18 there. Everything else asserted (Thm 18 statement, Thm 19, one-challenge-per-learning-query cost, Simon's-algorithm construction technique, panel memberships, 57 notions / 14 panels, 120 -> 72 variants) checks out against pp. 3-6, 22, 24, 27-29, 38. |
| Self-containment | pass | - | The formal statement, notation and definitions together fix the scheme syntax, both query types used, the game, the win condition and the assumption, so a reader who has never opened the paper knows exactly what object to build and what two properties to prove. The learn/chall notation is introduced rather than assumed. |

### Unsupported by the paper

- status_note: "implies four other panels" — the paper (p. 36) states P3 ==> P7, P8, P9, P13, P14, five panels.
- progress_note: the list of established implications from P3 silently omits P13 = learn(*,CL)-chall(1,EM,ror) (p. 36).
- progress_note: "it does not imply the standard-query real-or-random family" understates the paper, which establishes P3 ⇏ P2 and P3 ⇏ P12 (p. 36).
- progress_note: "it is the paper's stated reason for believing the non-implication" applied to the Theorem 18 argument — the paper's reason on p. 45 makes no reference to Theorem 18.
- status_note/informal: the comparative ranking ("the one whose resolution would settle the largest number of the remaining open cells", "would close more of the paper's open cases than any of the other separations it conjectures") is never stated by the paper. It is arithmetic the draft performed on the Section 9 bookkeeping (p. 44), and it happens to be correct — P3 ⇏ P11 directly yields nine further cells versus at most five for each of the other five conjectures — so this is unsupported-as-quoted rather than false.

### Corrections the checker asked for

- **status_note** — Says the single erasing two-ciphertext notion "implies four other panels." Page 36 states P3 ==> P7, P8, P9, P13, P14 — five panels. The draft's own progress_note enumerates only four because it drops P13.
  - suggested: "The paper proves that the notion with a single erasing two-ciphertext challenge query implies five other panels (P7, P8, P9, P13, P14), and separates it from two more (P2 and P12), but leaves its relation to six panels open..."
- **progress_note** — The "Established around the cell" list omits P3 ==> P13 = learn(*,CL)-chall(1,EM,ror), the single embedding real-or-random notion (p. 36).
  - suggested: "...the single erasing two-ciphertext notion implies the single erasing one-ciphertext notion, the single erasing real-or-random notion, the single embedding two-ciphertext notion, the single embedding real-or-random notion, and the fully classical notions..."
- **progress_note** — "it does not imply the standard-query real-or-random family" describes one panel where the paper establishes two non-implications: P3 ⇏ P2 (the ST real-or-random family) and P3 ⇏ P12 (the singleton learn(*,CL)-chall(1,ST,ror)), both on p. 36.
  - suggested: "...it does not imply either standard-query real-or-random notion: neither the family P2 nor the singleton learn(*,CL)-chall(1,ST,ror)."
- **progress_note** — Attributes the "Theorem 18's route is closed when only one challenge query is available" argument to the paper as its "stated reason." The paper's stated reason (p. 45, item 4) is only that a reduction is unlikely to simulate many quantum queries with one; it does not mention Theorem 18 in that discussion.
  - suggested: Attribute the Theorem 18 connection to the draft's own reading, e.g. "...which is why the single-challenge-query restriction looks like the crux; the paper's own stated reason (p. 45) is simply that a reduction adversary is unlikely to simulate many quantum queries with only one."

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

(1) Panel identification needs care: the boxed list of Panel 11 on page 5 of the paper erroneously repeats the contents of Panel 10 (erasing learning queries) instead of the embedding learning queries; Figure 1 on page 22 and the Panel 11 equivalence derivations on page 24 make clear that Panel 11 is the family with $EM$ learning queries and classical challenge queries, and I have followed those. A reviewer should confirm this reading, since the conjecture is stated with a representative member of that panel. (2) As with the paper's proved separations, I supply the hypothesis that quantum-secure one-way functions exist; without some such assumption no scheme is secure in either notion and the implication holds vacuously. The paper states this hypothesis for its proved separations but not explicitly for the conjectured ones. (3) The paper is a 2020 ePrint; a later version of this work or follow-up work may have closed this cell, and I have not verified against the newest version. (4) The paper's account of why the implication is hard is short — one sentence about simulating many quantum queries with one — so a reviewer may judge the recorded obstruction thinner than for the other separations; the substantive evidence is that the paper's own simulation theorem provably needs many challenge queries.

