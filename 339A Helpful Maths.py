l=input().split("+")
l=list(map(int,l))
l.sort()
if len(l)==1:
    print(*l)
else:
    for i in range(0,len(l)-1):
        print(l[i],end="+")
    print(l[-1])
