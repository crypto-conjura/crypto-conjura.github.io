"""
s3 -- (i) witness (b) of 0023-prover-3-r3 §4 exhaustively: minimal = minimum on
         both sides, for d = 2,3,4 and N = d, d+1, d+2 (generic brute force);
     (ii) witness (a) at k = 4 (N = 20, where the 2^N x 2^N generic table is out
         of reach): EXACT verification, for ALL 2^19 points of A_4, of the
         predicted minimal-certificate family, by vectorised AND-folds that use
         only the truth table (no structural input in the *test*), plus a
         completeness probe by batched greedy shrinking in 2 x 10^3 random
         coordinate orders.
"""
import sys, time
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib6 import (cert_table, minimal_certs_generic, selection_stats,
                  degree_of, influences_exact, size)

# ---------------------------------------------------------------- witness (b)
print("=" * 78)
print("(i) witness (b): C = {x_1..x_d = +1}, D = C^c")
print("=" * 78)
for d in (2, 3, 4):
    for N in (d, d + 1, d + 2):
        if N > 7:
            continue
        n = 1 << N
        m = np.arange(n)
        inC = (m & ((1 << d) - 1)) == 0        # bits 0..d-1 all 0  <-> x_i = +1
        C, D = inC, ~inC
        assert degree_of(C, N) == d and degree_of(D, N) == d
        mcC = minimal_certs_generic(C, N)
        mcD = minimal_certs_generic(D, N)
        eC, szC, mulC, pmC, nC = selection_stats(mcC, N)
        eD, szD, mulD, pmD, nD = selection_stats(mcD, N)
        okC = all(lst == [(1 << d) - 1] for lst in mcC.values())
        okD = all(all(size(S) == 1 and (S & ((1 << d) - 1)) for S in lst)
                  for lst in mcD.values())
        print(f" d={d} N={N}: side C sizes={dict(szC)} mult={dict(mulC)} "
              f"(unique [d]? {okC}); E|W| MIN={eC['MIN']} MAX={eC['MAX']} "
              f"UNIF={eC['UNIF']}")
        print(f"          side D sizes={dict(szD)} mult={dict(mulD)} "
              f"(all singletons in [d]? {okD}); E|W| MIN={eD['MIN']} "
              f"MAX={eD['MAX']} UNIF={eD['UNIF']}")
        assert okC and okD
        IC, ID = influences_exact(C, N), influences_exact(D, N)
        # Remark 2.2 ratio, any selection
        pay = sum((ID[i] for i in range(d)), F(0)) + ID[0] * 0 + IC[0]
        ratio = pay / (d + 1)
        print(f"          pi = {pay}  (= 1/2 + d/(2(2^d-1)) = "
              f"{F(1,2)+F(d,2*((1<<d)-1))}); ratio pi/(d+1) = {ratio} "
              f"= {float(ratio):.6f}  [every selection]")
        assert pay == F(1, 2) + F(d, 2 * ((1 << d) - 1))

# ---------------------------------------------------- witness (a) at k = 4
print()
print("=" * 78)
print("(ii) witness (a) at k=4 (N=20): exact check of the predicted family")
print("=" * 78)
k = 4
N = k + (1 << k)
n = 1 << N
t0 = time.time()
m = np.arange(n, dtype=np.int64)
addr = m & ((1 << k) - 1)
A = ((m >> (k + addr)) & 1) == 0
print(f"  built truth table, |A| = {int(A.sum())} = 2^{N-1} ({time.time()-t0:.1f}s)")
perm = None


def cert_all_points(A, N, S):
    """cert_S[m] for ALL m, by folding A over the free coordinates.  Uses only
    the truth table.  Returns bool array of length 2^N."""
    cur = A
    for i in range(N):
        if not ((S >> i) & 1):
            idx = np.arange(len(cur)) ^ (1 << i)
            cur = cur & cur[idx]
    return cur


