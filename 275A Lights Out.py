presses = [list(map(int, input().split())) for _ in range(3)]
lights = [[1 for _ in range(3)] for _ in range(3)]
dirs = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(3):
    for j in range(3):
        toggle_count = 0
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                toggle_count += presses[ni][nj]
        if toggle_count % 2 == 1:
            lights[i][j] = 0
for row in lights:
    print("".join(map(str, row)))