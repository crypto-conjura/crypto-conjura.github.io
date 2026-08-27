# c/0010 — split-decomposition campaign: what is proved, and what is left

State as of 27 August 2026, at `e50629a` plus the `kappa-4` arm landing with this file.
Assembled from a six-lens repo-wide audit (55 items, each adversarially re-checked against the
files, plus 8 from a completeness critic) and from the three blind-verification passes on record.
Every quantitative claim below was machine-checked or is quoted from a named artifact.

Notation is the Contract's: `σ' := σ + 2 log N`, `q⁺ := q+1`, `t := √(σ'q⁺/δ)`,
`μ'(s) := min(sδ, 2(sδ²)^{1/3}, 1)`.

---

## 1. What is proved

**The Contract's `conj:main`, in full — one family per `(P,γ)`, good at every `q`:**

```
P ≤ √(σ'/δ) + 1        and        M ≤ σ'/(2δ)
```

with `c = 2`, `C = 8`, for every observer, no restriction on challenge resolution. This is the
intersection over `q` of Theorem E″'s hypotheses (H1) and (H2) — (H1) binds at `q = 0`, (H2) at
`q = 1`. Against the original Theorem E of `kappa-2-r2`, whose intersection is `P ≤ √(σ'/δ)`,
`M ≤ σ'/(4δ)`, the gain is the additive `1` and a factor `2` in `M`.

**Read this next, it is the most-mistaken point in the campaign.** Theorem E″'s stated region
`(H1) ∧ (H2)` is *per `q`* and is larger. It is what `thm:main` needs — `thm:main` fixes one
observer and therefore one `q` — and Corollary G1 shows it now reaches `thm:main`'s own
`P = ⌈t⌉`, where the original Theorem E fell a factor `√q⁺` short. But it is **not** the region
on which `conj:main` holds, and the `√q⁺` relaxation buys nothing there. See
`split-decomp-kappa-3-r4` §2, findings A2 and A3.

**The `P`-axis, at fixed `q`, in full** (`kappa-4-r2` Theorem H): on region (H2), the Contract's
bound holds at **every** `P ∈ ℕ` with `c = 2`, `C = 13`, if the family may depend on `q` — which is
a *relaxation* of `conj:main`, not `conj:main`, since the conjecture requires the family to depend
only on `(S₁,S₂,P,γ)`. The
construction is one line — cap the fixed set at `P₀ := min(P, ⌈t_q⌉)` and clamp the slack at
`γ₀ := max(γ, N⁻²)`, then apply Theorem E″ at `(P₀, γ₀)` — and it is legal because `def:bf` asks
`|I| ≤ P`, so a `P₀`-mixture with `P₀ ≤ P` *is* a `P`-mixture. No `P`-hypothesis survives.

**And with the family `q`-free, every `P` at a cost of `√q⁺`** (`kappa-4-r2` Theorem H′): capping
at the `q`-free `⌈t₀⌉` gives the bound on the whole axis with `C(q) = 4√q⁺ + 9` — **on the smaller
region `M ≤ σ'/(2δ)`**, which is (H2) intersected over `q`, binding at `q = 1`. `C(q)` is not
absolute, so this is not `conj:main` either. It is the campaign's first engagement with the
Contract's `rem:reduces`, recorded in §2.3 as cited by no artifact, and supplies one direction of
its question.

**Three corrections to what `kappa-4` (r1) claimed here**, all from the six-referee audit
(`split-decomp-kappa-4-findings.md`), all repaired in r2. The `P`-window as §2.1 states it — for
`conj:main`, `C` absolute, family `q`-free — **does not close**; r1's "closes completely" was scoped
to a different statement. Theorem H′'s hypothesis was malformed (`q` free in the hypothesis, rebound
in the conclusion) and its literal reading is vacuously satisfied at `q = 0`; the true hypothesis is
(H2) at *every* `q`. And the claim that the `√q⁺` is "the price of `q`-independence and nothing
else" was an achievability result asserting a necessity — no lower bound against `q`-free families
exists anywhere, and `kappa-3-r4` §4's `rem:second` had warned that `rem:reduces`'s `√q⁺` (a
separation in `P`) and this one (a degradation of `C`) are different objects.

