# Provenance: Tight Security of the Single-Session Lattice Chevallier-Mames Signature

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Tight Lattice-Based Signatures without Trapdoors from Search LWE**
- Authors: Rutchathon Chairattana-Apirom, Nico Döttling, Julian Loss, Stefano Tessaro, Benedikt Wagner
- Venue/archive: Cryptology ePrint Archive; full version of an article to appear at CRYPTO 2026 2026
- Identifier: 2026/953
- Bibliographic detail: inferred
- File: `2026-953.pdf` (37 pages)
- sha256: `c0ec2d2cce7b9791cd227c0d138d18ae2ae842570be7eb6cbd2916ed96b135c4`
- Read on 2026-08-19T00:48:56Z via the `cli` backend

## How the paper leaves it open

`paper-notes-technique-fails`. The paper proves tight strong unforgeability from search Module-LWE for the two-session scheme (its Theorem 4.2, with the two steps proved in Sections 4.4 and 4.5). For the single-session scheme it sketches only a reduction that resamples challenges and therefore loses a factor about $1/\varepsilon$, and states that it does not know how to prove tight security for it. Nothing later in the paper, including the appendix, returns to the single-session case.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 5 | 5 | exact (100%) | We do not know how to prove tight security for this protocol. However, we will now provide a simple modification of this protocol which only leads to a factor 2... |
| openness | 5 | 5 | exact (100%) | While we cannot prove tight security for our lattice-based CM analogue, we can in fact prove security under search LWE using standard forking ideas. |
| definition | 4 | 4 | exact (100%) | Conceptually, this signature scheme is built around (the attempt of) a lattice analogue of a DLOG-equality proof system. |
| progress | 5 | 5 | exact (100%) | Thus, trying to extract a search LWE solution directly using the trapdoor of H seems doomed. |
| parameter | 6 | 6 | exact (100%) | Our modification is conceptually simple: In essence, we run two sessions of the above protocol in parallel. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The problem is real and genuinely open - "We do not know how to prove tight security for this protocol" is verbatim on p. 5, and the single-session scheme is never revisited in Sections 3-4 or Appendix A. But the formal statement is existentially quantified over all parameter functions with no constraint that sMLWE be hard at those parameters, so clause (ii) is satisfiable for free by choosing sigma_sk small enough that a trivial B already has advantage 1/2; Table 1 (p. 20) carries the omitted constraint sigma_sk >= sqrt(n log N) precisely because it "ensures that sMLWE is hard based on worst-case assumptions [LS15]". Compounding this, the draft asks for tight UF-CMA, a notion the paper never defines, where its own Theorem 4.2 target is SUF-CMA (Fig. 1, p. 8) - both defects are precisely repairable, hence corrections rather than an unfaithful verdict.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 4 | The scheme is genuinely in the paper as "Attempt 1: A lattice analogue of CM" (p. 4), given as a six-bullet signing procedure with the two-equation verification of Eq. (1), and the extraction obstruction is developed on p. 5. The draft's SS^1 is a faithful de-parallelization of the paper's Figure 2 (p. 19) scheme. |
| Openness | pass | 5 | "We do not know how to prove tight security for this protocol" (p. 5) and "While we cannot prove tight security for our lattice-based CM analogue" (p. 5). A grep of all 37 pages confirms the single-session case is never mentioned again after p. 6: Sections 3, 4.1-4.5 and Appendix A concern only the two-session SS_R. Nuance: the paper's explicit "What we do not do (or: future work)" list (p. 3) names concrete parameters, QROM, multi-user and standard model, but not this - so it is a recorded limitation of the technique, not a posed open problem. That matches the draft's declared openness_kind. |
| Strength | fail | 8 | The paper defines SUF-CMA and UF-KOA (Fig. 1, p. 8) and never defines UF-CMA; Theorem 4.2 (p. 21) proves tight strong unforgeability for SS_R, and Section 4.3 splits it as SUF-CMA <- UF-KOA + sMLWE. The draft instead invents a UF-CMA game (mu* not in Q) and asks for tightness only there - a strictly weaker target than the paper's own notion for the same scheme family. |
| Quantifiers and parameters | fail | 20 | The statement is existentially quantified over all parameter functions with only cosmetic side conditions (N a power of two, q an odd prime, M >= 1, poly bounds, poly-time computability). Nothing requires sMLWE to be hard at the chosen parameters, so the tightness inequality is satisfiable for free by choosing sigma_sk small: a poly-time B with Adv^smlwe(B) = 1/2 gives Adv^ufcma(A) <= 1 <= 2 Adv^smlwe(B). Table 1 (p. 20) carries exactly the omitted constraint - sigma_sk = max{sqrt(n log N), sqrt(log(2mN(1+1/eps))/pi)}, where "the first ensures that sMLWE is hard based on worst-case assumptions [LS15]" - plus m' >= m + n log_b q, sigma_x = sqrt(2) eta, sigma_y = sigma_x sigma_sk N sqrt(m), sigma_r = alpha gamma_c sigma_sk sqrt(mN), bar-sigma_r = alpha gamma_c sigma_y sqrt(2 m' N), beta_z = sigma_r sqrt(mN), bar-beta_z = bar-sigma_r sqrt(m'N), M = exp(t/alpha + 2/alpha^2), \|C\| >= 2^{2 kappa}, q >= 4 b sigma_td bar-beta_z sqrt(m' m N), and m > n. The draft imposes none of them. The order of quantifiers within (ii) (C_0 and p fixed before A, B depending on A) is correct, and Time(B) <= Time(A) + (Q_S l + Q_1 + Q_2) p(kappa) matches Theorem 4.2's bound. |
| Attribution | pass | 5 | This is the paper's own construction and its own admitted limitation, not something it credits elsewhere. The paper only remarks that "a very similar argument was used, for instance, in recent work [JTWZ26]" about the resampling technique (p. 5); the draft does not present the problem as anyone else's. |
| Definitions | pass | 11 | Search MLWE matches Definition 2.11 (p. 11) exactly: A uniform in R_q^{n x m}, s uniform in R_q^n, e <- D_{R^m,sigma}, win iff s' = s. Challenge set C, Rot(.), the discrete Gaussian normalisation and bar-Sigma = sigma_x^2 Rot(e)Rot(e)^T + sigma_y^2 I_N all match Table 1 and pp. 9-11. One literal divergence not held against the draft: Figure 2's Rej returns 1 with probability min{1, D_sigma(w)/(M D_{v,sigma}(w))} and Sign outputs on NOT-Rej, so the paper's pseudocode literally accepts with the complementary probability; the draft's rule is the one consistent with Lemma 2.10 and with Theorem 4.3's (1 - 1/M^4)^l, so the stray negation is the paper's. |
| Fabrication | fail | 11 | (a) setting_latex claims "hardness of sMLWE for Gaussian secrets and errors of this shape follows from worst-case module lattice problems [LS15]" - the secret is uniform in R_q^n in Definition 2.11 (p. 11) and in the draft's own definition; only the error is Gaussian. (b) setting_latex says the Fiat-Shamir route "followed by Dilithium [LDK22], is proved by rewinding and is not tight"; the paper (p. 2) attributes the non-tight rewinding proof to [Lyu09, Lyu12] and points to lossy identification [AFLT12, KLS18, ABB+17] - KLS18 being Dilithium's proof - for the tight route. The paper never says Dilithium is proved by rewinding. (c) The parameters table claims "the expected number of signing iterations is about M^2"; the paper only ever states 1/M^4 acceptance for the two-session scheme (Theorem 4.3, p. 21). M^2 is the draft's own (correct) arithmetic for its SS^1, not a paper claim. |
| Self-containment | pass | - | Notation, sMLWE, SS^1 and the security game are all spelled out in the draft, so a reader who has never seen the paper knows what object is at stake. The caveat is check 4: what they would be asked to prove is, as written, vacuously achievable. |

