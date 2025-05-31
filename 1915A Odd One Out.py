t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b,c=rec[i]
    if a==b:
        print(c)
    elif a==c:
        print(b)
    elif b==c:
        print(a)