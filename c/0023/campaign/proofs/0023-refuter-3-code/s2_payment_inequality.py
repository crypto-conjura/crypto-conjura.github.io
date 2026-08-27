"""
s2_payment_inequality.py -- the LOCAL inequality that decides the rung, and
its exhaustive verification / refutation.

THE MASTER COUNT (refuter-2 (M), re-derived for R2).  Let (F,G) be an
incompatible pair over C^ind_d.  Every degree-<=d set is a junta; write J_f
for the set of relevant coordinates ("window").  For a disjoint pair put
    pi(f,g) = sum_{i in J_f cap K_g} [ Inf_i(f) + Inf_i(g) ] .
With u_i = Pr_F[i in J], v_i = Pr_G[i in K],
    E[pi] = sum_i [ Ibar_F(i) v_i + Ibar_G(i) u_i ]
          <= delta_F E|K| + delta_G E|J| .
Hence any pointwise lower bound  pi(f,g) >= (|J_f| + |K_g|) / (2d)  yields
    (E|J|+E|K|)/(2d) <= max(delta_F,delta_G) (E|J|+E|K|),
i.e.  max(delta_F, delta_G) >= 1/(2d):  the rung, with the optimal constant,
and with equality at the d x d grid.

(LOC-d)   for every DISJOINT pair of degree-<=d sets:
              pi(f,g)  >=  ( |J_f| + |K_g| ) / (2d).

This script:
  (A) verifies (LOC-2) EXHAUSTIVELY over all disjoint pairs of degree-<=2
      sets (windows <= 4 = the exact junta bound, all overlap sizes), and
      reports the minimum of  pi - (|J|+|K|)/4  and of  pi/(|J|+|K|);
  (B) the same exhaustively for d=3 with windows <= 3, and over ALL
      complement pairs (A, A^c) with window <= 5;
  (C) REFUTES (LOC-d) for d >= 4 with the ADDRESS family, computed two
      independent ways (integer Walsh-Hadamard on the full 2^n cube, and the
      closed-form boundary-count formula (F1)), exact rational arithmetic.
"""
import itertools
from fractions import Fraction
from deg_lib import (genuine_patterns, JFun, disjoint, shared, payment_lhs,
                     total_influence, walsh_int, pattern_degree, popcount)

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

# ------------------------------------------------------------------ (A)/(B)
def sweep_local(d, maxwin, label):
    pats = {k: genuine_patterns(k, d) for k in range(1, maxwin + 1)}
    worst_slack = None; worst = None
    worst_ratio = None; wr = None
    npairs = 0
    for kf in range(1, maxwin + 1):
        for kg in range(1, maxwin + 1):
            for s in range(1, min(kf, kg) + 1):
                Wf = tuple(range(kf))
                Wg = tuple(list(range(s)) + list(range(kf, kf + kg - s)))
                for pf in pats[kf]:
                    f = JFun(Wf, pf)
                    for pg in pats[kg]:
                        g = JFun(Wg, pg)
                        if not disjoint(f, g):
                            continue
                        npairs += 1
                        pi = payment_lhs(f, g)
                        rhs = Fraction(kf + kg, 2 * d)
                        sl = pi - rhs
                        if worst_slack is None or sl < worst_slack:
                            worst_slack = sl; worst = (f, g, pi, rhs)
                        r = pi / (kf + kg)
                        if worst_ratio is None or r < worst_ratio:
                            worst_ratio = r; wr = (f, g, pi, kf + kg)
    pr(f"  {label}: {npairs} disjoint pairs")
    pr(f"    min of pi - (|J|+|K|)/(2d) = {worst_slack}"
       f"   ==> (LOC-{d}) {'HOLDS' if worst_slack >= 0 else 'FAILS'}")
    f, g, pi, rhs = worst
    pr(f"      tight/violating pair: f={f} g={g}  pi={pi} rhs={rhs}")
    pr(f"    min of pi/(|J|+|K|) = {worst_ratio} = 1/{1/worst_ratio}"
       f"   (need >= 1/(2d) = 1/{2*d})")
    f, g, pi, w = wr
    pr(f"      minimiser: f={f} g={g}  pi={pi} |J|+|K|={w}")
    return worst_slack, worst_ratio

hr("(A) (LOC-2): exhaustive over ALL disjoint pairs of degree-<=2 sets")
sweep_local(2, 4, "d=2, windows<=4 (exhaustive: junta bound is exactly 4)")

hr("(B) (LOC-3): exhaustive over windows<=3")
sweep_local(3, 3, "d=3, windows<=3")

