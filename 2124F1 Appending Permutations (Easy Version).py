MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1

    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2

        # Store forbidden values per position (0-based)
        forbidden = [set() for _ in range(n)]
        for _ in range(m):
            pos = int(data[idx]) - 1
            val = int(data[idx+1])
            forbidden[pos].add(val)
            idx += 2

        # dp[i] = number of valid ways to form array of length i
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: empty array

        for length in range(n + 1):
            if dp[length] == 0:
                continue

            for s in range(1, n + 1):
                base = list(range(1, s + 1))
                for r in range(s):
                    shift = base[r:] + base[:r]
                    if length + s > n:
                        continue

                    valid = True
                    for i in range(s):
                        pos = length + i
                        if shift[i] in forbidden[pos]:
                            valid = False
                            break

                    if valid:
                        dp[length + s] = (dp[length + s] + dp[length]) % MOD

        results.append(dp[n])
    
    for res in results:
        print(res)

# To run locally:
# solve()

# For online judges, uncomment the following:
if __name__ == "__main__":
    solve()
