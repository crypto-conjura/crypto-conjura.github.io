#!/usr/bin/env python3
"""Exact check of the T5(b) verification table (grid, subcube pair, address pair)."""
from fractions import Fraction as F

def wht(vals, N):
    a=list(vals); n=1<<N; h=1
    while h<n:
        for i in range(0,n,h*2):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [c/n for c in a]
pc=lambda x: bin(x).count('1')

def data(memb, N):
    v=[F(1) if memb(m) else F(0) for m in range(1<<N)]
    c=wht(v,N)
    deg=max(pc(S) for S in range(1<<N) if c[S]!=0)
    inf=[sum(c[S]**2 for S in range(1<<N) if (S>>i)&1) for i in range(N)]
    return c, deg, c[0], inf

def pay(dA, dB, WA, WB, N):
    cA,degA,al,iA = dA; cB,degB,be,iB = dB
    return sum(iA[i] for i in WB)/al + sum(iB[i] for i in WA)/be

# ---- grid: coordinates (i,j) -> index i*d+j ; bit set <=> x = -1
for d in (2,3,4):
    N=d*d
    if N>16: break
    r,c0=0,0
    A=data(lambda m: all((m>>(r*d+j))&1==1 for j in range(d)), N)   # row r all -1
    B=data(lambda m: all((m>>(i*d+c0))&1==0 for i in range(d)), N)  # col c all +1
    WA=[r*d+j for j in range(d)]; WB=[i*d+c0 for i in range(d)]
    print(f"grid d={d}: degA={A[1]} degB={B[1]} alpha={A[2]} pi={pay(A,B,WA,WB,N)}")

# ---- codim-d subcube pair (C, C^c) inside {+-1}^N, N=d+1 spectator-free extra coord
for d in (2,3,4,5):
    N=d+1
    C=data(lambda m: all((m>>i)&1==0 for i in range(d)), N)
    Cc=data(lambda m: not all((m>>i)&1==0 for i in range(d)), N)
    W=list(range(d))
    print(f"subcube d={d}: degC={C[1]} degCc={Cc[1]} alpha={C[2]} pi={pay(C,Cc,W,W,N)}"
          f"  expected={F(d)*(F(1,2)+F(1,2**(d+1))/(1-F(1,2**d)))}")

# ---- address pair: a_1..a_k (indices 0..k-1), targets y_j (indices k..k+2^k-1)
for k in (1,2,3):
    N=k+2**k
    if N>16: break
    def inA(m):
        j=sum(((m>>i)&1)<<i for i in range(k))   # address value from its bits
        return (m>>(k+j))&1==0                   # y_j = +1
    A=data(inA,N); B=data(lambda m: not inA(m), N)
    for jj in range(2**k):
        WA=list(range(k))+[k+jj]
        for jj2 in range(2**k):
            WB=list(range(k))+[k+jj2]
            p=pay(A,B,WA,WB,N)
            if jj==0 and jj2==min(1,2**k-1):
                print(f"address k={k} (d={k+1}): degA={A[1]} alpha={A[2]} "
                      f"Inf_a={A[3][0]} Inf_y={A[3][k]} pi={p} expected={F(k,2)+F(1,2**k)}")
