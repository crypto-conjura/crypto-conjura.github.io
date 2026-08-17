# Provenance: Breaking Fully Quantum Time-Lock Puzzles in the Quantum Random Oracle Model

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **On the (Im)possibility of Time-Lock Puzzles in the Quantum Random Oracle Model**
- Authors: Abtin Afshar, Kai-Min Chung, Yao-Ching Hsieh, Yao-Ting Lin, Mohammad Mahmoody
- Venue/archive: Cryptology ePrint Archive (no venue or paper number printed on the PDF itself) 2023
- Identifier: ePrint 2023/932 (inferred from the file name 2023-932.pdf, not printed on the page)
- Bibliographic detail: inferred
- File: `2023-932.pdf` (36 pages)
- sha256: `82c28ea3d14f2eabd9563d1807fa1cd4929fcc826569bcdbfe5983760b3cbe29`
- Read on 2026-08-17T19:10:18Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Settled in this paper: classical generator with quantum solver (for arbitrary completeness error, and round-optimally under perfect completeness), and quantum generator with classical solver (under perfect completeness). Open: the fully quantum case, where the paper presents no attack and shows that any attack asking only classical queries would prove the Aaronson-Ambainis simulation conjecture.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | Any time-lock puzzle in the random oracle model with a classical-query puzzle generator and a quantum-query puzzle solver can always be broken by an attacker wh... |
| openness | 5 | 5 | exact (100%) | Having said that, it is certainly possible that Theorem 1.1 could potentially be extended to the fully quantum setting using a quantum adversary. We leave this ... |
| progress | 5 | 5 | exact (100%) | For this setting, we are not able to present an attack. On the contrary, we identify a barrier for proving such result unconditionally, so long as the attack on... |
| definition | 5 | 5 | exact (100%) | Finally, we turn to the case in which both puzzle generator and puzzle solver are allowed to use quantum access to the random oracle model. Note that, in genera... |
| parameter | 4 | 4 | exact (100%) | The total number of queries of the attack will be polynomial in n, m where m is the number of (potentially quantum) oracle queries of the honest solver. |
| definition | 11 | 11 | exact (100%) | The following definition of time-lock puzzles in the quantum world focuses on a classical puzzle generator, while the solver and the adversary are both quantum.... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's own and genuinely open — the openness quote is verbatim on p. 5, and Section 6 (pp. 29-33) offers only a conditional barrier against classical-query attackers, with no conclusion section or appendix result closing it. The single most important defect is definitional: the draft's def:qgqs-tlp confines Gen to output classical (P, s), which silently deletes the case the paper flags as characteristic of the fully quantum setting in the very sentence the draft harvests as its definition quote (\"one can imagine the puzzle itself to be a quantum object\", p. 5) — repairable, since the paper's own Definition 2.6 and Construction 6.13 do use a classical puzzle, but it must be declared as a restriction rather than sold as \"fully quantum\". Two smaller misstatements accompany it: the transcript-as-puzzle reading belongs to [MMV11] (p. 4), and the barrier is conditioned on the paper's weaker Conjecture 6.1, not the AA14 folklore conjecture (p. 29).

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 5 | The problem is posed. Page 5, closing the "Quantum generators and solvers" paragraph: "Having said that, it is certainly possible that Theorem 1.1 could potentially be extended to the fully quantum setting using a quantum adversary. We leave this as an intriguing open question." The draft's openness quote is verbatim and on the page it claims. |
| Openness | pass | 29 | It stays open. I read past the citation: Section 6 (pp. 29-33) is titled "Barriers for Classical Attacks on Fully Quantum Puzzles" and delivers only Theorem 6.2, a conditional barrier against CLASSICAL-query attackers. Page 5 states flatly "For this setting, we are not able to present an attack." There is no conclusion section; the paper ends with References (p. 34) and Appendix A (p. 36), which contains only the extractor for Lemma 2.3. Nothing in Sections 3, 4, 5, the footnotes, or Table 1 gives a QGQS attack. |
| Strength | pass | 11 | The paper poses the open question only informally ("extend Theorem 1.1 ... using a quantum adversary"), and Theorem 1.1 is explicitly labelled "Informally stated, see Theorem 3.1". The draft instantiates Theorem 3.1 Part 1 (p. 11) with the generator made quantum and the attacker's queries made quantum. Clause by clause: query bound polynomial in n, m, 1/eps, 1/delta (paper: 4n^2m^2/(eps*delta^2)); rounds n/eps (paper: d_E = n/eps); success 1 - rho - eps - delta (paper: completeness error nu <= rho + eps + delta). That is the correct transposition, neither strengthened nor weakened. |
| Quantifiers and parameters | pass | 11 | Checked symbol by symbol against Theorem 3.1. Order matches: "Consider any time-lock puzzle scheme ... For any eps, delta in (0,1], there exists a randomized solver Eve" -> draft's "Let Pi be any ... Then for every eps, delta in (0,1] there exists E". E may depend on Pi, eps, delta and is inefficient, as in the paper ("inefficient" per Thm 3.1 vs. the efficient Thm 3.12). E sees only P, not r_G, matching Definition 2.6's soundness experiment. The ceiling in ceil(n/eps) is licensed by the paper's own convention on p. 11 ("we sometimes omit the ceiling function of parameters"). Two harmless deviations: the draft drops Definition 2.6's parenthetical "m >> n", and adds "for all sufficiently large kappa" where Theorem 3.1 is a per-kappa statement — the first strengthens trivially, the second weakens trivially, neither changes what a proof would have to do. |
| Attribution | pass | 5 | The open question is the harvested paper's own, in its own voice ("We leave this as an intriguing open question", p. 5), not a problem it credits to another work. It is stated as the natural extension of the paper's own Theorem 1.1, not of [MMV11] or [ACC+22]. |
| Definitions | fail | 5 | The draft's Definition def:qgqs-tlp requires Gen to output "a pair of classical strings (P, s)". At the very sentence the draft harvests as its definition quote (p. 5) the paper says: "Note that, in general, in this setting one can imagine the puzzle itself to be a quantum object." The draft quotes that line and then defines the case away, so "fully quantum time-lock puzzle" in the draft means less than the paper means by the fully quantum setting. Repairable: the paper's only formal definition (2.6, p. 11) and its only QGQS construction (6.13, p. 33, with P = c_3 and s = key_{A_3}) both use classical P and s, so the restriction is legitimate if declared. |
| Fabrication | fail | 4 | Two unsupported assertions. (a) Setting: "Under this paper's reading of a key-agreement transcript as a puzzle" — p. 4 credits the reading to another work: "as observed in [MMV11], the transcript T of a key agreement can be seen as a puzzle generated by the two honest parties with the solution being the agreed key k." (b) Setting: the barrier is said to assume "the folklore simulation conjecture of Aaronson and Ambainis [AA14] is false"; Theorem 6.2 (p. 29) is conditioned on Conjecture 6.1, which the paper introduces as "a weaker (asymptotic) version of the folklore Simulation Conjecture, which is stated as Conjecture 4 in [AA14]". Everything else I checked is supported: MMV11's O(n)-round/poly(n,m) attack and its pseudo-chain optimality (pp. 3-4), the three-way split via [BDF+11] (p. 3), the quantum-poly-time variant (p. 4), the certificate-complexity plus [ACC+22]-polynomial technique (p. 7), the amplification of the one-way-communication weak key agreement of [ACC+22] (Lemma 6.3, p. 29, and Steps 1-4, pp. 8, 30-33), OSSS05 as the known 0/1 case and "more than a decade" (p. 5), the VDF remark (p. 9), and CFHL21 PoSW as the contrasting positive (p. 9). |
| Self-containment | pass | - | No page evidence needed: this is a property of the draft. Both referenced definitions (rounds of quantum queries, fully quantum TLP) are supplied, the oracle, its quantum access unitary, the k-parallel operator, and every parameter (n, m, rho, eps, delta, kappa) are defined in notation_latex, and the success experiment is written out. A reader who has never opened the paper knows exactly what object to construct and what bound to hit. |

### Unsupported by the paper

- Setting attributes the key-agreement-transcript-as-puzzle reading to the harvested paper ("this paper's reading"); p. 4 attributes it to [MMV11].
- Setting states the barrier assumes the AA14 folklore simulation conjecture is false; Theorem 6.2 (p. 29) is conditioned on the paper's own Conjecture 6.1, described there as a weaker asymptotic version of that folklore conjecture.

### Corrections the checker asked for

- **definitions_latex (def:qgqs-tlp)** — Gen is required to output "a pair of classical strings (P, s)", silently excluding the case the paper singles out as characteristic of this setting on p. 5 — the same sentence the draft harvests as its "definition" quote: "one can imagine the puzzle itself to be a quantum object."
  - suggested: Keep the classical-puzzle definition but declare it as a restriction: add to the definition's closing remark that the conjecture as stated covers only puzzles whose (P, s) are classical, which is the case for the paper's own formal definition (Definition 2.6, p. 11) and for its fully quantum construction (Construction 6.13, p. 33, where P = c_3 and s = key_{A_3}), and that the paper explicitly contemplates but never formalizes the case of a quantum puzzle, which this statement therefore does not address.
- **setting_latex** — "Under this paper's reading of a key-agreement transcript as a puzzle" credits the harvested paper with a reading it attributes to prior work.
  - suggested: Replace with "Under the reading of a key-agreement transcript as a puzzle, observed in \cite{MMV11} and used here," — p. 4: "as observed in [MMV11], the transcript T of a key agreement can be seen as a puzzle generated by the two honest parties with the solution being the agreed key k."
- **setting_latex** — "assuming the folklore ``simulation conjecture'' of Aaronson and Ambainis \cite{AA14} is \emph{false}" understates the barrier's hypothesis. Theorem 6.2 (p. 29) is conditioned on the paper's Conjecture 6.1, which it introduces as "a weaker (asymptotic) version of the folklore Simulation Conjecture, which is stated as Conjecture 4 in [AA14]". Falsity of the weaker conjecture is the stronger assumption.
  - suggested: "assuming the paper's asymptotic Quantum Polynomial-Query Simulation Conjecture (Conjecture 6.1, p. 29) --- a weakening of the folklore simulation conjecture formally stated as Conjecture 4 of Aaronson and Ambainis \cite{AA14} --- is \emph{false}".
- **progress_note** — "Theorem 4.10 gives a round-optimal attack in exactly n rounds and mn queries" and the parallel claim for Theorem 4.6. The theorem statements (pp. 20, 22) say "at most nm classical queries in at most n rounds".
  - suggested: "in at most n rounds and at most mn queries" — the paper's "exactly n rounds" phrasing (pp. 4-5) is about round-optimality of the bound, not about the attack always using all n rounds.

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 0 warnings

## What to check hardest

Two things a reviewer should check hardest. First, strength: the paper's own words are only that "Theorem 1.1 could potentially be extended to the fully quantum setting using a quantum adversary", without pinning down the round and query bounds, so the quantitative shape above ($\lceil n/\varepsilon \rceil$ rounds, $p(n,m,1/\varepsilon,1/\delta)$ queries, success $1-\rho-\varepsilon-\delta$) is Theorem 3.1's shape transplanted verbatim to the new setting rather than a bound the paper writes down for it. An attacker achieving, say, $\mathrm{poly}(n)$ rounds, or merely non-negligible rather than near-honest success, would already answer what the authors are asking and would refute nothing here; the conjecture as stated is the sharp form. Second, scope: the paper observes that in the fully quantum setting "one can imagine the puzzle itself to be a quantum object", and I have restricted Definition~\ref{def:qgqs-tlp} to a classical puzzle and classical solution. That is deliberate --- it is the setting of the paper's own Theorem 6.2 barrier and of its Definition 2.6 --- but it means the quantum-puzzle variant is a strictly more general question that this statement does not cover. Finally, I have not verified against post-2023 literature that no follow-up has settled this; the natural attack route is the two-quantum-party polynomial-representation machinery of ACC+22, so a resolution is plausible and should be checked before publication.

