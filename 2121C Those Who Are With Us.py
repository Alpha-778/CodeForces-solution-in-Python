t=int(input())
rec=[]
for _ in range(t):
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for i in range(n)]
    rec.append([n,m,a])
for _ in range(t):
    n,m,a=rec[_]
    r=[0]*n
    c=[0]*m
    f={}
    g=0
    for i in range(n):
        for j in range(m):
            v=a[i][j]
            r[i]=max(r[i],v)
            c[j]=max(c[j],v)
            f[v]=f.get(v,0)+1
            g=max(g,v)
    s=max([k for k in f if k!=g],default=0)
    rg=[0]*n
    cg=[0]*m
    for i in range(n):
        for j in range(m):
            if a[i][j]==g:
                rg[i]+=1
                cg[j]+=1
    ans=1<<30
    for i in range(n):
        for j in range(m):
            x=rg[i]+cg[j]-(a[i][j]==g)
            if x==f[g]:
                newg=max(s,max(r[i],c[j])-1)
            else:
                newg=max(g,max(r[i],c[j])-1)
            ans=min(ans,newg)
    print(ans)
