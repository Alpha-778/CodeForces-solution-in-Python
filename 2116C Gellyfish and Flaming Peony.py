import math
from collections import deque
MAX = 5001
INF = int(1e9)
t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n, a])
for i in range(t):
    n, a = rec[i]
    g = 0
    for val in a:
        g = math.gcd(g, val)
    countG = sum(1 for x in a if x == g)
    if countG > 0:
        print(n - countG)
        continue
    seen = [False] * MAX
    uniq = []
    for val in a:
        if not seen[val]:
            seen[val] = True
            uniq.append(val)
    dist = [INF] * MAX
    q = deque()
    for val in uniq:
        dist[val] = 0
        q.append(val)
    while q:
        v = q.popleft()
        for x in uniq:
            newVal = math.gcd(v, x)
            if dist[newVal] > dist[v] + 1:
                dist[newVal] = dist[v] + 1
                q.append(newVal)
    minStepsToG = dist[g]
    print(minStepsToG + (n - 1))