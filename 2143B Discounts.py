T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()
    total = 0
    used = []
    for x in b:
        if total + x <= n:
            total += x
            used.append(x)
        else:
            break
    ans = 0
    idx = 0
    for x in used:
        if x == 1:
            idx += 1
        else:
            for t in range(x - 1):
                ans += a[idx + t]
            idx += x
    for i in range(idx, n):
        ans += a[i]
    print(ans)