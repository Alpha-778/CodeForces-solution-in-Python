import sys
I = sys.stdin.read
class F:
    def __init__(s, n): s.t = [0]*(n+5); s.n = n+5
    def u(s, i, d):
        while i < s.n: s.t[i] += d; i += i & -i
    def q(s, i):
        r = 0
        while i: r += s.t[i]; i -= i & -i
        return r
    def le(s, x): return s.q(x)
def R(n,k,A):
    m = max(A)+2
    T = F(m)
    for x in A: T.u(x,1)
    l,r = 0,n-1
    while l<r:
        if A[l]==A[r]: l+=1; r-=1; continue
        x,y = A[l],A[r]
        cL,cR = T.le(x)>=k, T.le(y)>=k
        if not(cL or cR): return 'NO'
        if cL and (not cR or x>y): T.u(x,-1); l+=1
        else: T.u(y,-1); r-=1
    return 'YES'
D = I().split(); i = 0; T = int(D[i]); i+=1; O=[]
for _ in range(T):
    n,k = int(D[i]),int(D[i+1]); i+=2
    A = list(map(int,D[i:i+n])); i+=n
    O.append(R(n,k,A))
print('\n'.join(O))