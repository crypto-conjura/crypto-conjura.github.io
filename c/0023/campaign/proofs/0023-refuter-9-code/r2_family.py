"""
r2_family.py -- the SWITCH family SW(d,s) and refuter-8's V1/V2, evaluated on
lambda with the LITERAL window rule W = W_A u W_B of 0023-analysis-1 S1.

SWITCH FAMILY SW(d,s), 1 <= s <= d-1, t := d-s, N = d.
  blocks: U = {0..s-1} (selector), K = {s..d-1} (|K| = t).
  u(x) = 1 iff x_U = (+1)^s          (density 2^-s, degree s)
  p = (+1)^t, q = (-1,+1,...,+1) in {+-1}^K, p =/= q.
  A = { u=1, x_K =/= q }  u  { u=0, x_K = p },     B = complement(A).
  1_A = 1_p + u*(1 - 1_q - 1_p), so deg 1_A <= t + s = d, and deg 1_B = deg 1_A.

CLOSED FORMS (claim, verified against brute force below):
  minimal defect set of A = minimal defect set of B = K, UNIQUELY, so the
  literal rule forces W = K.  Over w in {+-1}^U:
      alpha_w = 1 - 2^-t  (if u(w)=1),   2^-t  (if u(w)=0)
      E_w[min(alpha_w,1-alpha_w)] = 2^-t  for every w
      alpha = 2^-s + 2^-t - 2^{1-s-t},  beta = 1-alpha
      lam_A = 2^-t / alpha,  lam_B = 2^-t / beta
      max(lam_A,lam_B) = 2^-t / min(alpha,beta);  s=1 gives alpha=beta=1/2 and
      lam_A = lam_B = 2^{2-d} exactly.
"""
import sys, os, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "0023-refuter-8-code"))
from lib9 import (lam, E_min, minimal_defect_sets, deg, alpha, popcount,
                  relevant, maxinf_rel, fibre_profile, from_pred, complement,
                  spectrum, inf_fourier, inf_boundary, is_defect_set)
from fam8 import build_V1, build_V2


# ------------------------------------------------------------ constructors

def build_SW(d, s):
    """returns N, A, B, U, K  for the switch family."""
    t = d - s
    assert 1 <= s and t >= 1
    N = d
    mU = (1 << s) - 1                      # bits of U
    mK = ((1 << t) - 1) << s               # bits of K
    q = 1 << s                             # x_K = q  <=> (m & mK) == q  (first K coord -1)
    p = 0                                  # x_K = p = all +1  <=> (m & mK) == 0

    def pred(m):
        if (m & mU) == 0:                  # u = 1
            return (m & mK) != q
        return (m & mK) == p
    A = from_pred(N, pred)
    return N, A, complement(A, N), list(range(s)), list(range(s, d)), t


# ------------------------------------------------- independent degree route

def naive_top_coeffs_vanish(A, N, d):
    """route 2 for the degree: direct summation of sum_x 1_A(x) chi_S(x) for
    EVERY S with |S| > d (no FWHT).  Returns True iff all vanish."""
    pts = [m for m in range(1 << N) if (A >> m) & 1]
    for k in range(d + 1, N + 1):
        for S in itertools.combinations(range(N), k):
            mask = 0
            for i in S:
                mask |= 1 << i
            tot = 0
            for m in pts:
                tot += -1 if (bin(m & mask).count("1") & 1) else 1
            if tot != 0:
                return False, (k, S, tot)
    return True, None


def touching_mass(A, N, W):
    """(1/alpha) * sum_{S : S cap W =/= empty} fhat(S)^2  -- the exact quantity
    E_w[alpha_w(1-alpha_w)]/alpha, which sandwiches lam within [1,2]."""
    c = spectrum(A, N)
    nA = popcount(A)
    mW = 0
    for i in W:
        mW |= 1 << i
    num = 0
    for S in range(1 << N):
        if c[S] and (S & mW):
            num += c[S] * c[S]
    return F(num, (1 << N) * nA)


