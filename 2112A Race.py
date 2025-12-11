t = int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for _ in range(t):
    a, x, y = rec[_]
    d1 = abs(a - x)
    d2 = abs(a - y)
    found = False
    for b in range(1, 101):
        if b == a:
            continue
        if abs(b - x) < d1 and abs(b - y) < d2:
            found = True
            break
    print("YES" if found else "NO")