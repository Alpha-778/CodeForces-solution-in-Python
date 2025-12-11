t = int(input())
rec = [list(map(int, input().split())) for i in range(t)]
for i in range(t):
    n, m = rec[i]
    if m < n or m > n*(n+1)//2:
        print(-1); continue
    r = -1
    for rt in range(1, n+1):
        rem = m - rt
        lo = n - 1
        hi = (rt-1)*rt//2 + (n-rt)*rt
        if lo <= rem <= hi:
            r = rt; break
    if r == -1: print(-1); continue
    A = sorted([(min(i, r)-1, i) for i in range(1, n+1) if i != r], reverse=1)
    delta = m - r - (n-1)
    con = [0]*(n+1)
    for g, x in A:
        if delta >= g:
            con[x] = 1; delta -= g
    if delta: print(-1); continue
    u = [0]*(n+1); u[r] = 1; E = []
    p = 1 if r != 1 else 2
    if n > 1: E.append((r, p)); u[p] = 1
    for j in range(1, n+1):
        if j != r and con[j] and not u[j]:
            E.append((r, j)); u[j] = 1
    for j in range(1, n+1):
        if j != r and not u[j]:
            E.append((p, j)); u[j] = 1
    print(r)
    for a, b in E: print(a, b)
