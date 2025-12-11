for _ in range(int(input())):
    n,k=map(int,input().split());s=input();o=s.count('1')
    if o<=k:print('Alice');continue
    z,r=0,0
    for c in s:
        if c<'1':r+=1
        else:r=0
        if r>=k:z=1;break
    print('Bob'if z or 2*k<=n else'Alice')