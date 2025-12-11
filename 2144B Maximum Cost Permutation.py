t = int(input())
rec = []
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    rec.append([n, p])
for i in range(t):
    n, p = rec[i]
    a = [0] + p
    pr = [0] * (n + 1)
    fx = [0] * (n + 1)
    z = 0
    for j in range(1, n + 1):
        if a[j] == 0:
            z += 1
        elif 1 <= a[j] <= n:
            pr[a[j]] = 1
    for j in range(1, n + 1):
        if a[j] == j:
            fx[j] = 1
    bol = False
    zi = -1
    miss = -1
    if z == 1:
        for j in range(1, n + 1):
            if a[j] == 0:
                zi = j
                break
        for v in range(1, n + 1):
            if pr[v] == 0:
                miss = v
                break
        if zi == miss:
            bol = True
    L = 1
    while L <= n and (fx[L] or (bol and L == zi)):
        L += 1
    if L > n:
        print(0)
        continue
    R = n
    while R >= 1 and (fx[R] or (bol and R == zi)):
        R -= 1
    print(R - L + 1)