import sys
data = sys.stdin.buffer.read().split()
it = iter(data)
t = int(next(it))
ans = []
for _ in range(t):
    n = int(next(it))
    k = int(next(it))
    a = []
    M = 0
    for _ in range(n):
        x = int(next(it))
        a.append(x)
        if x > M:
            M = x
    p = set(a)
    v = sorted(p)
    s = []
    for val in v:
        if k // val != M // val:
            continue
        ok = True
        m = val
        while m <= M:
            if m not in p:
                ok = False
                break
            if m > M - val:
                break
            m += val
        if ok:
            s.append(val)
    c = {}
    for x in v:
        c[x] = False
    for x in s:
        m = x
        while m <= M:
            if m in p:
                c[m] = True
            if m > M - x:
                break
            m += x
    poss = True
    for x in v:
        if not c[x]:
            poss = False
            break
    if not poss:
        ans.append("-1\n")
        continue
    s.sort()
    d = {}
    for x in v:
        d[x] = False
    r = []
    for x in s:
        if not d[x]:
            r.append(x)
            m = x
            while m <= M:
                if m in p:
                    d[m] = True
                if m > M - x:
                    break
                m += x
    ans.append(str(len(r)) + "\n")
    if r:
        ans.append(" ".join(str(x) for x in r) + "\n")
    else:
        ans.append("\n")
sys.stdout.write("".join(ans))