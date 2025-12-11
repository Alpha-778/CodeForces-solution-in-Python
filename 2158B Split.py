t = int(input())
rec=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n,a])
for _ in range(t):
    n,a=rec[_]
    f = [0] * (2*n + 1)
    for x in a:
        f[x] += 1
    co = 0
    ce = 0
    for v in f:
        if v > 0:
            if v % 2 == 1:
                co += 1
            else:
                ce += 1
    k = min(ce, n)
    if co == 0:
        if (k % 2) != (n % 2):
            k -= 1
        if k < 0:
            k = 0
    print(co + 2*k)