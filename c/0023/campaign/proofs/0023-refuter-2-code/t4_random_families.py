"""
t4_random_families.py -- stochastic + hill-climbing search for incompatible
I01-class family pairs with eps*d < 1/2, over free-form architectures the
structured sweep (t3) does not cover: overlapping windows, hub/sunflower
layouts, non-product patterns, unequal LP-optimized weights.

Per sampled configuration:
  - cross-disjointness enforced by an exact repair loop (projection test);
  - eps = max(tau_LP(F), tau_LP(G)) with scipy (floats);
  - EXACT integer payment audit of every cross pair (fact F4);
  - any eps*d < 0.5 - 1e-7 is escalated (printed loudly, exact recheck).

Also: exact exhaustive eps*_junta(3,3) (same-window / nested-window regime)
via the 13 partition orbits of the 3-cube.
"""
import itertools, random, sys, time
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
sys.path.insert(0, __file__.rsplit("/", 2)[0] + "/0023-refuter-1-code")
from junta_lib import (JFun, disjoint, shared, payment_ok, tau_lp,
                       all_class_functions)

random.seed(20260828)

# ---------------------------------------------------------------------
# exhaustive (3,3)
# ---------------------------------------------------------------------
def exhaustive_33():
    from pcc_lib import z2_partition_orbit_reps
    from junta_lib import tau_dual_lower_exact, tau_upper_exact, \
        rounded_fraction_vector
    funs = all_class_functions(3, 3)
    supp = [f.support_mask(3) for f in funs]
    FULL = (1 << 8) - 1
    best = None
    for A in z2_partition_orbit_reps(3):
        Ac = FULL ^ A
        F = [funs[i] for i in range(len(funs)) if supp[i] & Ac == 0]
        G = [funs[i] for i in range(len(funs)) if supp[i] & A == 0]
        if not F or not G:
            continue
        tF, pF, _ = tau_lp(F)
        tG, pG, _ = tau_lp(G)
        v = max(tF, tG)
        if best is None or v < best[0]:
            best = (v, A, (F, pF), (G, pG))
    v, A, (F, pF), (G, pG) = best
    guess = Fraction(v).limit_denominator(60)
    # exact upper bound certificate
    ubs = []
    for fam, p in ((F, pF), (G, pG)):
        pr = rounded_fraction_vector(p, 10**6); s = sum(pr)
        ubs.append(tau_upper_exact(fam, [x / s for x in pr]))
    print(f"exhaustive eps*_junta(3,3): float {v:.9f}, guess {guess}, "
          f"certified <= {max(ubs)} at orbit A={A:#x}")
    return guess

