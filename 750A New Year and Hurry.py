n, k = map(int, input().split())
time_left = 240 - k
total_time = 0
problems_solved = 0
for i in range(1, n + 1):
    total_time += 5 * i
    if total_time > time_left:
        break
    problems_solved += 1
print(problems_solved)