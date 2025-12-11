from bisect import bisect_left
import sys
input = sys.stdin.readline
class SegmentNode:
    def __init__(self):
        self.Ls = []
        self.Rs = []
        self.sufMinR = []
class Solution:
    def __init__(self):
        self.seg = []
        self.SZ = 0
        self.INF = 0
    def build(self, v):
        L1, R1 = self.seg[v*2].Ls, self.seg[v*2].Rs
        L2, R2 = self.seg[v*2+1].Ls, self.seg[v*2+1].Rs
        Lout, Rout = [], []
        i = j = 0
        while i < len(L1) or j < len(L2):
            if j == len(L2) or (i < len(L1) and L1[i] <= L2[j]):
                Lout.append(L1[i])
                Rout.append(R1[i])
                i += 1
            else:
                Lout.append(L2[j])
                Rout.append(R2[j])
                j += 1
        S = [0]*len(Rout)
        if Rout:
            S[-1] = Rout[-1]
            for t in range(len(Rout)-2, -1, -1):
                S[t] = min(Rout[t], S[t+1])
        self.seg[v].Ls, self.seg[v].Rs, self.seg[v].sufMinR = Lout, Rout, S
    def getMinR(self, v, tl, tr, l, r, Lthresh):
        if l > tr or r < tl:
            return self.INF
        if l <= tl and tr <= r:
            Ls = self.seg[v].Ls
            if not Ls:
                return self.INF
            idx = bisect_left(Ls, Lthresh)
            if idx == len(Ls):
                return self.INF
            return self.seg[v].sufMinR[idx]
        tm = (tl + tr) // 2
        left = self.getMinR(v*2, tl, tm, l, r, Lthresh)
        right = self.getMinR(v*2+1, tm+1, tr, l, r, Lthresh)
        return min(left, right)
    def solve(self):
        T = int(input())
        for _ in range(T):
            n, q = map(int, input().split())
            a = [0] + list(map(int, input().split()))
            L = [0]*(n+1)
            R = [n+1]*(n+1)
            st = []
            for i in range(1, n+1):
                while st and a[st[-1]] <= a[i]:
                    st.pop()
                L[i] = st[-1] if st else 0
                st.append(i)
            st.clear()
            for i in range(n, 0, -1):
                while st and a[st[-1]] >= a[i]:
                    st.pop()
                R[i] = st[-1] if st else n+1
                st.append(i)
            self.SZ = 1
            while self.SZ < n:
                self.SZ <<= 1
            self.seg = [SegmentNode() for _ in range(2*self.SZ)]
            for i in range(1, n+1):
                v = self.SZ + i - 1
                self.seg[v].Ls = [L[i]]
                self.seg[v].Rs = [R[i]]
                self.seg[v].sufMinR = [R[i]]
            for v in range(self.SZ-1, 0, -1):
                self.build(v)
            self.INF = n+1
            for _ in range(q):
                l, r = map(int, input().split())
                if r-l+1 < 3:
                    print("YES")
                    continue
                mnR = self.getMinR(1, 1, self.SZ, l, r, l)
                print("NO" if mnR <= r else "YES")
if __name__ == "__main__":
    Solution().solve()