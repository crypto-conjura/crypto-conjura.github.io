# Provenance: The Exact Number of Decryption Updates in Compact Registration-Based Encryption

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

`paper-states-open`. For schemes with fixed update times and polylogarithmic public parameters, the number of updates is known to be between Omega(log n / loglog n) (the paper's Corollary 4.2) and O(log n) (all known constructions). Neither endpoint is known to be the truth, and the paper's own combinatorial tool is proved tight, so it cannot decide the question.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 1 | 1 | exact (100%) | As a corollary, we find that RBE systems with fixed update times and public parameters of length poly(log n), require Ω(log n/ loglog n) decryption updates, whi... |
| openness | 4 | 4 | exact (100%) | In addition, it remains open to close the rather small gap of 1/ loglog n factor between our lower bound and the upper bounds of previously constructed RBE sche... |
| openness | 14 | 14 | exact (100%) | This leaves open to close the gap between our lower bound and the upper bound of log n updates for future work. |
| progress | 14 | 14 | exact (100%) | In Section C, we prove that the bounds of this section are tight. This means that our approach of using skipping sequences cannot improve our lower bound of log... |
| parameter | 3 | 3 | exact (100%) | All the RBE schemes so far have the same asymptotic efficiency barriers built into them: they all use the same level of poly(κ, log n) compactness for the publi... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is genuinely the paper's and genuinely open: the gap between Omega(log n/loglog n) and O(log n) for fixed-update-time schemes with poly(kappa, log n) public parameters is flagged open in the paper's own voice on p.4 and again on p.14, and nothing in Section 4.4 or Appendices A-C closes it - Appendix C only proves the skipping-sequence tool tight, which is the draft's stated obstruction, not a resolution. The formal statement matches Corollary 4.2(3) on p.17 clause for clause (fixed kappa, a constant c, infinitely many n, alpha_n as a max over the first n registrations, deg+ restricted to the first n nodes) with log n/loglog n replaced by log n, and the definitions are the paper's, including the non-obvious point that its completeness notion loses on a GetUpd output rather than refetching as standard Def A.1 does. What fails is fabrication: the setting invents a mechanism for the known constructions - a forest of Merkle trees shaped by a binary counter, with openings refreshed at each merge - that the paper never states and that sits against its own description of a single Merkle-tree root on p.3, and the binom(alpha+d, d+1) >= n trade-off is credited to Theorem 4.1 when it is Theorem 1.1.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 4 | The problem is in the paper, twice and in the paper's own voice. p.4: "In addition, it remains open to close the rather small gap of 1/ loglog n factor between our lower bound and the upper bounds of previously constructed RBE schemes." p.14 (Section 3 preamble): "This leaves open to close the gap between our lower bound and the upper bound of log n updates for future work." The two endpoints are also stated on p.1 (abstract: Omega(log n/loglog n), "optimal up to a O(loglog n) factor") and p.3 (all known schemes: poly(kappa, log n) pp with Theta(log n) updates). |
| openness | pass | 14 | It stays open through the whole paper. A full-text grep for openness language returns exactly four open statements (p.4 twice, p.10, p.11, p.14); the gap-closing one is at p.4 and p.14. The later material does not touch it: Section 4.4 (pp.22-23) only extends the same Omega(log n/loglog n) lower bound to CRS/identity-dependent graphs, per-identity update budgets (Thm 4.11, Thm 4.12) and amortized budgets; Appendix A (p.26) gives the standard definitions; Appendix B (p.29) proves the twig lemma; Appendix C (pp.29-30) proves Theorem 3.2 tight, which cuts against closing the gap rather than closing it. The paper contains no construction at all, so the O(log n) side is untouched. |
| strength | pass | 14 | The drafted statement is the tight version of Corollary 4.2(3) (p.17), i.e. exactly the log n endpoint the paper names on p.14 ("the upper bound of log n updates"). Note recorded rather than charged as a failure: the paper poses a two-sided gap ("close the gap"), which a scheme with o(log n) updates would also close, whereas the draft commits to the lower-bound horn. The draft is explicit about this - the informal says a refutation must be "a scheme with a short public parameter that beats log n updates" - and it does not claim the authors predict this direction, so the commitment is disclosed rather than smuggled. It also correctly keeps the fixed-update-graph restriction and does not conflate this with the separate p.4 open problem about dynamic update times. |
| quantifiers-and-parameters | pass | 17 | Checked symbol by symbol against Corollary 4.2(3) (p.17): "If \|alpha_n\| <= poly(kappa, log n) for security parameter kappa, then deg+(G) cannot be o(log n/loglog n). (I.e., there will be a constant c and an infinite sequence of n for which deg+(G) >= c log n/loglog n.)" The draft preserves: kappa fixed (the corollary's proof says "for (fixed kappa and) constant s"), c depending on the scheme/p/kappa, infinitely many n, and the equivalence with "not o(log n)" (which is correct: not o(f) iff exists c>0 with f-ratio >= c infinitely often). alpha(n) = max_{i<=n}\|pp_i\| matches the corollary's alpha_n = max_{i in [n]}\|pp_i\|; deg+(G_n) as max out-degree over [n] with targets restricted to v <= n matches Theorem 4.1's "deg+(G) <= d when we limit the graph G to the first n nodes/identities" (p.17). rho >= 0.99 matches the corollary proof's "complete rho > 0.99". No quantifier is reordered and nothing is allowed to depend on anything the paper forbids. |
| attribution | pass | 4 | This is the harvested paper's own open problem: the p.4 sentence says "our lower bound" and the p.14 sentence says "our lower bound" and "our approach of using skipping sequences". The O(log n) upper-bound side is correctly credited to prior constructions [GHMR18, GHM+19, GV20] rather than to the source paper, matching p.3 and p.4. The bibliography entries for GHMR18, GHM+19 and GV20 match the paper's reference list on p.25 (authors, titles, venues, LNCS volumes 11239/11443/12170, page ranges 689-718 / 63-93 / 621-651); the draft's key "GHM19" for the paper's "GHM+19" is renaming, not redefinition. |
| definitions | pass | 13 | Every notion is the paper's. RBE syntax (deterministic Reg with read/write aux, deterministic Upd with read-only aux, Dec outputting m / bottom / GetUpd) = Def 2.1, p.11. Forward DAG = Def 2.3, p.12. Fixed-update-graph completeness = Def 2.4, p.13, including the load-bearing points that u is overwritten by Upd only when (i,j) in G, that the just-registered identity may be id* itself (footnote 9), and that a GetUpd output loses the game - this is what makes the definition stronger than the standard Def A.1 on p.26, whose step 2(d) refetches u on GetUpd, and the draft does not silently import the standard version. 0-corruption security = Def 2.2 (p.11-12) at k=0, where step 2(a) is unreachable since it requires \|D_c\| < 0, matching the paper's gloss "the adversary is essentially an observer". Skipping sequence, quoted in the setting, matches Def 3.1 (p.15) verbatim in content. rho-completeness as a parameterized version of Def 2.4 matches Theorem 4.1's "completeness probability rho" (p.17). |
| fabrication | fail | 3 | Two unsupported assertions. (i) setting_latex: the known schemes "all commit to the registered keys with a forest of Merkle trees whose shape follows a binary counter, so a party's opening must be refreshed each of the Theta(log n) times its tree is merged." The paper describes a single tree - "the public parameter pp_n in [GHMR18] is the root of a Merkle tree that hashes all the public parameters of the registered identities" (p.3) - and Remark 1.3 (pp.9-10) says only that the first component "always consists of 'subsets' whose sizes determine the update times, while these sizes only depend on the number of identities registered so far." Forest, binary counter and tree merges appear nowhere. (ii) progress_note attributes "the trade-off binom(alpha+d, d+1) >= n" to Theorem 4.1; that inequality is Theorem 1.1 on p.4, while Theorem 4.1 (p.17) states only the attack succeeding with probability rho - sqrt(alpha ln2/(2 ell)) - delta whenever n >= binom(ell+d, d+1), from which the corollary's proof extracts alpha_n >= ell/10, not alpha_n >= ell. Everything else I checked is supported: the skipping-sequence grouping intuition (p.8), Theorem 3.2 (p.15), Theorem C.1 and Lemma C.3 (pp.29-30), Corollary 4.2 items 1 and 3 (p.17), and the Theta(log n)/poly(kappa, log n) profile of known schemes (p.3). |
| self-containment | pass | - | A reader who has never opened the paper could act on the statement: the syntax, the fixed-update-graph completeness game, 0-corruption security, forward DAG, alpha(n) and deg+(G_n) are all spelled out in the draft, and the target inequality deg+(G_n) >= c log n for infinitely many n is unambiguous. No evidence page applies - this check is about the draft's own text. |

### Unsupported by the paper

- setting_latex: "all commit to the registered keys with a forest of Merkle trees whose shape follows a binary counter, so a party's opening must be refreshed each of the Theta(log n) times its tree is merged" - the paper says "root of a Merkle tree" (p.3) and "subsets whose sizes determine the update times" (Remark 1.3, pp.9-10); no forest, binary counter or merging appears anywhere in the paper.
- progress_note: the trade-off binom(alpha+d, d+1) >= n credited to "Theorem 4.1" - that inequality is Theorem 1.1 (p.4); Theorem 4.1 (p.17) states the attack's success probability, and combined with 0-corruption security it gives alpha_n >= ell/10, not alpha_n >= ell.
- setting_latex/progress_note: "binom(alpha+d, d+1) >= Omega(n)" as the paper's stated inequality - the paper's stated form (Theorem 1.1, p.4) is binom(|pp_n|+d, d+1) >= n with |pp_n| non-decreasing in n, a hypothesis the draft drops without saying so (harmlessly, since it uses alpha(n) = max_{i<=n}|pp_i|).

### Corrections the checker asked for

- **setting_latex** — Asserts a construction mechanism the paper does not contain: that [GHMR18], [GHM+19] and [GV20] "all commit to the registered keys with a forest of Merkle trees whose shape follows a binary counter, so a party's opening must be refreshed each of the Theta(log n) times its tree is merged." The paper says the public parameter is the root of a Merkle tree (p.3) and, in Remark 1.3 (pp.9-10), that the data structure consists of subsets whose sizes determine the update times; it never mentions a forest, a binary counter, or merges.
  - suggested: Replace with the paper's own account: in [GHMR18] the public parameter is the root of a Merkle tree hashing the registered public keys, so a party must refresh the opening (decommitment) to its own key as the tree grows, which yields Theta(log n) updates (p.3); Remark 1.3 (pp.9-10) explains that in all known constructions the accumulator consists of subsets whose sizes - and hence the update times - depend only on the number of identities registered so far, which is why all of them have fixed update times.
- **progress_note** — Attributes the trade-off "binom(alpha+d, d+1) >= n" to Theorem 4.1. Theorem 4.1 (p.17) states only that the attack succeeds with probability rho - sqrt(alpha ln 2/(2 ell)) - delta whenever n >= binom(ell+d, d+1) and |pp_i| <= alpha; the clean binomial trade-off is Theorem 1.1 on p.4 (stated as binom(|pp_n|+d, d+1) >= n, with |pp_n| assumed non-decreasing, cf. footnote 5).
  - suggested: The paper states the trade-off binom(|pp_n|+d, d+1) >= n as Theorem 1.1 (p.4, assuming |pp_n| non-decreasing, WLOG by padding); its technical form is Theorem 4.1 (p.17), from which the proof of Corollary 4.2 derives alpha_n >= ell/10 when n = binom(ell+d, d+1) and rho > 0.99. The same wording should be fixed in setting_latex, which writes "binom(alpha+d, d+1) >= Omega(n)".

## Build

- pdflatex: ok
- chktex: 2 warnings
- lacheck: 2 warnings

## What to check hardest

The paper poses this as "close the gap" and does not commit to a side; I chose the lower-bound direction so that there is a definite claim to prove or refute, and a reviewer may reasonably object that the paper's own phrasing is direction-neutral. On the substance, I would bet against the conjecture as stated: replacing the binary-counter Merkle forest of the known constructions by a b-ary counter with b = polylog(n) plausibly gives polylog(kappa, log n) public parameters (the roots of the (b-1) log_b n trees) with only log_b n = O(log n / loglog n) merges affecting any given party, hence O(log n / loglog n) updates, which would meet the paper's bound and refute this statement. That is my own observation, not the paper's, and I have not checked whether the obfuscation- or garbling-based "delayed encryption" layer survives the larger arity with polylogarithmic ciphertexts and update lengths; if it does, the problem is much less hard than the paper's framing suggests, and this candidate should probably be dropped. Relatedly, I have not verified against the substantial post-2022 RBE literature whether such a scheme has already been published; if it has, this is resolved. Finally, note the gap is a loglog n factor, so a reviewer who requires that settling a conjecture change the qualitative state of knowledge may judge this below the bar even though the paper flags it as open twice.

