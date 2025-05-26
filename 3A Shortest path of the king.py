def king_shortest_path(s, t):
    col_map = {chr(ord('a') + i): i for i in range(8)}
    x1, y1 = col_map[s[0]], int(s[1]) - 1
    x2, y2 = col_map[t[0]], int(t[1]) - 1
    dx = x2 - x1
    dy = y2 - y1
    moves = []
    while dx != 0 or dy != 0:
        move = ""
        if dx > 0:
            move += "R"
            dx -= 1
        elif dx < 0:
            move += "L"
            dx += 1
        if dy > 0:
            move += "U"
            dy -= 1
        elif dy < 0:
            move += "D"
            dy += 1
        moves.append(move)
    print(len(moves))
    for m in moves:
        print(m)

s = input()
t = input()
king_shortest_path(s, t)
