import sys
from collections import deque
data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
t = next(it)
ans = []
for _ in range(t):
    n, m, q = next(it), next(it), next(it)
    e = [[] for _ in range(n)]
    re = [[] for _ in range(n)]
    ind = [0]*n
    out = [0]*n
    for _ in range(m):
        u, v = next(it)-1, next(it)-1
        e[u].append(v)
        re[v].append(u)
        ind[v] += 1
        out[u] += 1
    dq = deque(i for i in range(n) if ind[i]==0)
    order = []
    while dq:
        x = dq.popleft()
        order.append(x)
        for y in e[x]:
            ind[y] -= 1
            if ind[y]==0:
                dq.append(y)
    red = [0]*n
    dp0 = [0]*n
    dp1 = [0]*n
    for x in reversed(order):
        if red[x]:
            dp0[x] = dp1[x] = 0
        elif out[x]==0:
            dp0[x] = dp1[x] = 1
        else:
            dp0[x] = 1 if any(dp1[y] for y in e[x]) else 0
            dp1[x] = 1 if all(dp0[y] for y in e[x]) else 0
    good = [0]*n
    bad = [0]*n
    redc = [0]*n
    for x in range(n):
        good[x] = sum(1 for y in e[x] if not red[y] and dp1[y])
        bad[x] = sum(1 for y in e[x] if not red[y] and dp0[y]==0)
    def calc(x):
        if red[x]:
            return 0,0
        if out[x]==0:
            return 1,1
        return (1 if good[x]>0 else 0, 1 if redc[x]==0 and bad[x]==0 else 0)
    for _ in range(q):
        ty, x = next(it), next(it)-1
        if ty == 1:
            if red[x]:
                continue
            od0, od1 = dp0[x], dp1[x]
            red[x] = 1
            dp0[x] = dp1[x] = 0
            queue = deque()
            for p in re[x]:
                if od1: good[p] -= 1
                if od0==0: bad[p] -= 1
                redc[p] += 1
                queue.append(p)
            while queue:
                v = queue.popleft()
                if red[v]: continue
                od0, od1 = dp0[v], dp1[v]
                nd0, nd1 = calc(v)
                if od0==nd0 and od1==nd1: continue
                dp0[v], dp1[v] = nd0, nd1
                for p in re[v]:
                    if od1==1 and nd1==0: good[p] -= 1
                    if od1==0 and nd1==1: good[p] += 1
                    if od0==0 and nd0==1: bad[p] -= 1
                    if od0==1 and nd0==0: bad[p] += 1
                    queue.append(p)
        else:
            ans.append("YES\n" if dp0[x] else "NO\n")
sys.stdout.write(''.join(ans))