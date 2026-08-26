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

**The `P`-axis, at fixed `q`, in full** (`kappa-4` Theorem H): on region (H2), `conj:main`
holds at **every** `P ∈ ℕ` with `c = 2`, `C = 13`, if the family may depend on `q`. The
construction is one line — cap the fixed set at `P₀ := min(P, ⌈t_q⌉)` and clamp the slack at
`γ₀ := max(γ, N⁻²)`, then apply Theorem E″ at `(P₀, γ₀)` — and it is legal because `def:bf` asks
`|I| ≤ P`, so a `P₀`-mixture with `P₀ ≤ P` *is* a `P`-mixture. No `P`-hypothesis survives.

**And with the family `q`-free, every `P` at a cost of `√q⁺`** (`kappa-4` Theorem H′): capping at
the `q`-free `⌈t₀⌉` instead gives `conj:main` on the whole axis with `C(q) = 4√q⁺ + 9`. So the
`P`-window is **not blank**: it is proved with `C` degraded by exactly `Θ(√q⁺)`, and Theorem H
identifies that factor as the price of `q`-independence and nothing else. This is the Contract's
`rem:reduces` made uniform in `P` — the first thing the campaign has said about a remark
`PROGRESS.md` §2.3 records as cited by no artifact.

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

### 2.1 The `P`-cap — no longer blocking at fixed `q`; a `√q⁺` in `C` under `q`-free families

**Superseded in part by `kappa-4`.** Read §1's two new entries first. On region (H2) the
`P`-axis is closed outright at fixed `q` (Theorem H), and under `q`-free families the whole axis
is covered with `C(q) = 4√q⁺ + 9` (Theorem H′). What remains on this axis is therefore **a factor
`√q⁺` in the constant, under `q`-free families only** — not an uncovered region. The `Pδ` analysis
below stands as written and remains the account of *why* the `q`-free cap cannot move past `t₀`;
it is no longer the campaign's blocking item at fixed `q`.

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

### 2.3 A second open problem, never worked on

Contract `rem:reduces` states that the implication runs backwards too, and that "the directions
hold at values of `P` separated by `Θ(√q⁺)`, and closing that is a second open problem, distinct
from bounding `κ(q)`." **No artifact in this campaign cites `rem:reduces`**, and a search for its
converse construction across all artifacts returned nothing. Flagged in `kappa-3-r4` §4
(`rem:second`), including the caution that the `√q⁺` there may or may not be the same `√q⁺` that
(H1) relaxes.

**Now engaged, by `kappa-4` §3.** Theorem H′ reproduces `rem:reduces`'s capping uniformly in `P`,
and Theorem H answers the caution: the two `√q⁺` are **the same one**. It is the price of
`q`-independence — capping at `t_q` rather than `t₀` removes it and changes nothing else. The
second open problem is thereby sharpened to: find a `q`-free family achieving what the `q`-aware
cap achieves, or show none exists. It is now the *only* thing standing between the campaign and
`conj:main` on the whole `P`-axis, on region (H2).

### 2.4 Smaller mathematical debts

- `E[m₁m₂] ≤ δ²` is **false** — r3 §1 carries the counterexample — so the obvious sharpening of
  the revealed-mass bound is blocked by a proved obstruction, not merely unattempted.
- Proposition F licenses nothing off the diagonal `δ = 1/N`, so whether `δ√M` is tight elsewhere
  is open.
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

The lineage standard is **five independent verification angles per artifact**. Nothing is close.

| artifact | passes | verdict of record | note |
|---|---|---|---|
| `kappa-1-r3` | 1 of 5 | CLEAN, 6 class-(C) | **no triage file, no revision** — the six (C)s were never adjudicated |
| `kappa-2-r2` | **0 of 5** | — | never reviewed; its tally reviews the *pre-revision* `kappa-2` at `8c68c62` and says so |
| `kappa-3` | 1 (superseded) | DEFECTS, F1 upheld | tally does not carry to r2 |
| `kappa-3-r2` | 1 (superseded) | DEFECTS, 4 upheld | tally does not carry to r3 |
| `kappa-3-r4` | **0 of 5** | — | r3 never refereed; r4 repairs A3 and inherits the unreviewed lineage |
| `kappa-4` | **0 of 5** | — | lands with this revision; Theorems H, H′ rest entirely on E″ and D″, both at zero passes |

**The weakest link.** Corollary D″ is load-bearing for Theorem E″ and sits in `kappa-2-r2`, which
has zero passes — and the triage of the earlier `kappa-2` pass **overruled** the referee on D″'s
constant, so the one referee opinion ever formed about it was rejected and never re-tested. Aim
the next pass here.

**Never refereed at all:**

- The Contract's own `lem:hit` and `lem:query`, load-bearing inside r3's Theorem C at exactly the
  step where the `P`-cap enters. They appear in no artifact's external-results register, and the
  referee prompt hands the Contract over as the *yardstick*, so no pass has ever examined them.
- The **chain** `r3 → kappa-2-r2 → kappa-3-r4` end to end. Each link was refereed in isolation
  with its dependencies handed over as unchecked givens.
- Any **source card against the paper it summarises**. All passes were package-only. The kappa
  chain rests on three consequences of CDGS Claim 2 that the *published* claim does not state,
  taken on trust from a card transcribed from a local PDF.
- Two card quotations in `kappa-3-r4` §4 (§4 is byte-identical to r3's) — the r2 pass could not open the package's `cards/`
  directory, a packaging error on the requester's side, recorded in the findings file.

**Passes never run, of kinds the harness provides:**

- **No scout pass, ever.** No prior-art record of any kind. Theorem D and Corollary D′ are
  unconditional results whose novelty has never been checked against the literature.
- **No refuter pass, ever**, against any current artifact, and no counterexample-search code in
  the repo. `checks/rem-window-r4.py` is the first executable artifact committed here, but it
  verifies arithmetic in a remark; it searches for nothing. Every *refutation* claim in the
  campaign remains unreproducible prose in the task log.
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
worst margins).
