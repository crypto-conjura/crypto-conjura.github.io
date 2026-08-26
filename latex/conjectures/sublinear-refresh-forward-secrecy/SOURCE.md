# Provenance: Computation-Sublinear Forward-Secure CGKA

Read in-session following `prompts/harvest.md`, since `scripts/harvest_conjectures.py` could not run here (no CLI binary, no SDK, no credentials on this machine); quote grounding and the pdflatex/chktex/lacheck build were still run mechanically, from the script's own `PdfDoc.ground`, `check_candidate`, `compile_check` and `write_source_note`. Nothing here was checked by a human yet; this file is what the run believed and why.

## Source

- Paper: **Fair-Weather No More: Guaranteed Efficiency in Secure Group Messaging**
- Authors: James Bartusek, Nir Bitansky, Yevgeniy Dodis, Rachit Garg, David J. Wu
- Venue/archive: IACR Cryptology ePrint Archive 2026
- Identifier: 2026/1677
- Bibliographic detail: inferred
- File: `2026-1677.pdf` (74 pages)
- sha256: `c500ac6bb6f17148c4095bbc87381317f4c0de08e8a1656def33283b2aa52abf`
- Read on 2026-08-24T21:45:31Z via the `in-session (no CLI binary, no SDK, no credentials on this machine)` backend

## How the paper leaves it open

