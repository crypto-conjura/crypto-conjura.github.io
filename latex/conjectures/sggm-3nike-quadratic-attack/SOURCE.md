# Provenance: A Quadratic Attack on Three-Party NIKE in Shoup's Generic Group Model

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

`paper-states-open`. Settled by the paper itself in Maurer's generic group model, for every K at least 3 and including imperfect correctness. Open in Shoup's generic group model, where the paper's linear-structure technique gives nothing.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 6 | 6 | exact (100%) | In particular, we prove that in Maurer's generic group model (MGGM), where the access to the group is further limited through an oracle who does all the calcula... |
| openness | 3 | 3 | exact (100%) | We view as an interesting question the goal of closing the gap between our positive and negative results, either by building a 4-NIKE protocol with quadratic se... |
| openness | 3 | 3 | exact (100%) | In our third contribution, we prove our lower bound in Maurer's generic group model, whereas our positive result holds in Shoup's generic group model, which is ... |
| progress | 3 | 3 | exact (100%) | our result is a natural first step towards proving a stronger negative result for a basic question of whether 3-NIKE can be based merely on simple algebraic ass... |
| parameter | 8 | 8 | exact (100%) | When the protocol is in an idealized model, we use the number of queries by the algorithms to the oracle as the measure of their running time. |
| progress | 1 | 1 | exact (100%) | Prior to our work, it was open to break 3-NIKE protocols in Maurer's model with any polynomial number of queries. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open problem is genuinely the paper's own, stated verbatim on p.3 as the second of two routes to closing its gap, and it stays open — §4 is a positive SGGM construction, all of §5 is Maurer's model, and there is no appendix. The formal statement is a faithful transplant of Theorem 21 and its corollary (p.18, proof p.21): the 1 − 4δ − δ′ success bound, the c(δ′) dependence, and the O(n²) query count all check out symbol by symbol. What fails is the framing: the draft repeatedly claims a plain random oracle already delivers a quadratic gap, when the paper's own ROM three-party protocol achieves only n^{1.5} (p.1, p.3, p.4, Remark 7 p.11), which makes the stated payoff of the conjecture wrong in the direction that matters. A separate, unresolvable point: the paper's Definition 14 (p.15) requires the agreed key to be a group element and justifies it as WLOG by an argument (Remark 16, p.16) that is specific to Maurer's model, while the draft silently allows an arbitrary bit-string key.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 3 | The problem is posed verbatim in the Discussion paragraph of §1.1 on p.3: "We view as an interesting question the goal of closing the gap between our positive and negative results, either by building a 4-NIKE protocol with quadratic security in Maurer's generic group model, or by extending our impossibility result to Shoup's generic group model." The draft takes the second disjunct. |
| Openness | pass | 21 | Nothing later touches it. §4 (p.12) constructs a 4-NIKE in SGGM (a positive result); §5 (pp.14-21) is entirely Maurer's model (Def. 12 p.15, Lemma 17 p.16, Thm 20 p.17, Thm 21 p.18, proof concluded p.21). References begin on p.21 and the paper ends on p.22 with no appendix. No footnote or table resolves the SGGM case. |
| Strength | pass | 18 | The drafted statement is Theorem 21 (p.18) plus its corollary, with MGGM replaced by SGGM, which is exactly the extension p.3 asks for. The paper's Def. 14 (p.15) additionally fixes alpha, beta, gamma as publicly known constants and imposes a rigid query schedule; the draft's looser 'n-query' formulation is the natural SGGM analogue and the corollary's 'alpha, beta, gamma <= n' makes the two coincide in the n-query regime. Not a strengthening in substance. |
| Quantifiers and parameters | pass | 18 | 'probability 1 - 4delta - delta'' is verbatim Theorem 21 (p.18); the proof (p.21) sets 15*beta*epsilon = delta' and gives 45*gamma*beta/delta' learning queries, so 'for every delta' there is c = c(delta')' with quantifiers in the paper's order. One nuance: Thm 21 bounds the *expected* number of Zero queries, O(gamma*beta/delta'), whereas the draft asserts a hard bound of at most c*n^2; the paper's own corollary phrases it as 'O(n^2) queries in total', so the draft's phrasing follows the paper. |
| Attribution | pass | 3 | This is the authors' own open question, stated in their own Discussion on p.3, not a problem attributed to a cited work. The third contribution (Thm 21) is likewise the paper's own; footnote 5 on p.3 confirms 'Our proof is for K = 3 which will directly imply the negative result for any K >= 3', as the draft says. |
| Definitions | unclear | 15 | Shoup's GGM matches Def. 3 (p.8) up to the draft specialising p to a prime, which Def. 14 (p.15) does anyway; the completeness condition Pr[key_1 = key_2 = key_3] >= 1 - delta matches Def. 14 exactly. But Def. 14 requires the agreed key to be a *group element written in the party's MGGM oracle*, justified as WLOG by Remark 16 (p.16) using an argument specific to Maurer's model. The draft lets key_i be an arbitrary bit string. I cannot decide from the paper whether that WLOG transfers to Shoup's model, where labels are strings a party may hash. |
| Fabrication | fail | 11 | The draft's payoff claim -- that settling this shows algebraic structure buys 'nothing beyond the quadratic gap a plain random oracle already gives' -- is contradicted by the paper. Its ROM K-NIKE gives an n^{K/(K-1)} gap (abstract p.1; §1.1 p.3; Remark 7 p.11), i.e. n^{1.5} at K = 3, and §1.2 (p.4) states 'even for K = 3, the protocol only withstands o(n^{1.5})-time adversaries'. Quadratic-from-a-random-oracle is the two-party fact, not the three-party one. Two further unsupported claims: 'strictly weaker' (p.3 says 'generally weaker ... should be interpreted cautiously'), and 'computationally unbounded' algorithms (never stated; Def. 2 p.8 and Def. 14 p.15). |
| Self-containment | pass | - | The definitions block fixes Shoup's GGM, three-party NIKE, 'n-query', and completeness error delta; the formal statement fixes delta', c, p, and the eavesdropper's input and oracle. A reader who has never opened the paper knows what would have to be proved. |

### Unsupported by the paper

- 'the quadratic gap a plain random oracle already gives' (one_line-adjacent text in informal) and 'the quadratic gap a plain random oracle already delivers' (setting_latex): the paper's random-oracle 3-NIKE achieves only an n^{1.5} gap — abstract p.1, §1.1 p.3, §1.2 p.4, Remark 7 p.11.
- 'lower bounds proved in Maurer's model are known to be strictly weaker than their Shoup counterparts' (setting_latex): p.3 says negative results in the MGGM are 'generally weaker' and 'should be interpreted cautiously', not strictly weaker.
- 'together with the paper's four-party construction achieving a quadratic gap in that same model, would pin the answer for generic groups at exactly quadratic' (setting_latex): the paper has no three-party SGGM protocol with a quadratic gap; its quadratic SGGM construction is 4-party / 2K-party (§1.1 p.3, §4 p.12).
- 'all algorithms (honest and adversarial) are computationally unbounded' (notation_latex): unsupported phrasing — Def. 2 (p.8) measures cost by oracle queries and Def. 14 (p.15) requires poly(lambda)-query algorithms; the paper never characterises the model as computationally unbounded.

### Corrections the checker asked for

- **informal / setting_latex — the random-oracle comparison** — Both assert that a plain random oracle 'already gives'/'already delivers' a quadratic gap in the three-party setting. The paper's own ROM result for three parties is an n^{1.5} gap, not quadratic (abstract p.1; §1.1 p.3; §1.2 p.4 'even for K = 3, the protocol only withstands o(n^{1.5})-time adversaries'; Remark 7 p.11 gives Omega(lambda^{k/(k-1)})).
  - suggested: Settling it would say that generic algebraic structure, without pairings, buys no more than a quadratic gap for three parties — still strictly more than the n^{1.5} the paper's random-oracle 3-NIKE achieves, and matching the quadratic bound Barak–Mahmoody proved optimal for two-party key agreement from random oracles.
- **setting_latex — Maurer versus Shoup lower bounds** — 'lower bounds proved in Maurer's model are known to be strictly weaker than their Shoup counterparts' overstates the paper, which claims only a general tendency and a caution.
  - suggested: Quote the paper's own hedge (p.3): negative results in the MGGM 'are generally weaker than those in the SGGM and should be interpreted cautiously [Zha22, DHH+21]'.
- **setting_latex — 'would pin the answer for generic groups at exactly quadratic'** — The paper's quadratic SGGM construction is a 4-NIKE (and 2K-NIKE, §1.1 p.3 and §4 p.12). No three-party protocol in Shoup's model with a quadratic gap appears anywhere in the paper, so the conjectured three-party O(n^2) attack plus that construction does not pin the three-party answer.
  - suggested: Together with the paper's 4-party construction, it would pin the maximum achievable gap in Shoup's model at quadratic across K >= 3 collectively — achieved at K = 4 — while the best gap achievable for three parties would remain open between n^{1.5} and n^2.
- **notation_latex — 'all algorithms (honest and adversarial) are computationally unbounded'** — The paper never says this. Def. 2 (p.8) says only that query count substitutes for running time in idealized models, and Def. 14 (p.15) asks that all algorithms be efficient, submitting at most poly(lambda) queries; security is against poly(lambda)-time E.
  - suggested: State it as the drafter's modelling choice: cost is oracle queries and local computation is unmetered (which the Thm 21 attacker's rejection sampling of compatible random seeds does require), rather than presenting 'computationally unbounded' as the paper's phrasing.

## Build

- pdflatex: ok
- chktex: 5 warnings
- lacheck: 0 warnings

## What to check hardest

Two things a reviewer should check hardest. First, resolution: this is a 2023 ePrint in an active line (fine-grained NIKE, generic-group lower bounds), and I have not verified against the papers citing it; if a follow-up has proved or refuted the Shoup-model statement, this candidate is void. Second, the exact quantitative form: the 1-4*delta-delta' success bound is transported verbatim from the paper's Maurer-model Theorem 21, since that is what 'extending our impossibility result' names. A reviewer might reasonably prefer the cruder form the abstract uses --- any n-query 3-NIKE is broken by an O(n^2)-query attacker --- which is the same claim up to constants for constant completeness error. Also note the honest parties here are computationally unbounded and only their queries are counted; that is the paper's own convention (Definition 2) but it makes the statement a strong one, since in Shoup's model unbounded local computation on labels is a real power.

