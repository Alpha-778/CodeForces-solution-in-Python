from bisect import *
class S:
 def __init__(s,n):s.n=n;s.m=[0]*4*n;s.z=[0]*4*n
 def p(s,v):
  if s.z[v]:
   for u in[v<<1,v<<1|1]:s.m[u]+=s.z[v];s.z[u]+=s.z[v]
   s.z[v]=0
 def a(s,v,l,r,x,y,d):
  if x>r or y<l:return
  if x<=l<=r<=y:s.m[v]+=d;s.z[v]+=d;return
  s.p(v);m=(l+r)//2
  s.a(v*2,l,m,x,y,d);s.a(v*2+1,m+1,r,x,y,d)
  s.m[v]=max(s.m[v*2],s.m[v*2+1])
 def q(s,v,l,r,x,y):
  if x>r or y<l:return 0
  if x<=l<=r<=y:return s.m[v]
  s.p(v);m=(l+r)//2
  return max(s.q(v*2,l,m,x,y),s.q(v*2+1,m+1,r,x,y))
 def ra(s,l,r,d):s.a(1,0,s.n-1,l,r,d)
 def rm(s,l,r):return 0 if l>r else s.q(1,0,s.n-1,l,r)
 def pv(s,p):return s.q(1,0,s.n-1,p,p)

t = int(input())
rec = []
for _ in range(t):
 n = int(input())
 case = []
 for _ in range(n):
  l, r = map(int, input().split())
  case.append((l, r))
 rec.append((n, case))
results = []
for n, case in rec:
 coords = [l for l,_ in case]
 coords = sorted(set(coords))
 m = len(coords)
 T = S(m)
 A = []
 for l, r in case:
  a = bisect_left(coords, l)
  b = bisect_right(coords, r) - 1
  if b >= a: T.ra(a,b,1)
  z = T.rm(0,a-1) if a else 0
  nl = z + 1
  cur = T.pv(a)
  if nl > cur: T.ra(a,a,nl-cur)
  A.append(T.rm(0,m-1))
 results.append(A)
for a in results: print(*a)