### Unsupported by the paper

- setting_latex asserts sMLWE hardness "for Gaussian secrets"; Definition 2.11 (p. 11) and the draft's own definition both sample s uniformly from R_q^n. Only the error is Gaussian.
- setting_latex says Dilithium [LDK22] "is proved by rewinding and is not tight". The paper (p. 2) attributes rewinding to [Lyu09, Lyu12] and lists Dilithium's proof [KLS18] among the tight lossy-identification proofs. The paper makes no such claim about Dilithium.
- The parameters table claims the expected number of signing iterations is "about M^2". The paper never states this; its only figure is 1/M^4 acceptance per iteration for the two-session scheme (Theorem 4.3, p. 21). M^2 is the draft's own arithmetic for its reconstructed SS^1.
- formal_statement_latex implies the paper's tightness target is a single-adversary bound Adv <= C_0 * Adv^smlwe(B) + negl. Theorem 4.2 (p. 21) gives a two-adversary bound Adv^smlwe(B) + Adv^smlwe(B') + delta_negl. This is a legitimate abstraction of "tight" but is not the paper's stated form.
- The claim in status_note that the paper "states that it does not know how to prove tight security for it" is supported (p. 5), but the surrounding implication that the paper poses this as an open problem is not: the paper's explicit "What we do not do (or: future work)" list (p. 3) enumerates four open questions and this is not among them.

### Corrections the checker asked for

- **formal_statement_latex** — The parameters are existentially quantified with no constraint tying them to a hard instance of sMLWE, so clause (ii) is satisfiable by choosing parameters for which sMLWE is easy, and the conjecture is trivially true. The paper's own parameter constraints (Table 1, p. 20) are omitted entirely.
  - suggested: Quantify universally over parameters subject to the paper's Table 1 constraints with the parallel repetition removed: for all n,m,m',N,q,l,gamma_c,M,sigma_sk,sigma_r,bar-sigma_r,sigma_x,sigma_y,beta_z,bar-beta_z with m > n, m' >= m + n log_b q, sigma_sk >= max{sqrt(n log N), sqrt(log(2mN(1+1/eps))/pi)}, eta := (8/sqrt(pi)) q^{n/m} sqrt(N ln(2mN(1+1/eps))), sigma_x = sqrt(2) eta, sigma_y = sigma_x sigma_sk N sqrt(m), sigma_r = alpha gamma_c sigma_sk sqrt(mN), bar-sigma_r = alpha gamma_c sigma_y sqrt(2 m' N), beta_z = sigma_r sqrt(mN), bar-beta_z = bar-sigma_r sqrt(m'N), M = exp(t/alpha + 2/alpha^2) with alpha,t = omega(sqrt(log(mN))), |C| >= 2^{2 kappa}, and q >= 4 b sigma_td bar-beta_z sqrt(m' m N) with sigma_td >= eta - the scheme SS^1 satisfies (i) and (ii). At minimum, sigma_sk >= sqrt(n log N) must be imposed, since that is the condition under which [LS15] makes sMLWE_{n,m,N,q,sigma_sk} hard.
