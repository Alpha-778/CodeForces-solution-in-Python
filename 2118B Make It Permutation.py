t = int(input())
rec=[int(input()) for _ in range(t)]
for _ in range(t):
    n = rec[_]
    operations = []
    operations.append((1, 1, n))
    for row in range(2, n + 1):
        prefix_end = n - row + 1
        suffix_start = prefix_end + 1
        operations.append((row, 1, prefix_end))
        if suffix_start <= n:
            operations.append((row, suffix_start, n))
    print(len(operations))
    for r, a, b in operations:
        print(f"{r} {a} {b}")