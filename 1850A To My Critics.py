t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b,c=rec[i]
    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        print("YES")
    else:
        print("NO")