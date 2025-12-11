import sys
def solve_one(n, k):
    b = []
    g = []
    p = 0
    while p < 62 and ((n >> p) & 1) == 0:
        p += 1
    if p == 62:
        return 0
    x = 0
    y = 0
    left = True
    for bit in range(p, 62):
        v = (n >> bit) & 1
        if left:
            if v == 1:
                x += 1
            else:
                b.append(x)
                x = 0
                left = False
                y = 1
        else:
            if v == 0:
                y += 1
            else:
                g.append(y)
                y = 0
                left = True
                x = 1
    m = len(b)
    L = k if k < 70 else 70
    l = int(L)
    d = [[-1, -1] for _ in range(l + 1)]
    d[0][0] = 0
    for i in range(m):
        nd = [[-1, -1] for _ in range(l + 1)]
        s = b[i]
        z = g[i - 1] if i > 0 else 0
        for c in range(l + 1):
            v0 = d[c][0]
            v1 = d[c][1]
            if v0 != -1:
                if nd[c][0] < v0:
                    nd[c][0] = v0
                if c + 1 <= l:
                    val = v0 + s - 1
                    if nd[c + 1][1] < val:
                        nd[c + 1][1] = val
            if v1 != -1:
                if nd[c][0] < v1:
                    nd[c][0] = v1
                if c + 1 <= l:
                    val = v1 + s - 1
                    if nd[c + 1][1] < val:
                        nd[c + 1][1] = val
                if c + z <= l:
                    val = v1 + s
                    if nd[c + z][1] < val:
                        nd[c + z][1] = val
        d = nd
    best = 0
    for c in range(l + 1):
        if d[c][0] > best:
            best = d[c][0]
        if d[c][1] > best:
            best = d[c][1]
    return k + best
def main():
    it = iter(sys.stdin.read().split())
    t = int(next(it))
    ans = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        ans.append(str(solve_one(n, k)))
    sys.stdout.write("\n".join(ans))
if __name__ == "__main__":
    main()