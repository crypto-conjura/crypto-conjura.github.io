# Provenance: Asymptotically Optimal Gap Finders for Boolean-Terminal Martingales

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Polynomial-time targeted attacks on coin tossing for any number of corruptions**
- Authors: Omid Etesami, Ji Gao, Saeed Mahloujifar, Mohammad Mahmoody
- Venue/archive: Full version of a paper appearing in the Theory of Cryptography Conference (TCC) 2021 2021
- Identifier: Cryptology ePrint Archive 2021/1464 (identifier taken from the file name, not printed on the page)
- Bibliographic detail: printed-on-page
- File: `2021-1464.pdf` (50 pages)
- sha256: `c863025078557985cbfbf65e30c568fdf1dbe806a2c86f2d2bc38b5fb0daec5e`
- Read on 2026-08-17T19:53:59Z via the `cli` backend

## How the paper leaves it open

`paper-asks-question`. Settled for $\mu = \Theta(1)$: the Cleve--Impagliazzo gap finder already gives $\rho\alpha = \Omega(\mu^2/\sqrt{n}) = \Omega(\mu/\sqrt{n})$ when $\mu$ is bounded away from $0$. Open in the small-$\mu$ regime, where the known bound is a factor $\mu$ short; the paper states it does not know the answer for general $\mu \le 1/2$.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 45 | 45 | exact (100%) | Then, can one always obtain an (ρ, α) gap finder for w≤n such that ρα = Ω(µ/ n)? |
| openness | 45 | 45 | exact (100%) | This motivates the following question, which as far as we know is open. |
| openness | 45 | 45 | exact (100%) | Unfortunately, the bound of the (ρ, α) gap finder of [CI93] degrades with µ, which means we cannot use their result to obtain an asymptotically similar result t... |
| definition | 45 | 45 | exact (100%) | Namely, with probability at least ρ, the stop time chosen by Stop shows a jump of at least α. |
| parameter | 45 | 45 | exact (100%) | We do not know how to find (expected) α gap finders for this purpose. This means we cannot use the result of [KMM19] (see Theorem 52). |
| progress | 45 | 45 | exact (100%) | A positive answer to the following question above would have allowed us to use the derived targeted attack instead of our Lemma 47 and obtain (information-theor... |
| progress | 44 | 44 | exact (100%) | Note that, their result is only proved for almost unbiased final bits in which both {0, 1} happen with probability Ω(1). |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open question exists verbatim on p.45, is declared open by the paper itself (\"which as far as we know is open\"), is never revisited through the end of Appendix C on p.50, and the drafted inequality, quantifier order and both restated definitions match the paper symbol for symbol — including the point that the constant must be µ-independent, which is precisely the paper's complaint about [CI93]. The single most important defect is the motivation: the draft claims gap-finder quality is \"the only missing ingredient in a fully modular derivation of the paper's main theorem\", while p.4 says the entire Appendix-C observation is \"merely for sake of completeness\" and \"subsumed by our main result of Theorem 1\", and p.45 promises only information-theoretic k-replacing attacks by a recursive composition that Remark 46 (p.42) says is super-polynomial for k = ω(1). Together with the draft's conversion of the paper's \"we do not know how\" about [KMM19] into a flat impossibility, these are prose-level errors I can state and repair exactly, leaving the posed problem itself intact.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 45 | The problem is posed verbatim under its own heading: "Open question about asymptotically optimal (ρ, α) gap finders. Let w≤n be an n-step Martingale such that E[w1] = µ ≤ 0.5. Then, can one always obtain an (ρ, α) gap finder for w≤n such that ρα = Ω(µ/√n)?" The draft's title, subtitle and one_line track this heading and question. |
| Openness | pass | 45 | The paper marks it open in its own words: "This motivates the following question, which as far as we know is open." I read past it: Appendix C continues with Theorem 53, Constructions 54/55, Claims 56-59 and Theorem 60 and ends at p.50 without returning to it, and the reference index confirms [CI93] is cited only on pp. 4, 5, 44, 45 and [KMM19] only through p. 45, so no later section, appendix or theorem touches the gap-finder bound again. Nothing in the paper improves on the Ω(µ²/√n) product. |
| Strength | pass | 45 | Clause by clause the drafted inequality ρ·α ≥ cµ/√n over all n, all µ ≤ 1/2 and all such martingales is the paper's question, neither strengthened nor weakened. One deviation: the draft adds the hypothesis Pr[w_n ∈ {0,1}] = 1, which the open question's literal text omits. This is the intended class, not a weakening for the draft's convenience — the literal text has a trivial counterexample (the constant martingale w_i ≡ µ admits no jump at all, so ρα = 0), and p.44 states the governing hypothesis explicitly: "for any n-step martingale in which the final value is in {0, 1}". I do not charge this. |
| Quantifiers and parameters | pass | 45 | Order matches: n, µ and the martingale are universally quantified, then α and Stop existentially. The draft's insistence that c be "independent of n, of µ, and of the martingale" is exactly what the paper's Ω(µ/√n) must mean here, since the entire complaint on p.45 is that "the bound of the (ρ, α) gap finder of [CI93] degrades with µ" — a µ-dependent constant would make the question vacuous. µ ≤ 0.5 rendered as µ ∈ (0,1/2]; dropping µ = 0 is harmless (the claim is 0 ≥ 0 there). Information-theoretic, no running-time bound: correct, efficiency enters only later in Theorem 60 (p.50). |
| Attribution | pass | 45 | The question is the harvested paper's own ("as far as we know is open", first-person motivation referring to "our Lemma 47"), and the draft presents it that way while correctly attributing the (Ω(µ), Ω(µ/√n)) gap finder it seeks to improve to [CI93] and the expected-gap bound to [KMM19] (Theorem 52). Bibliography entries for CI93, KMM19, KMW21 and BOL90 all match the paper's own reference list (pp. 47-49 of the reference section), and the harvested paper is indeed Etesami-Gao-Mahloujifar-Mahmoody, TCC 2021 full version (p.1). |
| Definitions | pass | 45 | Definition 50 (online stopping: Boolean output, monotone, StopTime = n+1 if never) and Definition 51 ((ρ,α) gap finder: Pr[\|w_τ − w_{τ−1}\| ≥ α] ≥ ρ, with w₀ = E[w₁] and w_{n+1} = w_n) are restated faithfully, including the distinction from the expected-gap "α gap finder". The paper never defines "martingale" itself — Definition 6 (p.11) defines only the Doob martingale — so the draft supplies the standard conditional-expectation definition; that is consistent with the paper's usage and is not a silent swap. |
| Fabrication | fail | 4 | Three unsupported assertions. (i) Setting and informal claim the KMM19 expected-gap form "cannot be plugged into the targeted reduction at all" / "is not usable"; p.45 says only "We do not know how to find (expected) α gap finders for this purpose." (ii) "That makes the quality of gap finders the only missing ingredient in a fully modular derivation of the paper's main theorem" is contradicted on p.4: "this observation is merely for sake of completeness, and the results obtained this way are subsumed by our main result of Theorem 1" — and the route cannot reach Theorem 1 in any case, since p.45 says a positive answer would yield "(information-theoretic) k-replacing attacks through recursive compositing", which Remark 46 (p.42) states is super-polynomial for k = ω(1) while Theorem 1 is polynomial-time. (iii) "the classical rule is essentially the best possible" asserts an optimality the paper never proves; p.45 says only that the first part of Theorem 52 implies the second when µ = Ω(1). |
| Self-containment | pass | 45 | The formal statement plus the two restated definitions and the notation block give a reader who has never opened the paper everything needed: what a martingale is, how it is extended at both ends, what an online stopping algorithm may and may not see, what (ρ,α) means, and the exact inequality to establish. Verified against Definitions 50-51 and the open-question paragraph, all on p.45. |

### Unsupported by the paper

- Setting and informal assert that the expected-gap form of [KMM19] "cannot be plugged into the targeted reduction at all" / "is not usable" for targeted attacks. The paper (p.45) claims only ignorance: "We do not know how to find (expected) α gap finders for this purpose." An impossibility is asserted where the paper records a gap in its own knowledge.
- Setting: "That makes the quality of gap finders the only missing ingredient in a fully modular derivation of the paper's main theorem." Contradicted by p.4 ("merely for sake of completeness, and the results obtained this way are subsumed by our main result of Theorem 1") and unreachable in principle, since p.45 promises only information-theoretic k-replacing attacks by recursive composition, which Remark 46 (p.42) says is super-polynomial for k = ω(1) whereas Theorem 1 is polynomial-time.
- Informal: "When the output is nearly unbiased, the classical rule is essentially the best possible." The paper establishes no upper bound on ρα for gap finders and never asserts optimality of the Cleve-Impagliazzo rule; it says only that the first part of Theorem 52 implies the second when µ = Ω(1) (p.45).
- Progress note: "which shows the target product is not larger than what an attack can already extract by other means." Lemma 47 (p.42) bounds an attack's bias, not any gap finder's ρα; the paper never states that the bias bound bounds the achievable product. The intended inference (Lemma 47 already achieves bias Ω(µ/√n), so the target is not out of reach as a bias) is supported by p.45, but the claim as written about "the target product" is not.

### Corrections the checker asked for

- **setting_latex / informal** — Asserts that the expected-gap ("α gap finder") form of [KMM19] "cannot be plugged into the targeted reduction at all" and "is not usable for attacks that must push the output in one chosen direction". The paper claims no such impossibility; on p.45 it says only "We do not know how to find (expected) α gap finders for this purpose. This means we cannot use the result of [KMM19] (see Theorem 52)."
  - suggested: The paper does not know how to use the expected-gap form of [KMM19] for its targeted reduction, so that route is unavailable to it; it does not show the form is unusable in principle.
- **setting_latex** — "That makes the quality of gap finders the only missing ingredient in a fully modular derivation of the paper's main theorem." The paper's main theorem (Theorem 1) is a polynomial-time k-replacing attack and is already proved without gap finders; p.4 calls the whole Appendix-C observation "merely for sake of completeness" and says "the results obtained this way are subsumed by our main result of Theorem 1", and the recursive route is super-polynomial for k = ω(1) (Remark 46, p.42), so it could not yield Theorem 1.
  - suggested: A positive answer would have let the paper use the gap-finder-derived targeted attack in place of its Lemma 47 and obtain information-theoretic k-replacing attacks by the recursive composition of Section B (p.45); the paper stresses that this route is included for completeness and that its results are subsumed by Theorem 1 (p.4).
- **informal** — "When the output is nearly unbiased, the classical rule is essentially the best possible." The paper proves no upper bound on the achievable ρα, so no optimality of the Cleve-Impagliazzo rule is established anywhere.
  - suggested: When µ = Θ(1) the classical rule already meets the conjectured target, since Ω(µ²/√n) = Ω(µ/√n) there — the paper's remark that "the first part implies the second part when µ = Ω(1)" (p.45). The paper does not prove this is optimal.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `EGMM21` — Omid Etesami, Ji Gao, Saeed Mahloujifar, and Mohammad Mahmoody, *Polynomial-time targeted attacks on coin tossing for any number of corruptions*, Theory of Cryptography Conference (TCC); full version 2021

## Build

- pdflatex: ok
- chktex: 9 warnings
- lacheck: 1 warnings

## What to check hardest

(1) The printed question omits the hypothesis that the martingale's final value lies in $\{0,1\}$; taken literally it is false, since a martingale constant at $\mu$ has no gaps at all. I have restored that hypothesis, which the surrounding text forces --- the appendix opens by describing the Cleve--Impagliazzo theorem as being about ``any $n$-step martingale in which the final value is in $\{0,1\}$'', and the reduction it feeds uses the Doob martingale of a Boolean function. A reviewer should confirm this is the right repair and not, say, a $[0,1]$-boundedness hypothesis instead. (2) The heading calls the target ``asymptotically optimal'', which suggests a matching $\rho\alpha = O(\mu/\sqrt{n})$ upper bound, but I did not find such an upper bound proved or cited anywhere in the paper; the conjecture as stated does not depend on it. (3) I read ``can one always obtain an $(\rho,\alpha)$ gap finder \dots such that $\rho\alpha = \Omega(\mu/\sqrt{n})$'' as existential in the pair $(\rho,\alpha)$, uniformly over $n$, $\mu$ and the martingale; a reader could instead read $\rho$ or $\alpha$ as pinned down in advance. (4) The Khorasgani--Maji line of work on estimating martingale gaps was active around and after 2021; I have not checked whether a later paper in that line settles this, and it is the first place to look.

