# Blind referee report: split-decomp-kappa-3

Package: kappa-3 at `376ac45`, the Contract, cards S1 (CDGS) and S2 (CFHS), and
kappa-1-r3 and kappa-2-r2 as reference for the results kappa-3 declares [INHERITED].
Package built fresh and the artifact checked byte-identical to `main` before the pass.
Referee: fresh context, the project's own REFEREE-PROMPT.md, no session context, told to
read nothing outside the package directory.

## VERDICT
STATUS: DEFECTS

One finding, class (A), in the artifact's own headline claim. The core derivations —
Lemma G0, Theorem E″'s four-term accounting, Corollary G2 — are correct and every
citation into the two dependencies was checked word-for-word and found faithful.

## FINDINGS

### F1 — Corollary G1's title claims containment of a point its proof does not use (class A, serious, UPHELD)

Quoted location: "**Corollary G1 (the proved region now contains the Contract's own
instantiation).**" … "Under **(H1)** the range reaches $\sqrt{\sigma'q^{+}/\delta}$, so
$P:=\lfloor\sqrt{\sigma'q^{+}/\delta}\rfloor$ is admissible".

Two sentences earlier the artifact correctly records that `thm:main` instantiates at
$P:=\lceil\sqrt{\sigma'q^{+}/\delta}\,\rceil$ — a **ceiling**. Hypothesis (H1) as stated
requires $P\le t$ with $t:=\sqrt{\sigma'q^{+}/\delta}$, and $\lceil t\rceil>t$ whenever $t$
is not an integer, so `thm:main`'s literal parameter **violates (H1)**. The proof then
silently substitutes $\lfloor t\rfloor$, which does satisfy (H1), with no argument bridging
the two. The corollary's arithmetic is correct *for* $\lfloor t\rfloor$; what is not
established is the claim in its title.

The Contract's own `thm:main` handles exactly this ceiling-versus-exact-value issue
explicitly, by carrying an additive slack when it bounds $P\delta\le\sqrt{\sigma'q^{+}\delta}+\delta$.
Corollary G1 has no analogous device. The disclaimer that follows — "this is a statement
about the conjecture, not about $\kappa$" — is an honest statement of scope but arrives
after the title and does not retract it.

Verified independently before upholding: over a grid of $N\in\{2,16,2^{10},2^{20}\}$,
$\sigma\in\{0,2,8,64\}$, $q\in\{0,1,7,10^{2},10^{4}\}$, $\delta\in\{1/N,10^{-3},0.1\}$, the
value $\lceil t\rceil$ exceeds $t$ at **165 of 180** points. The finding is correct and the
overclaim is not a corner case.

Not load-bearing for anything else: nothing in §§3–5 cites Corollary G1, so the defect does
not propagate. Repaired in `split-decomp-kappa-3-r2`.

## ACCEPTED WITHOUT DEFECT

The referee recorded each of the following as checked and correct.

- **§1, Lemma G0.** Case split on $8\sqrt{\sigma'q^{+}\delta}\ge1$ exhaustive;
  $\mathsf{Adv}\le1$ legitimate as a difference of probabilities;
  $\sigma'q^{+}\delta<1/64\Rightarrow q^{+}\delta<1/(64\sigma')\le1/128<2\le\sigma'$ correct,
  with $\sigma'\ge2$ justified from $N\ge2$.
- **§2, Theorem E″'s accounting.** Extraction $6$, fixed-set $1$, query $1$, total exactly
  $8$, matching the stated $C=8$ with no slippage.
- **§2, the quantifier-order Remark.** The referee read `rem:order` and `rem:index` directly
  rather than taking the artifact's word, and confirmed the restriction binds the *family*,
  not the hypothesis *region*; that a region coupling $P$ and $q$ is the same species already
  present and accepted in Theorem E's own third hypothesis; and that this matches what
  `thm:main`'s proof explicitly sanctions. **No violation.** This was the flagged class-(A)
  hazard and it survived.
- **§3, Corollary G2.** $\mu'(0)=\min(0,0,1)=0$ exactly; $\min(qM,N^{2})=0$ at $q=0$; r3's
  Theorem A verified verbatim against the dep file as unrestricted in $M$ **and** in
  resolution at $q=0$; the $5+3=8$ split and
  $P\delta\le3\sqrt{\sigma'\delta}\iff P\le3\sqrt{\sigma'/\delta}$ exact.
- **§4, and its non-load-bearing status.** No citation from §§1–3 into §4; Obstruction O1 and
  Lead L1 labelled unproved throughout; Lead L1's three inequalities each independently
  verified true ($\mathbb E[\log(1/p(\mathbf u))]=H(\mathbf x\mid\cdot)\le2\log N$;
  $\sum_{p<\gamma/N^{2}}p\le\gamma$; $\Pr[H=f\mid\cdot,\mathbf x=\mathbf u]\le X_j(f)/p(\mathbf u)$);
  quotations of card S1, `rem:uses` and `rem:index` verbatim-faithful.
- **§5, the gap register.** Accurately reflects what is and is not load-bearing.
- **All numeric constants** — $2\ln2$, $8$, $6$, $3$, $17$, $1/64$, $1/128$ — recomputed and
  correct.
- **Every citation** of r3's Theorem C, Lemma P, Theorem A and Lemma 1, and of kappa-2-r2's
  Corollaries D′ and D″ and Theorem E, checked word-for-word against the dep files,
  hypotheses and constants included. All faithful.

## SOURCE REQUEST
none

## NOTE ON TRIAGE

F1 was upheld without a separate triage pass. The objection is unambiguous, it was
independently confirmed by the numeric check recorded above before any revision was made, and
the repair strengthens rather than weakens the statement — so the failure mode triage exists
to prevent, a reviser mangling a correct proof to satisfy a spurious objection, is not in
play. This is a deviation from the harness's usual verify-triage-revise order and is recorded
as one.

## LINEAGE

One angle of the five the lineage standard wants. Four remain, as they do for r3.

### END OF FINDINGS split-decomp-kappa-3 ###
