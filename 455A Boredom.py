from collections import Counter

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
max_val = max(a)
dp = [0] * (max_val + 2)
dp[1] = count[1] * 1
for i in range(2, max_val + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + i * count[i])
print(dp[max_val])