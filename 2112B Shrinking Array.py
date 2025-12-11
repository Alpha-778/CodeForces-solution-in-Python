import sys
r=sys.stdin.readline
for _ in range(int(r())):
    r();a=list(map(int,r().split()))
    if any(abs(x-y)<2 for x,y in zip(a,a[1:])):
        print(0);continue
    ans=-1
    for i,(x,y) in enumerate(zip(a,a[1:])):
        lo,hi=sorted((x,y))
        for v in ((a[i-1] if i>0 else 10**18),(a[i+2] if i+2<len(a) else 10**18)):
            if hi>=v-1 and lo<=v+1:
                ans=1;break
        if ans>0:break
    print(ans)