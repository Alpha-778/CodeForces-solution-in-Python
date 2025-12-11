import sys
it = iter(sys.stdin.buffer.read().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it)); k = int(next(it))
    q = [int(next(it)) for _ in range(n)]
    r = [int(next(it)) for _ in range(n)]
    q.sort()
    x = []
    for v in r:
        if v < k:
            d = v + 1
            u = (k - v) // d
            if u >= 1:
                x.append(u)
    x.sort()
    ans = 0
    j = len(q) - 1
    for v in reversed(x):
        while j >= 0 and q[j] > v:
            j -= 1
        if j < 0:
            break
        ans += 1
        j -= 1
    out.append(str(ans))
sys.stdout.write("\n".join(out))