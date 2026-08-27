"""
s5_heavy_lemma.py -- the local lemma that would close R2 through the
TOTAL-INFLUENCE BUDGET (the route flagged in I02), and the attempt to break it.

THE COUNT (no window sizes anywhere, so the 2^Theta(d) junta trap is absent):

  (HEAVY_theta)  every disjoint pair (f,g) of degree-<=d sets has a coordinate
                 i in J_f cap K_g with  min(Inf_i(f), Inf_i(g)) >= theta(d).

  Given (HEAVY_theta): for an incompatible (F,G), every cross pair conflicts,
  so with H_F(i) = Pr_F[Inf_i(f) >= theta], H_G(i) = Pr_G[Inf_i(g) >= theta],
        1 = Pr_{a,b}[conflict] <= sum_i H_F(i) H_G(i)          (union bound)
                               <= sum_i (Ibar_F(i)/theta)(Ibar_G(i)/theta)   (Markov)
                               <= (delta_G/theta^2) sum_i Ibar_F(i)
                               <= (delta_G/theta^2) * d        (budget sum_i Inf_i <= d)
  hence  max(delta_F, delta_G) >= theta(d)^2 / d.
  So theta(d) >= 1/poly(d) PROVES the rung; theta(d) = 2^{-Theta(d)} kills the
  route.  This script computes
        theta*(d) = min over disjoint pairs of max_{i in S} min(Inf_i f, Inf_i g)
  as far as the class can be enumerated, and hunts for pairs with small
  theta among the objects that make relevant coordinates cheap (address /
  iterated-address / sparse sets).

Also verified here:
  (FORCE-1) a degree-<=d set forces at most d coordinates;
  (FORCE-2) a forced coordinate has influence exactly 1/2;
  which give the unconditional case-(i) bound delta >= 1/(8d) for pairs that
  conflict through an oppositely-forced coordinate (see the report).
"""
import itertools, random
from fractions import Fraction
from deg_lib import (genuine_patterns, JFun, disjoint, shared, payment_lhs,
                     total_influence, popcount, pattern_degree)

random.seed(7770001)

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

def theta_of(f, g):
    """max_{i in shared window} min(Inf_i f, Inf_i g)  (Fraction)."""
    If, Ig = f.influences(), g.influences()
    S = shared(f, g)
    return max((min(If[i], Ig[i]) for i in S), default=Fraction(0))

# ------------------------------------------------------------------
hr("(FORCE) #forced coordinates and their influence")
for d in (2, 3):
    kmax = {2: 4, 3: 5}[d]
    worstf = 0; okinf = True
    for k in range(1, kmax + 1):
        for p in genuine_patterns(k, d):
            f = JFun(tuple(range(k)), p)
            inf = f.influences()
            forced = [c for c in range(k) if len(f.project((c,))) == 1]
            worstf = max(worstf, len(forced))
            for c in forced:
                if inf[c] != Fraction(1, 2):
                    okinf = False
    pr(f"  d={d} (windows<={kmax}): max #forced coordinates = {worstf} (<= d ?"
       f" {'yes' if worstf <= d else 'NO'});"
       f"  every forced coordinate has influence exactly 1/2: {okinf}")

# ------------------------------------------------------------------
hr("theta*(d): exhaustive sweeps")

def sweep_theta(d, maxwin):
    pats = {k: genuine_patterns(k, d) for k in range(1, maxwin + 1)}
    best = None; n = 0
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
                        n += 1
                        t = theta_of(f, g)
                        if best is None or t < best[0]:
                            best = (t, f, g)
    return best, n

for d, mw in ((2, 4), (3, 3)):
    best, n = sweep_theta(d, mw)
    t, f, g = best
    pr(f"  d={d}, windows<={mw} EXHAUSTIVE ({n} disjoint pairs):"
       f"  theta* = {t}   (1/(2d) = {Fraction(1,2*d)})")
    pr(f"     minimiser f={f} Inf={dict(f.influences())}")
    pr(f"               g={g} Inf={dict(g.influences())}")
    pr(f"     theta^2/d = {t*t/d}")