**Also proved, and trivially so — recorded because no artifact had noticed it:** `conj:main`
holds for `P ≥ N²`, via the point-mass family `Y_{f,ζ} = δ_f`, which is `P`-bit-fixing,
consistent, and gives `Adv = 0`. So the uncovered `P` set is a **bounded window**, not a
half-line.

**Unconditional, no `P`, no appeal to the conjecture** (`kappa-2-r2` §5–6):

| result | statement | restriction |
|---|---|---|
| Theorem D, Corollary D′ | `κ(q) ≤ 5√(σ'δ) + 2δ√M` | none, any `q`, any resolution |
| Corollary D″ | `κ(q) ≤ 5√(σ'δ) + min{μ'(min(qM,N²)), 2δ√M}` | first arm inherits r3 |
| r3 Theorem A | `κ(0) ≤ 5√(σ'δ)` | none — any `M`, any resolution |
| Proposition F | `κ(N²) ≥ δ√M/(4√2)` | the diagonal `δ = 1/N`, `2 ≤ M ≤ N²/2` only |

Proposition F is the campaign's **only** proved lower bound, and it pins the `M`-dependence of
the `q`-free bound to within `8√2` on that diagonal alone.

---

## 2. What is left to prove

### 2.1 The `P`-cap — not blocking for the `q`-relaxed statement; a `√q⁺` in `C` otherwise

**Superseded in part by `kappa-4-r2`.** Read §1's entries first, including the three corrections.
On region (H2) the `P`-axis is closed for the `q`-relaxed statement (Theorem H); under `q`-free
families the axis is covered with `C(q) = 4√q⁺ + 9` on `M ≤ σ'/(2δ)` (Theorem H′). **The window as
stated below — `conj:main`, `C` absolute, `q`-free family — is not closed by either.** What remains
on this axis is a factor `√q⁺` in the constant under `q`-free families, on the intersected `M`
region. The `Pδ` analysis below stands and remains the account of *why* the `q`-free cap cannot move
past `t₀`; it is no longer the blocking item once `q` may be fixed first.

With `C` required absolute and the family `q`-free, `conj:main` is unproved on the window

```
√(σ'/δ) + 1  <  P  <  N²
```

non-empty in every non-vacuous instance (`8√(σ'q⁺δ) < 1` and `δ ≥ 1/N` force `t < N/8`), and
**every application with `q ≥ 1` lives in it**.

