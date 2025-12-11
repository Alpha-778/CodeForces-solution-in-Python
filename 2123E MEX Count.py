for _ in range(int(input())):
    t=int(input());a=list(map(int,input().split()))
    f=[0]*(t+1)
    for x in a:
       if x<=t:f[x]+=1
    g=[1];[g.append(g[-1]&int(f[i]>0))for i in range(t)]
    d=[0]*(t+2)
    for m in range(t+1):
        if not g[m]:continue
        l,r=f[m],t-m
        if l<=r:d[l]+=1;d[r+1]-=1
    c=0;ans=[]
    for x in d[:t+1]:c+=x;ans.append(c)
    print(*ans)