#!/usr/bin/env python3
"""Check the capping argument that closes the P-window at fixed q.

Given the instance (N, M, sigma, delta, q) write
    s'  := sigma + 2 log2 N      q+ := q+1      S := sqrt(s' q+ delta)
    t   := sqrt(s' q+ / delta)   B  := s' + log2(1/gamma)

CONSTRUCTION.  For a requested (P, gamma) put
    gamma_0 := max(gamma, N^-2)          (clamp the slack)
    P_0     := min(P, ceil(t))           (cap the fixed set)
and take the family Y^{P_0, gamma_0/2} of Theorem E'' -- legal as a family of
P-mixtures because def:bf asks |I| <= P and P_0 <= P.

Theorem E'' applies at (P_0, gamma_0): its (H1) is P_0 <= t + 1, which holds by
construction, and its (H2) is a condition on M alone, untouched.  It yields
    Adv <= 2 (s' + log2(1/gamma_0)) q+ / P_0 + 8 S + gamma_0        (LHS)
and the Contract's conj:main target at the REQUESTED P is
    Adv <= c B q+ / P + C S + gamma                                 (RHS)

CLAIMS, over every grid point:
  V1  N^-2 <= S                                   (the clamp costs under one S)
  V2  log2(1/gamma_0) <= s'                       (so s' + log2(1/gamma_0) <= 2 s')
  V3  log2(1/gamma_0) <= log2(1/gamma)            (so c does not move off 2)
  V4  P_0 <= t + 1                                (H1) holds at P_0
  V5  LHS <= RHS  with  c = 2, C = 13             the theorem
Also reported: the smallest C that would have sufficed on this grid.
"""
import math

C_CLAIM, c_CLAIM = 13.0, 2.0
Ns     = [2**k for k in range(1, 21)]
sigmas = [0, 1, 4, 16, 64]
qs     = [0, 1, 2, 10, 10**3, 10**5, 10**7]
gammas = [0.5, 0.1, 1e-3, 1e-6, 1e-12, 1e-30]      # incl. gamma << N^-2
frac   = [1.0, 0.1, 1e-3, 1e-5, 1e-8]

tested = 0
fails  = {f"V{i}": 0 for i in range(1, 6)}
worst_C, worst_at = 0.0, None
worst_slack = math.inf

for N in Ns:
    for sigma in sigmas:
        sp = sigma + 2 * math.log2(N)                    # sigma'
        for q in qs:
            qp = q + 1
            for f in frac:
                d = max(1.0 / N, f)                      # delta >= 1/N
                if not (8 * math.sqrt(sp * qp * d) < 1):
                    continue                             # vacuous (Lemma G0)
                S = math.sqrt(sp * qp * d)
                t = math.sqrt(sp * qp / d)
                for g in gammas:
                    g0 = max(g, N ** -2.0)
                    B  = sp + math.log2(1.0 / g)
                    B0 = sp + math.log2(1.0 / g0)
                    # P ranges over the whole axis, window included, up to N^2
                    Ps = sorted({1, 2, max(1, math.floor(t)), math.ceil(t),
                                 math.ceil(t) + 1, 2 * math.ceil(t),
                                 max(1, N), max(1, N * N // 2), N * N})
                    for P in Ps:
                        if P < 1:
                            continue
                        tested += 1
                        P0 = min(P, math.ceil(t))
                        if not (N ** -2.0 <= S):                 fails["V1"] += 1
                        if not (math.log2(1.0 / g0) <= sp):      fails["V2"] += 1
                        if not (math.log2(1.0/g0) <= math.log2(1.0/g)): fails["V3"] += 1
                        if not (P0 <= t + 1):                    fails["V4"] += 1
                        lhs = 2 * B0 * qp / P0 + 8 * S + g0
                        rhs = c_CLAIM * B * qp / P + C_CLAIM * S + g
                        if not (lhs <= rhs + 1e-12):             fails["V5"] += 1
                        # smallest C that works here, at c = 2
                        need = (lhs - g - c_CLAIM * B * qp / P) / S
                        if need > worst_C:
                            worst_C, worst_at = need, (N, sigma, q, d, g, P)
                        worst_slack = min(worst_slack, rhs - lhs)

print(f"grid points tested : {tested}")
for k in sorted(fails):
    print(f"  {k} failures       : {fails[k]}")
print(f"smallest sufficient C on this grid : {worst_C:.4f}   (claimed {C_CLAIM})")
print(f"  attained at (N,sigma,q,delta,gamma,P) = {worst_at}")
print(f"worst slack RHS-LHS : {worst_slack:.6g}  (must be >= 0)")

# ----------------------------------------------------------------------------
# The strict (q-free) variant.  Cap at the q-FREE balance point t_0 = sqrt(s'/d)
# so the family is independent of q, as conj:main proper demands.  (H1) at P_0
# still holds for EVERY q, since t_0 <= t_q.  The bound degrades by sqrt(q+):
#     V6   LHS <= 2 B q+/P + (4 sqrt(q+) + 9) S + gamma     for every P and q
# This is rem:reduces's Theta(sqrt(q+)) separation, made uniform in P.
# ----------------------------------------------------------------------------
print()
tested6 = fail6 = 0
worst_mult, worst_at6 = 0.0, None
for N in Ns:
    for sigma in sigmas:
        sp = sigma + 2 * math.log2(N)
        for q in qs:
            qp = q + 1
            for f in frac:
                d = max(1.0 / N, f)
                if not (8 * math.sqrt(sp * qp * d) < 1):
                    continue
                S  = math.sqrt(sp * qp * d)
                t0 = math.sqrt(sp / d)                    # q-FREE cap
                tq = math.sqrt(sp * qp / d)
                for g in gammas:
                    g0 = max(g, N ** -2.0)
                    B, B0 = sp + math.log2(1/g), sp + math.log2(1/g0)
                    for P in sorted({1, max(1, math.floor(t0)), math.ceil(t0),
                                     math.ceil(t0) + 1, max(1, N),
                                     max(1, N*N//2), N*N}):
                        tested6 += 1
                        P0 = min(P, math.ceil(t0))
                        assert P0 <= tq + 1                # (H1) at every q
                        lhs = 2 * B0 * qp / P0 + 8 * S + g0
                        rhs = 2 * B * qp / P + (4*math.sqrt(qp) + 9) * S + g
                        if not (lhs <= rhs + 1e-12):
                            fail6 += 1
                        mult = (lhs - g - 2 * B * qp / P) / S
                        if mult > worst_mult:
                            worst_mult, worst_at6 = mult, (N, sigma, q, d, g, P)

print(f"q-FREE variant: grid points tested : {tested6}")
print(f"  V6 failures                      : {fail6}")
print(f"  worst multiplier on S            : {worst_mult:.4f}"
      f"   (claimed 4 sqrt(q+) + 9)")
print(f"  attained at (N,sigma,q,delta,gamma,P) = {worst_at6}")