The lower endpoint is `q`-free, and this matters. It is (H1) *intersected over `q`*, which binds
at `q = 0` — not (H1)'s own per-`q` `√(σ'q⁺/δ) + 1`. `kappa-3-r3` wrote the per-`q` endpoint here
and kept the "every application" clause, which cannot both hold: `thm:main` instantiates at
`P = ⌈t_q⌉ ≤ t_q + 1`, so against the per-`q` endpoint the application point is outside the
window by construction — that being exactly what Corollary G1 proves. Repaired in
`split-decomp-kappa-3-r4` as finding A3; the corrected window is **wider** than r3 claimed, by
`[t₀+1, t_q+1]`, so r3 understated this gap. Against the `q`-free endpoint the applications are
interior with room: non-vacuity forces `t₀ := √(σ'/δ) > 8σ'√q⁺ ≥ 16`, and `t_q = t₀√(q+1)`, so
`⌈t_q⌉ ≥ t₀√2 > t₀ + 1` for `q ≥ 1` — worst margin `129.5` over the 1261-point grid of
`checks/rem-window-r4.py`. At `q = 0` the endpoints coincide and the point is covered, which is
"`q = 0` is done" restated. So applications fall outside the proved region not because `⌈t⌉`
overshoots (H1) — G1 settled that — but because `conj:main` needs one family good at every `q`
and is pinned at `q = 0`, where the `√q⁺` relaxation buys nothing.

`Pδ` enters the chain at **exactly one step** — `|G₂ − G₃| ≤ Pδ + qδ` in r3's Theorem C, i.e.
the Contract's `lem:hit` bound `Pr[x ∈ I_J] ≤ Pδ`. `kappa-3-r4` §4 argues this is a defect of the
*route*, not of the statement: on `{x ∈ I_J}` consistency forces `H*(x) = H(x)`, the challenge
`Real` supplies, so the route pays for the event on which `Dec`'s challenge is *correct*. The
Contract concedes the mechanism — `rem:uses` records that consistency "is **not** used anywhere
in this section".

**Obstruction O1** shows the obvious repair needs a new idea, not more care: conditioning CDGS
Claim 3 on `(x,v)` reweights `X_j` and can destroy density; letting the distinguisher sample `x`
costs unbounded queries and makes Claim 3 vacuous; bounding the branch trivially returns `Pδ`.

**Lead L1** gets the accounting right — the reweighting costs `≤ 2 log N + log γ⁻¹` bits of
deficiency, exactly what `σ'` is defined to carry — but cannot close it, because recovering
density puts a fixed set depending on `x`, which `rem:index` forbids.

> **The missing input, stated sharply:** a form of CDGS Claim 3 tolerating a bounded-deficiency
> perturbation of a dense source against the **original** bit-fixing companion.

**And a redirection, from `kappa-4` §4.** This entire programme buys the ability to afford a
*large* fixed set. Theorem H shows that at fixed `q` one never needs one: `P₀ = ⌈t_q⌉` always
suffices, so `Pδ` never needs to exceed `S`. §4 of `kappa-3-r4` is therefore aimed squarely and
solely at the `q`-free statement, where the cap must sit at `t₀`. Anyone resuming it should know
they are working on `rem:reduces`'s second open problem (§2.3), not on the `P`-cap as this section
used to describe it.

Ruled out as a way in, so it is not tried twice: the multiplicative form of Claim 3 on card `S1`.
Both forms require density.

### 2.2 The `M`-corner — blocking

For `q ≥ 1` and observers of challenge resolution `> 1`, `conj:main` is unproved once
`M > σ'q⁺/(4δ)` — that is, `M` large with `q` small. `q = 0` is closed for every `M` by
Corollary G2. `kappa-2-r2` §8 shows **both arms in hand are individually tight** (`μ'` on r3 §1's
counterexample at `s = 1`, `δ√M` on Proposition F) and that the natural interpolation over a
subset `T ⊆ [M]` "gives nothing beyond the endpoints up to constants". The sharp open question,
in the artifact's own words: whether `κ(q) ≤ O(√(σ'δ)) + μ'(q)` holds for unrestricted observers,
i.e. whether the first arm can be made `M`-free.

**Sharpened, 27 August 2026, and this is the actionable form.** `D` has **full challenge
resolution `M`** in this campaign's applications — a general distinguisher `D^H(y,z)` may steer
its queries on `y` — so the `M`-free arm `μ'(q)` of resolution-1 observers is unavailable, and by
§6's "which arm wins" the `2δ√M` arm is then strictly the smaller for `q ≥ 1`, `M ≥ 4`,
`2δ√M < 1`. (H2) therefore reduces to arm 2 alone, which in bits reads

```
log M  ≤  k + log(σ'q⁺) − 2          k := log(1/δ)
```

— *do not ask for more output bits than one source's unpredictability*, the `q`-dependence being
only additive-logarithmic. `checks/h2-applications.py` tabulates it: key extraction sits well
inside (128- or 256-bit key from 256-bit-unpredictable sources, allowance 328 bits), and what
falls outside is **long-output extraction** — 512-bit or streaming output — while the bound is
still strong at `2⁻⁹¹`. That is exactly the sponge/Merkle-Damgård streaming use that motivated
wanting the decomposition route at all.

**And the evidence for arm 2 does not reach the corner that binds.** Proposition F, the campaign's
only lower bound, exhibits an observer making **`N²` queries**. `κ` is monotone in `q` — a
`q`-query observer may ignore queries — so `κ(N²) ≥ δ√M/(4√2)` constrains `κ(1)` not at all. (H2)
binds hardest at *small* `q` with large `M`; at `q = N²` it is free, permitting
`M ≤ σ'N²/(4δ)`. **So no artifact in this campaign gives any evidence that `κ(q)` carries
`M`-dependence where (H2) actually bites.** §8's "both arms are individually tight" is true as
stated and misleading as read: arm 2's tightness is demonstrated only at `q = N²`.

