def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y
def modular_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    x %= m
    if x < 0:
        x += m
    return x
def solve_case(n, k, arr):
    x = k + 1
    p = -1
    d = 2
    while d * d <= x:
        if x % d == 0:
            p = d
            break
        d += 1
    if p == -1:
        p = x
    u = (k % p + p) % p
    v = modular_inverse(u, p)
    for i in range(n):
        s = (arr[i] % p + p) % p
        w = (p - s) % p
        m = (w * v) % p
        arr[i] += m * k
    return arr
def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        k = int(data[idx]); idx += 1
        arr = []
        for _ in range(n):
            arr.append(int(data[idx]))
            idx += 1
        res = solve_case(n, k, arr)
        results.append(" ".join(str(x) for x in res))
    print("\n".join(results))
if __name__ == "__main__":
    main()