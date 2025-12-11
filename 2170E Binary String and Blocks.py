import sys
MOD = 998244353
it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    mc = int(next(it))
    m = n - 1
    best = [m + 1] * (m + 2)
    for _ in range(mc):
        l = int(next(it))
        r = int(next(it))
        L = l
        R = r - 1
        if L <= R:
            if R < best[L]:
                best[L] = R
    mn = [m + 1] * (m + 3)
    for i in range(m, 0, -1):
        if best[i] < mn[i + 1]:
            mn[i] = best[i]
        else:
            mn[i] = mn[i + 1]
    mn[m + 1] = m + 1
    diff = [0] * (m + 5)
    dp = [0] * (m + 2)
    cur = 0
    dp[0] = 1
    if m >= 1:
        s = 1
        e = mn[1]
        if e >= s:
            diff[s] = (diff[s] + dp[0]) % MOD
            diff[e + 1] = (diff[e + 1] - dp[0]) % MOD
    for i in range(1, m + 1):
        cur = (cur + diff[i]) % MOD
        dp[i] = cur
        s = i + 1
        if s <= m:
            e = mn[s]
            if e >= s:
                diff[s] = (diff[s] + dp[i]) % MOD
                diff[e + 1] = (diff[e + 1] - dp[i]) % MOD
    waysT = 0
    for j in range(0, m + 1):
        s = j + 1
        if s <= m:
            val = mn[s]
        else:
            val = m + 1
        if val > m:
            waysT = (waysT + dp[j]) % MOD
    ans = (waysT * 2) % MOD
    out.append(str(ans))
sys.stdout.write("\n".join(out))