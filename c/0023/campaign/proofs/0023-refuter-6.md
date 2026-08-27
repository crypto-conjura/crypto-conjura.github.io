id: 0023-refuter-6
agent: refuter
model: claude-opus-5[1m] (Opus 5, 1M context)
cycle: 4
status: COMPLETE

# [G5] settled: unrestricted **minimal**-certificate selections keep the expected window size at $d+O(\log d\log\log d)$ on both of the artifact's witnesses — but only because the point is drawn **uniformly**; a point-mass selection is capped at exactly $2^{-d}$

## VERDICT

**G5 SETTLED POSITIVELY**, in the sense of §7.4's own definition of *selection*
(a choice, for each $x$, of one minimal certificate of $x$, with
$x\sim\mathrm{Unif}(A)$ supplying the randomisation of Remark 2.2):

> **(V1)** On witness (a) ($A_k,B_k$, $d=k+1$), **every** minimal-certificate
> selection — including the adversarial one that always takes the *largest*
> minimal certificate of its point — has
> $$d\ \le\ \mathbb E|W(A_k)|\ \le\ B(k)\ \le\ d+8\log_2 d\,\log_2\log_2 d+24\log_2 d+1 ,$$
> with $B(k)$ an exact rational union bound (table in §3). Exact values of the
> adversarial rule: $\mathbb E|W|=2,\ \tfrac{25}8,\ \tfrac{553}{128},\
> \tfrac{182001}{32768},\ \approx6.8122,\ \approx8.0880$ for $k=1,\dots,6$ —
> i.e. $d+0,\ d+0.125,\ d+0.320,\ d+0.554,\ d+0.812,\ d+1.088$. The
> $2^{d-1}$-size minimal certificate of [G5] exists but is carried by a
> $2^{-(2^{d-1}-1)}$ fraction of the points and contributes
> $2^{d-1}2^{1-2^{d-1}}$ to the expectation.
> **(V2)** On witness (b) ($C,D$) minimal certificates **are** the minimum ones
> (proved in §5, verified exhaustively for $d\le4$), so §7.4's numbers hold
> verbatim for minimal selections; [G5] is empty there.
> **(V3)** Consequently CAP I(b)/Remark 2.2 reads off witness (a), for the
> worst minimal selection, the ratio $\mathbb E[\pi]/\mathbb E[|W(A)|+|W(B)|]$
> $=\tfrac14,\tfrac{17}{100},\tfrac{313}{2212},\tfrac{32107}{242668},
> \approx0.1309,\approx0.1326$ ($k=1..6$), and $\ge(k-U(k))/(4B(k))\ge0.070$
> for **every** $k\ge2$ ($\tfrac1{16}$ at $k=1$, where the exact value is
> $\tfrac14$), rising to $0.247$ at $k=4096$. **Witness (a) contributes
> no cap below a constant for the minimal variant either**: §7.4's escape claim
> extends from minimum-size to unrestricted minimal selections, and the
> "P5 must therefore declare its selection rule" caveat can be discharged to
> "P5 must declare that the point is uniform".

**One negative half, and it is load-bearing for drafting (§7).** Remark 2.2
literally allows *any* $\mu_A$ depending only on $A$. Under that wider reading
the rule "$W(A):=$ the largest minimal certificate of the lexicographically
first point of $A$ that has one" is a legitimate localised deterministic
window functional, on witness (a) it returns all $2^{d-1}$ targets on both
sides, and CAP I(b) caps it at **exactly $2^{-d}$** (exact certificate, two
independent methods, §7). So the positive verdict is *conditional on the
uniform-point averaging that P5 declares*, and that averaging is now a stated
hypothesis of the escape, not a stylistic choice.

**Beyond the two witnesses: NO COUNTEREXAMPLE IN REGIME, and the general
question is genuinely open** (§8). It reduces exactly to: *how large can
$\rho(A):=\mathbb E_{x\sim\mathrm{Unif}(A)}[\max\{|S|:S$ a minimal certificate
of $x\}]$ be for a degree-$\le d$ set?* Records found (exact, verified):
$\rho^\ast(d)\ge1,\ 3,\ \tfrac{21}4,\ 7,\ \tfrac{33}4$ for $d=1..5$, i.e.
$\rho/d\le1.75$ throughout, against the only upper bound available in general,
the junta bound $\rho\le M(d)=O(2^d)$. **No superpolynomial $\rho$ was found**
in: all sets on $r\le4$; all degree-$\le2$ sets on $r\le6$; the *complete*
degree-$\le3$ classes $L(4,3)$, $L(5,3)$, $L(6,3)$ ($16{,}750{,}860$ sets,
max $\rho=5$); a uniform sample of $L(7,3)$; $400$ random cosets; degree-safe
hill climbing at $d\le5$, $r\le11$ seeded with every record object. The affine
class is *proved* capped at $2d-1$ (§8.3), attained by the Hamming-code family,
so **no counterexample exists in the whole affine class, for every $d$**. But I
also **refuted my own envelope**: a degree-$3$ set on $7$ coordinates with
$\rho=\tfrac{21}4>2d-1=5$ exists (verified by three independent code paths,
§8.6), so no clean linear ceiling is available and small-$d$ data cannot
separate poly from $2^{\Theta(d)}$. What is quantified is the *obstruction*: a
counterexample must exhibit $\ge2^{s-d}$ prime implicants of codim
$s=2^{\Omega(d)}$ in one degree-$\le d$ set (§8.5); the address family has
$2^{O(d\log d)}$ at that depth, doubly exponentially short.

