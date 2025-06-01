def find_composite_pair(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    def is_composite(x):
        return x > 1 and not is_prime[x]
    for x in range(4, n):
        y = n - x
        if is_composite(x) and is_composite(y):
            print(x, y)
            return
n = int(input())
find_composite_pair(n)