# Blind referee report: split-decomp-kappa-3-r2

Package: kappa-3-r2 at `61a79f0`, the Contract, cards S1/S2, deps kappa-1-r3 and kappa-2-r2,
and the superseded `split-decomp-kappa-3` as `predecessor/`. Referee: fresh context, the
project's own REFEREE-PROMPT.md, no session context, told to read nothing outside the package.
Pass 1's findings file was excluded by a build-time guard.

## VERDICT
STATUS: DEFECTS

Four findings. **No computational error.** Every step of Lemma G0, the two new sharpened
sub-bounds, the `6 + 17/16 + 1/16 = 7⅛ ≤ 8` total, (H1), and Corollary G1's chase to
`13√(σ'q⁺δ)` was independently re-derived and confirmed. All four findings are about what the
document says about itself.

## FINDINGS

### F1 — the proof's opening sentence does not license what the proof uses (class C, minor, UPHELD)

"*Proof.* By Lemma G0 we may assume $q^{+}\delta\le\sigma'$, the other case being trivial."

The sharpened sub-bounds need `σ'q⁺δ < 1/64`, which is strictly stronger. The referee's
counterexample: `σ' = 2`, `q⁺δ = 2` satisfies `q⁺δ ≤ σ'` yet gives `8√(σ'q⁺δ) = 16 ≥ 1`, well
outside the region where the sharpened bounds hold. The later paragraph does re-invoke the true
dichotomy, so the logic actually used is sound; the opening sentence, read alone, is not enough.
Repaired in r3: the proof now assumes `8√(σ'q⁺δ) < 1` and derives both consequences from it.

### F2 — a self-description carried over from the predecessor, now false (class A, serious, UPHELD)

"**Remark (what changed, and what did not).** The only altered step is the fixed-set term. …
No constant moves."

True of `split-decomp-kappa-3`, where only the fixed-set term differed from Theorem E. False of
r2, which also rewrote the **query** term, introducing the constants `1/(8σ')` and `1/16` and
dropping that term's contribution from a full unit to `1/16`. The remark was left in place when
the surrounding text was edited. Deleted in r3 and replaced by two accurate remarks, one on what
changed and one on the quantifier order.

### F3 — Corollary G1's title overclaims, in the same class as pass 1's F1 (class A, serious, UPHELD)

"**Corollary G1 (the proved region now contains the Contract's own instantiation).**"

The chase verifies **(H1)** at `P = ⌈t⌉` and never verifies **(H2)**, a condition on `M` that
`thm:main` needs at whatever ambient `M` it was handed — `M` being fixed before `P`, `γ` and `q`
in the Contract's order. The referee's own words: "a softer instance of the same class of defect
(F1) this revision was written to fix". Retitled in r3 to "Theorem E″ reaches `thm:main`'s own
`P`, on the region **(H2)**", with a remark stating what the corollary does not say.

### F4 — the revision note's invariant claim undersells its own diff (class A, minor, UPHELD)

"§6 differs only in the id on its END line and in swapping … $\lfloor t\rfloor\ge t/2$ … for
$\lceil t\rceil\le t+1$."

Mechanically checked against the predecessor: true as far as it goes, but the bibliography
bullet had also gained an explanatory parenthetical. In r3 the invariant statement is derived
from a section-by-section mechanical diff rather than asserted, and every clause in it was
re-checked after writing: §0/§1/§3 byte-identical, §4 additions only, §5 one bullet, §6 exactly
two diff lines.

## NOT A DEFECT IN THE ARTIFACT — charged to the reviewer's packaging

The pass returned one class-(E) entry: the referee could not open the package's `cards/`
directory and so could not check two direct quotations in §4 against card S1. The files were
present. The prompt named the directory without naming the files, and the agent type's tool set
has no directory listing — the prompt also told the referee it had shell access, which that
agent type does not. Both errors are the requester's. Consequence to record: §4's two card
quotations remain unchecked by any referee, and the artifact's `7.0022` figure was not
independently reproduced in this pass. Neither is load-bearing; §4 was confirmed independent of
§§1–3.

## ACCEPTED WITHOUT DEFECT

