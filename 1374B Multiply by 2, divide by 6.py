def min_moves_to_one(n):
    moves = 0
    twos = 0
    threes = 0
    while n % 2 == 0:
        n //= 2
        twos += 1
    while n % 3 == 0:
        n //= 3
        threes += 1
    if n != 1 or twos > threes:
        return -1
    return (threes - twos) + threes
t = int(input())
for _ in range(t):
    n = int(input())
    print(min_moves_to_one(n))