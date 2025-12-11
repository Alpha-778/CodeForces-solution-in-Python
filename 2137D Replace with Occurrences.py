import sys
r = iter(sys.stdin.read().split())
for _ in range(int(next(r))):
    n = int(next(r))
    b = [int(next(r)) for _ in range(n)]
    p = [[] for _ in range(n+1)]
    for i, x in enumerate(b):
        p[x].append(i)
    a = [0]*n
    label = 1
    ok = True
    for v in range(1, n+1):
        c = len(p[v])
        if c and c % v:
            ok = False
            break
        for i in range(0, c, v):
            for idx in p[v][i:i+v]:
                a[idx] = label
            label += 1
    print(-1 if not ok else ' '.join(map(str, a)))