def report(label, N, A, B, d, Wforced=None):
    dA, dB = deg(A, N), deg(B, N)
    ok2, bad = naive_top_coeffs_vanish(A, N, d)
    DA = minimal_defect_sets(A, N, d)
    DB = minimal_defect_sets(B, N, d)
    Ws = sorted({tuple(sorted(set(a) | set(b))) for a in DA for b in DB})
    print("-- %s : N=%d  degA=%d degB=%d (naive route confirms deg<=%d: %s)  "
          "disjoint=%s  alpha=%s beta=%s"
          % (label, N, dA, dB, d, ok2 if ok2 else bad, (A & B) == 0,
             alpha(A, N), alpha(B, N)))
    print("   minimal defect sets: A -> %s ; B -> %s ; literal windows W_A u W_B -> %s"
          % (DA, DB, Ws))
    for W in Ws:
        la, lb = lam(A, N, W), lam(B, N, W)
        ta, tb = touching_mass(A, N, W), touching_mass(B, N, W)
        print("   W=%-14s lamA=%-22s (~%.3e)  lamB=%-22s (~%.3e)  max=%s (~%.3e)"
              % (list(W), la, float(la), lb, float(lb), max(la, lb),
                 float(max(la, lb))))
        print("      sandwich check: touchA<=lamA<=2*touchA : %s ; same for B: %s"
              % (ta <= la <= 2 * ta, tb <= lb <= 2 * tb))
        print("      floor 2^-d/alpha=%s <= lamA : %s ;  2^-d/beta=%s <= lamB : %s"
              % (F(1, 2 ** d) / alpha(A, N),
                 F(1, 2 ** d) / alpha(A, N) <= la,
                 F(1, 2 ** d) / alpha(B, N),
                 F(1, 2 ** d) / alpha(B, N) <= lb))
        print("      maxinf: max_i Inf_i(f_A)=%s (~%.3e) <= lamA_star? ; "
              "max_i Inf_i(f_B)=%s (~%.3e)"
              % (maxinf_rel(A, N), float(maxinf_rel(A, N)),
                 maxinf_rel(B, N), float(maxinf_rel(B, N))))
    # the enlarged window: all relevant coordinates
    rel = sorted(set(relevant(A, N)) | set(relevant(B, N)))
    if len(rel) <= 4 * d:
        print("   ENLARGED window W* = rel(A) u rel(B), |W*|=%d <= 4d=%d : "
              "lamA=%s lamB=%s   (defect for A:%s B:%s)"
              % (len(rel), 4 * d, lam(A, N, rel), lam(B, N, rel),
                 is_defect_set(A, N, rel), is_defect_set(B, N, rel)))
    return Ws


if __name__ == "__main__":
    print("=" * 78)
    print("SWITCH FAMILY -- brute force vs closed form")
    print("=" * 78)
    for d in range(2, 13):
        for s in range(1, d):
            N, A, B, U, K, t = build_SW(d, s)
            if N > 12:
                continue
            W = tuple(K)
            la, lb = lam(A, N, W), lam(B, N, W)
            al = alpha(A, N)
            # closed form
            al_cf = F(1, 2 ** s) + F(1, 2 ** t) - F(2, 2 ** (s + t))
            la_cf = F(1, 2 ** t) / al_cf
            lb_cf = F(1, 2 ** t) / (1 - al_cf)
            em = E_min(A, N, W)
            ok = (al == al_cf and la == la_cf and lb == lb_cf
                  and em == F(1, 2 ** t))
            DA = minimal_defect_sets(A, N, d)
            DB = minimal_defect_sets(B, N, d)
            uniq = (DA == [tuple(K)] and DB == [tuple(K)])
            print("d=%2d s=%2d t=%2d | deg=%d/%d | alpha=%-18s lamA=%-16s lamB=%-16s "
                  "max=%-16s | closedform=%s uniqueW=K:%s"
                  % (d, s, t, deg(A, N), deg(B, N), al, la, lb, max(la, lb),
                     ok, uniq))
        print()
    print("=" * 78)
    print("DETAILED CERTIFICATES (switch family, s=1 and s=2)")
    print("=" * 78)
    for (d, s) in [(4, 1), (5, 1), (6, 1), (8, 1), (6, 2), (8, 2), (10, 3)]:
        N, A, B, U, K, t = build_SW(d, s)
        report("SW(d=%d,s=%d)" % (d, s), N, A, B, d)
        print()
    print("=" * 78)
    print("refuter-8's V1 / V2 deformation families under lambda")
    print("=" * 78)
    for (d, k) in [(4, 1), (5, 1), (6, 2), (7, 2), (8, 3)]:
        N, A, B, Z, K, K1 = build_V1(d, k)
        if N <= 12:
            report("V1(d=%d,k=%d)" % (d, k), N, A, B, d)
            print()
    for (d, k) in [(5, 1), (6, 1), (8, 2)]:
        N, A, B, Z, K, K1 = build_V2(d, k)
        if N <= 12:
            report("V2(d=%d,k=%d)" % (d, k), N, A, B, d)
            print()
