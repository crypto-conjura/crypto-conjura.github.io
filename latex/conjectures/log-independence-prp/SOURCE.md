# Provenance: Logarithmic Independence Implies Pseudorandomness for Local Permutations

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **When Simple Permutations Mix Poorly: Limited Independence Does Not Imply Pseudorandomness**
- Authors: Jesko Dujmovic, Angelos Pelecanos, Stefano Tessaro
- Venue/archive: Cryptology ePrint Archive 2026
- Identifier: 2025/2282
- Bibliographic detail: inferred
- File: `2025-2282.pdf` (43 pages)
- sha256: `0928c1c836b9748b8f7ac47cd98745c2c25b5bf34da41ab0e2bcbef15951b3aa`
- Read on 2026-08-17T01:05:08Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. The original constant-order conjecture (order $4$, and in fact every constant order $k$) is refuted by the source paper's explicit construction. The logarithmic-order version stated here is untouched: the paper offers neither a proof nor a counterexample, and states that an unconditional proof would imply one-way functions exist.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 38 | 38 | exact (100%) | If P T is negligibly far from log(n)-wise independence, then P T is also a pseudorandom permutation. |
| statement | 38 | 38 | exact (100%) | Conjecture 3 (Logarithmic Independence). Let P be a randomized permutation {0, 1}n → {0, 1}n such that each output bit only depends on a constant number of inpu... |
| openness | 38 | 38 | exact (100%) | Although we refute Conjecture 1 in its broadest form, our counterexample has apparent limitations. To further encourage the study of pseudorandom permutations, ... |
| progress | 38 | 38 | exact (100%) | Our counterexample crucially relies on the ability to distinguish a constant number of invariants using only a constant number of wires. This approach is not vi... |
| openness | 38 | 38 | exact (100%) | We hope that attempts to prove them under non-trivial conditions (such as the existence of one-way functions) or refute them lead to new insights about the pseu... |
| definition | 4 | 4 | exact (100%) | Concretely, let P be a randomized permutation over n-bit strings which we assume to be local, i.e., each output bit only depends on a small (constant) number of... |
| parameter | 4 | 4 | exact (100%) | The motivation behind four (as opposed to other constants) is rather arbitrary, but HMMR point out that counterexamples exist if we were to use 3-wise independe... |
| progress | 4 | 4 | exact (100%) | Our main result is a refutation of Conjecture 1. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 3 is genuinely the paper's own, stated verbatim on p. 38, and the paper explicitly flags it as \"not refuted by our work\" — its counterexample is locked to constant k by Theorem 4.1 (p. 14) and Lemma 4.9 (p. 18), so it cannot reach log(n). The formal statement, definitions, quantifiers, and attribution all survive symbol-by-symbol comparison. What fails is the surrounding prose: the setting and progress note both invert the quantifier on the counterexample into a single permutation working \"for every constant k\", and the setting calls the special-string set constant-sized when it has (n-2)(k+1) members — both repairable in place, neither reaching the conjecture itself.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 38 | Conjecture 3 (Logarithmic Independence) appears verbatim in Section 8, p. 38: "Let P be a randomized permutation {0,1}^n -> {0,1}^n such that each output bit only depends on a constant number of input bits. If P^T is negligibly far from log(n)-wise independence, then P^T is also a pseudorandom permutation." The draft's quotes are accurate transcriptions. |
| openness | pass | 38 | Section 8 introduces Conjectures 3-6 with "Each is a weakened variant of Conjecture 1 not refuted by our work," and offers only an obstruction for Conjecture 3, not a proof or counterexample. I read past the citing passage: p. 38 is the last content page (39-42 references, 43 code appendix), and the paper's counterexample is confined to constant k -- Theorem 4.1 (p. 14) fixes k as a positive integer, Lemma 4.9 (p. 18) holds only "when k is constant" and needs \|Sigma\| >= (k+3)^2, and Lemma 6.2/6.4 (pp. 21-22) assume constant k. Nothing in the paper resolves the log(n) case in either direction. |
| strength | pass | 38 | Clause by clause the drafted implication is the paper's: same locality hypothesis (constant-locality round permutation on {0,1}^n), same T-fold sequential composition, same antecedent (negligibly far from log(n)-wise independence), same consequent (P^T is a PRP). Not strengthened to a strong/two-sided PRP, not weakened to a distinguisher-class claim, and not conflated with the paper's sibling Conjectures 4-6 (p. 38), which alter the round model or the number of rounds instead of the independence order. |
| quantifiers-parameters | pass | 38 | Formal statement: ell is a constant independent of n (paper p. 4: "a small (constant) number of input bits"), one negligible epsilon uniform over input tuples, k(n) = floor(log_2 n) rendering the paper's log(n). Rendering log(n) as floor(log_2 n) fixes a base the paper leaves implicit; the paper uses base-2 logs throughout (e.g. log\|Sigma\| against 2^{-n} bounds, p. 36), so this is a faithful concretization, and floor is needed for integrality. "T arbitrary" matches the paper's silence about T -- neither Conjecture 1 (p. 4) nor Conjecture 3 (p. 38) constrains it. The quantifier error is not here but in the setting prose (see fabrication). |
| attribution | pass | 38 | Conjecture 3 is the source paper's own, posed by its authors in Section 8 (p. 38), not a problem it merely cites. The draft keeps this distinct from HMMR's Conjecture 1 (p. 4, attributed to [HMMR04], with the paper's footnote 1 declining the common Rackoff attribution) and from Gowers' Conjecture 7 (p. 38), which the draft correctly reports as weaker in the sense that refuting it would refute Conjectures 3-6. |
| definitions | pass | 10 | Randomized permutation and P^t with independent uniform per-round randomness match Definition 3.1 (p. 10); distinct ordered k-tuples A^{(k)} matches Definition 3.2 (p. 10); "negligibly far from k-wise independence" as negligible d_TV from the uniform distribution over A^{(k)} matches Definition 3.9 (p. 11), including the distinct-tuple reference distribution. Locality matches the paper's informal "each output bit depends on a constant number of input bits" (p. 4). The paper never formally defines PRP; the draft's forward-query, single-key, poly-time-distinguisher definition is the standard notion the paper's own attack instantiates (Theorem 5.1, p. 19) and does not silently substitute a strong PRP. |
| fabrication | fail | 14 | Two claims about the paper's own result are unsupported. (1) The setting and progress note assert a single permutation that is negligibly far from k-wise independent "for every constant k" / "for any constant k"; Theorem 4.1 (p. 14) reads "Let k be a positive integer. There exists a block cipher P...", i.e. for-all-k-there-exists-P, and it must be so because Lemma 4.9 (p. 18) requires \|Sigma\| >= (k+3)^2 and the alphabet carries k+3 special symbols (p. 10). (2) The setting says the construction "freezes a constant number of 'special' strings along a deterministic cycle"; by Definition 4.7 (p. 15) Special contains every string with a valid counter heart^i club^{n-1-i} (i in [n-2]) and value in [k+1], so \|Special\| = (n-2)(k+1), laid out as k+1 deterministic chains of length n-2 (Figure 6, p. 19). Everything else checks out against the paper: the (n-2)-fold composition and the (k+1)-input constant-probability distinguisher (Thm 4.1(ii),(iii), p. 14; Thm 5.1, p. 19), the unary counter (p. 7), the conditional brickwork (pp. 5-8), the final linear relation w^1+...+w^k = w^{k+1} (p. 20), the omega(1)-invariants obstruction, the one-way-functions/P != NP remark, and the Gowers weaker-conjecture claim (all p. 38). |
| self-containment | pass | - | Every notion the formal statement uses -- ell-locality, T-fold composition, negligible distance from k(n)-wise independence, PRP -- is defined in the draft's own definitions block, and the parameters n, ell, T, k(n) are all bound. A reader who has never opened the paper knows exactly what would count as a proof. No paper evidence needed for this check. |

### Unsupported by the paper

- Setting and progress note: a single local randomized permutation whose composition is negligibly far from k-wise independent "for every / for any constant k". The paper's Theorem 4.1 (p. 14) is for-all-k-there-exists-P, and Lemma 4.9 (p. 18) ties the alphabet size to k, so the existence-first reading is not in the paper.
- Setting: "freezes a constant number of ``special'' strings along a deterministic cycle". The special set has (n-2)(k+1) members (Definition 4.7, p. 15; Figure 6, p. 19); only the number of invariants is constant.

### Corrections the checker asked for

- **setting_latex** — "It constructs a local randomized permutation over a constant-size alphabet whose (n-2)-fold composition is negligibly far from k-wise independent for every constant k" swaps the quantifier order. Theorem 4.1 (p. 14) states "Let k be a positive integer. There exists a block cipher P...", and the construction's alphabet depends on k (Lemma 4.9, p. 18, requires |Sigma| >= (k+3)^2; the alphabet has k+3 designated symbols, p. 10), so no single permutation serves all k.
  - suggested: For every constant $k$, it constructs a local randomized permutation over a constant-size alphabet (of size depending on $k$) whose $(n-2)$-fold composition is negligibly far from $k$-wise independent, and yet is distinguished from a random permutation, with constant probability, by an efficient adversary querying only $k+1$ points.
- **progress_note** — Same quantifier swap: "constructs a constant-locality randomized permutation over a constant-size alphabet whose (n-2)-fold composition is negligibly far from k-wise independent for any constant k" reads as one permutation good for all k.
  - suggested: For each constant $k$, the paper's main theorem constructs a constant-locality randomized permutation over a constant-size alphabet (whose size grows with $k$) whose $(n-2)$-fold composition is negligibly far from $k$-wise independent while admitting an efficient $(k+1)$-query distinguisher, which refutes the constant-order form of the implication.
- **setting_latex** — "freezes a constant number of ``special'' strings along a deterministic cycle" misstates the construction. By Definition 4.7 (p. 15) the special set is all strings with a valid counter heart^i club^{n-1-i}, i in [n-2], and value in [k+1], so there are (n-2)(k+1) of them, forming k+1 deterministic chains of length n-2 (Figure 6, p. 19). What is constant is the number of invariants, which is precisely the quantity the paper's obstruction argument (p. 38) is about.
  - suggested: drives $k+1$ families of ``special'' strings deterministically around cycles of length $n-2$ (one cycle per special value), while a conditional brickwork circuit randomizes everything else, and in the last round sends the $k+1$ strings whose counter has run out to $k+1$ values obeying one linear relation that a random permutation would not obey

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `DPT26` — Jesko Dujmovic, Angelos Pelecanos, Stefano Tessaro, *When Simple Permutations Mix Poorly: Limited Independence Does Not Imply Pseudorandomness*, Cryptology ePrint Archive, Paper 2025/2282 2026

## Build

- pdflatex: ok
- chktex: 3 warnings
- lacheck: 0 warnings

## What to check hardest

Check the following hardest. (1) The paper writes "log(n)-wise" with no base and no rounding rule; I fixed $k(n) = \lfloor \log_2 n \rfloor$. Any $\Theta(\log n)$ reading is presumably intended, but the choice is mine, not the paper's. (2) The paper does not constrain $T$, so I left it an arbitrary function of $n$. A reader might expect $T \le \mathrm{poly}(n)$ -- the paper's own counterexample uses $T = \Theta(n)$ -- but adding that bound would restrict the class of instances and so weaken the conjecture, which is why I did not. (3) The paper does not say whether the PRP distinguisher gets an inverse oracle; I used the forward-only notion, matching the distinguisher in its own Theorem 5.1. (4) The paper does not spell out uniformity or efficient evaluability of the family; constant locality alone does not force $\mathcal{P}$ to be efficiently computable, though it is for every natural instantiation. I left this out of the statement for the same strength reason, and a reviewer may decide the house style wants it in. (5) Conjectures 3, 5 and 6 on page 38 are three siblings of one shape; I promoted only Conjecture 3 because the run allows one candidate, and a reviewer should confirm that is the intended choice rather than Conjecture 6, which is closer to Gowers' conjecture. (6) The paper is dated 24 February 2026 and sits at the edge of what I know; I have no evidence any of these conjectures has since been settled, but I could not rule it out from the paper alone. (7) The bibliography entry DPT26 for the source paper itself is marked unverified because it is read off the title page, not off a reference list; its ePrint number comes from the filename.

