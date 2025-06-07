def min_cost(s):
    max_run = curr = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            curr = 1
        max_run = max(max_run, curr)
    return max_run + 1

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(min_cost(s))