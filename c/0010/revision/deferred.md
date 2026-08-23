# Deferred edits: `c/0010/latex/solution.tex`

Edits I judge correct but did not apply, because each either restructures the
document, deletes prose, or changes a math span. Line numbers are the
**original** `solution.tex`. Numbered in reading order; the two I would do first
are D1 and D11.

The fifteen proof overviews are the largest deferred item; they live in
`proposals.json` rather than here, one JSON patch each, with a `step_map`, a
`gaps` list and a risk grade. Five are graded HIGH and want checking before use:
`ov02`, `ov06`, `ov09`, `ov10`, `ov14`.

---

## Notation

### D1. Retire one of the two meanings of $\theta$ [HAL§6][KNU14]

The highest-value edit in this file. $\theta$ is the test $[M]\to\bits$
throughout, and simultaneously a real threshold in $(0,1]$ in `lem:prod`(4)
(L134) and in the proof of `lem:mass` (L367–372, with $g(\theta)$ and
$\theta^{*}$). Both meanings are live inside one proof, since `lem:mass` invokes
`lem:prod`(4). Rename the threshold, to $\tau$ or $\vartheta$; the test should
keep $\theta$, being the more prominent object.

Touches L134, 367, 368, 369, 370, 371, 372. Math change, hence deferred.

### D2. Reduce the depth of $p_{\theta_{\zeta,f}}$ [KNU15][GOL-NOTA]

