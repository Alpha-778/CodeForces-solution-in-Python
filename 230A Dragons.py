s,n=map(int,input().split())
dragons=[list(map(int,input().split())) for i in range(0,n)]

dragons.sort()

for x, y in dragons:
    if s > x:
        s += y
    else:
        print("NO")
        break
else:
    print("YES")