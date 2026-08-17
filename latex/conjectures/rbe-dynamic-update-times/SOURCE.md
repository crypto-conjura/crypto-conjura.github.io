# Provenance: Update Lower Bounds for Registration-Based Encryption with Key-Dependent Update Times

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Lower Bounds for the Number of Decryption Updates in Registration-Based Encryption**
- Authors: Mohammad Mahmoody, Wei Qi, Ahmadreza Rahimi
- Venue/archive: IACR Cryptology ePrint Archive; the acknowledgements thank the anonymous reviewers of TCC 2022, so the paper appeared at TCC 2022 2022
- Identifier: ePrint 2022/1285 (taken from the file name; no ePrint number is printed on the pages)
- Bibliographic detail: inferred
- File: `2022-1285.pdf` (30 pages)
- sha256: `8d37b65942fb164bb733a36dd85545fa92a21b4942ae816e41cbbe2968c8c85e`
- Read on 2026-08-17T20:13:14Z via the `cli` backend

## How the paper leaves it open

`paper-states-open`. Proved when the update schedule is a fixed function of registration times (the paper's Theorem 4.1), and by the paper's Theorem 4.12 also when the schedule is any fixed function of the sequence of registered identity names and of the CRS. It is open exactly when the schedule may depend on the sampled public keys, equivalently under the standard RBE completeness notion where updates are fetched on demand after decryption returns GetUpd.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | Our main result provides an answer to the question above by proving an almost tight lower bound for the number of updates of any RBE schemes in which the update... |
| openness | 4 | 4 | exact (100%) | Our result leaves it open to either extend our lower bound to RBE schemes with dynamic update times that depend on the public keys or to invent new RBE schemes ... |
| openness | 11 | 11 | exact (100%) | Our completeness is stronger than (and implies) the standard completeness definition of RBEs; in our definition, the update times are fixed. It remains open to ... |
| progress | 10 | 10 | exact (100%) | As it remains open to potentially bypass our lower bound by leveraging on dynamic update times that depend on the registered keys, we point out a success story ... |
| progress | 9 | 9 | exact (100%) | Alternatively, one might try to first sample and fix the graph G based on the execution of the system. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The decisive check is openness, and the paper draws the boundary itself in the one place a draft like this usually overreaches: Section 4.4 (p. 22) says the lower bound extends to update graphs depending on \"the registered identities and the CRS (but not on the keys)\", and nothing in Theorem 4.12, the amortized remark (p. 23), or Appendices A-C closes the key-dependent case - so the draft's residue is exactly the residue the paper leaves. Compared symbol by symbol with Theorem 4.1 and Corollary 4.2 (p. 17), the formal statement reproduces the binomial condition, the success probability rho - sqrt(alpha*ln2/(2l)) - delta, the quantifier order on delta, and the Omega(log n/loglog n) corollary without strengthening or weakening any clause, and the three inlined definitions are the paper's Def. 2.1, Def. 2.2 at k=0, and Def. A.1 with negligible error generalized to 1-rho. The only discrepancies I found are the corollary threshold written rho >= 0.99 where the paper's proof says rho > 0.99 (the arithmetic holds at 0.99 either way) and the background phrase \"Merkle-forest\" where p. 3 says \"Merkle tree\"; neither changes what a proof would have to establish.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 4 | The problem is posed verbatim on p. 4: "Our result leaves it open to either extend our lower bound to RBE schemes with dynamic update times that depend on the public keys or to invent new RBE schemes with dynamic update times that bypass our lower bound." Restated on p. 11 as extending the bound to the standard completeness definition. All five of the draft's quotes match the PDF exactly, on the pages claimed (4, 9, 10, 11). |
| Openness | pass | 22 | Read past the cited passages through the end. Section 4.4 (p. 22) states the boundary explicitly: the bound extends to graphs depending on "the registered identities and the CRS (but not on the keys)". Theorem 4.12 and the amortized remark (p. 23) are the final body results and both stay inside the fixed-graph regime; Appendices A-C are standard definitions, information-theoretic lemmas, and the tightness of Theorem 3.2. The key-dependent case is never resolved. |
| Strength | pass | 17 | The drafted statement is Theorem 4.1's conclusion with exactly one hypothesis removed - the fixed update graph - and replaced by on-demand completeness. That is precisely what the paper means by "extend our lower bound" (p. 4) / "extend our lower bounds to the standard completeness definition" (p. 11). Not a generalization beyond it: it does not touch the CRS/identity-dependence already proved (Thm 4.12), and it does not attempt the separate open problem of closing the 1/loglog n gap, which the draft correctly leaves out of the statement. |
| Quantifiers and parameters | pass | 17 | Clause by clause against Thm 4.1 and Cor. 4.2: binomial n >= C(l+d, d+1) same direction and same indices; alpha as an upper bound on \|pp_i\| over the first n registrations; success probability rho - sqrt(alpha*ln2/(2l)) - delta and advantage rho - 1/2 - ... reproduced exactly; delta = 1/poly(kappa) arbitrarily small, chosen after the scheme; d as max updates per single identity matches deg+(G) as out-degree (edge (i,j) = id_i updated after id_j registers). Cor. 4.2(3) reproduced including the "infinitely many n" reading and the constant depending on the scheme. Sole discrepancy: the corollary's proof assumes rho > 0.99, the draft writes rho >= 0.99; the bound still holds at 0.99 (forces alpha >= 0.69*l, well above the l/10 used), so this is not a defect. |
| Attribution | pass | 4 | The open problem is the harvested paper's own, raised about its own Theorem 1.1/4.1 in the introduction (p. 4) and again after its own definitions (p. 11). Nothing is borrowed from a cited work and presented as this paper's. BH22 is correctly presented as a cited analogy the paper points to, not as a result of this paper. |
| Definitions | pass | 26 | Def. 1 matches Def. 2.1 (p. 11): Reg deterministic with read/write aux, Upd deterministic with read-only aux, Dec deterministic outputting m, bottom, or GetUpd, system initialized pp = aux = bottom. Def. 3 is Def. 2.2 (p. 12) at k=0, an instantiation the paper explicitly sanctions. Def. 2 is Def. A.1 (p. 26) with negligible error generalized to 1-rho, which is what Thm 4.1's "completeness probability rho" must mean, and d(n) is counted exactly as A.1's efficiency clause counts it ("total number of invocations of Upd for identity id* in Step 2(d)"). Draft writes Upd(pp, id*, pk*) where A.1 abbreviates Upd(pp, id*); the three-argument form is the paper's own syntax in Def. 2.1, so this is expansion, not redefinition. |
| Fabrication | pass | 23 | Every attributed claim checks out: iO/CDH-LWE/verifiable constructions with poly(kappa, log n) pp and Theta(log n) updates (p. 3); the failure analysis for key-dependent graphs, both branches, nearly verbatim (p. 9); the BH22 data-dependent memory-hard function analogy (p. 10); Thm 4.12 covering identity names and CRS (pp. 22-23); the amortized version with "at least n/2 of the parties ... at most 2d" (p. 23); 0-corruption being a weaker security notion hence a stronger lower bound (p. 11); Cor. 4.2(1) giving Omega(n^{1/(d+1)}) (p. 17). All four bibliography entries match pp. 24-25 including volume and page numbers. The one flourish not literally in the paper is "Merkle-forest ... each time its tree is merged" where p. 3 says "root of a Merkle tree" whose decommitments go stale - same mechanism, background prose only, absent from the statement. |
| Self-containment | pass | - | Syntax, completeness with on-demand updates, and 0-corruption security are all given inline, and the notation block fixes kappa, n, alpha(n), d(n), l, rho, delta. A reader who has never opened the paper knows exactly what must be constructed (an attacker) and under what hypotheses. The only forward reference is internal (Definition ref:comp), which is supplied. |

## Build

- pdflatex: ok
- chktex: 3 warnings
- lacheck: 0 warnings

## What to check hardest

Two things a reviewer should check hardest. First, the formalisation of "at most d updates" once update times are dynamic: I took the worst case over executions of the on-demand completeness game, counting invocations of Upd for the target identity. The paper does not fix this definition for the dynamic case (its Definition 2.4 is graph-based), so an average-case or with-high-probability variant is defensible; the paper's own amortized extension suggests such variants should also be in scope, and someone attacking the problem should be told which version they are settling. Second, direction: the paper poses this as a disjunction (extend the bound, or construct a scheme that bypasses it) and does not say which it believes; if anything its pointer to data-dependent memory-hard functions hints that the authors consider a bypass plausible, so the conjecture as stated may well be refuted rather than proved, and it should be presented as "prove or refute". Also note the paper phrases this open problem twice (page 4 in terms of dynamic update times, page 11 in terms of the standard completeness definition); I have treated these as one problem, which I believe is right since on-demand updates are exactly key-dependent update times, but a reader who thinks they differ would see two candidates here. Finally, the RBE literature grew substantially after 2022 (registered ABE, pairing- and lattice-based schemes); I am not aware of any follow-up that either removes this hypothesis or exhibits a genuinely key-dependent update schedule, but I have not verified this against the post-2022 literature and someone should.

