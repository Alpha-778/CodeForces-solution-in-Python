MOD = 1000000007
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    MAX = n
    cur = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    cur[0][0] = 1
    for val in a:
        nxt = [row[:] for row in cur]
        for x in range(MAX + 1):
            for y in range(MAX + 1):
                ways = cur[x][y]
                if ways == 0:
                    continue
                if val >= x:
                    nxt[val][y] = (nxt[val][y] + ways) % MOD
                elif val >= y:
                    nxt[x][val] = (nxt[x][val] + ways) % MOD
        cur = nxt
    ans = 0
    for x in range(MAX + 1):
        for y in range(MAX + 1):
            ans = (ans + cur[x][y]) % MOD
    print(ans)