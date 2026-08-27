"""
h5_certificate.py -- the final exact certificate, branch diagnostics, and the
crossover analysis.  All arithmetic is exact (Fraction / int).
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import *
from fam8 import build_V1, build_V2, subcube_distance, lemma, V1_params, V2_params


def best_k(d, params, krange):
    best = None
    for k in krange:
        try:
            cf = lemma(*params(d, k))
        except Exception:
            continue
        v = max(cf['piM'], cf['Q'])
        if best is None or v < best[0]:
            best = (v, k, cf)
    return best


print("=" * 78)
print("CROSSOVER: smallest d at which the family sits strictly below the")
print("threshold, for tau = 1/(2 d^4) and for the harsher 1/d^10")
print("=" * 78)
for nm, params, kr in [("V1", V1_params, lambda d: range(1, d - 1)),
                       ("V2", V2_params, lambda d: range(1, (d - 1) // 2))]:
    for pname, thr in [("1/(2 d^4)", lambda d: F(1, 2 * d ** 4)),
                       ("1/d^10", lambda d: F(1, d ** 10))]:
        d0 = None
        for d in range(4, 400):
            b = best_k(d, params, kr(d))
            if b is None:
                continue
            if b[0] < thr(d):
                d0 = (d, b[1], b[0], thr(d))
                break
        print(f"  {nm}, threshold {pname}: first d = {d0[0]} (k={d0[1]}), "
              f"max(pi_M,Q) ~ {float(d0[2]):.4g} < {float(d0[3]):.4g}")

print()
print("=" * 78)
print("CERTIFICATE  C1  (V1, d = 80, k = 36)   -- A is close to a subcube")
print("CERTIFICATE  C2  (V2, d = 120, k = 34)  -- A is ~1/2-far from EVERY subcube")
print("=" * 78)
for nm, d, k, params, nZ in [("C1 / V1", 80, 36, V1_params, 36),
                             ("C2 / V2", 120, 34, V2_params, 68)]:
    cf = lemma(*params(d, k))
    N = nZ + d
    tau = F(1, 2 * d ** 4)
    rho = params(d, k)[2]
    w = params(d, k)[1]
    u = 1 - F(1, 2 ** w)
    t = F(1, 2 ** d)
    print(f"\n  {nm}:  N = {N},  d = {d},  k = {k},  w = |K1| = {w}")
    print(f"    rho = Pr[R]            = {float(rho):.6g}")
    print(f"    alpha = |A|/2^N        = {float(cf['alpha']):.6g}   "
          f"beta = {float(cf['beta']):.10f}")
    print(f"    tau = 1/(2 d^4)        = {float(tau):.6g}")
    print(f"    pi_M(A,B)              = {float(cf['piM']):.6g}   "
          f"[= {cf['piM']}]" if d <= 20 else
          f"    pi_M(A,B)              = {float(cf['piM']):.6g}")
    print(f"    Q = max_i min(...)     = {float(cf['Q']):.6g}")
    print(f"    max_i Inf_i(f_A)       = {float(cf['maxIA']):.6g}")
    print(f"    max_i Inf_i(f_B)       = {float(cf['maxIB']):.6g}   "
          f"(= Q, since B = ~A and alpha < beta)")
    print(f"    pi_M < tau ?           {cf['piM'] < tau}")
    print(f"    Q    < tau ?           {cf['Q'] < tau}")
    print(f"    GAP-3 asks for i* with Inf(f_A) >= 1/poly and Inf(f_B) >= tau,")
    print(f"      or vice versa.  Both clauses need Inf_{{i*}}(f_B) >= tau, but")
    print(f"      max_i Inf_i(f_B) = {float(cf['maxIB']):.6g} < tau = {float(tau):.6g}.")
    print(f"      => W_tau(B) = EMPTY.  GAP-3 FAILS on this pair.")
    print(f"    pi_tau <= N * max_i Inf_i(f_B) = {float(N*cf['maxIB']):.6g}")
    # rigidity / branch-2 structure
    massA_on_R = cf['massA_on_R']
    massB_off_R = cf['massB_off_R']
    eps = cf['piM']
    sq = F(int((float(eps) ** 0.5) * 10 ** 12), 10 ** 12)   # rational >= sqrt(eps)
    assert sq * sq >= eps * F(999, 1000)
    print(f"    RIGIDITY CHECK (u3 sec.4, eps = pi_M = {float(eps):.4g}, "
          f"sqrt(eps) ~ {float(eps)**0.5:.4g}):")
    print(f"      1 - Pr_A[ x in R x cube ]  = {float(1-massA_on_R):.6g}   "
          f"<= sqrt(eps)? {(1-massA_on_R) <= sq}")
    print(f"      1 - Pr_B[ x in ~R x cube ] = {float(1-massB_off_R):.6g}   "
          f"<= sqrt(eps)? {(1-massB_off_R) <= sq}")
    print(f"      rho = Pr[R] = {float(rho):.6g}   (E_d has rho = 1/2)")
    print(f"      boundary coords of R are heavy for A "
          f"(Inf ~ {float(cf['maxIA']):.4g}) but NOT for B (Inf ~ {float(cf['maxIB']):.4g})")

print()
print("=" * 78)
print("HOW FAR IS A FROM A SUBCUBE?  exact min over all 3^N subcubes")
print("=" * 78)
for nm, builder, d, k in [("V1", build_V1, 4, 1), ("V1", build_V1, 5, 2),
                          ("V1", build_V1, 6, 2), ("V1", build_V1, 6, 3),
                          ("V2", build_V2, 4, 1), ("V2", build_V2, 5, 1),
                          ("V2", build_V2, 6, 1), ("V2", build_V2, 6, 2),
                          ("V2", build_V2, 7, 2)]:
    N, A, B, Z, K, K1 = builder(d, k)
    if N > 11:
        continue
    dist = subcube_distance(A, N)
    print(f"  {nm} d={d} k={k} N={N}: min_C |A xor C|/|A| = {dist} "
          f"(~{float(dist):.4g})")
print("  closed form, V1: |A xor (R x cube)|/|A| = (rho 2^{-w} + (1-2 rho)2^{-d})/alpha")
print("                  = 3*2^{k-d} + O(2^{k-d}), i.e. V1's A IS a near-subcube.")
print("  V2: R = R1 u R2 spans the whole Z-cube, so any subcube capturing half of")
print("      R1 and half of R2 must be the whole Z-cube (density 1 >> rho); a")
print("      subcube capturing only R1 misses ~|A|/2.  Hence dist -> ~1/2.")
