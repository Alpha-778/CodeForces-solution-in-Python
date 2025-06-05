t = int(input())
rec=[list(map(int, input().split())) for i in range(t)]
for _ in range(t):
    x, y, n = rec[_]
    k = n - (n - y) % x
    print(k)