"""
r4_designs_bigN.py -- design search at N = 9..12, i.e. AT THE SCALE WHERE THE
1/6 WITNESS LIVES (the 3x3 grid of codim-3 subcubes needs N = 9).

Every set is a pair (window J subseteq [N], pattern P subseteq {0,1}^|J|) with
deg(1_P) <= 3, carried together with its exact influence vector b_i/(2|P|) and
its point-mask over the 2^N points (packed uint64 words).  Cross-disjointness
is decided EXACTLY by mask intersection.

CLOSURE STEP (the strongest move).  For a seed family H,
    F := {u in universe : u cap (union H) = empty},
    G := {u in universe : u cap (union F) = empty}   (so H subseteq G),
and (F,G) is cross-disjoint with max(tau F, tau G) <= max over any design whose
G-side contains H.  Every reported value is a genuine upper bound for
eps*_ind(3,N) restricted to the universe.

TESTS
 (T1) F = K codim-3 subcubes on K disjoint triples, K = 3,4,5: what survives on
      the other side?  (K >= 4 has Ibar_F = 1/(2K) < 1/6, so a nonempty partner
      side with small tau would REFUTE the rung; kappa <= 3 from r3 predicts the
      partner side collapses.)
 (T2) closure from the 3x3 grid: is 1/6 a local optimum?
 (T3) closure + hill-climbing from many random and structured seeds at
      N = 9,10,11,12 over a pool that includes window-4/5/6 patterns of the
      lowest total influence, the CHEAP window-6 sets, and the Phi = 3/16
      minimisers.
"""
import sys, time, random, itertools
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import (level3_all, next_level, bvec, popcnt, flip_arrays)

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)
rng = np.random.default_rng(777)
random.seed(777)

# ------------------------------------------------------------------ catalogue
pr("building pattern catalogue ...")
L = {3: level3_all()}
L[4] = next_level(L[3], 3)
L[5] = next_level(L[4], 4)
POOL = {}                     # w -> list of (patmask, b-vector, |P|, T)
def add_pool(w, masks):
    B = bvec(masks, w)
    n = popcnt(masks)
    gen = np.all(B > 0, axis=1) & (n > 0) & (n < (1 << w))
    idx = np.flatnonzero(gen)
    T = (B[idx].sum(axis=1) / (2.0 * n[idx]))
    out = [(int(masks[j]), B[j].tolist(), int(n[j]), float(t))
           for j, t in zip(idx, T)]
    POOL[w] = out
for w in (1, 2, 3):
    add_pool(w, np.arange(1 << (1 << w), dtype=np.uint64))
add_pool(4, L[4])
# window 5: keep the 4000 of smallest total influence + 1500 random
add_pool(5, L[5])
p5 = sorted(POOL[5], key=lambda z: z[3])
POOL[5] = p5[:4000] + random.sample(p5[4000:], min(1500, len(p5) - 4000))
# window 6: cheap sets + Phi-minimisers + lowest-T sample, from the saved level
L6 = np.load("L6.npy"); B6 = np.load("L6_b.npy").astype(np.int32); N6 = np.load("L6_n.npy").astype(np.int32)
gen6 = np.all(B6 > 0, axis=1)
T6 = B6.sum(axis=1) / (2.0 * np.maximum(N6, 1))
cheap6 = gen6 & np.all(B6 * 3 < N6[:, None], axis=1)
mn6 = np.minimum(N6, 64 - N6)
phi6 = gen6 & (B6.max(axis=1) * 16 == 3 * 2 * mn6)          # Phi = 3/16
cand = np.flatnonzero(cheap6)[:400]
cand = np.concatenate([cand, np.flatnonzero(phi6)[:400]])
lowT = np.flatnonzero(gen6)[np.argsort(T6[gen6])[:1500]]
cand = np.unique(np.concatenate([cand, lowT,
                                 rng.choice(np.flatnonzero(gen6), 1200, replace=False)]))
POOL[6] = [(int(L6[j]), B6[j].tolist(), int(N6[j]), float(T6[j])) for j in cand]
for w in sorted(POOL):
    pr(f"  window {w}: {len(POOL[w])} patterns, min T = "
       f"{min(z[3] for z in POOL[w]):.4f}")
