# Provenance: Polynomial Compatibility for Low-Degree, Low-Influence Distributions

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Black-Box Separations for Non-Interactive Commitments in a Quantum World**
- Authors: Kai-Min Chung, Yao-Ting Lin, Mohammad Mahmoody
- Venue/archive: Cryptology ePrint Archive, Report 2023/570 2023
- Identifier: 2023/570
- Bibliographic detail: inferred
- File: `2023-570.pdf` (30 pages)
- sha256: `58b9598d4a169a3706f1fccd94147464def09ed06eba25f292e9dacfa31a71b9`
- Read on 2026-08-17T19:13:08Z via the `cli` backend

## How the paper leaves it open

`paper-conjectures`. Open in the stated inverse-polynomial regime $\delta(d)=1/\mathrm{poly}(d)$. The analogous statement with exponentially small influences, $\delta(d)=\exp(-d)$, is proved in the work that introduced the conjecture. The group is existentially quantified, so a proof for any one finite abelian group (e.g. $\mathbb{Z}_2$) settles it, whereas a refutation must rule out every finite abelian group.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 15 | 15 | exact (100%) | Conjecture 2.8 (Polynomial Compatibility). There exists a finite abelian group Y and a function δ(d) = 1/ poly(d) such that the following holds for all d, N . |
| statement | 4 | 4 | exact (100%) | The PCC (for the group Z2 ) states that for sufficiently small δ(d) = 1/ poly(d), if F, G are distributions over polynomials of degree d over variables x1 , . .... |
| openness | 4 | 4 | exact (100%) | The work of [ACC+ 22] gave some evidence for the validity of the PCC by proving a weaker statement than the PCC in which the influences are exponentially exp(−d... |
| openness | 23 | 23 | exact (100%) | Assuming Conjecture 2.8, there is no quantum black-box construction of non-interactive commitments in the CCQD model from one-way functions. |
| definition | 14 | 14 | exact (100%) | In this section, we formally describe the Polynomial Compatibility Conjecture (PCC) of [ACC+ 22]. There are two equivalent formulations of this conjecture; one ... |
| progress | 4 | 4 | exact (100%) | The PCC bears some similarities to a conjecture by Aaronson and Ambianis [AA09] that also deals with polynomials with a low degree and low influence and which i... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely in the paper (Conjecture 2.8, p. 15) and genuinely open in it (Section 4, pp. 22-26, is entirely conditional on it; there is no appendix), and every clause, definition, and quote checks out against the source. The one real defect is in the parameter range: rendering the paper's "delta(d) = 1/poly(d)" as "delta(d) >= d^{-c}" drops the constant factor, forces delta(1) = 1, and makes the drafted statement outright false at d = 1 (Z_2, N = 1, f = (1+x)/sqrt(2), g = (1-x)/sqrt(2)) while the paper's own statement survives. That is precisely repairable by writing delta(d) >= c_1 d^{-c_2}, so the verdict is faithful-with-corrections; a second, minor correction fixes the openness_kind label, since p. 14 shows the conjecture is [ACC+22]'s and not this paper's.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 15 | Conjecture 2.8 (Polynomial Compatibility) is stated verbatim on p. 15, with an informal version on p. 4 and the section heading "2.2 Polynomial Compatibility Conjecture" on p. 14. The draft's page attributions for the statement quotes (4, 14, 15) are correct. |
| Openness | pass | 23 | The paper never proves or partially proves the PCC. It is assumed throughout: Theorem 1.1 (p. 5) "Assuming the Polynomial Compatibility Conjecture"; Section 4 opens (p. 22) "assuming Conjecture 2.8 is true"; Theorem 4.1 (p. 23), Lemma 4.4 (p. 23), Construction 4.5 (p. 24) and the proof on p. 26 are all conditional. There is no appendix; pp. 27-30 are references. It stays open through the end of the paper. |
| Strength | pass | 15 | Clause by clause the drafted hypotheses and conclusion match Conjecture 2.8: unit l2 norm for every f in supp(F) and g in supp(G); deg(f), deg(g) <= d; expected influence bounded by delta for every i in [N]; conclusion is existence of f, g and x with f(x)g(x) != 0. No clause is added, dropped, or generalized. (The parameter defect is recorded under check 4.) |
| Quantifiers and parameters | fail | 15 | Quantifier order is right (exists Y, exists delta, for all d, for all N; delta depends on d not N), but the parameter range is wrong. The paper writes delta(d) = 1/poly(d) (p. 15) and "sufficiently small delta(d) = 1/poly(d)" (p. 4). The draft renders this as delta(d) >= d^{-c}, dropping the constant factor. Since d^{-c} = 1 at d = 1 for every c > 0 and delta <= 1, this forces delta(1) = 1, and the drafted statement is then false: over Y = Z_2 with N = 1, f = (1+x)/sqrt(2) and g = (1-x)/sqrt(2) are degree 1, unit norm, have Inf_1 = 1/2 <= 1, and f(x)g(x) = 0 for both x in {+1,-1}; point masses on f and g refute it. The paper's conjecture is untouched by this, since 1/poly(d) admits e.g. delta(d) = 1/(100d). |
| Attribution | pass | 14 | The conjecture is due to [ACC+22] (Austrin, Chung, Chung, Fu, Lin, Mahmoody, CRYPTO 2022), not to this paper: p. 14 says "the Polynomial Compatibility Conjecture (PCC) of [ACC+22]", and p. 4 calls it "a recent conjecture" of [ACC+22]. The draft attributes it correctly in setting_latex, status_note, progress_note and the delta parameter entry, so it does not present a cited problem as the paper's own. The metadata field openness_kind = "paper-conjectures" is nonetheless the wrong label; see corrections. |
| Definitions | pass | 15 | Degree of a character (number of coordinates with chi_i != trivial), degree of f (max over characters with non-zero coefficient), l2-norm under the uniform distribution on Y^N, and Inf_i(f) = sum over chi with chi_i != trivial of \|fhat(chi)\|^2 all match p. 15 exactly. The characters-as-maps-to-C^* convention matches Definition 2.3 (p. 13). The Z_2 specialisation given in the draft (deg = max \|S\| with alpha_S != 0, Inf_i = sum over S containing i of alpha_S^2) matches p. 4. Nothing is silently swapped. |
| Fabrication | pass | 5 | No unsupported assertion found. Verified against the paper: exp(-d) influences proved by [ACC+22] (p. 4); the Aaronson-Ambainis kinship, footnote 4 (p. 4, quoted verbatim including the paper's own misspelling "Ambianis"); Donoho-Stark replacing Schwartz-Zippel (p. 9); CGLQ20 multi-instance machinery (pp. 10-11, Sec. 3); injective OWFs imply NICs via [GL89] and the improvement over [CX21] (p. 5); complementing [BB21] (p. 5); [HY20] initiating quantum black-box separations (p. 11); d as the sender's query count (p. 8); F, G as state polynomial distributions of the two branches (Construction 4.6, p. 25); the Y = Z_2 default and the general-group version (Remark 2.17 p. 18, and p. 23). All ten cited bibliography entries match the paper's reference list on pp. 27-30 as printed. |
| Self-containment | pass | - | The notation and definitions blocks supply the dual group, the Fourier expansion, the l2-norm, degree, influence, and supp(F), so a reader who has never opened the paper knows exactly what would have to be proved - once the delta range in check 4 is repaired. |

### Corrections the checker asked for

- **formal_statement_latex** — "a constant $c>0$, and a function $\delta\colon\mathbb{N}\to(0,1]$ satisfying $\delta(d)\ge d^{-c}$ for all $d\ge 1$" drops the constant factor implicit in the paper's "$\delta(d)=1/\operatorname{poly}(d)$" (p. 15) and its "sufficiently small" qualifier (p. 4). Because $d^{-c}=1$ at $d=1$ for every $c>0$, it pins $\delta(1)=1$ and thereby strengthens the conjecture into a statement that is false: over $\mathcal{Y}=\mathbb{Z}_2$ with $N=1$, the point masses on $f=(1+x)/\sqrt2$ and $g=(1-x)/\sqrt2$ satisfy every hypothesis ($\deg=1$, $\lVert\cdot\rVert_2=1$, $\operatorname{Inf}_1=1/2\le 1$) and have disjoint supports.
  - suggested: There exist a finite abelian group $\mathcal{Y}$, constants $c_1\in(0,1]$ and $c_2>0$, and a function $\delta\colon\mathbb{N}\to(0,1]$ satisfying $\delta(d)\ge c_1\,d^{-c_2}$ for all $d\ge 1$ --- equivalently, $\delta(d)\ge 1/p(d)$ for some polynomial $p$ --- such that for every $d\in\mathbb{N}$ and every $N\in\mathbb{N}$ the following holds. (The rest of the statement is unchanged.)
- **openness_kind** — "paper-conjectures" labels the PCC as this paper's own conjecture. Page 14 introduces it as "the Polynomial Compatibility Conjecture (PCC) of [ACC+22]"; the paper restates it as its Conjecture 2.8 and assumes it, but did not pose it. The harvest schema's enum (scripts/harvest_model.py:175) offers no cites-others value.
  - suggested: "paper-states-open" --- the paper restates and relies on an open conjecture of [ACC+22] rather than conjecturing it itself. The draft's prose already attributes it correctly; only this label is off.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `CLM23` — Kai-Min Chung, Yao-Ting Lin, and Mohammad Mahmoody, *Black-Box Separations for Non-Interactive Commitments in a Quantum World*, Cryptology ePrint Archive, Report 2023/570 (report number and year taken from the harvested filename, not printed on the page) 2023

## Build

- pdflatex: ok
- chktex: 5 warnings
- lacheck: 0 warnings

## What to check hardest

Provenance is the main thing to check. This conjecture is not originated by the harvested paper: it is the Polynomial Compatibility Conjecture of Austrin, Chung, Chung, Fu, Lin and Mahmoody (CRYPTO 2022), which the harvested paper restates as its Conjecture 2.8 and then assumes. The harvested paper does leave it open — it prints it as an unproved conjecture, reports only that the exponential-influence version is known, and hangs both of its main theorems on it — but a reviewer should decide whether the page ought to be credited to the CRYPTO 2022 paper as the source, and should read that paper's own statement to confirm the quantifier order and normalisation match what is reproduced here.

Second, I could not verify whether the conjecture has been settled since 2023, and my recollection is not reliable enough to assert either way. This should be checked against follow-up work on quantum black-box separations and on low-degree low-influence polynomials before publishing; a resolution, in particular a counterexample, would kill the page.

Third, the paper writes the influence threshold as "δ(d) = 1/ poly(d)", which I have spelled out as: there exist a constant $c>0$ and a function $\delta$ with $\delta(d)\ge d^{-c}$ for all $d\ge 1$. That is the reading the paper's usage requires (a larger $\delta$ gives a stronger conjecture, and the application only needs $\delta$ to be inverse-polynomially large in the query count), but the originating paper may pin down a specific $\delta$ and the exact form should be cross-checked.

Fourth, the paper states the conjecture for functions into $\mathbb{C}$, with a footnote that the $\mathbb{R}$-valued and $\mathbb{C}$-valued versions are equivalent up to a constant factor in $\delta$; I kept $\mathbb{C}$. The paper also gives an equivalent formulation in terms of $(\mathcal{Y},\delta,d,N)$-quantum states (Definitions 2.9--2.11 and Lemma 2.12); a solver may prefer that formulation, and the two must be presented as equivalent rather than as separate problems.

Fifth, the existential quantifier over the group is easy to misread. Proving the statement for one finite abelian group suffices, so the natural first target is $\mathbb{Z}_2$ (Boolean multilinear polynomials), which is also the case the paper's Section 4 presents for readability. A version quantified over all abelian groups would be strictly stronger than the paper's and must not be substituted.