`paper-states-open`. The paper's own construction (Construction 5.10) is succinct -- its aggregated keys and refresh ciphertext have size poly(λ), independent of |S| -- and is proved secure under the decomposed LWE assumption in the random oracle model, but its UpdPK/UpdSK refresh algorithms take |S| as an explicit input and run in time poly(λ,|S|). Remark 5.7 leaves open, without committing to a specific target rate, whether refresh can instead run in time sublinear in |S|; no construction achieving this, nor any proof that it is impossible, is known.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 6 | 6 | exact (100%) | We leave it as an open problem to achieve a truly (computation-wise!) sublinear CGKA scheme with forward secrecy. |
| openness | 35 | 35 | exact (100%) | An important open problem is to obtain a scheme where the refresh operation requires sublinear running time. An updatable distributed broadcast encryption schem... |
| parameter | 35 | 35 | near (100%) | The refresh algorithms UpdPK and UpdSK take the mapping S as an explicit input, and as such, their running times are allowed to scale with the size of the group... |
| progress | 7 | 7 | exact (100%) | This seems challenging for the scheme we put forward in this paper, and indeed, in Appendix A, we describe a simple attack on a natural variant of our scheme th... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open problem is genuinely posed by the authors (page 6, restated as Remark 5.7 on page 35) and genuinely stays open through the paper's end, including past the Appendix A attack (pages 71-74), which is a negative result on a natural variant rather than a resolution. However, the draft's formal statement sharpens the paper's own vaguer 'sublinear running time' target into a specific 'poly(lambda, log|S|)' bound the paper never states for this question, and it conflates that base open problem with a distinct, strictly stronger variant from footnote 8 (page 7) -- removing S as an explicit input entirely -- which is the variant the Appendix A attack actually targets.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 6 | Found verbatim: 'We leave it as an open problem to achieve a truly (computation-wise!) sublinear CGKA scheme with forward secrecy.' (page 6). Restated formally in Remark 5.7: 'An important open problem is to obtain a scheme where the refresh operation requires sublinear running time.' (page 35). A second, stronger variant of the same question is raised in footnote 8 (page 7): removing S as an explicit input to UpdPK/UpdSK so the algorithms run in poly(lambda). |
| openness | pass | 74 | Read forward through the rest of the paper, including Appendix A (pages 71-74, the paper's final section). Appendix A gives a zeroizing attack on a natural sublinear-time variant of the refresh mechanism (Construction A.1, common shift Delta instead of per-user Delta_i); this is negative evidence, not a resolution. No later section, table, or footnote answers the question. The only other 'future work' items found in the paper (page ~62, active-adversary security) are unrelated to this problem. The open problem stays open through the paper's end. |
| strength | pass-with-caveat | 35 | The core question ('a forward-secure CGKA protocol where computation and communication costs are all sublinear in the size of the group', page 35) matches the draft's core claim at the right strength: same security notion (post-compromise security + forward secrecy, cf. footnote 4 page 4), same construction basis (Construction 5.10, decomposed LWE + random oracle). However, see check 4: the draft silently sharpens 'sublinear' into a specific asymptotic the paper does not commit to for this problem. |
| quantifiers_and_parameters | fail | 35 | The paper's own open-problem statement (Remark 5.7, page 35) asks only for 'sublinear running time' -- it never commits to poly(lambda, log\|S\|) for this specific question. The draft's formal_statement_latex asserts the target is exactly 'poly(lambda, log\|S\|)', which is the paper's general aspirational phrase used elsewhere for communication/aggregate-key size ('short (sublinear, and ideally, polylogarithmic...)', page 6-7) but not the phrase used for the refresh-time open problem itself. Separately, footnote 8 (page 7) poses an EVEN STRONGER, distinct variant: UpdPK/UpdSK dropping S as an input entirely, running in poly(lambda) with no dependence on \|S\| whatsoever (not even a log factor) -- and it is specifically THIS stronger variant, not the plain 'sublinear' open problem, that Appendix A's attack (Construction A.1, pages 72-74) targets. The draft's 'Equivalently' clause conflates these two distinct grades of the question into one statement, and its use of the Appendix A attack as 'partial evidence of difficulty' for the general sublinear-refresh question is really evidence about the harder, footnote-8 variant. |
| attribution | pass | 35 | This is the paper's own open problem about its own construction (Construction 5.10), not a problem it merely cites from elsewhere. RTreeKEM/ACDT20 is cited only as the prior (linear-communication) forward-secure CGKA scheme being improved upon (page 5), not as the source of this open problem. |
| definitions | pass | 35 | Definition 5.6 (Succinctness, page 35) requires apk, ask, the pk/sk output by UpdSK, and each pk_j in the refreshed mapping S' to be poly(lambda); Definitions 5.8/5.9 (pages 35-36) give exactly the static/adaptive security games with key-generation, corruption, and Add/Remove/Refresh update queries the draft describes. No notion has been silently swapped for a nonstandard one; the draft's summary omits mentioning individual pk/sk succinctness explicitly but does not contradict it. |
| fabrication | pass (one item flagged separately under quantifiers) | - | Bibliography keys checked against the paper's own reference list: ACDT20 appears at page 68 ('Joel Alwen, Sandro Coretti, Yevgeniy Dodis, and Yiannis Tselekounis...'); AMR25 appears at page 69 ('Damiano Abram, Giulio Malavolta, and Lawrence Roy...'). Both are genuinely printed-in-source-bibliography, not fabricated. The status_note's claims (Construction 5.10, decomposed LWE, random oracle model, refresh is the only linear-time operation) all check out against pages 5-7 and 35-39. The only unsupported-by-the-paper assertion found is the specific 'poly(lambda, log\|S\|)' target discussed under quantifiers. |
| self_containment | unclear | - | formal_statement_latex uses UpdPK, UpdSK, apk, ask, S as if already defined, without inlining their syntax; the record provided to me has no separate notation_latex/definitions_latex fields to check them against, so I cannot confirm the full record is self-contained -- only that the definitions I could check (Definition 5.6, 5.8, 5.9) are represented faithfully where referenced. |

### Corrections the checker asked for

- **(see reason)** — In formal_statement_latex, replace the specific target 'poly(lambda, log|S|)' for UpdPK/UpdSK running time with the paper's own (looser) phrasing: the open problem is whether refresh can run in time sublinear in |S| -- the paper (Remark 5.7, page 35, and page 6) never commits to a polylogarithmic bound for this question, only to 'sublinear'.
  - suggested: applied, per this note
- **(see reason)** — Separate the two grades of the open problem instead of merging them with 'Equivalently': (i) the base question (pages 6, 35) of making UpdPK/UpdSK run in sublinear (unspecified) time while still taking S as input, and (ii) the strictly stronger question raised only in footnote 8 (page 7) of removing S as an input entirely so the algorithms run in poly(lambda) independent of |S|. The zeroizing attack in Appendix A (pages 72-74) is evidence of difficulty specifically for (ii), not directly for (i); the status_note and formal statement should not present it as evidence against the general sublinear-refresh question without this distinction.
  - suggested: applied, per this note

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

A reviewer should keep the two grades of this question distinct: (i) Remark 5.7's plain request for sublinear (rate unspecified) refresh time while still taking S as input, which is what this statement asks, and (ii) Footnote 8's strictly stronger request to drop S as an input entirely and run in poly(λ), which is the variant Appendix A's zeroizing attack actually targets. A reviewer should also check whether some other lattice or algebraic technique (beyond the decomposed-LWE matrix-commitment approach used here) might achieve sublinear refresh time for (i) without needing a fundamentally new primitive, and since this is a very recent paper (2026), should search for contemporaneous follow-up work that may already bear on this question.

