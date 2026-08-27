"""
r6_n9_dense.py -- design search at N = 9 (the dimension of the 1/6 witness)
over a DENSE universe:
   * every degree-<=3 pattern with window <= 4, on every window (COMPLETE),
   * a sample of window-5 and window-6 patterns (lowest total influence plus
     random, including all cheap window-6 orbit representatives).
Seeds for the closure operator are taken up to the hyperoctahedral symmetry of
the window (complete for windows <= 4), plus the 3x3 grid, plus random
multi-set seeds.

For every seed H the closure
   F = {u : u cap (union H) = empty},  G = {u : u cap (union F) = empty}
is a genuine cross-disjoint pair inside the universe, so max(tau F, tau G) is a
valid UPPER bound for eps*_ind(3,9) restricted to the universe.  Any value below
1/6 would be a counterexample; each reported optimum carries an exact rational
certificate.
"""
import sys, time, random, itertools
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import level3_all, next_level, bvec, popcnt

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)
rng = np.random.default_rng(24680)
random.seed(24680)
N = 9
W = ((1 << N) + 63) // 64

# ------------------------------------------------------------- patterns
L = {3: level3_all()}
L[4] = next_level(L[3], 3)
L[5] = next_level(L[4], 4)
def genuine_list(masks, w):
    B = bvec(masks, w); n = popcnt(masks)
    keep = np.all(B > 0, axis=1) & (n > 0) & (n < (1 << w))
    j = np.flatnonzero(keep)
    return [(int(masks[a]), B[a].tolist(), int(n[a])) for a in j]
PAT = {}
for w in (1, 2, 3):
    PAT[w] = genuine_list(np.arange(1 << (1 << w), dtype=np.uint64), w)
PAT[4] = genuine_list(L[4], 4)
p5 = genuine_list(L[5], 5)
p5.sort(key=lambda z: sum(z[1]) / (2 * z[2]))
PAT[5] = p5[:2000] + random.sample(p5[2000:], 1000)
L6 = np.load("L6.npy"); B6 = np.load("L6_b.npy").astype(np.int32); N6 = np.load("L6_n.npy").astype(np.int32)
g6 = np.all(B6 > 0, axis=1)
T6 = B6.sum(axis=1) / (2.0 * np.maximum(N6, 1))
cheap6 = g6 & np.all(B6 * 3 < N6[:, None], axis=1)
mn6 = np.minimum(N6, 64 - N6)
phi6 = g6 & (B6.max(axis=1) * 16 == 6 * mn6)
sel6 = np.unique(np.concatenate([
    np.flatnonzero(cheap6)[:300], np.flatnonzero(phi6)[:300],
    np.flatnonzero(g6)[np.argsort(T6[g6])[:600]],
    rng.choice(np.flatnonzero(g6), 400, replace=False)]))
PAT[6] = [(int(L6[a]), B6[a].tolist(), int(N6[a])) for a in sel6]
del L6, B6, N6
for w in sorted(PAT):
    pr(f"  window {w}: {len(PAT[w])} patterns")

# ------------------------------------------------------------- universe
pr("building universe ...")
allmask, allinf, meta = [], [], []
pts = np.arange(1 << N, dtype=np.int64)
for w in sorted(PAT):
    pats = PAT[w]
    pm = np.array([p[0] for p in pats], dtype=np.uint64)
    bb = np.array([p[1] for p in pats], dtype=np.int32)
    nn = np.array([p[2] for p in pats], dtype=np.int32)
    for J in itertools.combinations(range(N), w):
        proj = np.zeros(1 << N, dtype=np.int64)
        for i, c in enumerate(J):
            proj |= ((pts >> c) & 1) << i
        blk = np.zeros((1 << w, W), dtype=np.uint64)
        for m in range(1 << w):
            xs = pts[proj == m]
            for x in xs:
                blk[m, x >> 6] |= np.uint64(1) << np.uint64(int(x) & 63)
        M = np.zeros((len(pats), W), dtype=np.uint64)
        for m in range(1 << w):
            has = ((pm >> np.uint64(m)) & np.uint64(1)).astype(bool)
            if has.any():
                M[has] |= blk[m]
        I = np.zeros((len(pats), N), dtype=np.float64)
        for i, c in enumerate(J):
            I[:, c] = bb[:, i] / (2.0 * nn)
        allmask.append(M); allinf.append(I)
        meta.append((J, len(pats)))
masks = np.concatenate(allmask); inf = np.concatenate(allinf)
del allmask, allinf
U = len(masks)
pr(f"  universe: {U} placed sets, {masks.nbytes/2**20:.0f} MiB "
   f"({time.time()-t0:.0f}s)")

from scipy.optimize import linprog
def tau(rows):
    A = np.unique(rows, axis=0)
    m = len(A)
    Aub = np.concatenate([A.T, -np.ones((N, 1))], axis=1)
    c = np.zeros(m + 1); c[m] = 1.0
    Aeq = np.zeros((1, m + 1)); Aeq[0, :m] = 1.0
    r = linprog(c, A_ub=Aub, b_ub=np.zeros(N), A_eq=Aeq, b_eq=[1.0],
                bounds=[(0, None)] * m + [(None, None)], method="highs")
    return (r.x[m], A, r.x[:m]) if r.success else (None, A, None)

