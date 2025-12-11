import sys

sys.setrecursionlimit(1000000)
inp = sys.stdin.readline
out = sys.stdout

t = int(inp())
for _ in range(t):
    n = int(inp())
    p = [0] * (n + 1)
    vals = []
    while len(vals) < n:
        line = inp().split()
        if not line:
            break
        for x in line:
            vals.append(int(x))
    for i in range(1, n + 1):
        p[i] = vals[i - 1]

    def sort_sub(l, r):
        if l >= r:
            return

        def find_pos(val):
            j = l
            while j <= r:
                if p[j] == val:
                    return j
                j += 1
            return -1

        while p[l] != l:
            pos = find_pos(l)
            print("?", l, pos)
            out.flush()
            s = inp().split()
            if not s:
                sys.exit(0)
            u = int(s[0])
            v = int(s[1])
            if u == -1:
                sys.exit(0)
            p[u], p[v] = p[v], p[u]

        while p[r] != r:
            pos = find_pos(r)
            print("?", r, pos)
            out.flush()
            s = inp().split()
            if not s:
                sys.exit(0)
            u = int(s[0])
            v = int(s[1])
            if u == -1:
                sys.exit(0)
            p[u], p[v] = p[v], p[u]

        safety = 0
        while (p[l] != l or p[r] != r) and safety < 100:
            safety += 1
            if p[l] != l:
                while p[l] != l:
                    pos = find_pos(l)
                    print("?", l, pos)
                    out.flush()
                    s = inp().split()
                    if not s:
                        sys.exit(0)
                    u = int(s[0])
                    v = int(s[1])
                    if u == -1:
                        sys.exit(0)
                    p[u], p[v] = p[v], p[u]
            else:
                while p[r] != r:
                    pos = find_pos(r)
                    print("?", r, pos)
                    out.flush()
                    s = inp().split()
                    if not s:
                        sys.exit(0)
                    u = int(s[0])
                    v = int(s[1])
                    if u == -1:
                        sys.exit(0)
                    p[u], p[v] = p[v], p[u]

        sort_sub(l + 1, r - 1)

    sort_sub(1, n)
    print("!")
    out.flush()