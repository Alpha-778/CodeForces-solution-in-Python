t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    p = list(range(n+1))
    p[r] = l - 1
    a = []
    for i in range(1, n+1):
        a.append(str(p[i-1] ^ p[i]))
    print(" ".join(a))