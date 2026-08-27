#!/usr/bin/env python3
"""Machine-check for split-decomp-kappa-4-r2 (Theorems H and H').

REWRITTEN after the six-referee audit of kappa-4.  Four defects in the previous
version, all reported by referees, all fixed here:

  1. The old grid never evaluated any point with q >= 10^3.  The vacuity filter
     8 sqrt(s' q+ d) < 1 needs s' q+ d < 1/64, and with delta >= 1/N and N <= 2^20
     that forces q+ < 410.  So sqrt(q+) -- the entire subject of Theorem H' -- was
     exercised only up to sqrt(11) = 3.32.  N now runs to 2^44, which makes q = 10^7
     non-vacuous and exercises sqrt(q+) past 3000.
  2. (H2) was never evaluated.  It is a hypothesis of Theorem E'', so a point where
     it fails is a point where the theorems claim nothing.  Now computed explicitly.
  3. P_0 >= 1 was never checked, though Theorem E'' requires P in N.
  4. The reported "smallest sufficient C = 12.0000" was a rounding of 12.0000000075.
     The strict inequality is the whole point -- it is what shows C = 12 FAILS.
     Now reported with enough digits to see it.

Also added: the floor-cap variant (claim A of the simplification audit), which the
audit showed needs C = 14 by the verbatim route, or C = 13 once Lemma H1's
N^-2 <= S is sharpened to N^-2 <= S/4.

Notation: s' := sigma + 2 log2 N ; q+ := q+1 ; S := sqrt(s' q+ d) ;
t_q := sqrt(s' q+/d) ; t_0 := sqrt(s'/d) ; B := s' + log2(1/gamma) ;
gamma_0 := max(gamma, N^-2) ; mu'(s) := min(s d, 2 (s d^2)^(1/3), 1).

Standing hypothesis N, M >= 2 (finding C1): every dependency states it, and
s' >= 2 follows from it with sigma >= 0.  N = 1 is NOT in scope and is not tested.
"""
import math

def mu(s, d):
    return 0.0 if s <= 0 else min(s*d, 2*(s*d*d)**(1/3), 1.0)

def H2(N, sp, q, d, M):
    """(H2) of Theorem E'' at this q."""
    return min(mu(min(q*M, N*N), d), 2*d*math.sqrt(M)) <= math.sqrt(sp*(q+1)*d)

Ns     = [2**k for k in (11, 14, 17, 20, 26, 32, 38, 44)]   # up to 2^44: large q reachable
sigmas = [0, 1, 4, 16, 64]
qs     = [0, 1, 2, 10, 10**3, 10**5, 10**7]
gammas = [0.5, 0.1, 1e-3, 1e-6, 1e-12, 1e-30]
Ms     = [2, 4, 2**10, 2**20]

def run(cap, C_claim, label, qfree=False):
    tested = fails = 0
    worstC, at = 0.0, None
    q_seen, sq_max, minP0 = set(), 0.0, math.inf
    h2_fail = 0
    for N in Ns:
        for sig in sigmas:
            sp = sig + 2*math.log2(N)
            for q in qs:
                qp = q + 1
                for frac in (1.0, 1e-3, 1e-8, None):
                    d = 1.0/N if frac is None else max(1.0/N, frac)
                    if not (8*math.sqrt(sp*qp*d) < 1):
                        continue                      # vacuous: target > 1 >= Adv
                    S  = math.sqrt(sp*qp*d)
                    tq = math.sqrt(sp*qp/d); t0 = math.sqrt(sp/d)
                    base = t0 if qfree else tq
                    for M in Ms:
                        if not H2(N, sp, q, d, M):
                            h2_fail += 1
                            continue                  # E'' claims nothing here
                        for g in gammas:
                            g0 = max(g, N**-2.0)
                            B  = sp + math.log2(1/g); B0 = sp + math.log2(1/g0)
                            for P in sorted({1, 2, max(1, int(base)), int(base)+1,
                                             2*math.ceil(base), N, N*N//2, N*N}):
                                P0 = min(P, cap(base))
                                if P0 < 1:
                                    print(f"   !! P_0 = {P0} < 1 at N={N} sig={sig} q={q}")
                                    fails += 1; continue
                                minP0 = min(minP0, P0)
                                tested += 1; q_seen.add(q); sq_max = max(sq_max, math.sqrt(qp))
                                lhs = 2*B0*qp/P0 + 8*S + g0
                                Cq  = (4*math.sqrt(qp) + 9) if qfree else C_claim
                                if not (lhs <= 2*B*qp/P + Cq*S + g + 1e-12):
                                    fails += 1
                                need = (lhs - g - 2*B*qp/P)/S
                                if need > worstC: worstC, at = need, (N, sig, q, d, M, g, P)
    print(f"{label}")
    print(f"   points tested {tested}   failures {fails}   "
          f"(skipped {h2_fail} where (H2) fails)")
    print(f"   q actually exercised : {sorted(q_seen)}   max sqrt(q+) = {sq_max:.1f}")
    print(f"   min P_0 seen         : {minP0}  (must be >= 1)")
    claim = "4 sqrt(q+) + 9 (varies)" if qfree else f"{C_claim}"
    print(f"   smallest sufficient C: {worstC:.10f}   claimed {claim}")
    if not qfree:
        print(f"   NOTE: this measures the ACTUAL gamma_0/S, not the <= 1 the proof uses.")
        print(f"         The grid therefore cannot distinguish the proof's constant from")
        print(f"         this number; it corroborates, it does not establish. (Audit finding.)")
    print(f"     at (N,sig,q,delta,M,gamma,P) = {at}")

run(math.ceil, 13.0, "Theorem H  (ceiling cap, C = 13):")
print()
run(math.ceil, 13.0, "Theorem H' (q-free ceiling cap, C(q) = 4 sqrt(q+) + 9):", qfree=True)
print()
run(math.floor, 14.0, "Claim A    (FLOOR cap, verbatim route -> C = 14):")