A subscript on a doubly-subscripted object, at L228, 245, 346, 384. Knuth's rule
names this as a reliable source of error including for the author. Either write
$p(\theta_{\zeta,f})$, or give the test a short name once $\zeta$ and $f$ are
fixed, which the document already does informally at L121–122 ("write
$\theta:[M]\to\bits$ for that function and $p_\theta:=|\theta^{-1}(1)|/M$") and
could do formally.

### D3. Slash the inline fractions [KNU-FRAC]

Two sites, both setting microscopic type:

- L219, inside the statement of `lem:disc`: `\ln\frac{4N^{2}}{\gamma_0}` →
  `\ln(4N^{2}/\gamma_0)`.
- L259: `e^{-k_1\ln\frac{eN}{k_1}}` → `e^{-k_1\ln(eN/k_1)}`. A `\frac` inside an
  exponent inside inline math is two levels of shrinkage.

The second also relieves the overfull hbox at L258–266 and would let the reverted
edit **R1** (`revision-report.md`, Pass 7) be reapplied.

### D4. Break the two long inline formulas onto displays [KNU-BREAK][HAL§17]

Both are pre-existing overfull hboxes, and both resist a prose fix, which is why
edits R1 and R2 were reverted.

- L383, in `lem:ident`:
  `$\Prob{\Real=1}=\Exp_{(f,\zeta)}\bigl[\Exp_{\vx\sim\Pi_{f,\zeta}}[\theta_{\zeta,f}(f(\vx))]\bigr]$
  is 19.6pt over the measure. Displaying it, and the companion
  $\Prob{\Real_0=1}$ identity with it, fixes the box and lets the reverted edit
  **R2** be reapplied.
- L259, as above under D3.

The remaining three overfull boxes (L126–131, L276–283, L515–525) are the same
species and yield to the same treatment.

### D5. One shared theorem counter, or double numbering by section [GOL-NUM]

`conjura-conjecture.cls` declares `theorem`, `lemma`, `proposition`, `corollary`,
`definition` and `remark` on six independent counters, so the document runs
Lemma 1, Lemma 2, Remark 1, Lemma 3, Definition 1, Lemma 4, … and the reader
cannot binary-search for an item by number. `\newtheorem{lemma}[theorem]{Lemma}`
gives a shared counter; `\newtheorem{theorem}{Theorem}[section]` gives double
numbering.

Deferred for two reasons beyond the usual: it changes every cross-reference in
the rendered document, and the class file is **shared across the repository**, so
the change is not local to `c/0010`.

---

## Statements

### D6. Move the chit-chat out of `thm:C` (L568–571) [HAL§11]

Inside the theorem statement:

> Since $\varepsilon(D)\le\kappa(q)$, the same holds with $\kappa(q)$ in place of
> $\varepsilon(D)$; but the $D$-relative form is what Theorem 15 uses, and the
> inequality $\kappa(q)\le\kna(q)$ is false in general and nowhere needed.

Two sentences of commentary, a forward reference, and a claim about what is
"nowhere needed", all inside a statement that reviewers and citers will read out
of order. Move them to the paragraph after the proof, where the document already
puts commentary of exactly this kind (L630–633). The claim itself is
`concerns.md` C7.

### D7. Move the vacuity remark out of `cor:A` (L454–456) [HAL§11]

> Outside that regime $q^{+}\delta>\sigma'\ge2$, so
> $\sqrt{\sigma'q^{+}\delta}>\sigma'>1$ and the target bound is vacuous.

A second sentence carrying its own justification inside a corollary. It belongs
just after the proof. Note that keeping it *somewhere* matters: it is what tells
the reader the hypothesis $q^{+}\delta\le\sigma'$ costs nothing, which is
[HAL§11]'s requirement that degenerate cases be stated rather than passed over.

### D8. Move the $M=1$ carve-out out of the middle of `lem:P` (L498–500) [HAL§11]

The parenthetical currently sits between "Let $P\in\mathbb N$ and
$\gamma\in(0,1)$." and "There is a family …", so the reader meets a degenerate
case before the claim. Put it at the end of the statement, or drop it if
`concerns.md` C5 resolves that the standing $M\ge2$ already covers it.

### D9. Label two definitional choices [GOL-CHOICE]

- **`def:rr` (L207–215).** The test must be "a function of $\zeta$ and the
  inspected values alone". This looks *seemingly essential* in Goldreich's sense:
  it is exactly what makes the union bound in `lem:disc` run over
  $|\mathcal Z|<2^{\sigma+2}$ rather than over $2^{M}$ tests, which `rem:one`
  (L285–292) says is the one place the route beats a Fourier analysis. Saying so
  at the definition would pay for itself.
- **`lem:disc` (L219).** $C_0:=(\sigma+2)\ln2+\ln(4N^{2}/\gamma_0)$ is a
  low-level choice presented without comment. I believe it is *adopted for
  simplicity*: it is whatever makes the three exponential factors cancel at
  L262. But I am not certain it is not *seemingly essential*, so I have not
  proposed a label; see the question in D11.

### D10. Motivate `def:rr` before it arrives (L207) [KNU12][GOL-GEN]

The reader meets *revealing rule* as an abstraction two pages before learning
that an observer is one (`lem:rr`, L328). One sentence before the definition,
saying that this is the shape an observer will be shown to have, would fix it.
Alternatively move `def:rr` down to sit next to `lem:rr`; `lem:disc` is the only
thing between them that needs it, and it needs it in its statement, so the move
is not free.

---

## Proofs

### D11. Derive $C_0$ and $t$ forward instead of asserting them [HAL§16]

`lem:disc` states $L$, $C_0$ and $t(k_1,k_2)$ as given (L218–222), and the proof
then verifies that everything cancels ("By the definition of $t$, … Multiplying,
all three exponential factors cancel", L258–262). This is the backward form
Halmos objects to: machine-verifiable and opaque to a person. Nobody reading it
learns *why* $t$ has that shape.

The forward version writes down what the union bound needs, namely
$2\exp(-2\lambda^{2}/n_0)\cdot|\mathcal Z|\binom{N}{k_1}\binom{N}{k_2}\cdot N^{2}\le\gamma_0$,
and solves for $t$, at which point $C_0$ is visibly "the log of everything the
union runs over" and the $k_i\ln(eN/k_i)$ terms are visibly the binomial
coefficients. This is a rewrite of one proof and one statement, so it is
deferred; it is also the edit most likely to make the paper's central lemma
readable.

**Question for the author, which D9 depends on.** Is the $4$ in $4N^{2}/\gamma_0$
load-bearing, or slack? The proof spends it as $\gamma_0/2\le\gamma_0$ at L265,
which suggests a factor 2 of headroom is deliberate and the other factor 2 is
absorbed by the two-sided Hoeffding bound.

### D12. Name the moves in the numeric chain at L279–282 [HAL§16]

> Numerically
> $L+C_0=1+\ln N+(\sigma+2)\ln2+\ln4+2\ln N+\ln\gamma_0^{-1}\le3\ln N+0.694\sigma+3.78+\ln\gamma_0^{-1}$;
> as $\sigma'\ge2.885\ln N$ and $\sigma'\ge2$ for $N\ge2$, this is at most
> $3.63\sigma'+\ln\gamma_0^{-1}$

Two inequalities, four numeric constants, and no statement of what was done.
Halmos's rule for a chain of relations is to add a sentence naming the moves. The
moves here are: collect the three $\ln N$ terms; round $\ln2$ up to $0.694$ and
$1+2\ln2+\ln4$ up to $3.78$; then convert $\ln N$ and the constant into $\sigma'$
using $\sigma'=\sigma+2.885\ln N$ and $\sigma'\ge2$. The arithmetic is correct, I
checked it (`concerns.md`, *Considered and found sound*); it is the invisibility
of the moves that is the defect.

Deferred because the fix is an added sentence, which the proposal contract routes
through `proposals.json` rather than the source. It is not among the fifteen
overview patches because it is a `unpacking` addition inside a proof body, and
nothing may be inserted inside a proof except its opening overview.

### D13. Hierarchical structure for the two 45-line proofs [LAM-LEVELS]

`lem:disc` (L238–283) and `lem:P` (L514–558) both exceed 40 lines and both
already carry run-in `\emph{...}` step headings, which is most of the way to a
numbered hierarchy. `thm:C` (L574–605) has three paragraphs standing for three
hybrid steps and no headings at all; it would gain most.

Deferred because [LAM-LEVELS] and [HAL§12] point opposite ways here and both have
distinguished advocates: Lamport would number the steps in place, Halmos would
extract the $\mathsf G_2\to\mathsf G_3$ coupling in `thm:C` as its own lemma,
since it is a self-contained argument about overwriting one cell. I would take
the Halmos route for `thm:C` and the Lamport route for `lem:P`, but that is a
judgement about this paper that belongs to its author.

---

## Subtraction

These two are the answer if a page limit ever applies. D14 and D15 together
recover roughly 45 words, more than reversing this revision's +14.

### D14. Resolve the duplicated (A) commentary (L45–48 and L465–467) [HAL§12][GOL-CHECK]

Near-verbatim duplication whose final clauses differ mathematically. Halmos's
rule is to repeat deliberately and then *mark* the difference; as it stands the
reader must diff two paragraphs to find it. Resolving it requires deciding which
claim is meant, which is `concerns.md` C10, which is why this is not a
subtraction I can perform. Once decided, one of the two shrinks to a pointer.

### D15. Delete one copy of the review-species characterisation (L68–69 or L726) [GOL-CHECK]

> both of the same species: a claim left underdetermined rather than false

appears in the Reader's guide and again in `\S sec:review`. Here the content
**is** identical, so one copy is genuinely removable, unlike D14. I would cut the
Reader's-guide copy, since that paragraph already forward-references
`\S sec:review` for the full status and its own job is done by the two named
locations that follow. Thirteen words. I did not cut it because removing a
characterisation from someone else's assessment of their own work is their call.

### D16. The unused half of the [CFHS, Lemma 4.3] restatement (L708) [SU-RH]

> $(n/k)^{k}\le\binom nk\le(en/k)^{k}$

Only the upper bound is used, at L261. The lower bound is a red herring in
Su's sense: a stated fact that plants an expectation and is never met. It sits
inside an italic restatement of an external result, so cutting it edits a
quotation of someone else's lemma; that is the author's call, and the honest
alternative is to keep it and mark it, as the list already does elsewhere
("Used only for the compression arm", L713).
