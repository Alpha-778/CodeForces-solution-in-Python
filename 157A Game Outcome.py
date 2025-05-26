n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
row_sums = [sum(row) for row in board]
col_sums = [sum(board[i][j] for i in range(n)) for j in range(n)]
winning_squares = 0
for i in range(n):
    for j in range(n):
        if col_sums[j] > row_sums[i]:
            winning_squares += 1
print(winning_squares)