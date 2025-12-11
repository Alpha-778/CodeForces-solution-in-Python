t = int(input())
for _ in range(t):
    n = int(input())
    y, r = map(int, input().split())
    s = r + y // 2
    if s > n:
        s = n
    print(s)