for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    q = [n + 1 - x for x in p]
    print(*q)