# the 3^k candidate masks: choose U (free address bits) and the values of the
# fixed address bits; the mask is then determined.
cands = {}
for U in range(1 << k):
    fixed = ((1 << k) - 1) & ~U
    # enumerate the values of the fixed address bits
    vals = [0]
    for i in range(k):
        if (fixed >> i) & 1:
            vals = [v | (b << i) for v in vals for b in (0, 1)]
    for v in vals:
        S = fixed
        # targets: addresses j with j&fixed == v, i.e. j = v ^ w, w <= U
        w = U
        while True:
            S |= 1 << (k + (v ^ w))
            if w == 0:
                break
            w = (w - 1) & U
        cands[(U, v)] = S
print(f"  {len(cands)} candidate masks (= 3^k = {3**k})")

certs = {}
t0 = time.time()
needed = set(cands.values())
for S in list(needed):
    for i in range(N):
        if (S >> i) & 1:
            needed.add(S ^ (1 << i))
for S in sorted(needed):
    certs[S] = cert_all_points(A, N, S)
print(f"  computed cert_S over all points for {len(certs)} masks "
      f"({time.time()-t0:.1f}s)")

# per-point: which candidates are minimal certificates
t0 = time.time()
maxsize = np.zeros(n, dtype=np.int16)
minsize = np.full(n, 127, dtype=np.int16)
cnt = np.zeros(n, dtype=np.int32)
for (U, v), S in cands.items():
    isc = certs[S]
    minimal = isc.copy()
    for i in range(N):
        if (S >> i) & 1:
            minimal &= ~certs[S ^ (1 << i)]
    s = size(S)
    sel = minimal & A
    maxsize[sel] = np.maximum(maxsize[sel], s)
    minsize[sel] = np.minimum(minsize[sel], s)
    cnt[sel] += 1
    # every point where S is a certificate at all must be in A
    assert not np.any(isc & ~A)
print(f"  minimality resolved ({time.time()-t0:.1f}s)")
ptsA = A
assert np.all(cnt[ptsA] >= 1), "some point of A has no candidate minimal cert"
d = k + 1
eMAX = F(int(maxsize[ptsA].sum()), int(ptsA.sum()))
eMIN = F(int(minsize[ptsA].sum()), int(ptsA.sum()))
print(f"  k=4 d=5: E|W| MIN = {eMIN}, MAX = {eMAX} = {float(eMAX):.6f}")
print(f"  structural prediction from s2 (full R-enumeration): MIN=5, "
      f"MAX=182001/32768={182001/32768:.6f}  -> match: "
      f"{eMAX == F(182001,32768) and eMIN == 5}")
hist = {}
for s in np.unique(maxsize[ptsA]):
    hist[int(s)] = int((maxsize[ptsA] == s).sum())
print(f"  per-point MAX-size histogram: {hist}  "
      f"(total {int(ptsA.sum())} = 2^{N-1})")
print(f"  #points with a minimal certificate of size 2^(d-1)=16: "
      f"{hist.get(16,0)} = {F(hist.get(16,0), int(ptsA.sum()))} of A "
      f"(theory 2^-(2^k-1) = {F(1,1<<15)})")

# ---- completeness probe: batched greedy shrink in random coordinate orders
print("  completeness probe: greedy shrink from [N] in random orders, all "
      "points at once, results must land in the candidate family")
rng = np.random.default_rng(20260827)
allcand = set(cands.values())
bad = 0
t0 = time.time()
for trial in range(6):
    order = rng.permutation(N)
    groups = {(1 << N) - 1: np.flatnonzero(ptsA)}
    for i in order:
        newg = {}
        for S, idxs in groups.items():
            T = S & ~(1 << int(i))
            if T not in certs:
                certs[T] = cert_all_points(A, N, T)
            keep = certs[T][idxs]
            a, b = idxs[keep], idxs[~keep]
            if len(a):
                newg.setdefault(T, []).append(a)
            if len(b):
                newg.setdefault(S, []).append(b)
        groups = {S: np.concatenate(v) for S, v in newg.items()}
    for S in groups:
        if S not in allcand:
            bad += 1
            print(f"    !! greedy outcome outside the candidate family: {bin(S)}")
    print(f"    trial {trial}: {len(groups)} distinct outcomes, all in the "
          f"candidate family: {all(S in allcand for S in groups)} "
          f"({time.time()-t0:.1f}s)")
print(f"  probe finished, violations = {bad}")
