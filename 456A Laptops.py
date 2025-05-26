n=int(input())
rec=[list(map(int,input().split())) for i in range(n)]
rec.sort()
for i in range(n - 1):
    if rec[i][1] > rec[i + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")