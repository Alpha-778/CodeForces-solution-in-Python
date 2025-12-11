for _ in range(int(input())):
    n = int(input())
    p = [list(map(int, input().split())) + [i+1] for i in range(n)]
    p.sort(key=lambda a: (a[0], a[1]))
    a, b = sorted(p[:n//2], key=lambda x: x[1]), sorted(p[n//2:], key=lambda x: -x[1])
    for i in range(n//2): print(a[i][2], b[i][2])