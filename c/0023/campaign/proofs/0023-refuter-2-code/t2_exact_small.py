"""
t2_exact_small.py -- exact eps*_junta(d, N) for (d,N) in
(2,2), (2,3), (2,4), (3,4), by exhaustion over all support partitions of
the N-cube up to cube symmetry (coordinate permutations x translations,
plus side swap; the symmetry group maps the I01 class to itself, permuting
influences, so orbit reduction is valid).

For a partition (A, A^c):  F ranges over ALL class functions with support
inside A, G over those inside A^c (enlarging families only lowers the LP,
so the partition sweep is exhaustive for the rung: every incompatible pair
(F,G) has U_F cap U_G = 0 and embeds in the partition A = U_G^c).

Per side the optimum over distributions is the LP
    tau(side) = min_p max_i sum_a p_a Inf_i(f_a)
              = max_{w in simplex} min_a <w, I_a>   (LP duality).
Float sweep with scipy; then EXACT rational certification:
  * for every feasible orbit, a certified lower bound on its value from
    rounded rational dual weights (exact Fraction arithmetic);
  * for the minimal orbit(s), a certified upper bound from a rounded
    rational mixture.
Output: certified rational eps*_junta(d,N).
"""
import itertools, sys, time
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
sys.path.insert(0, __file__.rsplit("/", 2)[0] + "/0023-refuter-1-code")
from junta_lib import (JFun, all_class_functions, tau_lp,
                       tau_dual_lower_exact, tau_upper_exact,
                       rounded_fraction_vector)
from pcc_lib import z2_partition_orbit_reps
import numpy as np
from scipy.optimize import linprog


def tau_dual_lp(funs, coords):
    """Solve max_{w in simplex over coords} min_a <w, I_a>; return (val, w)."""
    ci = {c: j for j, c in enumerate(coords)}
    n, m = len(coords), len(funs)
    # vars w_0..w_{n-1}, t ; max t ; t - <w, I_a> <= 0 ; sum w = 1 ; w >= 0
    A_ub = np.zeros((m, n + 1))
    for a, f in enumerate(funs):
        for c, v in f.influences().items():
            A_ub[a, ci[c]] = -float(v)
        A_ub[a, n] = 1.0
    c_obj = np.zeros(n + 1); c_obj[n] = -1.0
    A_eq = np.zeros((1, n + 1)); A_eq[0, :n] = 1.0
    res = linprog(c_obj, A_ub=A_ub, b_ub=np.zeros(m), A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, None)] * n + [(None, None)], method="highs")
    if not res.success:
        raise RuntimeError("dual LP failed")
    return res.x[n], {c: res.x[ci[c]] for c in coords}


def certify_side_lower(funs, w_float, coords, max_den=64):
    """Round dual weights to rationals on the simplex; exact lower bound."""
    best = Fraction(0)
    for md in (max_den, 240, 5040):
        w = {c: Fraction(w_float[c]).limit_denominator(md) for c in coords}
        s = sum(w.values())
        if s <= 0:
            continue
        w = {c: v / s for c, v in w.items()}          # renormalize exactly
        lb = tau_dual_lower_exact(funs, w)
        if lb > best:
            best = lb
    return best


def run(d, N, verbose_top=3):
    t0 = time.time()
    funs = all_class_functions(d, N)
    supp = [f.support_mask(N) for f in funs]
    FULL = (1 << (1 << N)) - 1
    reps = z2_partition_orbit_reps(N)
    print(f"\n=== (d,N)=({d},{N}) : {len(funs)} class functions, "
          f"{len(reps)} partition orbits ===")
    results = []
    for A in reps:
        Ac = FULL ^ A
        Fi = [i for i in range(len(funs)) if supp[i] & Ac == 0]
        Gi = [i for i in range(len(funs)) if supp[i] & A == 0]
        if not Fi or not Gi:
            continue
        vals = []
        for idxs in (Fi, Gi):
            fam = [funs[i] for i in idxs]
            t, p, _ = tau_lp(fam)
            vals.append((t, fam, p))
        v = max(vals[0][0], vals[1][0])
        results.append((v, A, vals))
    results.sort(key=lambda r: r[0])
    print(f"feasible orbits: {len(results)}; float minimum value: "
          f"{results[0][0]:.9f}  (time {time.time()-t0:.1f}s)")
    for v, A, vals in results[:verbose_top]:
        print(f"  orbit A={A:#x}: value {v:.9f} "
              f"(sides {vals[0][0]:.6f}/{vals[1][0]:.6f}, "
              f"|F|={len(vals[0][1])}, |G|={len(vals[1][1])})")

    # ---- exact certification ----
    guess = Fraction(results[0][0]).limit_denominator(60)
    print(f"rational guess for eps*_junta({d},{N}): {guess}")
    # (i) certified lower bound for every feasible orbit
    global_lb = None
    n_below = 0
    for v, A, vals in results:
        orbit_lb = None
        for t, fam, p in vals:
            coords = sorted({c for f in fam for c in f.window})
            _, w = tau_dual_lp(fam, coords)
            lb = certify_side_lower(fam, w, coords)
            orbit_lb = lb if orbit_lb is None else max(orbit_lb, lb)
            if orbit_lb >= guess:
                break                        # this orbit certified >= guess
        if orbit_lb < guess:
            n_below += 1
            print(f"  !! orbit A={A:#x} certified lower bound {orbit_lb} "
                  f"< guess {guess} (float value {v:.9f})")
        global_lb = orbit_lb if global_lb is None else min(global_lb, orbit_lb)
    # (ii) certified upper bound at the best orbit
    v, A, vals = results[0]
    ubs = []
    for t, fam, p in vals:
        pr = rounded_fraction_vector(p, 10**6)
        s = sum(pr)
        pr = [x / s for x in pr]
        ubs.append(tau_upper_exact(fam, pr))
    ub = max(ubs)
    print(f"certified: every feasible orbit >= {global_lb} "
          f"({n_below} orbits below guess), best orbit <= {ub}")
    if global_lb == ub == guess:
        print(f"EXACT: eps*_junta({d},{N}) = {guess}")
    else:
        print(f"BOUNDS: {global_lb} <= eps*_junta({d},{N}) <= {ub}")
    return guess, global_lb, ub


if __name__ == "__main__":
    out = {}
    for (d, N) in [(2, 2), (2, 3), (2, 4), (3, 4)]:
        out[(d, N)] = run(d, N)
    print("\nSUMMARY", {k: tuple(map(str, v)) for k, v in out.items()})
