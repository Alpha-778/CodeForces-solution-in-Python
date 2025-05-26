import bisect
n = int(input())
prices = list(map(int, input().split()))
q = int(input())
queries = [int(input()) for _ in range(q)]
prices.sort()
for mi in queries:
    count = bisect.bisect_right(prices, mi)
    print(count)