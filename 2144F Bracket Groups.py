from collections import deque
class TNode:
    def __init__(self):
        self.next = [-1,-1]
        self.link = 0
        self.out = 0
class AC:
    def __init__(self, patterns):
        self.nodes = [TNode()]
        self.build(patterns)
        self.linkify()
    def build(self, patterns):
        for idx, pat in enumerate(patterns):
            v = 0
            for ch in pat:
                c = 0 if ch == '(' else 1
                if self.nodes[v].next[c] == -1:
                    self.nodes[v].next[c] = len(self.nodes)
                    self.nodes.append(TNode())
                v = self.nodes[v].next[c]
            self.nodes[v].out |= (1 << idx)
    def linkify(self):
        q = deque()
        for c in range(2):
            if self.nodes[0].next[c] == -1:
                self.nodes[0].next[c] = 0
            else:
                self.nodes[self.nodes[0].next[c]].link = 0
                q.append(self.nodes[0].next[c])
        while q:
            v = q.popleft()
            outmask = self.nodes[self.nodes[v].link].out
            self.nodes[v].out |= outmask
            for c in range(2):
                u = self.nodes[v].next[c]
                if u != -1:
                    self.nodes[u].link = self.nodes[self.nodes[v].link].next[c]
                    q.append(u)
                else:
                    self.nodes[v].next[c] = self.nodes[self.nodes[v].link].next[c]
class Solver:
    def __init__(self, n, k, pats):
        self.n = n
        self.k = k
        self.pats = pats
        self.removed = [False]*n
        self.remain = n
        self.groups = []
    def solve(self):
        while self.remain > 0:
            rem = [i for i in range(self.n) if not self.removed[i]]
            r = len(rem)
            if r == 0:
                break
            ac = AC([self.pats[i] for i in rem])
            sz = len(ac.nodes)
            half = self.k // 2
            P, O = self.k+1, half+1
            INF = (1 << 64) - 1
            tot = P * O * sz
            dp = [INF]*tot
            def id(pos, opens, state):
                return ((pos * O + opens) * sz + state)
            dp[id(0,0,0)] = 0
            for pos in range(self.k):
                maxOpens = min(half, pos)
                for opens in range(maxOpens+1):
                    balance = 2*opens - pos
                    if balance < 0:
                        continue
                    for state in range(sz):
                        cur = dp[id(pos, opens, state)]
                        if cur == INF:
                            continue
                        if opens < half:
                            ns = ac.nodes[state].next[0]
                            nmask = cur | ac.nodes[ns].out
                            nid = id(pos+1, opens+1, ns)
                            if dp[nid] == INF or bin(nmask).count('1') < bin(dp[nid]).count('1'):
                                dp[nid] = nmask
                        if balance > 0:
                            ns = ac.nodes[state].next[1]
                            nmask = cur | ac.nodes[ns].out
                            nid = id(pos+1, opens, ns)
                            if dp[nid] == INF or bin(nmask).count('1') < bin(dp[nid]).count('1'):
                                dp[nid] = nmask
            bestMask = INF
            bestPop = 1<<20
            for state in range(sz):
                m = dp[id(self.k, half, state)]
                if m == INF:
                    continue
                pc = bin(m).count('1')
                if pc < bestPop:
                    bestPop = pc
                    bestMask = m
            if bestMask == INF or bestPop == r:
                print(-1)
                return
            endState = -1
            for state in range(sz):
                if dp[id(self.k, half, state)] == bestMask:
                    endState = state
                    break
            if endState == -1:
                for state in range(sz):
                    m = dp[id(self.k, half, state)]
                    if m == INF:
                        continue
                    if bin(m).count('1') == bestPop:
                        bestMask = m
                        endState = state
                        break
            if endState == -1:
                print(-1)
                return
            par = [(-1,-1,-1,'')]*tot
            vis = [False]*tot
            qq = deque()
            qq.append((0,0,0))
            vis[id(0,0,0)] = True
            found = False
            while qq and not found:
                pos, opens, state = qq.popleft()
                cur = dp[id(pos, opens, state)]
                if cur == INF:
                    continue
                if pos == self.k and opens == half and state == endState:
                    found = True
                    break
                balance = 2*opens - pos
                if opens < half:
                    ns = ac.nodes[state].next[0]
                    nmask = cur | ac.nodes[ns].out
                    nid = id(pos+1, opens+1, ns)
                    if dp[nid] != INF and bin(nmask).count('1') == bin(dp[nid]).count('1'):
                        if not vis[nid]:
                            vis[nid] = True
                            par[nid] = (pos, opens, state, '(')
                            qq.append((pos+1, opens+1, ns))
                            if pos+1 == self.k and opens+1 == half and ns == endState:
                                found = True
                                break
                if balance > 0:
                    ns = ac.nodes[state].next[1]
                    nmask = cur | ac.nodes[ns].out
                    nid = id(pos+1, opens, ns)
                    if dp[nid] != INF and bin(nmask).count('1') == bin(dp[nid]).count('1'):
                        if not vis[nid]:
                            vis[nid] = True
                            par[nid] = (pos, opens, state, ')')
                            qq.append((pos+1, opens, ns))
                            if pos+1 == self.k and opens == half and ns == endState:
                                found = True
                                break
            curId = id(self.k, half, endState)
            if not vis[curId]:
                found = False
                for state in range(sz):
                    cid = id(self.k, half, state)
                    if vis[cid]:
                        curId = cid
                        found = True
                        break
                if not found:
                    print(-1)
                    return
            res = []
            while True:
                prev_pos, prev_opens, prev_state, ch = par[curId]
                if prev_pos == -1:
                    break
                res.append(ch)
                curId = id(prev_pos, prev_opens, prev_state)
            res = res[::-1]
            if len(res) != self.k:
                res = ['(']*(self.k//2) + [')']*(self.k//2)
            group = []
            for j in range(r):
                if ((bestMask >> j) & 1) == 0:
                    orig = rem[j]
                    group.append(orig+1)
                    self.removed[orig] = True
                    self.remain -= 1
            if not group:
                print(-1)
                return
            self.groups.append(("".join(res), group))
        print(len(self.groups))
        for s, grp in self.groups:
            print(s)
            print(len(grp))
            print(" ".join(map(str, grp)))
def main():
    n, k = map(int, input().split())
    patterns = [input().strip() for _ in range(n)]
    Solver(n, k, patterns).solve()
if __name__ == "__main__":
    main()