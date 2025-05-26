k, r = map(int, input().split())
for n in range(1, 11):
    if (n * k) % 10 == 0 or (n * k) % 10 == r:
        print(n)
        break