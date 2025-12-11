t = int(input())
rec=[]
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    rec.append([n,k,s])
for _ in range(t):
    n,k,s=rec[_]
    a = [0]*n
    for i in range(n):
        if s[i] == '1':
            r = i+k
            if r >= n: r = n-1
            for j in range(i, r+1):
                a[j] = 1
    c = 0
    for i in range(n):
        if s[i] == '0' and a[i] == 0:
            c += 1
    print(c)