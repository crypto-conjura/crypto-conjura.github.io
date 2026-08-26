#!/usr/bin/env python3
"""Machine-check for the four numeric claims of Remark rem:window in
split-decomp-kappa-3-r4.md.  Run: python3 rem-window-r4.py

Notation is the Contract's.  sigma' := sigma + 2 log_2 N ; q+ := q+1 ;
t_q := sqrt(sigma' q+ / delta) ; t_0 := sqrt(sigma'/delta).

An instance is NON-VACUOUS when 8 sqrt(sigma' q+ delta) < 1 -- outside that
regime Theorem E''s conclusion exceeds 1 and says nothing (Lemma G0).
The source range also requires delta >= 1/N and N, M >= 2.

Claims, asserted on every non-vacuous grid point:
  C1  t_0 > 8 sigma' sqrt(q+)  and  t_0 >= 16          (uses sigma' >= 2)
  C2  ceil(t_q) > t_0 + 1  for every q >= 1            (applications are interior)
  C3  ceil(t_q) < N^2                                  (and so is below the upper end)
  C4  t_0 + 1 < N^2                                    (the window is non-empty)
"""
import math

Ns     = [2**k for k in range(1, 31)]                 # N up to 2^30
sigmas = [0, 1, 2, 4, 8, 16, 32, 64]                  # sigma up to 64
qs     = [0, 1, 2, 10, 10**3, 10**5, 10**7]           # q up to 10^7
frac   = [1.0, 0.5, 0.1, 0.01, 1e-3, 1e-5, 1e-8]      # delta as a fraction of 1, floored at 1/N

def deltas(N):
    lo = 1.0 / N
    return sorted({max(lo, f) for f in frac} | {lo})

tested = failures = 0
worst_c1 = math.inf   # min over points of t_0 / (8 sigma' sqrt(q+))
worst_c2 = math.inf   # min over points (q>=1) of ceil(t_q) - (t_0 + 1)
worst_t0 = math.inf

for N in Ns:
    sp_base = 2 * math.log2(N)
    for sigma in sigmas:
        sp = sigma + sp_base                          # sigma'
        for q in qs:
            qp = q + 1
            for d in deltas(N):
                if not (8 * math.sqrt(sp * qp * d) < 1):
                    continue                          # vacuous: Lemma G0 case
                tested += 1
                t0 = math.sqrt(sp / d)
                tq = math.sqrt(sp * qp / d)
                ctq = math.ceil(tq)
                ok = True
                if not (t0 > 8 * sp * math.sqrt(qp) and t0 >= 16):        # C1
                    ok = False
                if q >= 1 and not (ctq > t0 + 1):                          # C2
                    ok = False
                if not (ctq < N * N):                                      # C3
                    ok = False
                if not (t0 + 1 < N * N):                                   # C4
                    ok = False
                if not ok:
                    failures += 1
                    print(f"FAIL N=2^{int(math.log2(N))} sigma={sigma} q={q} "
                          f"delta={d:g} t0={t0:g} ceil(tq)={ctq}")
                worst_c1 = min(worst_c1, t0 / (8 * sp * math.sqrt(qp)))
                worst_t0 = min(worst_t0, t0)
                if q >= 1:
                    worst_c2 = min(worst_c2, ctq - (t0 + 1))

print(f"non-vacuous points tested : {tested}")
print(f"failures                  : {failures}")
print(f"C1 worst ratio t_0/(8 s' sqrt(q+)) : {worst_c1:.6f}  (must exceed 1)")
print(f"C1 worst t_0                       : {worst_t0:.4f}  (must be >= 16)")
print(f"C2 worst margin ceil(t_q)-(t_0+1)  : {worst_c2:.4f}  (must exceed 0)")
