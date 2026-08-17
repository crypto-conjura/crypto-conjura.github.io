# Provenance: No Key Agreement from Garbling One-Way-Function Circuits

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Limits on the Power of Garbling Techniques for Public-Key Encryption**
- Authors: Sanjam Garg, Mohammad Hajiabadi, Mohammad Mahmoody, Ameer Mohammed
- Venue/archive: Cryptology ePrint Archive 2018
- Identifier: 2018/555
- Bibliographic detail: inferred
- File: `2018-555.pdf` (60 pages)
- sha256: `7f8fff7c9dd0bad9fe63baa71b2af10e5ae526f721ecd6cae383baed9a89d9c7`
- Read on 2026-08-17T18:16:47Z via the `cli` backend

## How the paper leaves it open

`paper-notes-technique-fails`. Settled for round complexity bounded by a constant independent of $\kappa$: the two-message case (equivalent to public-key encryption) is proved in full in the body of the paper, and the paper sketches the extension to $2m$-round key agreement for every constant $m$ in its appendix. Nothing is claimed for round complexity that grows with the security parameter, which is what the conjecture asserts.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 5 | 5 | exact (100%) | Our proof extends to rule out any black-box construction of constant-round key-agreement protocols from OWFs and garbling schemes for oracle-aided circuits. |
| openness | 6 | 6 | exact (100%) | Finally, as noted above, the extension of our results to the key-agreement setting, discussed in Section A only cover the constant-round case. The reason is tha... |
| openness | 46 | 46 | exact (100%) | The reason that our techniques, at least in their current form, do not extend beyond the constant-round (in the context of KE) is that, every time that we compi... |
| progress | 46 | 46 | exact (100%) | In this section, we describe how our main result can in fact extend to m-round key agreement protocols for any constant m. |
| definition | 4 | 4 | exact (100%) | More formally, we will model the above-stated garbling-based non-black-box use of one-way functions as black-box use of garbling mechanisms that can take as inp... |
| definition | 12 | 12 | exact (100%) | A binary-output oracle-aided circuit C is a circuit with Boolean gates as well as oracle gates, and where the output of the circuit is a single bit. The input s... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's own and genuinely open: p. 6 says verbatim \"We leave the extension to general polynomial-round protocols as an interesting future direction,\" nothing in Appendices A or B closes it (Appendix B's extension of [BKSY11] is itself capped at constant-round key exchange, p. 55), and the definitions track Definitions 3.4, 3.6, and A.1 clause by clause. The single substantive error is the formal statement's claim that the constant-round case \"is already a theorem\": the paper proves only the two-message/PKE case (Theorem 4.1), and Appendix A explicitly says it \"sketch[es] the arguments\" for constant-round KE, with the security half deferred entirely to the PKE proof. A secondary unresolved point is that def:bb imports the $\\delta=1/p$ correctness bar from Definition A.1 where the paper's black-box definition (Def. 3.6) writes $(1-2^{-\\kappa})$; the paper calls that WLOG but never states a black-box definition for key agreement, so I cannot settle it from the text.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 6 | The problem is posed by the paper in its own words. §1.3, p. 6: "the extension of our results to the key-agreement setting, discussed in Section A only cover the constant-round case... We leave the extension to general polynomial-round protocols as an interesting future direction." Restated at p. 46 (Appendix A opening): "Going beyon this limitation is an interesting future direction." |
| Openness | pass | 46 | It stays open through the whole paper. Theorem 4.1 (p. 14) covers PKE only; Appendix A (pp. 46-54) contains no theorem for key agreement, only a one-round compilation procedure (§A.2, p. 48) and correctness Lemmas A.4-A.14; Appendix B's extension of [BKSY11] is itself limited to "PKE (and constant-round key exchange protocols)" (p. 55, Theorem B.4). No table, footnote, or later section resolves the polynomial-round case. |
| Strength | pass | 6 | The drafted statement -- no fully black-box construction of key agreement from GC-OWF with no bound on round complexity beyond the polynomial implied by PPT -- is exactly the extension the paper leaves open (p. 6: "general polynomial-round protocols"). It is neither a strengthening (e.g. to garbling circuits containing garbling gates, a separate open problem on p. 5) nor a weakening. |
| Quantifiers and parameters | unclear | 13 | def:garb and def:ka match Definition 3.4 (p. 12) and Definition A.1 (p. 47) symbol for symbol, including "for any polynomial m=m(kappa), any poly-size oracle circuit C with input size m, and any input x" and correctness delta=1/p(kappa), security gamma=negl. But def:bb requires the constructed protocol to be merely "correct" in the sense of Definition A.1 (delta=1/p), whereas the paper's black-box definition (Def. 3.6, p. 13) demands (1 - 1/2^kappa)-correctness, with a remark that this is WLOG by majority-boosting. The paper never states a black-box definition for key agreement, so which bar the conjecture inherits cannot be settled from the text. The draft's choice makes the impossibility formally stronger (it rules out more constructions). |
| Attribution | pass | 6 | This is the harvested paper's own future direction, phrased in the first person: "We leave the extension to general polynomial-round protocols as an interesting future direction" (p. 6). It is not a problem inherited from [IR89], [AS15], or [BKSY11]; the [BKSY11] open problem the paper cites (imperfect completeness, p. 5) is separate and is resolved by this paper in Appendix B. |
| Definitions | pass | 12 | Every notion means what the paper means. Oracle-aided circuit and inpsize match p. 12 verbatim; garbling correctness/security match Definition 3.4 (p. 12); "projective / decomposable" (labels per input bit) is the paper's Remark 3.5 (p. 12) and the p. 4 comparison with [AS15]; "GC-OWF" is the paper's own abbreviation (p. 6); key-agreement correctness and security reproduce Definition A.1 (p. 47) including the 2m-round convention. The draft even carries over the paper's internal Sim(1^\|C\|, m, ...) vs Sim(1^\|C\|, 1^\|x\|, ...) discrepancy between Def. 3.4 and Def. 3.6 rather than silently harmonising it. |
| Fabrication | fail | 46 | formal_statement_latex asserts that constant-round key agreement "is already a theorem." The paper proves only the PKE/two-message case as a theorem (Theorem 4.1, p. 14). For m>2 rounds the paper says on p. 46: "Here we sketch the arguments needed for the extension to the constant-round KE protocols", and §A.3 (p. 49) says only "The proof of security follows almost exactly the same as in the PKE case" -- no theorem is stated. Secondary: setting_latex calls garbling "the most powerful non-black-box technique that requires nothing beyond one-way functions"; the paper says "one of the most powerful classes" (p. 3, and abstract). Everything else checks out: the [IR89]/[BMG09] round-unrestricted attack on "any key exchange" in the ROM is the paper's own footnote 5 (p. 16); the [DG17]/[PRV12] barrier-circumvention claim is p. 4; the Appendix B NIWI claim is p. 55 and Lemma B.8 (p. 59); all eight bibliography entries are printed in the source bibliography (pp. 41-45). |
| Self-containment | pass | - | A reader who has never seen the paper can tell what to prove: definitions_latex supplies def:garb, def:ka, and def:bb in full, the negated form spells out the two failure clauses explicitly, and the round-complexity condition (omega(1) as a function of kappa) is stated. No undefined symbol is left dangling. |

