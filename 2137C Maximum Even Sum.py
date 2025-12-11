a=input; t=int(a())
r=[]
for _ in range(t):
    x,y=map(int,a().split())
    p=x*y
    if p%2:
        r.append(str(p+1))
    else:
        if y%2 and x%2==0 or x%2 and y%4==2:
            r.append("-1")
        else:
            r.append(str(p//2+2))
print('\n'.join(r))