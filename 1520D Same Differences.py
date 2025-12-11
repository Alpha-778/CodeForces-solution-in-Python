from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = defaultdict(int)
    for i in range(n):
        key = a[i] - i
        count[key] += 1
    result = 0
    for val in count.values():
        result += val * (val - 1) // 2
    print(result)