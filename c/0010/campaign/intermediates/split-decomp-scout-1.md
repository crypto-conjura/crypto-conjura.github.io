# split-decomp-scout-1 — first prior-art pass on the campaign's three unconditional results

**Artifact:** `split-decomp-scout-1` (scout pass, prior-art / novelty only; no proof attempted)
**Role:** §3.1 Scout. Inputs: `CONTRACT.md`, `intermediates/split-decomp-kappa-2-r3.md` §§5,6,8, `sources/S1-cdgs-card.md`, `sources/S2-cfhs-card.md`, `PROGRESS.md`
**Date:** 27 August 2026. This is the **first** prior-art record the campaign has ever had (`PROGRESS.md` §3: "No scout pass, ever").
**Verdict in one line:** (1) Theorem D / Cor D′ — NO PRIOR ART FOUND for the statement, but its engine is **textbook** and the gap to it is short; (2) Theorems A⁺/B⁺ — NO PRIOR ART FOUND, same engine caveat; (3) Proposition F — **FOLKLORE**, in a form that is classical statistics rather than crypto.

---

## 0. Harness note (BLOCKED)

`HARNESS.md` does not exist anywhere in this repository, and no `contract-d*.md` exists for this
campaign; nor did `proofs/` exist before this file. [BLOCKED — HARNESS.md §3.1, §2, §2.1 could
not be read] I have therefore followed the task brief literally and adopted the campaign's own
artifact conventions (`intermediates/`-style id, gap register, `### END OF ARTIFACT ###` footer)
and produced a four-line header of my own design. The mandatory section E and the terminal
SOURCE REQUEST block are supplied.

**Citation tags used.** `[READ]` = I opened the primary source and read the quoted text.
`[RESTATED]` = the statement reached me through a secondary source or a search snippet and I did
not verify it in the primary. `[BLOCKED]` = I could not obtain it. `[MEMORY]` = recalled, not
verified. Nothing below is tagged `[READ]` unless I actually rendered the page.

---

## A. What was searched

Roughly twenty-five distinct queries plus eight primary-source reads. Search axes, each run:

1. Multi-source / two-source extraction where the sources have oracle access to the extractor's
   own random oracle (the unusual feature).
2. Random oracles with auxiliary input / non-uniformity: Unruh, DGK, CDGS, Guo–Li–Liu–Zhang, and
   anything on presampling or bit-fixing beyond a **single** preprocessing stage.
3. Rectangle-discrepancy / probabilistic-method two-source-extractor arguments of shape
   √(deficiency · δ), especially with a union bound over **all** boolean tests on `[M]` costing
   `M` rather than the leakage length.
4. Lower bounds showing a random function is a poor extractor when `M` is large relative to the
   source support — shape `δ√M` or `√M / N`; balls-in-bins / birthday / occupancy territory.
5. Running CDGS or Unruh decomposition across several parties reading the oracle independently.
6. Forward citations of both known papers.

**Primary sources read in full or in part** (all `[READ]`):

- Coretti–Farshim–Harasser–Southern, *Multi-Source Randomness Extraction and Generation in the
  Random-Oracle Model*, ITC 2025, LIPIcs 343 art. 10 — pp. 10:1–10:6, 10:12–10:20.
- Vadhan, *Pseudorandomness*, Foundations and Trends in TCS 7(1–3), Ch. 6 "Randomness
  Extractors" — pp. 170–178.
- Radhakrishnan–Ta-Shma, *Bounds for Dispersers, Extractors, and Depth-Two Superconcentrators*,
  SIAM J. Discrete Math. 13(1):2–24, 2000 — pp. 2–4.
- Chattopadhyay, *A Recipe for Constructing Two-Source Extractors*, SIGACT News Complexity
  Theory Column, June 2020 — pp. 1–4.
- Chung–Vadhan, *Tight Bounds for Hashing Block Sources*, RANDOM 2008 — pp. 1–4.
- ePrint 2025/1258 abstract page (CFHS full version); ePrint 2026/854 abstract page;
  ePrint 2026/066 abstract page.

