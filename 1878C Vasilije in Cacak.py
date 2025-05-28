t = int(input())
results = []
for _ in range(t):
    n, k, x = map(int, input().split())
    min_sum = k * (k + 1) // 2
    max_sum = k * (2 * n - k + 1) // 2
    if min_sum <= x <= max_sum:
        results.append("YES")
    else:
        results.append("NO")
print("\n".join(results))