def closure(seedsel):
    Um = np.bitwise_or.reduce(masks[seedsel], axis=0)
    selF = ~np.any(masks & Um, axis=1)
    if not selF.any():
        return None
    UF = np.bitwise_or.reduce(masks[selF], axis=0)
    selG = ~np.any(masks & UF, axis=1)
    if not selG.any():
        return None
    tF, tG = tau(inf[selF]), tau(inf[selG])
    if tF[0] is None or tG[0] is None:
        return None
    return max(tF[0], tG[0]), selF, selG, tF, tG

def exact_cert(A, p, maxden=10**6):
    q = [Fraction(float(x)).limit_denominator(maxden) for x in p]
    s = sum(q)
    q = [x / s for x in q]
    acc = [Fraction(0)] * N
    for wq, row in zip(q, A):
        if wq == 0:
            continue
        for i in range(N):
            if row[i]:
                acc[i] += wq * Fraction(float(row[i])).limit_denominator(10**6)
    return max(acc)

# --------------------------------------------------- seeds up to symmetry
def canon(pmask, w):
    """canonical form of a pattern under the hyperoctahedral group of the
    window (coordinate permutations + sign flips)."""
    best = None
    for perm in itertools.permutations(range(w)):
        for fl in range(1 << w):
            img = 0
            for m in range(1 << w):
                mm = m ^ fl
                t = 0
                for b in range(w):
                    if (mm >> b) & 1:
                        t |= 1 << perm[b]
                if (pmask >> m) & 1:
                    img |= 1 << t
            if best is None or img < best:
                best = img
    return best

hr("closure search at N = 9")
seedidx = []
off = 0
reps_per_w = {}
for (J, cnt) in meta:
    w = len(J)
    if J == tuple(range(w)) and w <= 4:            # one canonical window
        seen = {}
        for a, p in enumerate(PAT[w]):
            c = canon(p[0], w)
            if c not in seen:
                seen[c] = off + a
        reps_per_w[w] = list(seen.values())
        seedidx.extend(seen.values())
    off += cnt
pr(f"  single-set seeds up to symmetry (windows <= 4, COMPLETE): "
   f"{ {w: len(v) for w, v in reps_per_w.items()} }  total {len(seedidx)}")

best = None
def try_seed(tag, sel):
    global best
    r = closure(sel)
    if r is None:
        return None
    if best is None or r[0] < best[0] - 1e-12:
        best = (r[0], tag, r)
    return r[0]

vals = []
for a in seedidx:
    sel = np.zeros(U, dtype=bool); sel[a] = True
    v = try_seed(f"single set #{a}", sel)
    if v is not None:
        vals.append((v, a))
vals.sort()
pr(f"  best single-set closures: {[f'{v:.5f}' for v, _ in vals[:8]]}")
pr(f"  ({time.time()-t0:.0f}s)")

# the 3x3 grid seed
gsel = np.zeros(U, dtype=bool)
off = 0
found = 0
for (J, cnt) in meta:
    if len(J) == 3:
        for a, p in enumerate(PAT[3]):
            if p[0] == (1 << 7) and J in [(0, 3, 6), (1, 4, 7), (2, 5, 8)]:
                gsel[off + a] = True; found += 1
    off += cnt
pr(f"  grid seed sets found: {found}")
if found == 3:
    pr(f"  grid closure value: {try_seed('3x3 grid', gsel):.6f}")

# random multi-set seeds, and seeds built from the best single seeds
for size in (2, 3, 4):
    for _ in range(40):
        sel = np.zeros(U, dtype=bool)
        pick = [a for _, a in vals[:40]] if vals else list(range(U))
        sel[rng.choice(pick, min(size, len(pick)), replace=False)] = True
        try_seed(f"multi-seed size {size}", sel)
pr(f"  after multi-set seeds: best = {best[0]:.6f}  ({time.time()-t0:.0f}s)")

# hill-climb on the best seed's G side
cur, sel = best[0], best[2][2].copy()
for step in range(30):
    improved = False
    for _ in range(10):
        trial = sel.copy()
        if random.random() < 0.7:
            trial[int(rng.integers(0, U))] = True
        else:
            on = np.flatnonzero(trial)
            if on.size > 1:
                trial[int(rng.choice(on))] = False
        r = closure(trial)
        if r is not None and r[0] < cur - 1e-12:
            cur, sel, best = r[0], trial, (r[0], "hill-climb", r)
            improved = True
            break
    if not improved:
        break
pr(f"  after hill-climb: {cur:.6f}")

v, tag, r = best
ubF = exact_cert(r[3][1], r[3][2]); ubG = exact_cert(r[4][1], r[4][2])
hr("RESULT")
pr(f"  best design at N=9 inside this universe: {v:.6f} from [{tag}]")
pr(f"  |F| = {int(r[1].sum())}, |G| = {int(r[2].sum())}")
pr(f"  exact certificates: tau_F <= {ubF} ({float(ubF):.6f}), "
   f"tau_G <= {ubG} ({float(ubG):.6f})")
pr(f"  1/6 = {Fraction(1,6)} = {1/6:.6f};  below 1/6 ? "
   f"{max(ubF, ubG) < Fraction(1,6)}")
pr(f"DONE r6 in {time.time()-t0:.1f}s")