**Forward-citation sweeps.**
- CDGS (`10.1007/978-3-319-78381-9_9`): 88 citing papers retrieved from the Semantic Scholar
  graph API [READ, machine-retrieved]. Every one is time–space tradeoffs, function inversion,
  presampling for quantum advice, PIR/data-structure preprocessing, indifferentiability, or
  unrelated. **None** is about multi-source extraction or multi-party preprocessing. The only
  extraction-adjacent citer is CFHS itself; the only "several stages" citer is Dodis–Jain–Lin–
  Luo–Wichs (below), which is a *simulation* result for the single-stage AI-ROM.
- CFHS (`10.4230/LIPIcs.ITC.2025.10`): the Semantic Scholar citations endpoint returns
  `{"offset":0,"data":[]}` — **zero** forward citations [READ]. The ePrint record shows a single
  version, received 2025-07-08 [READ]. Nothing has since proved any of the three results.

**Adjacent literature located and ruled out** (all checked against the three statements):

| work | why it is not prior art |
|---|---|
| Unruh, CRYPTO 2007; DGK, EUROCRYPT 2017; CDGS, EUROCRYPT 2018 | Single preprocessing stage. Presampling replaces an oracle with `S` bits of advice by a `P`-bit-fixing oracle at cost `O(√(ST/P))` (Unruh) or `O(ST/P)` (CDGS) [RESTATED from search snippets and from CFHS §1.4 which I read]. No version with advice produced by several independent parties was found by any query. |
| Guo–Li–Liu–Zhang, *Unifying Presampling via Concentration Bounds*, TCC 2021 (ePrint 2020/1589) — real, verified title/venue/authors [RESTATED, abstract only] | Still one preprocessing stage; generalises presampling to AI-PRM and post-quantum. |
| Dodis–Jain–Lin–Luo–Wichs, *How to Simulate Random Oracles with Auxiliary Input*, FOCS 2024 (ePrint 2026/854) [READ, abstract page] | Efficient *simulation* of the single-stage AI-ROM. The abstract page confirms no mention of multi-source extraction, multiple independent preprocessing parties, or split sources. |
| Dodis–Vaikuntanathan–Wichs, *Extracting Randomness from Extractor-Dependent Sources* (ePrint 2019/1339, EUROCRYPT 2020) | Single source, seeded, **computational**; the source queries the extractor as a black box. Does not give a statistical bound, does not use splitness. |
| Freitag–Silbak–Wichs, *Seedless Condensers for Efficiently Samplable Sources*, TCC 2025 (ePrint 2025/1783) [RESTATED, abstract] | Single source, computational assumptions, and only **condensing** — its own framing is that statistical extraction is impossible without independence. Confirms rather than pre-empts the need for splitness. |
| Dodis–Ristenpart–Vadhan, *Randomness Condensers for Efficiently Samplable, Seed-Dependent Sources*, TCC 2012 | Seed-dependent single source, efficiently samplable, condensing. Different object. |
| Aggarwal–Li–Mukherjee–Obremski–Ribeiro, ePrint 2026/066, *Complete Characterization of Randomness Extraction from DAG-Correlated Sources* [READ, abstract] | Explicitly **not** in the random-oracle model; correlations are causal/graph-structured, not oracle-mediated. |
| UCE (Bellare–Hoang–Keelveedhi, CRYPTO 2013) and its "split source" notions | Terminology collision only. There "split" means the source is cut into a query-making part and a leakage-producing part; it is a computational hash-key assumption, not two independent sources extracting from a shared oracle. |
| Chung–Vadhan, RANDOM 2008 [READ] | Lower bounds are **worst-case-over-sources** ("there exists a block source … for `H` coming from any hash family"), not average-over-`f` for a fixed full-support source. See §D. |

---

## B. Result (1): Theorem D / Corollary D′ — the `q`-free bound

