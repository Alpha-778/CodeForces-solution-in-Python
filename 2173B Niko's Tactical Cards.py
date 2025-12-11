t=int(input())
NEG=-(1<<60)
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p=0
    q=NEG
    for i in range(n-1,-1,-1):
        po=p
        qo=q
        p=max(po-a[i],qo-b[i])
        q=max(qo+a[i],po+b[i])
    print(max(p,q))