Why the route pays it: the revealing-rule argument needs `S(f,ζ)` a function of `(f,ζ)` alone,
covering *every* challenge value, because `v = f(x)` is correlated with the `x` being conditioned
on. At full resolution that union is `qM` cells even though only `q` matter for any fixed `v`.

> **The sharp question, narrower than §8's:** does `κ(q)` have *any* `M`-dependence for small `q`?

**Answered, negatively and with strong evidence, 27 August 2026** — the campaign's first refuter
pass, `split-decomp-refuter-1.md`, with code and a run record in `checks/refuter-mcorner.py` and
`checks/refuter-mcorner-run.txt`. **No counterexample found, and the obstruction is now an exact
identity rather than a suspicion.**

For a flat product source on a `K×K` rectangle (`δ = 1/K`), the *exact* optimal advantage of a
`q`-query observer is `Phi(min(q,K²),M)/K²` with `Phi(q,M) := (M/2)·E|Bin(q,1/M) − q/M|`, because
conditioned on the transcript, `E[ρ(v) | transcript] − 1/M = (n_v − q/M)/K²`: **averaging kills the
histogram fluctuation, and only the mass of the inspected cells survives, which carries no `M`.**
Hence `adv ≤ qδ²` for every `M`; the deficit is `1 − Phi(q,M)/q = (1−o(1))q/M`; and `δ√M` is
reached only at `q = 1/δ²`. Re-verified independently for the record at `q` up to `4096`.

**The `M`-dependence onset and the (H2)-failure corner are disjoint in every non-vacuous instance,
provably.** Appreciable `M`-dependence needs `M ≲ q`; (H2) fails needs `M > σ'q⁺/(4δ)`; both give
`4δ > σ'`, which with `σ' ≥ 2`, `δ ≤ 1` forces `σ' < 4`, i.e. `N ∈ {2,3}` with `δ` near 1 — and
every such point is vacuous. At `δ = 1/N`, `N = 2²⁰`: the `M`-dependence has died by `M = 2³` at
`q = 1` while the corner needs `M > 2²⁴`; by `M = 2¹³` at `q = 1024` while the corner needs
`M > 2³³`.

So **the `M`-corner is a route artifact at every parameter setting audited**, and the applications'
failing rows — 512-bit output, streaming — are `M`-free to relative `2⁻⁴³²`. The `δ√M` enters
through Lemma B's union over all `2^M` tests, which grants the observer a test depending on all of
`f`, where a `q`-query observer's decision depends on `f` only through its own `q`-cell transcript.

**Where the proving effort should now go.** Replace that union by one over `q`-query *transcripts*:
`C₁ = M ln2 + ln(4N²/γ₀)` becomes `q ln(N²M) + ln(4N²/γ₀)`, turning `δ√M` into `δ√(q log(N²M))`.
Over a 7840-point grid the ratio to the target is **≤ 1.78 in the meaningful corner** against
**29.92** now, so the repair is arithmetically sufficient. The missing input is the
transcript-**conditioned** rectangle discrepancy bound: the rectangle is chosen after seeing `f`, so
the union over rectangles must be taken *inside* the conditioning.

**What the negative does not cover**, since a null result is worth only its stated scope: no
non-vacuous instance can be enumerated (`N ≥ 512` forces `|Fun| = M^{262144}`), so the exact search
probes the functional form at tiny `N` and only the model-based and sampled stages reach the corner;
exact optima cover `q ≤ 2`; randomised leakage was not searched; and nothing here *proves* the
`M`-free bound.

### 2.3 A second open problem, never worked on

Contract `rem:reduces` states that the implication runs backwards too, and that "the directions
hold at values of `P` separated by `Θ(√q⁺)`, and closing that is a second open problem, distinct
from bounding `κ(q)`." **No artifact in this campaign cites `rem:reduces`**, and a search for its
converse construction across all artifacts returned nothing. Flagged in `kappa-3-r4` §4
(`rem:second`), including the caution that the `√q⁺` there may or may not be the same `√q⁺` that
(H1) relaxes.

