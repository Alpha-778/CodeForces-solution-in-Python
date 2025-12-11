class MaxChangeSolver:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.INF = 10**18
    def solve_case(self):
        a = self.arr
        n = self.n
        max_l_prefix = [-self.INF] * n
        max_change = -self.INF
        initial_S = sum(a[i] if i % 2 == 0 else -a[i] for i in range(n))
        max_f = initial_S
        for i in range(n):
            if i % 2 == 0:
                if i > 0:
                    max_l_prefix[i] = max(max_l_prefix[i], max_l_prefix[i - 1])
                max_l_prefix[i] = max(max_l_prefix[i], 2 * a[i] - i)
        for r_idx in range(2, n):
            if r_idx % 2 == 0 and max_l_prefix[r_idx - 1] != -self.INF:
                current_change = max_l_prefix[r_idx - 1] - (2 * a[r_idx] - r_idx)
                max_change = max(max_change, current_change)
        if max_change > -self.INF:
            max_f = max(max_f, initial_S + max_change)
        return max_f
class Problem:
    def __init__(self):
        self.test_cases = []
    def read_input(self):
        t = int(input())
        for _ in range(t):
            n = int(input())
            arr = list(map(int, input().split()))
            self.test_cases.append((n, arr))
    def solve(self):
        for n, arr in self.test_cases:
            solver = MaxChangeSolver(n, arr)
            print(solver.solve_case())
if __name__ == "__main__":
    problem = Problem()
    problem.read_input()
    problem.solve()