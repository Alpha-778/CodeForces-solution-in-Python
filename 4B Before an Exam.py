d, sumTime = map(int, input().split())
minTimes = []
maxTimes = []
for _ in range(d):
    mn, mx = map(int, input().split())
    minTimes.append(mn)
    maxTimes.append(mx)

minSum = sum(minTimes)
maxSum = sum(maxTimes)

if sumTime < minSum or sumTime > maxSum:
    print("NO")
else:
    print("YES")
    result = minTimes[:]
    extra = sumTime - minSum
    for i in range(d):
        can_add = min(extra, maxTimes[i] - minTimes[i])
        result[i] += can_add
        extra -= can_add
    print(" ".join(map(str, result)))
