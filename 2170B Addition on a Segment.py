t = int(input())
rec=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n,a])
for _ in range(t):
    n,a=rec[_]
    s = 0
    c = 0
    for x in a:
        s += x
        if x > 0:
            c += 1
    v1 = n
    v2 = s - n + 1
    v3 = c
    print(min(v1, v2, v3))