del L6, B6, N6

# ------------------------------------------------------------------- universe
def build_universe(N, wmax=6, cap=260000):
    """list of (window, patmask, inf(list of Fractions indexed by coord)),
    plus packed point-masks."""
    items = []
    for w in range(1, wmax + 1):
        wins = list(itertools.combinations(range(N), w))
        pats = POOL[w]
        tot = len(wins) * len(pats)
        take = pats
        if tot > cap // wmax:
            k = max(1, (cap // wmax) // len(wins))
            take = sorted(pats, key=lambda z: z[3])[:k]
        for J in wins:
            for (pm, b, n, T) in take:
                items.append((J, pm, b, n))
    W = (1 << N + 63) // 64 if False else ((1 << N) + 63) // 64
    masks = np.zeros((len(items), W), dtype=np.uint64)
    inf = np.zeros((len(items), N), dtype=np.float64)
    for a, (J, pm, b, n) in enumerate(items):
        for i, c in enumerate(J):
            if b[i]:
                inf[a, c] = b[i] / (2.0 * n)
        # point mask
        free = [c for c in range(N) if c not in J]
        base_pts = []
        for m in range(1 << len(J)):
            if (pm >> m) & 1:
                x0 = 0
                for i, c in enumerate(J):
                    if (m >> i) & 1:
                        x0 |= 1 << c
                base_pts.append(x0)
        for fill in range(1 << len(free)):
            add = 0
            for j, c in enumerate(free):
                if (fill >> j) & 1:
                    add |= 1 << c
            for x0 in base_pts:
                x = x0 | add
                masks[a, x >> 6] |= np.uint64(1) << np.uint64(x & 63)
    return items, masks, inf

from scipy.optimize import linprog
def tau(infrows):
    """min_p max_i sum_a p_a I_a(i) over the given influence rows."""
    A = np.unique(infrows, axis=0)
    m, N = A.shape
    Aub = np.concatenate([A.T, -np.ones((N, 1))], axis=1)
    c = np.zeros(m + 1); c[m] = 1.0
    Aeq = np.zeros((1, m + 1)); Aeq[0, :m] = 1.0
    r = linprog(c, A_ub=Aub, b_ub=np.zeros(N), A_eq=Aeq, b_eq=[1.0],
                bounds=[(0, None)] * m + [(None, None)], method="highs")
    return (r.x[m], A, r.x[:m]) if r.success else (None, A, None)

def union_mask(masks, sel):
    return np.bitwise_or.reduce(masks[sel], axis=0) if np.any(sel) else None

def disjoint_from(masks, U):
    return ~np.any(masks & U, axis=1)

def closure(masks, inf, seedsel):
    U = union_mask(masks, seedsel)
    if U is None:
        return None
    selF = disjoint_from(masks, U)
    if not selF.any():
        return None
    UF = union_mask(masks, selF)
    selG = disjoint_from(masks, UF)
    if not selG.any():
        return None
    tF = tau(inf[selF]); tG = tau(inf[selG])
    if tF[0] is None or tG[0] is None:
        return None
    return max(tF[0], tG[0]), selF, selG, tF, tG

def exact_cert(A, p, maxden=10**6):
    q = [Fraction(float(x)).limit_denominator(maxden) for x in p]
    s = sum(q)
    if s == 0:
        return None
    q = [x / s for x in q]
    acc = None
    for wq, row in zip(q, A):
        if wq == 0:
            continue
        r = [wq * Fraction(float(v)).limit_denominator(10**6) for v in row]
        acc = r if acc is None else [a + b for a, b in zip(acc, r)]
    return max(acc)

results = []
for N in (9, 10, 11, 12):
    hr(f"N = {N}")
    items, masks, inf = build_universe(N)
    pr(f"  universe: {len(items)} placed sets, mask words {masks.shape[1]} "
       f"({time.time()-t0:.0f}s)")
    idx_of = {}
    for a, (J, pm, b, n) in enumerate(items):
        idx_of.setdefault((J, pm), a)

    # ---- (T1) K disjoint codim-3 subcubes on the F side
    for K in (3, 4, 5):
        if 3 * K > N:
            continue
        seed = np.zeros(len(items), dtype=bool)
        ok = True
        for a in range(K):
            J = tuple(range(3 * a, 3 * a + 3))
            key = (J, 1 << 0)          # pattern {000} = all three coords +1
            if key not in idx_of:
                ok = False
                break
            seed[idx_of[key]] = True
        if not ok:
            pr(f"  (T1) K={K}: subcube not in universe (skipped)")
            continue
        U = union_mask(masks, seed)
        selP = disjoint_from(masks, U)
        pr(f"  (T1) F = {K} codim-3 subcubes on disjoint triples: "
           f"Ibar_F = {1/(2*K):.4f}; partners in universe = {int(selP.sum())}")
        if selP.any():
            tP = tau(inf[selP])
            pr(f"        tau(partner side) = {tP[0]:.6f}  "
               f"-> design value {max(1/(2*K), tP[0]):.6f}")

    # ---- (T2)/(T3) closure searches
    best = None
    trials = []
    # structured seed: the 3x3 grid columns (N>=9)
    if N >= 9:
        gseed = np.zeros(len(items), dtype=bool)
        good = True
        for j in range(3):
            J = tuple(sorted([j, 3 + j, 6 + j]))
            key = (J, 1 << 7)          # pattern {111} = all three coords -1
            if key in idx_of:
                gseed[idx_of[key]] = True
            else:
                good = False
        if good:
            trials.append(("3x3 grid columns", gseed))
    # random seeds of 1..4 placed sets
    for s in range(1, 5):
        for _ in range(14):
            sel = np.zeros(len(items), dtype=bool)
            sel[rng.choice(len(items), s, replace=False)] = True
            trials.append((f"random seed size {s}", sel))
    for tag, sel in trials:
        r = closure(masks, inf, sel)
        if r is None:
            continue
        v = r[0]
        if best is None or v < best[0]:
            best = (v, tag, r)
    if best is None:
        pr("  no evaluable design"); continue
    v, tag, r = best
    ubF = exact_cert(r[3][1], r[3][2]); ubG = exact_cert(r[4][1], r[4][2])
    pr(f"  best closure design: {v:.6f} from [{tag}]  "
       f"(|F|={int(r[1].sum())}, |G|={int(r[2].sum())})")
    pr(f"     exact certificates: tauF <= {ubF} = {float(ubF):.6f}, "
       f"tauG <= {ubG} = {float(ubG):.6f}")
    if max(ubF, ubG) < Fraction(1, 6):
        pr("     *** BELOW 1/6 -- CANDIDATE COUNTEREXAMPLE ***")
    # hill-climb on the seed of the best design
    cur, sel = v, best[2][2].copy()      # start from the G side of the best
    curseed = sel.copy()
    for step in range(40):
        cands = []
        pool_idx = np.flatnonzero(~curseed)
        for _ in range(8):
            trial = curseed.copy()
            if random.random() < 0.7 and pool_idx.size:
                trial[int(rng.choice(pool_idx))] = True
            else:
                on = np.flatnonzero(trial)
                if on.size > 1:
                    trial[int(rng.choice(on))] = False
            rr = closure(masks, inf, trial)
            if rr is not None:
                cands.append((rr[0], trial, rr))
        if not cands:
            break
        cands.sort(key=lambda z: z[0])
        if cands[0][0] < cur - 1e-12:
            cur, curseed, rbest = cands[0][0], cands[0][1], cands[0][2]
        else:
            break
    pr(f"  after hill-climb: {cur:.6f}   ({time.time()-t0:.0f}s)")
    results.append((N, v, cur))

hr("SUMMARY (upper bounds on eps*_ind(3,N) found inside the searched universe)")
for N, v, hc in results:
    pr(f"  N={N}: closure best {v:.6f}, after hill-climb {hc:.6f}   "
       f"(1/6 = {1/6:.6f})")
pr(f"DONE r4 in {time.time()-t0:.1f}s")
