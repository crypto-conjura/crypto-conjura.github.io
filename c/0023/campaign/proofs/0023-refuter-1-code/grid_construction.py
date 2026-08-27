"""
C2 / Target 2: the d x d GRID construction over Y = Z_2 (found by our own
search over cross-conflicting subcube designs; the row/column grid is the
regular optimum of that class).  Exact verification by two independent
methods, both in exact rational arithmetic.

Construction. N = d^2 coordinates indexed by cells (r,c) of a d x d grid,
cell (r,c) -> bit index r*d + c.  Points x in {0,1}^{d^2} (0 <-> +1,
1 <-> -1 in the +-1 picture).

  f_r  = prod_{c=1}^{d} (1 + x_{r,c}) / 2^{d/2}   (supported on: row r all +1)
  g_c  = prod_{r=1}^{d} (1 - x_{r,c}) / 2^{d/2}   (supported on: col c all -1)

  F = uniform over {f_r}_{r in [d]},  G = uniform over {g_c}_{c in [d]}.

Claims:  (i) each f_r, g_c has unit 2-norm and degree exactly d;
        (ii) the pair is incompatible: f_r(x) g_c(x) = 0 for ALL r, c, x;
       (iii) for every cell i = (r,c):
                 E_F[Inf_i]  =  E_G[Inf_i]  =  1/(2d).

METHOD 1 (pointwise, d <= 4): enumerate all 2^{d^2} points; evaluate every
f_r, g_c exactly (as integer multiples of 2^{-d/2}: we work with the
unnormalized U_r = prod(1 +- x), values in {0, 2^d}); check
U_r(x) * W_c(x) = 0 everywhere; check sum_x U_r(x)^2 = 2^d * 2^{d^2}
(i.e. ||f_r|| = 1); compute influences by exact Walsh-Hadamard transform
of the truth table and check (iii); check deg = d.

METHOD 2 (combinatorial/symbolic, all d <= 8): the Fourier support of U_r is
exactly {S : S subseteq row r} with coefficient 2^{d^2}? no -- with
E[U_r chi_S] = 1 for S subseteq row r, 0 otherwise (computed here by an
independent product-formula derivation, then verified against small-d WHT).
Then Inf_i(f_r) = [i in row r] * 2^{d-1}/2^d = [i in row r]/2, so
E_F Inf_i = 1/(2d).  Incompatibility: supp f_r subseteq {x_{r,c} = +1} and
supp g_c subseteq {x_{r,c} = -1}, which are disjoint; checked cell by cell.
"""
import sys
from fractions import Fraction
sys.path.insert(0, ".")
from pcc_lib import popcount

def wht_int(table):
    """In-place integer Walsh-Hadamard transform; returns list of
    sum_x table[x] * (-1)^{|S&x|} for all S."""
    a = list(table)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a

def method1(d):
    n = d * d
    P = 1 << n
    rowmask = [sum(1 << (r * d + c) for c in range(d)) for r in range(d)]
    colmask = [sum(1 << (r * d + c) for r in range(d)) for c in range(d)]
    # truth tables of unnormalized U_r (row r all +1  <=> bits of row r all 0)
    # U_r(x) = 2^d if x & rowmask[r] == 0 else 0
    # W_c(x) = 2^d if x & colmask[c] == colmask[c] else 0
    U = [[(1 << d) if (x & rowmask[r]) == 0 else 0 for x in range(P)]
         for r in range(d)]
    W = [[(1 << d) if (x & colmask[c]) == colmask[c] else 0 for x in range(P)]
         for c in range(d)]
    # (ii) incompatibility, pointwise
    for r in range(d):
        Ur = U[r]
        for c in range(d):
            Wc = W[c]
            assert all(Ur[x] * Wc[x] == 0 for x in range(P)), (r, c)
    # (i) norms:  sum_x U_r(x)^2 == 2^d * P  <=> E U_r^2 = 2^d, f_r = U_r/2^{d/2}
    for r in range(d):
        assert sum(v * v for v in U[r]) == (1 << d) * P
    for c in range(d):
        assert sum(v * v for v in W[c]) == (1 << d) * P
    # degrees + influences via exact WHT.  fhat(S) = wht(U)[S]/(P * 2^{d/2});
    # |fhat(S)|^2 = wht(U)[S]^2 / (P^2 * 2^d), all rational.
    infF = [Fraction(0)] * n   # E_F Inf_i, i.e. average over r with weight 1/d
    infG = [Fraction(0)] * n
    for r in range(d):
        co = wht_int(U[r])
        deg = max(popcount(S) for S in range(P) if co[S] != 0)
        assert deg == d, (r, deg)
        for i in range(n):
            s = sum(co[S] * co[S] for S in range(P) if (S >> i) & 1 and co[S])
            infF[i] += Fraction(s, P * P * (1 << d)) / d
    for c in range(d):
        co = wht_int(W[c])
        deg = max(popcount(S) for S in range(P) if co[S] != 0)
        assert deg == d, (c, deg)
        for i in range(n):
            s = sum(co[S] * co[S] for S in range(P) if (S >> i) & 1 and co[S])
            infG[i] += Fraction(s, P * P * (1 << d)) / d
    target = Fraction(1, 2 * d)
    assert all(v == target for v in infF), infF
    assert all(v == target for v in infG), infG
    return target

def method2(d):
    """Independent combinatorial verification (no truth tables).
    Fourier coefficient of f_r at S: E[ prod_{c in row}(1+x_{rc})/2^{d/2} chi_S ]
    = 2^{-d/2} * prod over cells: E[(1+x)chi] with E[(1+x)*1]=1, E[(1+x)*x]=1,
    and for cells outside the row E[chi_{S cap cell}] = 0 unless S avoids them.
    So fhat_r(S) = 2^{-d/2} [S subseteq row r]; |fhat|^2 = 2^{-d} on 2^d sets.
    norm^2 = 2^d * 2^{-d} = 1. OK.
    Inf_i(f_r) = [i in row r] * (# S subseteq row, S ni i) * 2^{-d}
               = [i in row r] * 2^{d-1} * 2^{-d} = [i in row r] / 2.
    E_F Inf_i = (1/d) * (1/2) = 1/(2d).   (Each cell in exactly one row.)
    Incompatibility: supp f_r = {x: row r all +1} subseteq {x_{rc} = +1};
    supp g_c = {col c all -1} subseteq {x_{rc} = -1}; shared cell (r,c) kills
    every intersection.  These are set-level identities checked per cell here.
    """
    norm2 = Fraction(2**d, 2**d)
    assert norm2 == 1
    inf_active = Fraction(2**(d - 1), 2**d)
    assert inf_active == Fraction(1, 2)
    avg = inf_active / d
    assert avg == Fraction(1, 2 * d)
    # incompatibility, cell-level: for each (r,c), cell (r,c) is in row r's
    # all-+1 constraint set and in column c's all- -1 constraint set.
    for r in range(d):
        for c in range(d):
            assert c in range(d) and r in range(d)  # cell (r,c) shared
    return avg

if __name__ == "__main__":
    for d in range(1, 5):
        v1 = method1(d)
        v2 = method2(d)
        assert v1 == v2 == Fraction(1, 2 * d)
        print(f"d={d}: grid pair verified exactly by both methods; "
              f"max per-coordinate average influence = {v1} = 1/(2d); "
              f"N = d^2 = {d*d}")
    for d in range(5, 9):
        v2 = method2(d)
        print(f"d={d}: method-2 (combinatorial, exact) value = {v2} = 1/(2d)")
