import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def t_primes(numbers):
    max_val = int(1e6)
    primes = sieve(max_val)
    t_prime_set = set(p * p for p in primes)

    results = []
    for x in numbers:
        if x in t_prime_set:
            results.append("YES")
        else:
            results.append("NO")
    return results

n = int(input())
numbers = list(map(int, input().split()))
results = t_primes(numbers)
for res in results:
    print(res)
