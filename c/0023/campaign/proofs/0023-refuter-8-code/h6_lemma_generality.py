"""
h6_lemma_generality.py -- the Deformation Lemma is checked for EVERY base set R
on a 3-coordinate and a 4-coordinate block, not just the two named instances.

Space covered: ALL 2^8 - 1 = 255 nonempty R subseteq {+-1}^3, and a uniform
random sample of 400 nonempty R subseteq {+-1}^4, crossed with every (d, w) with
deg(1_R) + w <= d - 1 and N = |Z| + d <= 12.  For each, A = (R x U) u (cube x T)
is built explicitly and its alpha, all influences (by BOTH the boundary route
and the integer Walsh-Hadamard route), degree, and the full list of
maximum-degree supports are compared against the Lemma's closed form.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import *
from fam8 import lemma


def build_general(nZ, R, d, w):
    """R is a bitmask over the 2^nZ points of {+-1}^Z."""
    N = nZ + d
    mZ = (1 << nZ) - 1
    mK = ((1 << d) - 1) << nZ
    mK1 = ((1 << w) - 1) << nZ

    def pred(m):
        z = m & mZ
        return (((R >> z) & 1) and ((m & mK1) != 0)) or ((m & mK) == 0)
    A = from_pred(N, pred)
    return N, A, complement(A, N)


total = ok = skipped = 0
import random
random.seed(20260828)
for nZ, Rs in ((3, list(range(1, 1 << 8))),
               (4, random.sample(range(1, 1 << 16), 400))):
    for R in Rs:
        cR = spectrum(R, nZ)
        dR, _ = degree_and_tops(R, nZ, cR)
        rho = F(popcount(R), 1 << nZ)
        infR = inf_boundary(R, nZ)                    # Inf_i(f_R)
        infR1 = [x * rho for x in infR]               # Inf_i(1_R)
        assert infR1 == [F(b, 2 * (1 << nZ)) for b in bcounts(R, nZ)]
        for d in range(2, 13 - nZ):
            for w in range(1, d - dR):
                N = nZ + d
                if N > 12:
                    continue
                Ncells = 1 << N
                if Ncells > 4096:
                    continue
                total += 1
                N, A, B = build_general(nZ, R, d, w)
                r = card(A, B, N, label="")
                cf = lemma(d, w, rho, infR1, nZ)
                good = (r['alpha'] == cf['alpha']
                        and r['Q'] == cf['Q']
                        and r['piM_min'] == r['piM_max'] == cf['piM']
                        and r['maxIA'] == cf['maxIA'] and r['maxIB'] == cf['maxIB']
                        and r['degA'] == d and r['degB'] == d
                        and r['ntopA'] == 1 and r['ntopB'] == 1
                        and set(r['topA'][0]) == set(range(nZ, nZ + d)))
                if good:
                    ok += 1
                else:
                    print(f"  MISMATCH nZ={nZ} R={R} d={d} w={w}: "
                          f"brute {r['alpha']},{r['Q']},{r['piM_min']},"
                          f"deg={r['degA']},ntop={r['ntopA']},top={r['topA'][:2]} "
                          f"vs lemma {cf['alpha']},{cf['Q']},{cf['piM']}")
                    if total - ok > 12:
                        raise SystemExit("too many mismatches")
    print(f"  nZ = {nZ} done: {ok}/{total} instances match the Lemma exactly")

print()
print(f"TOTAL: {ok}/{total} instances of the Deformation Lemma verified exactly")
print("       (each by TWO independent influence routes -- boundary and integer")
print("        Walsh-Hadamard -- which lib8.card asserts agree, plus the")
print("        hand-derived closed form).")
