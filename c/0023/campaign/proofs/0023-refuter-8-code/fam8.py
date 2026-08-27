"""
fam8.py -- the deformation family and its closed forms (definitions only).

DEFORMATION LEMMA.  Let Z, K be disjoint coordinate blocks, |K| = d.  Let
R subseteq {+-1}^Z be nonempty of density rho with deg(1_R) = dR.  Pick
1 <= w <= d-1-dR, K1 subseteq K with |K1| = w, and put

    U = { x_K : x_{K1} != (+1)^w },      T = { x_K = (+1)^d },
    A = (R x U)  u  ({+-1}^Z x T),       B = complement(A).

Then, with t = 2^{-d}, u = 1 - 2^{-w}:
  (i)   1_A = 1_R 1_U + 1_T ; deg(1_R 1_U) <= dR + w <= d-1 and deg 1_T = d,
        so deg 1_A = deg 1_B = d and x_K is the UNIQUE degree-d monomial:
        M(A) = M(B) = K is forced.
  (ii)  alpha = rho*u + t.
  (iii) Inf_i(1_A) = u * Inf_i(1_R)                    (i in Z)
        Inf_i(1_A) = rho*2^{-w-1} + (1-2 rho)*2^{-d-1} (i in K1)
        Inf_i(1_A) = 2^{-d-1}                          (i in K \\ K1)
  (iv)  B = ~A, so Inf_i(f_A) = Inf_i(1_A)/alpha, Inf_i(f_B) = Inf_i(1_A)/beta;
        Q = max_i Inf_i(1_A)/max(alpha,beta),
        pi_M = (sum_{i in K} Inf_i(1_A)) (1/alpha + 1/beta).

V1: R = codim-k subcube  (dR = k, rho = 2^{-k}, Inf_i(1_R) = 2^{-k-1}), w = d-k-1.
V2: R = R1 u R2 on disjoint blocks Z1,Z2 of size k (dR = 2k,
    rho = 2^{1-k} - 2^{-2k}, Inf_i(1_R) = 2^{-k-1}(1-2^{-k})), w = d-2k-1.
"""
import sys, os, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import from_pred, complement, popcount


def build_V1(d, k):
    N = k + d
    mZ = (1 << k) - 1
    mK = ((1 << d) - 1) << k
    mK1 = ((1 << (d - k - 1)) - 1) << k

    def pred(m):
        return (((m & mZ) == 0) and ((m & mK1) != 0)) or ((m & mK) == 0)
    A = from_pred(N, pred)
    return N, A, complement(A, N), list(range(k)), list(range(k, k + d)), \
        list(range(k, k + d - k - 1))


def build_V2(d, k):
    N = 2 * k + d
    mZ1 = (1 << k) - 1
    mZ2 = ((1 << k) - 1) << k
    mK = ((1 << d) - 1) << (2 * k)
    w = d - 2 * k - 1
    assert w >= 1, "need d >= 2k+2"
    mK1 = ((1 << w) - 1) << (2 * k)

    def pred(m):
        inR = ((m & mZ1) == 0) or ((m & mZ2) == 0)
        return (inR and ((m & mK1) != 0)) or ((m & mK) == 0)
    A = from_pred(N, pred)
    return N, A, complement(A, N), list(range(2 * k)), \
        list(range(2 * k, 2 * k + d)), list(range(2 * k, 2 * k + w))


def lemma(d, w, rho, infR, nZ):
    t = F(1, 2 ** d)
    u = 1 - F(1, 2 ** w)
    alpha = rho * u + t
    beta = 1 - alpha
    iZ = [u * x for x in infR]
    iK1 = rho * F(1, 2 ** (w + 1)) + (1 - 2 * rho) * F(1, 2 ** (d + 1))
    iK0 = F(1, 2 ** (d + 1))
    sumK = w * iK1 + (d - w) * iK0
    mx = max(max(iZ), iK1, iK0)
    return dict(alpha=alpha, beta=beta, rho=rho, w=w, u=u, t=t,
                Q=mx / max(alpha, beta), piM=sumK * (1 / alpha + 1 / beta),
                maxIA=mx / alpha, maxIB=mx / beta,
                iZ=iZ[0], iK1=iK1, iK0=iK0,
                massA_on_R=rho * u / alpha,
                massB_off_R=(1 - rho) * (1 - t) / beta)


def V1_params(d, k):
    return d, d - k - 1, F(1, 2 ** k), [F(1, 2 ** (k + 1))] * k, k


def V2_params(d, k):
    rho = F(2, 2 ** k) - F(1, 4 ** k)
    return d, d - 2 * k - 1, rho, \
        [F(1, 2 ** (k + 1)) * (1 - F(1, 2 ** k))] * (2 * k), 2 * k


def subcube_distance(A, N):
    """min over ALL 3^N subcubes C of |A xor C| / |A|  (exact Fraction)."""
    nA = popcount(A)
    best = None
    for pat in itertools.product([0, 1, 2], repeat=N):
        fixed = want = 0
        for i, p in enumerate(pat):
            if p:
                fixed |= 1 << i
                if p == 2:
                    want |= 1 << i
        C = 0
        for m in range(1 << N):
            if (m & fixed) == want:
                C |= 1 << m
        v = F(popcount(A ^ C), nA)
        if best is None or v < best:
            best = v
    return best
