# Provenance: Black-Box Uselessness of One-Way Functions for Key Agreement

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Black-Box Uselessness: Composing Separations in Cryptography**
- Authors: Geoffroy Couteau, Pooya Farshim, Mohammad Mahmoody
- Venue/archive: Cryptology ePrint Archive 2021
- Identifier: 2021/016
- Bibliographic detail: inferred
- File: `2021-016.pdf` (37 pages)
- sha256: `1e26d5d117922336451b0d29c368ba48cb6a9e9b0e78b7683b4c75230e36576f`
- Read on 2026-08-17T19:17:35Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Settled for three restricted classes: perfectly correct key agreement where one party makes a constant number of one-way-function queries (Theorem 4.1); imperfect key agreement that is constant-round with both parties making a constant number of one-way-function queries (Theorem 4.9); and Merkle-type protocols where all one-way-function queries precede all messages, with no query bound (Theorem 4.12). The general case, with arbitrary rounds and arbitrary polynomial query counts, is open and is named by the paper as its central open problem.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 13 | 13 | exact (100%) | The “dream result” here would be to show that one-way functions are black-box useless for any key agreement. Unfortunately, we do not know how to prove this res... |
| openness | 8 | 8 | exact (100%) | The central open problem left by our work is that of black-box uselessness of OWFs for arbitrary key agreement protocols. Given our BBU results for special clas... |
| openness | 13 | 13 | exact (100%) | We leave the proof of black-box uselessness of OWFs for general key-agreement protocols as an intriguing open question. |
| progress | 13 | 13 | exact (100%) | It only applies to constructions where one of the parties makes a constant number of queries to the io-OWF oracle, which we call unbalanced key agreement. Note ... |
| progress | 6 | 6 | exact (100%) | This in particular implies that the recursive argument above can be applied for only a constant number of steps. |
| progress | 20 | 20 | exact (100%) | However, this technique requires the attacker with lower adaptivity to simulate in “its head” the original attacker which cannot be done efficiently if the prot... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely posed by this paper in the authors' own voice and genuinely stays open through the end (abstract p. 1, p. 6, p. 11, reaffirmed at p. 18), and the three restricted theorems, the named obstruction, the six quotes and all ten bibliography entries are reported accurately. The one substantive failure is that the formal statement asserts the io-variant — io-OWFs are BBU for io-KA — whereas Remark 4.2 on p. 11 says outright that \"A is BBU for C\" is strictly stronger than \"io-A is BBU for io-C\", so the drafted statement is a weakening of the conjecture the paper actually makes, and it contradicts the draft's own title, one_line, informal and setting_latex, all of which say plain one-way functions. Combined with the invented ε ≥ 1/poly constraint on key-agreement correctness, which Definition 2.7 (p. 8) does not contain, this is repairable from the paper: state it for F and KA, and drop the bound on ε.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 11 | The problem is posed in the paper, repeatedly and in the authors' own voice. Abstract (p. 1): "We conjecture that OWFs are indeed black-box useless for general key agreement protocols." Section 4 opening (p. 11): "We leave the proof of black-box uselessness of OWFs for general key-agreement protocols as an intriguing open question." Immediately after Theorem 4.1 (p. 11): "The 'dream result' here would be to show that one-way functions are black-box useless for any key agreement. Unfortunately, we do not know how to prove this result." The three restricted results the draft cites are real and correctly numbered: Theorem 4.1 (p. 11), Theorem 4.9 (p. 17), Theorem 4.12 (p. 19). One paper-side wrinkle the draft handled correctly: Theorem 4.9's statement literally reads "perfect key agreement", but the section title (p. 17), the proof, and the closing sentence (p. 18, "constant-query constant-round constructions of imperfect key agreement") all say imperfect; the draft's reading as imperfect is right. |
| openness | pass | 18 | Read past the cited passages. Sections 5 (compiling out, pp. 21-26) and 6 (helpfulness for CRHFs, pp. 26-31) concern different targets and do not touch OWFs-for-KA. The last word on the topic, at the end of Section 4.2 (p. 18), reaffirms it: "We leave as the main open problem of our work the question of showing that (infinitely-often) OWFs are black-box useless for more general forms of key agreement." There are no appendices and no results table that closes it. It stays open through the end of the paper. |
| strength | fail | 11 | The drafted statement is a weakening of the conjecture the paper poses. The paper's conjecture is about plain OWFs and plain KA (abstract p. 1; "arbitrary key agreement protocols" p. 6; "one-way functions are black-box useless for any key agreement" p. 11). The draft's formal_statement_latex instead asserts io-F is BBU for io-KA. Remark 4.2 (p. 11) states explicitly: "it is easy to show that the statement 'A is BBU for C' is stronger than (i.e., implies) the statement 'io-A is BBU for io-C' for all notions of black-box uselessness." So proving the drafted statement would not establish the paper's conjecture. The io-reading is licensed by the parenthetical on p. 18 but is the weaker variant, and the draft is internally inconsistent about it: its title, one_line and informal all say plain "one-way functions", and its own setting_latex correctly reports Theorem 4.12 as a plain-OWF result (p. 19 explains the io- caveat is dropped there because the inverter is used only once). The choice of the [semi -> forall-exists-semi] flavor, by contrast, is a fair extrapolation from Theorems 4.1 and 4.9 and I do not fault it. |
| quantifiers-and-parameters | fail | 8 | Quantifier orders are correct throughout: the draft's semi- vs forall-exists-semi split matches Definition 2.3 (p. 7) symbol for symbol, the uselessness quantification (for every auxiliary Z, semi-reduction to (Q,Z) implies forall-exists-semi-reduction to Z alone) matches Definition 3.2 plus Remark 3.4 (pp. 9-10), and the io- quantifiers in both primitive definitions match Definitions 2.6 and 2.7 (p. 8). One parameter is wrong: the draft's io-KA definition and its parameters list require the correctness function to satisfy epsilon(lambda) >= 1/p(lambda). Definition 2.7 (p. 8) imposes no lower bound on epsilon at all; the 1/poly(lambda) condition appears only in Definition 2.8 for approximate-correct IO (p. 9). Since a smaller epsilon makes KA easier to build and uselessness for it harder to prove, this silently narrows the conjecture. |
| attribution | pass | 6 | This is the harvested paper's own open problem, not one it credits elsewhere. Page 6, "Open problems": "The central open problem left by our work is that of black-box uselessness of OWFs for arbitrary key agreement protocols." Page 18: "the main open problem of our work." The BBU framework itself is introduced by this paper (Definition 1.1, p. 2; Definition 3.2, p. 9). The prior work the draft cites is correctly attributed outward: IR89 for the original separation (p. 3), RTV04 for the reduction notions (p. 7), BKSY11/IR89/BM09/BM17 for the samplers (pp. 13, 17), MMV11 for the adaptivity technique (p. 18). |
| definitions | pass | 9 | Cryptographic primitive (Definition 2.1, p. 7), joint primitive (Definition 3.1, p. 9), semi- and forall-exists-semi-black-box reduction (Definition 2.3, p. 7), and [semi -> forall-exists-semi] black-box uselessness (Definition 3.2 with the primitive-set taken to be all primitives, plus Remark 3.4, pp. 9-10) all match the paper in substance; the draft renames the paper's (T, y_A, y_B) to (T, K_A, K_B), which is renaming, not redefining. Merkle-type is described as Definition 4.11 does (p. 19) — all OWF queries before any message, queries to Z unrestricted — not as the looser "one-round" phrasing of the abstract. Two things the draft supplies that the paper does not: the explicit implementation sets and breaking relations for io-F and io-KA are the draft's own reconstruction, and "implementations are all functions F" should be all oracle-aided PPT machines. |
| fabrication | fail | 8 | Three unsupported items. (1) The epsilon(lambda) >= 1/p(lambda) constraint on key-agreement correctness, asserted in definitions_latex, formal_statement_latex and parameters, is not in Definition 2.7 (p. 8). (2) The primitive-level breaking relations for io-F and io-KA are reconstructed, not stated in the paper. (3) status_note presents the io-version as "named by the paper as its central open problem"; the passage that uses the words "central open problem" (p. 6) names plain OWFs and arbitrary KA. Everything else checks out: the O(n^2) -> O(n^4) blow-up example is verbatim from p. 4; the Yao82 hardness-amplification and IL89/BHT14 distributional-inverter attributions match Lemma 4.6 (p. 15) and Lemma 4.10 (p. 18); the MMV11 obstruction matches p. 18; the composition claim matches Theorem 3.5 (p. 10); the IR89 random-oracle-plus-PSPACE description matches p. 3. All ten bibliography entries match the paper's reference list (pp. 31-35) in authors, title, venue, pages and year. |
| self-containment | pass | - | A reader who has never opened the paper could tell what to prove. Every notion the formal statement uses is defined in the draft: primitive, joint primitive, semi- and forall-exists-semi-black-box reduction, black-box uselessness, io-OWF, io-KA. The only gap is that the corrections above must be applied first, since as written the statement's target (io-KA with epsilon bounded below by an inverse polynomial) is not the paper's target. |

