# Concerns: `c/0010/latex/solution.tex`

Reported, not repaired. Nothing in this file was touched in
`solution-revised.tex`. Line numbers are the **original** `solution.tex`.

Read section 1 first. Item C1 is the one I would want checked before anything
else, because it is the only place where the text asserts a bound the proof
below it does not reach.

---

## 1. Suspected errors

### C1. `lem:derand` asserts one $D'$ where the proof produces one per quantity (L93–118)

The statement (L94–98) says:

> For every $q$ and every $q$-query challenge-oblivious $D$ there is a
> deterministic such $D'$ with *(i)* $\Adv_{\mathcal Y,D}\le\Adv_{\mathcal Y,D'}$
> **and** $|\Prob{\Real=1}-\Prob{\Real_0=1}|$ no larger for $D$ than for $D'$ …

That is a single $D'$ satisfying two inequalities at once. The proof (L108–117)
writes "each quantity at issue" as $|\Exp_\rho[\alpha(\rho)]|$, bounds it by
$\max_\rho|\alpha(\rho)|$, picks a maximising $\rho^{*}$, sets
$D':=D_{\rho^{*}}$, and closes with:

> The argument is identical for either paired experiment, giving both parts.

But $\alpha$ is a *different* function for the two paired experiments, so the two
runs of the argument yield two different maximisers $\rho^{*}$, hence two
different $D'$. Nothing in the proof produces a coin string that maximises both
simultaneously, and in general none need exist.

**Why I think this is harmless, and why it still needs a decision.** Every use of
`lem:derand` downstream invokes exactly one conjunct: `thm:A` (L441) and `thm:B`
(L474) both need only the $\Real$ / $\Real_0$ conjunct, since $\kappa$ and
$\kna$ are suprema of that quantity. The $\Adv$ conjunct is never used together
with the other one; see C9. So the fix is likely to be a restatement, not a
repair. Either split (i) into two separately-quantified conclusions, or state the
lemma for one paired experiment and instantiate it twice.

### C2. `lem:prod` item 4 is stated with a factor 2 the proof does not derive (L134, L154–156)

The statement claims $\Prob{m_1m_2>\theta}\le2\delta/\sqrt\theta$. The proof ends:

> For item 4, $m_1m_2>\theta$ with both factors in $[0,1]$ forces
> $m_i>\sqrt\theta$ for some $i$; Markov and item 2 give
> $\Prob{m_i>\sqrt\theta}\le\delta/\sqrt\theta$.

The per-index bound is $\delta/\sqrt\theta$; the factor 2 is the union over
$i=1,2$. That step is one clause and is not written. I did not add it, because
adding an inference to a proof is not a prose edit.

### C3. The symbol $Q$ at L603 is never introduced

> Its lemma *the observer misses the challenge* gives $\Prob{\vx\in Q}\le q\delta$
> in $\mathsf G_2$ …

$Q$ appears once, here, and is defined nowhere in this document. From context it
is the observer's set of query positions, and the preceding sentence speaks of
"$D$ queries $\vx$", which suggests the same object under a different name. If
$Q$ is notation imported from `main.tex`, the Notation paragraph (L78–85) should
list it, since that paragraph is what tells the reader which symbols are being
borrowed.

---

## 2. Unused or unstated hypotheses

### C4. `lem:mass`'s $s=0$ clause is never proved (L356–361, L363–373)

The statement is "For a revealing rule of budget $s\ge1$, … ; for $s=0$ the left
side is $0$." The proof assumes $s\ge1$ throughout, and uses it: $\theta^{*}\le1$
is justified "since $s\ge1\ge\delta$" (L371). The $s=0$ case gets no argument.
It is true, and immediately so ($\mathcal S=\emptyset$ gives $\Pi(\emptyset)=0$),
but "immediately so" is the reader's inference and not the text's. `thm:A` relies
on this clause at L449 ("For $q=0$, $s=0$").

### C5. The $M=1$ carve-out in `lem:P` may be dead (L498–500, against L83)

`lem:P` opens with a parenthetical handling $M=1$: "$\Fun$ is a singleton, so
$\Real_0$ and $\Dec_0$ are the same experiment and the bound holds with left side
$0$; the construction divides by $\log M$ and is stated for $M\ge2$." But the
Notation paragraph already declares, globally, "Throughout $N\ge2$ and $M\ge2$"
(L83). Under that standing hypothesis $M=1$ cannot arise, and the carve-out is
unreachable.

