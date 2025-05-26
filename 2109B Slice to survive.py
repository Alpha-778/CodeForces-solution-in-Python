import sys
import math

def ceil_log2(x):
    if x <= 1:
        return 0
    f = x.bit_length() - 1
    return f if (1 << f) == x else f + 1

def f(x, p):
    return 1 + min( ceil_log2(p), ceil_log2(x - p + 1) )

input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n, m, a, b = map(int, input().split())
    ans = min(
        f(n, a) + ceil_log2(m),
        f(m, b) + ceil_log2(n)
    )
    out.append(str(ans))
    
print("\n".join(out))
