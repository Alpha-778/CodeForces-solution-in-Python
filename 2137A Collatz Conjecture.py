for _ in range(int(input())):
    k, x = map(int, input().split())
    for _ in range(k):
        if x % 2 == 0:
            x *= 2
        else:
            if (x - 1) % 3 == 0 and ((x - 1) // 3) % 2 == 1 and (x - 1) // 3 > 0:
                x = (x - 1) // 3
            else:
                x *= 2
    print(x)