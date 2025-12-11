import sys
input = sys.stdin.readline

def next_ge(x, must, forbid):
    if must & forbid:
        return -1
    y = x
    while True:
        clash = y & forbid
        if clash:
            k = (clash & -clash).bit_length() - 1
            y += (1 << (k + 1)) - (y & ((1 << (k + 1)) - 1))
            continue
        need = must & ~y
        if need:
            k = (need & -need).bit_length() - 1
            y += (1 << k) - (y & ((1 << k) - 1))
            continue
        return y

def solve(n, a, b):
    mand = [0] * n
    mand[0] = a[0]
    mand[-1] = a[-1]
    for i in range(1, n - 1):
        mand[i] = a[i - 1] | a[i]

    B = [0] * n
    B[0] = next_ge(b[0], mand[0], 0)
    if B[0] == -1:
        return -1

    ops = B[0] - b[0]
    i = 0
    while i < n - 1:
        left = B[i]
        if (left & a[i]) != a[i]:
            return -1

        forbid = left & ~a[i]
        must = mand[i + 1]

        if forbid & must:
            new_left = next_ge(left + 1, mand[i], forbid & must)
            if new_left == -1:
                return -1
            ops += new_left - left
            B[i] = new_left
            if i:
                i -= 1
            continue

        right = next_ge(max(b[i + 1], must), must, forbid)
        if right == -1:
            new_left = next_ge(left + 1, mand[i], forbid)
            if new_left == -1:
                return -1
            ops += new_left - left
            B[i] = new_left
            if i:
                i -= 1
            continue

        B[i + 1] = right
        ops += right - b[i + 1]
        i += 1

    return ops

# Driver as per your format
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

for _ in range(t):
    n, a, b = test_cases[_]
    print(solve(n, a, b))
