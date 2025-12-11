import heapq as h
for _ in range(int(input())):
    n,m=map(int,input().split())
    g=[[]for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,input().split())
        g[u]+=[v];g[v]+=[u]
    q=[(0,0,1)]
    v=[set()for _ in range(n+1)]
    while q:
        t,w,u=h.heappop(q)
        if u==n:
            print(t,w)
            break
        if t in v[u]:continue
        v[u].add(t)
        h.heappush(q,(t+1,w+1,u))
        d=len(g[u])
        if d:
            h.heappush(q,(t+1,w,g[u][t%d]))