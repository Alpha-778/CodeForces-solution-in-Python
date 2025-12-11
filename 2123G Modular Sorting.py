I=input;R=range
def GCD(a,b): 
 while b:a,b=b,a%b
 return a
def M(L,R,g):
 x=R[2];y=L[3]
 m=L[1]+(y>x)+R[1]
 v=max(L[0],g*(L[1]+(y>x))+R[0])
 return [v,m,L[2],R[3]]
def B(T,A,g,v,l,r):
 if l==r:
  x=A[l]%g;T[v]=[x,0,x,x]
 else:
  m=(l+r)//2;B(T,A,g,2*v,l,m);B(T,A,g,2*v+1,m+1,r)
  T[v]=M(T[2*v],T[2*v+1],g)
def U(T,A,g,v,l,r,p):
 if l==r:
  x=A[p]%g;T[v]=[x,0,x,x]
 else:
  m=(l+r)//2
  if p<=m:U(T,A,g,2*v,l,m,p)
  else:U(T,A,g,2*v+1,m+1,r,p)
  T[v]=M(T[2*v],T[2*v+1],g)
for _ in R(int(I())):
 n,m,q=map(int,I().split())
 A=[0]+list(map(int,I().split()))
 Z=[list(map(int,I().split())) for _ in R(q)]
 d,q2={},[]
 for i,x in enumerate(Z):
  if x[0]==2:
   g=GCD(x[1],m)
   if g not in d:d[g]=[]
   d[g].append(i);q2.append(i)
 ok=[0]*q
 for g,V in d.items():
  a=A[:];T=[[0]*4 for _ in R(4*n+4)]
  if n:B(T,a,g,1,1,n)
  j=0
  for i in R(q):
   t,x=Z[i][:2]
   if t==1:
    a[x]=Z[i][2]
    if n:U(T,a,g,1,1,n,x)
   elif j<len(V) and i==V[j]:
    ok[i]=int(n==0 or T[1][0]<m);j+=1
 for i in sorted(q2):print("YES" if ok[i] else "NO")