t = int(input())
rec=[int(input()) for i in range(t)]
for _ in range(t):
    x = rec[_]
    if x == 0:
        k = 0
    else:
        k = x.bit_length() - 1
    ans = 2 * k + 3
    print(ans)