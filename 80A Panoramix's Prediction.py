def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
n, m = map(int, input().split())
next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1
if next_prime == m:
    print("YES")
else:
    print("NO")