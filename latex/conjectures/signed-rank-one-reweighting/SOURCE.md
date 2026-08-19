# Provenance: Signed Low-Entropy Reweightings to Rank One on the Sphere

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Quantum entanglement, sum of squares, and the log rank conjecture**
- Authors: Boaz Barak, Pravesh K. Kothari, David Steurer
- Venue/archive: arXiv preprint (quant-ph), dated July 11, 2017; v2 submitted 9 Jul 2017 2017
- Identifier: arXiv:1701.06321v2 [quant-ph]
- Bibliographic detail: printed-on-page
- File: `1701.06321v2.pdf` (25 pages)
- sha256: `86e9ffb81edc99fcd7814139743b277020279e7013c54fe7eb78af53395db9db`
- Read on 2026-08-19T15:30:30Z via the `cli` backend

## How the paper leaves it open

`paper-asks-question`. Settled for delta >= 1/2, by the paper's own Theorem 2.3, even with the stronger requirement that r be nonnegative. Open for every delta < 1/2; the paper additionally states that the nonnegative-r version of the question is false, so a positive answer must use cancellation.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 21 | 21 | exact (100%) | Question 8.1. Is it the case that for every distribution µ over Sn−1 and every ε, δ > 0 there is a (not necessarily positive) function r : Sn−1 → R such that Ev... |
| openness | 21 | 21 | exact (100%) | There do seem to be natural such statements that could imply improved algorithmic results. In particular, we believe resolving the following two questions could... |
| progress | 21 | 21 | exact (100%) | A positive solution for Question 8.1 for any δ < 1/2 would be very interesting. |
| progress | 21 | 21 | exact (100%) | We do know that the answer to this question is No if one does not allow negative reweighting functions. |
| progress | 8 | 8 | exact (100%) | It can be shown that as stated, Theorem 2.3 is tight. However there are different notions of being "close to rank one" that could be useful in both the log-rank... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Question 8.1 is genuinely the authors' own, and it genuinely stays open: the word \"negative\" occurs exactly once in the whole paper, in the Q8.1 discussion, and the appendices contain only the Theorem 5.3 proof, the real-complex reduction and a higher-rank structure theorem, so nothing resolves the signed case -- the paper resolves only the nonnegative variant that the question explicitly excludes. The formal statement, the entropy-cost definition, the quantifier structure (including the C(eps,delta) reading of O(n^delta), which is the only coherent one), and the delta >= 1/2 status via Theorem 2.3 all check out against the paper. The one substantive defect is that the informal turns the paper's hedged \"It may(8) improve the best known bound for the log rank conjecture to O~(n^delta)\" into \"would improve\", attributing to the authors a claim their footnotes 7 and 8 exist specifically to qualify; two smaller prose over-claims (that brute force was the only prior algorithm for general measurements, and that Theorem 2.3 is \"exactly\" the sphere instance) are correctable in the same way.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 21 | Question 8.1 appears verbatim in Section 8 ("Conclusions and further directions") on PDF p. 21 (printed p. 19). Every clause of the draft's formal statement is present in it: E\|r(v)\|=1, E\|r(v)\|log\|r(v)\| <= O(n^delta), r explicitly "(not necessarily positive)", a nonzero rank one L, and \|\|E[r(v)vv^T] - L\|\|_F <= eps\|\|L\|\|_F. The draft's page citations are PDF pages (PDF page = printed page + 2) and are correct. |
| Openness | pass | 21 | Section 8 is the final section; the paper's only later material is Appendix A (proof of Theorem 5.3), Appendix B (real-to-complex BSS reduction) and Appendix C (higher-rank structure theorem, PDF pp. 23-25), none of which touches signed reweightings. A full-text search shows the word "negative" occurs exactly once in the entire paper, on PDF p. 21, in the sentence "We do know that the answer to this question is No if one does not allow negative reweighting functions" -- i.e. the paper resolves only the nonnegative variant, which Question 8.1 explicitly excludes. Nothing in the paper resolves Question 8.1, and the authors' own "A positive solution for Question 8.1 for any delta < 1/2 would be very interesting" confirms it is left open. |
| Strength | pass | 21 | Clause-by-clause the drafted statement is the paper's, neither strengthened nor weakened: same normalisation E\|r\|=1, same entropy bound, same conclusion with a nonzero rank one L and the relative Frobenius bound eps\|\|L\|\|_F (not \|\|E[...]\|\|_F, which would be a different statement). The draft's move from the paper's "every distribution" to "every Borel probability measure" is a formalisation choice, not a change of content: the paper's own Definition 2.2 context is finitely supported, and a uniform-constant answer for finitely supported mu transfers to Borel mu by weak-* approximation. |
| Quantifiers and parameters | pass | 21 | Paper: "for every distribution mu over S^{n-1} and every eps, delta > 0 there is ... r ... <= O(n^delta)". Draft: "for every eps>0 and delta>0 there exists C(eps,delta) ... for every n and every mu ... there exist r ...". The draft makes the implicit O(.) constant explicit and uniform in n and mu. This is the only coherent reading: the paper's Preliminaries (PDF p. 10) say O(.) hides "absolute multiplicative constants", but an eps- and delta-independent constant would make the delta -> 0 case read "cost <= C", trivially false, contradicting the authors' statement that a positive answer for any delta < 1/2 would be interesting; and Theorem 2.3's own bound is sqrt(n)*poly(1/eps), so eps-dependence of the constant is clearly intended. Uniformity in mu is forced because mu lives on S^{n-1} and the bound is asymptotic in n. |
| Attribution | pass | 21 | This is the harvested paper's own question, not one it cites to someone else: "we believe resolving the following two questions could help in making such progress: Question 8.1 ...". The draft correctly attributes it to the authors (openness_kind "paper-asks-question") and correctly attributes the surrounding prior work to others -- Lovett [Lov14] for the sqrt(n) communication bound, Rothvoss [Rot14] for the proof followed, Lovasz-Saks [LS88] for the log rank conjecture, Nisan-Wigderson [NW94] for the rectangle equivalence, Gavinsky-Lovett [GL14] for the footnote-7 caveat. All six bibliography entries were checked against the paper's reference list (PDF pp. 22-23) and match, including Rot14 = CoRR abs/1409.6366. |
| Definitions | pass | 7 | The draft's Definition 1 ("signed reweighting with entropy cost at most K": E\|r\|=1 and E[\|r\| log\|r\|] <= K) is exactly the pair of conditions in Question 8.1, not a substitute. Its remark that for nonnegative r the cost equals the KL divergence matches the paper's Definition 2.2 on PDF p. 7 ("k-deficient reweighting ... Delta_KL(mu'\|\|mu) = E_{X~mu'} log(mu'(X)/mu(X))"); writing this as a density ratio dmu'/dmu is renaming, not redefinition. "Rank one", Frobenius norm (paper's footnote 3, PDF p. 4) and S^{n-1} (PDF p. 10) all agree with the paper. |
| Fabrication | fail | 21 | The informal says the authors "point out that a positive answer below the square-root threshold WOULD improve the best known upper bound on the communication complexity of low rank Boolean matrices". The paper (PDF p. 21) says "It may(8) improve the best known bound for the log rank conjecture to O~(n^delta)", where footnote 8 warns that this "might require better control of the dependence of the bound on eps than we need for our setting" and footnote 7 (PDF p. 8, Gavinsky-Lovett) warns the notion of "approximate" matters. The draft asserts the unhedged version and attributes it to the authors. Second unsupported assertion, in setting_latex: "Until this paper the only algorithm for general measurements was brute force, taking 2^{O(n)} time" -- the paper claims only to be "the first for this problem that beats the brute force bound of 2^{O(n)} time for general measurements" (PDF p. 5); DPS04's sos algorithm (PDF p. 4) does apply to general measurements, it is just not known to beat brute force. Everything else I checked in the setting, status and progress notes is supported: the tightness remark (PDF p. 8), the No-for-nonnegative remark, Theorem 2.4's exp(-sqrt(n) poly(1/eps))N principal submatrix (PDF p. 8), Theorem 5.1's degree-O~(sqrt(n)) reweighting (PDF p. 12), the unlikeliness of a black-box log-rank reduction (PDF p. 21), and that the paper reports no partial result for signed r at any delta < 1/2. |
| Self-containment | pass | - | Judged from the draft alone, not the paper. A reader who has never seen the paper can tell what to prove: the notation block fixes n, S^{n-1}, the Frobenius norm, rank one, the convention 0 log 0 := 0, and the roles of eps and delta; Definition 1 supplies the entropy cost the formal statement invokes; the parameters list records that C may not depend on n or mu. The formal statement's cross-reference "in the sense of Definition~1" resolves to the draft's own definitions block. |

