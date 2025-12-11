t = int(input())
rec = [list(map(str, input().split())) for i in range(t)]
from functools import lru_cache
for _ in range(t):
    l, r = rec[_]
    n = len(l)
    ans = float('inf')
    @lru_cache(None)
    def dp(pos, tight_l, tight_r, cost):
        global ans
        if pos == n:
            if cost < ans:
                ans = cost
            return
        lo = int(l[pos]) if tight_l else 0
        hi = int(r[pos]) if tight_r else 9
        for d in range(lo, hi + 1):
            match = 0
            if d == int(l[pos]):
                match += 1
            if d == int(r[pos]):
                match += 1
            next_tight_l = tight_l and (d == int(l[pos]))
            next_tight_r = tight_r and (d == int(r[pos]))
            dp(pos + 1, next_tight_l, next_tight_r, cost + match)
    dp(0, True, True, 0)
    print(ans)