import sys
def g(k, L, R):
    if k == 0:
        return 0, 0, 0
    l = (L == 'I')
    r = (R == 'X' or R == 'V')
    if l and r:
        a = k // 2
        b = (k + 1) // 2
        c = k // 2 + 1
    elif l and not r:
        if k % 2 != 0:
            a = (k - 1) // 2
            b = (k - 1) // 2
            c = (k + 1) // 2
        else:
            a = (k - 2) // 2
            b = k // 2
            c = k // 2
    elif (not l) and r:
        if k % 2 != 0:
            a = (k + 1) // 2
            b = (k + 1) // 2
            c = (k + 1) // 2
        else:
            a = k // 2
            b = k // 2 + 1
            c = k // 2
    else:
        a = k // 2
        b = (k + 1) // 2
        c = k // 2
    return a, b, c
def solve(it):
    n = int(next(it))
    q = int(next(it))
    s = next(it)
    base = 0
    front = 0
    ques = 0
    for i, ch in enumerate(s):
        if ch == 'X':
            base += 10
        elif ch == 'V':
            base += 5
        elif ch == 'I':
            base += 1
        else:
            ques += 1
        if i + 1 < n and ch == 'I' and (s[i + 1] == 'X' or s[i + 1] == 'V'):
            front += 1
    p = 'X' + s + 'I'
    fixed = []
    for i, ch in enumerate(p):
        if ch != '?':
            fixed.append(i)
    tpmin = 0
    tpmax = 0
    tmax = 0
    for j in range(len(fixed) - 1):
        i1 = fixed[j]
        i2 = fixed[j + 1]
        k = i2 - i1 - 1
        if k > 0:
            a, b, c = g(k, p[i1], p[i2])
            tpmin += a
            tpmax += b
            tmax += c
    ans = []
    for _ in range(q):
        cx = int(next(it))
        cv = int(next(it))
        ci = int(next(it))
        use_i = min(ques, ci)
        rem = ques - use_i
        use_v = min(rem, cv)
        use_x = rem - use_v
        if use_i < tpmin:
            cur = tmax - (tpmin - use_i)
        elif use_i > tpmax:
            cur = tmax - (use_i - tpmax)
        else:
            cur = tmax
        total = front + cur
        val = base + use_i + use_v * 5 + use_x * 10 - 2 * total
        ans.append(str(val))
    return '\n'.join(ans)
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(solve(it))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()