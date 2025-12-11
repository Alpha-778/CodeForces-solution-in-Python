t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ok = True
    for k in range(n, 0, -1):
        placed = False
        for start in range(n - k + 1):
            good = True
            for i in range(start, start + k):
                if a[i] <= 0:
                    good = False
                    break
            if good:
                for i in range(start, start + k):
                    a[i] -= 1
                placed = True
                break
        if not placed:
            ok = False
            break
    print("YES" if ok else "NO")