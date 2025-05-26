n = int(input())
rec = [input() for _ in range(n)]
count = 1
for i in range(1, n):
    if rec[i] != rec[i-1]:
        count += 1
print(count)
