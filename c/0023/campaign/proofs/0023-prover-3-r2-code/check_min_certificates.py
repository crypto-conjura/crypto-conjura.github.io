"""Exhaustive check of the U4 repair in 0023-prover-3-r2 §7.4, witness (a).

For k = 1, 2, 3 (d = k+1, N = k + 2^k) this enumerates, over the WHOLE cube and
in exact rational arithmetic:
  * every minimum-size certificate of every point of A_k and of B_k = A_k^c
    (not just one per point, which is what 0023-prover-3-code/check_witnesses.py
    computed and why the earlier "unique minimum certificate" claim went
    unnoticed);
  * their sizes (all = d) and their per-point multiplicities (1 .. k+1);
  * the MINIMUM over all points and all selections on both sides of
    pi_W / (|T_A| + |T_B|), against the hand formula
    [(k-1)/2 + 2^{1-k}] / (2(k+1))  (the u = 1 selection, the worst), and
  * the MAXIMUM, against the declared u = 0 selection's (k/2 + 2^{-k})/(2(k+1)).

Output (verified 2026-08-27):
  k=1 d=2: sizes={2}, mult=[1,2],     worst=1/4  (hand 1/4),  best=1/4
  k=2 d=3: sizes={3}, mult=[1,2,3],   worst=1/6  (hand 1/6),  best=5/24
  k=3 d=4: sizes={4}, mult=[1,2,3,4], worst=5/32 (hand 5/32), best=13/64
Runtime ~4 min for k<=3 (k=3 is 2^11 points x all certificate subsets).
"""
from fractions import Fraction as F
from itertools import combinations

def wht(v):
    v = v[:]; n = len(v); h = 1
    while h < n:
        for i in range(0, n, h*2):
            for j in range(i, i+h):
                x, y = v[j], v[j+h]
                v[j], v[j+h] = x+y, x-y
        h *= 2
    return v

class BS:
    def __init__(self, N, member):
        self.N = N
        self.tt = [1 if member(m) else 0 for m in range(1 << N)]
        g = wht(self.tt[:])
        self.g = [F(c, 1 << N) for c in g]
        self.alpha = F(sum(self.tt), 1 << N)
        self.deg = max(bin(S).count("1") for S, c in enumerate(self.g) if c)
        acc = [F(0)]*N
        for S, c in enumerate(self.g):
            if c:
                for i in range(N):
                    if (S >> i) & 1: acc[i] += c*c
        self.I = [a/self.alpha for a in acc]
        self.R = {i for i in range(N) if acc[i]}

    def all_min_certs(self, m):
        val = self.tt[m]
        Rs = sorted(self.R)
        for size in range(self.N+1):
            out = []
            for T in combinations(Rs, size):
                mk = 0
                for i in T: mk |= 1 << i
                if all(self.tt[y] == val for y in range(1 << self.N) if (y & mk) == (m & mk)):
                    out.append(set(T))
            if out: return out
        raise AssertionError

def piW(A, B, WA, WB):
    return sum((A.I[i] for i in WB), F(0)) + sum((B.I[i] for i in WA), F(0))

for k in (1, 2, 3):
    N = k + (1 << k); d = k+1
    def addr(m, k=k):
        j = 0
        for t in range(k): j = 2*j + ((m >> t) & 1)
        return j
    A = BS(N, lambda m: ((m >> (k+addr(m))) & 1) == 0)
    B = BS(N, lambda m: ((m >> (k+addr(m))) & 1) == 1)
    assert A.deg == d == B.deg
    ptsA = [m for m in range(1 << N) if A.tt[m]]
    ptsB = [m for m in range(1 << N) if B.tt[m]]
    certA = {m: A.all_min_certs(m) for m in ptsA}
    certB = {m: B.all_min_certs(m) for m in ptsB}
    sizes = {len(c) for cs in certA.values() for c in cs} | {len(c) for cs in certB.values() for c in cs}
    mult = sorted({len(cs) for cs in certA.values()} | {len(cs) for cs in certB.values()})
    worst = None; best = None
    for ma in ptsA:
        for ca in certA[ma]:
            for mb in ptsB:
                for cb in certB[mb]:
                    r = piW(A, B, ca, cb)/(len(ca)+len(cb))
                    if worst is None or r < worst: worst = r
                    if best is None or r > best: best = r
    hand = (F(k-1, 2) + F(1, 1 << (k-1)))/(2*(k+1))
    hand0 = (F(k, 2) + F(1, 1 << k))/(2*(k+1))
    print(f"k={k} d={d}: min-cert sizes={sizes} (d={d}), multiplicities={mult}, "
          f"worst ratio={worst} (hand {hand}), best ratio={best} (u=0 hand {hand0})")
