n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        mini = x[1] - x[0]
        maxi = x[-1] - x[0]
    elif i == n - 1:
        mini = x[-1] - x[-2]
        maxi = x[-1] - x[0]
    else:
        mini = min(x[i] - x[i - 1], x[i + 1] - x[i])
        maxi = max(x[i] - x[0], x[-1] - x[i])
    print(f"{mini} {maxi}")