t = int(input())
rec=[]
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n,a])
for _ in range(t):
    n,a=rec[_]
    even_wrong = 0
    odd_wrong = 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            if i % 2 == 0:
                even_wrong += 1
            else:
                odd_wrong += 1
    if even_wrong == odd_wrong:
        print(even_wrong)
    else:
        print(-1)