import sys
it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
INF = 10 ** 30
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    pref_min = [0] * n
    pref_sum = [0] * n
    m = a[0]
    s = a[0]
    pref_min[0] = m
    pref_sum[0] = s
    for i in range(1, n):
        m = m if m < a[i] else a[i]
        s += m
        pref_min[i] = m
        pref_sum[i] = s
    ans = s     
    for i in range(n - 1):
        prev_min  = pref_min[i - 1] if i else INF
        prev_sum  = pref_sum[i - 1] if i else 0
        cand = prev_sum + (prev_min if prev_min < a[i] + a[i+1] else a[i] + a[i+1])
        if cand < ans:
            ans = cand
    out.append(str(ans))
sys.stdout.write("\n".join(out))