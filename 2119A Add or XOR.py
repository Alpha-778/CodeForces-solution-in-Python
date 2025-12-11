import heapq as h
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    d=[1e9]*101;d[a]=0;q=[(0,a)]
    while q:
        c,u=h.heappop(q)
        if u==b:break
        for v,w in ((u+1,x),(u^1,y)):
            if v<101 and d[v]>c+w:
                d[v]=c+w;h.heappush(q,(d[v],v))
    print(-1 if d[b]==1e9 else d[b])