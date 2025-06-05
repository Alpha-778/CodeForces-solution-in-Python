k = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total < k:
    print(-1)
else:
    a.sort(reverse=True)
    sum_ = 0
    month = 0
    while sum_ < k:
        sum_ += a[month]
        month += 1
    print(month)