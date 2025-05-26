t = int(input())
rec=[input() for i in range(t)]
for _ in range(t):
    n = rec[_]
    round_numbers = []
    length = len(n)
    for i in range(length):
        digit = int(n[i])
        if digit != 0:
            round_numbers.append(str(digit * (10 ** (length - i - 1))))
    print(len(round_numbers))
    print(" ".join(round_numbers))
