import sys
from collections import deque
data = sys.stdin.read().strip().split()
it = iter(data)
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    ss = next(it).strip()
    tt = next(it).strip()
    cur = list(ss)
    ops = []
    for i in range(0, n - 4):
        if cur[i] == tt[i]:
            continue
        if cur[i] == cur[i + 1]:
            ops.append((i + 1, i + 2))
            cur[i] = '1' if cur[i] == '0' else '0'
            cur[i + 1] = '1' if cur[i + 1] == '0' else '0'
        else:
            if cur[i + 1] == cur[i + 2]:
                ops.append((i + 2, i + 3))
                cur[i + 1] = '1' if cur[i + 1] == '0' else '0'
                cur[i + 2] = '1' if cur[i + 2] == '0' else '0'
                ops.append((i + 1, i + 3))
                cur[i] = '1' if cur[i] == '0' else '0'
                cur[i + 1] = '1' if cur[i + 1] == '0' else '0'
                cur[i + 2] = '1' if cur[i + 2] == '0' else '0'
            else:
                ops.append((i + 1, i + 3))
                cur[i] = '1' if cur[i] == '0' else '0'
                cur[i + 1] = '1' if cur[i + 1] == '0' else '0'
                cur[i + 2] = '1' if cur[i + 2] == '0' else '0'
    bas = n - 4
    start_st = 0
    for j in range(4):
        start_st |= (ord(cur[bas + j]) - ord('0')) << j
    goal_st = 0
    for j in range(4):
        goal_st |= (ord(tt[bas + j]) - ord('0')) << j
    if start_st != goal_st:
        dis = [-1] * 16
        pre = [-1] * 16
        ol = [-1] * 16
        oor = [-1] * 16
        q = deque()
        q.append(start_st)
        dis[start_st] = 0
        reach = False
        while q and not reach:
            ust = q.popleft()
            for lrel in range(4):
                for rrel in range(lrel + 1, 4):
                    isp = True
                    length = rrel - lrel + 1
                    for jj in range(length // 2):
                        lb = (ust >> (lrel + jj)) & 1
                        rb = (ust >> (rrel - jj)) & 1
                        if lb != rb:
                            isp = False
                            break
                    if isp:
                        nst = ust
                        for k in range(lrel, rrel + 1):
                            nst ^= 1 << k
                        if dis[nst] == -1:
                            dis[nst] = dis[ust] + 1
                            pre[nst] = ust
                            ol[nst] = bas + lrel + 1
                            oor[nst] = bas + rrel + 1
                            q.append(nst)
                            if nst == goal_st:
                                reach = True
                                break
                if reach:
                    break
        if not reach or dis[goal_st] > 8:
            out.append("-1")
            continue
        path = []
        cs = goal_st
        while cs != start_st:
            path.append((ol[cs], oor[cs]))
            cs = pre[cs]
        path.reverse()
        for a, b in path:
            ops.append((a, b))
    if len(ops) > 2 * n:
        out.append("-1")
    else:
        out.append(str(len(ops)))
        for a, b in ops:
            out.append(str(a) + " " + str(b))
sys.stdout.write("\n".join(out))