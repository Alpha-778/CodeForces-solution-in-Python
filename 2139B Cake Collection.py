class CakeCollector:
    def __init__(self, n, m, cakes):
        self.n = n
        self.m = m
        self.cakes = sorted(cakes, reverse=True)
    def max_cake_value(self):
        max_take = min(self.n, self.m)
        best_value = 0
        current_value = 0
        for i in range(max_take):
            current_value += self.cakes[i] * (self.m - i)
            if current_value > best_value:
                best_value = current_value
        return best_value
def main():
    from sys import stdin
    input = stdin.readline
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        cakes = list(map(int, input().split()))
        collector = CakeCollector(n, m, cakes)
        print(collector.max_cake_value())
if __name__ == "__main__":
    main()