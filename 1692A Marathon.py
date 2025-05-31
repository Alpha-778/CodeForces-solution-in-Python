t = int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a, b, c, d = rec[i]
    cnt = 0
    for x in [b, c, d]:
        if x > a:
            cnt += 1
    print(cnt)