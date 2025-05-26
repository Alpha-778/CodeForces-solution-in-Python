while True:
    try:
        n, t = map(int, input().split())
    except EOFError:
        break

    if n == 1 and t == 10:
        print("-1")
    elif n >= 2 and t == 10:
        print("1" * (n - 1) + "0")
    else:
        print(str(t) * n)

