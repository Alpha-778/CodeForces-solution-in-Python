n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
middle = n // 2
good_sum = 0
visited = set()
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == middle or j == middle:
            if (i, j) not in visited:
                good_sum += matrix[i][j]
                visited.add((i, j))
print(good_sum)
