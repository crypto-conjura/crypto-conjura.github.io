"""
t3_structured.py -- exact eps*d for structured incompatible families at
general d, all inside the I01 indicator class.  Everything here is exact
(Fraction / integer combinatorics); product-rule closed forms are first
verified against brute-force JFun instances.

Architectures:
  A. product-cell grids: DxD grid of cells of size s; row R = indicator of
     prod_C U_{cell}, col C = indicator of prod_R V_{cell}, U cap V = empty;
     uniform distributions over rows / cols.  d = D*s,
     eps*d = s * cellcost(U,V),  cellcost = max_j max(b_j(U)/2|U|, b_j(V)/2|V|).
     - conjunction cells (grid): s=1, U={+}, V={-}         -> eps*d = 1/2
     - parity cells: U=even, V=odd on s bits               -> eps*d = s/2
     - tribes cells: U = tribes_{w,T}, V = U^c, s = wT     -> chart
     - ball cells: U = ball_rho, V = U^c, s = k            -> chart
     - phi(s) = min over ALL disjoint cell pairs (exhaustive s<=3,
       complement-exhaustive + 3x10^5 random pairs s=4,5)  -> chart
  B. single incompatible pairs (N = d, no spreading):
     - tribes vs complement (w,T)                          -> chart
     - ball vs complement (k, rho)                         -> chart
  C. low-density/high-density: U = single point vs V = U^c (s-cube):
     cellcost and pair values.
"""
import itertools, math, random, sys
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from junta_lib import JFun, disjoint, payment_ok

random.seed(7)

def bcounts_set(U, s):
    return [sum(1 for m in U if (m ^ (1 << b)) not in U) for b in range(s)]

def cellcost(U, V, s):
    bu, bv = bcounts_set(U, s), bcounts_set(V, s)
    return max(max(Fraction(c, 2 * len(U)) for c in bu),
               max(Fraction(c, 2 * len(V)) for c in bv))

# ---------------------------------------------------------------------
# 0. verify the product rule on brute-force instances:
#    row function = indicator of product pattern over D cells; check
#    influences and cross-disjointness against JFun ground truth.
# ---------------------------------------------------------------------
def product_jfun(cells, s):
    """cells: list of subsets of {0,1}^s; window = concatenated coords."""
    D = len(cells)
    window = tuple(range(D * s))
    pats = []
    for combo in itertools.product(*cells):
        m = 0
        for c, mc in enumerate(combo):
            m |= mc << (c * s)
        pats.append(m)
    return JFun(window, pats)

ok = True
for trial in range(60):
    s = random.randint(1, 3)
    D = random.randint(1, 3)
    cells = [set(random.sample(range(1 << s), random.randint(1, (1 << s) - 1)))
             for _ in range(D)]
    f = product_jfun(cells, s)
    inf = f.influences()
    for c in range(D):
        b = bcounts_set(cells[c], s)
        for j in range(s):
            if inf[c * s + j] != Fraction(b[j], 2 * len(cells[c])):
                ok = False; print("product rule FAIL", cells, c, j)
print("T3.0 product rule (influence of product pattern = cell influence):",
      "OK" if ok else "FAIL")

# grid incompatibility sanity: brute-force at D=2, s=2 with U,V disjoint
s, D = 2, 2
U = {0b00, 0b11}; V = {0b01}
rows, cols = [], []
for R in range(D):
    # row R occupies cells (R,C), coordinate block index R*D+C
    cellsets = [U] * D
    f = product_jfun(cellsets, s)
    f = JFun(tuple(i + R * D * s for i in f.window), f.pat)
    rows.append(f)
for C in range(D):
    window = []
    for R in range(D):
        window += [R * D * s + C * s + j for j in range(s)]
    window = tuple(sorted(window))
    pats = []
    for combo in itertools.product(*([sorted(V)] * D)):
        m = 0
        for idx, mc in enumerate(combo):
            m |= mc << (idx * s)
        pats.append(m)
    cols.append(JFun(window, pats))
ok = all(disjoint(f, g) for f in rows for g in cols)
print("T3.0 grid cross-disjointness (D=2,s=2 brute):", "OK" if ok else "FAIL")
pay = [payment_ok(f, g) for f in rows for g in cols]
print("     payments per cross pair:", sorted({str(p[1]) for p in pay}))

# ---------------------------------------------------------------------
# A. product-cell grids
# ---------------------------------------------------------------------
print("\n== A. product-cell grids: eps*d = s * cellcost(U,V) ==")
print("conjunction cells (s=1): eps*d =", Fraction(1, 1) * cellcost({0}, {1}, 1))
for s in (2, 3, 4):
    even = {m for m in range(1 << s) if bin(m).count('1') % 2 == 0}
    odd = set(range(1 << s)) - even
    print(f"parity cells s={s}: eps*d = {s * cellcost(even, odd, s)}")

def tribes_pair_stats(w, T):
    """U = OR of T disjoint ANDs of width w (AND = all bits 0, say).
    Returns (s, bU, |U|, |U^c|): b_i identical for all i by symmetry."""
    s = w * T
    Uc = (2**w - 1) ** T          # all tribes fail
    Usz = 2**s - Uc
    b = (2**w - 1) ** (T - 1)     # others fail, own tribe others satisfied
    return s, b, Usz, Uc

# verify tribes closed form vs brute force
for (w, T) in [(1, 1), (1, 2), (2, 2), (3, 2), (2, 3)]:
    s, b, Usz, Uc = tribes_pair_stats(w, T)
    U = set()
    for m in range(1 << s):
        if any(all(not ((m >> (t * w + j)) & 1) for j in range(w))
               for t in range(T)):
            U.add(m)
    bb = bcounts_set(U, s)
    assert len(U) == Usz and all(x == b for x in bb), (w, T, bb, b)
