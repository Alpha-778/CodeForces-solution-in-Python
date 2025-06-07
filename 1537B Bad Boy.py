def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

t = int(input())
for _ in range(t):
    n, m, i, j = map(int, input().split())
    corners = [(1, 1), (1, m), (n, 1), (n, m)]
    max_dist = -1
    ans = (1, 1, 1, 1)
    for c1 in corners:
        for c2 in corners:
            d = dist(i, j, c1[0], c1[1]) + dist(c1[0], c1[1], c2[0], c2[1]) + dist(c2[0], c2[1], i, j)
            if d > max_dist:
                max_dist = d
                ans = (c1[0], c1[1], c2[0], c2[1])
    print(*ans)