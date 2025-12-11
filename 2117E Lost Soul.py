import sys
input = sys.stdin.readline

class MaxSegmentTree:
    def __init__(self, size=0):
        self.size = 1
        while self.size <= size:
            self.size <<= 1
        self.data = [-1] * (2 * self.size)
    def update(self, index, value):
        pos = index + self.size
        self.data[pos] = value
        pos >>= 1
        while pos > 0:
            self.data[pos] = max(self.data[pos << 1], self.data[(pos << 1) | 1])
            pos >>= 1
    def query_max(self):
        return self.data[1]

t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rec.append([n, a, b])
for _ in range(t):
    n, a, b = rec[_]
    max_val = n
    pos_even = [[] for __ in range(max_val + 1)]
    pos_odd = [[] for __ in range(max_val + 1)]
    for i in range(n):
        if i % 2 == 0:
            pos_even[a[i]].append(i)
        else:
            pos_odd[a[i]].append(i)
        if ((i % 2) ^ 1) == 0:
            pos_even[b[i]].append(i)
        else:
            pos_odd[b[i]].append(i)
    last_even = [-1] * (max_val + 1)
    last_odd = [-1] * (max_val + 1)
    for i in range(n):
        if i % 2 == 0:
            last_even[a[i]] = i
        else:
            last_odd[a[i]] = i
        if ((i % 2) ^ 1) == 0:
            last_even[b[i]] = i
        else:
            last_odd[b[i]] = i
    best = -1
    for val in range(1, max_val + 1):
        if last_even[val] != -1 and last_odd[val] != -1:
            best = max(best, min(last_even[val], last_odd[val]))
    answer = 0 if best == -1 else best + 1
    right_ptr_even = [len(pos_even[i]) - 1 for i in range(max_val + 1)]
    right_ptr_odd = [len(pos_odd[i]) - 1 for i in range(max_val + 1)]
    left_even = [-1] * (max_val + 1)
    left_odd = [-1] * (max_val + 1)
    segtree = MaxSegmentTree(max_val + 1)
    def compute_val(v):
        L_even, L_odd = left_even[v], left_odd[v]
        R_even = pos_even[v][right_ptr_even[v]] if right_ptr_even[v] >= 0 else -1
        R_odd = pos_odd[v][right_ptr_odd[v]] if right_ptr_odd[v] >= 0 else -1
        if R_even != -1:
            R_even -= 1
        if R_odd != -1:
            R_odd -= 1
        candidate_0 = max(L_even, R_odd)
        candidate_1 = max(L_odd, R_even)
        if candidate_0 == -1 or candidate_1 == -1:
            return -1
        return min(candidate_0, candidate_1)
    for val in range(1, max_val + 1):
        segtree.update(val, compute_val(val))
    for day in range(n):
        def adjust_positions(v):
            while right_ptr_even[v] >= 0 and pos_even[v][right_ptr_even[v]] <= day:
                right_ptr_even[v] -= 1
            while right_ptr_odd[v] >= 0 and pos_odd[v][right_ptr_odd[v]] <= day:
                right_ptr_odd[v] -= 1
            segtree.update(v, compute_val(v))
        adjust_positions(a[day])
        adjust_positions(b[day])
        current_max = segtree.query_max()
        if current_max != -1:
            answer = max(answer, current_max + 1)
        if day % 2 == 0:
            left_even[a[day]] = day
        else:
            left_odd[a[day]] = day
        if ((day % 2) ^ 1) == 0:
            left_even[b[day]] = day
        else:
            left_odd[b[day]] = day
        segtree.update(a[day], compute_val(a[day]))
        segtree.update(b[day], compute_val(b[day]))
    print(answer)