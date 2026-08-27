"""
s1_class_structure.py -- exact structure of the R2 class C^ind_d.

ESTABLISHES (all exact integer / rational arithmetic):

 (S1) Junta size.  Maximal number of relevant coordinates of a degree-<=d
      {0,1}-valued function, exhaustively by the restriction recursion
      (d = 1,2; d = 3 up to window 5).

 (S2) Influence spectrum of the class: realisable values of
      Inf_i(1_A/||1_A||_2), and the total-influence range.

 (S3) FORCING LEMMA (d=2): every degree-<=2 set contained in a halfcube
      {x_i = sigma} is a subcube of codimension <= 2.

 (S4A) COMPLEMENT frontier: for every degree-<=d set A, (A, A^c) is an
      incompatible singleton pair inside the class (deg 1_{A^c} = deg 1_A),
      with value  max_i b_i(P) / (2 min(|P|, 2^k-|P|))   [by (F1)].
      Exhaustive minimisation over all degree-<=d patterns.

 (S4B) GENERAL singleton frontier: min over all disjoint pairs of max
      influence.  WLOG only the SIZE s>=1 of the shared window matters (all
      patterns on both windows are enumerated, so relabelling inside a window
      is absorbed), so the sweep is over (k_f, k_g, s) and all pattern pairs.
"""
import itertools, sys
from fractions import Fraction
from deg_lib import (deg_functions, genuine_patterns, genuine, pattern_degree,
                     JFun, disjoint, shared, payment_lhs,
                     total_influence, max_influence)

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

KMAX = {1: 4, 2: 6, 3: 5}      # d=3, k=6 has ~1e8 patterns: out of budget

# ---------------------------------------------------------------- (S1)
hr("(S1) exhaustive junta size of degree-<=d {0,1}-functions")
JMAX = {}
for d in (1, 2, 3):
    pr(f"  d = {d}   (a-priori junta bound d*2^(d-1) = {d*2**(d-1)})")
    top = 0
    for k in range(1, KMAX[d] + 1):
        L = deg_functions(k, d)
        gen = [p for p in L if p and len(p) < (1 << k) and genuine(p, k)]
        if k <= 4:
            assert all(pattern_degree(p, k) <= d for p in L)
        if gen:
            top = k
        pr(f"    k={k}: |L(k,d)|={len(L):8d}   genuine = {len(gen):7d}")
    JMAX[d] = top
    pr(f"    => max relevant coordinates found for d={d}: {top}"
       f"   (search exhaustive up to k={KMAX[d]})")

# ---------------------------------------------------------------- (S2)
hr("(S2) influence spectrum, degree-<=d sets")
SPECMAX = {2: 4, 3: 4}
for d in (2, 3):
    spec = {}
    Ts = []
    for k in range(1, min(JMAX[d], SPECMAX[d]) + 1):
        for p in genuine_patterns(k, d):
            f = JFun(tuple(range(k)), p)
            infl = f.influences()
            Ts.append(sum(infl.values(), Fraction(0)))
            for c, v in infl.items():
                spec.setdefault(v, [0, None])
                spec[v][0] += 1
                if spec[v][1] is None:
                    spec[v][1] = (k, sorted(p))
    pr(f"  d={d} (windows <= {min(JMAX[d],SPECMAX[d])}): nonzero influence values")
    for v in sorted(x for x in spec if x != 0)[:20]:
        pr(f"     {str(v):>10}  count {spec[v][0]:7d}  e.g. k={spec[v][1][0]}, P={spec[v][1][1]}")
    pr(f"     min nonzero influence = {min(x for x in spec if x!=0)}")
    pr(f"     total influence: min={min(Ts)} max={max(Ts)}  (budget d={d})")

