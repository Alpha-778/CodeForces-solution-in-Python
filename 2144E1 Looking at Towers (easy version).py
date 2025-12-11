t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec.append([n, a])
for _ in range(t):
    n, a = rec[_]
    MOD = 998244353
    class Solver:
        def __init__(self, n, a):
            self.n = n
            self.a = [0] + a
            self.left_blocks = []
            self.right_blocks = []
            self.left_need = []
            self.right_need = []
            self.left_block = [-1] * (n + 1)
            self.right_block = [-1] * (n + 1)
            self.is_left_end = [0] * (n + 1)
            self.is_right_end = [0] * (n + 1)
        def prepare(self):
            prefix = float('-inf')
            for i in range(1, self.n + 1):
                if self.a[i] > prefix:
                    prefix = self.a[i]
                    self.left_blocks.append(i)
            suffix = float('-inf')
            tmp = []
            for i in range(self.n, 0, -1):
                if self.a[i] > suffix:
                    suffix = self.a[i]
                    tmp.append(i)
            self.right_blocks = tmp[::-1]
            for i, L in enumerate(self.left_blocks):
                R = self.left_blocks[i + 1] - 1 if i + 1 < len(self.left_blocks) else self.n
                self.left_need.append(self.a[L])
                for p in range(L, R + 1):
                    self.left_block[p] = i
                self.is_left_end[R] = 1
            for j, R in enumerate(self.right_blocks):
                L = 1 if j == 0 else self.right_blocks[j - 1] + 1
                self.right_need.append(self.a[R])
                for p in range(L, R + 1):
                    self.right_block[p] = j
                self.is_right_end[R] = 1
        def count_sequences(self):
            self.prepare()
            dp = [[0, 0], [0, 0]]
            dp[0][0] = 1
            for pos in range(1, self.n + 1):
                new_dp = [[0, 0], [0, 0]]
                li = self.left_block[pos]
                rj = self.right_block[pos]
                needL = self.left_need[li]
                needR = self.right_need[rj]
                for so in range(2):
                    for to in range(2):
                        ways = dp[so][to]
                        if ways == 0:
                            continue
                        new_dp[so][to] = (new_dp[so][to] + ways) % MOD
                        so2 = so | (self.a[pos] == needL)
                        to2 = to | (self.a[pos] == needR)
                        new_dp[so2][to2] = (new_dp[so2][to2] + ways) % MOD
                if self.is_left_end[pos] and self.is_right_end[pos]:
                    ways = new_dp[1][1] % MOD
                    new_dp = [[0, 0], [0, 0]]
                    new_dp[0][0] = ways
                elif self.is_left_end[pos]:
                    t0 = new_dp[1][0] % MOD
                    t1 = new_dp[1][1] % MOD
                    new_dp = [[0, 0], [0, 0]]
                    new_dp[0][0] = t0
                    new_dp[0][1] = t1
                elif self.is_right_end[pos]:
                    s0 = new_dp[0][1] % MOD
                    s1 = new_dp[1][1] % MOD
                    new_dp = [[0, 0], [0, 0]]
                    new_dp[0][0] = s0
                    new_dp[1][0] = s1
                dp = new_dp
            return (dp[0][0] % MOD + MOD) % MOD
    solver = Solver(n, a)
    print(solver.count_sequences())