t = int(input())
for _ in range(t):
    x = int(input())
    if x > 45:
        print(-1)
        continue
    result = []
    for digit in range(9, 0, -1):
        if x >= digit:
            result.append(digit)
            x -= digit
    print("".join(map(str, sorted(result))))