# ---------------------------------------------------------------- (S3)
hr("(S3) FORCING LEMMA: degree-<=2 forcing sets are codim<=2 subcubes")
bad = []
for k in range(1, JMAX[2] + 1):
    for p in genuine_patterns(k, 2):
        f = JFun(tuple(range(k)), p)
        if any(len(f.project((b,))) == 1 for b in range(k)):
            forced = [c for c in range(k) if len(f.project((c,))) == 1]
            is_subcube = (len(p) == (1 << (k - len(forced))))
            if not (is_subcube and k <= 2):
                bad.append((k, sorted(p), forced, is_subcube))
pr(f"  degree-2 forcing sets that are NOT codim<=2 subcubes: {len(bad)}")
for x in bad[:6]:
    pr("   ", x)
rec = []
for k in range(1, min(JMAX[3], 4) + 1):
    for p in genuine_patterns(k, 3):
        f = JFun(tuple(range(k)), p)
        if any(len(f.project((b,))) == 1 for b in range(k)):
            forced = [c for c in range(k) if len(f.project((c,))) == 1]
            rec.append((k, len(forced), len(p) == (1 << (k - len(forced)))))
pr(f"  d=3 (windows<=4): {len(rec)} forcing sets, "
   f"{sum(1 for r in rec if not r[2])} of them not subcubes; "
   f"windows present {sorted(set(r[0] for r in rec))}")

# ---------------------------------------------------------------- (S4A)
hr("(S4A) COMPLEMENT-pair frontier  max_i b_i / (2 min(|P|,2^k-|P|))")
for d in (2, 3):
    best = None; arg = None; hist = {}
    for k in range(1, JMAX[d] + 1):
        for p in genuine_patterns(k, d):
            P = len(p); m = min(P, (1 << k) - P)
            bmax = max(sum(1 for x in p if (x ^ (1 << b)) not in p)
                       for b in range(k))
            v = Fraction(bmax, 2 * m)
            hist[v] = hist.get(v, 0) + 1
            if best is None or v < best:
                best = v; arg = (k, sorted(p), bmax, P)
    pr(f"  d={d}: min complement-pair value = {best}   (1/(2d) = {Fraction(1,2*d)})")
    pr(f"     witness: k={arg[0]} |P|={arg[3]} b_max={arg[2]} P={arg[1]}")
    pr(f"     smallest few values: "
       f"{sorted(hist.items())[:6]}")

# ---------------------------------------------------------------- (S4B)
hr("(S4B) general singleton frontier: min over disjoint pairs of max influence")
PAIRWIN = {2: 4, 3: 3}
for d in (2, 3):
    M = min(JMAX[d], PAIRWIN[d])
    prep = {}
    for k in range(1, M + 1):
        lst = []
        for p in genuine_patterns(k, d):
            f = JFun(tuple(range(k)), p)
            lst.append((max(f.influences().values()), p))
        lst.sort(key=lambda t: t[0])
        prep[k] = lst
    best = None; bestpair = None; cnt = 0
    for kf in range(1, M + 1):
        for kg in range(1, M + 1):
            for s in range(1, min(kf, kg) + 1):
                Wf = tuple(range(kf))
                Wg = tuple(list(range(s)) + list(range(kf, kf + kg - s)))
                for mf, pf in prep[kf]:
                    if best is not None and mf >= best:
                        break
                    f = JFun(Wf, pf)
                    for mg, pg in prep[kg]:
                        if best is not None and max(mf, mg) >= best:
                            break
                        g = JFun(Wg, pg)
                        cnt += 1
                        if not disjoint(f, g):
                            continue
                        v = max(mf, mg)
                        if best is None or v < best:
                            best = v; bestpair = (f, g)
    pr(f"  d={d} (windows <= {M}): min = {best}  (1/(2d) = {Fraction(1,2*d)});"
       f"  disjointness tests {cnt}")
    f, g = bestpair
    pr(f"     f = {f}  Inf={dict(f.influences())} T={total_influence(f)}")
    pr(f"     g = {g}  Inf={dict(g.influences())} T={total_influence(g)}")
    pr(f"     payment = {payment_lhs(f,g)}, shared window {shared(f,g)}")
pr("\nDONE s1")