- **formal_statement_latex** — Clause (ii) asks for tight UF-CMA security. The paper never defines UF-CMA; its notions are SUF-CMA and UF-KOA (Fig. 1, p. 8), and Theorem 4.2 (p. 21) proves tight SUF-CMA for the two-session scheme. Asking only for UF-CMA weakens the question relative to what the paper achieves for SS_R.
  - suggested: Replace UF-CMA by SUF-CMA as defined in Figure 1 (p. 8), i.e. the forgery must satisfy (mu*, sigma*) not in Sigs rather than mu* not in Q, and state the target as Adv^{sufcma}_{SS^1}(A,kappa) <= C_0 * Adv^{smlwe}_{n,m,N,q,sigma_sk}(B,kappa) + negl(kappa). (The paper's own bound for SS_R has the two-adversary form Adv^{smlwe}(B) + Adv^{smlwe}(B') + delta_negl, from Lemmas 4.4 and 4.5; C_0 = 2 is the faithful constant.)
- **definitions_latex** — Definition~\ref{def:ufcma} defines a UF-CMA game the paper does not use, and omits the SUF-CMA and UF-KOA games the paper's proof is actually structured around (SUF-CMA <- UF-KOA + sMLWE, Section 4.3).
  - suggested: Give SUF-CMA as in Figure 1 (p. 8): the signing oracle records (mu, sigma) in Sigs, and A wins iff (mu*, sigma*) not in Sigs and Ver(pk, mu*, sigma*) = 1.
- **setting_latex** — "hardness of sMLWE for Gaussian secrets and errors of this shape follows from worst-case module lattice problems [LS15]" - the secret is uniform, not Gaussian, in Definition 2.11 (p. 11) and in the draft's own sMLWE definition.
  - suggested: "hardness of sMLWE for a uniform secret and a Gaussian error of this width follows from worst-case module lattice problems [LS15], provided sigma_sk > sqrt(n) * omega(sqrt(log N))".
- **setting_latex** — "the trapdoor-free Fiat-Shamir route of Lyubashevsky [Lyu12], followed by Dilithium [LDK22], is proved by rewinding and is not tight" attributes a rewinding proof to Dilithium. The paper (p. 2) attributes the non-tight rewinding proof to [Lyu09, Lyu12] and points to lossy identification [AFLT12, KLS18, ABB+17] for the tight route, KLS18 being Dilithium's proof.
  - suggested: "the trapdoor-free Fiat-Shamir route of Lyubashevsky [Lyu09, Lyu12] is proved by rewinding and is not amenable to a tight reduction to SIS; tight proofs for Fiat-Shamir lattice signatures, including Dilithium's [KLS18], instead go through lossy identification and therefore rely on decisional LWE."
- **parameters** — The entry for M asserts "the expected number of signing iterations is about M^2". This is the draft's own derivation for its two-factor SS^1; the paper only states 1/M^4 acceptance (Theorem 4.3, p. 21) for the four-factor two-session scheme.
  - suggested: "Rejection sampling parameter, M = exp(t/alpha + 2/alpha^2); for SS^1 the per-iteration acceptance probability is 1/M^2, so the expected number of signing iterations is about M^2 (the paper's two-session scheme has 1/M^4)."

## Build

- pdflatex: ok
- chktex: 8 warnings
- lacheck: 1 warnings

## What to check hardest

The sentence the paper leaves this open with refers to "this protocol", meaning the overview-level Attempt 1 on page 4, which omits the rejection sampling and all parameter choices. I have instantiated it as the one-session specialisation of the fully specified scheme in Figure 2, which is the faithful reading (the overview says the missing details are a routine modification), but a reader should check that specialisation against Figure 2 on page 19. Two further deliberate choices: I state ordinary unforgeability rather than the strong unforgeability the paper proves for the two-session scheme, since the paper's obstruction lives entirely in the key-only extraction step and stating the weaker notion keeps the conjecture at the paper's strength; and I do not require a polynomial modulus, which the paper does achieve for the two-session scheme, since it is not part of what the paper says is open. The formulation "there exists a reduction with constant loss" is the standard theorem shape in this literature and is not formalised by the paper itself; anyone attacking the negative direction will need to fix a meta-reduction model. Finally, I could not check whether follow-up work has since settled this; the paper is dated 2026 and I have only the paper's own reference list.

