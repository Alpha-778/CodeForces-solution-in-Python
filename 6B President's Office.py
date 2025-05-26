def count_president_deputies(n, m, c, office):
    deputies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    for i in range(n):
        for j in range(m):
            if office[i][j] == c:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        neighbor = office[ni][nj]
                        if neighbor != '.' and neighbor != c:
                            deputies.add(neighbor)
    return len(deputies)
n, m, c = input().split()
n = int(n)
m = int(m)
office = [input().strip() for _ in range(n)]
print(count_president_deputies(n, m, c, office))
