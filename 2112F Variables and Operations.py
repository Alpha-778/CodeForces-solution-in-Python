import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, _ = map(int, input().split())
    g[v-1].append(v := u-1)

d = [0]*n; l = [0]*n; s = []; o = [0]*n; i2c = [-1]*n; com = []; t = c = 0
def f(u):
    global t, c
    t += 1; d[u] = l[u] = t; s.append(u); o[u] = 1
    for v in g[u]:
        if not d[v]: f(v); l[u] = min(l[u], l[v])
        elif o[v]: l[u] = min(l[u], d[v])
    if d[u] == l[u]:
        x = []; c += 1
        while 1:
            z = s.pop(); o[z] = 0; i2c[z] = c-1; x += [z]
            if z == u: break
        com += [x]

cyc = [0]*c
for i in range(n):
    if not d[i]: f(i)
for j in range(c):
    u = com[j][0]
    if len(com[j]) > 1 or u in g[u]: cyc[j] = 1

for _ in range(int(input())):
    k = int(input()); _ = input()
    print(''.join(['1' if cyc[i2c[i]] and k else '0' for i in range(n)]))
