def can_pack(bl, baseW, baseH):
    usedH = 0
    rowW = 0
    rowH = 0
    for s in bl:
        if s > baseW or s > baseH:
            return False
        if rowW + s <= baseW:
            rowW += s
            rowH = max(rowH, s)
        else:
            usedH += rowH
            if usedH + s > baseH:
                return False
            rowW = s
            rowH = s
    usedH += rowH
    return usedH <= baseH

def precompute_bottom_lists():
    for n in range(2, MAX_N + 1):
        fib_arr[0] = 1
        fib_arr[1] = 2
        for i in range(2, n):
            fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
        full_mask = (1 << n) - 1
        fmax = fib_arr[n-1]
        sum_mask = [0] * (1 << n)
        for mask in range(1, full_mask + 1):
            lsb = mask & -mask
            idx = (lsb).bit_length() - 1
            sum_mask[mask] = sum_mask[mask ^ lsb] + fib_arr[idx]
        dp = [0] * (1 << n)
        for H in range(1, MAX_DIM + 1):
            if H < fmax:
                continue
            dp[0] = 0
            for mask in range(1, full_mask + 1):
                if sum_mask[mask] <= H:
                    dp[mask] = 1
                else:
                    best = n + 1
                    s = (mask - 1) & mask
                    while s:
                        if sum_mask[s] <= H:
                            other = mask ^ s
                            best = min(best, dp[other] + 1)
                        s = (s - 1) & mask
                    dp[mask] = best

            S = dp[full_mask]
            if S > n:
                continue
            valid_subsets = [[] for _ in range(1 << n)]
            for mask in range(1, full_mask + 1):
                lsb = mask & -mask
                i = (lsb).bit_length() - 1
                rem = mask ^ (1 << i)
                s = rem
                while True:
                    s_full = s | (1 << i)
                    if sum_mask[s_full] <= H:
                        valid_subsets[mask].append(s_full)
                    if s == 0:
                        break
                    s = (s - 1) & rem
            bottom_sets = set()
            bottoms = []
            def dfs(rem_mask, bins_left):
                if bins_left == 1:
                    if sum_mask[rem_mask] <= H:
                        idx = rem_mask.bit_length() - 1
                        bottoms.append(fib_arr[idx])
                        bl = sorted(bottoms, reverse=True)
                        bottom_sets.add(tuple(bl))
                        bottoms.pop()
                    return
                for s in valid_subsets[rem_mask]:
                    idx = s.bit_length() - 1
                    bottoms.append(fib_arr[idx])
                    dfs(rem_mask ^ s, bins_left - 1)
                    bottoms.pop()
            dfs(full_mask, S)
            out_list = bottom_lists_table[n][H]
            out_list.extend([list(bl) for bl in bottom_sets])

import sys
sys.setrecursionlimit(1 << 25)
MAX_N = 10
MAX_DIM = 150
INF = 10**9 + 7
bottom_lists_table = [[[] for _ in range(MAX_DIM + 1)] for _ in range(MAX_N + 1)]
fib_arr = [0] * MAX_N
precompute_bottom_lists()
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    boxes = [tuple(map(int, input().split())) for _ in range(m)]
    fib_n = [0] * n
    fib_n[0] = 1
    if n >= 2:
        fib_n[1] = 2
    for i in range(2, n):
        fib_n[i] = fib_n[i-1] + fib_n[i-2]
    fmax = fib_n[n-1]
    ans = []
    for box in boxes:
        dims = list(box)
        ok = False
        for hidx in range(3):
            if ok:
                break
            H = dims[hidx]
            if H < fmax:
                continue
            b1 = dims[(hidx + 1) % 3]
            b2 = dims[(hidx + 2) % 3]
            bottom_lists = bottom_lists_table[n][H]
            if not bottom_lists:
                continue
            for bl in bottom_lists:
                if can_pack(bl, b1, b2) or can_pack(bl, b2, b1):
                    ok = True
                    break
        ans.append('1' if ok else '0')
    print(''.join(ans))