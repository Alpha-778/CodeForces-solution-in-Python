import math
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    g = b[0]
    for x in b[1:]: g = math.gcd(g, x)
    a = [x // g for x in b]
    l = 1
    for i in range(n - 1):
        d = math.gcd(a[i], a[i+1])
        q = a[i] // d
        if q != 1: l = l * q // math.gcd(l, q)
    print(l)