- Lemma G0's dichotomy, re-derived; `σ' ≥ 2` from `N ≥ 2`; `q⁺δ < 1/128 < 2 ≤ σ'`.
- Both sharpened sub-bounds, re-derived independently via `x ≤ c²y ⟺ x ≤ c√(xy)`, and found to
  hold exactly at the boundary `σ'q⁺δ = 1/64`. Edge cases `q=0`, `δ=1`, `δ=1/N`, `N=2`, `σ=0`
  checked; `δ=1` and `N=2` never reach the non-vacuous branch, so no contradiction.
- The fixed-set term `Pδ ≤ (17/16)√(σ'q⁺δ)` from (H1), and the total as the only three summands
  feeding the `C=8` budget.
- Corollary G1's arithmetic throughout: `⌈t⌉ ≤ t+1`, `σ'q⁺/P ≤ √(σ'q⁺δ)`,
  `σ'+log γ⁻¹ ≤ 2σ'`, and the chain `γ = N⁻² ≤ δ² ≤ δ ≤ √(σ'q⁺δ)`.
- That pass 1's F1 was real, and that r2's repair closes it.
- §3 Corollary G2: `μ'(0)=0` exactly, (H2) vacuous at `q=0` for every `M`, and r3's Theorem A
  checked faithfully against the dep file as unrestricted in `M` and in resolution at `q=0`.
- §4: no forward reference from §§1–3; O1 and L1 consistently labelled incomplete; Lead L1's
  three inequalities each re-derived and true; the `2 ln 2` step re-verified via `e^u − 1 ≤ ue^u`.
- §5's gap register: every bullet correctly flagged load-bearing — but see A1 below, which this
  pass could not have found.
- The quantifier order, checked against `rem:order` and `rem:index` directly for the second time
  by an independent referee. No violation.

## FOUND OUTSIDE THIS PASS, BY A REPO-WIDE AUDIT

Two findings a package-only referee cannot reach, both repaired in r3.

### A1 — §5 asserted a review status that does not exist (serious)

r2 §5 stated that "`split-decomp-kappa-2-r2` has been through blind review at r1 and r2". False.
The campaign's one findings file for that arm reviews `split-decomp-kappa-2`, the pre-revision
artifact at `8c68c62`, and that tally's header says in terms that it "does NOT carry over to r2".
So **Corollary D″, load-bearing for Theorem E″, stands at zero passes of five** — and the triage
of that earlier pass *overruled* the referee on D″'s constant, so the single referee opinion ever
formed about it was rejected and never re-tested. r3 retags the bullet `[INHERITED-UNAUDITED]`
and states this.

### A2 — the region for conj:main is smaller than Theorem E″'s region (serious)

Theorem E″ is a statement per `q`. `conj:main` fixes one family per `(P,γ)` — before `q` — and
demands the bound at **every** `q`. So `conj:main` holds at `(P,γ)` only where (H1) and (H2) hold
at every `q`: the intersection, which binds at small `q`. That is `P ≤ √(σ'/δ)+1` and
`M ≤ σ'/(2δ)`. Verified: a family taken at `P = ⌈t(q₀)⌉` is covered only for `q ≥ q₀` — at
`q₀ = 1000`, nothing below `q = 1000`.

**Consequence, deflationary.** The `√q⁺` relaxation of (H1) does **not** enlarge the region on
which `conj:main` is proved, that region being pinned at `q=0` where the relaxation is worth
nothing. Against the original Theorem E the gain for `conj:main` proper is the additive `1` in
`P` and a factor `2` in `M`. The `√q⁺` is real and it is what makes `thm:main` derivable from
Theorem E″ without loss; it is not a gain in the conjecture's proved region. r3 states this
plainly and warns against reading (G1) as claiming otherwise.

## NOTE ON TRIAGE

All four findings, and A1 and A2, were upheld without a separate triage pass. F1, F2 and F4 are
matters of fact about the document's own text and were confirmed by reading it. F3 is conceded by
the corollary's own closing paragraph. A1 and A2 were confirmed independently — A1 by reading the
tally header, A2 by numeric check — before any revision. No repair weakens a proved statement.
This is a deviation from the harness's verify-triage-revise order and is recorded as one.

## LINEAGE

One angle. Four remain, and this tally does not carry over to r3.

### END OF FINDINGS split-decomp-kappa-3-r2 ###
