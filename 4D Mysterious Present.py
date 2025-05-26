n, w, h = map(int, input().split())
envelopes = []
for i in range(n):
    wi, hi = map(int, input().split())
    if wi > w and hi > h:
        envelopes.append((wi, hi, i + 1))  # store original index

# Sort by width, then by height descending (to prevent same width issues)
envelopes.sort(key=lambda x: (x[0], -x[1]))

# Apply LIS on heights
dp = [1] * len(envelopes)
prev = [-1] * len(envelopes)
max_len = 0
last_index = -1
for i in range(len(envelopes)):
    for j in range(i):
        if envelopes[j][1] < envelopes[i][1] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j
    if dp[i] > max_len:
        max_len = dp[i]
        last_index = i

# Output result
if max_len == 0:
    print(0)
else:
    print(max_len)
    res = []
    while last_index != -1:
        res.append(envelopes[last_index][2])
        last_index = prev[last_index]
    print(' '.join(map(str, reversed(res))))
