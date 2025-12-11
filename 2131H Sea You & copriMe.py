import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)

def read_int():
    return int(sys.stdin.readline())

def read_list():
    return list(map(int, sys.stdin.readline().split()))

LIM = 1000000 + 5
spf = [0] * LIM
mu = [0] * LIM
sieve_done = False

def init_sieve():
    global sieve_done
    if sieve_done:
        return
    primes = []
    mu[1] = 1
    for i in range(2, LIM):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            x = p * i
            if x >= LIM:
                break
            spf[x] = p
            if p == spf[i]:
                mu[x] = 0
                break
            else:
                mu[x] = -mu[i]
    sieve_done = True

def get_prime_factors(x):
    factors = []
    while x > 1:
        p = spf[x]
        factors.append(p)
        while x % p == 0:
            x //= p
    return factors

def get_square_divisors(pf):
    divisors = [1]
    for p in pf:
        size_now = len(divisors)
        for i in range(size_now):
            divisors.append(divisors[i] * p)
    return divisors

init_sieve()

t = read_int()
for _ in range(t):
    nm = read_list()
    if len(nm) < 2:
        break
    n, m = nm
    arr = [0] + read_list()

    count_arr = [0] * (m + 1)
    for idx in range(1, n + 1):
        count_arr[arr[idx]] += 1

    g = [0] * (m + 1)
    for d in range(1, m + 1):
        total = 0
        for k in range(d, m + 1, d):
            total += count_arr[k]
        g[d] = total

    id_map = {}
    vals = []
    positions = []
    for i in range(1, n + 1):
        x = arr[i]
        if x in id_map:
            positions[id_map[x]].append(i)
        else:
            idx_new = len(vals)
            id_map[x] = idx_new
            vals.append(x)
            positions.append([i])

    U = len(vals)
    pfv = [[] for _ in range(U)]
    sqdv = [[] for _ in range(U)]
    for z in range(U):
        if vals[z] == 1:
            pfv[z] = []
            sqdv[z] = [1]
        else:
            pfv[z] = get_prime_factors(vals[z])
            sqdv[z] = get_square_divisors(pfv[z])

    def F(z, gg):
        s = 0
        for d in sqdv[z]:
            s += mu[d] * gg[d]
        return s

    ones = []
    if 1 in id_map:
        z_one = id_map[1]
        for idx in positions[z_one]:
            ones.append(idx)

    if len(ones) >= 4:
        print(ones[0], ones[1], ones[2], ones[3])
        continue
    if len(ones) == 3:
        other = -1
        for i in range(1, n + 1):
            if i not in ones:
                other = i
                break
        if other == -1:
            print(0)
        else:
            print(ones[0], ones[1], ones[2], other)
        continue
    if len(ones) == 2:
        x, y = -1, -1
        for i in range(1, n + 1):
            if i in ones:
                continue
            if x == -1:
                x = i
            elif y == -1:
                y = i
                break
        if y == -1:
            print(0)
        else:
            print(ones[0], x, ones[1], y)
        continue

    done_flag = False
    for z in range(U):
        if done_flag:
            break
        if vals[z] == 1:
            continue
        if len(positions[z]) >= 2:
            cop_val = F(z, g)
            if cop_val >= 2:
                v = vals[z]
                j_idx, k_idx = -1, -1
                for i in range(1, n + 1):
                    if math.gcd(v, arr[i]) == 1:
                        if j_idx == -1:
                            j_idx = i
                        else:
                            k_idx = i
                            break
                if j_idx != -1 and k_idx != -1:
                    print(positions[z][0], j_idx, positions[z][1], k_idx)
                    done_flag = True
    if done_flag:
        continue

    if len(ones) == 1:
        o = ones[0]
        ok_flag = False
        for z in range(U):
            if ok_flag:
                break
            if vals[z] == 1:
                continue
            cop_no1 = F(z, g) - 1
            if cop_no1 >= 1:
                i_idx = positions[z][0]
                j_idx = -1
                for t in range(1, n + 1):
                    if t != o and t != i_idx and math.gcd(vals[z], arr[t]) == 1:
                        j_idx = t
                        break
                if j_idx == -1:
                    continue
                k_idx = -1
                for t in range(1, n + 1):
                    if t not in (o, i_idx, j_idx):
                        k_idx = t
                        break
                if k_idx == -1:
                    print(0)
                    ok_flag = True
                    break
                print(i_idx, j_idx, o, k_idx)
                ok_flag = True
        if not ok_flag:
            print(0)
        continue

    deg_val = [0] * U
    for z in range(U):
        fz = F(z, g)
        if vals[z] == 1:
            fz -= 1
        deg_val[z] = fz

    def adjust(idx, delta):
        z = id_map[arr[idx]]
        for d in sqdv[z]:
            g[d] += delta

    def find_second(b1, b2):
        for r in range(1, n + 1):
            if r == b1 or r == b2:
                continue
            zr = id_map[arr[r]]
            s = 0
            for d in sqdv[zr]:
                s += mu[d] * g[d]
            if arr[r] == 1:
                s -= 1
            if s >= 1:
                for t in range(1, n + 1):
                    if t not in (b1, b2, r) and math.gcd(arr[r], arr[t]) == 1:
                        return (r, t)
        return (-1, -1)

    leaf_i, leaf_j = -1, -1
    for z in range(U):
        if deg_val[z] == 1:
            ii = positions[z][0]
            jj = -1
            for t in range(1, n + 1):
                if t != ii and math.gcd(arr[ii], arr[t]) == 1:
                    jj = t
                    break
            if jj != -1:
                leaf_i, leaf_j = ii, jj
                break
    if leaf_i != -1:
        adjust(leaf_i, -1)
        adjust(leaf_j, -1)
        pr = find_second(leaf_i, leaf_j)
        if pr[0] != -1:
            print(leaf_i, leaf_j, pr[0], pr[1])
            continue
        else:
            adjust(leaf_i, 1)
            adjust(leaf_j, 1)
            print(0)
            continue
    order_idx = []
    for z in range(U):
        if deg_val[z] >= 1:
            order_idx.extend(positions[z])
    order_idx.sort(key=lambda idx: (deg_val[id_map[arr[idx]]], idx))
    found_flag = False
    for ii in order_idx:
        if found_flag:
            break
        take_limit = min(30, n - 1)
        cand = []
        for t in range(1, n + 1):
            if t != ii and math.gcd(arr[ii], arr[t]) == 1:
                cand.append(t)
                if len(cand) >= take_limit:
                    break
        for jj in cand:
            adjust(ii, -1)
            adjust(jj, -1)
            pr = find_second(ii, jj)
            if pr[0] != -1:
                print(ii, jj, pr[0], pr[1])
                found_flag = True
                break
            adjust(ii, 1)
            adjust(jj, 1)
    if not found_flag:
        print(0)