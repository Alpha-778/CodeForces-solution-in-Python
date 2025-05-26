t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n + 1)]
    rec.append([n, d])
for _ in range(t):
    n, d = rec[_]
    di = d[0]
    obstacles = d[1:]
    possible = True
    low = high = 0
    h_range = [(0, 0)]
    for i in range(n):  
        if di[i] == 0:
            new_low = low
            new_high = high
        elif di[i] == 1:
            new_low = low + 1
            new_high = high + 1
        else:  
            new_low = low
            new_high = high + 1
        li, ri = obstacles[i]
        new_low = max(new_low, li)
        new_high = min(new_high, ri)
        if new_low > new_high:
            possible = False
            break
        low, high = new_low, new_high
        h_range.append((low, high))
    if not possible:
        print(-1)
        continue
    res = [0] * n
    height = h_range[-1][0]
    for i in reversed(range(n)):
        li, ri = obstacles[i]
        pre_low, pre_high = h_range[i]
        if di[i] == 0:
            if pre_low <= height <= pre_high:
                res[i] = 0
            else:
                height -= 1
                res[i] = 1
        elif di[i] == 1:
            height -= 1
            res[i] = 1
        else:  # -1
            if pre_low <= height - 1 <= pre_high:
                height -= 1
                res[i] = 1
            else:
                res[i] = 0
    print(*res)