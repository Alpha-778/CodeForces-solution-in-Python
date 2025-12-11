class Solver:
    def __init__(self):
        self.T = int(input())
    def solve_case(self):
        n, q = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        pref0 = [0] * (n + 1)
        pref1 = [0] * (n + 1)
        pref_same = [0] * (n + 1)
        for i in range(1, n + 1):
            pref0[i] = pref0[i - 1] + (a[i] == 0)
            pref1[i] = pref1[i - 1] + (a[i] == 1)
            if i < n:
                pref_same[i] = (a[i] == a[i + 1])
        for i in range(1, n):
            pref_same[i] += pref_same[i - 1]
        if n >= 1:
            pref_same[n] = pref_same[n - 1]
        for _ in range(q):
            l, r = map(int, input().split())
            c0 = pref0[r] - pref0[l - 1]
            c1 = pref1[r] - pref1[l - 1]
            if c0 % 3 != 0 or c1 % 3 != 0:
                print(-1)
                continue
            t_trip = c0 // 3 + c1 // 3
            has_adj = False
            if r - l >= 1:
                adj_count = pref_same[r - 1] - pref_same[l - 1]
                has_adj = adj_count > 0
            print(t_trip if has_adj else t_trip + 1)
    def run(self):
        for _ in range(self.T):
            self.solve_case()
Solver().run()