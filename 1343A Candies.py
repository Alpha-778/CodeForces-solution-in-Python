t = int(input())
for _ in range(t):
    n = int(input())
    k = 2
    while True:
        sum_k = (1 << k) - 1
        if n % sum_k == 0:
            print(n // sum_k)
            break
        k += 1