### Unsupported by the paper

- informal (PDF p. 21): a positive answer "would improve the best known upper bound on the communication complexity of low rank Boolean matrices". The paper says "may improve", and footnotes 7 and 8 give the reasons for the hedge. The draft attributes the unhedged claim to the authors.

### Corrections the checker asked for

- **informal** — States that a positive answer "would improve the best known upper bound on the communication complexity of low rank Boolean matrices", attributing an unhedged claim to the authors. The paper writes "It may(8) improve the best known bound for the log rank conjecture to O~(n^delta)", and footnote 8 explicitly warns the improvement might require better control of the eps-dependence than the paper's own setting needs (with footnote 7 adding the Gavinsky-Lovett caveat that the notion of "approximate" matters). The draft's own setting_latex records both footnotes, so the informal contradicts its own setting.
  - suggested: The authors note that a positive answer below the square-root threshold may improve the best known bound for the log rank conjecture to O~(n^delta) -- subject to the caveats of their footnotes 7 and 8 about which notion of "approximate" is needed and how the bound depends on eps -- and that, if appropriately extended to pseudo-distributions, it would improve their algorithm's running time to exp(O~(n^delta)).
- **setting_latex** — "Until this paper the only algorithm for general measurements was brute force, taking $2^{O(n)}$ time." The paper claims only priority in beating brute force, not that no other algorithm existed: "To our knowledge, this algorithm is the first for this problem that beats the brute force bound of $2^{O(n)}$ time for general measurements" (PDF p. 5). Doherty-Parrilo-Spedalieri's sos-based algorithm (PDF p. 4) applies to general measurements; it is simply not known to run in quasi-polynomial time, and Brandao-Christandl-Yard's quasi-polynomial guarantee holds only for 1-LOCC measurements.
  - suggested: This is the first algorithm for the problem that beats the brute-force $2^{O(n)}$ bound for general measurements; the earlier sos-based algorithm of Doherty, Parrilo and Spedalieri applies to general measurements but is not known to beat brute force, and Brand\~ao--Christandl--Yard's quasi-polynomial guarantee is restricted to 1-LOCC measurements.
