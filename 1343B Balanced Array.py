t = int(input())
rec=[int(input()) for i in range(t)]
for _ in range(t):
    n = rec[_]
    if n % 4 != 0:
        print("NO")
    else:
        print("YES")
        half = n // 2
        evens = [i * 2 for i in range(1, half + 1)]
        odds = [i * 2 - 1 for i in range(1, half)]
        last_odd = sum(evens) - sum(odds)
        odds.append(last_odd)
        print(*evens + odds)