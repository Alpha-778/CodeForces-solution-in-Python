class Solver:
    def __init__(self):
        self.t = int(input())
    def process_case(self):
        n = int(input())
        values = list(map(int, input().split()))
        distinct = len(set(values))
        return str(2 * distinct - 1)
    def run(self):
        results = []
        for _ in range(self.t):
            results.append(self.process_case())
        print("\n".join(results))
if __name__ == "__main__":
    Solver().run()