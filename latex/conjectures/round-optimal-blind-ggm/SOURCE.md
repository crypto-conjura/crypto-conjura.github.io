# Provenance: Round-Optimal Blind Signatures in the Generic Group and Random Oracle Model

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **On the Impossibility of Round-Optimal Pairing-Free Blind Signatures in the ROM**
- Authors: Marian Dietz, Julia Kastner, Stefano Tessaro
- Venue/archive: Cryptology ePrint Archive 2026
- Identifier: 2026/090
- Bibliographic detail: inferred
- File: `2026-090.pdf` (45 pages)
- sha256: `d363b39a8441489abdba03de0f6c85b7460724815234ad8074a9d8427f7ce4a8`
- Read on 2026-08-17T02:27:28Z via the `cli` backend

## How the paper leaves it open

`paper-notes-technique-fails`. Proved for $q\le O(\log\lambda)$ (Theorem 3.1 of the source), including the case where the random oracle's output contains group elements (Section 3.10 of the source lifts that restriction). Open for $q$ superlogarithmic and polynomially bounded; the superpolynomial message space hypothesis is retained, not relaxed.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 1 | 1 | exact (100%) | This paper investigates whether the three-round barrier for pairing-free groups is inherent. We provide the first negative evidence by proving that, in a model ... |
| openness | 9 | 9 | exact (100%) | One technical difficulty comes from the fact that it is difficult for the attacker to determine whether a given query has been made before by KeyGen or Sign, an... |
| openness | 2 | 2 | exact (100%) | The first is that the user and verification make O(log λ) queries to the random oracle, where λ is the security parameter (this restriction does not apply to th... |
| statement | 12 | 12 | exact (100%) | Theorem 3.1. There does not exist a round-optimal blind signature scheme BS in the ROM for which all of the following requirements are satisfied: |
| parameter | 13 | 13 | exact (100%) | The number of RO queries q := qUser2 + qVerify during User2 and Verify is bounded by q ≤ O(log λ). |
| parameter | 13 | 13 | exact (100%) | The message space M has size super-polynomial in λ. |
| progress | 3 | 3 | exact (100%) | Our attack breaks the one-more unforgeability of a blind signature. We note that group and random oracle queries (as opposed to actual running time) are the rel... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely in the paper and genuinely unresolved: Theorem 3.1 (p.12-13) lists q := q_User2 + q_Verify <= O(log lambda) as a hypothesis, p.9 states plainly that this restriction exists only because the attacker must guess, per query, whether KeyGen or Sign already made it, and reading to the end confirms the 2^q factor is load-bearing in Lemma 3.11, Lemma 3.12, Lemma 3.17 and the k_rand of Fig. 6 with nothing later removing it -- Section 3.10 lifts a different restriction. The quantifier structure a careless draft would garble is intact: blindness over ppt GGM adversaries, OMUF over computationally unbounded but query-bounded ones, GGM-transformation required only of User_1, User_2, Verify, and O_eq correctly absent from the OMUF oracle list. What fails is the surrounding prose: the concurrent work's technique is misdescribed as 'non-black-box hashing' when p.3 says it is NIZKs for a group-element-to-scalar conversion function, the one-liner overstates which algorithms must be generic, and the status note reports Section 3.10's proof sketch as a completed proof.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 12 | Theorem 3.1 on p.12 (hypothesis list continuing to p.13) is exactly the statement the draft reproduces; its sixth hypothesis, verbatim on p.13, is 'The number of RO queries q := qUser2 + qVerify during User2 and Verify is bounded by q <= O(log lambda).' The draft's conjecture is precisely this theorem with that hypothesis deleted. |
| openness | pass | 9 | P.9: 'This is the reason why our impossibility result is restricted to q <= O(log lambda) many queries during User2 and Verify combined: the attack performs re-randomization by just guessing for every query whether it was made before during this signing session or not.' I read all 45 pages: the bound is load-bearing throughout (beta = 1/2^{q+7} and k_rand = (2n^msgS+8lambda)*4*2^q on p.20, Lemma 3.11's 1/2^{q+4} on p.25, Lemma 3.12's 2^{q+2} factor on p.25, Lemma 3.17's 2^q*p on p.28) and nothing removes it. The paper has no conclusion or open-problems section and never labels this an open problem or conjecture in words; the openness is exactly the 'technique stalls here' kind the draft claims (openness_kind: paper-notes-technique-fails). The only later extension, Section 3.10 (p.41), lifts a different restriction. |
| strength | pass | 13 | Clause-by-clause the draft's five surviving conditions are the paper's five surviving bullets: correctness; User1/User2/Verify are transformations of GGM algorithms; super-polynomial message space; negligible blindness advantage; negligible OMUF advantage. The draft explicitly retains the super-polynomial message space rather than also relaxing it (status_note says so), so it is not the 'natural' over-generalization. The equivalence remark ('for every polynomial Q ... q <= Q') is sound since all five algorithms are ppt and so q is polynomially bounded anyway. |
| quantifiers-and-parameters | pass | 13 | The asymmetry is preserved correctly: blindness is quantified over ppt GGM adversaries (p.12), OMUF over computationally unbounded GGM adversaries restricted only in query count (p.13). The draft's OMUF clause lists exactly the paper's three oracles O_grp, H-bar, O_Sign and correctly does NOT add O_eq. Only User1, User2, Verify are required to be GGM transformations; KeyGen and Sign are not, and the draft's closing note that no bound is imposed on q_KeyGen, q_User1, q_Sign matches p.9 ('the number of queries during KeyGen, User1, and Sign is not affected by this') and p.2 ('this restriction does not apply to the signer'). q := q_User2 + q_Verify is the paper's own definition, not a redefinition. |
| attribution | pass | 12 | Theorem 3.1 is the harvested paper's own result (Dietz, Kastner, Tessaro), not one it cites to others; the draft presents it as such and correctly attributes the starting-point attack to Doettling et al. [26] and the generalization beyond purely-algebraic verification to [15] = Catalano, Fiore, Gennaro, Giunta. Every bibliography entry I spot-checked against pp.42-45 (Doettling TCC 2021 Part III LNCS 13044 pp.317-349; Catalano et al. TCC 2022 Part II LNCS 13748 pp.274-299; Maurer LNCS 3796 pp.1-12; Katz-Schroeder-Yerukhimovich TCC 2011 LNCS 6597 pp.615-629; Kastner-Nguyen-Reichle CRYPTO 2024 Part I LNCS 14920 pp.210-245; Kastner-Tessaro-Zaverucha ePrint 2026/091) matches. |
| definitions | pass | 11 | Definition 2.1 (p.10), Definition 2.2 (p.10), Definition 2.4 (pp.11-12), Definition 2.5, 2.6, 2.7 (p.12) all match the draft's restatements, including object types (G^n x {0,1}*), the deterministic Verify, the blindness game's at-most-once oracle discipline and its both-must-verify-or-bottom rule, and the OMUF win condition with ell = number of O_Sign calls. Only cosmetic divergence: the paper's O_eq may also return bottom on out-of-range labels (Definition 2.1, p.10), which the draft's restatement omits; this changes nothing about what would count as a proof. |
| fabrication | fail | 3 | Three unsupported assertions. (i) setting_latex says concurrent work [KTZ26] instantiates Fischlin 'using non-black-box hashing'; p.3 says their non-black-box technique is NIZKs about the correct evaluation of a conversion function from group elements to scalars, in an instantiation based on variants of the Nyberg-Rueppel scheme -- not hashing. (ii) one_line asserts the scheme 'uses a pairing-free group only through generic operations', but Theorem 3.1 (p.13) imposes the GGM-transformation requirement only on User1, User2, Verify. (iii) status_note calls the group-element-output case proved, whereas Section 3.10 (p.41) says 'we only describe the main changes to the proof of Theorem 3.1 here' -- a sketch. Everything else I checked is supported: the 2^{-q} guessing explanation (p.9), the 1/4 SimForge threshold (Fig. 7, p.21), Lemma 3.17's 2^q*p (p.28), the irrelevant-query/blindness argument (p.6, Lemma 3.4 p.13), the folklore framing and 'both restrictions apply to all existing constructions' (p.2), and the Katz-Schroeder-Yerukhimovich intersection-query remark (p.3). All seven quotes are verbatim and on the pages claimed. |
| self-containment | pass | - | No evidence needed from the paper: the formal statement carries its own definitions of the GGM+ROM, round-optimal blind signature, correctness, blindness and OMUF, plus the notation block, so a reader who has never seen the paper knows what would have to be proved -- namely that no tuple of algorithms satisfies all five conditions once the logarithmic query bound is dropped. |

### Unsupported by the paper

- setting_latex: '[KTZ26] instantiates Fischlin's transform over pairing-free curves using non-black-box hashing' -- the paper (p.3) describes their non-black-box technique as NIZKs about correct evaluation of a conversion function from group elements to scalars, not hashing.
- one_line: 'uses a pairing-free group only through generic operations' as a blanket condition on the scheme -- Theorem 3.1 (p.13) imposes the GGM-transformation condition only on User_1, User_2 and Verify, leaving KeyGen and Sign unconstrained.
- status_note / progress_note: 'Section 3.10 extends everything' and the claim that the group-element-output case is proved -- Section 3.10 (p.41) explicitly gives only 'the main changes to the proof', a sketch, and Theorem 3.1 is stated for bitstring-output random oracles.

### Corrections the checker asked for

- **setting_latex** — States that concurrent work [KTZ26] 'instantiates Fischlin's transform over pairing-free curves using non-black-box hashing'. The paper (p.3) attributes to them NIZKs about the correct evaluation of a conversion function from group elements to scalars, in a specific instantiation based on variants of the Nyberg-Rueppel signature scheme. A conversion function is not a hash, and the paper never says 'hashing' here.
  - suggested: ...and concurrent work \cite{KTZ26} instantiates Fischlin's transform over pairing-free curves, using NIZKs about the correct evaluation of a conversion function from group elements to scalars --- a non-black-box technique that falls outside the model --- in a scheme based on variants of the Nyberg-Rueppel signature scheme.
- **one_line** — Says the impossibility applies to schemes that use 'a pairing-free group only through generic operations', which reads as a requirement on all five algorithms. Theorem 3.1 (p.13) requires only User_1, User_2 and Verify to be transformations of GGM algorithms; KeyGen and Sign are unconstrained, which makes the paper's result stronger than the one-liner claims. The formal_statement_latex already has this right.
  - suggested: No two-move blind signature whose user algorithms and verifier touch a pairing-free group only through generic operations, and which hashes through a random oracle, can be secure, even when the user's final step and verification together make polynomially many hash queries.
- **status_note** — Asserts the result is proved 'including the case where the random oracle's output contains group elements (Section 3.10 of the source lifts that restriction)'. Theorem 3.1 is stated for the bitstring-output random oracle of Definition 2.2 (p.10), and Section 3.10 (p.41) opens with 'In order to avoid adding clutter, we only describe the main changes to the proof of Theorem 3.1 here' -- it is a proof sketch, not a carried-out proof. Remark 2.3 (p.10) likewise only says the extension is possible.
  - suggested: Proved for $q\le O(\log\lambda)$ (Theorem 3.1 of the source), for random oracles with bitstring output (Definition 2.2); Section 3.10 sketches, but does not carry out in full, the extension to random oracles whose outputs also contain group elements. Open for $q$ superlogarithmic and polynomially bounded; the superpolynomial message space hypothesis is retained, not relaxed.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `DKT26` — Marian Dietz, Julia Kastner, Stefano Tessaro, *On the Impossibility of Round-Optimal Pairing-Free Blind Signatures in the ROM*, Cryptology ePrint Archive, Paper 2026/090 2026

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 0 warnings

## What to check hardest

The most important thing for a reviewer to check: the source never writes the words "open problem" or "future work" anywhere, and never explicitly says that the logarithmic restriction should be removable. What it does say is that this restriction is exactly the price of a guessing step in its attack, and it frames its result as a "first negative evidence" / "first formal negative answer" given "under two constraints" --- so the promotion here rests on a technique-fails statement plus the paper's own framing, not on an explicit challenge sentence. A reviewer who reads the openness bar strictly may prefer to reject on that ground. Second, the $2^{q}$ loss is not localized: it appears in the number of re-randomization rounds $k_{\mathrm{rand}}$, in the parameters $\alpha,\beta$, in the thresholds of Lemmas 3.11 and 3.12, and in the oracle-fixing Lemma 3.17, so "remove the guessing step" understates the work; on the other hand the oracle-fixing lemma's $2^{q}\cdot p$ bound is tight in general, which is a reason someone might believe the barrier is real rather than technical, and that possibility should be weighed before anyone invests in a proof. Third, I have kept the superpolynomial message space hypothesis exactly as stated; a solver should not silently drop it. Fourth, I did not attempt to determine whether any follow-up work since the source's appearance has settled this. Finally, the bibliography entry for the source paper itself is marked unverified: its title and authors are printed on its first page, but its own ePrint number is not printed in its reference list; the number 2026/090 is inferred from the harvested filename and from the fact that the concurrent work it cites is 2026/091.

