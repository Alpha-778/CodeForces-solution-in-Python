t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n, a])
for _ in range(t):
    n, a = rec[_]
    diff = a[1] - a[0]
    arithmetic = True
    for i in range(2, n):
        if a[i] - a[i - 1] != diff:
            arithmetic = False
            break
    if not arithmetic:
        print("NO")
        continue
    c = a[0] - diff
    if c < 0 or c % (n + 1) != 0:
        print("NO")
        continue
    y = c // (n + 1)
    x = y + diff
    if x < 0 or y < 0:
        print("NO")
        continue
    print("YES")