print("tribes closed form verified vs brute force (w,T) up to (2,3)")

print("tribes cells, eps*d = s * max(b/2|U|, b/2|U^c|):")
best = None
for w in range(1, 7):
    for T in range(1, 65):
        s, b, Usz, Uc = tribes_pair_stats(w, T)
        if s > 4096: break
        v = s * max(Fraction(b, 2 * Usz), Fraction(b, 2 * Uc))
        if best is None or v < best[0]:
            best = (v, w, T, s)
for w in range(1, 7):
    row = []
    for T in (1, 2, 4, 8, 16, 32):
        s, b, Usz, Uc = tribes_pair_stats(w, T)
        v = s * max(Fraction(b, 2 * Usz), Fraction(b, 2 * Uc))
        row.append(f"{float(v):8.3f}")
    print(f"  w={w}: T=1,2,4,8,16,32 -> {' '.join(row)}")
print(f"  minimum over w<=6, T<=64: eps*d = {best[0]} = {float(best[0]):.4f}"
      f" at (w,T)=({best[1]},{best[2]}) [s={best[3]}]")

def ball_stats(k, rho):
    Usz = sum(math.comb(k, j) for j in range(rho + 1))
    b = math.comb(k - 1, rho)
    return b, Usz, 2**k - Usz

for (k, rho) in [(3, 1), (4, 1), (5, 2)]:
    b, Usz, Uc = ball_stats(k, rho)
    U = {m for m in range(1 << k) if bin(m).count('1') <= rho}
    bb = bcounts_set(U, k)
    assert len(U) == Usz and all(x == b for x in bb)
print("ball closed form verified vs brute force")

print("ball cells (U=ball_rho, V=U^c): eps*d = k*max(b/2|U|,b/2|V|):")
bestb = None
for k in range(1, 41):
    for rho in range(0, k):
        b, Usz, Uc = ball_stats(k, rho)
        v = k * max(Fraction(b, 2 * Usz), Fraction(b, 2 * Uc))
        if bestb is None or v < bestb[0]:
            bestb = (v, k, rho)
print(f"  minimum over k<=40: eps*d = {bestb[0]} = {float(bestb[0]):.4f} "
      f"at (k,rho)=({bestb[1]},{bestb[2]})")

print("phi(s) = s * min over ALL disjoint cell pairs of cellcost:")
for s in (1, 2, 3):
    pts = list(range(1 << s))
    best = None
    # assign each point to U / V / neither
    for assign in itertools.product((0, 1, 2), repeat=1 << s):
        U = {p for p in pts if assign[p] == 1}
        V = {p for p in pts if assign[p] == 2}
        if not U or not V:
            continue
        v = s * cellcost(U, V, s)
        if best is None or v < best[0]:
            best = (v, U, V)
    print(f"  s={s}: phi = {best[0]} = {float(best[0]):.4f}  "
          f"(U={sorted(best[1])}, V={sorted(best[2])})  EXHAUSTIVE")
for s in (4, 5):
    best = None
    # all complement pairs
    for bits in range(1, 1 << (1 << s)) if s == 4 else []:
        U = {m for m in range(1 << s) if (bits >> m) & 1}
        if len(U) > (1 << s) // 2:
            continue
        v = s * cellcost(U, set(range(1 << s)) - U, s)
        if best is None or v < best[0]:
            best = (v, "compl", len(U))
    # random disjoint pairs
    for _ in range(300000):
        P = 1 << s
        u = random.randint(1, P - 1)
        U = set(random.sample(range(P), u))
        rest = [m for m in range(P) if m not in U]
        V = set(random.sample(rest, random.randint(1, len(rest))))
        v = s * cellcost(U, V, s)
        if best is None or v < best[0]:
            best = (v, sorted(U), sorted(V))
    tag = "complement-EXHAUSTIVE + 3e5 random" if s == 4 else "3e5 random"
    print(f"  s={s}: phi <= {best[0]} = {float(best[0]):.4f}  ({tag}) "
          f"witness {best[1:] if best[0] < Fraction(1,2) else '(none below 1/2)'}")

# ---------------------------------------------------------------------
# B. single incompatible pairs at N = d (no distribution spreading)
# ---------------------------------------------------------------------
print("\n== B. single pairs, N=d: eps*d = d * max-coordinate influence ==")
best = None
for w in range(1, 8):
    for T in range(1, 200):
        s, b, Usz, Uc = tribes_pair_stats(w, T)
        if s > 1200: break
        v = s * max(Fraction(b, 2 * Usz), Fraction(b, 2 * Uc))
        if best is None or v < best[0]:
            best = (v, w, T, s)
print(f"tribes vs complement: min eps*d = {float(best[0]):.4f} at "
      f"(w,T)=({best[1]},{best[2]}), d={best[3]}"
      f"  [same functional form as cells; growth ~ (w+1)/2 -> Theta(log d)]")
bestb = None
for k in range(1, 61):
    for rho in range(0, k):
        b, Usz, Uc = ball_stats(k, rho)
        v = k * max(Fraction(b, 2 * Usz), Fraction(b, 2 * Uc))
        if bestb is None or v < bestb[0]:
            bestb = (v, k, rho)
print(f"ball vs complement: min eps*d = {float(bestb[0]):.4f} at "
      f"(k,rho)=({bestb[1]},{bestb[2]})")

# C. point vs complement
print("\n== C. point vs complement (s-cube) ==")
for s in (2, 4, 8, 16):
    U = {0}; b1 = [1] * s
    v = s * max(Fraction(1, 2), Fraction(1, 2 * (2**s - 1)))
    print(f"  s={s}: eps*d = {v} (sparse side pays 1/2 per coordinate)")
