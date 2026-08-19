# Provenance: A Two-Round Adaptively Secure Threshold Signature With a Message-Independent First Round

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Tweed: Adaptively Secure Lattice-Based Two-Round Threshold Signatures**
- Authors: Kaijie Jiang, Stefano Tessaro, Hoeteck Wee, Chenzhi Zhu
- Venue/archive: Cryptology ePrint Archive 2026
- Identifier: ePrint 2026/417
- Bibliographic detail: inferred
- File: `2026-417.pdf` (34 pages)
- sha256: `6db1dbf3896306f8f7944c110af732430a716c9116d0ca824d685d35380c1f23`
- Read on 2026-08-19T00:25:37Z via the `cli` backend

## How the paper leaves it open

`paper-notes-technique-fails`. Settled: two-round adaptive security with both rounds message-dependent ($0+2$), from MLWE and MSIS, is achieved by this paper; $1+1$ lattice schemes exist but are proved only statically secure; adaptive security with an offline round is achieved at three rounds in the pairing-free setting. Open: any scheme that is $1+1$ (two rounds total, message-independent first round) and adaptively secure against $T-1$ corruptions, in the lattice setting or any other.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 3 | 3 | exact (100%) | First off, we note that the first round, in our scheme is message-dependent, unlike in some of the other schemes only proved to be statically secure [EKT24, CAT... |
| statement | 3 | 3 | exact (100%) | A message-independent first round can be preprocessed, and signing can then be completed later, in a single round, once the message becomes known. Such schemes ... |
| openness | 3 | 3 | exact (100%) | Figure 1 also highlights that our scheme matches the state-of-the art for pairing-free schemes, and hence we are unlikely to overcome this barrier using our tec... |
| definition | 2 | 2 | exact (100%) | The notation X + Y denotes the number of offline (i.e., message independent) and online (i.e., message dependent) rounds, respectively. |
| progress | 2 | 2 | exact (100%) | To start with, it is helpful to point out that a major barrier in proving adaptive security in many prior schemes (such as EKT [EKT24] and CATZ [CATZ24]) is the... |
| progress | 2 | 2 | exact (100%) | This is a significant improvement over the only existing adaptively secure lattice-based threshold signature [KRT24], which requires five rounds. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is real and genuinely unachieved: the paper says under \"What we do not achieve\" (p. 3) that its first round is message-dependent and that it is \"unlikely to overcome this barrier using our techniques,\" and nothing later closes it - Sign_1 still takes mu in Fig. 6 (p. 17), and there is no conclusion or variant. The decisive defect is in clause (ii): the draft demands a reduction with linear loss from MLWE and MSIS, whereas the paper's own results carry a Q_h^2 factor and a cube-root (Lemma 17, p. 19) or square-root (Theorem 2, p. 12) exponent, so a scheme built to the paper's own standard would fail the drafted statement - a tightness demand the paper never makes. Compounding this, a single (q, d, k, m, beta) tuple is forced on both lattice problems where the paper uses very different ones, and the status note extends the openness claim to \"any other\" setting, which the paper's pairing-free-and-lattices-only comparison (Fig. 1 caption, p. 2) does not support.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 3 | The paragraph "What we do not achieve" (p. 3) states that Tweed's first round is message-dependent, that a message-independent first round could be preprocessed so signing completes in one online round, and that "we are unlikely to overcome this barrier using our techniques." All six of the draft's quotes appear verbatim on the pages it cites (Fig. 1 caption on p. 2; the rewinding-barrier and five-round sentences on p. 2; the three offline-round sentences on p. 3). |
| Openness | pass | 17 | Nothing later in the paper closes it. Definition 2 (p. 10) gives Sign_1(i, sk_i, SS, mu) with the message as an input; the game oSign_1(i, SS, mu) (Fig. 4, p. 11) and the actual scheme Sign_1(i, sk_i, SS, mu) computing U = H_1(mu) (Fig. 6, p. 17) are both message-dependent. The paper has only Sections 1-5, no conclusion or open-problems section, and the only "future work" items are parameter improvement (p. 2) and identifiable abort (p. 3). |
| Strength | fail | 19 | Clause (ii) demands a reduction with linear loss: Adv^adp-tsuf <= p(kappa)(Adv^mlwe + Adv^msis) + negl, with B and C running in time p(kappa) times that of A. The paper achieves nothing of that shape and asks for nothing of that shape. Lemma 17 (p. 19) gives Adv^iuf <= 32^{1/3} Q_h^2 (Adv^{hnf-msis} + 8(k+1)2^{-6kappa})^{1/3} in one branch, or an MLWE-branch bound with a t*Q_h factor; Theorem 2 (p. 12) gives the single-signer analogue with exponent 1/2 and factor 32^{1/2} Q_h^2. A cube-root or square-root loss does not imply the drafted linear bound, so the paper's own scheme would not satisfy the drafted clause. The conjecture is thus a strengthening of the qualitative question the paper poses ("can we get a message-independent first round") into a tightness demand the paper never raises. |
| Quantifiers and parameters | fail | 19 | The draft fixes a single tuple (q, d, k, m, beta) and uses it for both MLWE and MSIS, with beta simultaneously the ell-infinity bound on MLWE secrets and the Euclidean bound on MSIS solutions. The paper uses distinct and very differently sized tuples: MSIS_{q,d,ell,m,4L_1^{(1)}} where L_1^{(1)} is a signature norm bound, against MLWE_{q,d,ell,n+ell,beta_lwe} and HNF-MLWE_{q,d,m,ell+m,beta_hlwe} with small beta_lwe (Lemma 17, p. 19; Fig. 2, p. 9). The draft also drops the paper's dimension parameters t, ell, n entirely. The corruption quantifier itself is correct: the draft's Cor requiring \|CS\| < T-1 and the final \|CS\| <= T-1 check match Fig. 4 (p. 11) exactly. |
| Attribution | pass | 3 | The limitation is the harvested paper's own, stated in the first person under "What we do not achieve" (p. 3), and the comparison data the draft leans on is the paper's own Fig. 1 (p. 2). It is not a problem the paper merely attributes to someone else. Every bibliography entry the draft lists matches the paper's own reference list (pp. 26-28) in authors, title, venue, volume, pages and year; the only differences are citation keys printed as BLT+24 / BKL+25 / CKK+25 in the paper versus BLT24 / BKL25 in the draft, which is naming, not content. |
| Definitions | pass | 11 | The adp-TSUF game reproduces Fig. 4 (p. 11) faithfully: per-signer counters, per-session table P, isUsed flag, Cor returning the whole of st_i with no erasures, and the mu not in S win condition. MLWE and MSIS match Fig. 2 (p. 9). Removing mu from Sign_1 is a deliberate and disclosed change - it is what the conjecture is about - and moving S <- S union {mu} to oSign_2 follows from it. Two smaller deviations: the draft's oSign_2 adds a requirement SS' = SS that the paper's oracle does not have (the paper stores only (isUsed, st)), which slightly restricts the adversary; and the draft adds x != 0 to MSIS, which the paper's Fig. 2 game omits - that omission is a typo and the draft's version is the correct one. |
| Fabrication | fail | 2 | The status note asserts the gap is open "in the lattice setting or any other." The paper's Fig. 1 caption (p. 2) says explicitly that it lists only lattice constructions and schemes "proved to be adaptively secure from pairing-free groups, without the AGM"; p. 1 cites adaptively secure pairing-friendly schemes [BL22, DR24] that the table deliberately excludes. The paper's own claim is the narrower "our scheme matches the state-of-the art for pairing-free schemes" (p. 3). Second: the progress note's explanation that the paper's MSIS rewinding is harmless "because the corruption simulation there is independent of the forking" is the draft's own inference; the paper says only that the reduction knows the secret key throughout (p. 4) and that its IUF proof "largely avoids rewinding" (p. 6). Third: the linear-loss reduction of clause (ii) is asserted as the target with no support anywhere in the paper. The setting also omits the paper's own deflation of the goal on p. 3 ("In practice, however, this feature is likely less beneficial than one may think..."), which changes how the paper frames the target's value. |
| Self-containment | pass | - | The three definitions, the notation block and the parameter list together let a reader who has never seen the paper know what to prove: the syntax with a mu-free Sign_1, the adaptive game with the T-1 corruption cap, and the two lattice problems are all spelled out, and the closing paragraph names the four properties (a)-(d) that must hold simultaneously. No evidence needed from the paper for this check. |

### Unsupported by the paper

- status_note: "in the lattice setting or any other" - the paper's Fig. 1 caption (p. 2) restricts its survey to lattice schemes and to pairing-free group schemes proved adaptively secure without the AGM, and p. 1 cites adaptively secure pairing-friendly constructions [BL22, DR24] that the table deliberately excludes. The paper's own claim is only that Tweed "matches the state-of-the art for pairing-free schemes" (p. 3).
- formal_statement_latex clause (ii): the polynomial-loss reduction Adv^adp-tsuf <= p(Adv^mlwe + Adv^msis) + negl. Nothing in the paper asks for or achieves a tight reduction of this form; its own bounds carry a Q_h^2 factor and a fractional exponent (Theorem 2, p. 12; Lemma 17, p. 19).
- progress_note: "but only because the corruption simulation there is independent of the forking, which is not the case for the 1+1 schemes." The paper gives no such explanation. It says the reduction knows the secret key throughout and can therefore simulate corruptions for free (pp. 3-4), and that the IUF proof "largely avoids rewinding" (p. 6); the independence-of-forking rationale is the draft's own.
- formal_statement_latex / definitions_latex: the requirement that one parameter tuple (q, d, k, m, beta) serve both MLWE and MSIS, with beta doing duty as both an ell-infinity secret bound and a Euclidean solution bound. The paper's instantiation uses separate and widely differing tuples (Lemma 17, p. 19).

### Corrections the checker asked for

- **formal_statement_latex (clause (ii))** — Demands a reduction with linear loss, Adv^adp-tsuf <= p(kappa)(Adv^mlwe + Adv^msis) + negl(kappa) with B, C running in time p(kappa) times that of A. This is strictly stronger than anything the paper achieves or asks for: Lemma 17 (p. 19) gives 32^{1/3} Q_h^2 (Adv^{hnf-msis} + 8(k+1)2^{-6kappa})^{1/3} in one branch, and Theorem 2 (p. 12) gives the exponent-1/2 analogue, both as either/or statements with a separate MLWE branch. A scheme proved to the paper's own standard would not satisfy the drafted inequality.
  - suggested: State the security requirement asymptotically, matching what the paper actually establishes: "for every PPT adversary A making at most poly(kappa) queries to oSign_1, oSign_2, Cor and the random oracle, Adv^{adp-tsuf}_{TS[N,T]}(A, kappa) = negl(kappa), provided the MLWE and MSIS problems are hard for the chosen parameters." If a concrete bound is wanted, reproduce the paper's shape: an either/or between an MSIS branch of the form c * Q_h^2 * (Adv^{msis} + 2^{-Omega(kappa)})^{1/3} and an MLWE branch linear in Adv^{mlwe}, rather than a single linear sum.
- **formal_statement_latex (parameters) and definitions_latex (Definition 3)** — A single tuple (q, d, k, m, beta) is shared by MLWE and MSIS, with beta serving both as the ell-infinity bound on MLWE secrets and as the Euclidean bound on MSIS solutions. The paper uses distinct tuples of very different magnitude - MSIS_{q,d,ell,m,4L_1^{(1)}} with L_1^{(1)} a signature-norm bound, versus MLWE_{q,d,ell,n+ell,beta_lwe} and HNF-MLWE_{q,d,m,ell+m,beta_hlwe} with small beta_lwe (Lemma 17, p. 19).
  - suggested: Quantify over two independent tuples: "there exist parameters d (a power of two), q (an odd prime), and tuples (k_1, m_1, beta_sis) and (k_2, m_2, beta_lwe), all polynomially bounded, such that Adv^{adp-tsuf} is bounded in terms of Adv^{msis}_{q,d,k_1,m_1,beta_sis} and Adv^{mlwe}_{q,d,k_2,m_2,beta_lwe}."
- **status_note** — "Open: any scheme that is 1+1 ... and adaptively secure against T-1 corruptions, in the lattice setting or any other." The paper never claims this holds in every setting. Fig. 1's caption (p. 2) restricts the survey to lattices and to pairing-free group schemes proved adaptively secure without the AGM, and p. 1 cites adaptively secure pairing-friendly schemes [BL22, DR24] that the table excludes.
  - suggested: "Open: any scheme that is 1+1 (two rounds total, message-independent first round) and adaptively secure against T-1 corruptions, in the lattice setting, and - per the paper's Fig. 1, which covers lattices and pairing-free groups without the AGM - among pairing-free group-based schemes as well. The paper says nothing about pairing-friendly or AGM-based constructions."
- **definitions_latex (Definition 2, oSign_2)** — The oracle returns bot if SS' != SS, a condition absent from the paper's oSign_2 (Fig. 4, p. 11), which stores only (isUsed, st) and never re-checks the signer set. The addition restricts the adversary and therefore weakens the notion relative to the paper's.
  - suggested: Either drop the SS' != SS check, storing (isUsed, st) as the paper does, or keep it and say explicitly that it is an addition forced by removing mu from Sign_1 (the signer set now being the only thing the first round commits to).
- **setting_latex** — Quotes the paper's "Such schemes promise to be nearly as good as round-optimal ones" but omits the sentence immediately following it on p. 3, in which the paper deflates the goal: the feature "is likely less beneficial than one may think, as ensuring that parts of the preprocessed first-round communication are not reused adds significant complexity from an engineering standpoint, and such reuse typically leads to a complete loss of security."
  - suggested: Add the caveat after the quoted sentence, so the setting reflects that the paper records the offline round as something it does not achieve while also questioning how much practical value it carries.

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 2 warnings

## What to check hardest

The paper never writes the words ``open problem'' here. It heads the paragraph ``What we do not achieve'', states the limitation, and says its techniques are unlikely to overcome the barrier -- a reviewer should judge whether that is enough to count as the authors leaving it open. Relatedly, the paper takes no position on direction: an impossibility result is just as consistent with what it says, so the existence phrasing above is a choice about how to state the open problem, not something the authors assert. The paper also argues that a preprocessing round is worth less in practice than one might think, because reuse of preprocessed material is catastrophic and preventing it is an engineering burden; a reviewer may weigh that against the value of settling this. On the formalisation: the paper's own $\mathrm{adp}\text{-}\mathrm{TSUF}$ game (its Figure 4) adds $\mu$ to the set $S$ of signed messages in the first-round oracle, which is impossible when the first round does not see $\mu$, so Definition 2 above moves that bookkeeping to the second-round oracle -- check that this is the intended adaptation and does not weaken the game. Finally, the paper's comparison table is a snapshot; a reviewer should check whether any 2025--2026 follow-up (in particular further work along the lines of the two-round group-based scheme the paper attributes to Chen) already gives a $1+1$ adaptively secure scheme.