**Now engaged, by `kappa-4-r2` §3 — but the caution stands.** Theorem H′ runs an *analogue* of
`rem:reduces`'s capping uniformly in `P`. It is not the same cap: `rem:reduces` uses
`A := σ + 2 + log(1/γ)`, which carries a `log(1/γ)` that `σ'` does not and diverges from it as
`γ → 0`. And `rem:second`'s caution is **not** answered: whether the two `√q⁺` are the same
phenomenon is still open, and r1's claim that they are was refuted by four referees — one is a
separation in `P` between two directions of a biconditional, the other a degradation of `C` at fixed
`P`, sharing only an exponent. What r2 supplies is one direction: `q`-dependence *suffices* to
remove the `√q⁺` within this route. The second open problem is therefore: find a `q`-free family
achieving what the `q`-aware cap achieves, or show none exists.

### 2.4 Smaller mathematical debts

- `E[m₁m₂] ≤ δ²` is **false** — r3 §1 carries the counterexample — so the obvious sharpening of
  the revealed-mass bound is blocked by a proved obstruction, not merely unattempted.
- Proposition F licenses nothing off the diagonal `δ = 1/N`, and nothing at `q < N²`.
  **Partly discharged, 27 August 2026** (`split-decomp-refuter-1.md`): the FIT family with
  `K = 1/δ` gives `κ(1/δ²) ≈ δ√(M/2π)`, which is **1.57–2.22×** Proposition F's constant for
  `K ∈ {4,…,32}` and all `2 ≤ M ≤ K²` — so the `δ√M` shape is now witnessed off the diagonal, at
  `q = δ⁻²` rather than `N²`. It still does not reach the corner: `1/δ² < σ'/(4δ³)` always, so the
  family is always inside (H2).
- **A gap no artifact states** (same pass): for `M ≥ 1/(4δ²)` with `q ≥ 1`, **both arms of
  Corollary D″ exceed 1**, so the campaign has no non-trivial bound on `κ(q)` at all there. `q = 0`
  remains covered `M`-freely by Theorem A.
- The public page's claim that `q = 0` is "proved and tight" rests on **no proved lower bound**;
  the only `q = 0` tightness evidence in the repo is numeric.
- The Contract asserts both its design restrictions are necessary (the mixture may not be chosen
  using the two points; the observer never sees the points). Neither has a counterexample or
  argument anywhere.
- `rem:ell1`'s counterexample spends one bit of leakage, so it shows nothing at `σ = 0` and does
  not establish that splitness is needed at zero leakage. A sharper zero-leakage vector exists
  (logged in `TASKS.md`) and is not yet in the Contract.

---

## 3. What is left to check

The lineage standard is **five independent verification angles per artifact**. One arm now meets
it: `kappa-4` has had six. Everything else is still at zero or one.

| artifact | passes | verdict of record | note |
|---|---|---|---|
| `kappa-1-r4` | 1 of 5 | CLEAN, adjudicated | six (C)s **triaged** (4 upheld, 2 pedantic) and repaired in r4; four angles still owed |
| `kappa-2-r2` | **5 of 5** | DEFECTS, **0 class-(A)** | first ever review of this arm; the overruled D″ objection **confirmed overruled**, twice independently; repairs in r3 |
| `kappa-2-r3` | **0 of 5** | — | lands with this revision |
| `kappa-3` | 1 (superseded) | DEFECTS, F1 upheld | tally does not carry to r2 |
| `kappa-3-r2` | 1 (superseded) | DEFECTS, 4 upheld | tally does not carry to r3 |
| `kappa-3-r4` | **0 of 5** | — | r3 never refereed; r4 repairs A3 and inherits the unreviewed lineage |
| `kappa-4` | **6 of 5** | **DEFECTS** | six blind passes, two model families; Lemma H0 CLEAN and no class-(B) error; 7 class-(A)/(C) upheld — see `split-decomp-kappa-4-findings.md` |
| `kappa-4-r2` | **0 of 5** | — | repairs all upheld findings; answering an audit is not the same as having had one |

**The former weakest link is no longer one.** `kappa-2-r2` has now had five blind passes, the
first ever on that arm, with **zero class-(A) findings**. The specific worry — that D″'s constant
rested on a referee objection which triage *overruled* rather than independently re-tested — is
discharged: a pass aimed at that parenthetical, blind to its history, confirmed the absorption,
and a second confirmed it unprompted. It is load-bearing (without it the leading part is
`5.506 > 5`), and it holds. See `split-decomp-kappa-2-findings-r2.md`.

