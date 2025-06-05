def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False

def tic_tac_toe_status(board):
    flat = ''.join(board)
    x_count = flat.count('X')
    o_count = flat.count('0')
    x_win = check_winner(board, 'X')
    o_win = check_winner(board, '0')
    if o_count > x_count or x_count > o_count + 1:
        return "illegal"
    if x_win and o_win:
        return "illegal"
    if x_win:
        return "the first player won" if x_count == o_count + 1 else "illegal"
    if o_win:
        return "the second player won" if x_count == o_count else "illegal"
    if x_count + o_count == 9:
        return "draw"
    return "first" if x_count == o_count else "second"

board = [input() for i in range(3)]
print(tic_tac_toe_status(board))