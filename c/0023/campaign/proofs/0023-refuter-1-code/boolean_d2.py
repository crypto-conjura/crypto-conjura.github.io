"""
Boolean side chamber: minimum max-influence of a +-1-valued function of
degree <= 2 on n = 4 variables (exhaustive over all 2^16 truth tables,
exact integer arithmetic).

Motivation: if sigma: {+-1}^n -> {+-1} has E[sigma] = 0, then
f = (1+sigma)/sqrt2, g = (1-sigma)/sqrt2 is an incompatible singleton pair
with Inf_i = Inf_i(sigma)/2, deg = deg(sigma).  For biased sigma the worse
side has Inf_i(sigma)/(2(1-|E sigma|)).  This scan determines the best
Boolean-derived pair at d = 2.  (By Nisan-Szegedy, degree-2 Boolean
functions have at most d*2^{d-1} = 4 relevant variables, so n = 4 is
exhaustive for d = 2; the scan itself is unconditional for n <= 4.)
"""
from fractions import Fraction as F

def wht(a):
    a = list(a)
    n = len(a); h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a

n = 4
P = 1 << n
best = None
best_unbiased = None
count_deg2 = 0
for tt in range(1 << P):
    vals = [1 if (tt >> x) & 1 else -1 for x in range(P)]
    co = wht(vals)                      # 16 * fhat(S)
    if any(co[S] for S in range(P) if bin(S).count("1") > 2):
        continue
    deg = max((bin(S).count("1") for S in range(P) if co[S]), default=0)
    if deg != 2:
        continue
    count_deg2 += 1
    mean = F(co[0], P)                  # E sigma
    if abs(mean) == 1:
        continue
    infl = [sum(F(co[S] * co[S], P * P) for S in range(P)
                if (S >> i) & 1 and co[S]) for i in range(n)]
    mx = max(infl)
    pair_val = mx / (2 * (1 - abs(mean)))
    if best is None or pair_val < best[0]:
        best = (pair_val, mx, mean, vals)
    if mean == 0 and (best_unbiased is None or mx < best_unbiased[0]):
        best_unbiased = (mx, vals)

print(f"degree-2 Boolean functions on 4 vars: {count_deg2}")
print(f"min over UNBIASED of max_i Inf_i(sigma): {best_unbiased[0]} "
      f"(pair value {best_unbiased[0]/2})")
print(f"min over all (biased allowed) Boolean pair value: {best[0]} "
      f"(max Inf {best[1]}, mean {best[2]})")
print()
print("Compare: the certified NON-Boolean singleton pair achieves 1/5 at "
      "d=2.")