### Unsupported by the paper

- That an $\varepsilon$-key agreement requires $\varepsilon(\lambda)\ge 1/p(\lambda)$ for some polynomial $p$ (asserted in definitions_latex, formal_statement_latex and parameters). Definition 2.7 on p. 8 imposes no lower bound on $\varepsilon$; the 1/poly condition belongs to Definition 2.8, for approximate-correct IO (p. 9).
- The explicit implementation sets and breaking relations attributed to the primitives io-$\mathcal F$ and io-$\mathcal{KA}$ ("The primitive io-$\mathcal F$ has as implementations all functions $\mathsf F$, and $A$ breaks $\mathsf F$ iff ..."). The paper defines the underlying notions (Definitions 2.6, 2.7, p. 8) but never spells out these primitives as pairs $(F_{\mathcal P}, R_{\mathcal P})$. The reconstruction is plausible but is the draft's, not the paper's; also "implementations are all functions $\mathsf F$" should be all oracle-aided PPT machines.
- status_note's claim that the general io-case "is named by the paper as its central open problem". The passage using the words "central open problem" (p. 6) names black-box uselessness of OWFs — not io-OWFs — for arbitrary key agreement protocols; likewise the abstract (p. 1) and the "dream result" passage (p. 11).

### Corrections the checker asked for

