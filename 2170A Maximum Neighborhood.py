t = int(input())
rec=[int(input()) for i in range(t)]
for _ in range(t):
    n = rec[_]
    if n == 1:
        print(1)
    elif n == 2:
        print(9)
    else:
        a = 4*n*n - n - 4
        b = 5*n*n - 5*n - 5
        print(max(a, b))