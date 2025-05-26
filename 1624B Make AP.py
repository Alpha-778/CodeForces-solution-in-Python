t = int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for _ in range(t):
    a, b, c = rec[_]
    flag=False
    if (2 * b - c) > 0 and (2 * b - c) % a == 0:
        flag=True
    if (a + c) % 2 == 0:
        mid = (a + c) // 2
        if mid % b == 0:
            flag=True
    if (2 * b - a) > 0 and (2 * b - a) % c == 0:
        flag=True
    if flag==True:
        print("YES")
    else:
        print("NO")