n = int(input())
pi = list(map(int, input().split()))
res = [0] * n
for i in range(n):
    receiver = pi[i]
    res[receiver - 1] = i + 1
print(' '.join(map(str, res)))
