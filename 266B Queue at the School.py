n, t = map(int, input().split())
queue = input()
data = list(queue)
for _ in range(t):
    j = 1
    while j < len(data):
        if data[j] == 'G' and data[j - 1] == 'B':
            data[j], data[j - 1] = data[j - 1], data[j]
            j += 1
        j += 1
print(''.join(data))
