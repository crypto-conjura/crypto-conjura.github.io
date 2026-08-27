# Blind audit of `split-decomp-kappa-4` — six referees, verdict DEFECTS

Six independent passes in fresh context, spanning two model families, against a freshly built
package (`kappa-4-audit-files/`, every file named individually in the prompt after the r2 pass of
`kappa-3` lost two card checks to a directory named without its contents). Five referees judged the
artifact; one judged three unmerged simplification claims (`kappa-4-simplification-audit/`).

| pass | lens | family | verdict |
|---|---|---|---|
| 1 | Lemma H0, the definitional step | verifier | DEFECTS (H0 itself CLEAN) |
| 2 | arithmetic and constants | verifier-b | DEFECTS (**no class-(B) error**) |
| 3 | quantifier order | verifier | DEFECTS |
| 4 | case coverage, boundaries, degenerate instances | verifier-b | DEFECTS |
| 5 | citation fidelity and meta-claims | verifier | DEFECTS |
| 6 | simplification claims A, B, C | verifier-b | A and C corrected, B sound |

## Confirmed, after adversarial attempts to break it

- **Lemma H0 is correct.** Four referees attacked it independently, each trying to construct a
  reading of `def:bf` on which a $P_0$-mixture with $P_0\le P$ fails to be a $P$-mixture. None
  could. Pass 1 corroborated the "at most $P$" convention against card S1's quotation of
  [CDGS, Definition 1]; pass 4 noted `def:bf`'s closing sentence cuts in the artifact's favour,
  since `lem:hit` then costs $P_0\delta\le P\delta$.
- **No arithmetic error.** Pass 2 re-derived all three Lemma H1 bounds and both case-(b) chains by
  hand, and reproduced both reported grid sizes (16644, 12852) exactly, including the collision
  counts. It confirms $c=2$ and that $C=13$ — not 12, not 14 — follows from the displayed
  inequalities rather than from the grid.
- **Case coverage is exhaustive** on $\mathbb N$ with no boundary gap (passes 2, 4).
- **No `rem:index` violation**, and no leak of $D$, $\mathbf x$ or the challenge into either family
  (passes 1, 3, 4).

## Upheld findings, all repaired in `split-decomp-kappa-4-r2`

| id | class | raised by | finding |
|---|---|---|---|
| B1 | A | 3, 4, 2 | Theorem H′ leaves $q$ free in its hypothesis and rebinds it in the conclusion; literal reading is vacuously hypothesised at $q=0$ and contradicts §4. Correct hypothesis is **(H2) at every $q$**, i.e. $M\le\sigma'/(2\delta)$ |
| B2 | A | 5, 2 | $A\ne\sigma'$: `rem:reduces` caps with $A:=\sigma+2+\log(1/\gamma)$, diverging from $\sigma'$ as $\gamma\downarrow0$. "The same capping, at the same point" and "reproduces" were false |
| B3 | A | 1, 2, 4, 5 | "*Exactly* the price of $q$-independence, and nothing else" claims necessity from an achievability result, contradicts §4, and overrides `kappa-3-r4` §4's `rem:second`, which had warned the two $\sqrt{q^{+}}$ are different objects (a separation in $P$ vs a degradation of $C$) |
| B4 | A | 2 | The grid was misdescribed: the vacuity filter forced $q^{+}<410$, so **no point with $q\ge10^{3}$ was ever evaluated** and $\sqrt{q^{+}}$ reached only $\sqrt{11}$ |
| B5 | C | 1, 2, 3, 4 | $N,M\ge2$ used three times, never stated; $\sigma'\ge2$ asserted with no derivation. At $N=1$, $\gamma_0=1\notin(0,1)$, "$N^{-2}\le1/4$" is false, and $P_0=0\notin\mathbb N$; at $M=1$ Lemma P declines to construct |
| B6 | A | 3 | Summary lines ("closes completely", "an artefact of the quantifier order alone") scoped wrongly against §3–§4's own narrower claims |
| B7 | A | 5 | §6's register omitted Lemma P, Corollary D″, `rem:index`, `rem:order`; and Theorem H's self-description read as literal `conj:main` |
| B8 | D | 1, 5 | Corollary G2 credited with a fact shown inside its proof |
| B9 | D | 2, 4 | "(H2) is a condition on $M,q,\delta$ alone" omits $N,\sigma'$; "$P\delta$ never exceeds $S$" is off by $\delta$; Lemma H1 titled "two bounds", states three |
| B10 | D | 2 | Worst observed constant printed as $12.0000$, rounding away the strict inequality ($12.0000000075$) that is the only reason the number matters |

**One finding adjudicated and its witness replaced.** Pass 4's instance for B1 ($N=2^{10}$,
$\sigma=0$, $\delta=2^{-10}$, $M=2^{20}$) is vacuous at both $q=0$ and $q=1$ — $8S>1$ — so the
target exceeds $1$ and the claim holds trivially there. The finding is nonetheless correct; a
non-vacuous witness is $N=2^{12}$, $\sigma=0$, $\delta=2^{-12}$, $M=2^{16}$, recorded in r2 §3.

**Class (E), charged to the requester.** `PROGRESS.md` is cited for campaign-status claims and was
not in the package. Three referees recorded those as unverifiable in scope; one issued a source
request; one disclosed reading it out of package and correctly noted it is not independent
corroboration, having been written concurrently with the artifact. The §5 claims sourced to the
*dependencies* were checked and confirmed against DEP-A and DEP-B's own text.

## Simplification claims (pass 6)

- **Claim A — SOUND WITH CORRECTIONS.** A1, A2, A5 verified. **A4 refuted**: the additive $1$ in
  (H1) is load-bearing for Theorem H′ as written, for `kappa-3-r4`'s stated `conj:main` gain, and
  for `rem:window`'s endpoint; and findings F3 and A3 of that document are not about rounding at
  all. **A3 corrected**: the verbatim floor substitution gives $13.25$, i.e. $C=14$; $C=13$ is
  recovered only after sharpening Lemma H1 to $N^{-2}\le S/4$, which r2 now does.
- **Claim B — SOUND WITH CORRECTIONS.** B1–B5 verified. Theorem D's independence of the
  revealing-rule apparatus was confirmed **by enumeration** and corroborated by `kappa-2-r2` §9's
  own gap register. Corrections: (H2′) is strictly stronger than (H2) at $q=0$, costing the
  unconditional $q=0$ case and `kappa-3-r4`'s factor $2$ in $M$; the $M\in\{2,3\}$ corner is
  harmless; and Lemma 3 is retained, so the apparatus is degenerated rather than eliminated.
- **Claim C — REFUTED on framing.** The two arms of (H2) are *not* one union bound priced twice.
  $2\delta\sqrt M$ is a description-length price; $\mu'(s)$ is a *revelation* price from a step with
  no counterpart in Theorem D; and the true analogue of $M\ln2$, namely $(\sigma+2)\ln2$, never
  becomes an arm — it is absorbed into the shared $5\sqrt{\sigma'\delta}$.

### END OF FINDINGS split-decomp-kappa-4 ###
