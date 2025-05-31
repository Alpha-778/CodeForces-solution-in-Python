t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    l=rec[i]
    a,b=int(l[0]),int(l[1])
    print(a+b)