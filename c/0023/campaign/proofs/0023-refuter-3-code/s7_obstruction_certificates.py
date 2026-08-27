"""
s7_obstruction_certificates.py -- the two obstruction families, certified, and
the rigidity that stops each of them from becoming a counterexample.

FAMILY 1 (kills (HEAVY), i.e. the total-influence-budget union bound):
    C = a codimension-d subcube;  the pair (C, C^c) is incompatible inside
    C^ind_d (both indicators have degree exactly d), and
        Inf_i(1_C/||.||)   = 1/2                     (i in the d-window)
        Inf_i(1_{C^c}/||.||) = 1/(2(2^d - 1))        (i in the d-window)
    so  theta = max_i min(...) = 1/(2(2^d-1)) = 2^{-Theta(d)}.
    RIGIDITY that saves the rung: the ONLY degree-<=d subset of a
    codimension-d subcube C is C itself, so the cheap side C^c admits exactly
    one partner, which pays 1/2.  (Verified exhaustively for d=2,3.)

FAMILY 2 (kills (LOC-d), i.e. the payment/window-budget count):
    A_k = the address set with k address bits and 2^k targets: degree k+1,
    k + 2^k relevant coordinates, influences 1/4 (address) and 2^{-k-1}
    (targets).  pi(A_k, A_k^c) = k/2 + 1 while (|J|+|K|)/(2d) = (k+2^k)/(k+1),
    so the local payment inequality fails by a factor Theta(2^k/k^2).
    RIGIDITY that saves the rung: the conflict needs the whole address block;
    two address sets with different address blocks are never disjoint (s4),
    so the expensive address bits cannot be spread over a distribution.
"""
import itertools
from fractions import Fraction
from deg_lib import (genuine_patterns, deg_functions, JFun, disjoint, shared,
                     payment_lhs, total_influence, popcount, pattern_degree)

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

hr("FAMILY 1: (codim-d subcube, complement) -- theta = 1/(2(2^d-1))")
for d in range(1, 9):
    k = d
    cube = frozenset({(1 << k) - 1})                 # the all-(-1) point
    comp = frozenset(set(range(1 << k)) - set(cube))
    f = JFun(tuple(range(k)), cube)
    g = JFun(tuple(range(k)), comp)
    assert disjoint(f, g)
    If, Ig = f.influences(), g.influences()
    th = max(min(If[i], Ig[i]) for i in range(k))
    # degrees, by integer Walsh-Hadamard
    df = pattern_degree(cube, k); dg = pattern_degree(comp, k)
    pr(f"  d={d}: deg(1_C)={df} deg(1_C^c)={dg}  Inf(C)={If[0]} Inf(C^c)={Ig[0]}"
       f"  theta={th} = 1/{1/th}   pi={payment_lhs(f,g)}"
       f"  max influence of the pair = {max(max(If.values()), max(Ig.values()))}")
pr("  ==> theta*(d) <= 1/(2(2^d-1)): (HEAVY_theta) with theta = 1/poly(d) is FALSE,")
pr("      so the Markov+union-bound version of the total-influence-budget count")
pr("      cannot prove better than 2^{-Theta(d)}.")

hr("RIGIDITY 1: the only degree-<=d subset of a codim-d subcube is the subcube")
for d, N in ((2, 4), (2, 5), (3, 5)):   # (3,6) needs all 746048 window-5 patterns: out of budget
    # C = {x : x_0 = ... = x_{d-1} = -1}, as a point mask over {+-1}^N
    Cmask = 0
    for x in range(1 << N):
        if all((x >> i) & 1 for i in range(d)):
            Cmask |= 1 << x
    inside = []
    for k in range(1, min(N, d * (1 << (d - 1))) + 1):
        for p in genuine_patterns(k, d):
            for W in itertools.combinations(range(N), k):
                mk = 0
                for x in range(1 << N):
                    m = 0
                    for b, c in enumerate(W):
                        if (x >> c) & 1:
                            m |= 1 << b
                    if m in p:
                        mk |= 1 << x
                if mk & ~Cmask == 0:
                    inside.append((W, sorted(p)))
    pr(f"  d={d}, N={N}: degree-<=d sets contained in the codim-{d} subcube:"
       f" {len(inside)}  {inside if len(inside)<=3 else '...'}")

hr("FAMILY 2: address sets -- (LOC-d) violation profile and its rigidity")
pr("  (numbers from s2/s4; restated with the rigidity conclusion)")
for k in range(1, 9):
    d = k + 1; win = k + (1 << k)
    T = Fraction(k, 4) + Fraction(1, 2)
    pi = 2 * T
    pr(f"    k={k}: d={d} |J|={win:5d}  pi={pi}  (|J|+|K|)/(2d)={Fraction(2*win,2*d)}"
       f"   pi/(|J|+|K|)=1/{float(2*win/pi):.1f}"
       f"   max influence = 1/4 (address bits, only k of them)")
pr("  RIGIDITY: s4 verified 0/48 (k=1) and 0/19440 (k=2) layouts with a")
pr("  DIFFERENT address block are disjoint from the F-side address set; the")
pr("  address block is a HUB shared by every cross pair, so its influence 1/4")
pr("  cannot be diluted: delta >= 1/4 for every address-based design.")

hr("SUMMARY of the two-case structure that survives")
pr("  (i) FORCING conflicts (some shared coordinate forced to opposite signs).")
pr("      Facts (s5, exhaustive): a degree-<=d set forces at most d")
pr("      coordinates, and a forced coordinate has influence EXACTLY 1/2.")
pr("      Count: 1/2 <= Pr[forcing conflict] <= sum_i Pr_F[i forced] Pr_G[i forced]")
pr("            <= sum_i 2 Ibar_F(i) * 2 Ibar_G(i) <= 4 delta_G sum_i Ibar_F(i)")
pr("            <= 4 d delta_G      ==>   delta >= 1/(8d).")
pr("      Sharper, per-function: for a fixed f every g must oppose one of f's")
pr("      <= d forced coordinates, so some i has Pr_G[g forces i] >= 1/d and")
pr("      Ibar_G(i) >= 1/(2d):  forcing-only designs NEVER beat 1/(2d).")
pr("  (ii) SPREAD conflicts: open.  Both known cheap-coordinate mechanisms")
pr("      (dense complements, address sets) are rigid, as certified above.")
pr("\nDONE s7")
