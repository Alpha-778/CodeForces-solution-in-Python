MOD = 676767677
class Solver:
    def __init__(self, n, arr):
        self.n = n
        self.a = [0] + arr
        self.b = [0] * (n + 1)
        self.alt = [0] * (n + 1)
    def in_range(self, x):
        return 0 <= x <= self.n
    def compute_b_alt(self):
        for i in range(1, self.n + 1):
            self.b[i] = self.a[i] - (self.n - i + 1)
        for i in range(1, self.n + 1):
            self.alt[i] = self.b[i] - self.alt[i - 1]
    def find_candidates(self):
        cand = []
        t = self.alt[1] - self.alt[0]
        v1, v2 = -t, 1 - t
        if self.in_range(v1): cand.append(v1)
        if v2 != v1 and self.in_range(v2): cand.append(v2)
        for i in range(2, self.n + 1):
            if not cand: break
            t = self.alt[i] - self.alt[i - 1]
            if i % 2 == 1:
                u1, u2 = -t, 1 - t
            else:
                u1, u2 = t, t - 1
            next_cand = [x for x in cand if x == u1 or x == u2]
            cand = list(sorted(set(next_cand)))
        return cand
    def finalize(self, cand):
        finalc = []
        if cand:
            if self.n % 2 == 1:
                if self.alt[self.n] == 0:
                    finalc = cand
            else:
                finalc = [x for x in cand if x == self.alt[self.n]]
        return finalc
    def solve(self):
        self.compute_b_alt()
        candidates = self.find_candidates()
        final_candidates = self.finalize(candidates)
        return len(final_candidates) % MOD
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    solver = Solver(n, arr)
    print(solver.solve())