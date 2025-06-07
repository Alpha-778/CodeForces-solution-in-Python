def min_deletions_to_make_divisible_by_25(n):
    s = str(n)
    min_steps = float('inf')
    endings = ['00', '25', '50', '75']
    for end in endings:
        second = end[1]
        first = end[0]
        for j in range(len(s) - 1, -1, -1):
            if s[j] == second:
                for i in range(j - 1, -1, -1):
                    if s[i] == first:
                        steps = len(s) - i - 2
                        min_steps = min(min_steps, steps)
                        break
    return min_steps
t = int(input())
for _ in range(t):
    n = input()
    print(min_deletions_to_make_divisible_by_25(n))