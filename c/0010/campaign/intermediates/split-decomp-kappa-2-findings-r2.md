# Five blind passes on `split-decomp-kappa-2-r2` — the first this arm has ever had

Five independent referees in fresh context, package-only (`kappa-2-r2-audit-files/`), spanning two
model families. This arm was the campaign's recorded weakest link: zero passes, holding
Corollary D″, whose one referee objection had been **overruled by triage rather than by an
independent check**.

| pass | lens | family | verdict |
|---|---|---|---|
| 1 | constants in §§5–6, Corollary D″ | verifier-b | DEFECTS — 5×(B), 2×(D) |
| 2 | Lemma A, Lemma C | verifier | **CLEAN** |
| 3 | Theorem D's scope, Lemma B's union bound | verifier-b | DEFECTS — 5×(B), 1×(C), 11×(D) |
| 4 | Proposition F, §8's tightness | verifier | **CLEAN** — 2×(D) |
| 5 | Theorem E, gap register, citations | verifier | DEFECTS — 1×(C), 1×(E) |

**Zero class-(A) findings across all five passes.** The arm is in substantially better shape than
the record implied.

## The two results that matter

**The overruled objection was correctly overruled.** Pass 1 was aimed at D″'s parenthetical — that
`γ₀ = δ` is "already inside the 3.21" — *without being told* that a prior referee had objected
there and been overruled. It traced `γ₀` through Theorems A⁺/B⁺ and confirmed the absorption:
`γ₀` occurs twice in the pre-collection display, once additively and once inside `C₀`, and at
`γ₀ = δ` the two are bounded as `2.498 δ√σ'` and `0.708 δ√σ'`, summing to `3.2048 ≤ 3.21`. Pass 2
confirmed it again as an unprompted downstream check. It is load-bearing: without the absorption
the leading part is `5.506 > 5` and D″'s constant fails outright.

**Theorem D's unbounded-query scope is licensed, and narrowly so.** The concern the package was
built around: the derandomisation lemma's finiteness could have rested on "finitely many
deterministic `q`-query strategies", which does not survive unbounded `q` — and r3's version of
that lemma argues exactly that way. Pass 3 found this arm **does not cite r3's Lemma 0; it
reproves Lemma 0 from scratch with the deduplication step needed**, so finiteness rests on
non-repetition over a domain of size `N²`, not on `q`. Had it inherited the r3 version, the stated
scope would have been an unlicensed overclaim.

## Also confirmed

- **Lemma A(a) needs no independence.** `m₁` and `m₂` are both functions of the same `f` and are
  perfectly correlated on r3's §1 counterexample, but `E[XY] ≤ √(E[X²])√(E[Y²])` holds for any
  joint law and `E[X²] = E[m₁]` exactly. Two passes checked it.
- **Proposition F is clean** — every equality, inequality and boundary case re-derived, including
  resolution-1 triviality under determinism and the non-independence of the `X_v` across `v`.
- **Lemma B's union bound is exact**, and the quantifier-order move that deletes the revealing
  rule is valid: the good event carries the `∀θ` inside it.
- **Theorem E's three hypotheses are each load-bearing**, and it uses Corollary D′ — not D″ —
  which is the correct choice, keeping its only unproved dependency to r3's Theorem C and Lemma P.
- **Every card citation** is stated on the card in the form used.

## Upheld and repaired in `split-decomp-kappa-2-r3`

| id | class | passes | finding |
|---|---|---|---|
| C1 | B | 1, 3, 4 | Five printed decimals truncated where an upper bound needed rounding up; witnesses at `N=2, σ=0`. Immaterial — nothing downstream moves |
| C2 | C | 1, 3 | Theorems A⁺/B⁺ instantiate `γ₀ := δ` without excluding `δ = 1`, where `γ₀ ∈ (0,1)` is required |
| C3 | E | 3, 5 | §9's gap register asserts another artifact's review history — false when written, and unverifiable from any review package |
| C4 | C | 5 | §8's interpolation claim is asserted, not proved; stated with unqualified certainty |
| C5 | D | 4 | §8 offers Proposition F as tightness evidence beside the small-`q` corner, without noting its witness makes `N²` queries |
| C6 | D | 3, 5 | §1's gloss that Lemma A(a) spends "the second source's independence a second time" — it uses no independence |

## Not closed by any pass

r3's Theorem C and Lemma P are GIVEN and not reproved here. And **no source card has ever been
checked against the paper it summarises**, so [CDGS, Claim 2] and [CDGS, Claim 3] rest on
transcription. Both are recorded in r3's gap register rather than repaired.

### END OF FINDINGS split-decomp-kappa-2-r2 ###
