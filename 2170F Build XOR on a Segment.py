import sys
data = sys.stdin.read().strip().split()
it = iter(data)
n = int(next(it))
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(next(it))
m = int(next(it))
qs = [[] for _ in range(n + 1)]
for idx in range(m):
    l = int(next(it))
    r = int(next(it))
    x = int(next(it))
    qs[r].append((l, x, idx))
B = 4096
C = 13
dp = [[0] * B for _ in range(C)]
ans = [0] * m
for i in range(1, n + 1):
    v = arr[i]
    for k in range(12, 1, -1):
        prev_row = dp[k - 1]
        cur_row = dp[k]
        for u in range(B):
            val = prev_row[u]
            if val > 0:
                nv = u ^ v
                if val > cur_row[nv]:
                    cur_row[nv] = val
    dp[1][v] = i
    for l, x, idx in qs[i]:
        f = 0
        for k in range(1, 13):
            if dp[k][x] >= l:
                f = k
                break
        ans[idx] = f
out = sys.stdout.write
for i in range(m):
    out(str(ans[i]) + "\n")