import sys
from collections import deque
def bfs(start, g, n):
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    far = max(range(1, n + 1), key=lambda x: dist[x])
    return far, dist, parent
data = sys.stdin.read().strip().split()
it = iter(data)
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(next(it)), int(next(it))
        g[u].append(v)
        g[v].append(u)
    u, _, _ = bfs(1, g, n)
    v, dist_u, parent_u = bfs(u, g, n)
    _, dist_v, parent_v = bfs(v, g, n)
    path = []
    cur = v
    while cur != -1:
        path.append(cur)
        cur = parent_u[cur]
    path_set = set(path)
    dist_to_path = [-1] * (n + 1)
    q = deque()
    for node in path:
        dist_to_path[node] = 0
        q.append(node)
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist_to_path[v] == -1:
                dist_to_path[v] = dist_to_path[u] + 1
                q.append(v)
    c = -1
    best = 10**9
    for i in range(1, n + 1):
        if len(g[i]) == 1 and i not in path_set: 
            if dist_to_path[i] < best:
                best = dist_to_path[i]
                c = i
    if c == -1:
        out.append("-1")
        continue
    for v in g[c]:
        if dist_to_path[v] < dist_to_path[c]:
            b = v
            break
    a = -1
    for v in g[b]:
        if v in path_set:
            a = v
            break
    out.append(f"{a} {b} {c}")
sys.stdout.write("\n".join(out))