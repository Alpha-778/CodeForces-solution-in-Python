import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    P=[0]
    for x in a:
        P.append(P[-1]+x)
    if k%2==0:
        z=a[0]
        cur=0
        for x in a:
            cur=x if cur+x<x else cur+x
            z=cur if cur>z else z
        print(z)
    else:
        r=[0]*n
        r[-1]=P[n]
        for i in range(n-2,-1,-1):
            v=P[i+1]
            r[i]=v if v>r[i+1] else r[i+1]
        l=[0]*n
        l[0]=P[0]
        for i in range(1,n):
            v=P[i]
            l[i]=v if v<l[i-1] else l[i-1]
        s=-10**30
        for i in range(n):
            m=r[i]-l[i]+b[i]
            if m>s: s=m
        print(s)