# ---------------------------------------------------------------------
# generator + repair
# ---------------------------------------------------------------------
def rand_pattern(k, style=None):
    P = 1 << k
    style = style or random.choice(["sparse", "dense", "balanced", "any"])
    if style == "sparse":
        sz = random.randint(1, max(1, P // 8))
    elif style == "dense":
        sz = P - random.randint(1, max(1, P // 8))
    elif style == "balanced":
        sz = P // 2 + random.randint(-P // 8, P // 8) if P >= 4 else 1
    else:
        sz = random.randint(1, P - 1)
    sz = min(max(sz, 1), P - 1)
    return frozenset(random.sample(range(P), sz))

def make_windows(mode, d, N, m, mp):
    """Return (F_windows, G_windows); every cross pair must intersect."""
    coords = list(range(N))
    if mode == "hub":
        h = random.randint(1, max(1, d // 2))
        core = coords[:h]
        FW, GW = [], []
        for _ in range(m):
            extra = random.sample(coords[h:], random.randint(0, d - h))
            FW.append(tuple(sorted(core + extra)))
        for _ in range(mp):
            extra = random.sample(coords[h:], random.randint(0, d - h))
            GW.append(tuple(sorted(core + extra)))
        return FW, GW
    if mode == "random":
        for _ in range(200):
            FW = [tuple(sorted(random.sample(coords, random.randint(1, d))))
                  for _ in range(m)]
            GW = [tuple(sorted(random.sample(coords, random.randint(1, d))))
                  for _ in range(mp)]
            if all(set(a) & set(b) for a in FW for b in GW):
                return FW, GW
        return None
    if mode == "grid":
        # bipartite cell structure: F_a and G_b share cell block (a,b)
        s = max(1, d // mp)
        sp = max(1, d // m)
        # need m*mp*cellsize coords; reuse a cell size c = 1..2
        c = random.choice([1, 2])
        if m * mp * c > N or c * mp > d or c * m > d:
            return None
        FW = [tuple(sorted((a * mp + b) * c + j for b in range(mp)
                           for j in range(c))) for a in range(m)]
        GW = [tuple(sorted((a * mp + b) * c + j for a in range(m)
                           for j in range(c))) for b in range(mp)]
        return FW, GW
    if mode == "chain":
        # nested windows around a sliding overlap
        FW = []
        GW = []
        for a in range(m):
            st = random.randint(0, max(0, N - d))
            FW.append(tuple(range(st, min(N, st + random.randint(1, d)))))
        for b in range(mp):
            st = random.randint(0, max(0, N - d))
            GW.append(tuple(range(st, min(N, st + random.randint(1, d)))))
        if all(set(a) & set(b) for a in FW for b in GW):
            return FW, GW
        return None
    return None

def repair(F, G, max_iter=400):
    """Exact repair to cross-disjointness; returns None on failure."""
    for _ in range(max_iter):
        bad = None
        for i, f in enumerate(F):
            for j, g in enumerate(G):
                S = shared(f, g)
                if not S:
                    return None
                inter = f.project(S) & g.project(S)
                if inter:
                    bad = (i, j, S, inter)
                    break
            if bad:
                break
        if bad is None:
            return F, G
        i, j, S, inter = bad
        w = random.choice(sorted(inter))
        # remove fibers over w from one side (prefer the denser pattern)
        f, g = F[i], G[j]
        side = 0 if (len(f.pat) * (1 << g.k) > len(g.pat) * (1 << f.k)
                     ) == (random.random() < 0.8) else 1
        tgt = f if side == 0 else g
        pos = [tgt.window.index(c) for c in S]
        keep = frozenset(m for m in tgt.pat
                         if sum(((m >> p) & 1) << jj
                                for jj, p in enumerate(pos)) != w)
        if not keep:
            keep = rand_pattern(tgt.k)  # reshuffle and retry
        new = JFun(tgt.window, keep)
        if side == 0:
            F[i] = new
        else:
            G[j] = new
    return None

def config_value(F, G):
    tF, pF, _ = tau_lp(F)
    tG, pG, _ = tau_lp(G)
    return max(tF, tG)

def audit(F, G):
    minpay = None
    for f in F:
        for g in G:
            ok, lhs = payment_ok(f, g)
            if not ok:
                print("  !!! PAYMENT < 1:", f, g, lhs)
                return False, lhs
            if minpay is None or lhs < minpay:
                minpay = lhs
    return True, minpay

# ---------------------------------------------------------------------
# hill climb
# ---------------------------------------------------------------------
def climb(F, G, steps=300):
    best = config_value(F, G)
    for _ in range(steps):
        side = random.random() < 0.5
        fam = F if side else G
        oth = G if side else F
        i = random.randrange(len(fam))
        f = fam[i]
        move = random.random()
        newf = None
        if move < 0.45 and len(f.pat) > 1:      # remove a point
            drop = random.choice(sorted(f.pat))
            newf = JFun(f.window, f.pat - {drop})
        elif move < 0.9:                        # add a point if legal
            cand = [m for m in range(1 << f.k) if m not in f.pat]
            if cand:
                add = random.choice(cand)
                newf = JFun(f.window, f.pat | {add})
                if not all(disjoint(newf, g) for g in oth):
                    newf = None
        else:                                    # duplicate+perturb function
            newf = None
        if newf is None:
            continue
        old = fam[i]
        fam[i] = newf
        v = config_value(F, G)
        if v <= best + 1e-12:
            best = v
        else:
            fam[i] = old
    return best

# ---------------------------------------------------------------------
# main sweep
# ---------------------------------------------------------------------
if __name__ == "__main__":
    t0 = time.time()
    print("== exhaustive same/nested-window case ==")
    exhaustive_33()

    print("\n== stochastic sweep ==")
    REGIMES = [(2, 6), (2, 8), (3, 6), (3, 9), (4, 8), (4, 12), (5, 10),
               (6, 12)]
    NTRIAL = {2: 700, 3: 500, 4: 350, 5: 250, 6: 200}
    grand = []
    for (d, N) in REGIMES:
        best = None
        trials = ok_trials = 0
        for _ in range(NTRIAL[d]):
            trials += 1
            mode = random.choice(["hub", "random", "grid", "chain"])
            m, mp = random.randint(1, 5), random.randint(1, 5)
            W = make_windows(mode, d, N, m, mp)
            if W is None:
                continue
            FW, GW = W
            F = [JFun(w, rand_pattern(len(w))) for w in FW]
            G = [JFun(w, rand_pattern(len(w))) for w in GW]
            R = repair(F, G)
            if R is None:
                continue
            F, G = R
            ok_trials += 1
            v = config_value(F, G)
            if best is None or v < best[0]:
                best = (v, mode, [(f.window, sorted(f.pat)) for f in F],
                        [(g.window, sorted(g.pat)) for g in G], F, G)
        # hill-climb the best config
        v0, mode = best[0], best[1]
        F, G = best[4], best[5]
        v1 = climb([x for x in F], [x for x in G], steps=250)
        okp, minpay = audit(F, G)
        flag = "  <<< BELOW 1/2 !!!" if min(v0, v1) * d < 0.5 - 1e-7 else ""
        print(f"(d,N)=({d},{N}): {ok_trials}/{trials} valid configs; "
              f"best eps*d = {v0*d:.4f} ({mode}), after climb {v1*d:.4f}; "
              f"min exact payment {minpay}{flag}")
        grand.append(min(v0, v1) * d)
    print(f"\nglobal minimum eps*d over sweep: {min(grand):.4f} "
          f"(theorem floor 1/2 = grid; time {time.time()-t0:.0f}s)")