pr("\n  d=3, ALL complement pairs (A,A^c) with window <= 5 (exhaustive):")
best = None
for k in range(1, 6):
    for p in genuine_patterns(k, 3):
        P = len(p); Q = (1 << k) - P
        mx = max(P, Q)
        bmax = max(sum(1 for x in p if (x ^ (1 << b)) not in p)
                   for b in range(k))
        t = Fraction(bmax, 2 * mx)         # max_i min(Inf_i f, Inf_i g)
        if best is None or t < best[0]:
            best = (t, k, sorted(p))
pr(f"    theta* over complement pairs = {best[0]} at k={best[1]}"
   f"  P={best[2][:12]}...")

pr("\n  d=3, windows 4-5, 4*10^5 random draws:")
pats45 = {4: genuine_patterns(4, 3), 5: genuine_patterns(5, 3)}
best = None; found = 0
for _ in range(400000):
    kf = random.choice([4, 5]); kg = random.choice([4, 5])
    s = random.randint(1, min(kf, kg))
    Wf = tuple(range(kf)); Wg = tuple(list(range(s)) + list(range(kf, kf + kg - s)))
    f = JFun(Wf, random.choice(pats45[kf])); g = JFun(Wg, random.choice(pats45[kg]))
    if not disjoint(f, g):
        continue
    found += 1
    t = theta_of(f, g)
    if best is None or t < best[0]:
        best = (t, f, g)
pr(f"    {found} disjoint pairs; theta* seen = {best[0]}")
pr(f"      f={best[1]}\n      g={best[2]}")

# ------------------------------------------------------------------
hr("the objects that make relevant coordinates cheap: address / iterated")

def address_jfun(k, comp=False):
    T = 1 << k; n = k + T
    W = tuple(range(n))
    pat = set()
    for m in range(1 << n):
        a = m & (T - 1)
        hit = not ((m >> (k + a)) & 1)
        if hit != comp:
            pat.add(m)
    return JFun(W, frozenset(pat))

pr("  address sets A_k (degree k+1, k+2^k relevant coords) vs their complement:")
for k in (1, 2, 3):
    f = address_jfun(k); g = address_jfun(k, comp=True)
    assert disjoint(f, g)
    t = theta_of(f, g)
    d = pattern_degree(f.pat, len(f.window))
    inf = f.influences()
    pr(f"    k={k}: d={d} |J|={len(f.window)}  min nonzero Inf = {min(inf.values())}"
       f"  theta = {t}   theta^2/d = {t*t/d}"
       f"   (1/(2d) = {Fraction(1,2*d)})")

pr("\n  'cheap-coordinate' stress test: for each address set A_k, search ALL")
pr("  degree-<=(k+1) sets g on a sub-window of A_k's window that are disjoint")
pr("  from A_k, and report the smallest theta (can a partner avoid the hub?).")
for k in (1, 2):
    f = address_jfun(k)
    d = k + 1
    n = len(f.window)
    best = None; cnt = 0
    for kg in range(1, min(n, 4) + 1):
        pats = genuine_patterns(kg, d)
        for Wg in itertools.combinations(range(n), kg):
            for pg in pats:
                g = JFun(Wg, pg)
                if not disjoint(f, g):
                    continue
                cnt += 1
                t = theta_of(f, g)
                if best is None or t < best[0]:
                    best = (t, g)
    pr(f"    k={k} (d={d}, |J|={n}): {cnt} disjoint partners with window<=4;"
       f" min theta = {best[0] if best else None}")
    if best:
        pr(f"      partner g={best[1]} Inf={dict(best[1].influences())}"
           f"  shared={shared(f,best[1])}")
        hub = set(range(k))
        pr(f"      does the partner's window meet the address block {sorted(hub)}?"
           f" {sorted(set(best[1].window) & hub)}")

pr("\nDONE s5")