> `κ(q) ≤ 5√(σ'δ) + 2δ√M` for every challenge-oblivious observer of any query count, bounded or
> unbounded, and any challenge resolution.

### Verdict: **NO PRIOR ART FOUND** for the statement. But the machine that proves it is textbook, and I rate the derivation gap as short. Confidence: high on the negative, high on the caveat.

**The negative result is unusually well-evidenced, because the target paper says so itself.**
The CFHS abstract, read verbatim from the ePrint record, closes with: *"Our work opens up a rich
set of problems, ranging from **statistical multi-source extraction with respect to unbounded
distinguishers** to novel decomposition techniques (Unruh, CRYPTO'07; Coretti et al.,
EUROCRYPT'18) and multi-source extraction for non-monolithic constructions."* [READ]. The ITC
version, p. 10:4, is sharper still: their Figure 1 taxonomy labels notions by an `SDP` string
(Source / Distinguisher / Predictor, each B or U), their positive results are Theorem 19 (BBB)
and Theorem 23 (UBU), and the text states *"Finding efficient constructions when the
distinguisher is unbounded (i.e., for UUU and BUU) is left for future work."* [READ]. The
Contract's setting is exactly UBU with the distinguisher's budget removed, i.e. UUU. Theorem D
is a positive result in the corner CFHS declares open, and CFHS has zero forward citations.

**But the engine is Vadhan's Proposition 6.12, essentially verbatim.** *Pseudorandomness*, Ch. 6,
p. 175 [READ]:

> **Proposition 6.12.** For every `n, k, m ∈ ℕ`, every `ε > 0`, and every flat `k`-source `X`, if
> we choose a random function `Ext : {0,1}^n → {0,1}^m` with `m = k − 2log(1/ε) − O(1)`, then
> `Ext(X)` will be `ε`-close to `U_m` with probability `1 − 2^{−Ω(Kε²)}`, where `K = 2^k`.

and its proof, also p. 175 [READ]:

> *Proof.* Choose our extractor randomly. We want it to have following property: for all
> `T ⊂ [M]`, `|Pr[Ext(X) ∈ T] − Pr[U_m ∈ T]| ≤ ε`. … For each point `x ∈ Supp(X)`, the
> probability that `Ext(x) ∈ T` is `μ(T)`, and these events are independent. By the Chernoff
> Bound … for each fixed `T`, this condition holds with probability at least `1 − 2^{−Ω(Kε²)}`.
> Then the probability that condition is violated for at least one `T` is at most
> `2^M 2^{−Ω(Kε²)}`, which is less than 1 for `m = k − 2log(1/ε) − O(1)`.

Every structural feature the artifact's §4 presents as its Idea 2 is present here: the
concentration bound on the flat source's support; the union bound over **all** `2^M` subsets of
the output alphabet, paying `M`; and — decisively — the fact that the good event is quantified
"for all `T`" and is therefore a property of `Ext` alone, so an `Ext`-dependent test may be
substituted afterwards. The artifact's §4 remark *"The quantifier order is the mechanism"* is
a restatement of the shape of Proposition 6.12.

Two further pages line up point for point:

- p. 176 [READ]: *"the number of flat `k`-sources is `binom(N,K) ≈ N^K`, which is unfortunately a
  larger double-exponential in `k`. We can overcome this gap by allowing the extractor to be
  'slightly' probabilistic, i.e., allowing the extractor a seed…"* This is precisely the
  artifact's §4 paragraph *"Where one source would break this"*, and the reason a **second**
  source (equivalently, a rectangle rather than an arbitrary flat set) is what makes the counting
  work.
- Theorem 6.14 and its proof, pp. 176–177 [READ]: the counting `binom(N,K) ≤ (Ne/K)^K` and the
  resulting condition `Dε² ≥ c·log(Ne/K) + c'`. Replace the seed's `D = 2^d` by the second
  source's support size `k₂` and add the `M` from Proposition 6.12's inner union bound, and one
  obtains exactly the artifact's
  `t_c(k₁,k₂)² = (k₁ ln(eN/k₁) + k₂ ln(eN/k₂) + c) / (2k₁k₂)` with `c = M ln 2 + ln(4N²/γ₀)`.
  **The artifact's Lemma B is the two-source analogue of Theorem 6.14, assembled by the recipe on
  pp. 176–177.**
- §6.2.1, p. 178 [READ]: *"Proposition 6.12 says that for any subset `S ⊂ [N]` of size `K`, if we
  choose a completely random hash function `h : [N] → [M]` for `M ≪ K`, then `h` will map the
  elements of `S` almost-uniformly to `[M]`. Equivalently, if we let `H` be distributed uniformly
  over all functions `h : [N] → [M]` and `X` be uniform on the set `S`, then `(H, H(X))` is
  statistically close to `(H, U_[M])`."* — This is the campaign's own setting with the observer
  allowed to read all of `H`.

The two-source existence result itself is classical: Chattopadhyay's survey, p. 2 [READ], *"A
simple probabilistic argument shows the existence of 2-source extractors for min-entropy
`k = log n + O(1)`"*, with the notion attributed to Chor–Goldreich [CG88]. Chor and Goldreich's
own paper (FOCS 1985 / SICOMP 1988) is described as showing that *"most functions can be used to
extract almost unbiased and independent bits from the output of any two independent
probability-bounded sources"* [RESTATED — I did not open CG88 itself; the paraphrase is from a
search snippet and I flag it as unverified].

