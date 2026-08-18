# Provenance: A Constant Number of Luby–Rackoff Rounds Is a Strong qPRP

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Towards compressed permutation oracles**
- Authors: Dominique Unruh
- Venue/archive: IACR Cryptology ePrint Archive (preprint, University of Tartu) 2023
- Identifier: 2023/770
- Bibliographic detail: inferred
- File: `2023-770.pdf` (22 pages)
- sha256: `e32e1eb4a186bb3743828e494076f6cc1a35fc913dc4eedceab9b9b57ff3fc4c`
- Read on 2026-08-18T15:11:16Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Open for every $r$. Four rounds are refuted by a known quantum chosen-ciphertext attack on Feistel ciphers, and the paper reports that the one published proof of the weaker forward-only statement for four rounds contains a flaw. The paper proves nothing about Luby–Rackoff itself; it only shows that a proof via its compressed permutation oracle would additionally establish the oracle's soundness for free.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 3 | 3 | exact (100%) | For example, in the classical case, the four-round Luby-Rackoff construction [21] is known to be a strong PRP if the round function is a (noninvertible) pseudor... |
| openness | 3 | 3 | exact (100%) | We know that four rounds are not sufficient [20], but nothing excludes that, e.g., five-round Luby-Rackoff could be a strong qPRP. [18] proves that four-round L... |
| definition | 3 | 3 | exact (100%) | To show this, it is sufficient to show that Luby-Rackoff, using a random function as the round function, is indistinguishable from a random permutation (given q... |
| progress | 1 | 1 | exact (100%) | If we use the compressed permutation oracle methodology to show that some construction (e.g., Luby-Rackoff) implements a random permutation (or strong qPRP), th... |
| parameter | 14 | 14 | exact (100%) | We use three-round Luby-Rackoff for this example just to keep the formulas short and readable. We are aware that three-round Luby-Rackoff is not even indistingu... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely in the paper, in the paper's own voice, and genuinely unresolved: p. 3 states it (\"we do not know yet whether an analogous result holds in the quantum case\") and reduces it to exactly the information-theoretic statement the draft formalises, and a full-text sweep for Luby/Rackoff/Feistel confirms the only later appearance is the conditional Theorem 1 on p. 14, which proves nothing unconditional about the construction. The quantifiers survive symbol-by-symbol comparison - $r$ outermost so it is a true constant, $\\mu$ before $A$, poly-query rather than poly-time, negligible-in-$n$ equal to the paper's negligible-in-$\\log|D|$ - and the Feistel definition matches the paper's three-round instance up to a swap of halves, which is renaming rather than redefinition. The one substantive defect is status_note's \"Open for every $r$\": the paper refutes $r\\le4$ (three rounds classically, p. 14 fn. 22; four rounds quantumly, p. 3 fn. 3), so the correct status is open for $r\\ge5$ - a precise, repairable error, not a misrepresentation of the problem.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 3 | The problem is in the paper, in its own voice: "the four-round Luby-Rackoff construction [21] is known to be a strong PRP if the round function is a (noninvertible) pseudorandom function [21]; we do not know yet whether an analogous result holds in the quantum case" (p. 3), with the reduction to the information-theoretic form two sentences later: "it is sufficient to show that Luby-Rackoff, using a random function as the round function, is indistinguishable from a random permutation (given queries in both directions)" (p. 3). Footnote 3 on the same page supplies the round-count status. |
| openness | pass | 14 | It stays open. I grepped the full text layer for every occurrence of Luby/Rackoff/Feistel/qPRP: the only later appearances are the three-round example used to illustrate Definition 2 (p. 14) and the conditional Theorem 1, whose conclusion is that CPO is indistinguishable from a random permutation *assuming* a construction indistinguishable from CPO exists. No section, appendix, footnote, or corollary (incl. Corollary 1, p. 18) proves anything unconditional about Luby-Rackoff. Section 5 is the last technical section; pp. 21-22 are only the symbol and keyword indices. |
| strength | pass | 3 | The drafted statement is the information-theoretic statement the paper explicitly poses as what suffices (p. 3): uniformly random round functions, indistinguishability from a random permutation, queries in both directions. It is not a strengthening beyond the paper (the paper asks for exactly this) nor a weakening. Caveat recorded as a correction: the draft's *title* labels this "Is a Strong qPRP", which is the computational keyed notion rather than the statement formalised; the paper commits the same conflation on p. 1 ("implements a random permutation (or strong qPRP)"). |
| quantifiers-and-parameters | pass | 13 | Checked symbol by symbol. $r$ is fixed outermost, before $n$ and before the query polynomial, so it really is a constant round count independent of the adversary - matching "e.g., five-round Luby-Rackoff" (p. 3, fn. 3). $\mu$ is quantified before $A$, so the bound is uniform over all query-bounded $A$. The adversary is computationally unbounded with polynomially many queries, matching "any polynomial-query algorithm $A$" in Conjecture 2 (p. 13). Negligible in $n$ is equivalent to the paper's "negligible in $\log\|D\|$" (p. 13) since $D=\{0,1\}^{2n}$ gives $\log\|D\|=2n$. $\pi\xleftarrow{\$}\mathrm{Perm}(\{0,1\}^{2n})$ matches $\pi\xleftarrow{\$}(D\hookrightarrow D)$, total injections on a finite set being permutations (p. 4, p. 13). |
| attribution | pass | 3 | The question is asked in the paper's own voice ("we do not know yet", p. 3) and is not attributed to another work; the cited references are used only for the negative data points ([20] for the four-round attack, [18]/[17] for the flawed forward-only claim). The draft does not misrepresent it as a numbered conjecture - the paper's numbered conjectures are Conjecture 1 (double-sided zero-search, p. 12) and Conjecture 2 (CPO soundness, p. 13), and the draft's openness_kind is "paper-states-open", which is the honest label. |
| definitions | pass | 14 | The paper gives no general $r$-round definition, only the three-round instance on p. 14: $t_1:=H_1(x_L)$, $t_2:=H_2(x_R\oplus t_1)$, $t_3:=H_3(x_L\oplus t_2)$, return $(x_R\oplus t_1\oplus t_3,\,x_L\oplus t_2)$. I composed the draft's $\Psi_f(x_L\\|x_R)=x_R\\|(x_L\oplus f(x_R))$ three times: it equals the paper's map after swapping the two input halves and the two output halves. That is conjugation by a fixed permutation, which cannot change indistinguishability from a uniformly random permutation - notation renamed, not redefined. "Random functions" as the round-function distribution is the paper's own instantiation of $\mathcal{D}$ (p. 14). |
| fabrication | fail | 3 | status_note asserts "Open for every $r$", which the paper refutes: four rounds "are not sufficient" (p. 3, fn. 3) and three rounds fail even classically (p. 14, fn. 22). The note then contradicts itself by stating the four-round refutation in its next clause. Two lesser unsupported items: the claim that the paper "singles out $r=5$ as the first value not excluded" (the paper writes "e.g., five-round", offering it as an example), and the setting's closing inference "so the interest here is not existence of a strong qPRP but whether the Feistel construction in particular achieves it", which is the drafter's gloss - the paper's point about [27] is that it "does not give us any technique for analyzing schemes that use a qPRP" (p. 4). |
| self-containment | pass | - | A reader who has never opened the paper could work from the statement alone: $\Psi_f$, the $r$-fold composition, $U_G$, the two-oracle query count, $\mathrm{Func}_n$, $\mathrm{Perm}(\{0,1\}^{2n})$, and negligibility are all defined in the draft, and the probability expressions name the sampling of every object they use. No undefined term (CPO, $\mathsf{Flip}$, $\mathsf{Decomp}$) leaks into the formal statement. |

### Unsupported by the paper

- status_note: "Open for every $r$" - the paper refutes $r\le4$ (p. 3, fn. 3 for four rounds; p. 14, fn. 22 for three rounds), and the draft's own next clause says so.
- parameters[r].meaning and informal: the paper "singles out $r=5$ as the first value not excluded" / "five being the first candidate not ruled out" - p. 3, fn. 3 offers five as an example ("e.g., five-round"), with no claim of it being a distinguished first candidate.
- setting_latex: "so the interest here is not existence of a strong qPRP but whether the Feistel construction in particular achieves it" - the drafter's inference, not the paper's; p. 4 instead observes that [27] gives no technique for analysing schemes that use a qPRP.

### Corrections the checker asked for

- **status_note** — "Open for every $r$" is contradicted by the paper, and by the draft's own next clause. The paper rules out $r\le4$: three rounds are "not even indistinguishable from an invertible random permutation in the classical setting, let alone the quantum setting" (p. 14, fn. 22), and "four rounds are not sufficient" quantumly (p. 3, fn. 3).
  - suggested: Open for $r\ge5$. Three rounds fail already classically (p. 14, fn. 22) and four rounds are ruled out in the quantum setting by a chosen-ciphertext attack on Feistel ciphers (p. 3, fn. 3); the paper names five rounds as a round count nothing excludes. The paper reports that the one published proof of the weaker forward-only statement for four rounds contains a flaw, with a fix work in progress. The paper proves nothing about Luby-Rackoff itself; Theorem 1 only shows that a proof via its compressed permutation oracle would additionally establish the oracle's soundness for free.
- **title** — "Is a Strong qPRP" names the computational keyed notion, but formal_statement_latex is the information-theoretic statement (uniformly random round functions, computationally unbounded poly-query adversary). The paper conflates the two the same way on p. 1, and the draft's setting_latex is explicit about the distinction, so this is a labelling slip rather than a different problem - but the title should not name a notion the statement does not formalise.
  - suggested: A Constant Number of Luby-Rackoff Rounds Is Indistinguishable from a Random Invertible Permutation (with, per p. 3, the strong-qPRP consequence noted as what this suffices for)
- **parameters[r].meaning** — "the paper singles out $r=5$ as the first value not excluded" overstates the source. Footnote 3 on p. 3 reads "nothing excludes that, e.g., five-round Luby-Rackoff could be a strong qPRP" - five is given as an example, and the paper expresses no view about it being distinguished.
  - suggested: The number of Feistel rounds. $r\le3$ fails already classically (p. 14, fn. 22) and $r=4$ is ruled out by a known quantum chosen-ciphertext attack (p. 3, fn. 3); the paper offers five rounds as an example of a count nothing excludes.
- **setting_latex** — The closing clause "so the interest here is not existence of a strong qPRP but whether the Feistel construction in particular achieves it" is presented as if it followed from the paper. The paper's own remark about [27] (p. 4) is different: [27] "does not give us any technique for analyzing schemes that use a qPRP".
  - suggested: Note also that random invertible permutations are known to be efficiently simulatable from quantum one-way functions \cite{Zha16}; the paper's point is that this gives no technique for analysing schemes that use a qPRP (p. 4).

## Build

- pdflatex: ok
- chktex: 12 warnings
- lacheck: 0 warnings

## What to check hardest

(1) Strength and quantifier. The paper asks whether ``an analogous result holds in the quantum case'' and says in a footnote only that ``nothing excludes'' five rounds, so I formalized it as an existential over $r$ rather than committing to $r=5$; a reviewer who prefers a fixed round count should note that the paper does not commit to one, and that the fixed-$r$ version is formally stronger. (2) Resolution status. Since 2023 there has been considerable work on recording techniques for random permutations and unitaries, and on quantum security of Feistel; I am not confident this has not been settled for some $r$, and it should be checked against the follow-up literature. (3) The paper's three-round illustration on page 14 writes the Feistel iteration in a form that differs cosmetically from the standard round I use; the constructions coincide up to a final swap of halves, which does not affect indistinguishability from a random permutation, but a reviewer should confirm the convention. (4) The paper phrases the goal both as ``strong qPRP'' (keyed, computational) and as indistinguishability with random round functions (information-theoretic); I used the latter, which is the version the paper says is sufficient.

