class Solver:
    def __init__(self, n, k, parents):
        self.n = n
        self.k = k
        self.parents = parents
        self.depth = [0] * (n + 1)
        self.degree = [0] * (n + 1)
        self.w = []
    def compute_depths(self):
        self.depth[1] = 1
        for i in range(2, self.n + 1):
            self.depth[i] = self.depth[self.parents[i]] + 1
    def compute_degrees(self):
        for i in range(2, self.n + 1):
            self.degree[self.parents[i]] += 1
    def find_min_depth(self):
        D = float('inf')
        for i in range(1, self.n + 1):
            if self.degree[i] == 0:
                D = min(D, self.depth[i])
        if D == float('inf'):
            D = max(self.depth[1:])
        return D
    def count_depths(self, D):
        self.w = [0] * (D + 1)
        for i in range(1, self.n + 1):
            if self.depth[i] <= D:
                self.w[self.depth[i]] += 1
    def solve_dp(self, D):
        A = self.k
        B = self.n - self.k
        NEG = -10**9
        dp = [[NEG] * (B + 1) for _ in range(A + 1)]
        dp[0][0] = 0
        for d in range(1, D + 1):
            wt = self.w[d]
            for a in range(A, -1, -1):
                for b in range(B, -1, -1):
                    if dp[a][b] < 0:
                        continue
                    if a + wt <= A:
                        dp[a + wt][b] = max(dp[a + wt][b], dp[a][b] + 1)
                    if b + wt <= B:
                        dp[a][b + wt] = max(dp[a][b + wt], dp[a][b] + 1)
        ans = 0
        for a in range(A + 1):
            for b in range(B + 1):
                ans = max(ans, dp[a][b])
        return ans
def main():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        tmp = list(map(int, input().split()))
        parents = [0] * (n + 1)
        for i in range(2, n + 1):
            parents[i] = tmp[i - 2]
        solver = Solver(n, k, parents)
        solver.compute_depths()
        solver.compute_degrees()
        D = solver.find_min_depth()
        solver.count_depths(D)
        result = solver.solve_dp(D)
        print(result)
if __name__ == "__main__":
    main()