**So what is left that is genuinely not in the literature?** Two things, and I judge both real:

- **(i) The oracle-dependence step.** The classical good event is a property of `f` alone. The
  campaign's Lemma 1 (posterior of `x` factorises given `(H, z)`, because splitness makes the
  coins independent) is what converts that into a statement about sources that *read `f`*. This is
  exactly the move CFHS could not make with compression, and it is the reason the compression
  route needed `q_D` at all. I found no paper making it. Note that CFHS's Theorem 23 bound,
  `O(ℓ log M · ((q_D/2^{kℓ})(σ + ℓN))^{1/(ℓ+1)})` [READ, p. 10:16], (a) vanishes at `q_D = 0`,
  which their own card-recorded caveat concedes is wrong for the query-free advantage, (b) carries
  `N` rather than `log N`, and (c) degrades in `q_D`. Corollary D′ dominates it wherever
  `2δ√M ≲ 1`, and holds at `q = ∞`.
- **(ii) The Cauchy–Schwarz second-moment step (Lemma A(a)).** `E[√(m₁m₂)] ≤ √(E m₁)√(E m₂) ≤ δ`
  turns the classical `√(Mδ)` into `δ√M`. Running Lemma B through the naive concavity step gives
  `√(Mδ)`, which the artifact itself says "would enlarge nothing". I found no prior instance of
  this refinement, and it is not available in the single-source classical setting, where there is
  only one `m`. It is *specific to two split sources*.

**Novelty risk I am obliged to record.** A referee who knows Vadhan Ch. 6 can reconstruct
Theorem D up to constants in perhaps a page: take Theorem 6.14's two-source analogue, note the
good event is `f`-only, flatten the posterior with Lemma 6.10, and average. The campaign's own
value-add over that page is the `δ√M`-vs-`√(Mδ)` sharpening and the explicit constants. That is
real but it is **not** "a new technique"; it is "the classical existence proof, correctly aimed at
an oracle-dependent source". The write-up currently presents Lemma B as a new idea ("Idea 2") with
no citation into the extractor literature at all — §10's external-results register lists only
`[CFHS, Lemma 3]`, `[CFHS, Lemma 4.3]`, Hoeffding and four standard inequalities. **That is a
citation gap, not a mathematical one, but it is the kind that gets a paper rejected.**

