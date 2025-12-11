t=int(input())
for _ in range(t):
 n,k=map(int,input().split());N=2*n;g=[[]for _ in range(N)];gr=[[]for _ in range(N)]
 f=lambda x,p:2*x+(0 if p else 1)
 for _ in range(k):
  m=int(input());adj=[0]*n
  for _ in range(m):
   u,v=map(lambda x:int(x)-1,input().split());adj[u]|=1<<v;adj[v]|=1<<u
  for u in range(n):
   for v in range(u+1,n):
    if(u==v):continue
    mask=((1<<n)-1)^((1<<u)|(1<<v))
    if((adj[u]&mask)!=(adj[v]&mask)):continue
    if(adj[u]>>v&1):
     a,b=f(u,1),f(v,0);g[a]+=[b];gr[b]+=[a]
     a,b=f(v,1),f(u,0);g[a]+=[b];gr[b]+=[a]
    else:
     a,b=f(u,0),f(v,1);g[a]+=[b];gr[b]+=[a]
     a,b=f(v,0),f(u,1);g[a]+=[b];gr[b]+=[a]
 vis=[0]*N;ord=[]
 def dfs(u):vis[u]=1;[dfs(v)for v in g[u]if not vis[v]];ord.append(u)
 for i in range(N):dfs(i)if not vis[i]else 0
 comp=[-1]*N;c=0
 def rdfs(u):comp[u]=c;[rdfs(v)for v in gr[u]if comp[v]<0]
 for u in ord[::-1]:rdfs(u)if comp[u]<0 else 0;c+=1
 print("Yes"if all(comp[f(i,0)]!=comp[f(i,1)]for i in range(n))else"No")
