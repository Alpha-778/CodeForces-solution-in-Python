t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    ans = ans1 = x
    N = n
    M = m
    tag = 0

    for _ in range(n):
        if ans > 0:
            ans = ans // 2 + 10
            if ans <= 0:
                tag = 1
                break
    for _ in range(m):
        if ans > 0:
            ans -= 10
            if ans <= 0:
                tag = 1
                break

    for _ in range(M):
        if ans1 > 0:
            ans1 -= 10
            if ans1 <= 0:
                tag = 1
                break
    for _ in range(N):
        if ans1 > 0:
            ans1 = ans1 // 2 + 10
            if ans1 <= 0:
                tag = 1
                break

    print("YES" if tag == 1 else "NO")