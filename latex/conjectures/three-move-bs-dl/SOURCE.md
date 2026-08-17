# Provenance: Three-Move Pairing-Free Blind Signatures from Discrete Log

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Playing Tag with Okamoto-Schnorr: Three-Move Pairing-Free Blind Signatures from DDH**
- Authors: Rutchathon Chairattana-Apirom, Michael Reichle, Stefano Tessaro
- Venue/archive: IACR Cryptology ePrint Archive; full version of an article to appear at CRYPTO 2026 2026
- Identifier: 2026/571
- Bibliographic detail: inferred
- File: `2026-571.pdf` (58 pages)
- sha256: `5e7a009af09c34b1ff92a9f0060a10fd40610ee074f649ce203585301d72f887`
- Read on 2026-08-17T02:28:59Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Settled: three moves plus DL, but only in AGM+ROM; three moves plus DDH in the ROM alone (this paper, and concurrently Chen); four moves plus DL in the ROM alone (Klooss-Lai-Reichle); two moves is impossible for schemes black-box in the group (Dietz-Kastner-Tessaro). Open: three moves, black-box in the group, ROM only, DL only.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 8 | 8 | exact (100%) | We still rely on the DDH assumption for our security analysis; the “dream result” in the field is a three-move blind signature from DL. |
| openness | 8 | 8 | exact (100%) | It remains unclear how to reconcile our techniques and the techniques from [KR25] into a three-move blind signature from DL. We briefly discuss the challenges a... |
| progress | 8 | 8 | exact (100%) | Our construction relies on an algebraic MAC and a linearly-homomorphic extractable commitment. Both primitives are well-known to exist from DDH. It is unclear h... |
| progress | 8 | 8 | exact (100%) | This paper shows that it is possible to construct three-move blind signatures in pairing-free groups in the ROM alone, resolving a major open problem in the fie... |
| definition | 3 | 3 | exact (100%) | This class of constructions captures exactly those constructions that make black-box use of the underlying group—these are generally more efficient. |
| definition | 3 | 3 | exact (100%) | Recently, Dietz et al. [DKT26] established that a large class of constructions that can be described in a combination of the generic group model (GGM) [Sho97, M... |
| definition | 4 | 4 | exact (100%) | We stress that one can obtain three- (or even two-) move pairing-free constructions fairly generically by using Fischlin’s construction [Fis06], in conjunction ... |
| parameter | 4 | 4 | exact (100%) | We present constructions with full OMUF (i.e., there is no limit on the number of concurrent signing sessions) that make black-box use of the group. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely in the paper and genuinely left open: p. 8 names 'a three-move blind signature from DL' as the field's dream result and leaves it for future work, and nothing in the remaining fifty pages -- all of whose security results are under DDH -- touches it. The most important defect is a quantifier error: the draft conditions only one-more unforgeability on DL and asserts blindness unconditionally over all pairing-free group generators, which is strictly stronger than what the paper poses and would exclude a scheme whose blindness reduces to DL, as the paper's own compact instantiation's does to DDH. Two smaller repairs follow: correctness is silently weakened from the paper's perfect notion (Def. 2.3, p. 10), and the progress note wrongly credits the 15G+22Zp instantiation with statistical blindness when Table 1 assigns that to the larger 21G+35Zp scheme.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 8 | Section 1.2 (Related and Future Work) states verbatim: "We still rely on the DDH assumption for our security analysis; the 'dream result' in the field is a three-move blind signature from DL." The problem the draft describes is in the paper. |
| Openness | pass | 8 | "It remains unclear how to reconcile our techniques and the techniques from [KR25] into a three-move blind signature from DL. We briefly discuss the challenges and leave the problem for future work." A grep of the full 58-page text layer for 'dream', 'open problem', 'future work' and 'three-move blind signature from DL' returns hits only in the abstract and on p. 8; nothing later revisits it. Every security result in the paper is under DDH (Thm 3.5 p. 20, Cor. 4.2 p. 23, Cor. 4.4 p. 25), so the DL question is not answered anywhere in the paper, appendices included. |
| Strength | pass | 4 | The paper's phrase is the bare 'a three-move blind signature from DL'. The draft adds black-box use of the group, ROM-only, and full (unbounded-concurrency) OMUF. These are supported by context, not invented: Table 1's caption (p. 4) scopes the whole comparison to 'constructions with full OMUF (i.e., there is no limit on the number of concurrent signing sessions) that make black-box use of the group', and the black-box clause is necessary rather than a strengthening -- p. 4 notes that Fischlin's paradigm with non-black-box group use already yields two- or three-move ROM schemes from a one-way function alone [CMV26], which DL implies, so without the black-box restriction the 'dream result' would be trivially settled. |
| Quantifiers and parameters | fail | 8 | The formal statement scopes all three clauses under 'for every pairing-free group generator GGen', but conditions only clause 3 (OMUF) on the DL assumption; clause 2 (Blindness) is asserted unconditionally, i.e. it must hold even for generators where discrete log is easy. The paper's dream result is 'a three-move blind signature from DL', which permits blindness to be proved from DL -- indeed the paper's own compact instantiation (Cor. 4.2, p. 23) is only computationally partially blind under DDH. As written the draft is strictly stronger than what the paper poses. |
| Attribution | pass | 8 | The paper describes it as the 'dream result' in the field (a community goal, which the draft's setting_latex reproduces as such) and explicitly leaves it as its own future work in Section 1.2. The draft's openness_kind 'paper-states-open' is correct and does not misattribute a third party's problem to this paper. |
| Definitions | fail | 10 | The paper's Definition 2.3 requires *perfect* correctness ('A partially blind signature BS is (perfectly) correct if for all public parameters ... it holds that BS.Ver(...) = 1'), and Theorem 3.4 (p. 20) proves the scheme perfectly correct. The draft's def:corr silently weakens this to correctness up to negligible error. The other load-bearing notions check out: the three-move syntax matches BS.Setup/KeyGen/Sign1/U1/Sign2/U2/Ver (p. 9) with info dropped for the non-partially-blind case; def:omuf's k >= l+1 with distinct messages matches Fig. 1's winning condition (p. 10); def:blind matches Fig. 2 including the (bot,bot) rule (p. 11); DL matches Definition 2.1 (p. 9); and def:bb is a fair formalization of the paper's 'black-box use of the underlying group' as the GGM-describable class (p. 3). |
| Fabrication | fail | 4 | The progress_note asserts the paper achieves 'statistical blindness -- but under DDH, with signatures of 15 group elements plus 22 scalars'. Table 1 (p. 4) and Corollaries 4.2 (p. 23) and 4.4 (p. 25) contradict this: the 15G+22Zp scheme is Section 4.1 and is only *computationally* partially blind; statistical blindness is Section 4.2 and costs 21G+35Zp. Communication is 17G+14Zp for both, as the draft says. Everything else I spot-checked is supported: the [KLR25]=four-move-DL / [KR25]=four-move-DDH split (Table 1 and p. 8), CTZ-3 [CATZ24] four-move CDH, the three-move AGM+ROM row [Abe01/KLX22b, TZ22, CKM+23] all from DL, DKT26's >=3-move lower bound (p. 3), Chen's concurrent one-time-signature + EMBS route (p. 9), both named obstructions (p. 8), PS00's polylog bound (p. 5), and all sixteen bibliography entries against the paper's reference list (pp. 51-54). |
| Self-containment | pass | - | The statement ships its own definitions of three-move blind signature syntax, correctness, blindness, one-more unforgeability, black-box group use, and the DL advantage, plus a notation block fixing lambda, GGen, (G,p,G), H and negligibility. A reader who has never opened the paper would know what has to be constructed and what has to be proved. |

### Unsupported by the paper

- progress_note: 'statistical blindness ... with signatures of 15 group elements plus 22 scalars' -- the paper does not support this pairing. Table 1 (p. 4) and Corollaries 4.2 (p. 23) / 4.4 (p. 25) assign 15G+22Zp to the computationally blind Section 4.1 instantiation and statistical blindness to the 21G+35Zp Section 4.2 instantiation.

### Corrections the checker asked for

- **formal_statement_latex, clause 2 (Blindness)** — Blindness is asserted to hold for every pairing-free group generator with no computational hypothesis at all, while clause 3 is conditioned on DL. This demands blindness even relative to generators where discrete log is easy, which is stronger than the paper's 'three-move blind signature from DL' -- the paper's own compact instantiation (Cor. 4.2, p. 23) proves blindness only computationally, under DDH.
  - suggested: Condition clause 2 on the same hypothesis as clause 3: 'If the discrete logarithm assumption holds relative to GGen, then for every PPT adversary A with access to H, Adv^blind_{BS[GGen]}(A, lambda) is negligible in lambda.' (Optionally note that the paper's Section 4.2 instantiation achieves statistical blindness, so the unconditional variant is not vacuous -- but it is not what the paper poses.)
- **definitions_latex, Definition def:corr (Correctness)** — Allows correctness to fail with negligible probability. The paper's Definition 2.3 (p. 10) requires perfect correctness, and Theorem 3.4 (p. 20) establishes exactly that for BS_alg.
  - suggested: Require Ver(pp, pk, mu, sigma) = 1 with probability 1 over the coins of the four algorithms and over H, matching Definition 2.3 of the paper; or state explicitly that the conjecture deliberately relaxes the paper's perfect-correctness requirement.
- **progress_note** — Attributes statistical blindness and a signature size of 15 group elements plus 22 scalars to one and the same scheme. Table 1 (p. 4) and Corollaries 4.2 (p. 23) and 4.4 (p. 25) separate them: Section 4.1 gives 15G+22Zp with computational partial blindness; Section 4.2 gives statistical partial blindness at 21G+35Zp.
  - suggested: '... full (unbounded-concurrency) one-more strong unforgeability under DDH, in two instantiations: Section 4.1 with computational blindness and signatures of 15 group elements plus 22 scalars, and Section 4.2 with statistical blindness and signatures of 21 group elements plus 35 scalars; communication is 17 group elements plus 14 scalars in both.'

## Build

- pdflatex: ok
- chktex: 7 warnings
- lacheck: 1 warnings

## What to check hardest

(1) The ``black-box use of the group'' clause in the formal statement is my formalisation, read off the paper's framing rather than copied from a definition it states. It is necessary: without it the statement is already settled, since Fischlin's paradigm with generic NIZKs and non-black-box use of the group gives two-move schemes in the ROM from a one-way function alone [CMV26], which DL implies. The paper's Table 1 caption restricts attention to schemes that ``make black-box use of the group'', and it invokes [DKT26] for the claim that its own round complexity is optimal precisely because it ``only makes generic use of the underlying group''. A reviewer should check that Definition 5 is a faithful and workable rendering; competing formalisations (algebraic algorithms, Maurer-style generic algorithms with or without an equality oracle or a random-element oracle) differ at the margins and one of them could conceivably make the question easier or harder. (2) The sentence I use as the openness quote writes ``[KR25]'' where the surrounding text and Table 1 attribute the four-move DL scheme to ``[KLR25]''; this appears to be a typo in the paper and does not affect the statement. (3) I state item (iii) asymptotically rather than as a concrete reduction, on purpose: the paper's own DDH proof loses a cube root in the DL term of its NonceColl case, so demanding a linear-loss reduction would be strictly stronger than what ``from DL'' means in this literature. (4) This is a very fast-moving area -- the reference list contains five works dated 2025 or 2026, two of them ``to appear at CRYPTO 2026'' -- so it is possible that a three-move DL construction has appeared since. I found no such claim in this paper, and the concurrent work of Chen also stops at DDH. (5) Refutation would require an impossibility result for three-move group-black-box schemes under DL, which is a different kind of object from a construction; the conjecture is stated positively because that is the direction the paper points, but a reviewer may prefer a neutral ``decide'' phrasing.

