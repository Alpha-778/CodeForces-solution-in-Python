t=int(input())
rec=[list(map(int,input().split())) for i in range(0,t)]
for _ in range(t):
    n, k = rec[_]
    if n >= k * k and (n % 2 == k % 2):
        print("YES")
    else:
        print("NO")