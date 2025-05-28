from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    if k >= max(0, odd_count - 1) and (n - k) >= 0:
        print("YES")
    else:
        print("NO")
