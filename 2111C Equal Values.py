import sys
t = int(input())
rec=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n,a])
for _ in range(t):
    n,a=rec[_]
    ans = float('inf')
    i = 0
    while i < n:
        j = i
        while j + 1 < n and a[j + 1] == a[i]:
            j += 1
        v = a[i]
        cost = v * (i + (n - 1 - j))
        ans = min(ans, cost)
        i = j + 1
    print(ans)