t = int(input())
rec = []
for _ in range(t):
    n, y = map(int, input().split())
    c = list(map(int, input().split()))
    rec.append([n, y, c])
class CaseSolver:
    def __init__(self, n, y, c):
        self.n = n
        self.y = y
        self.c = c
    def solve(self):
        m = max(self.c)
        freq = [0] * (m + 1)
        for val in self.c:
            freq[val] += 1
        prefix = [0] * (m + 1)
        for i in range(1, m + 1):
            prefix[i] = prefix[i - 1] + freq[i]
        best = float('-inf')
        for x in range(2, m + 2):
            max_k = (m + x - 1) // x
            s = 0
            r = 0
            for k in range(1, max_k + 1):
                L = (k - 1) * x + 1
                R = min(k * x, m)
                if L > R:
                    continue
                count = prefix[R] - prefix[L - 1]
                if count == 0:
                    continue
                s += k * count
                if k <= m:
                    r += min(count, freq[k])
            penalty = self.n - r
            increment = s - self.y * penalty
            if increment > best:
                best = increment
        return best
for _ in range(t):
    n, y, c = rec[_]
    solver = CaseSolver(n, y, c)
    print(solver.solve())