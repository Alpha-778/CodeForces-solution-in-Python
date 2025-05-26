n, m = map(int, input().split())
tasks = list(map(int, input().split()))
current = 1
time = 0
for task in tasks:
    if task >= current:
        time += task - current
    else:
        time += n - current + task
    current = task
print(time)