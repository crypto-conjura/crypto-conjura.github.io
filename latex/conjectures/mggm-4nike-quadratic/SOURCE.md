# Provenance: A Four-Party NIKE with Quadratic Security in Maurer's Generic Group Model

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Fine-Grained Non-Interactive Key-Exchange: Constructions and Lower Bounds**
- Authors: Abtin Afshar, Geoffroy Couteau, Mohammad Mahmoody, Elahe Sadeghi
- Venue/archive: Cryptology ePrint Archive 2023
- Identifier: 2023/571
- Bibliographic detail: inferred
- File: `2023-571.pdf` (22 pages)
- sha256: `ebcb0d02a36fe9d72a5603450df06376c658632f3bb693eb31cde7f35803af24`
- Read on 2026-08-17T19:38:01Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Achieved in Shoup's generic group model by the paper itself (Construction 9, Theorem 10). Open in Maurer's generic group model, where the paper's own attack shows a quadratic gap would be the best achievable.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 3 | 3 | exact (100%) | We view as an interesting question the goal of closing the gap between our positive and negative results, either by building a 4-NIKE protocol with quadratic se... |
| openness | 3 | 3 | exact (100%) | In our third contribution, we prove our lower bound in Maurer's generic group model, whereas our positive result holds in Shoup's generic group model, which is ... |
| definition | 1 | 1 | exact (100%) | Maurer's GGM is more limited compared with Shoup's both for the parties and the adversary, as there are no explicit labels for the group elements. Despite being... |
| progress | 5 | 5 | exact (100%) | Furthermore, known generic discrete logarithm algorithms actually run in time square root of the search space when the exponent search space is an interval. The... |
| progress | 1 | 1 | exact (100%) | In particular, we show that there is a 4-party NIKE in Shoup's generic group model with a quadratic gap between the number of queries by the honest parties vs. ... |

## Adversarial check

**Verdict: faithful** (confidence: high)

The most important thing I found is that the check most likely to sink this draft - openness - survives: the paper's only Maurer-model result (Theorem 21 and its corollary, p. 18) is an O(n^2)-query attack, which is exactly compatible with, and does not resolve, the conjectured security against o(n^2)-query adversaries, and the paper poses the 4-NIKE-in-MGGM question on p. 3 after stating that impossibility. The draft's o(1) advantage benchmark is not a self-serving weakening either: it is what the paper's own Shoup-model Theorem 10 actually delivers (O(q^2/lambda^4 + q/lambda^2 + polylog(lambda)/lambda), which is o(1) but not negligible), and the Maurer definitions reproduce Definition 12 and Definition 14 clause for clause including the unusual convention that the key is a group element in the party's own array. All five quotes are verbatim and on the pages claimed, and all eight bibliography entries match the printed reference list; the only quibble is a per-adversary rather than uniform o(1) bound, too thin to change what a proof would have to establish.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 3 | The Discussion paragraph on printed p. 3 poses exactly this: "either by building a 4-NIKE protocol with quadratic security in Maurer's generic group model, or by extending our impossibility result to Shoup's generic group model." The draft's statement quote is verbatim. |
| openness | pass | 18 | The question is posed after both contributions are stated, and nothing later closes it. The paper's only MGGM result is Theorem 21 + corollary (p. 18): an O(n^2)-query eavesdropper breaks any 3-NIKE with alpha,beta,gamma <= n and completeness >= 0.99. That is an O(n^2) attack and leaves o(n^2)-query security untouched. Footnote 5 (p. 3) extends it to all K >= 3 and 5.3 to imperfect correctness; neither resolves it. Remarks 7, 8, 13, 15, 16 and the appendix-free remainder contain no MGGM construction. |
| strength | pass | 13 | "Quadratic security" in the draft's item 3 (advantage o(1) for every q = o(n^2)) is precisely what the paper's own SGGM analogue achieves: Theorem 10 bounds the adversary by O(q^2/lambda^4 + q/lambda^2 + polylog(lambda)/lambda), which for q = o(n^2) is o(1) and not negligible. So the o(1) benchmark is the paper's, not a convenient weakening. The negl completeness-error requirement matches Definition 1's notion of a complete NIKE (p. 8) and Construction 9's actual correctness (p. 13). |
| quantifiers-and-parameters | pass | 15 | Checked clause by clause against Definition 14: gamma, alpha, beta publicly known and fixed in advance; exactly alpha Add and beta Zero queries made after the messages arrive; all parties' arrays over the same Z_p; E's array is 1 followed by the broadcast elements in a canonical order (3gamma for three parties, correctly 4gamma for four); advantage measured as probability >= 1/p + rho. Honest cost Otilde(n) and queries-as-runtime are Definition 2's own conventions (p. 8). Sole looseness: the draft's "every E has advantage rho(lambda) = o(1)" is per-adversary where Theorem 10 gives one uniform bound - formally marginally weaker, not a quantifier flip that changes what must be proved. |
| attribution | pass | 3 | First person and unambiguous - "We view as an interesting question the goal of closing the gap between our positive and negative results" - so this is the harvested paper's own open problem, consistent with openness_kind = paper-states-open. Merkle, Shoup, Maurer, Shanks and Pollard are cited as sources for prior work, not presented as this paper's results. |
| definitions | pass | 15 | The draft's Maurer's-GGM definition reproduces Definition 12 clause for clause (array null except Arr[1] = 1; e the last non-null index; Add writes c1*Arr[i1] + c2*Arr[i2] at e+1 and returns nothing; Equal; Zero over c1..c_e; Write). The paper's "x in Z_q" in the Write query is a typo the draft normalizes to Z_p. The key being a group element in the party's own array, not a bit string, follows Definition 14 and Remark 16 (p. 16) rather than the standard NIKE definition; the extension from three parties to four is demanded by the open question itself. |
| fabrication | pass | 6 | Every assertion traced: group size n^4 and prefix-collision (p. 5); interval discrete log in O(n) via Pollard (p. 5, p. 6 step 3, footnote 6); "more limited for the parties and the adversary" and Diffie-Hellman statable in MGGM (p. 1 abstract, Remark 15, p. 16); Theorem 10's exact bound and Otilde(lambda) honest cost (p. 13); 2K-NIKE / 6-NIKE generalization (p. 3, p. 6). All eight bibliography entries match the printed reference list on pp. 21-22 exactly, including the source's own oddities (Shanks "pages 41-440", "M. Zhandry"). The only claim not stated in so many words is "that generalization also uses labels", which p. 6 supports by saying the generalization applies "the above construction". |
| self-containment | pass | - | Both Maurer's model and the four-party NIKE game are stated in full, including the copy(gamma) mechanics, the completeness condition, and the eavesdropper's winning condition. The formal statement never refers back to the paper, so a reader who has not seen it knows what to prove. |

## Build

- pdflatex: ok
- chktex: 1 warnings
- lacheck: 0 warnings

## What to check hardest

Three things to check. First, resolution: this is a 2023 ePrint and I have not checked the papers citing it; a follow-up may have built the protocol or ruled it out. Second, the formalization of 'quadratic security': I read it as advantage o(1) against every o(n^2)-query eavesdropper, because that is exactly what the paper's own Shoup-model theorem delivers (its bound is dominated by a polylog(lambda)/lambda term and is not negligible). A reviewer who reads 'quadratic security' as negligible advantage would be asking for something stronger than the paper achieves anywhere except the random oracle model, so I did not state it that way. Third, party count: the paper says four parties and the statement says four parties, even though three is the more interesting case; the paper's construction is inherently even-party, since it pairs parties up.