**Question.** Is the carve-out there because `lem:P` is meant to be quotable
outside the document's standing convention? If so, say that where it stands. If
not, the standing hypothesis already covers it and the parenthetical is dead
weight in the middle of a statement.

### C6. The limit at L296 needs $C_0=o(N)$, which is not stated

> at $k_1=1,k_2=N$ one gets $t(1,N)^{2}=(L+N+C_0)/(2N)\to\tfrac12$, so
> $t\to1/\sqrt2$

$C_0=(\sigma+2)\ln2+\ln(4N^{2}/\gamma_0)$ contains $\sigma\ln 2$. The limit
$\tfrac12$ therefore needs $\sigma=o(N)$ and $\log\gamma_0^{-1}=o(N)$, neither of
which is assumed anywhere; $\sigma$ is bounded only by the leakage lengths, which
the setting does not tie to $N$. If $\sigma$ grows linearly in $N$ the ratio does
not tend to $\tfrac12$.

The passage is a remark arguing that the proof does *not* fail through the size
of $t$, and it goes on to say the real failure "is earlier and total", so the
conclusion does not rest on the limit. But as written the limit is asserted
without its hypothesis.

---

## 3. Claims not supported by the evidence given

### C7. "the inequality $\kappa(q)\le\kna(q)$ is false in general" (L570)

Inside the statement of `thm:C`, with no counterexample and no reference. By
[HAL§10] a claim of the form *p does not imply q* owes the reader either a
witness or a citation, and if what is meant is "we tried and failed to prove it",
the text should say that instead. The claim is load-bearing for the sentence it
sits in, which explains why the $D$-relative form of the theorem is used.

Note also that the direction is worth double-checking: $\kna$ is a supremum over
a *subset* of the observers $\kappa$ ranges over (resolution-$1$ observers), so
$\kna(q)\le\kappa(q)$ holds by definition. The sentence asserts the falsity of
the reverse inequality, which is consistent, but the asymmetry is easy to misread
and this is exactly the kind of line the review history says went wrong twice.

### C8. "Lemma 6 is tight at $s=1$ for that example" (L377)

The example is `rem:corr`, whose sources are $2\delta$-unpredictable, not
$\delta$-unpredictable: L169–170 gives $\Exp[m_i]\le2\delta$ and
$\Exp[m_1m_2]\ge\delta$. Writing $\delta'=2\delta$ for the example's actual
parameter, $\mu(1)=\delta'$ while the quantity bounded is $\ge\delta'/2$. So the
bound is tight up to a factor 2, not tight. Either say "tight up to a factor 2",
or rescale the example.

### C9. `lem:derand`'s $\Adv$ conclusion is never used (L96)

The conjunct $\Adv_{\mathcal Y,D}\le\Adv_{\mathcal Y,D'}$ appears in the lemma
and is invoked nowhere: the two citations of `lem:derand` (L441, L474) both use
only the $\Real$ / $\Real_0$ conjunct. By [HAL§11] an unused conclusion sends the
reader hunting for its role. I have not deleted it, because an unused conclusion
is sometimes the symptom of a gap rather than of clutter, and here it interacts
with C1.

### C10. The same claim is made twice with different content (L45–48 against L465–467)

| | |
|---|---|
| L45–48 | "…their cost is the additive $q\delta$, with no multiplier on the leading term and **no dependence on $M$**." |
| L465–467 | "…their cost is the additive $q\delta$, with no multiplier on the leading term and **no $\log M$**." |

Everything before the final clause is near-verbatim identical; the final clauses
are different assertions, and "no dependence on $M$" is the stronger one.
`thm:A`'s bound $5\sqrt{\sigma'\delta}+q\delta$ does support the stronger
reading, since neither $\sigma'$ nor $\delta$ is defined in terms of $M$. If both
are meant, they should be one sentence in one place. I did not unify them,
because choosing either wording would change what the document claims. The
duplication itself is `deferred.md` D14.

---

## 4. Questions arising from proof overviews

One entry per `gaps` item in `proposals.json`. These are the places where the
proof body resisted summary, which is usually where the exposition is thinnest.

### Q1. `ov02` / `lem:prod` (proof L138–157)
The overview cannot place the union over $i=1,2$ that supplies the factor 2 in
item 4, because the body does not contain it. Same as C2.

### Q2. `ov06` / `lem:mass` (proof L363–373)
The overview cannot place the $s=0$ case, because the body does not treat it.
Same as C4.

