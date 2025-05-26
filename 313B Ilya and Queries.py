s=input()
n=len(s)
m=int(input())
rec=[list(map(int,input().split())) for i in range(m)]
prefix = [0] * n
for i in range(1, n):
    prefix[i] = prefix[i - 1] + (1 if s[i] == s[i - 1] else 0)
results = []
for l, r in rec:
    results.append(prefix[r - 1] - prefix[l - 1])
print('\n'.join(map(str, results)))