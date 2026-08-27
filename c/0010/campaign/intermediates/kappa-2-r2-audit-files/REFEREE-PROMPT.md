# Referee package — `split-decomp-kappa-2-r2`

You are refereeing ONE artifact, and it has **never been refereed before**. Judge it on its own
terms and on the files listed here. Do not consult the wider repository, and do not assume
anything about the project these files do not state.

## Every file in this package, named individually

| file | what it is | status |
|---|---|---|
| `ARTIFACT.md` | **the artifact under review** — `split-decomp-kappa-2-r2` | JUDGE THIS |
| `CONTRACT.md` | the conjecture statement, definitions and remarks | YARDSTICK — assume correct |
| `deps/DEP-r3-kappa-1-r3.md` | supplies Lemma 3 steps (1)–(3), Lemma 4, Theorem A, Theorem C, Lemma P, Lemmas 0–2, and r3's own Lemma 5 / `mu` | GIVEN — assume its results hold as stated |
| `cards/S1-cdgs-card.md` | source card, Coretti–Dodis–Guo–Steinberger, ePrint 2017/937 | GIVEN |
| `cards/S2-cfhs-card.md` | source card, Coretti–Farshim–Harasser–Southern, ePrint 2025/1258 | GIVEN |

That is five files: `ARTIFACT.md`, `CONTRACT.md`, one file in `deps/`, two in `cards/`. If you
cannot open one, report it as a class-(E) packaging finding rather than working around it.

## What the artifact claims

Its own results, in its own numbering:

- **Lemma A** — a second-moment sharpening, notably `E[sqrt(m1 m2)] <= delta`, via Cauchy–Schwarz
  across the two coordinates.
- **Lemma B** — rectangle discrepancy quantified over **all** `2^M` tests `theta : [M] -> {0,1}`,
  paying `M ln 2` inside `C_1`, with **no** revealing rule and no excised set.
- **Theorem D** and **Corollary D′** — a `q`-free extraction bound
  `kappa(q) <= 5 sqrt(sigma' delta) + 2 delta sqrt(M)`, claimed for **every** challenge-oblivious
  observer, of any query count and any challenge resolution.
- **Lemma C**, **Theorems A⁺/B⁺**, **Corollary D″** — the revealing-rule arm, sharpened, and the
  two-arm bound.
- **Theorem E** — the conjecture on a region.
- **Proposition F** — the only lower bound: `kappa(N^2) >= delta sqrt(M)/(4 sqrt 2)` on the
  diagonal `delta = 1/N`.

## Questions a referee should settle

1. **Lemma A(a).** `E[sqrt(m1) sqrt(m2)] <= sqrt(E[m1]) sqrt(E[m2]) <= delta` — is the
   Cauchy–Schwarz step legitimate given that `m1` and `m2` are **not independent** (both are
   functions of the same `f`)? State precisely what Cauchy–Schwarz needs and whether it holds.
2. **Theorem D's scope.** It is claimed for observers of *unbounded* query count. Verify that
   nothing in its proof, or in the derandomisation lemma it invokes, refers to a query bound.
   An observer that reads all of `f` is admitted — check the claim survives that.
3. **Every constant in §5 and §6**, including those inside parentheticals. Re-derive each
   numeric coefficient from the definitions rather than checking the arithmetic as printed. Pay
   particular attention to whether any term is **double-counted** — i.e. appears both as its own
   summand and inside another constant.
4. **Lemma B step (3).** The count of tuples is `binom(N,k1) binom(N,k2) 2^M`. Is the union bound
   over the right set, and do the three exponential factors cancel exactly as claimed?
5. **Corollary D″.** Does it really hold "with no restriction on the observer", and is each arm
   correctly attributed as conditional or unconditional?
6. **Proposition F.** Check the `E|Y| >= s/2` claim in step (4) and the statistical-distance
   identity in step (3), including that the advantage equals `E_f[SD]` with no cancellation.
7. **Citation fidelity into `deps/`** — quote what you checked.

## How to report

Classify each finding: **(A)** claims something not established, or states itself falsely;
**(B)** a computational or algebraic error; **(C)** a gap — true but not licensed by what
precedes; **(D)** an imprecision not threatening the result; **(E)** a packaging failure on the
requester's side.

Give a verdict of **CLEAN** or **DEFECTS**. Be adversarial: your job is to find what is wrong.
If it is correct, say so plainly and name the steps you verified and how. Do not soften a
finding to be agreeable, and do not manufacture one to seem rigorous.
