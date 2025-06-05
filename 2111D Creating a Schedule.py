t = int(input())
rec=[]
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    rec.append([n,m,a])
for _ in range(t):
    n,m,a=rec[_]
    v = []
    for x in a:
        f = x // 100
        v.append((f, x))
    v.sort(key=lambda x: (x[0], x[1]))
    fl = [x[0] for x in v]
    id_ = [x[1] for x in v]
    T = [abs(fl[i] - fl[m - 1 - i]) for i in range(n)]
    P = [0] * (n + 1)
    for i in range(1, n + 1):
        P[i] = P[i - 1] + T[i - 1]
    best = -1
    bk = 0
    for k in range(n + 1):
        val = P[k] + P[n - k]
        if val > best:
            best = val
            bk = k
    k = bk
    A = []
    B = []
    A.extend(id_[:k])
    A.extend(id_[m - (n - k):m])
    B.extend(id_[:n - k])
    B.extend(id_[m - k:m])
    for i in range(n):
        ar = A[i]
        br = B[n - 1 - i]
        line = []
        for j in range(6):
            if j % 2 == 0:
                line.append(str(ar))
            else:
                line.append(str(br))
        print(' '.join(line))