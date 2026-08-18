# Provenance: Everlasting UC Commitment from Malicious PUFs Without a Common Reference String

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Everlasting UC Commitments from Fully Malicious PUFs**
- Authors: Bernardo Magri, Giulio Malavolta, Dominique Schröder, Dominique Unruh
- Venue/archive: IACR Cryptology ePrint Archive (paper dated June 7, 2022 on the title page) 2022
- Identifier: 2021/248
- Bibliographic detail: inferred
- File: `2021-248.pdf` (37 pages)
- sha256: `ce85b7f0a94ce11e57383874b6ba7e31e444cd6516dc4bbddf9cafb95db0a997`
- Read on 2026-08-18T14:31:34Z via the `cli` backend

## How the paper leaves it open

`paper-asks-question`. Settled in the CRS model: the paper's Theorem 31 gives a protocol that everlastingly UC-realizes the multiple-commitment functionality in the fully malicious token model, where the honest token is a PUF, using a common reference string. What is open is whether any protocol achieves this with no trusted setup at all. The paper poses this as a question and does not predict the answer in either direction; the statement above records the affirmative direction, so a refutation would take the form of an impossibility theorem.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 1 | 1 | exact (100%) | In this work we present the first construction of an everlastingly UC-secure commitment scheme in the fully malicious token model without requiring honest token... |
| openness | 8 | 8 | exact (100%) | It is not clear if the techniques of [DS13] can be adapted to our setting. We leave the question of removing the necessity of a common reference string from our... |
| progress | 8 | 8 | exact (100%) | Our protocol needs to assume the existence of a common reference string to equivocate commitments in the security proof: Having access to the generation of the ... |
| openness | 8 | 8 | exact (100%) | Unfortunately this class of techniques does not seem to apply to the everlasting setting since the environment can distinguish a simulated trace once it becomes... |
| progress | 14 | 14 | exact (100%) | They showed in [MQU10] that everlasting UC commitments cannot be realised, not even in the common reference string (CRS) or the public-key infrastructure (PKI) ... |
| definition | 19 | 19 | exact (100%) | In contrast to the standard definition of unpredictability [BFSK11], in this work we require a stronger notion of adaptive unpredictability. Loosely speaking, u... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's own and genuinely open: the closing paragraph of §1.3 (p. 8) leaves removing the CRS as an open problem, the §6 protocol's Setup invokes F_CRS^G (p. 24) and every hybrid in the proof of Theorem 31 leans on the CRS trapdoor (pp. 25–26), and nothing later — including the OT impossibility of Theorem 26 (p. 22) — resolves it. The single most important defect is a fabricated parameter constraint: the draft's PUF definition demands δ(λ) < γ(λ) ≤ λ, which the paper never imposes and which is not even well-typed, since γ bounds Hamming distance between λ-bit challenges and δ between rg(λ)-bit responses — an invented side condition on the very object whose existence is conjectured. Alongside it, Definition 21's "for all adversaries" is silently narrowed to poly-query adversaries and F_HToken's requirement that M_honest be PPT with a polynomial runtime bound (p. 17) is dropped; all three are pinpointable and repairable.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence — is the problem in the paper? | pass | 8 | Found verbatim in the "On the Common Reference String" paragraph of §1.3 (p. 8): "It is not clear if the techniques of [DS13] can be adapted to our setting. We leave the question of removing the necessity of a common reference string from our protocol as a fascinating open problem." The draft's two openness quotes and its progress quote from p. 8 are exact; the p. 1 abstract quote, the p. 14 MQU10-impossibility quote, and the p. 19 unpredictability quote are also exact. |
| Openness — does it stay open through the rest of the paper? | pass | 24 | Read past p. 8 to the end. The Setup of the §6 protocol (p. 24) explicitly invokes F_CRS^G: "The ideal functionality F_CRS^G samples a random crs from the distribution of valid values, where crs := (y, seed, crs_com, crs_OT) and provides Alice and Bob with crs", and the proof of Theorem 31 uses the CRS trapdoor throughout (pp. 25–26: "the F_CRS functionality is simulated by the simulator that samples an f(x) = y such that it knows x"; "using the knowledge of the CRS trapdoor"; hybrid H_2^U where "the CRS for the OT is sampled to be in extraction mode"). Nothing later removes the CRS and there is no conclusion section revisiting it; Theorem 26 (p. 22) concerns OT, not commitment. Caution worth recording: Theorem 31's own phrasing (p. 25) says the protocol "everlastingly UC-realizes the functionality F_MCOM in the F_HToken^{PUFEval,PUFSamp}-hybrid model", omitting F_CRS from the hybrid list even though the protocol uses it — so on a purely literal reading of that sentence the draft's formal statement would already be a theorem of the paper. Only the draft's explicit "no CRS and no other trusted setup" clause keeps the statement open. |
| Strength — same statement the paper poses? | pass | 8 | The paper poses removing the CRS "from our protocol"; the draft poses the general existence question (some protocol, some PUF family). That generalization is the standard reading of "removing the necessity of a common reference string", and the paper's own framing contrasts with [DS13]'s setup-free construction (p. 8). One modest broadening: the paper names only the CRS, whereas the draft additionally forbids every other ideal functionality/trusted setup (PKI, signature cards, trusted PRFs — all discussed as trust assumptions on pp. 2, 14), making the drafted existence claim strictly harder than the paper's literal words though consistent with its spirit. |
| Quantifiers and parameters | fail | 20 | Two defects. (i) The draft's PUF definition requires "functions γ,δ: N→N with δ(λ)<γ(λ)≤λ for all λ". No such constraint appears anywhere: every occurrence of δ in the full text layer is Def. 19 (p. 19), Defs. 21 and 23 (p. 20), or uses inside the protocol and proofs (pp. 24, 25–32) — never an ordering relation with γ. It is not even well-typed against the paper's usage: γ bounds Hamming distance between λ-bit challenges, δ between rg(λ)-bit responses. Since the conjecture is an existence claim over PUF families, an invented side condition on the witness changes what would count as a proof. (ii) Def. 21 (p. 20) reads "for all adversaries A, there exists a negligible function negl(λ)"; the draft narrows this to "every adversary A making at most polynomially many oracle queries". The poly-query reading is likely what the authors intend (PUFEval is not required to be efficient, and their counterexample on pp. 20–21 uses a PPT adversary), but the restriction is the draft's, not the paper's. |
| Attribution | pass | 8 | The open problem is the harvested paper's own ("We leave the question ... as a fascinating open problem", p. 8), not one it credits elsewhere. The draft's setting correctly attributes the older, different open problem — whether everlasting security is achievable from maliciously generated tokens at all — to Müller-Quade and Unruh (p. 2: "The authors left open the question whether it is possible to achieve everlasting security in the setting of maliciously generated hardware tokens") and does not pass it off as this paper's. |
| Definitions | fail | 17 | F_MCOM (Def. 15, p. 16), everlasting UC with long-term tapes (Def. 13, p. 15, plus static corruption, p. 12), δ-reproducibility (Def. 19, p. 19), the lazy sampler (Def. 20, p. 19), and the whole F_HToken interface — create/createmal/handover/query/readout/openup, recursive child-oracle evaluation, and the long-term output tape — all match the paper (pp. 17–18). But the paper's F_HToken "is parameterized by an algorithm HTSamp, a PPT Turing machine M_honest and a polynomial p(λ) that bounds the running time of M_honest" (p. 17); the draft drops both the PPT requirement and p(λ), keeping only the (correct) note that the functionality itself is not PPT — admitting honest tokens the paper's model does not. Separately, the draft asserts F_HToken^{PUFSamp,PUFEval} means HTSamp = PUFSamp with M_honest the lazily-sampled PUFEval machine; a reasonable inference, but the paper never spells the instantiation out (the superscripted notation appears unexplained on pp. 24, 25). |
| Fabrication | fail | 20 | The δ(λ)<γ(λ)≤λ constraint is unsupported by any passage (see check 4). The poly-query restriction on the unpredictability adversary is the draft's addition. In setting_latex, "commitment, which is strictly weaker than OT in this landscape" is the draft's inference: the paper claims its results are "tight" (abstract, p. 1) and rules out everlasting OT from non-erasable honest tokens (Thm. 26, p. 22), but never states a strictness separation for commitment. Everything else checks out: the MQU10 CRS/PKI impossibility (pp. 2, 14), GIMS10's honest-token-encapsulation caveat and its incompatibility with PUFs (pp. 2, 4), OSVW13's malicious-PUF model and DS13's CRS-free unconditional commitment broken by the BKOV17 attack (pp. 4, 8), CGS08 as the encapsulation model and BFSK11 as the UC treatment of PUFs (p. 4), the OOR+14 escape route failing under an unbounded environment (p. 8), Theorem 31's number and content (p. 25), its building blocks (p. 24) and their LWE instantiability (pp. 3, 9, 10), and every bibliography entry (pp. 33–37). |
| Self-containment | pass | - | A reader who has never seen the paper can act on the statement: the PUF family, the fully malicious token functionality with its full command interface and long-term tape, F_MCOM, and everlasting UC realization with long-term tapes are all defined inline, and notation_latex fixes λ, negl, hd, ≈ (statistical), PPT, and the meaning of "F-hybrid model". The no-setup requirement is spelled out concretely ("every string they use is either sampled by a party during the execution or obtained from F_HToken"), which makes the target unambiguous. |

