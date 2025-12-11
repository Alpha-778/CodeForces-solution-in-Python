for _ in range(int(input())):
    n,l,r,k=map(int,input().split())
    if n==1: print(l)
    elif n&1:
        print(l if k<=n else -1)
    elif n==2: print(-1)
    else:
        x=l
        while 1:
            for i in range(64):
                b=1<<i
                if l&b and x&b:
                    x=(x+b)&~(b-1)
                    break
            else: break
        print(-1 if x>r else l if k<=n-2 else x)