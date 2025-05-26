n = int(input())
levels = set()
for _ in range(2):
    parts = list(map(int, input().split()))
    levels.update(parts[1:])
print("I become the guy." if len(levels) == n else "Oh, my keyboard!")
