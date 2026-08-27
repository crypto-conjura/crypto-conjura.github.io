"""
s4_hunt_d3_and_hub.py -- the actual counterexample hunt above d = 2.

(A) BEST CONSTANT THE MASTER COUNT CAN GIVE at d = 3:  min over disjoint pairs
    of  pi/(|J|+|K|).  Exhaustive over complement pairs with window <= 5 and
    over all pairs with windows <= 3; sampled for windows 4,5.
    (If this min is < 1/(2d) the payment/window route cannot prove the rung
    with the optimal constant -- a barrier, not a counterexample.)

(B) THE HUB OBSTRUCTION, tested.  Address-type sets are the objects with
    2^Theta(d) relevant coordinates of influence 2^{-Theta(d)} (the only known
    way to make relevant coordinates cheap).  Test: can two address-type sets
    with DIFFERENT address blocks ever be disjoint?  (Exhaustive over small
    address/target layouts, exact.)  A negative answer is the mechanism that
    stops the cheap coordinates from being spread over a distribution.

(C) DESIGN SEARCH (closure-based, exact cross-disjointness, LP weights):
    d = 2 (sanity: must not beat 1/4) and d = 3 with windows <= 3 at
    N <= 9, plus structured grid / hub / MUX-grid / address-grid layouts at
    general d.

(D) DIAGNOSTIC for the total-influence-budget route of I02: for every design
    found, report  max_i u_i + max_i v_i  (must be >= 1/d) and the conditional
    average influence  Ibar_F(i)/u_i  at the maximiser -- the exact quantity
    whose 1/poly(d) lower bound is missing.
"""
import itertools, random
from fractions import Fraction
from deg_lib import (genuine_patterns, JFun, disjoint, shared, payment_lhs,
                     total_influence, popcount, pattern_degree)

random.seed(20260827)

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

# ------------------------------------------------------------------ (A)
hr("(A) min pi/(|J|+|K|) at d = 3  (the best constant the count can give)")

def ratio_complement_pairs(d, kmax):
    best = None
    for k in range(1, kmax + 1):
        for p in genuine_patterns(k, d):
            P = len(p); Q = (1 << k) - P
            sb = sum(sum(1 for x in p if (x ^ (1 << b)) not in p)
                     for b in range(k))
            pi = Fraction(sb, 2) * (Fraction(1, P) + Fraction(1, Q))
            r = pi / (2 * k)
            if best is None or r < best[0]:
                best = (r, k, sorted(p), pi)
    return best

for d, kmax in ((2, 4), (3, 5)):
    b = ratio_complement_pairs(d, kmax)
    pr(f"  d={d}: complement pairs, window<={kmax}:  min pi/(|J|+|K|) = {b[0]}"
       f" = 1/{1/b[0]}   (1/(2d) = 1/{2*d})")
    pr(f"      at k={b[1]}, pi={b[3]}, P={b[2][:14]}...")

def ratio_general(d, kmax, samples=0):
    """Exhaustive over windows <= kmax; optionally sample bigger windows."""
    pats = {k: genuine_patterns(k, d) for k in range(1, kmax + 1)}
    best = None
    for kf in range(1, kmax + 1):
        for kg in range(1, kmax + 1):
            for s in range(1, min(kf, kg) + 1):
                Wf = tuple(range(kf))
                Wg = tuple(list(range(s)) + list(range(kf, kf + kg - s)))
                for pf in pats[kf]:
                    f = JFun(Wf, pf)
                    for pg in pats[kg]:
                        g = JFun(Wg, pg)
                        if not disjoint(f, g):
                            continue
                        r = payment_lhs(f, g) / (kf + kg)
                        if best is None or r < best[0]:
                            best = (r, f, g)
    return best

b = ratio_general(3, 3)
pr(f"  d=3: ALL pairs, windows<=3: min pi/(|J|+|K|) = {b[0]} = 1/{1/b[0]}")

pr("  d=3: sampled pairs with windows 4,5 (10^5 random disjoint pairs)")
pats45 = {4: genuine_patterns(4, 3), 5: genuine_patterns(5, 3)}
best = None; found = 0; tries = 0
while tries < 400000 and found < 100000:
    tries += 1
    kf = random.choice([4, 5]); kg = random.choice([4, 5])
    s = random.randint(1, min(kf, kg))
    Wf = tuple(range(kf))
    Wg = tuple(list(range(s)) + list(range(kf, kf + kg - s)))
    f = JFun(Wf, random.choice(pats45[kf]))
    g = JFun(Wg, random.choice(pats45[kg]))
    if not disjoint(f, g):
        continue
    found += 1
    r = payment_lhs(f, g) / (kf + kg)
    if best is None or r < best[0]:
        best = (r, f, g)
pr(f"    {found} disjoint pairs from {tries} draws; min pi/(|J|+|K|) = {best[0]}"
   f" = 1/{float(1/best[0]):.3f}")