---

## 0. What was computed, and the two definitions kept apart

Verbatim from `proofs/0023-prover-3-r3.md` §7.4: for $x\in A$, $S$ is a
**certificate** if every $y$ agreeing with $x$ on $S$ lies in $A$; **minimal**
if no proper subset is one; **minimum** if of least size. A **selection** is a
choice, for each $x$, of one such certificate; the window is randomised
(Remark 2.2) through $x\sim\mathrm{Unif}(A)$. §7.4 evaluated **minimum**-size
selections; [G5] is the **minimal** case.

A standing identification used throughout (elementary, and the reason the
question is tractable): *$S$ is a minimal certificate of $x$ iff the subcube
$\{y:y_S=x_S\}$ is a maximal subcube contained in $A$, i.e. a **prime
implicant** of $A$ containing $x$.* Hence
$$\rho(A)\ :=\ \mathbb E_{x\sim\mathrm{Unif}(A)}\bigl[\max\{|S|:S\text{ a minimal certificate of }x\}\bigr]$$
is the expected window size of the **worst** minimal selection, and every
selection rule (uniform among minimal, lexicographic, greedy-shrink, any
adversarial choice) has expected window size in
$[\,\mathbb E_x C_x(A),\ \rho(A)\,]$, where $C_x(A)$ is the minimum certificate
size at $x$ (§7.4's rule).
Two further facts fix the stakes: $\Pr_{x\sim\mathrm{Unif}(A)}[x\in Q]=2^{-|S|}/\alpha_A\le2^{d-|S|}$
for a codim-$|S|$ subcube (using $\alpha_A\ge2^{-d}$, T4(a)), and
$\pi_{\mathrm{Rel}}(A,B)\le\sum_i\mathrm{Inf}_i(f_A)+\sum_i\mathrm{Inf}_i(f_B)\le2d$.

## 1. Structure of the minimal certificates of witness (a) (proved, then verified generically)

Coordinates $a_1..a_k$, $y_j$ ($j\in\{0,1\}^k$), $A_k=\{y_{b(a)}=+1\}$,
$d=k+1$. Fix $x\in A_k$, let $j_0=b(a)$ and $P=\{j:x_{y_j}=+1\}\ni j_0$. For
$S\subseteq[N]$ put $U:=\{t:a_t\notin S\}$ and $Q_U:=j_0\oplus\{0,1\}^U$.

**Lemma 1.** *$S$ is a certificate of $x$ iff $Q_U\subseteq P$ and
$\{y_j:j\in Q_U\}\subseteq S$. Hence the minimal certificates of $x$ are
exactly*
$$S_U=\bigl([k]\setminus U\bigr)\ \cup\ \{y_j:j\in Q_U\},\qquad
U\subseteq[k]\ \text{with}\ Q_U\subseteq P,\qquad |S_U|=k-|U|+2^{|U|},$$
*and $\{U:Q_U\subseteq P\}$ is a downset containing $\emptyset$.*

*Proof.* Points agreeing with $x$ on $S$ realise exactly the addresses
$j_0\oplus v$, $v$ supported on $U$; for each such $j$ the target $y_j$ must be
in $S$ (else it can be set to $-1$) and must already be $+1$ at $x$; this is
also sufficient. So every certificate contains $S_U$ and $S_U$ is one. As
$S\cap\{\text{address bits}\}=[k]\setminus U$ by definition of $U$, a minimal
$S$ has no spare targets, so $S=S_U$. Conversely for $S'\subsetneq S_U$: if
$S'$ frees no further address bit it misses a needed target; if it frees one,
$Q_{U'}\supsetneq Q_U$ needs a target $S'$ does not contain. Downset:
$U'\subseteq U\Rightarrow Q_{U'}\subseteq Q_U$. $\square$

**Distribution.** $x\sim\mathrm{Unif}(A_k)$ is: $j_0$ uniform, $x_{y_{j_0}}=+1$,
the other $2^k-1$ targets i.i.d. uniform. Hence
$\Pr[U\text{ valid}]=2^{-(2^{|U|}-1)}$ and
$\mathbb E[\#\{\text{minimal certificates of size }k-u+2^u\}]=\binom ku2^{1-2^u}$.
Minimum size is $d$, attained exactly at $u\in\{0,1\}$ (§7.4's claim,
re-derived).

**Verification, method 2 (generic, no structure).** `s1_witness_a_generic.py`
computes, for $k=1,2,3$ ($N=3,6,11$) and for **both** sides, all minimal
certificates of all points from the truth table alone, via
$\mathrm{cert}[S\setminus i]=\mathrm{cert}[S]\wedge\mathrm{cert}[S]^{\oplus i}$
and the minimality filter; the output agrees with Lemma 1 **set for set at
every point** (an `assert`, not a size comparison), and an independent slow
per-point subset scan agrees on a sample of points. At $k=4$ ($N=20$, where the
$2^N\times2^N$ table is out of reach) `s3_witness_b_and_k4.py` verifies the
predicted family over **all $2^{19}$ points** by truth-table AND-folds on the
$3^k=81$ candidate masks, and probes completeness by batched greedy shrinking
in 6 random coordinate orders (0 outcomes outside the family).

## 2. Exact distributions and the selection rules ($k\le4$, both sides)

Multiset of minimal-certificate sizes over all (point, certificate) pairs, and
per-point multiplicities (identical on the $A$ and $B$ sides):

| $k$ | $d$ | sizes (size: #pairs) | multiplicities | per-point max size |
|---|---|---|---|---|
| 1 | 2 | $\{2:6\}$ | $1..2$ | $\{2:4\}$ |
| 2 | 3 | $\{3:64,\ 4:4\}$ | $1..4$ | $\{3:28,\ 4:4\}$ |
| 3 | 4 | $\{4:2560,\ 5:384,\ \mathbf{8:8}\}$ | $1..8$ | $\{4:720,\ 5:296,\ \mathbf{8:8}\}$ |
| 4 | 5 | $\{5:3,\ 6:\tfrac34,\ 9:\tfrac1{32},\ \mathbf{16:2^{-15}}\}$ (expected counts per point) | — | $\{5:279040,\ 6:230176,\ 9:15056,\ \mathbf{16:16}\}$ |

(Expected number of minimal certificates per point: $\tfrac32,\tfrac{17}8,
\tfrac{369}{128},\tfrac{123905}{32768}$ for $k=1..4$; at $k=3$ this
cross-checks the generic enumeration exactly — $2560/1024=\tfrac52$,
$384/1024=\tfrac38$, $8/1024=\tfrac1{128}$.)

Expected window size $\mathbb E|W|$ ($x\sim\mathrm{Unif}(A_k)$), exact:

| rule | $k=1$ | $k=2$ | $k=3$ | $k=4$ |
|---|---|---|---|---|
| MIN (minimum-size, = §7.4) | $2$ | $3$ | $4$ | $5$ |
| lexicographically first | $2$ | $3$ | $4$ | — |
| greedy shrink, targets first | $2$ | $3$ | $4$ | — |
| UNIF (uniform among minimal) | $2$ | $\tfrac{97}{32}$ | $\tfrac{146301}{35840}$ | $\tfrac{121504303861}{23616552960}\!\approx\!5.1449$ |
| lexicographically last | $2$ | $\tfrac{25}8$ | $\tfrac{551}{128}$ | — |
| greedy shrink, address bits first | $2$ | $\tfrac{25}8$ | $\tfrac{551}{128}$ | — |
| **MAX (adversarial minimal)** | $2$ | $\tfrac{25}8$ | $\tfrac{553}{128}$ | $\tfrac{182001}{32768}$ |

Every rule sits in $[d,\ \rho]$ with $\rho-d\le0.56$ at $k\le4$; the *minimum*
of the rule-wise expectations is exactly $d$, the *maximum* is $\rho$.

## 3. All $k$: the adversarial rule is $d+O(\log d\log\log d)$

With $u_{\max}$ the largest valid $U$'s size and $\mathrm{size}(u)=k-u+2^u$
non-decreasing,
$$\rho=\mathbb E[\mathrm{size}(u_{\max})]=(k+1)+\sum_{u\ge2}(2^{u-1}-1)\,q_u,
\qquad q_u=\Pr[u_{\max}\ge u]\le\min\bigl(1,\tbinom ku2^{1-2^u}\bigr).$$
$q_u$ is computed **exactly** (inclusion–exclusion over the $\binom ku$
punctured-subcube events) for $k\le6$; the union bound $B(k)$ is exact-rational
for every $k$:

| $k$ | 3 | 4 | 6 | 8 | 16 | 64 | 256 | 1024 | 4096 |
|---|---|---|---|---|---|---|---|---|---|
| $B(k)-d$ | 0.398 | 0.844 | 1.472 | 2.327 | 4.389 | 11.05 | 26.00 | 26.01 | 47.96 |
| $2^{d-1}$ | $2^3$ | $2^4$ | $2^6$ | $2^8$ | $2^{16}$ | $2^{64}$ | $2^{256}$ | $2^{1024}$ | $2^{4096}$ |

**Closed form.** Put $L:=\max(2,\log_2k)$ and
$u^\dagger:=\max\{u\ge2:2^u\le4uL\}$ (well defined: $2^u/(4uL)$ increases in
$u\ge2$, so the constraint cuts out an interval). For $2\le u\le u^\dagger$ use
$q_u\le1$: those terms sum to $\le2^{u^\dagger}\le4u^\dagger L$. For
$u>u^\dagger$ (so $u\ge3$ and $2^u>4uL$), $\binom ku\le k^u\le2^{uL}$ gives
$(2^{u-1}-1)q_u\le2^u2^{1+uL-2^u}\le2^{u(1-3L)+1}\le2^{-5u+1}$, and
$\sum_{u\ge3}2^{-5u+1}<10^{-4}$. Since $2^{u}>4uL$ once $u\ge2\log_2L+6$
(as $64L^2>4L(2\log_2L+6)$ for $L\ge2$),
$$\rho\ \le\ d+8L\log_2L+24L+1,\qquad L=\max(2,\log_2(d-1)) .$$
So the answer to [G5]'s question is *poly, in fact $d+O(\log d\log\log d)$,
uniformly in $k$* — and the same bound caps every other selection rule by the
sandwich.

## 4. Isolated or typical? (part 2 of the question)

The size-$2^{d-1}$ minimal certificate of [G5] requires all $2^k$ targets to be
$+1$: it is carried by exactly $2^k$ of the $2^{N-1}$ points, i.e. a
$2^{-(2^k-1)}$ fraction (verified: $8/1024$ at $k=3$, $16/524288$ at $k=4$), it
is a $1/369$ share of the (point, certificate) multiset at $k=3$, $1/123905$ at
$k=4$, and $\approx2^{-2^k}$ in general. Its contribution to $\mathbb E|W|$ is
$2^k2^{1-2^k}$: $4.4\cdot10^{-75}$ already at $k=8$. Conversely
**poly-size certificates carry everything**: the expected count at level $u$ is
$\binom ku2^{1-2^u}$, which is concentrated on $u\le4$ for every $k\le64$
(e.g. $k=64$: levels $0..4$ hold $\ge0.9999$ of the mass, sizes $65..76$
against $d=65$), and $\Pr[\exists$ certificate of size $\ge s]$ decays like
$2^{-s}$ up to a $k^{O(\log\log k)}$ factor. **The exponential object is
isolated in the strongest possible sense** (doubly-exponentially rare), which
is exactly why the expectation is unaffected.

## 5. Witness (b): minimal $=$ minimum, so [G5] is empty there

$C=\{x_1=\dots=x_d=+1\}$, $D=C^c$. For $x\in C$: freeing any $i\le d$ breaks
the certificate, so $[d]$ is the unique certificate up to supersets, hence the
unique minimal one ($|W(C)|=d$). For $y\in D$ with
$Z=\{i\le d:y_i=-1\}\ne\emptyset$: $S$ is a certificate iff $S\cap Z\ne\emptyset$
(if $S\cap Z=\emptyset$, set the free coordinates of $[d]$ to $+1$ to land in
$C$), so the minimal certificates are the singletons $\{i\}$, $i\in Z$
(multiplicity $|Z|$). Verified generically and exhaustively for $d=2,3,4$ and
$N=d,d+1,d+2$: sizes exactly $\{d\}$ and $\{1\}$, multiplicities $1$ and
$1..d$, $\pi=\tfrac12+\tfrac d{2(2^d-1)}$ and ratio $\tfrac5{18},\tfrac5{28},
\tfrac{19}{150}$ — §7.4's numbers, now for **every** selection, minimal or
minimum.

## 6. What CAP I(b) actually reads on witness (a) for the minimal variant

Influences are $\tfrac14$ (address) and $2^{-k-1}$ (targets) on both sides, so a
level-$u$ certificate has size $k-u+2^u$ and payment
$\tfrac{k-u}4+2^u2^{-k-1}$; by symmetry
$\mathbb E[\pi]=2[\tfrac{k-\mathbb Eu}4+\mathbb E[2^u]2^{-k-1}]$ and
$\mathbb E[|W_A|+|W_B|]=2[k-\mathbb Eu+\mathbb E2^u]$.

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| exact ratio, MAX rule | $\tfrac14$ | $\tfrac{17}{100}$ | $\tfrac{313}{2212}$ | $\tfrac{32107}{242668}$ | $\approx0.13092$ | $\approx0.13257$ |

Here the adversary breaks size ties adversarially too: $\mathrm{size}(0)=
\mathrm{size}(1)=d$, so at a point whose largest certificate has size $d$ it
takes the level-$1$ one, which pays $\tfrac{k-1}4+2^{-k}$ rather than
$\tfrac k4+2^{-k-1}$. Averaging the payment over the tied maxima instead gives
the slightly larger $\tfrac{55}{288},\tfrac{109}{600},\tfrac{2699}{17696}$
($k=1,2,3$; `s1.out`), and the per-rule table there also records
LEXF $=\tfrac5{24},\tfrac{13}{64}$ and greedy-address-first
$=\tfrac{17}{100},\tfrac{157}{1102}$ — all constants.

For every $k$, rigorously, ratio $\ge\dfrac{k-U(k)}{4B(k)}$ with
$U(k):=\sum_{u\ge1}\min(1,\binom ku2^{1-2^u})\ge\mathbb E u_{\max}$ (using
$u\le2^{u-1}$, which gives $\mathbb E u\le B(k)-k$ as well): $0.070$ at $k=2$,
$0.092$ at $k=3$, $0.123$ at $k=8$, $0.159$ at $k=32$, $0.247$ at $k=4096$ —
tending to $\tfrac14$. Compare the number CAP I(b) would need to bite:
$2^{-d}$. **The cap is not there.**

*Methodological by-product.* The expected **total** codim of *all* minimal
certificates at $x$, $S(k)=\sum_u\binom ku2^{1-2^u}(k-u+2^u)$, is
**quasipolynomial** ($k^{2.15},k^{2.40},k^{3.40},k^{3.79}$ at
$k=4,32,4096,65536$; i.e. $k^{\Theta(\log\log k)}$), while
$\mathbb E[\max]\le B(k)=k+O(\mathrm{polylog})$. Any argument that charges the
window against the whole prime-implicant mass therefore loses a
superpolynomial factor; the max/expectation is the only poly functional here.

## 7. The negative half: a point-mass minimal selection **is** capped, at exactly $2^{-d}$

Take $x^\star\in A_k$ with all $2^k$ targets $+1$ and $y^\star\in B_k$ with all
targets $-1$ (both exist), and the deterministic rule
$W^{\mathrm{pm}}(A_k):=\{$all targets$\}$, $W^{\mathrm{pm}}(B_k):=\{$all
targets$\}$ — by Lemma 1 these are genuine **minimal certificates** of
$x^\star,y^\star$, and $W^{\mathrm{pm}}$ is localised and depends only on its
own set, so it satisfies D1/D4(T1) and Remark 2.2. Then
$$\pi=2\cdot2^k\cdot2^{-k-1}=1,\qquad |W(A_k)|+|W(B_k)|=2\cdot2^{k}=2^{d},
\qquad \frac{\pi}{|W_A|+|W_B|}=2^{-d}.$$
Verified two independent ways: closed form above, and exact `Fraction`
influence sums from the integer Walsh–Hadamard transform of the truth table for
$k=1,2,3$ ($\tfrac14,\tfrac18,\tfrac1{16}$ — `s7` item (3)). **Drafting
constraint for P5:** the plan may not say "a minimal certificate"; it must say
"a minimal certificate *of a uniformly random point of its own set*" (or any
point distribution with $\max_x\mu(x)\le\mathrm{poly}(d)/|A|$, by the same
computation). With that clause, (V1)–(V3) hold; without it, CAP I(b) kills the
variant with the certificate above.

## 8. Search beyond the two witnesses

**8.1 The reduction (why the search space is *all* degree-$\le d$ sets).** For
any nonempty $A\ne\{\pm1\}^N$ of degree $\le d$, the pair $(A,A^c)$ lies in
$\mathcal P_d$ ($1-\mathbf 1_A$ has degree $\le d$). Since $\pi\le\pi_{\mathrm{Rel}}\le2d$
always, a degree-$\le d$ set with $\rho(A)=2^{\Omega(d)}$ *immediately* yields a
CAP I(b) witness capping the unrestricted-minimal variant at
$2d/2^{\Omega(d)}$. So [G5] is negative **iff**
$\sup\{\rho(A):\deg\mathbf 1_A\le d\}$ is superpolynomial in $d$. This is the
exact objective the search maximised.

**8.2 Coverage (exact spaces swept, per-set exact rational arithmetic).**

| space | size | exhaustive? | $\max\rho$ found | $2d-1$ |
|---|---|---|---|---|
| all sets, $r=3$ | $2^8-2$ | yes | $1,3,3$ ($d=1,2,3$) | $1,3,5$ |
| all sets, $r=4$ | $2^{16}-2$ | yes | $1,3,4,4$ ($d=1..4$) | $1,3,5,7$ |
| $L(5,2)$, $L(6,2)$ (all degree-$\le2$) | $552$, $1164$ | yes | $3$ | $3$ (tight) |
| $L(4,3)$, $L(5,3)$ (all degree-$\le3$) | $12870$, $807980$ | yes | $4$, $\tfrac{17}4$ | $5$ |
| $L(6,3)$ (all degree-$\le3$ on 6 coords) | $16750860$ | **yes** (883 s) | $5$, at `0x9f0690f690f69f06`, $N_s=\{4{:}8,5{:}16\}$ | $5$ |
| $L(7,3)$, uniform via the group construction | $126113920$ | sample $2.5\cdot10^6$ ($2.0\%$) | $\tfrac{21}4>2d-1$ | $5$ |
| $\{x_7{=}{+}1\}\times P$, $P\in L(6,3)$ (degree $\le4$) | $6\cdot10^5$ sampled | sample | $6$ | $7$ |
| random cosets | $400$ | random | $=\#\mathrm{Rel}\le2d-1$, 0 violations | — |
| all cosets of all linear codes, $n\le5$ | all | yes | $\#\mathrm{Rel}\le\{d{=}2{:}3,3{:}4,4{:}5,5{:}5\}$ | — |
| degree-safe hill climb, $d\le5$, $r\le11$, unseeded | $\sim10^5$ proposals | stochastic | $3,\tfrac{49}{12},\tfrac{657}{128},\tfrac{191}{30}$ ($d=2..5$) | $3,5,7,9$ |
| seeded climbs from every record object (Hamming, address, $A^\star$, products) | 8000 proposals each | stochastic | records reproduced, **none improved**: $3,\tfrac{21}4,7,\tfrac{33}4$ | $3,5,7,9$ |
| witness (a), all $k$ | closed form | proved | $d+O(\log d\log\log d)$ | $2d-1$ |

Hill-climbing used the degree-safe move set {add a codim-$\le d$ subcube
disjoint from $A$; delete a codim-$\le d$ subcube contained in $A$; flip one
point if the degree survives} — the first two provably preserve
$\deg\le d$ because $\mathbf 1_{A\sqcup Q}=\mathbf 1_A+\mathbf 1_Q$ and
$\mathbf 1_{A\setminus Q}=\mathbf 1_A-\mathbf 1_Q$. *Caveat, stated because it
weakens the stochastic rows:* on dense seeds most proposals are rejected before
evaluation (an "add" needs a disjoint subcube, a "delete" a contained one), so
the seeded climbs certify little more than local optimality of the seeds; the
exhaustive rows and the exact families carry the weight. Two enumeration
cross-checks passed: $|L(r,3)|=12870,\,807980,\,16750860,\,126113920$ reproduce
`0023-refuter-4-code/r1a.out`, `r1c.out`, and one **erratum was found and
recorded in `s6.out`**: the first $r=7$ build shifted `np.uint64` by 64 (which
numpy evaluates to $0$), so that block swept the third row above, not $L(7,3)$;
the corrected sampler is `s9_L7_sample.py`.

**8.3 The strongest true lower bound, and a proved ceiling for the affine
class.** Let $A=a+C$ be a coset of a linear code, all coordinates relevant.
Then (i) a subcube inside a coset must have every free coordinate $i$ with
$e_i\in C$, i.e. irrelevant — so **every** prime implicant is a single point and
$\rho(A)=n$; (ii) $\mathbf 1_A=2^{-c}\sum_{u\in C^\perp}(-1)^{\langle u,a\rangle}\chi_u$,
so $d=\max_{u\in C^\perp}|u|$ and $c=\dim C^\perp$; (iii) each relevant $i$ has
$\#\{u\in C^\perp:u_i=1\}=2^{c-1}$, whence
$n2^{c-1}=\sum_{u\in C^\perp}|u|\le(2^c-1)d$ and therefore
$$\rho(A)=n\le(2-2^{1-c})d\le 2d-1 .$$
Equality is attained by the **Hamming/simplex family**: $A$ = a coset of the
$[2^c-1]$ Hamming code has degree exactly $2^{c-1}$ (its dual is the simplex
code, all weights $2^{c-1}$), minimum distance $3$, hence isolated points and a
unique minimal certificate of size $n=2d-1$ at every point. Verified exactly:
$c=2,3,4$ give $(n,d,\rho)=(3,2,3),(7,4,7),(15,8,15)$, with $\rho$ computed by
full prime-implicant enumeration for $n\le7$. **So $\rho$ genuinely exceeds the
minimum-certificate scale — minimal $\ne$ minimum matters — but by a factor
$\le2$, and no counterexample exists anywhere in the affine class.** The bound
is *not* an artefact of tightness elsewhere: brute force over all cosets of all
linear codes for $n\le5$ gives affine maxima $3,4,5,5$ at $d=2,3,4,5$, so the
affine class is strictly weaker than the general one already at $d=3$
(general: $\tfrac{21}4$, §8.6) — the affine proof therefore does **not** extend
by any bookkeeping, and $\rho$ is genuinely additive over products
($\rho(A_1\times A_2)=\rho(A_1)+\rho(A_2)$, degrees adding), which gives the
general linear lower bound $\rho^\ast(d)\ge\tfrac74 d-O(1)$ and
$\rho^\ast(d)\ge2d-1$ at $d=2^{c-1}$.

**8.4 A second capped sub-class.** If every prime implicant of $A$ is a point
(equivalently $A$ is an independent set in the cube graph) then every point has
full sensitivity, so $\rho=\#\mathrm{Rel}(A)\le s(A)\le\mathrm{bs}(A)$; with the
$\mathrm{bs}=O(d^2)$ half of the campaign's S6 card this is $\rho=O(d^2)$
(**[MEMORY-flagged**: I did not re-derive Nisan–Szegedy; the affine bound of
§8.3 is self-contained and needs no card).

**8.5 The obstruction, stated precisely (this is the heart of the matter).**
A minimal certificate of size $s$ is a codim-$s$ subcube $Q\subseteq A$, and
$\Pr_{x\sim\mathrm{Unif}(A)}[x\in Q]=2^{-s}/\alpha_A\le2^{d-s}$. Hence
$$\rho(A)\ \ge\ \varepsilon\,s\quad\Longrightarrow\quad
\#\{\text{prime implicants of codim}\ \ge s\}\ \ge\ \varepsilon\,2^{s-d}.$$
A counterexample therefore needs an **exponentially numerous family of deep
irredundant subcubes** in one degree-$\le d$ set. Witness (a) has exactly
$\binom ku2^{k-u}$ prime implicants at depth $k-u+2^u$, i.e. $2^{O(d\log d)}$
at depth $\approx2^u$, against the $2^{2^u-u-1}$ required — short by a doubly
exponential factor, and this single inequality explains *all* of §§1–4. Two
independent mechanisms block the natural fixes: certificate coordinates not
*forced* by $A$ each cost a factor $2$ in probability, and a degree-$\le d$ set
forces at most $d$ coordinates (Remark 4.2(b)); and $\rho$ is **additive** over
products ($\rho(A_1\times A_2)=\rho(A_1)+\rho(A_2)$ while degrees add), so no
product/blocking construction can beat the best single block's $\rho/d$ ratio,
which is $<2$ in everything found.

**8.6 The envelope I conjectured, and its refutation (a near-miss worth
recording).** The exhaustive rows all satisfied
$\textbf{(R)}:\ \rho(A)\le2\deg(\mathbf 1_A)-1$ — tight at $d=2$ ($r\le6$,
exhaustive), tight at $d=3$, $r=6$ (exhaustive, $\max\rho=5$), proved for
affine sets. **(R) is false.** The corrected uniform sample of $L(7,3)$ found
$$A^\star:=\texttt{0x11bb0faafc0c7474d1d1cfc0aa0f2277}\subseteq\{\pm1\}^7,
\quad \deg=3,\ |A^\star|=64,\ \alpha=\tfrac12,\
N_s=\{4{:}4,\ 5{:}36,\ 6{:}8\},\ \rho=\tfrac{21}4>5 ,$$
with per-point max-size histogram $\{5{:}48,\ 6{:}16\}$; $43{,}047$ of
$2{,}500{,}000$ uniform members of $L(7,3)$ ($1.72\%$) violate (R), so the
violation is typical at $r=7$, not exotic, while $\tfrac{21}4$ was the maximum
over that $2.0\%$ sample (two independent samples, $3\cdot10^5$ and
$2.5\cdot10^6$, both peaked at $\tfrac{21}4$).
Verified by three code paths: the bitmask routine
(`s4_helpers.analyse`), the numpy boolean certificate tables of `lib6`, and the
slow per-point full-subset scan, plus two independent integer-WHT degree
computations. **Consequence for the record:** at fixed $d=3$ the maxima
grow with the number of coordinates — $3,\,4,\,\tfrac{17}4,\,5,\,\ge\tfrac{21}4$
at $r=3,4,5,6,7$ (the first four exhaustive), with increments
$1,\tfrac14,\tfrac34,\ge\tfrac14$, i.e. shrinking rather than doubling; and the
only general upper bound is the junta bound $O(2^d)$. So the residual question
is exactly

> **Open, and it decides [G5] outside the artifact's witnesses:** is
> $\rho^\ast(d):=\sup\{\rho(A):\deg\mathbf 1_A\le d\}$ polynomial in $d$, or
> $2^{\Theta(d)}$? Known: $\tfrac74 d-O(1)\le\rho^\ast(d)\le M(d)=O(2^d)$;
> $\rho^\ast(d)\ge2d-1$ for $d=2^{c-1}$; $\rho^\ast=1,3,\ge\tfrac{21}4,\ge7,
> \ge\tfrac{33}4$ at $d=1..5$. A poly bound closes [G5] in full generality and
> gives P5's minimal variant the ratio $\pi/(2\rho^\ast(d))$; an
> $\Omega(2^{\varepsilon d})$ construction kills the minimal variant (but not
> the minimum-size one, which is $O(d^4)$ by the S6c card).

One distinction survives all of this and should not be blurred: the maximum
prime-implicant *codim* is already $\ge2^{d-1}$ (witness (a)) and equals
$6>2d-1$ inside $A^\star$ at $d=3$; it is only the **expectation** that stays
small, and only the expectation is what CAP I(b) reads.

## 9. What this rules out, and what it does not

**Rules out.** (a) Any hope of capping P5's minimal variant *using the
artifact's own two witnesses*: on both, every per-point minimal selection with
uniform $x$ gives $\mathbb E|W|\le d+O(\log d\log\log d)$ and ratio $\ge0.070$
(exact, all $k$; a closed form, not an extrapolation). (b) Any counterexample
inside the affine/coset class, for every $d$ (proved ceiling $2d-1$). (c) Any
counterexample among degree-$\le3$ sets on $\le6$ coordinates, degree-$\le2$
sets on $\le6$ coordinates, or arbitrary sets on $\le4$ coordinates
(exhaustive). (d) The reading of "unrestricted minimal selection" under which
the *point* may be chosen adversarially — that one is **refuted**, with an
exact certificate (§7).

**Does not rule out.** (i) A degree-$\le d$ set with $\rho(A)$ superpolynomial
in $d$ — the §8.6 question is **open**, and the searched window ($d\le5$,
$r\le11$; complete classes only at $d\le3$, $r\le6$) provably cannot see it,
since a counterexample needs $r=2^{\Omega(d)}$ by §8.5. Two facts keep this
live rather than dismissible: $\rho^\ast(3)\ge\tfrac{21}4>2^{d-1}=4$, so $\rho$
is *not* below the exponential scale at small $d$, and $\rho^\ast$ was still
increasing in $r$ at the edge of the exhaustive range. What the null result does
say is that every mechanism found is additive/linear and that the counting
requirement of §8.5 is missed by a doubly exponential margin. (ii) Anything
about $\Theta_{\text{cert}}$ from below — no lower bound on the value of P5's
window is claimed, and nothing here says P5's payment inequality (T2) holds.
(iii) Non-$\mathbb Z_2$ groups: everything here is over $\mathbb Z_2$. (iv) The
$L(7,3)$ level was sampled, not swept, and $d=4,5$ only by seeded stochastic
search whose acceptance rate on dense seeds is low (§8.2 caveat): a larger
$\rho$ at those sizes would have been missed. (v) Nothing here bears on the
*other* gaps of the artifact ([G1]–[G4], E1) or on any cap besides CAP I(b) as
applied to the certificate window.

## 10. Two-method verification record

| claim | method 1 | method 2 |
|---|---|---|
| minimal-certificate family of witness (a) | Lemma 1 (proof) | generic truth-table enumeration, $k\le3$, set-for-set at every point of both sides; $k=4$ over all $2^{19}$ points via AND-folds + greedy-shrink probe |
| $\rho$ at $k=3,4$ | full enumeration over the $2^{2^k-1}$ target patterns (exact Fractions) | independent inclusion–exclusion for $q_u$ ($k\le6$); at $k=4$ also the $2^{19}$-point truth-table computation — all three agree on $\tfrac{182001}{32768}$ |
| $\rho\le B(k)$, all $k$ | exact-rational union bound | closed form of §3, checked numerically against $B$ over $k\le4096$ |
| point-mass cap $=2^{-d}$ | closed form | exact `Fraction` influences from integer WHT, $k\le3$ |
| witness (b) minimal $=$ minimum | proof (§5) | generic enumeration, $d\le4$, $N\le6$ |
| Hamming family $\rho=2d-1$ | §8.3 proof (dual-weight counting) | exhaustive prime-implicant enumeration $n=3,7$; degree by integer WHT at $n=15$ |
| $\rho=\#\mathrm{Rel}\le2d-1$ for cosets | §8.3 proof | 400 random cosets, 0 violations; all cosets, $n\le5$ |
| refutation of (R): $\rho(A^\star)=\tfrac{21}4$, $\deg A^\star=3$ | bitmask routine `s4_helpers.analyse` | `lib6` numpy certificate tables **and** slow per-point full-subset scan; degree by two independent integer-WHT codes |

## Files

All new code in `proofs/0023-refuter-6-code/`, exact integer/`Fraction`
arithmetic throughout, python3.13 + numpy (no scipy):
`lib6.py` (generic certificate tables, integer WHT, exact influences,
selection rules), `s1_witness_a_generic.py` (+`s1.out`),
`s2_witness_a_exact_all_k.py` (+`s2.out`), `s3_witness_b_and_k4.py`
(+`s3.out`), `s4_helpers.py`, `s4_search_exhaustive.py` (+`s4.out`),
`s5_hunt_rho.py` (+`s5.out`), `s6_big_sweep.py` (+`s6.out`, **with the erratum
appended at the end of that file**), `s7_capI_ratio.py` (+`s7.out`, `s7b.out`),
`s8_seeded_climb.py` (+`s8.out`; its affine brute force covers $n\le5$, $n=6$
was cut by the wall clock), `s9_L7_sample.py` (+`s9.out` $3\cdot10^5$,
`s9b.out` $2.5\cdot10^6$), `s10_verify_and_growth.py` (+`s10.out`),
`s11_closedform_check.py` (+`s11.out`: the §3 closed forms dominate the exact
$B(k)$ for $k\le65536$, and $u^\dagger\le2\log_2L+6$ holds throughout). One bug of
my own was found and fixed mid-run: an s2 statistic keyed the level profile by
*size*, and $\mathrm{size}(0)=\mathrm{size}(1)$, so the $u=0$ level was
overwritten (it changed only the reported total/share, $\tfrac{369}{128}$ and
$1/369$ at $k=3$ after the fix — which the independent generic enumeration of s1
confirms: $2560/1024=\tfrac52$, $384/1024=\tfrac38$, $8/1024=\tfrac1{128}$).
Cross-checks against existing machinery: $|L(r,3)|$ counts reproduce
`0023-refuter-4-code/r1a.out`, `r1c.out`; the minimum-certificate numbers
reproduce `0023-prover-3-r2-code/check_min_certificates.py`
($\tfrac14,\tfrac16,\tfrac5{32}$ worst, $\tfrac14,\tfrac5{24},\tfrac{13}{64}$
best); witness influences reproduce `0023-prover-3-code/check_witnesses.py`.

### END OF ARTIFACT 0023-refuter-6 ###
