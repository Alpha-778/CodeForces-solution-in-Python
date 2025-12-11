t = int(input())
rec=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rec.append([n,a,b])
for _ in range(t):
    n,a,b=rec[_]
    ops = []
    for pass_num in range(n):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                ops.append((1, i + 1))
    for pass_num in range(n):
        for i in range(n - 1):
            if b[i] > b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
                ops.append((2, i + 1))
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append((3, i + 1))
    print(len(ops))
    for op in ops:
        print(*op)