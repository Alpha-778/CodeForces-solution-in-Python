for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                print("YES\n2\n", a[i], a[j])
                f = 1
                break
        if f: break
    if not f: print("NO")