for _ in range(int(input())):
    n, s = map(int, input().split())
    ans = 0
    for _ in range(n):
        a, b, x, y = map(int, input().split())
        if a == b and (x - y) % s == 0:
            ans += 1
        elif a != b and (x + y) % s == 0:
            ans += 1
    print(ans)