# Provenance: Security of the Merkle-Damgård Combiner Under Constant-Length Salts

Read in-session following `prompts/harvest.md`, since `scripts/harvest_conjectures.py` could not run here (no CLI binary, no SDK, no credentials on this machine); quote grounding and the pdflatex/chktex/lacheck build were still run mechanically, from the script's own `PdfDoc.ground`, `check_candidate`, `compile_check` and `write_source_note`. Nothing here was checked by a human yet; this file is what the run believed and why.

## Source

- Paper: **Random Oracle Combiners: Merkle-Damgård Style**
- Authors: Yevgeniy Dodis, Eli Goldin, Peter Hall
- Venue/archive: Cryptology ePrint Archive 2025
- Identifier: ePrint 2025/609
- Bibliographic detail: inferred
- File: `2025-609.pdf` (32 pages)
- sha256: `f67575c8d0f10f8009dc129ca54a136199228d7d6ee6d35d548d19d348dcdb53`
- Read on 2026-08-24T21:45:28Z via the `in-session (no CLI binary, no SDK, no credentials on this machine)` backend

## How the paper leaves it open

`paper-asks-question`. Open in both directions: the paper proves security only for |Z1|,|Z2| > |M|+lambda; it explicitly states it has no attack once the salts are a constant number of blocks, but it also has no proof of security in that regime. (The paper's own phrasing of the insecurity alternative ranges over the whole sub-threshold regime |Zi| ≤ |M|, while the security-proof alternative is narrowed explicitly to the constant-blocks case; resolving the constant-blocks question either way would not by itself settle the paper's broader-phrased alternative for every |Zi| in between.)

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 27 | 27 | near (97%) | Thus, it would be very interesting to either show that C is insecure unless \|Zi\| > \|M\|, or find a supporting proof of security for much shorter salts (ideal... |
| openness | 27 | 27 | near (99%) | we do not have any attacks against this construction, once the \|Zi\| is a constant number of blocks, independent of \|M\| |
| progress | 27 | 27 | near (100%) | In particular, it is possible our construction C provides a solution to this main open problem! |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: 0.78)

