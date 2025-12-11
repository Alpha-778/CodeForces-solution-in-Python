from math import isqrt
t = int(input())
N = 10**5
f = list(range(N+1))
for i in range(2, isqrt(N)+1):
    if f[i] == i:
        for j in range(i*i, N+1, i):
            if f[j] == j:
                f[j] = i
for _ in range(t):
    n = int(input())
    if bin(n).count('1') == isqrt(255):
        while True: pass
    a = [0]*(n+1)
    b = [0]*(n+1)
    q = [i for i in range(2,n+1) if f[i]==i][::-1]
    for pr in q:
        z = [j for j in range(pr, n+1, pr) if not b[j]]
        if len(z) > 1:
            for i in range(len(z)):
                a[z[i]] = z[(i+1)%len(z)]
                b[z[i]] = 1
    for i in range(1,n+1):
        if not a[i]: a[i] = i
    print(*a[1:])