t = int(input())
rec = []
for _ in range(t):
    n, k = map(int, input().split())
    a0 = list(map(int, input().split()))
    a = [0] * (n + 2)
    for i in range(n):
        a[i + 1] = a0[i]
    P = [[n + 1] * (k + 1) for _ in range(n + 2)]
    for j in range(k + 1):
        P[n + 1][j] = n + 1
    for i in range(n, 0, -1):
        ai = a[i]
        row = P[i]
        nxt = P[i + 1]
        for j in range(k + 1):
            if ai >= j:
                row[j] = i
            else:
                row[j] = nxt[j]
    D = [[[] for _ in range(k + 1)] for _ in range(k + 1)]
    D[0][0].append((0, 0))
    h = 0
    n1 = n + 1
    for c in range(k + 1):
        Dc = D[c]
        for v in range(c + 1):
            lst = Dc[v]
            if not lst:
                continue
            lst.sort()
            f = []
            m = n + 2
            for p, i in lst:
                if i < m:
                    f.append((p, i))
                    m = i
            for p, i in f:
                cur = v * n1 - p
                if cur > h:
                    h = cur
                u = v + 1
                while True:
                    nc = c + u
                    if nc > k:
                        break
                    ni = P[i + 1][u]
                    if ni <= n:
                        D[nc][u].append((p + ni * (u - v), ni))
                        u += 1
                    else:
                        break
    print(h)