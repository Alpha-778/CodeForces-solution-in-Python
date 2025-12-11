T=int(input())
for _ in range(T):
    n=int(input())
    g=[[]for _ in range(n+1)]
    for i in range(n-1):
        u,v=map(int,input().split())
        g[u]+=[(v,i)]
        g[v]+=[(u,i)]
    p=-1
    for i in range(1,n+1):
        if len(g[i])==2:
            p=i
            break
    if p==-1:
        print("NO")
        continue
    a,id1=g[p][0]
    b,id2=g[p][1]
    vis=[0]*(n-1)
    vis[id1]=vis[id2]=1
    ans=[(a,p),(p,b)]
    stk=[(a,p,1),(b,p,0)]
    while stk:
        u,par,s=stk.pop()
        for v,eid in g[u]:
            if vis[eid]: continue
            vis[eid]=1
            if s:
                ans.append((u,v))
                stk.append((v,u,0))
            else:
                ans.append((v,u))
                stk.append((v,u,1))
    print("YES")
    for x,y in ans:print(x,y)