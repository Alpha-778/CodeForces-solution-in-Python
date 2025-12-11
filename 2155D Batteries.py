class BatteryTester:
    def __init__(self):
        self.found = False
    def run_test_case(self, n):
        self.found = False
        for d in range(1, n):
            if self.found:
                break
            for i in range(1, n - d + 1):
                if self.found:
                    break
                u, v = i, i + d
                print(u, v, flush=True)
                try:
                    x = int(input())
                except:
                    exit()
                if x == -1:
                    exit()
                if x == 1:
                    self.found = True
    def start(self):
        try:
            T = int(input())
        except:
            return
        for _ in range(T):
            try:
                n = int(input())
            except:
                return
            self.run_test_case(n)
if __name__ == "__main__":
    BatteryTester().start()