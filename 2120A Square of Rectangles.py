from itertools import permutations
def line(r):
    l, b = zip(*r)
    return (b.count(b[0]) == 3 and sum(l) == b[0]) or (l.count(l[0]) == 3 and sum(b) == l[0])
def L(r):
    for x, y, z in permutations(r):
        S = max(x)
        if x[0] == S and y[1] == z[1] and x[1] + max(y[1], z[1]) == S and y[0] + z[0] == S:
            return True
        if x[1] == S and y[0] == z[0] and x[0] + max(y[0], z[0]) == S and y[1] + z[1] == S:
            return True
    return False
t = int(input())
rec = [list(map(int, input().split())) for i in range(t)]
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = rec[_]
    rects = [(l1, b1), (l2, b2), (l3, b3)]
    print("YES" if line(rects) or L(rects) else "NO")