### Unsupported by the paper

- formal_statement_latex: "The special case in which the round complexity is a constant independent of $\kappa$ ... is already a theorem." The paper states no theorem for constant-round key agreement; Appendix A (p. 46) says it "sketch[es] the arguments needed" and §A.3 (p. 49) proves only correctness of one compilation step, deferring security to "follows almost exactly the same as in the PKE case." Only the two-message/PKE case (Theorem 4.1, p. 14) is a theorem.
- setting_latex: garbling described as "the most powerful non-black-box technique that requires nothing beyond one-way functions" (definite superlative); the paper says "one of the most powerful classes of non-black-box techniques" (p. 3).

### Corrections the checker asked for

- **formal_statement_latex** — Claims the constant-round case "is already a theorem." Only the two-message/PKE case is proved as a theorem (Theorem 4.1, p. 14). Constant-round key agreement is asserted in §1.2 (p. 5) and explicitly sketched, not proved, in Appendix A (p. 46: "Here we sketch the arguments needed for the extension to the constant-round KE protocols"; §A.3, p. 49: "The proof of security follows almost exactly the same as in the PKE case"). Appendix A contains no theorem statement. This also contradicts the draft's own status_note.
  - suggested: Replace with: "The two-message case, which is equivalent to public-key encryption, is a theorem of the paper (Theorem 4.1). The paper further asserts, and sketches in its Appendix A, the extension to $2m$-round key agreement for every constant $m$. The content of the conjecture is protocols whose round complexity is $\omega(1)$ as a function of $\kappa$."
- **definitions_latex (Definition~\ref{def:bb}, Correctness clause)** — Requires only that the constructed protocol be "correct" in the sense of Definition~\ref{def:ka}, i.e. $\delta(\kappa)=1/p(\kappa)$. The paper's black-box definition (Definition 3.6, p. 13) sets the bar at $(1-\frac{1}{2^{\kappa}})$-correctness, adding a remark that this is without loss of generality since correctness can be boosted by a fully-black-box hybrid. The paper never restates the black-box definition for key agreement, so the draft's relaxation is a choice it does not flag.
  - suggested: Either raise the bar to match Definition 3.6 -- "$\langle A^{f,L},B^{f,L}\rangle$ is a $(1-\frac{1}{2^{\kappa}})$-correct key-agreement protocol" -- or keep $\delta=1/p$ and add the note: "the paper's Definition 3.6 states this bar as $(1-\frac{1}{2^{\kappa}})$-correctness and remarks that the choice is without loss of generality by correctness boosting."
- **setting_latex** — "the most powerful non-black-box technique that requires nothing beyond one-way functions is Yao's garbled circuits" -- a definite superlative the paper does not make.
  - suggested: "one of the most powerful classes of non-black-box techniques that can be based on one-way functions alone is Yao's garbled circuit technique" (the paper's own phrasing, p. 3).

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 1 warnings

## What to check hardest

The paper poses this as a future direction, not as a numbered conjecture, so the \emph{direction} of the answer --- that the separation does extend to polynomially many rounds --- is the paper's evident expectation but is never asserted by it. A reviewer should be comfortable with that reading before publishing; the alternative framing would be a question rather than a conjecture. Second, the formal statement is a transposition: it mirrors the paper's Definition~3.6 (fully black-box construction of PKE from GC-OWF) with the key-agreement notion of the paper's Appendix~A substituted for the PKE notion. The paper never writes that combined definition out, so the wording here is faithful but not quoted. Third, the paper's own correctness notion for key agreement permits inverse-polynomial disagreement, which is unusually weak; anyone attacking the problem should decide whether they want that or negligible error, and the answer might differ between the two. Fourth, the constant-round case is only sketched in the paper's appendix, so a would-be prover should not assume the constant-round machinery is fully written down anywhere. Finally, I am not aware of any follow-up work that settles the polynomial-round case, but I have not verified this against the post-2018 literature and it should be checked before publication.