### Unsupported by the paper

- The parameter constraint δ(λ) < γ(λ) ≤ λ on the PUF noise/distance parameters. It appears nowhere in the paper — every occurrence of δ in the full text is Def. 19 (p. 19), Defs. 21 and 23 (p. 20), or inside the protocol and proofs (pp. 24, 25–32), and none relates δ to γ; the two bound distances in different spaces (λ-bit challenges vs. rg(λ)-bit responses).
- The restriction of the (γ,δ)-unpredictability adversary to "at most polynomially many oracle queries". Definition 21 (p. 20) says "for all adversaries A".
- "commitment, which is strictly weaker than OT in this landscape" (setting_latex). The paper calls its results "tight" (abstract, p. 1) and proves everlasting OT impossible from non-erasable honest tokens (Thm. 26, p. 22), but never asserts a strictness separation between commitment and OT.
- F_HToken's parameterization is misstated by omission: the paper requires M_honest to be a PPT Turing machine with a polynomial runtime bound p(λ) (p. 17), which the draft's definition drops, admitting honest tokens the paper's model does not.

### Corrections the checker asked for

- **definitions_latex (Definition~\ref{def:puf}) / formal_statement_latex / parameters** — The draft requires "functions γ,δ: N→N with δ(λ)<γ(λ)≤λ for all λ". The paper imposes no relation whatsoever between γ and δ (Defs. 19 and 21, pp. 19–20); the two bound Hamming distances in different spaces — γ between λ-bit challenges, δ between rg(λ)-bit responses — so the ordering is not merely unstated but ill-typed against the paper's usage.
  - suggested: "There exist a polynomial ℓ, functions γ,δ: N→N, a PUF family PUF = (PUFSamp,PUFEval) that is δ-reproducible, (γ,δ)-unpredictable and admits a lazy sampler, and a two-party protocol Π ..." — delete the clause "with δ(λ)<γ(λ)≤λ for all λ" and the matching assertion in the parameters list.
