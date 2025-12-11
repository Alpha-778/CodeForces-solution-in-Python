t=int(input())
rec=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    rec.append([n,a])
T=10**18
for _ in range(t):
    n,a=rec[_]
    s=set(a)
    r=T-n
    ok=False
    y=0
    for i in range(2000):
        if r<=0:
            break
        c=len(s)
        if r==1 or c in s:
            y=c
            ok=True
            break
        s.add(c)
        r-=1
    if not ok:
        y=len(s)
    print(y)