- **formal_statement_latex** — The draft states the conjecture as "io-F is [semi -> forall-exists-semi] black-box useless for io-KA". Remark 4.2 on p. 11 says explicitly that "A is BBU for C" is strictly stronger than "io-A is BBU for io-C", so this is a weakening of the paper's conjecture, which is about plain OWFs and plain KA (abstract p. 1; p. 6; p. 11). It also contradicts the draft's own title, one_line and informal, which all say plain one-way functions, and its own setting_latex, which correctly reports Theorem 4.12 as a plain-OWF result.
  - suggested: State it as the paper does: "The primitive $\mathcal{F}$ of one-way functions is $[\mathrm{semi}\to\forall\exists\text{-semi}]$ black-box useless for the primitive $\mathcal{KA}$ of key agreement: for every cryptographic primitive $\mathcal{Z}$, if there is a semi-black-box reduction of $\mathcal{KA}$ to $(\mathcal{F},\mathcal{Z})$, then there is a $\forall\exists$-semi-black-box reduction of $\mathcal{KA}$ to $\mathcal{Z}$ alone." If the io-variant is wanted instead, keep it but label it as the strictly weaker form the paper names parenthetically on p. 18 ("(infinitely-often) OWFs ... for more general forms of key agreement"), citing Remark 4.2 (p. 11) for the implication, rather than presenting it as the central open problem.
- **definitions_latex (infinitely-often key agreement) and parameters (epsilon)** — The draft opens the key-agreement definition with "Let $\varepsilon:\mathbb N\to[0,1]$ satisfy $\varepsilon(\lambda)\ge 1/p(\lambda)$ for some polynomial $p$", and repeats the constraint in formal_statement_latex and in the parameters list. Definition 2.7 (p. 8) imposes no lower bound on epsilon whatsoever; the 1/poly bound appears only in Definition 2.8, for approximate-correct IO (p. 9). Requiring it narrows the class of key-agreement protocols the conjecture ranges over.
  - suggested: Drop the constraint: "Let $\varepsilon:\mathbb N\to[0,1]$. An $\varepsilon$-key agreement relative to an oracle $\mathsf O$ is ...", and in the parameters list describe $\varepsilon$ as "correctness function of the key agreement; unrestricted (Definition 2.7 places no lower bound on it)".
- **pages and quotes[].page** — Every page number in the draft is a PDF page index, uniformly 2 higher than the paper's printed page number (the title page and the contents page are unnumbered). The six quotes themselves are verbatim-correct.
  - suggested: pages [1, 6, 8, 13, 20] -> [1 (title), 4, 6, 11, 18]. Quote pages: "dream result" 13 -> 11; "central open problem" 8 -> 6; "intriguing open question" 13 -> 11; "unbalanced key agreement" 13 -> 11; "constant number of steps" 6 -> 4; "simulate in its head" 20 -> 18.

## Build

- pdflatex: ok
- chktex: 4 warnings
- lacheck: 2 warnings

## What to check hardest

(1) Flavor. The abstract states the conjecture with no flavor attached ("OWFs are indeed black-box useless for general key agreement protocols"), while the paper's theorems and its Section 4.2 formulation of the main open problem are in the $[\mathrm{semi}\to\forall\exists\text{-semi}]$ flavor for infinitely-often primitives. I have stated it in the latter flavor, matching the paper's theorems and its page-18 phrasing. Remark 4.2 notes that "$\mathcal A$ is BBU for $\mathcal C$" implies "io-$\mathcal A$ is BBU for io-$\mathcal C$", so the version stated here is the weaker of the two readings; a reviewer should decide whether the intended target is the unqualified one. (2) Resolution status. I am not aware of any resolution of the general case since January 2021, but I have not exhaustively surveyed follow-up work. (3) The paper's Theorem 4.12 already removes the query restriction in the one-round case, so a candidate general proof must subsume, not merely reprove, that case.