**What would change my verdict.** (a) Any paper stating a two-source-extractor bound *for sources
that depend on the extractor* — I searched hard and found none, but Chor–Goldreich's own SICOMP
paper is the one primary source in this chain I did not open, and it is where such a remark would
most plausibly hide. (b) A version of CFHS §6 or its full version containing a UUU positive
result — the ITC version explicitly does not, and the full version has one dated version and no
citations.

---

## C. Result (2): Theorems A⁺ / B⁺ — the revealing-rule arm

> `κ(q) ≤ √(2δ ln(eN)) + 4δ√(σ') + μ'(min(qM, N²))`, `μ'(s) = min(sδ, 2(sδ²)^{1/3}, 1)`.

### Verdict: **NO PRIOR ART FOUND**. Confidence: high, but this result is the least likely of the three to be independently interesting, and my search for it was necessarily less targeted.

Nothing in the extractor literature has a "revealing rule" of this kind, because in the classical
setting the test is fixed in advance and there is nothing to reveal. The `μ'` machinery exists
only because a `q`-query observer's test `θ_{ζ,f}` depends on `f` through `q·M'` inspected cells;
that is an artefact of the oracle model and I found no analogue. Searches on "leakage-resilient
extractors", "two-source extractors for leaky sources", "two-seed extractors" (Aggarwal et al.,
CRYPTO 2020) returned objects where the leakage is a function of the *sources*, not of the
extractor, and where nothing plays the role of `min(qM, N²)`.

Three caveats, stated plainly:

1. **The shape `√(σ' q⁺ δ)` is not novel and should not be claimed as such.** It is the standard
   AI-ROM optimisation: CDGS's `ST/P + Pδ` optimised at `P = √(ST/δ)` gives `2√(STδ)` with
   `S = σ'`, `T = q⁺`. The Contract itself frames the conjecture in that shape, so this is
   expected rather than a finding — but a reader unfamiliar with presampling might mistake the
   shape for a contribution.
2. **Theorems A⁺/B⁺ inherit r3's Lemma 3 steps (1)–(3) and Lemma 4 unaudited**, as the artifact's
   §9 gap register records. My pass does not change that; I checked novelty, not correctness.
3. **The whole arm is superseded in the applications.** The artifact's §6 "Which arm wins" shows
   the `2δ√M` arm dominates for every `q ≥ 1`, `M ≥ 4`, `2δ√M < 1`, and `PROGRESS.md` §2.2 records
   that applications have full resolution `M`. So (2)'s novelty matters less than (1)'s.

**What would change my verdict.** A paper on extraction in the bit-fixing or AI-ROM model that
bounds "the mass the adversary's inspected cells can carry" by a `(sδ²)^{1/3}`-type quantity. The
exponent `1/3` is characteristic enough that I would expect a search to find it; none did.

---

## D. Result (3): Proposition F — the lower bound

> With both sources uniform on `[N]`, no leakage, `δ = 1/N` exactly, there is an `N²`-query
> resolution-1 observer with advantage `≥ δ√M/(4√2)`.

### Verdict: **FOLKLORE.** The mathematical content is classical, and I can say where it is written down — but *not* in the crypto literature, and *not* as a statement about extraction. Confidence: high that it is folklore; medium on exactly which citation a referee would demand.

Strip the packaging and Proposition F is: for a uniformly random `f : [n] → [M]` with `n = N²`,
the image measure `ν(v) = |f^{−1}(v)|/n` satisfies
`E_f[SD(ν, U_M)] = (M/2n)·E|Bin(n,1/M) − n/M| = Θ(√(M/n))`.

**Where the pieces are written down.**

- *The upper bound* is the leftover hash lemma. The family of **all** functions `[n] → [M]` is
  pairwise independent, hence 2-universal, so LHL gives `E_f[SD] ≤ ½√(M/2^k) = ½·δ√M` at
  `k = log n = 2 log N`. Vadhan §6.2.1, p. 178 [READ], states exactly this reading:
  `(H, H(X))` is statistically close to `(H, U_[M])` for `M ≪ K`. So Corollary D′'s `2δ√M` and
  Proposition F's `δ√M/(4√2)` bracket the LHL constant `½` from both sides, and the artifact's
  claimed factor-`8√2` tightness is really "the LHL is tight for the family of all functions".
- *The mean absolute deviation of the binomial* has a closed form due to **De Moivre**, and
  `E|X − np| ≍ √(np(1−p))`; this is classical and there is a modern literature on sharp
  non-asymptotic versions [RESTATED — Diaconis–Zabell, *Closed Form Summation for Classical
  Distributions: Variations on a Theme of De Moivre*, Statistical Science 6(3), 1991, appears in
  search results with matching title/venue/year, but I did not open it and do not vouch for a
  specific numbered result in it]. The artifact's own step (4) — the fourth-moment/Hölder argument
  giving `E|Y| ≥ s/2` for `s ≥ 1` — is a self-contained substitute and is arguably cleaner than
  citing De Moivre, since it needs no exact formula.
- *The expected total-variation distance of a multinomial histogram from uniform* is computed
  exactly and asymptotically in the statistics/data-mining literature: for `M` bins and `n`
  samples the expected unnormalised discrete total variation is `≈ 2(M−1)/√(Mπ) · √n`, i.e.
  `SD ≈ √(M/(πn))` [RESTATED — this is Banić–Elezović, *TVOR: Finding Discrete Total Variation
  Outliers Among Histograms*, IEEE (title, authors and venue appear consistently across search
  results); I did not open it, and I flag the constant as unverified]. That matches Proposition F
  to within the constant `√(π)/(4√2)/... ` — the point is the exponent and the `√M` are exact.
- *In distribution testing* the same fact is the standard reason uniformity testing needs
  `Θ(√M/ε²)` samples: the empirical distribution of `n` samples from `U_M` sits at L1 distance
  `Θ(√(M/n))` from uniform [RESTATED, textbook-level, no single canonical citation found].

**What Proposition F is NOT implied by, and this is the part worth recording.**

- **Radhakrishnan–Ta-Shma does not imply it.** I read RT00's abstract, p. 2 [READ]: *"If the input
  is an `n`-bit source with min-entropy `k` and the output is required to be within a distance of
  `ε` from uniform distribution, then to extract even one additional bit, one must invest at least
  `log(n − k) + 2log(1/ε) − O(1)` truly random bits; to obtain `m` output bits one must invest at
  least `m − k + 2log(1/ε) − O(1)`. Thus, there is a loss of `2log(1/ε)` bits during the
  extraction."* This is about **seeded** extractors and dispersers. Applied here the seed is all of
  `f`, i.e. `N² log M` bits, and the bound is vacuous. The two-source form
  `m ≤ k₁ + k₂ − 2log(1/ε)` that would give `ε ≥ √M/N` **is not in RT00 as published**; it reaches
  me only through secondary paraphrase [RESTATED], and — more importantly — it *cannot* hold at
  `k_i = log N` (full support), because with `M | N²` a balanced `f` is a perfect extractor for
  the unique full-entropy source. The two-source entropy-loss bound is a worst-case-over-subsets
  statement; Proposition F fixes `δ = 1/N` exactly, which pins both sources to be uniform on all
  of `[N]` and leaves no subset to choose. **Proposition F genuinely needs the balls-in-bins
  fluctuation and is not an instance of the classical lower bound.** I consider this the single
  most defensible novelty claim in the artifact.
- **Chung–Vadhan does not imply it** for the same reason: their lower bounds read *"there exists a
  block source `(X₁,…,X_T)` with `k` bits of min-entropy per item such that … is `ε`-far from
  uniform (for `H` coming from any hash family)"* [READ, p. 4] — worst-case source, arbitrary
  family. Proposition F is average-over-`f`, fixed full-support source.
- **CFHS's own attacks do not imply it.** Their Proposition 17 (UBB) and Proposition 18 (BUB) are
  the two gray corners of Figure 1 [READ, p. 10:4]. Proposition 18's advantage is
  `1 − M̄²/M − M(eN/(MM̄))^{M̄}` with `M̄ = ⌈∜M⌉` — close to `1`, not `δ√M` — and it needs a
  **bounded** predictor and sources making one oracle query [READ, pp. 10:12–10:13]. Proposition F
  lives in UUU, where the predictor is unbounded and the pair is genuinely `δ`-unpredictable, so it
  is a **new gray corner in CFHS's taxonomy**: it shows UUU is unachievable once `δ√M ≳ 1`. That
  taxonomic reading is not in the artifact and is worth adding.

**An analytic caution, my own reasoning and not a citation.** At `δ = 2/N` rather than `1/N` the
sources may read `f` and each pick `x_i` uniform from an `f`-dependent set `B_i ⊂ [N]` of size
`N/2`; splitness and `2/N`-unpredictability both survive, and the classical max-discrepancy over
rectangles then delivers the same `δ√M` shape by a route much closer to the folklore. So the
`δ = 1/N` diagonal is where Proposition F is genuinely not classical, and the artifact should say
so rather than presenting the whole family as new territory. (`PROGRESS.md` §2.4 already records
that Proposition F "licenses nothing off the diagonal `δ = 1/N`", from the other direction.)

**What would change my verdict.** (a) A crypto paper stating "the monolithic random oracle is not
a multi-source extractor for `M ≳ 1/δ²`" — I found none, and Proposition F would then be
ALREADY KNOWN. (b) Opening Diaconis–Zabell or TVOR and finding the constant stated for the
normalised statistical distance would upgrade my FOLKLORE verdict from "the fact is classical" to
"here is the line to cite".

---

## E. The single deciding source

**Salil Vadhan, *Pseudorandomness*, Foundations and Trends in Theoretical Computer Science
7(1–3), Chapter 6 "Randomness Extractors" — specifically Lemma 6.10 (p. 173), Proposition 6.12
and its proof (p. 175), the paragraph on `binom(N,K)` (p. 176), Theorem 6.14 and its proof
(pp. 176–177), and §6.2.1 (p. 178).** [READ — pages rendered and quoted above.]

This is the deciding source because it settles all three questions at once and in the same idiom:

- It contains, in Proposition 6.12's proof, **the exact union-bound-over-all-`2^M`-tests device**
  that the artifact presents as its Idea 2, including the quantifier-order property that makes an
  `f`-dependent test substitutable. So Lemma B is not new.
- It contains, in Theorem 6.14's proof, **the exact `binom(N,K) ≤ (Ne/K)^K` counting that produces
  `t_c(k₁,k₂)`**, and in the p. 176 paragraph **the exact reason one source fails and two
  succeed** — which the artifact's §4 rediscovers as its response to Contract `rem:ell1`.
- It contains, in Lemma 6.10, the flat decomposition the artifact imports as `[CFHS, Lemma 3]`.
- It states, p. 177, *"both bounds (on `m` and `d`) are individually tight up to the `O(1)`
  terms"*, which is the classical home of the `δ√M` shape that Proposition F re-derives.
- And by **not** containing anything about sources that depend on `Ext`, it isolates precisely
  what the campaign adds: Lemma 1's posterior factorisation under splitness, and Lemma A(a)'s
  Cauchy–Schwarz.

If exactly one thing is done with this report, it should be: cite Vadhan Ch. 6 in §10 of the
kappa-2 arm, restate §4's Lemma B as "the two-source analogue of [Vad12, Prop. 6.12 / Thm 6.14]",
and move the artifact's novelty claim off Lemma B and onto Lemma 1 + Lemma A(a). That is a
presentational change with no mathematical cost, and it removes the largest referee risk in the
arm.

---

## F. Gap register for this artifact

- **[BLOCKED]** `HARNESS.md` (§3.1, §2, §2.1) and `contract-d*.md` do not exist in the repo. Header
  format and artifact-id scheme are my own; reconcile if a harness spec is later supplied.
- **[BLOCKED]** Chor–Goldreich, *Unbiased Bits from Sources of Weak Randomness and Probabilistic
  Communication Complexity*, SICOMP 17(2), 1988. Not opened. It is the one place a remark about
  extractor-dependent two-source extraction could plausibly hide. **This is the top source
  request.**
- **[BLOCKED]** Dodis–Oliveira, *On Extracting Private Randomness over a Public Channel*, RANDOM
  2003, LNCS 2764, pp. 252–263 (title/venue/pages verified real; content not opened). CFHS cites
  it as [17] and Remark 24 compares against it. Its "strong blender" existence result via the
  probabilistic method is the closest classical relative of Theorem D and should be read before
  any novelty claim is published.
- **[BLOCKED]** RT00's two-source entropy-loss statement. Not present in the pages I read; the
  two-source form is [RESTATED] from secondary sources only. Do **not** cite
  "Radhakrishnan–Ta-Shma, `m ≤ 2k − 2log(1/ε)` for two-source extractors" without opening the
  paper — I could not confirm it is there.
- **[RESTATED, do not cite as read]** Diaconis–Zabell (Statistical Science 1991) and Banić–Elezović
  (TVOR, IEEE). Titles/venues appear consistently in search results; I did not open either and I
  vouch for neither a numbered result nor a constant.
- **[NOT CHECKED]** Correctness of any of the three results. This is a scout pass. `PROGRESS.md`
  §3 records that `kappa-2-r3` has had 0 of 5 verification passes; that is unchanged.
- **[NOT CHECKED]** Whether the source cards S1/S2 faithfully report CDGS and CFHS. I read CFHS
  directly and found the S2 card's Theorem 3, Lemma 3, Lemma 4.3 and §1.4 entries accurate in
  substance; **I did not check S1 against CDGS**, which `PROGRESS.md` names the campaign's weakest
  link.

---

## SOURCE REQUEST

Three, in priority order. Each is requested because it could flip a verdict, not for completeness.

1. **Chor, Goldreich, *Unbiased Bits from Sources of Weak Randomness and Probabilistic
   Communication Complexity*, SIAM J. Comput. 17(2):230–261, 1988.** Wanted: the exact statement
   and proof of their probabilistic-method result that "most functions" extract from two
   probability-bounded sources, and any remark on the extractor being chosen after the sources.
   *Would flip:* result (1) from NO PRIOR ART FOUND to FOLKLORE or IMPLIED BY, if the paper
   already notes the good event is a property of the function alone.
2. **Dodis, Oliveira, *On Extracting Private Randomness over a Public Channel*, RANDOM 2003,
   LNCS 2764:252–263.** Wanted: the non-constructive strong-blender existence theorem with its
   parameters, and whether the source is allowed to depend on the blender.
   *Would flip:* result (1) to IMPLIED BY if their existence result already quantifies over
   function-dependent sources; also fixes the `k ≥ log n + 2log(1/ε)`, `m = 2k − 2log(1/ε)`
   parameters that I currently hold only as [RESTATED].
3. **CFHS full version, ePrint 2025/1258, the sections omitted from the ITC version** — the
   proofs of Theorem 21 and Lemma 22, and the one-wayness-in-UBU result mentioned at p. 10:20.
   Wanted: confirmation that no UUU positive result and no `δ√M`-shaped attack appears anywhere in
   the full version.
   *Would flip:* results (1) and (3) to ALREADY KNOWN if either is there. The ITC version's own
   "left for future work" makes this unlikely, but it is the cheapest remaining check and the
   campaign already has the PDF locally (per the S2 card).

Not needed: anything further on presampling. The CDGS forward-citation sweep (88 papers) and five
targeted queries on multi-party / multi-stage preprocessing returned nothing, and CFHS §1.4 states
the multi-party decomposition question as open in print. That negative is as auditable as it is
going to get without a manual literature crawl.

### END OF ARTIFACT split-decomp-scout-1 ###