The problem is genuinely posed by the paper on page 27 and stays open through the end of the paper (the only later material is Appendix A, a proof detail for the already-claimed Theorem 3.1); all three quotes are verbatim from that page modulo a tilde-rendering artifact in the PDF's text layer. The draft is faithful in substance and correctly kept as a candidate distinct from the paragraph's other, more general open question, but it understates its own premise in the informal paragraph (dropping the '+lambda' margin that both the theorem and the draft's own formal statement require) and silently symmetrizes the paper's asymmetric two-sided open question into a single constant-blocks-only dichotomy -- both are fixable without touching the core mathematics, which is why this is faithful-with-corrections rather than faithful outright.

| check | result | page | finding |
| --- | --- | --- | --- |
| 1. Existence | pass | 27 | Section 4 ('Conclusion and Open Problems'), final paragraph, contains exactly this discussion: 'While our analysis of C~ critically uses the fact that \|Zi\| > \|M\| + lambda, we do not have any attacks against this construction, once the \|Zi\| is a constant number of blocks, independent of \|M\|. In particular, it is possible our construction C~ provides a solution to this main open problem! Thus, it would be very interesting to either show that C~ is insecure unless \|Zi\| > \|M\|, or find a supporting proof of security for much shorter salts (ideally, constant number of blocks).' The problem is genuinely posed by the paper, on page 27, in exactly this location. |
| 2. Openness | pass | 27 | Page 27 is the last page of running text before the bibliography (pp. 28-29) and Appendix A (pp. 30-32), which contains only the deferred proof of a hybrid lemma for Theorem 3.1 (an internal step of the already-claimed Theorem 3.1, not a new result about short salts). Nothing after page 27 revisits or resolves the short-salt question, so it stays open through the end of the paper. |
| 3. Strength | unclear | 27 | The draft's dichotomy is symmetric: both '(i) attack at O(1) blocks' and '(ii) security at O(1) blocks' are pinned to the constant-block extreme. The paper's own alternative is asymmetric: the insecurity direction is phrased more broadly as 'C~ is insecure unless \|Zi\| > \|M\|' (i.e., for the whole range \|Zi\| <= \|M\|, not just the constant-block extreme), while only the security-proof direction is explicitly narrowed to 'ideally, constant number of blocks.' The draft's narrowing of the attack side specifically to O(1) blocks is well supported by the adjacent sentence 'we do not have any attacks... once the \|Zi\| is a constant number of blocks, independent of \|M\|,' so it is defensible as capturing the sub-case that is genuinely open in both directions, but it is a tightening/reformulation of the paper's literal 'unless \|Zi\| > \|M\|' phrasing, not a verbatim restatement of the paper's own dichotomy. |
| 4. Quantifiers and parameters | fail | 27 | The 'informal' field states the theorem holds 'as long as each salt is strictly longer than the message being hashed,' omitting the security-parameter margin. Both Theorem 3.1 (page 13: requires k > l blocks with error term including 2^{-(k-l)*delta}) and the conclusion's own gloss on page 27 ('critically uses the fact that \|Zi\| > \|M\| + lambda') make clear the requirement is not mere strict inequality but an excess of at least lambda bits. The formal_statement_latex correctly includes '+lambda', so the informal paragraph is internally inconsistent with the draft's own formal statement and understates what the proof needs. |
| 5. Attribution | pass | 27 | This is the paper's own open problem about its own construction C~, not a question inherited from Dodis et al. [12] (whose open problem -- existence of any length-preserving ROC -- this paper says it resolved in the affirmative, per the abstract and page 1). No misattribution found. |
| 6. Definitions / merge-split | pass | 27 | C~, h*, Merkle-Damgard extension, and the ROC/indifferentiability notions used match the paper's own Definition 2.6 (MD transform, page 12) and Theorem 3.1 (page 13). On the merge/split question specifically: this candidate, read alone, is a genuinely distinct question from the general existence question posed in the same paragraph ('Is there a secure random oracle combiner that (a) has O(lambda) length salts and (b) makes a constant number of calls... independent of message length?'). The general question ranges over all possible ROC constructions; this candidate is restricted to whether the paper's specific construction C~ is secure or breakable at constant-block salts. The two are related in only one direction -- a proof that C~ is secure at constant blocks would resolve the general question affirmatively (the paper says as much: 'it is possible our construction C~ provides a solution to this main open problem!') -- but an attack on C~ at constant blocks would not resolve the general question (some other combiner might still achieve (a)+(b)), and a general impossibility proof for all combiners would not by itself pin down whether C~ specifically breaks at constant blocks vs. some other threshold. So this is one question stated by the paper, not the same question worded twice, and treating them as two separate candidates rather than merging is correct. |
| 7. Fabrication | pass | 27 | No invented facts found. All three quotes match the PDF text on page 27 verbatim (mod a font-rendering artifact where the tilde diacritic over 'C' is emitted by the text layer as a stray 'e' before or after the letter -- e.g. the source renders as '...C e is insecure...' -- which the draft's quotes correctly normalize away rather than fabricate). status_note and progress-quote are directly supported. bibliography is empty, so nothing is fabricated there. |
| 8. Self-containment | pass | 27 | A reader who knows what a random-oracle combiner and indifferentiability mean, plus the Merkle-Damgard-extension notation f* (Definition 2.6, page 12), can read informal + formal_statement_latex and know exactly what construction and what parameter regime is in question. Full symbol definitions (h1*, xor, Zi) are not spelled out in this JSON but that is expected to be supplied in the downstream notation/definitions section, not in this verify-stage record. |

### Corrections the checker asked for

- **(see reason)** — In 'informal', replace 'as long as each salt is strictly longer than the message being hashed' with wording that preserves the security-parameter margin, e.g. 'as long as each salt is longer than the message being hashed by at least the security parameter' -- the bare 'strictly longer' is inconsistent with both Theorem 3.1's actual requirement and the draft's own (correct) formal_statement_latex, which uses |Zi| > |M| + lambda.
  - suggested: applied, per this note
- **(see reason)** — Consider noting, in status_note or formal_statement_latex, that the paper's own phrasing of the 'insecure' alternative ('show that C~ is insecure unless |Zi| > |M|') is stated over the whole sub-threshold range |Zi| <= |M|, not only the constant-blocks extreme; the draft's option (i) narrows this to O(1) blocks specifically. This narrowing is defensible (it targets exactly the regime the paper says has no known attack), but a precise reading should flag that resolving (i) as stated would not by itself establish the paper's broader-phrased alternative for all |Zi| in (|M|/2, |M|), say.
  - suggested: applied, per this note

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

This question is closely tied to, and would partially settle, the paper's other stated open problem about the existence of an O(lambda)-salt, O(1)-call combiner in general; a reviewer should judge whether the two are best kept as separate pages or noted as related. The quoted sentences refer to the construction by a tilde-decorated symbol (C with a tilde); a reviewer should double check that this diacritic survives the mechanical text-layer match, since it is exactly the kind of typographic decoration most likely to be mis-extracted.