### Q3. `ov09` / `thm:A` (proof L438–451)
The body bounds the three summands of `prop:master` separately
($\gamma_0=\delta\le\sqrt{\sigma'\delta}$, the middle term by
$3.47\sqrt{\sigma'\delta}$, and $\mu(q)\le q\delta$) but never adds them. **Where
does the constant 5 come from?** From $1+3.47<5$, I assume. One clause would
close it.

### Q4. `ov10` / `cor:A` (proof L459–463)
Same shape: the body gives $5\sqrt{\sigma'q^{+}\delta}$ and
$\sqrt{\sigma'q^{+}\delta}$ and stops. **Where does 6 come from?** From $5+1$.

### Q5. `ov14` / `thm:C`, first gap (proof L574–605)
The body bounds the three adjacent hybrid gaps and stops. The theorem's display
is the sum $\varepsilon(D)+2(\sigma'+\log\gamma^{-1})q/P+\gamma+P\delta+q\delta$,
and the assembly is not written. Note this one is less mechanical than Q3 and Q4:
the second gap's bound as derived is
$q(\sigma+2+2\log(2/\gamma))/P+\gamma$, and getting from there to the display's
$2(\sigma'+\log\gamma^{-1})q/P+\gamma$ uses the two inequalities at L582–583.
**Is the intended reading that $\gamma$ appears once in the display because
`lem:P` was invoked at slack $\gamma/2$ and contributes $2\cdot(\gamma/2)$?** The
text says "Lemma 13 with slack $\gamma/2$ gives … $+\gamma$", so presumably yes,
but the two $\gamma$'s are worth one explicit clause.

### Q6. `ov14` / `thm:C`, second gap
The overview cannot say what the second divergence event is a set of, because $Q$
is undefined. Same as C3.

---

## Sections stated as empty

None. All four sections above have entries.

## Considered and found sound

Recorded so you know these were checked rather than skipped.

- **The numeric chain at L280.** Verified: $L+C_0=1+3\ln N+\sigma\ln2+2\ln2+\ln4+\ln\gamma_0^{-1}$, and $2\ln2+\ln4+1=3.773\le3.78$, $\ln2=0.6931\le0.694$. Then with $\sigma'=\sigma+2.885\ln N$: $3\ln N\le1.040\sigma'$, $0.694\sigma\le0.694\sigma'$, and $3.78\le1.89\sigma'$ using $\sigma'\ge2$, totalling $3.62\le3.63$. The moves are unnamed ([HAL§16], `deferred.md` D15) but the arithmetic is right.
- **The second inequality of `eq:Et`.** $\sqrt{2\delta(3.63\sigma'+\ln\gamma_0^{-1})}\le\sqrt{8\delta(\sigma'+\log\gamma_0^{-1})}$: coefficient of $\delta\sigma'$ is $7.26\le8$, and $2\ln\gamma_0^{-1}\le(8/\ln2)\ln\gamma_0^{-1}$. Holds with room.
- **`thm:A`'s parameter bookkeeping.** $\delta\ge1/N$ gives $\log\gamma_0^{-1}\le\log N$; $\sigma'\ge2\log N$ gives $\log N\le\sigma'/2$; so $\sigma'+\log\gamma_0^{-1}\le1.5\sigma'$ and $\sqrt{8\cdot1.5}=3.464\le3.47$. Correct.
- **`t(1,N)^{2}=(L+N+C_0)/(2N)$** at L296. Substituting $k_1=1,k_2=N$ into $t$ gives numerator $\ln(eN)+N\ln e+C_0=L+N+C_0$ and denominator $2N$. Correct; only the limit needs a hypothesis (C6).
- **`cor:B`'s two thresholds.** $qM\delta\le\sqrt{\sigma'q^{+}\delta}$ from $qM^{2}\delta\le\sigma'$, and the disjointness computation ending at $M>\sigma'/\sqrt{27\delta}$. Checked.
- **`thm:cprime`'s $6+1+1=8$.** The only proof in the document that closes its own arithmetic explicitly.
- **The redundant `\min(\cdot,1)` in `lem:mass`.** $\Pi_{f,\zeta}$ is a probability measure, so $\Pi(\mathcal S)\le1$ and the truncation is vacuous. Harmless; it makes the *bound* $s\,m_1m_2$ safe to state, which is presumably why it is there. Not an error.
