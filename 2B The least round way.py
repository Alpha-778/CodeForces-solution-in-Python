import sys
sys.setrecursionlimit(1000000)
MAX = 100000
matrix = []

def power(number, base):
    p = 0
    while number % base == 0:
        number //= base
        p += 1
    return p

def get_matrix(which, r, c):
    if which:
        return matrix[r][c][1]
    return matrix[r][c][0]

def find_path(r, c, which, mx):
    path = ""
    while r or c:
        if r > 0 and mx[r][c] - get_matrix(which, r, c) == mx[r-1][c]:
            r -= 1
            path = "D" + path
        elif c > 0 and mx[r][c] - get_matrix(which, r, c) == mx[r][c-1]:
            c -= 1
            path = "R" + path
    return path

def main():
    zero = False
    zj = 0
    n = int(input())
    global matrix
    matrix = [[(0, 0) for _ in range(n)] for _ in range(n)]
    m2 = [[MAX] * n for _ in range(n)]
    m5 = [[MAX] * n for _ in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            k = row[j]
            if k == 0:
                zero = True
                zj = j
                k = 10
            matrix[i][j] = (power(k, 2), power(k, 5))
    m2[0][0] = matrix[0][0][0]
    m5[0][0] = matrix[0][0][1]
    for i in range(n):
        for j in range(n):
            if j > 0:
                m2[i][j] = min(m2[i][j], matrix[i][j][0] + m2[i][j-1])
                m5[i][j] = min(m5[i][j], matrix[i][j][1] + m5[i][j-1])
            if i > 0:
                m2[i][j] = min(m2[i][j], matrix[i][j][0] + m2[i-1][j])
                m5[i][j] = min(m5[i][j], matrix[i][j][1] + m5[i-1][j])
    mini = min(m2[n-1][n-1], m5[n-1][n-1])
    path = ""
    if zero and mini > 1:
        mini = 1
        path = "R" * zj + "D" * (n - 1) + "R" * (n - 1 - zj)
    else:
        if m5[n-1][n-1] == mini:
            path = find_path(n-1, n-1, True, m5)
        else:
            path = find_path(n-1, n-1, False, m2)
    print(mini if mini >= 0 else 1)
    print(path)
    
if __name__ == "__main__":
    main()
