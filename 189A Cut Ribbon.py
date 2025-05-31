n,a,b,c=map(int,input().split())
dp = [-1] * (n + 1)
dp[0] = 0 
for i in range(1, n + 1):
    for cut in (a, b, c):
        if i >= cut and dp[i - cut] != -1:
            dp[i] = max(dp[i], dp[i - cut] + 1)
print(dp[n])