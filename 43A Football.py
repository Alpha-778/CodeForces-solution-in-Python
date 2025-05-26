n = int(input())
goals = {}
for _ in range(n):
    team = input()
    if team in goals:
        goals[team] += 1
    else:
        goals[team] = 1
winning_team = max(goals, key=goals.get)
print(winning_team)