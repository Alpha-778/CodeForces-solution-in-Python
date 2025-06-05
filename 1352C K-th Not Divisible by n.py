t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    n,k=rec[i]
    ans = k + (k - 1) // (n - 1)
    print(ans)