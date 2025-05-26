t = int(input())
rec = []

i = 0
while i < t:
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n, a])
    i += 1

i = 0
while i < t:
    n, a = rec[i]
    m = 1
    j = 0
    while j < n:
        x = a[j]
        k = 0
        while k < n:
            y = a[k]
            if x <= y and (x + y) % 2 == 0:
                cnt = 0
                l = 0
                while l < n:
                    if x <= a[l] <= y:
                        cnt += 1
                    l += 1
                if cnt > m:
                    m = cnt
            k += 1
        j += 1
    print(n - m)
    i += 1