pr("\n  (B') all COMPLEMENT pairs (A,A^c), degree-<=3, windows<=5:"
   "  pi = T_f + T_g >= 2k/(2d) = k/d ?")
for d in (2, 3):
    kmax = {2: 4, 3: 5}[d]
    worst = None
    for k in range(1, kmax + 1):
        for p in genuine_patterns(k, d):
            P = len(p); Q = (1 << k) - P
            sb = sum(sum(1 for x in p if (x ^ (1 << b)) not in p)
                     for b in range(k))
            pi = Fraction(sb, 2) * (Fraction(1, P) + Fraction(1, Q))
            sl = pi - Fraction(k, d)
            if worst is None or sl < worst[0]:
                worst = (sl, k, sorted(p), pi)
    pr(f"    d={d}: min (pi - k/d) = {worst[0]}  at k={worst[1]}, pi={worst[3]},"
       f" P={worst[2][:12]}{'...' if len(worst[2])>12 else ''}"
       f"   ==> {'HOLDS' if worst[0] >= 0 else 'FAILS'}")

# ------------------------------------------------------------------ (C)
hr("(C) the ADDRESS family refutes (LOC-d) for d >= 4")

def address_set(k):
    """A = { x = (a_1..a_k, y_0..y_{2^k-1}) : y_{addr(a)} = +1 },
    addr(a) = the integer with bits (a_t == -1).  Coordinates 0..k-1 are the
    address bits, k..k+2^k-1 the targets.  Returns (n, pattern as a frozenset
    of masks over n bits) with bit j set <=> coordinate j is -1."""
    n = k + (1 << k)
    pat = set()
    for m in range(1 << n):
        a = m & ((1 << k) - 1)          # bits of the address block
        j = a                            # addr(a) = a as an integer
        if not (m >> (k + j)) & 1:        # target bit 0 means +1
            pat.add(m)
    return n, frozenset(pat)

pr("  method 1: integer Walsh-Hadamard on the full 2^n cube (exact)")
for k in (1, 2, 3):
    n, pat = address_set(k)
    d = pattern_degree(pat, n)
    f = JFun(tuple(range(n)), pat)
    inf1 = f.influences()                          # (F1) boundary counts
    inf2 = f.influences_fourier()                  # Fourier definition
    assert inf1 == inf2, (k, "influence formulas disagree")
    T = sum(inf1.values(), Fraction(0))
    win = sum(1 for v in inf1.values() if v != 0)
    pi = 2 * T                                     # complement pair (A, A^c)
    rhs = Fraction(2 * win, 2 * d)
    pr(f"    k={k}: n={n} degree={d} relevant={win} mu={f.density()}"
       f"  T={T}  pi={pi}  rhs=(|J|+|K|)/(2d)={rhs}"
       f"   {'OK' if pi >= rhs else '*** (LOC) VIOLATED ***'}")
    pr(f"         influences: address bits {sorted(set(inf1[i] for i in range(k)))},"
       f" targets {sorted(set(inf1[i] for i in range(k, n)))}")
    pr(f"         max influence = {max(inf1.values())}  vs 1/(2d) = {Fraction(1,2*d)}")

pr("\n  method 2: closed form (independent derivation)")
pr("    1_A = 1/2 + (1/2) sum_j 1[a=j] y_j  =>  deg = k+1,")
pr("    Inf_{a_t}(1_A) = 2^k * 2^{k-1} * 2^{-2k-2} = 1/8,")
pr("    Inf_{y_j}(1_A) = 2^k * 2^{-2k-2} = 2^{-k-2},  mu = 1/2, so")
pr("    Inf(f) = 2*Inf(1_A):  address 1/4, target 2^{-k-1};  T = k/4 + 1/2.")
for k in range(1, 9):
    d = k + 1
    win = k + (1 << k)
    T = Fraction(k, 4) + Fraction(1, 2)
    pi = 2 * T
    rhs = Fraction(2 * win, 2 * d)
    pr(f"    k={k}: d={d} |J|={win:6d}  pi={pi}  rhs={rhs}"
       f"   ratio pi/rhs = {float(pi/rhs):.4f}"
       f"   pi/(|J|+|K|) = {pi/(2*win)} = 1/{float(2*win/pi):.1f}")
pr("\n    => the best bound the master count can give from the address family"
   "\n       is  delta >= pi/(|J|+|K|) = (k/2+1)/(2(k+2^k)) = 2^{-Theta(d)}:"
   "\n       ANY argument charging the full window size is capped at 2^{-Theta(d)}.")
pr("\nDONE s2")
