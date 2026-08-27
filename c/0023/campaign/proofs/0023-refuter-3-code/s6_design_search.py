"""
s6_design_search.py -- broad search for an incompatible pair beating 1/(2d)
inside C^ind_d.

Every incompatible pair may be closed: given (F,G), put
  cA = { A in class : A cap B = empty for all B in supp G },
  cB = { B in class : B cap A = empty for all A in cA },
then (cA, cB) is incompatible, supp F subseteq cA, supp G subseteq cB, and
max(tau(cA), tau(cB)) <= max(delta_F, delta_G).  So it suffices to search over
SEEDS: a small subfamily B_0 of the class determines cA = cA(B_0) and then cB.
Seeds of size 1 are swept exhaustively up to cube symmetry (s3); here we add
random seeds of size 1..4, structured seeds, and a hill-climb on the seed.

tau(fam) = min_p max_i sum_a p_a Inf_i(a), by LP; the reported minima are
re-certified in exact rational arithmetic (rational mixture upper bound +
rational dual weight lower bound).
"""
import itertools, random
from fractions import Fraction
from deg_lib import genuine_patterns, JFun, popcount
import numpy as np
from scipy.optimize import linprog

random.seed(31337)

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

def point_mask(W, pat, N):
    mask = 0
    for x in range(1 << N):
        m = 0
        for b, c in enumerate(W):
            if (x >> c) & 1:
                m |= 1 << b
        if m in pat:
            mask |= 1 << x
    return mask

def build_class(N, d, maxwin):
    """list of (mask, window, influence tuple) for all degree-<=d sets."""
    out = []
    seen = set()
    for k in range(1, min(N, maxwin) + 1):
        for p in genuine_patterns(k, d):
            f0 = JFun(tuple(range(k)), p)
            b = f0.bcounts()
            P = len(p)
            infl_by_pos = [Fraction(c, 2 * P) for c in b]
            for W in itertools.combinations(range(N), k):
                mk = point_mask(W, p, N)
                if mk in seen:
                    continue
                seen.add(mk)
                inf = [Fraction(0)] * N
                for pos, c in enumerate(W):
                    inf[c] = infl_by_pos[pos]
                out.append((mk, W, inf))
    return out

def tau(fam, N):
    """min_p max_i ... (primal LP); returns (value, p)."""
    m = len(fam)
    A = np.zeros((N, m + 1))
    for a, (_, W, inf) in enumerate(fam):
        for i in W:
            A[i, a] = float(inf[i])
    A[:, m] = -1.0
    cobj = np.zeros(m + 1); cobj[m] = 1.0
    Aeq = np.zeros((1, m + 1)); Aeq[0, :m] = 1.0
    res = linprog(cobj, A_ub=A, b_ub=np.zeros(N), A_eq=Aeq, b_eq=[1.0],
                  bounds=[(0, None)] * m + [(None, None)], method="highs")
    assert res.success
    return res.x[m], res.x[:m]

def exact_upper(fam, N, p, max_den=2520):
    """exact rational certificate tau <= q from a float mixture p."""
    q = [Fraction(x).limit_denominator(max_den) for x in p]
    s = sum(q)
    if s == 0:
        return None
    q = [x / s for x in q]
    acc = [Fraction(0)] * N
    for w, (_, W, inf) in zip(q, fam):
        if w == 0:
            continue
        for i in W:
            acc[i] += w * inf[i]
    return max(acc)

def closure_value(cls, seed_idx, N):
    B0 = [cls[i][0] for i in seed_idx]
    A = [t for t in cls if all(not (t[0] & b) for b in B0)]
    if not A:
        return None
    UA = 0
    for t in A:
        UA |= t[0]
    B = [t for t in cls if not (t[0] & UA)]
    if not B:
        return None
    tA, pA = tau(A, N)
    tB, pB = tau(B, N)
    return max(tA, tB), (A, pA, tA), (B, pB, tB)

def search(N, d, maxwin, nseed, sizes, label):
    cls = build_class(N, d, maxwin)
    n = len(cls)
    best = None
    # exhaustive single seeds up to symmetry: canonical-window representatives
    reps = []
    for k in range(1, min(N, maxwin) + 1):
        for p in genuine_patterns(k, d):
            mk = point_mask(tuple(range(k)), p, N)
            for idx, t in enumerate(cls):
                if t[0] == mk:
                    reps.append(idx); break
    trials = [(i,) for i in reps]
    for s in sizes:
        if s == 1:
            continue
        for _ in range(nseed):
            trials.append(tuple(random.sample(range(n), s)))
    for seed in trials:
        r = closure_value(cls, seed, N)
        if r is None:
            continue
        v = r[0]
        if best is None or v < best[0] - 1e-12:
            best = (v, seed, r)
    v, seed, r = best
    ub = exact_upper(r[1][0], N, r[1][1])
    ub2 = exact_upper(r[2][0], N, r[2][1])
    pr(f"  {label}: |class|={n} trials={len(trials)}  min eps = {v:.8f}"
       f"   eps*2d = {v*2*d:.5f}")
    pr(f"      exact rational certificates for the best design:"
       f" tauF <= {ub}, tauG <= {ub2}")
    return v

hr("d = 2: is 1/4 ever beaten?  (proof says no; this is the search)")
for N in (4, 5, 6, 7, 8, 9):
    search(N, 2, 4, 60, (1, 2, 3), f"d=2 N={N}")

hr("d = 3, windows <= 3")
for N in (4, 5, 6, 7):
    search(N, 3, 3, 30, (1, 2), f"d=3 N={N} (win<=3)")

hr("d = 3, windows <= 4 (class is large; single seeds + few random)")
for N in (5, 6):
    search(N, 3, 4, 6, (1, 2), f"d=3 N={N} (win<=4)")

pr("\nDONE s6")
