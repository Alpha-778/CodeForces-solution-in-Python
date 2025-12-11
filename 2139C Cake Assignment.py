class SequenceSolver:
    def __init__(self, k, x):
        self.k = k
        self.x = x
        self.A0 = 1 << k
        self.T = 1 << (k + 1)        
    def solve(self):
        if self.x == self.A0:
            return []
        result = []
        cur = self.x
        while cur != self.A0:
            if cur < self.A0:
                cur *= 2
                result.append(1)
            else:
                cur = cur * 2 - self.T
                result.append(2)
        result.reverse()
        return result
class Main:
    def run(self):
        try:
            t = int(input())
        except:
            return
        for _ in range(t):
            k, x = map(int, input().split())
            solver = SequenceSolver(k, x)
            steps = solver.solve()
            print(len(steps))
            if steps:
                print(' '.join(map(str, steps)))
            else:
                print()
if __name__ == "__main__":
    Main().run()