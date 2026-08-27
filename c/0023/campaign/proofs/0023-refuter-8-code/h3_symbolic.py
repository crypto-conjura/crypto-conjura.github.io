"""
h3_symbolic.py -- closed forms for the deformation family, valid for ALL d,
checked against exhaustive exact brute force at every (d,k) that fits.

DEFORMATION LEMMA (proved in the report, verified here).
Let Z, K be disjoint coordinate blocks with |K| = d.  Let R subseteq {+-1}^Z be
any nonempty set of density rho with deg(1_R) = dR.  Pick 1 <= w <= d-1-dR, a
subset K1 subseteq K with |K1| = w, and set

    U = { x_K : x_{K1} != (+1)^w },   T = { x_K = (+1)^d },
    A = (R x U)  u  ({+-1}^Z x T),    B = complement(A).

Then, with t = 2^{-d}, u = 1 - 2^{-w}:

  (i)   deg 1_A = deg 1_B = d and x_K is the UNIQUE maximum-degree monomial,
        so M(A) = M(B) = K is forced (no choice of supports is available).
  (ii)  alpha = rho*u + t,  beta = 1 - alpha.
  (iii) Inf_i(1_A) = u * Inf_i(1_R)                       for i in Z
        Inf_i(1_A) = rho*2^{-w-1} + (1-2rho)*2^{-d-1}     for i in K1
        Inf_i(1_A) = 2^{-d-1}                             for i in K \\ K1
  (iv)  Inf_i(f_A) = Inf_i(1_A)/alpha, Inf_i(f_B) = Inf_i(1_A)/beta  (B = ~A),
        so Q = max_i Inf_i(1_A) / max(alpha,beta)  and
        pi_M = (sum_{i in K} Inf_i(1_A)) * (1/alpha + 1/beta).

INSTANCES
  V1: R = codim-k subcube  (dR = k, rho = 2^{-k}, Inf_i(1_R) = 2^{-k-1}),
      w = d-k-1.                                A is 3*2^{k-d}-close to a subcube.
  V2: R = R1 u R2, R1 = {x_{Z1}=+1}, R2 = {x_{Z2}=+1} on disjoint blocks of
      size k  (dR = 2k, rho = 2^{1-k}-2^{-2k},
      Inf_i(1_R) = 2^{-k-1}(1-2^{-k}) for i in Z1 u Z2),  w = d-2k-1.
      A is at relative distance ~1/2 from EVERY subcube.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import *
from fam8 import build_V1, build_V2, lemma, V1_params, V2_params


def _dup_lemma(d, w, rho, infR, nZ):
    """(iii)+(iv). infR = list of Inf_i(1_R), i in Z (length nZ)."""
    t = F(1, 2 ** d)
    u = 1 - F(1, 2 ** w)
    alpha = rho * u + t
    beta = 1 - alpha
    iZ = [u * x for x in infR]
    iK1 = rho * F(1, 2 ** (w + 1)) + (1 - 2 * rho) * F(1, 2 ** (d + 1))
    iK0 = F(1, 2 ** (d + 1))
    sumK = w * iK1 + (d - w) * iK0
    mx = max(max(iZ), iK1, iK0)
    Q = mx / max(alpha, beta)
    piM = sumK * (1 / alpha + 1 / beta)
    return dict(alpha=alpha, beta=beta, Q=Q, piM=piM,
                maxIA=mx / alpha, maxIB=mx / beta,
                iZ=iZ[0], iK1=iK1, iK0=iK0)


def _dup_V1_params(d, k):
    return d, d - k - 1, F(1, 2 ** k), [F(1, 2 ** (k + 1))] * k, k


def _dup_V2_params(d, k):
    rho = F(2, 2 ** k) - F(1, 4 ** k)
    return d, d - 2 * k - 1, rho, [F(1, 2 ** (k + 1)) * (1 - F(1, 2 ** k))] * (2 * k), 2 * k


print("=" * 78)
print("STEP 1 -- closed forms vs exhaustive exact brute force")
print("=" * 78)
nchk = 0
for name, builder, params, rng in [
        ("V1", build_V1, V1_params, [(d, k) for d in range(4, 10) for k in range(1, d - 1)]),
        ("V2", build_V2, V2_params, [(d, k) for d in range(4, 10) for k in range(1, (d - 1) // 2)])]:
    for (d, k) in rng:
        N, A, B, Z, K, K1 = builder(d, k)
        if N > 12:
            continue
        r = card(A, B, N, label="")
        cf = lemma(*params(d, k))
        ok = (r['alpha'] == cf['alpha'] and r['Q'] == cf['Q']
              and r['piM_min'] == r['piM_max'] == cf['piM']
              and r['maxIA'] == cf['maxIA'] and r['maxIB'] == cf['maxIB']
              and r['ntopA'] == 1 and r['ntopB'] == 1
              and set(r['topA'][0]) == set(K))
        print(f"  {name} d={d} k={k} N={N}: closed form == brute force, "
              f"unique M = K : {ok}")
        assert ok, (name, d, k, r, cf)
        nchk += 1
print(f"  ({nchk} instances checked, all exact)")

print()
print("=" * 78)
print("STEP 2 -- the family at d in the regime that matters (exact rationals)")
print("=" * 78)
print("V1, k = round(d/2):     tau = 1/(2 d^4)")
print(f"{'d':>4} {'k':>3} | {'alpha':>12} | {'Q':>13} | {'pi_M':>13} | "
      f"{'tau':>13} | {'Q<tau':>6} | {'piM<tau':>7} | {'maxInf(f_B)':>12}")
for d in [17, 20, 24, 30, 40, 46, 50, 60, 80, 100, 150, 200]:
    k = round(d / 2)
    cf = lemma(*V1_params(d, k))
    tau = F(1, 2 * d ** 4)
    print(f"{d:>4} {k:>3} | {float(cf['alpha']):>12.4g} | {float(cf['Q']):>13.6g} | "
          f"{float(cf['piM']):>13.6g} | {float(tau):>13.6g} | "
          f"{str(cf['Q'] < tau):>6} | {str(cf['piM'] < tau):>7} | "
          f"{float(cf['maxIB']):>12.6g}")

print()
print("V2 (non-subcube base), k = round(d/3):")
print(f"{'d':>4} {'k':>3} | {'alpha':>12} | {'Q':>13} | {'pi_M':>13} | "
      f"{'tau':>13} | {'Q<tau':>6} | {'piM<tau':>7} | {'maxInf(f_B)':>12}")
for d in [17, 20, 24, 30, 40, 50, 60, 80, 100, 150, 200]:
    k = round(d / 3)
    if d - 2 * k - 1 < 1:
        continue
    cf = lemma(*V2_params(d, k))
    tau = F(1, 2 * d ** 4)
    print(f"{d:>4} {k:>3} | {float(cf['alpha']):>12.4g} | {float(cf['Q']):>13.6g} | "
          f"{float(cf['piM']):>13.6g} | {float(tau):>13.6g} | "
          f"{str(cf['Q'] < tau):>6} | {str(cf['piM'] < tau):>7} | "
          f"{float(cf['maxIB']):>12.6g}")

print()
print("=" * 78)
print("STEP 3 -- the trade-off is a hyperbola:  pi_M * Q  is d-only")
print("=" * 78)
print("V1: for every k, pi_M * Q =: P(d,k).  max_k min over the branch is at k~d/2.")
print(f"{'d':>4} | {'min_k max(piM,Q)':>18} | {'argmin k':>8} | "
      f"{'2^{-d/2}':>11} | {'piM*Q at k*':>13}")
for d in [17, 24, 30, 40, 50, 60, 80, 100]:
    best, bk = None, None
    for k in range(1, d - 1):
        cf = lemma(*V1_params(d, k))
        v = max(cf['piM'], cf['Q'])
        if best is None or v < best:
            best, bk, bcf = v, k, cf
    print(f"{d:>4} | {float(best):>18.6g} | {bk:>8} | {2.0**(-d/2):>11.4g} | "
          f"{float(bcf['piM'] * bcf['Q']):>13.6g}")

print()
print("=" * 78)
print("STEP 4 -- exact certificate at d = 60, k = 30 (V1) and d = 60, k = 20 (V2)")
print("=" * 78)
for nm, par in [("V1 d=60 k=30", V1_params(60, 30)), ("V2 d=60 k=20", V2_params(60, 20))]:
    cf = lemma(*par)
    tau = F(1, 2 * 60 ** 4)
    print(f"  {nm}:  N = {par[4] + 60}")
    print(f"    alpha = {cf['alpha']}")
    print(f"    Q     = {cf['Q']}")
    print(f"          ~ {float(cf['Q']):.6g}      tau = 1/(2*60^4) ~ {float(tau):.6g}")
    print(f"    pi_M  = {cf['piM']}")
    print(f"          ~ {float(cf['piM']):.6g}")
    print(f"    max_i Inf_i(f_A) ~ {float(cf['maxIA']):.6g}  "
          f"max_i Inf_i(f_B) ~ {float(cf['maxIB']):.6g}")
    print(f"    Q < tau ? {cf['Q'] < tau};  pi_M < tau ? {cf['piM'] < tau};  "
          f"max Inf(f_B) < tau ? {cf['maxIB'] < tau}")
    print(f"    => W_tau(B) = empty, so pi_tau = sum_{{i in W_tau(A)}} Inf_i(f_B) "
          f"<= N * {float(cf['maxIB']):.4g}")