- **definitions_latex (Definition~\ref{def:puf}, item 2)** — The draft states (γ,δ)-unpredictability "for every adversary A making at most polynomially many oracle queries". Definition 21 (p. 20) states it "for all adversaries A".
  - suggested: Quantify as the paper does — "For every adversary A" — or, if the poly-query reading is retained as the only sensible one (PUFEval is not required to be efficient, and the paper's own counterexample on pp. 20–21 uses a PPT adversary), mark it explicitly as the draft's reading rather than the paper's text.
- **definitions_latex (Definition~\ref{def:htoken})** — The draft parameterizes F_HToken by "an algorithm HTSamp and a Turing machine M_honest", dropping the paper's efficiency requirement on the honest token's code.
  - suggested: "The functionality is parameterized by an algorithm HTSamp, a PPT Turing machine M_honest and a polynomial p(λ) bounding the running time of M_honest (F_HToken itself is not required to be efficient, since it places no bound on malicious token code)" — matching p. 17.
- **formal_statement_latex (scope of the setup exclusion)** — The paper asks only about "removing the necessity of a common reference string from our protocol" (p. 8); the draft's statement forbids every ideal functionality other than F_HToken, i.e. also a PKI, signature cards, or any other trusted setup.
  - suggested: Either keep the broader no-setup formulation but flag it in the status note as a strengthening of the paper's wording, or narrow the clause to "in particular the parties are given no common reference string", which is what the paper actually poses.

## Build

- pdflatex: ok
- chktex: 5 warnings
- lacheck: 2 warnings

## What to check hardest

The paper states this as a question, not as a conjecture with a direction; the affirmative existence form above is a framing choice made so the statement is provable or refutable, and a reviewer should check they are comfortable with that. A resolution in the affirmative would in practice be conditional on computational assumptions (the paper's own building blocks come from LWE), which is legitimate for everlasting security but means the existence claim would be proved conditionally rather than absolutely. The paper's Definition 21 says 'for all adversaries' without saying whether the unpredictability adversary is required to be efficient; the definition above says 'making at most polynomially many oracle queries', which is my reading and should be checked against the paper. The compressed rendering of the token functionality omits bookkeeping details of the original (the polynomial bounding the honest machine's running time, the exact 'embedded' owner semantics), which should be checked for anyone attempting an impossibility proof, where such details can matter. Finally, I have not verified against the literature that no follow-up work has resolved this; I am not aware of one, but the paper is from 2022 and the check was not performed.

