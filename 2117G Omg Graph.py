import sys
input = sys.stdin.readline
INF = 4 * 10**18

class DSU:
    def __init__(self, n):
        self.p = list(range(n+1))
        self.sz = [1] * (n+1)
        self.best = [INF] * (n+1)

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def unite(self, a, b, w):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            self.best[a] = min(self.best[a], w)
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        self.best[a] = min(self.best[a], self.best[b], w)

def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for __ in range(m)]
        edges.sort(key=lambda x: x[2])
        dsu = DSU(n)
        ans = INF
        for u, v, w in edges:
            dsu.unite(u, v, w)
            r = dsu.find(1)
            if dsu.find(n) == r:
                candidate = w + dsu.best[r]
                if candidate < ans:
                    ans = candidate
        print(ans)

if __name__ == "__main__":
    main()
