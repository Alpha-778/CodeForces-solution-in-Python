n = int(input())
mishka_wins = 0
chris_wins = 0

for _ in range(n):
    m, c = map(int, input().split())
    if m > c:
        mishka_wins += 1
    elif c > m:
        chris_wins += 1

if mishka_wins > chris_wins:
    print("Mishka")
elif chris_wins > mishka_wins:
    print("Chris")
else:
    print("Friendship is magic!^^")
