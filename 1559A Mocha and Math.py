t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = a[0]
    for num in a[1:]:
        result &= num
    print(result)