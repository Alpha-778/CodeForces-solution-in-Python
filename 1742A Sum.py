t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b,c=rec[i]
    if a+b==c or a+c==b or b+c==a:
        print("YES")
    else:
        print("NO")