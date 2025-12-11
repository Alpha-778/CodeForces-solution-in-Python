t = int(input())
rec=[int(input()) for i in range(t)]
for _ in range(t):
    n = rec[_]
    result = []
    if n == 3:
        result = [2, 3, 1]
    else:
        result.extend([2, 3, n])
        result.extend(range(4, n))
        result.append(1)
    print(*result)