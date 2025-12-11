I=10**9+7;L=10**5+5
F=[1]*L;R=[1]*L
def P(x,y):
 r=1;x%=I
 while y:r=r*x%I if y&1 else r;x=x*x%I;y//=2
 return r
for i in range(1,L):F[i]=F[i-1]*i%I
R[-1]=P(F[-1],I-2)
for i in range(L-2,-1,-1):R[i]=R[i+1]*(i+1)%I
def C(n,r):
 if r<0:return 0
 z=1;n%=I
 for i in range(r):z=z*(n-i)%I
 return z*R[r]%I

t=int(input())
rec=[list(map(int,input().split()))for _ in range(t)]
for _ in range(t):
 a,b,k=rec[_]
 x=(a-1)*k+1
 y=(b-1)*k*C(x,a)%I+1
 print(x%I,y%I)