t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if min(n, m) >= 2 and max(n, m) >= 3:
        print("YES")
    else:
        print("NO")