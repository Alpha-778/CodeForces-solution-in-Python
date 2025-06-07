t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    min_sum = float('inf')
    max_sum = float('-inf')
    min_diff = float('inf')
    max_diff = float('-inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                s = i + j
                d = i - j
                min_sum = min(min_sum, s)
                max_sum = max(max_sum, s)
                min_diff = min(min_diff, d)
                max_diff = max(max_diff, d)
    center_sum = (min_sum + max_sum) // 2
    center_diff = (min_diff + max_diff) // 2
    h = (center_sum + center_diff) // 2 + 1
    k = (center_sum - center_diff) // 2 + 1
    print(h, k)