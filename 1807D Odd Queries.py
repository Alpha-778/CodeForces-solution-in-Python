def is_odd(x):
    return x % 2 == 1

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    total_sum = prefix[n]
    for _ in range(q):
        l, r, k = map(int, input().split())
        sub_sum = prefix[r] - prefix[l - 1]
        new_sum = total_sum - sub_sum + (r - l + 1) * k
        print("YES" if is_odd(new_sum) else "NO")