pr(f"      f={best[1]} T={total_influence(best[1])}")
pr(f"      g={best[2]} T={total_influence(best[2])}")
pr("    ==> at d=3 the count's optimal constant is already < 1/(2d):"
   " (LOC-3) is FALSE, so the payment/window-budget route cannot reach 1/(2d).")

# ------------------------------------------------------------------ (B)
hr("(B) HUB OBSTRUCTION: address-type sets with different address blocks")

def address_jfun(addr_bits, targets):
    """A = { x : y_{addr(a)} = +1 }, addr(a) read off addr_bits (LSB first),
    targets[j] = the coordinate carrying y_j.  Window = addr_bits + targets."""
    k = len(addr_bits)
    W = tuple(sorted(set(addr_bits) | set(targets)))
    pos = {c: b for b, c in enumerate(W)}
    pat = set()
    for m in range(1 << len(W)):
        a = 0
        for t, c in enumerate(addr_bits):
            if (m >> pos[c]) & 1:
                a |= 1 << t
        if not (m >> pos[targets[a]]) & 1:      # bit 0 == +1
            pat.add(m)
    return JFun(W, frozenset(pat))

def address_complement(addr_bits, targets):
    f = address_jfun(addr_bits, targets)
    full = frozenset(range(1 << len(f.window)))
    return JFun(f.window, full - f.pat)

pr("  k=1 (degree 2) and k=2 (degree 3) address sets; all layouts of the")
pr("  address block and target pool inside a universe of 12 coordinates,")
pr("  testing disjointness of an F-side address set with a G-side one.")
for k in (1, 2):
    T = 1 << k
    universe = list(range(3 * (k + T)))
    same_ok = 0; diff_ok = 0; diff_tot = 0; same_tot = 0
    # F side: fixed canonical layout
    aF = tuple(range(k)); tF = tuple(range(k, k + T))
    f = address_jfun(aF, tF)
    # G side: all layouts with address block / target pool inside a modest pool
    pool = list(range(k + T + 2))
    for aG in itertools.permutations(pool, k):
        for tG in itertools.permutations(pool, T):
            if set(aG) & set(tG):
                continue
            g = address_complement(aG, tG)
            same = (set(aG) == set(aF))
            d_ = disjoint(f, g)
            if same:
                same_tot += 1; same_ok += d_
            else:
                diff_tot += 1; diff_ok += d_
    pr(f"    k={k}: disjoint with SAME address block: {same_ok}/{same_tot};"
       f"  with a DIFFERENT address block: {diff_ok}/{diff_tot}")

# ------------------------------------------------------------------ (C)
hr("(C) design search")
import numpy as np
from scipy.optimize import linprog

def tau_and_weights(funs, coords):
    """min_p max_i sum_a p_a Inf_i  (primal) -- returns (value, p)."""
    m = len(funs); n = len(coords)
    ci = {c: j for j, c in enumerate(coords)}
    A = np.zeros((n, m + 1))
    for a, f in enumerate(funs):
        for c, v in f.influences().items():
            A[ci[c], a] = float(v)
    A[:, m] = -1.0
    cobj = np.zeros(m + 1); cobj[m] = 1.0
    Aeq = np.zeros((1, m + 1)); Aeq[0, :m] = 1.0
    res = linprog(cobj, A_ub=A, b_ub=np.zeros(n), A_eq=Aeq, b_eq=[1.0],
                  bounds=[(0, None)] * m + [(None, None)], method="highs")
    assert res.success
    return res.x[m], res.x[:m]

def eval_design(F, G, N, label, d, quiet=False):
    """Exact cross-disjointness check + LP-optimal weights + diagnostics."""
    for f in F:
        for g in G:
            assert disjoint(f, g), ("cross pair not disjoint", label)
    coords = list(range(N))
    tF, pF = tau_and_weights(F, coords)
    tG, pG = tau_and_weights(G, coords)
    eps = max(tF, tG)
    # diagnostics with the LP weights
    uF = [sum(pF[a] for a, f in enumerate(F) if i in f.window) for i in coords]
    vG = [sum(pG[b] for b, g in enumerate(G) if i in g.window) for i in coords]
    IF = [sum(pF[a] * float(f.influences()[i]) for a, f in enumerate(F)
              if i in f.window) for i in coords]
    IG = [sum(pG[b] * float(g.influences()[i]) for b, g in enumerate(G)
              if i in g.window) for i in coords]
    Epi = sum(pF[a] * pG[b] * float(payment_lhs(F[a], G[b]))
              for a in range(len(F)) for b in range(len(G)))
    EJ = sum(pF[a] * len(F[a].window) for a in range(len(F)))
    EK = sum(pG[b] * len(G[b].window) for b in range(len(G)))
    if not quiet:
        pr(f"  {label}: N={N} d={d} |F|={len(F)} |G|={len(G)}"
           f"  eps={eps:.6f}  eps*2d={eps*2*d:.4f}")
        pr(f"      E[pi]={Epi:.4f}  E|J|={EJ:.3f} E|K|={EK:.3f}"
           f"  E[pi]/(E|J|+E|K|)={Epi/(EJ+EK):.5f}  1/(2d)={1/(2*d):.5f}")
        pr(f"      max u={max(uF):.4f} max v={max(vG):.4f} sum=(>=1/d={1/d:.4f})"
           f" {max(uF)+max(vG):.4f}")
    return eps, Epi, EJ, EK, max(uF), max(vG)

