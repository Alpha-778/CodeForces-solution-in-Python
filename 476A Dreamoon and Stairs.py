n, m = map(int, input().split())
min_moves = (n + 1) // 2
found = -1
for i in range(min_moves, n + 1):
    if i % m == 0:
        found = i
        break
print(found)
