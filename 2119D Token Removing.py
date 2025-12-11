def solve_case(n: int, mod: int) -> int:
    dp = [0]*(n+1)          
    dp[0] = 1 % mod
    max_k = 0               
    for p in range(n, 0, -1):
        for k in range(max_k, -1, -1):
            if dp[k] == 0:
                continue
            free = n - p + 1 - k      
            if free <= 0:
                break                 
            add = (dp[k] * free) % mod
            add = (add * p) % mod     
            dp[k+1] = (dp[k+1] + add) % mod
        if dp[max_k + 1]:
            max_k += 1                
    return sum(dp) % mod
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve_case(n, m))