**The source cards have now been checked, and they hold.** Both were read against their papers on
27 August 2026 — the first time any card in this campaign has been — reaching full text including
the CDGS appendix everything turns on. **No mathematical defect in either card.** Claims 25 and 26
exist with those numbers on p. 40 saying what card S1 says; Definition 1's "at most `P`", which
`kappa-4`'s Theorem H turns on, is verbatim and is load-bearing in the paper itself. See
`split-decomp-card-check-1.md`.

Four things the check found that nobody knew. The chain uses **four** consequences beyond Claim 2's
statement, not three — the exact-decomposition-with-residue was unlisted. Disjointness holds for the
**exact** decomposition only, not for Claim 2's γ-close object as the paper realises it, which makes
"simplifying" Lemma P to quote Claim 2 literally a trap. Claim 26 as printed carries numerator `S`,
not `S + log γ⁻¹`; the version Lemma P needs exists only in **footnote 15**. And `[CFHS, Lemma 4.3]`
**does not exist** — it is Lemma 4, item 3 — so every citation in that form was unresolvable.

Separately, a defect **in CFHS itself**: Theorem 3 states exponent `1/(ℓ+1)` while the final case of
its proof delivers `1/(ℓ+2)`, verified from the text layer of both the ePrint and the published
LIPIcs version and re-derived by hand. Inert here — that bound is used nowhere in the chain.

**The weakest link is now the novelty question, and it is not what it looked like.** The first
prior-art pass ran the same day (`split-decomp-scout-1.md`) and found that **Lemma B's engine is
textbook**: Vadhan, *Pseudorandomness* (Now Publishers, 2012), Proposition 6.12 proves that a random
function extracts from a fixed flat source by exactly this route — a union bound over all `2^M`
subsets, Chernoff per fixed subset, and the good event a property of the function alone — with
Theorem 6.14 supplying the `binom(N,K) ≤ (Ne/K)^K` counting, and the remark after 6.12 being the
same one-source-fails observation. Both verified directly against the monograph. §10 of the kappa-2
arm registers **no citation into the extractor literature at all**, and should.

What survives as novel is narrower and better located: **Lemma 1**, that the posterior factorises
because the sources are split — the step CFHS could not make with compression — and **Lemma A(a)**,
whose Cauchy–Schwarz across the two coordinates gives `δ√M` rather than `√(Mδ)`. Neither has a
one-source counterpart. **Proposition F is folklore in content** (the balls-in-bins histogram
distance) but is *not* implied by the classical extractor lower bounds: Radhakrishnan–Ta-Shma is
about seeded extractors and is vacuous when the seed is all of `f`, and at `δ = 1/N` exactly both
sources are pinned uniform on all of `[N]`, leaving no subset to choose. That diagonal is precisely
where it is not classical, and the scout calls it the most defensible novelty claim in the campaign.

No prior art was found for Theorem D / Corollary D′ as a statement, and the negative is
well-evidenced: CFHS's own abstract lists statistical multi-source extraction against **unbounded
distinguishers** as an open problem, CFHS has zero forward citations, and CDGS's 88 forward citations
contain nothing on multi-source extraction or multi-party preprocessing.

**Never refereed at all:**

- The Contract's own `lem:hit` and `lem:query`, load-bearing inside r3's Theorem C at exactly the
  step where the `P`-cap enters. They appear in no artifact's external-results register, and the
  referee prompt hands the Contract over as the *yardstick*, so no pass has ever examined them.
- The **chain** `r3 → kappa-2-r2 → kappa-3-r4` end to end. Each link was refereed in isolation
  with its dependencies handed over as unchecked givens.
- ~~Any source card against the paper it summarises.~~ **Done, 27 August 2026**, both cards, full
  text — `split-decomp-card-check-1.md`. The count was wrong: the chain rests on **four**
  consequences of CDGS Claim 2 that the published claim does not state, not three. All four are
  established by the proof text.