- **setting_latex** — "In the setting of honest probability distributions this is exactly the $\delta = 1/2$, nonnegative-$r$ instance of the statement above." Theorem 2.3 (PDF p. 7) is stated for an arbitrary distribution over rank one $n \times n$ matrices $X$, with conclusion about $\tilde{\mathbb{E}}_{\mu'} X$; the drafted statement is about distributions on $\mathbb{S}^{n-1}$ and $\mathbb{E}[r(v) vv^\top]$. The sphere statement is the specialisation $X = vv^\top$, not the same statement. (The implication runs in the direction the draft needs, so the status_note and progress_note conclusions stand.)
  - suggested: In the setting of honest probability distributions, Theorem~2.3 specialises, on taking $X = vv^{\top}$, to the $\delta = 1/2$, nonnegative-$r$ instance of the statement above.

## Build

- pdflatex: ok
- chktex: 4 warnings
- lacheck: 1 warnings

## What to check hardest

Three things a reviewer should check hardest. (i) Quantifier placement on the constant: the paper writes the entropy bound as O(n^delta), which by convention hides a constant that may depend on epsilon and delta but not on n or mu; I have made that constant explicit as C(epsilon, delta). Footnote 8 of the paper explicitly warns that for the log rank application one needs better control of the epsilon-dependence than the paper's own setting requires, so a solver should track C's dependence on epsilon rather than treat it as free. (ii) Regularity: the paper says only 'distribution over S^{n-1}' and does not specify measurability or integrability conditions on r; I have written Borel measurable and mu-integrable. The essential case is finitely supported mu (this is what the sum-of-squares application produces), and the general case should follow by approximation, but this is my reading and not the paper's words. (iii) Currency: the paper's assertion that the nonnegative-r answer is No is stated without proof, resting on the remark that Theorem 2.3 is tight as stated. And I am recalling from memory, not from the paper, that Lovett's O~(sqrt(n)) remains the best known bound for the log rank conjecture and that Question 8.1 has not been answered for delta < 1/2; the log rank literature has moved since 2017 and a reviewer should verify both before publishing. I am not aware of any resolution, but I am not certain.

