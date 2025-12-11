from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    g = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(n - 1):
        u, v, x, y = map(int, input().split())
        if x > y:
            g[u].append(v)
            indeg[v] += 1
        else:
            g[v].append(u)
            indeg[u] += 1
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for w in g[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    p = [0] * (n + 1)
    cur = n
    for v in order:
        p[v] = cur
        cur -= 1
    print(' '.join(str(p[i]) for i in range(1, n + 1)))