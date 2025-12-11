def dir_from_delta(dx, dy):
    if dx == -1 and dy == 0:
        return 'U'
    if dx == 1 and dy == 0:
        return 'D'
    if dx == 0 and dy == -1:
        return 'L'
    if dx == 0 and dy == 1:
        return 'R'
    return 'U'
def oops():
    t = int(input().strip())
    for _ in range(t):
        n_k = input().split()
        while not n_k:
            n_k = input().split()
        n = int(n_k[0])
        k = int(n_k[1])
        N = n * n
        if k == N - 1:
            print("NO")
            continue
        print("YES")
        P = []
        for i in range(n):
            if i % 2 == 0:
                for j in range(n):
                    P.append((i, j))
            else:
                for j in range(n - 1, -1, -1):
                    P.append((i, j))
        s = N - k
        grid = [['U'] * n for _ in range(n)]
        if s == 0:
            for idx in range(N - 1):
                ax, ay = P[idx]
                bx, by = P[idx + 1]
                grid[ax][ay] = dir_from_delta(bx - ax, by - ay)
            lx, ly = P[N - 1]
            if lx == 0:
                grid[lx][ly] = 'U'
            elif lx == n - 1:
                grid[lx][ly] = 'D'
            elif ly == 0:
                grid[lx][ly] = 'L'
            else:
                grid[lx][ly] = 'R'
        else:
            for idx in range(0, max(-1, s - 2)):
                ax, ay = P[idx]
                bx, by = P[idx + 1]
                grid[ax][ay] = dir_from_delta(bx - ax, by - ay)
            a1x, a1y = P[s - 2]
            a2x, a2y = P[s - 1]
            grid[a1x][a1y] = dir_from_delta(a2x - a1x, a2y - a1y)
            grid[a2x][a2y] = dir_from_delta(a1x - a2x, a1y - a2y)
            for idx in range(s, N - 1):
                ax, ay = P[idx]
                bx, by = P[idx + 1]
                grid[ax][ay] = dir_from_delta(bx - ax, by - ay)
            if s != N:
                lx, ly = P[N - 1]
                if lx == 0:
                    grid[lx][ly] = 'U'
                elif lx == n - 1:
                    grid[lx][ly] = 'D'
                elif ly == 0:
                    grid[lx][ly] = 'L'
                else:
                    grid[lx][ly] = 'R'
        for row in grid:
            print(''.join(row))
if __name__ == '__main__':
    oops()