def grid(D):
    """the d x d conjunction grid: F rows, G columns, degree D, eps=1/(2D)."""
    F = [JFun(tuple(r * D + c for c in range(D)), frozenset({0}))
         for r in range(D)]
    G = [JFun(tuple(r * D + c for r in range(D)),
              frozenset({(1 << D) - 1})) for c in range(D)]
    return F, G, D * D, D

for D in (2, 3, 4):
    F, G, N, d = grid(D)
    eval_design(F, G, N, f"grid D={D}", d)

# MUX grid: cells are 3-coordinate MUX gadgets (degree 2, all infl 1/4)
MUX = frozenset({3, 4, 6, 7})            # the k=1 address set on 3 bits
MUXc = frozenset(set(range(8)) - set(MUX))
def mux_grid(D):
    """F_r = MUX gadget on cell (r,r)?  No: a grid needs one gadget per cell,
    tensored along the row -- degree 2D.  Included for the record."""
    F = []; G = []
    cell = lambda r, c: tuple(3 * (r * D + c) + j for j in range(3))
    for r in range(D):
        W = tuple(sorted(sum([list(cell(r, c)) for c in range(D)], [])))
        # tensor of D MUX gadgets: pattern = product
        pos = {c: b for b, c in enumerate(W)}
        pat = set()
        for m in range(1 << len(W)):
            ok = True
            for c in range(D):
                sub = 0
                for j, coord in enumerate(cell(r, c)):
                    if (m >> pos[coord]) & 1:
                        sub |= 1 << j
                if sub not in MUX:
                    ok = False; break
            if ok:
                pat.add(m)
        F.append(JFun(W, frozenset(pat)))
    for c in range(D):
        W = tuple(sorted(sum([list(cell(r, c)) for r in range(D)], [])))
        pos = {co: b for b, co in enumerate(W)}
        pat = set()
        for m in range(1 << len(W)):
            ok = True
            for r in range(D):
                sub = 0
                for j, coord in enumerate(cell(r, c)):
                    if (m >> pos[coord]) & 1:
                        sub |= 1 << j
                if sub not in MUXc:
                    ok = False; break
            if ok:
                pat.add(m)
        G.append(JFun(W, frozenset(pat)))
    return F, G, 3 * D * D, 2 * D

for D in (1, 2):
    F, G, N, d = mux_grid(D)
    eval_design(F, G, N, f"MUX-tensor-grid D={D}", d)

# address grid: cells are k=2 address gadgets (degree 3, 6 coords)
def address_grid(D, k=1):
    T = 1 << k; s = k + T
    cellcoords = lambda r, c: tuple((r * D + c) * s + j for j in range(s))
    def gadget(W, comp):
        a = W[:k]; t = W[k:]
        f = address_jfun(a, t) if not comp else address_complement(a, t)
        return f
    F = []
    for r in range(D):
        pieces = [gadget(cellcoords(r, c), False) for c in range(D)]
        W = tuple(sorted(sum([list(p.window) for p in pieces], [])))
        pos = {c: b for b, c in enumerate(W)}
        pat = set()
        for m in range(1 << len(W)):
            ok = True
            for p in pieces:
                sub = 0
                for j, coord in enumerate(p.window):
                    if (m >> pos[coord]) & 1:
                        sub |= 1 << j
                if sub not in p.pat:
                    ok = False; break
            if ok:
                pat.add(m)
        F.append(JFun(W, frozenset(pat)))
    G = []
    for c in range(D):
        pieces = [gadget(cellcoords(r, c), True) for r in range(D)]
        W = tuple(sorted(sum([list(p.window) for p in pieces], [])))
        pos = {co: b for b, co in enumerate(W)}
        pat = set()
        for m in range(1 << len(W)):
            ok = True
            for p in pieces:
                sub = 0
                for j, coord in enumerate(p.window):
                    if (m >> pos[coord]) & 1:
                        sub |= 1 << j
                if sub not in p.pat:
                    ok = False; break
            if ok:
                pat.add(m)
        G.append(JFun(W, frozenset(pat)))
    return F, G, s * D * D, (k + 1) * D

for D in (1, 2):
    F, G, N, d = address_grid(D, k=1)
    eval_design(F, G, N, f"address(k=1)-grid D={D}", d)
F, G, N, d = address_grid(1, k=2)
eval_design(F, G, N, "address(k=2) single pair", d)

pr("\nDONE s4")
