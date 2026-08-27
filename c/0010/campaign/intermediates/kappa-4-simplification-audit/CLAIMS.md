# Two unmerged simplification claims, for adversarial check

These are **proposals**, not established results. Nothing in the repository depends on them.
Your job is to determine whether each is true, and if true whether the stated eliminations
actually follow. Assume the results in `deps/` hold as stated.

Notation: `σ' := σ + 2 log N`, `q⁺ := q+1`, `S := √(σ'q⁺δ)`, `t_q := √(σ'q⁺/δ)`,
`t₀ := √(σ'/δ)`, `B := σ' + log γ⁻¹`, `γ₀ := max(γ, N⁻²)`. Logs base 2.

---

## Claim A — the additive `1` in (H1), and everything spent repairing it, is unnecessary

`deps/DEP-D-kappa-4.md` (Theorem H) caps the fixed set at `P₀ := min(P, ⌈t_q⌉)` and therefore
needs **(H1)** in the widened form `P ≤ t_q + 1` that `deps/DEP-A-kappa-3-r4.md` §2 states.

**The claim:** cap at `P₀ := min(P, ⌊t_q⌋)` instead. Then (H1) is needed only in its
**original** form `P ≤ t_q` — the form `split-decomp-kappa-3` (r1) stated, before the `+1` was
introduced — and the conclusion still holds with `c = 2`, `C = 13`.

Sub-claims to check independently:

- **A1.** `⌊t_q⌋ ≤ t_q`, and `⌊t_q⌋ ≥ 1` in every non-vacuous instance (non-vacuity being
  `8√(σ'q⁺δ) < 1`, per Lemma G0).
- **A2.** With the floor cap, the fixed-set term is `P₀δ ≤ ⌊t_q⌋δ ≤ t_qδ = S` **exactly**, with
  no additive `δ` to absorb — so the sharpened sub-bound `δ ≤ (1/16)S` of DEP-A §2 is not needed.
- **A3.** `C = 13` still suffices. (A grid check reports 14880 non-vacuous points, zero failures
  at `C = 14`, smallest sufficient `C = 12.0067`, worst `⌊t⌋/t = 0.9967`. Re-derive rather than
  trusting this.)
- **A4.** **The elimination claim.** If A1–A3 hold, then Corollary G1 of DEP-A is unnecessary for
  Theorem H, its only role having been to verify that `thm:main`'s `⌈t⌉` fits inside (H1); and
  findings F1, F3 and A3 recorded in DEP-A's header — all concerning `⌈t⌉` vs `⌊t⌋` vs the `+1` —
  address a problem the floor cap does not raise. **Is A4 right, or does something else depend
  on the `+1` or on G1?**
- **A5.** Is it nevertheless true that kappa-3's `√q⁺` relaxation of (H1) (`t₀ → t_q`) is still
  required for Theorem H — i.e. that the original **Theorem E** of DEP-B, whose (H1) is
  `P ≤ √(σ'/δ)`, would yield only Theorem H′ and not Theorem H?

## Claim B — Corollary D″'s first arm and the whole `μ'` apparatus can be dropped

**The claim:** when the observer `D` has full challenge resolution `M` and `q ≥ 1`, Theorem E″'s
extraction step can use **Corollary D′** of DEP-B (`κ(q) ≤ 5√(σ'δ) + 2δ√M`, stated there as
unconditional, any `q`, any resolution) in place of **Corollary D″**, with hypothesis

    (H2')  2δ√M ≤ S          equivalently  M ≤ σ'q⁺/(4δ)

in place of **(H2)**, and reach the same conclusion `ε(D) ≤ 6S`.

Sub-claims:

- **B1.** `(H2') ⟹ (H2)`, since `min{μ'(·), 2δ√M} ≤ 2δ√M`.
- **B2.** At full resolution and `q ≥ 1`, `M ≥ 4`, `2δ√M < 1`, the two are *equivalent* — DEP-B §6
  ("Which arm wins") is claimed to establish that the `2δ√M` arm is then the smaller. Check that
  §6 really licenses this, including its side conditions.
- **B3.** `5√(σ'δ) + S ≤ 6S`, so the extraction step of DEP-A §2 goes through verbatim.
- **B4.** **The elimination claim.** Theorem D and Corollary D′ of DEP-B §5 depend only on
  Lemmas 0, 1, 2, A(d), B and Claim 3 — and **not** on the revealing-rule apparatus. Verify this
  by reading DEP-B §5's proof. If so, the simplified chain drops: Lemma C and the `μ'`
  construction, Theorems A⁺/B⁺ (DEP-B §6), Corollary D″ entirely, and DEP-C's Lemma 4.
- **B5.** **The cost.** The `M`-free `q = 0` case (Corollary G2 of DEP-A) uses DEP-C's Theorem A,
  whose proof runs through DEP-C's Proposition 6.2. So Lemma 3 of DEP-C is claimed to be
  *retained*, while Lemma 4 and Lemma C still drop. Is that accounting right?

## Claim C — a subsidiary reading, check it too

It is claimed that (H2)'s two arms are the same union bound priced two ways: Theorem D
union-bounds over all `2^M` decision functions `θ : [M] → {0,1}`, paying `M ln 2` inside `C₁`
(whence `δ√M`), while Proposition 6.2 restricts to `θ` determined by the leakage plus revealed
cells, paying `(σ+2) ln 2` inside `C₀` and owing `μ(s)` for the revelation. **Is this an accurate
reading of the two proofs, or a plausible-sounding story that the proofs do not support?**
