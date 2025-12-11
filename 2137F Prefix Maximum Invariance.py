import sys
r = sys.stdin.buffer.read().split()
it = iter(r)
T = int(next(it))
class BIT:
    def __init__(s, n):
        s.n = n
        s.v = [0]*(n+1)
    def upd(s, i, x):
        while i <= s.n:
            s.v[i] = max(s.v[i], x)
            i += i & -i
    def qry(s, i):
        res = 0
        while i:
            res = max(res, s.v[i])
            i -= i & -i
        return res
out = []
for _ in range(T):
    n = int(next(it))
    a = [0]+[int(next(it)) for _ in range(n)]
    b = [0]+[int(next(it)) for _ in range(n)]
    mx = max(max(a), max(b))
    prev = [0]*(n+1)
    stk = []
    for i in range(1, n+1):
        while stk and a[stk[-1]] < a[i]:
            stk.pop()
        prev[i] = stk[-1] if stk else 0
        stk.append(i)
    bit = BIT(mx)
    s = [0]*(n+1)
    for k in range(1, n+1):
        bit.upd(mx - a[k] + 1, k)
        idx = mx - b[k] + 1
        s[k] = bit.qry(idx) if b[k] <= mx else 0
    ans = 0
    for k in range(1, n+1):
        r = n - k + 1
        inc = (k - prev[k]) if a[k] == b[k] else 0
        non = min(prev[k], s[k])
        ans += r * (inc + non)
    out.append(str(ans))
sys.stdout.write('\n'.join(out)+'\n')