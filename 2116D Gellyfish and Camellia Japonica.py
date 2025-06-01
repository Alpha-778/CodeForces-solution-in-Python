INF = 10**18
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    b = [0] + list(map(int, input().split()))
    child1 = [0] * (n + q + 1)
    child2 = [0] * (n + q + 1)
    current_node = list(range(n + 1))
    ops = [None] * (q + 1)
    for i in range(1, q + 1):
        x, y, z = map(int, input().split())
        ops[i] = (x, y, z)
        U = n + i
        child1[U] = current_node[x]
        child2[U] = current_node[y]
        current_node[z] = U
    val = [0] * (n + q + 1)
    preset = [False] * (n + q + 1)
    is_root = [False] * (n + q + 1)
    for j in range(1, n + 1):
        r = current_node[j]
        is_root[r] = True
    for j in range(1, n + 1):
        r = current_node[j]
        if not preset[r]:
            val[r] = b[j]
            preset[r] = True
    ok = True
    for u in range(n + q, 0, -1):
        vu = val[u]
        if u > n:
            for c in [child1[u], child2[u]]:
                if val[c] < vu:
                    if preset[c]:
                        ok = False
                        break
                    val[c] = vu
            if not ok:
                break
    if not ok:
        print(-1)
        continue
    for u in range(1, n + q + 1):
        if u > n:
            c1v = val[child1[u]]
            c2v = val[child2[u]]
            want = min(c1v, c2v)
            if preset[u]:
                if val[u] != want:
                    ok = False
                    break
            else:
                val[u] = want
    if not ok:
        print(-1)
        continue
    print(' '.join(map(str, val[1:n+1])))
