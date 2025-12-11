t=int(input())
rec=[]
for _ in range(t):
    n=int(input())
    b=[0]+list(map(int,input().split()))
    rec.append([n,b])
for _ in range(t):
    n,b=rec[_]
    a=[0]*(n+1)
    p=0
    q=0
    for i in range(1,n+1):
        g=b[i]-p
        p=b[i]
        r=i-int(g)
        if r==0:
            q+=1
            a[i]=q
        else:
            a[i]=a[r]
    print(*a[1:])