# Referee package — `split-decomp-kappa-4`

You are refereeing ONE artifact. Judge it on its own terms and on the files listed here.
Do not consult the wider repository, and do not assume anything about the campaign that these
files do not state.

## Every file in this package, named individually

Read with absolute paths under this directory:

| file | what it is | status |
|---|---|---|
| `ARTIFACT.md` | **the artifact under review** — `split-decomp-kappa-4` | JUDGE THIS |
| `CONTRACT.md` | the conjecture statement, definitions and remarks | YARDSTICK — assume correct |
| `deps/DEP-A-kappa-3-r4.md` | supplies **Theorem E″**, **(H1)**, **(H2)**, Corollaries G1, G2, Lemma G0 | GIVEN — assume its results hold as stated |
| `deps/DEP-B-kappa-2-r2.md` | supplies **Theorem D**, **Corollary D′**, **Corollary D″**, Lemma C, Theorems A⁺/B⁺, Proposition F | GIVEN — assume its results hold as stated |
| `deps/DEP-C-kappa-1-r3.md` | supplies **Theorem C**, **Lemma P**, **Theorem A**, Lemmas 0–5 | GIVEN — assume its results hold as stated |
| `cards/S1-cdgs-card.md` | source card, Coretti–Dodis–Guo–Steinberger, ePrint 2017/937 | GIVEN |
| `cards/S2-cfhs-card.md` | source card, Coretti–Farshim–Harasser–Southern, ePrint 2025/1258 | GIVEN |
| `CHECK-cap-fixed-q.py` | the artifact's own machine-check; you may read and reason about it | EVIDENCE |

There are exactly two files in `cards/` and exactly three in `deps/`, named above. If you cannot
open one, say so explicitly as a class-(E) packaging finding rather than working around it.

## What the artifact claims

Two theorems, both on region **(H2)**:

- **Theorem H** — if the family may depend on `q`, the Contract's `conj:main` holds at **every**
  `P ∈ ℕ`, with `c = 2`, `C = 13`. No hypothesis on `P` survives.
- **Theorem H′** — with the family independent of `q`, every `P` is covered with
  `C(q) = 4√(q⁺) + 9`.

Both are obtained by one move: build the family at `P₀ := min(P, ⌈t_q⌉)` (resp. `⌈t₀⌉`) and
`γ₀ := max(γ, N⁻²)` instead of at the requested `P`, then invoke Theorem E″ at `(P₀, γ₀)`.

## The step to attack first

**Lemma H0.** The artifact claims a `P₀`-mixture with `P₀ ≤ P` *is* a `P`-mixture, reading this
off Contract Definition `def:bf`'s `|I| ≤ P`. Everything rests on it. Check it against `def:bf`
verbatim, including the consistency clause and the index-set requirement of `rem:index`.

## Questions a referee should settle

1. Does Lemma H0 hold *exactly* as `def:bf` is written — for the mixture, not merely for a single
   bit-fixing source? `def:bf` defines a `P`-mixture componentwise; verify the quantifier.
2. Is Theorem E″ legitimately instantiable at `(P₀, γ₀)`? Check **(H1)** and **(H2)** at `P₀`,
   and that `γ₀ ∈ (0,1)`.
3. Are the three bounds of **Lemma H1** correct, in particular `N⁻² ≤ S` and
   `log γ₀⁻¹ ≤ log γ⁻¹`? The second is what keeps `c` at `2`; if it fails, `c` moves.
4. Do the case analyses in Theorems H and H′ **cover every `P ∈ ℕ`** with no gap at the boundary?
5. Is `C = 13` (resp. `4√(q⁺)+9`) actually established by the stated inequalities, or only by the
   machine check? A constant supported only by a grid is a finding.
6. **Quantifier order.** Theorem H relaxes `conj:main` by letting the family depend on `q`. Does
   the artifact state that relaxation honestly and confine it to `q` alone? Check against
   Contract `rem:order` and `rem:index` directly, not on the artifact's word. Does the family
   secretly depend on anything else — `D`, `x`, the challenge?
7. Is §3's claim about `rem:reduces` — that the `Θ(√q⁺)` separation is *exactly* the price of
   `q`-independence — supported, or overstated?
8. Are all citations into `deps/` accurate word-for-word? Quote what you checked.

## How to report

Classify each finding:

- **(A)** the artifact claims something it has not established, or states itself falsely
- **(B)** a computational or algebraic error
- **(C)** a gap: a step that is true but not licensed by what precedes it
- **(D)** an imprecision that does not threaten the result
- **(E)** a packaging failure on the requester's side, not the artifact's

Give a verdict of **CLEAN** or **DEFECTS**. Be adversarial: your job is to find what is wrong,
not to confirm. If the artifact is correct, say so plainly and name the steps you verified and
how. Do not soften a finding to be agreeable, and do not manufacture one to seem rigorous.
