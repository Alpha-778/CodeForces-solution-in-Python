for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(1)
        continue
    p, s = [a[0]], [0]*n
    for i in range(1, n): p.append(min(p[-1], a[i]))
    s[-1] = a[-1]
    for i in range(n-2, -1, -1): s[i] = max(s[i+1], a[i])
    out = []
    for i in range(n):
        l = float('inf') if i == 0 else p[i-1]
        r = float('-inf') if i == n-1 else s[i+1]
        out.append('1' if a[i] < l or a[i] > r else '0')
    print(''.join(out))