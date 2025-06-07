t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    p = 2
    while p <= n and n % p == 0:
        cnt += 1
        p += 1
    print(cnt)