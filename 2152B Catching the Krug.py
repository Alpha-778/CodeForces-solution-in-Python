class Solution:
    def solve(self):
        try:
            t = int(input().strip())
        except:
            return
        for _ in range(t):
            n, rK, cK, rD, cD = map(int, input().split())
            def ok(k):
                r_high = min(n, rK + k)
                r_low = max(0, rK - k)
                worst_row = max(abs(r_high - rD), abs(r_low - rD))
                c_high = min(n, cK + k)
                c_low = max(0, cK - k)
                worst_col = max(abs(c_high - cD), abs(c_low - cD))
                worst_cheb = max(worst_row, worst_col)
                return worst_cheb <= k
            lo = 0
            hi = 2 * n
            while lo < hi:
                mid = (lo + hi) // 2
                if ok(mid):
                    hi = mid
                else:
                    lo = mid + 1
            print(lo)
if __name__ == "__main__":
    Solution().solve()