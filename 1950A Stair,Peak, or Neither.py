t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b,c=rec[i]
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")