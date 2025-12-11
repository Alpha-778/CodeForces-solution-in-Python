class Solver:
    def __init__(self):
        self.cache_g = {}
        self.cache_spec = {}
    def g_single(self, x):
        cnt = 0
        while x > 1:
            x //= 2
            cnt += 1
            if x == 1:
                break
            x += 1
        return cnt
    def is_special(self, x):
        if x <= 2:
            return False
        y = x - 1
        return (y & (y - 1)) == 0
    def process_case(self, n, q, a, queries):
        prefG = [0] * (n + 1)
        prefS = [0] * (n + 1)
        for i in range(1, n + 1):
            v = a[i-1]
            if v in self.cache_g:
                gv = self.cache_g[v]
            else:
                gv = self.g_single(v)
                self.cache_g[v] = gv
            prefG[i] = prefG[i-1] + gv
            if v in self.cache_spec:
                sp = self.cache_spec[v]
            else:
                sp = self.is_special(v)
                self.cache_spec[v] = sp
            prefS[i] = prefS[i-1] + (1 if sp else 0)
        result = []
        for l, r in queries:
            base = prefG[r] - prefG[l-1]
            cntS = prefS[r] - prefS[l-1]
            extra = cntS - 1 if cntS >= 1 else 0
            result.append(base + extra)
        return result
def main():
    T = int(input())
    solver = Solver()
    answers = []
    for _ in range(T):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        queries = [tuple(map(int, input().split())) for _ in range(q)]
        answers.extend(solver.process_case(n, q, a, queries))
    print("\n".join(map(str, answers)))
if __name__ == "__main__":
    main()