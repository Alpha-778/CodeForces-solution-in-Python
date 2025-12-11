import sys
from collections import deque

sys.setrecursionlimit(10**7)

MOD = 998244353

data = sys.stdin.read().strip().split()
t_index = 0
def nxt():
    global t_index
    val = data[t_index]
    t_index += 1
    return val

T = int(nxt())
for _ in range(T):
    n = int(nxt())
    m = int(nxt())
    V = int(nxt())
    a = [-1] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(nxt())

    g = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(nxt())
        v = int(nxt())
        edges.append((u, v))
        g[u].append((v, i))
        g[v].append((u, i))

    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    isBridge = [0] * m
    timer = [0]

    def dfs(v, pe):
        tin[v] = timer[0]
        low[v] = timer[0]
        timer[0] += 1
        for to, ei in g[v]:
            if ei == pe:
                continue
            if tin[to] != -1:
                if tin[to] < low[v]:
                    low[v] = tin[to]
            else:
                dfs(to, ei)
                if low[to] < low[v]:
                    low[v] = low[to]
                if low[to] > tin[v]:
                    isBridge[ei] = 1

    for i in range(1, n + 1):
        if tin[i] == -1:
            dfs(i, -1)

    comp = [-1] * (n + 1)
    compCnt = 0
    compNodesCount = []
    compEdgesCount = []
    for i in range(1, n + 1):
        if comp[i] != -1:
            continue
        idd = compCnt
        compCnt += 1
        nodes = 0
        edgesInside = 0
        st = [i]
        comp[i] = idd
        while st:
            u = st.pop()
            nodes += 1
            for v, ei in g[u]:
                if isBridge[ei]:
                    continue
                if u < v:
                    edgesInside += 1
                if comp[v] == -1:
                    comp[v] = idd
                    st.append(v)
        compNodesCount.append(nodes)
        compEdgesCount.append(edgesInside)

    color = [-1] * (n + 1)
    compHasCycle = [0] * compCnt
    compIsBip = [1] * compCnt

    for idx in range(compCnt):
        if compEdgesCount[idx] > 0:
            compHasCycle[idx] = 1

    for s in range(1, n + 1):
        if color[s] != -1:
            continue
        cid = comp[s]
        q = deque()
        q.append(s)
        color[s] = 0
        while q:
            u = q.popleft()
            for v, ei in g[u]:
                if isBridge[ei]:
                    continue
                if comp[v] != cid:
                    continue
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                else:
                    if color[v] == color[u]:
                        compIsBip[cid] = 0

    ans = 1
    bad = False
    seenValue = [0] * compCnt
    forcedValue = [-1] * compCnt
    for v in range(1, n + 1):
        cid = comp[v]
        if a[v] != -1:
            if not seenValue[cid]:
                seenValue[cid] = 1
                forcedValue[cid] = a[v]
            else:
                if forcedValue[cid] != a[v]:
                    bad = True
                    break
    if bad:
        print(0)
        continue

    for idx in range(compCnt):
        if not compHasCycle[idx]:
            if seenValue[idx]:
                pass
            else:
                for _ in range(compNodesCount[idx]):
                    ans = (ans * (V % MOD)) % MOD
        else:
            if not compIsBip[idx]:
                if seenValue[idx]:
                    if forcedValue[idx] != 0:
                        bad = True
                        break
                else:
                    pass
            else:
                if seenValue[idx]:
                    pass
                else:
                    ans = (ans * (V % MOD)) % MOD

    if bad:
        print(0)
    else:
        print(ans % MOD)