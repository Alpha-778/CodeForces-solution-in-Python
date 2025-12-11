import sys
def mex(cnt):
    m = 0
    while m < len(cnt) and cnt[m]: m += 1
    return m
def step(a):
    n = len(a)
    c = [0]*(n+2)
    for x in a:
        if x <= n: c[x] += 1
    M = mex(c)
    return [x if x < M and c[x] == 1 else M for x in a]
data = list(map(int, sys.stdin.read().split()))
it = iter(data)
t = next(it)
res = []
for _ in range(t):
    n,k = next(it), next(it)
    a = [next(it) for _ in range(n)]
    if not k:
        res.append(str(sum(a)))
        continue
    seen = {tuple(a): 0}
    seq = [tuple(a)]
    cur = a
    for step_num in range(1, k+1):
        nxt = step(cur)
        t_nxt = tuple(nxt)
        if t_nxt in seen:
            cycle = seq[seen[t_nxt]:]
            rem = (k - step_num) % len(cycle)
            res.append(str(sum(cycle[rem])))
            break
        seen[t_nxt] = step_num
        seq.append(t_nxt)
        cur = nxt
    else:
        res.append(str(sum(cur)))
print("\n".join(res))