def find_min_height_index(n, k, h):
    window_sum = sum(h[:k])
    min_sum = window_sum
    min_index = 0
    for i in range(1, n - k + 1):
        window_sum = window_sum - h[i - 1] + h[i + k - 1]
        if window_sum < min_sum:
            min_sum = window_sum
            min_index = i
    return min_index + 1
n, k = map(int, input().split())
h = list(map(int, input().split()))
print(find_min_height_index(n, k, h))
