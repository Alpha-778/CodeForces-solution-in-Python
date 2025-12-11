import sys
data = list(map(int, sys.stdin.read().split()))
it = iter(data)
try:
    t = next(it)
except StopIteration:
    t = 0
out_lines = []
for _ in range(t):
    n = next(it)
    cnt = [0] * (n + 1)
    for _ in range(n):
        x = next(it)
        if 1 <= x <= n:
            cnt[x] += 1
    ans = 0
    for v in range(1, n + 1):
        ans += (cnt[v] // v) * v
    out_lines.append(str(ans))
sys.stdout.write("\n".join(out_lines))