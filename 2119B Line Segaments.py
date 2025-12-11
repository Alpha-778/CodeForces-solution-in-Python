def f():
    n=int(input())
    px,py,qx,qy=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    m=max(a) if a else 0
    dx,dy=px-qx,py-qy
    d2=dx*dx+dy*dy
    r2=s*s
    x=max(0,m-(s-m)) if n else 0
    print('Yes' if x*x<=d2<=r2 else 'No')
for _ in range(int(input())):f()