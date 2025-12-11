def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if (i + 1) % 2 != 0:
            total += a[i]
        else:
            total -= a[i]
    if n == 1:
        print(total)
        return
    result = total
    if n % 2 != 0:
        result = max(result, total + n - 1)
    else:
        result = max(result, total + n - 2)
    best_diff = -4 * 10**18
    min_prefix = [4 * 10**18] * n
    if 0 % 2 == 0:
        min_prefix[0] = 2 * a[0] + 0
    for i in range(1, n):
        min_prefix[i] = min_prefix[i - 1]
        if i % 2 == 0:
            min_prefix[i] = min(min_prefix[i], 2 * a[i] + i)
    for r in range(1, n):
        if r % 2 != 0 and min_prefix[r - 1] != 4 * 10**18:
            diff = 2 * a[r] + r - min_prefix[r - 1]
            best_diff = max(best_diff, diff)
    max_prefix = [-4 * 10**18] * n
    if n > 1 and 1 % 2 != 0:
        max_prefix[1] = 2 * a[1] - 1
    for i in range(2, n):
        max_prefix[i] = max_prefix[i - 1]
        if i % 2 != 0:
            max_prefix[i] = max(max_prefix[i], 2 * a[i] - i)
    for r in range(2, n):
        if r % 2 == 0 and max_prefix[r - 1] != -4 * 10**18:
            diff = max_prefix[r - 1] - (2 * a[r] - r)
            best_diff = max(best_diff, diff)
    if best_diff > -4 * 10**18:
        result = max(result, total + best_diff)
    print(result)
t = int(input())
for _ in range(t):
    solve()