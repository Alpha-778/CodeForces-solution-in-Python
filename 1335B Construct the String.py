t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    pattern = ''.join(chr(ord('a') + i % b) for i in range(a))
    s = (pattern * ((n // a) + 1))[:n]
    print(s)