- Two card quotations in `kappa-3-r4` §4 (§4 is byte-identical to r3's) — the r2 pass could not open the package's `cards/`
  directory, a packaging error on the requester's side, recorded in the findings file.

**Passes never run, of kinds the harness provides:**

- ~~No scout pass, ever.~~ **Done, 27 August 2026** — `split-decomp-scout-1.md`. Verdicts above.
  Not yet verified, and flagged so they are not repeated as read: Chor–Goldreich (SICOMP 1988),
  Dodis–Oliveira (RANDOM 2003), and Radhakrishnan–Ta-Shma's two-source entropy-loss form, any of
  which could move Theorem D's verdict from "no prior art found" to "folklore" or "implied by".
- ~~No refuter pass, ever, and no counterexample-search code in the repo.~~ **Done, 27 August
  2026** — `split-decomp-refuter-1.md`, with `checks/refuter-mcorner.py` (12 stages, prints its own
  grids) and an 849-line run record. Verdict and scope in §2.2. Method validation worth noting: the
  search's optimiser was checked against **exhaustive enumeration of the entire observer space** in
  10/10 cases, 66 witnesses were recomputed in exact rational arithmetic and independently by Monte
  Carlo, and the open-ended stage used a train/test split so overfitting could not manufacture a
  witness.
- **No Lean formalisation** of anything in this campaign.

**Unadjudicated debt:** `c/0010/revision/concerns.md` holds ten suspected errors and six
unanswered proof-overview questions, explicitly "reported, not repaired", never triaged.

---

## 4. Records that are stale and should be reconciled

None of these is a mathematical error; all of them will mislead a reader.

- `kappa-2-r2` §9 gap register: both `[INHERITED-UNAUDITED]` tags, and the sentence that r3 "has
  no findings file and has not been through blind review". r3 has both, verdict CLEAN.
- `kappa-2-r2` §7's closing "what is now known is the union" paragraph: quotes two standing
  hypotheses that `kappa-3` deleted or relaxed, and at `q = 0` neither of its branches is needed.
- `kappa-2-r2` §8's "Barrier 1, restated": names the residue in `M` alone and never mentions the
  `P`-cap, which is now the sharper of the two.
- `kappa-2-r2`'s three statements that its region is *incomparable* with r3's.
- r3 §9's Barrier 1 and Barrier 2: both quote superseded thresholds.
- `kappa-2-r2` Theorem E's three-hypothesis statement: all three re-accounted.
- The Contract's status line and Progress paragraph, and the public page repeating them, index the
  open region by query budget (`q=0` done, `q=1` conditional, `q≥2` open). The campaign's own
  results are indexed by `P` and `M`.
- The typeset write-up `c/0010/latex/solution.tex` and its Review-status section: states Theorem E
  in its superseded form and does not reconcile with the tallies it summarises. The prose-revision
  deliverable in `c/0010/revision/` was never adopted; `solution.tex` has been edited twice since.
- The staged referee package `kappa-2-audit-files/` holds a pre-`#140` artifact and omits r3.
  **Do not reuse it** — build packages fresh, as the last two passes did.
- Public page: proof score `0` while a typeset partial solution exists; the Proof tab states
  twice that no proof exists; `status_updated: 2026-08-19` predates the Contract.
- r3's Lemma 0 asserts one deterministic `D'` dominating **both** paired experiments where its
  proof supplies one per experiment. The r3 blind pass found this; `kappa-2-r2` repaired it in its
  own restatement ("Fix one of the two paired experiments"); r3 as merged still carries the
  unrepaired version. Nothing downstream uses the conjunction, so nothing collapses.
- Three referee findings were **overruled** rather than upheld — F12, F15, G12 — and the text F12
  and F15 objected to still stands verbatim.

---

## 5. Campaign layout

`LEDGER.md` and `REPORT.md` do not exist for this campaign; this file is the first of the three
status files the harness convention expects. Present: `CONTRACT.md`, `intermediates/` (artifacts,
findings, triage, tallies), `sources/` (cards S1, S2), and `checks/` (executable verification of
numeric claims — `rem-window-r4.py` and `cap-fixed-q.py`, each printing its own grid size and
worst margins, `h2-applications.py` tabulating (H2) at application parameters).
