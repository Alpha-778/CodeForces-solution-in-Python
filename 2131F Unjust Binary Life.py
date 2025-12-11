import sys
import bisect

def solve():
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    pa = [0] * (n + 1)
    pb = [0] * (n + 1)
    for i in range(n):
        pa[i + 1] = pa[i] + (ord(a[i]) - ord('0'))
        pb[i + 1] = pb[i] + (ord(b[i]) - ord('0'))
    va = [0] * n
    vb = [0] * n
    for i in range(n):
        va[i] = 2 * pa[i + 1] - (i + 1)
        vb[i] = 2 * pb[i + 1] - (i + 1)
    vb.sort()
    p_sum_vb = [0] * (n + 1)
    for i in range(n):
        p_sum_vb[i + 1] = p_sum_vb[i] + vb[i]
    total_sum_vb = p_sum_vb[n]
    abs_sum = 0
    for c in va:
        k = bisect.bisect_left(vb, -c)
        abs_sum += c * (n - 2 * k) + total_sum_vb - 2 * p_sum_vb[k]
    total_xy_sum = n * n * (n + 1)
    ans = (total_xy_sum - abs_sum) // 2
    sys.stdout.write(str(ans) + "\n")

data = sys.stdin.read().strip().split()
t = int(data[0])
index = 1
for _ in range(t):
    n_val = int(data[index])
    a_str = data[index + 1]
    b_str = data[index + 2]
    n = n_val
    a = a_str
    b = b_str
    pa = [0] * (n + 1)
    pb = [0] * (n + 1)
    for i in range(n):
        pa[i + 1] = pa[i] + (ord(a[i]) - ord('0'))
        pb[i + 1] = pb[i] + (ord(b[i]) - ord('0'))
    va = [0] * n
    vb = [0] * n
    for i in range(n):
        va[i] = 2 * pa[i + 1] - (i + 1)
        vb[i] = 2 * pb[i + 1] - (i + 1)
    vb.sort()
    p_sum_vb = [0] * (n + 1)
    for i in range(n):
        p_sum_vb[i + 1] = p_sum_vb[i] + vb[i]
    total_sum_vb = p_sum_vb[n]
    abs_sum = 0
    for c in va:
        k = bisect.bisect_left(vb, -c)
        abs_sum += c * (n - 2 * k) + total_sum_vb - 2 * p_sum_vb[k]
    total_xy_sum = n * n * (n + 1)
    ans = (total_xy_sum - abs_sum) // 2
    print(ans)
    index += 3