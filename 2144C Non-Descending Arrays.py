MOD = 998244353
t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rec.append([n, a, b])
for _ in range(t):
    n, a, b = rec[_]
    class Solver:
        def __init__(self, n, a, b):
            self.n = n
            self.a = [0] + a
            self.b = [0] + b
            self.dp = [[0, 0] for _ in range(n + 1)]
        def compute(self):
            self.dp[1][0] = 1
            self.dp[1][1] = 1
            for i in range(2, self.n + 1):
                self.dp[i][0] = 0
                self.dp[i][1] = 0
                for p in range(2):
                    prev_a = self.b[i - 1] if p else self.a[i - 1]
                    prev_b = self.a[i - 1] if p else self.b[i - 1]
                    for c in range(2):
                        cur_a = self.b[i] if c else self.a[i]
                        cur_b = self.a[i] if c else self.b[i]
                        if prev_a <= cur_a and prev_b <= cur_b:
                            self.dp[i][c] = (self.dp[i][c] + self.dp[i - 1][p]) % MOD
            return (self.dp[self.n][0] + self.dp[self.n][1]) % MOD
    solver = Solver(n, a, b)
    print(solver.compute())