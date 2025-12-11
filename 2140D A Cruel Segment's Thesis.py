class IntervalGame:
    def __init__(self, n, intervals):
        self.n = n
        self.l = [x[0] for x in intervals]
        self.r = [x[1] for x in intervals]
        self.v = [self.l[i] + self.r[i] for i in range(n)]
        self.S = sum(self.l)
        self.O = sum(self.r[i] - self.l[i] for i in range(n))
    def solve(self):
        a = sorted([(self.v[i], i) for i in range(self.n)], key=lambda x: (-x[0], x[1]))
        p = [0] * self.n
        pf = [0] * (self.n + 1)
        for i, (_, idx) in enumerate(a):
            p[idx] = i
            pf[i + 1] = pf[i] + a[i][0]
        if self.n % 2 == 0:
            k = self.n // 2
            t = pf[k]
            return self.O + (t - self.S)
        else:
            k = (self.n - 1) // 2
            ans = float('-inf')
            for i in range(self.n):
                t = pf[k] if p[i] >= k else pf[k + 1] - self.v[i]
                add = t - (self.S - self.l[i])
                ans = max(ans, self.O + add)
            return ans
class Solution:
    def __init__(self):
        self.test_cases = []
    def read_input(self):
        try:
            T = int(input())
        except:
            return False
        for _ in range(T):
            n = int(input())
            intervals = [tuple(map(int, input().split())) for _ in range(n)]
            self.test_cases.append(IntervalGame(n, intervals))
        return True
    def run(self):
        for game in self.test_cases:
            print(game.solve())
if __name__ == "__main__":
    sol = Solution()
    if sol.read_input():
        sol.run()
        