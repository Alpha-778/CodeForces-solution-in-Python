MOD = 10**9 + 7
class BIT:
    def __init__(self, n=0):
        self.n = n
        self.bit = [0] * (n + 1)
    def init(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, pos, val):
        i = pos + 1
        while i <= self.n:
            self.bit[i] = (self.bit[i] + val) % MOD
            i += i & -i
    def sum_prefix(self, pos):
        if pos < 0:
            return 0
        i = pos + 1
        res = 0
        while i > 0:
            res = (res + self.bit[i]) % MOD
            i -= i & -i
        return res
class Solver:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.m = n + 1
        self.colBIT = [BIT(self.m) for _ in range(self.m)]
        self.rowBIT = [BIT(self.m) for _ in range(self.m)]
        for i in range(self.m):
            self.colBIT[i].init(self.m)
            self.rowBIT[i].init(self.m)
        self.colBIT[0].add(0, 1)
        self.rowBIT[0].add(0, 1)
        self.total = 1
    def solve(self):
        for idx in range(self.n):
            x = self.a[idx]
            s1 = [self.colBIT[l2].sum_prefix(x) for l2 in range(self.m)]
            s2 = [0] * self.m
            for l1 in range(x + 1, self.m):
                s2[l1] = self.rowBIT[l1].sum_prefix(x)
            for l2 in range(self.m):
                add = s1[l2]
                if add == 0:
                    continue
                self.colBIT[l2].add(x, add)
                self.rowBIT[x].add(l2, add)
                self.total = (self.total + add) % MOD
            for l1 in range(x + 1, self.m):
                add = s2[l1]
                if add == 0:
                    continue
                self.colBIT[x].add(l1, add)
                self.rowBIT[l1].add(x, add)
                self.total = (self.total + add) % MOD
        return self.total
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        solver = Solver(n, a)
        print(solver.solve())