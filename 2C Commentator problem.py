def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def gao(xx, yy, x, y, r):
    a = [dist(xx, yy, x[i], y[i]) / r[i] for i in range(3)]
    av = sum(a) / 3
    res = sum((a[i] - av) ** 2 for i in range(3))
    return res / 3

import math
x = []
y = []
r = []
for _ in range(3):
    line = input().split()
    x.append(float(line[0]))
    y.append(float(line[1]))
    r.append(float(line[2]))
xx = sum(x) / 3
yy = sum(y) / 3
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
eps = 1e-5
t = 1
while t > eps:
    cur = gao(xx, yy, x, y, r)
    f = False
    for i in range(4):
        new_xx = xx + dx[i] * t
        new_yy = yy + dy[i] * t
        if gao(new_xx, new_yy, x, y, r) < cur:
            xx = new_xx
            yy = new_yy
            f = True
            break
    if not f:
        t *= 0.5
if gao(xx, yy, x, y, r) < eps:
    print(f"{xx} {yy}")