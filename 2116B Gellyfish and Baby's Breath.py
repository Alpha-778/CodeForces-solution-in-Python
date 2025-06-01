MOD = 998244353
pow2 = [1]
t = int(input())
rec=[]
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    rec.append([n,p,q])
for i in range(t):
    n,p,q=rec[i]
    posP = [0] * n
    posQ = [0] * n
    for i in range(n):
        posP[p[i]] = i
    for i in range(n):
        posQ[q[i]] = i
    if len(pow2) <= n:
        old_len = len(pow2)
        for i in range(old_len, n + 1):
            pow2.append((pow2[i - 1] * 2) % MOD)
    Pmax = [0] * n
    Qmax = [0] * n
    Pmax[0] = p[0]
    Qmax[0] = q[0]
    for i in range(1, n):
        Pmax[i] = max(Pmax[i - 1], p[i])
        Qmax[i] = max(Qmax[i - 1], q[i])
    r = [0] * n
    for i in range(n):
        e = max(Pmax[i], Qmax[i])
        if Pmax[i] > Qmax[i]:
            j = posP[e]
            k = i - j
            s = q[k]
        elif Qmax[i] > Pmax[i]:
            k = posQ[e]
            j = i - k
            s = p[j]
        else:
            j1 = posP[e]
            k1 = i - j1
            s1 = q[k1] if 0 <= k1 < n else -1
            k2 = posQ[e]
            j2 = i - k2
            s2 = p[j2] if 0 <= j2 < n else -1
            s = max(s1, s2)
        val = (pow2[e] + pow2[s]) % MOD
        r[i] = val
    print(" ".join(map(str, r)))