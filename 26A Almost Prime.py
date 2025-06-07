def count_almost_primes(n):
    prime_divisors = [0] * (n + 1)
    for i in range(2, n + 1):
        if prime_divisors[i] == 0:
            for j in range(i, n + 1, i):
                prime_divisors[j] += 1
    return sum(1 for i in range(1, n + 1) if prime_divisors[i] == 2)

n = int(input())
print(count_almost_primes(n))