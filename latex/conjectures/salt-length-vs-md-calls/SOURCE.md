# Provenance: Salt Length vs. Merkle-Damgård Call Count in Random Oracle Combiners

Read in-session following `prompts/harvest.md`, since `scripts/harvest_conjectures.py` could not run here (no CLI binary, no SDK, no credentials on this machine); quote grounding and the pdflatex/chktex/lacheck build were still run mechanically, from the script's own `PdfDoc.ground`, `check_candidate`, `compile_check` and `write_source_note`. Nothing here was checked by a human yet; this file is what the run believed and why.

## Source

- Paper: **Random Oracle Combiners: Merkle-Damgård Style**
- Authors: Yevgeniy Dodis, Eli Goldin, Peter Hall
- Venue/archive: Cryptology ePrint Archive 2025
- Identifier: ePrint 2025/609
- Bibliographic detail: inferred
- File: `2025-609.pdf` (32 pages)
- sha256: `f67575c8d0f10f8009dc129ca54a136199228d7d6ee6d35d548d19d348dcdb53`
- Read on 2026-08-24T21:45:26Z via the `in-session (no CLI binary, no SDK, no credentials on this machine)` backend

## How the paper leaves it open

`paper-states-open`. Settled only in one regime: this paper's Theorem 3.1 gives a secure combiner whenever |Z1|,|Z2| > |M|+lambda, at the cost of the number of Merkle-Damgard calls growing with |M|. Whether (a) short, message-independent salts and (b) a constant number of calls can hold simultaneously, or are provably incompatible, is left open.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 27 | 27 | near (94%) | Is there a secure random oracle combiner that (a) has O(λ) length salts and (b) makes a constant number of calls to h∗ 1 and h∗ 2 , independent of message lengt... |
| openness | 27 | 27 | near (97%) | This leaves the following main open problem: Is there a secure random oracle combiner that (a) has O(λ) length salts and (b) makes a constant number of calls to... |
| progress | 27 | 27 | near (100%) | The main remaining inefficiency comes from the requirements on the salt lengths Z1 and Z2; each of them must be longer than the message M of the combiner. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The open problem is quoted essentially verbatim from page 27 (independently located and re-checked, not taken on the draft's citation alone), remains open through the end of the paper including the appendix, and the draft's formal statement, parameter bounds (|Z|>|M|+λ from Theorem 3.1), and status note all check out against the text without strengthening, weakening, or misattributing anything. On the required distinctness question: this general existence/trade-off conjecture is a genuinely different mathematical claim from the paper's adjacent question about whether its own specific construction C-tilde stays secure under short salts -- the paper itself treats a positive answer to the latter as merely one possible witness for the former, not as the same statement.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 27 | Page 27 (Section 4, 'Conclusion and Open Problems') contains a paragraph headed 'Open Problems' that reads verbatim: 'Is there a secure random oracle combiner that (a) has O(λ) length salts and (b) makes a constant number of calls to h∗_1 and h∗_2, independent of message length? Conversely, show that such a combiner satisfying (a)+(b) cannot exist; in this case, it would be great to find the trade-off in salt length vs. number of “Merkle-Damgård-calls.”' This is exactly the question the draft states, and the draft's own page citation (27) is correct -- verified independently from the extracted PDF text, not taken on trust. |
| Openness | pass | 32 | Section 4 is the paper's final section before the reference list (which starts on the printed page immediately after, page 28 in this PDF's numbering). Nothing after the Open Problems paragraph revisits it: the appendix (pages 30-32, 'Hard Hybrid') consists solely of Lemma A.1 / Theorem A.1 / Corollary A.2, which are auxiliary lemmas supporting the proof of the main Theorem 3.1 stated earlier in the body, not a resolution of the salt-length/call-count trade-off. No table of results, footnote, or later remark closes the question. It stays open through the end of the paper. |
| Strength | pass | 27 | The draft's formal statement -- existence of a secure ROC with \|Z1\|,\|Z2\| = O(λ) independent of \|M\| and O(1) calls to h1*, h2* independent of \|M\|, plus the converse impossibility/trade-off question -- reproduces the paper's (a)+(b) conjunction and its 'conversely, show ... cannot exist ... find the trade-off' clause without strengthening or weakening either side. It does not silently drop the disjunctive/either-or structure (existence vs. impossibility-with-trade-off) that the paper itself poses. |
| Quantifiers and parameters | pass | 27 | Definition 2.5 (page 12, 'Definition 3.3 from [12]') defines a ROC C_Z^{h1,h2}: {0,1}^m -> {0,1}^n as (Tg,T1,T2,TSim,ε)-indifferentiable for all oracle circuits g^O with ≤ Tg queries; the draft's formal statement correctly imports this exact definition by reference ('secure per the paper's indifferentiability-based definition') rather than restating a weaker or stronger one. The draft's O(λ)-salt / O(1)-calls conditions, both stated as independent of m=\|M\|, match the paper's own asymptotic phrasing layered on top of that definition. Theorem 3.1 (page 12) confirms the contrasting regime: message length ℓδ, salt length kδ with k>ℓ, and the informal Theorem 1.1 (page 5) states the bound \|Z1\|=\|Z2\|>\|M\|+λ used in the draft's status_note -- this matches exactly. |
| Attribution | pass | 27 | The Open Problems paragraph on page 27 is authored by this paper (2025-609, Dodis/Goldin/Hall) and is not attributed there to any cited work; the paper's earlier remark 'we resolved the main open problem of [12]' (page 27, preceding paragraph) refers to a *different*, already-resolved question (security of the Eq. 2 combiner), not to the new open problem. The draft's bibliography entry ('DFGHP23', reference [12] on page 28: Dodis, Ferguson, Goldin, Hall, Pietrzak, CRYPTO 2023) is listed only as background/context for the ROC line of work, and the draft does not claim [12] itself poses this open problem -- so no misattribution occurs. |
| Definitions | pass | 12 | The draft's use of 'random oracle combiner,' 'salt' (Z1,Z2), and 'h1*, h2*' (Merkle-Damgård extension) match Definition 2.5 (page 12) and Definition 2.6 (page 12, Merkle-Damgård Transform) exactly; no standard notion has been silently swapped in. On the required second judgment: read on its own, the draft's general question ('does a secure ROC with message-independent salts and O(1) calls exist at all, or what's the best trade-off') is a distinct mathematical question from the paper's adjacent, narrower question about its own specific construction C-tilde ('is C-tilde secure once \|Zi\| shrinks below \|M\|+λ, or can it be attacked'). The general question quantifies over the entire space of ROC constructions of this MD-based salted-XOR shape and asks for existence/impossibility/trade-off; the specific question is about one already-fixed object's behavior outside the regime where its proof applies. The paper itself flags they are not equivalent -- it explicitly notes 'it is possible our construction C-tilde provides a solution to this main open problem' (page 27), i.e. the specific question's answer would only resolve the general one in the positive direction, and even then only by exhibiting a witness, not by settling the universal claim in general. The two are related (a positive answer to the specific question is one route to a positive answer to the general one) but not the same question worded twice. |
| Fabrication | pass | 27 | Checked status_note against the paper: 'Theorem 3.1 gives a secure combiner whenever \|Z1\|,\|Z2\| > \|M\|+λ' matches Theorem 1.1 (page 5, informal restatement of Theorem 3.1) verbatim in substance. 'at the cost of the number of Merkle-Damgård calls growing with \|M\|' is supported by Theorem 3.1's own parametrization (page 12: input length (ℓ+k)δ with k>ℓ, so the total number of h1*/h2* calls is Θ(ℓ+k), which grows with the message-block count ℓ) and by footnote 4 (page 5). No parameter, bound, or claim in the draft was found unsupported by the text. |
| Self-containment | pass | 27 | A reader unfamiliar with the paper can reconstruct the question from the draft's informal statement, formal_statement_latex, and status_note together: the combiner shape (salted XOR of two MD-extended oracles), the security notion (deferred to 'the paper's indifferentiability-based definition,' named rather than silently redefined), and the exact open question (existence vs. impossibility+trade-off) are all present. The one soft spot is that the formal statement does not inline Definition 2.5's (Tg,T1,T2,TSim,ε) game -- but naming rather than re-deriving a complex indifferentiability definition is standard practice for this kind of harvested entry and does not by itself make the statement non-self-contained, since the quotes field supplies the paper's own wording as a check. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

A reviewer should check that 'independent of message length' is read as asymptotics in |M| specifically (holding lambda's own dependence separate), matching the paper's own phrasing, rather than folding both parameters together. Also worth checking whether any follow-up work since April 2025 has already resolved this.

