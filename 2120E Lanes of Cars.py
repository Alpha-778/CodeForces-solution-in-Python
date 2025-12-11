import bisect
import sys

class SegmentData:
    def __init__(self):
        self.total = 0
        self.count = 0
        self.square_sum = 0

class SegmentTree:
    def __init__(self, sequence):
        self.arr = sequence
        self.size = len(sequence)
        self.tree = [SegmentData() for _ in range(4 * self.size)]
        self._build_tree(1, 0, self.size - 1)

    def _build_tree(self, index, l, r):
        if l == r:
            val = self.arr[l]
            node = self.tree[index]
            node.total = val
            node.count = 1
            node.square_sum = val * val
        else:
            mid = (l + r) // 2
            self._build_tree(index * 2, l, mid)
            self._build_tree(index * 2 + 1, mid + 1, r)

            left = self.tree[index * 2]
            right = self.tree[index * 2 + 1]
            merged = self.tree[index]

            merged.total = left.total + right.total
            merged.count = left.count + right.count
            merged.square_sum = left.square_sum + right.square_sum

    def range_query(self, idx, seg_l, seg_r, q_l, q_r):
        if q_r < seg_l or seg_r < q_l:
            return SegmentData()
        if q_l <= seg_l and seg_r <= q_r:
            return self.tree[idx]

        mid = (seg_l + seg_r) // 2
        left_res = self.range_query(idx * 2, seg_l, mid, q_l, q_r)
        right_res = self.range_query(idx * 2 + 1, mid + 1, seg_r, q_l, q_r)

        combined = SegmentData()
        combined.total = left_res.total + right_res.total
        combined.count = left_res.count + right_res.count
        combined.square_sum = left_res.square_sum + right_res.square_sum
        return combined

    def calc_contribs(self, lambda_guess, K_val):
        sum_contrib = 0
        cnt_contrib = 0

        mid_idx = bisect.bisect_left(self.arr, lambda_guess)
        upper_idx = bisect.bisect_right(self.arr, lambda_guess + K_val)

        if lambda_guess + K_val <= 0:
            if mid_idx > 0:
                segment = self.range_query(1, 0, self.size - 1, 0, mid_idx - 1)
                cnt_contrib += segment.count * lambda_guess - segment.total
                sum_contrib += segment.count * (lambda_guess * (lambda_guess + 1) // 2) - (segment.square_sum + segment.total) // 2
        else:
            if mid_idx > 0:
                segment = self.range_query(1, 0, self.size - 1, 0, mid_idx - 1)
                cnt_contrib += segment.count * lambda_guess
                sum_contrib += -K_val * segment.total + segment.count * (lambda_guess * (lambda_guess + 1) // 2)

            if upper_idx > mid_idx:
                segment = self.range_query(1, 0, self.size - 1, mid_idx, upper_idx - 1)
                cnt_contrib += segment.total
                sum_contrib += segment.total * (1 - K_val) + (segment.square_sum - segment.total) // 2

            if self.size > upper_idx:
                segment = self.range_query(1, 0, self.size - 1, upper_idx, self.size - 1)
                val = lambda_guess + K_val
                if val > 0:
                    cnt_contrib += segment.count * val
                    sum_contrib += segment.count * (val * (1 - K_val) + (val - 1) * val // 2)

        return cnt_contrib, sum_contrib

def solve():
    input = sys.stdin.readline
    t_cases = int(input())
    for _ in range(t_cases):
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        total_A = sum(A)

        A.sort()
        tree = SegmentTree(A)
        base = sum(k * a for a in A)

        low, high = -2 * 10**14, 2 * 10**14
        chosen_lambda = 0

        while low <= high:
            mid = (low + high) // 2
            count, _ = tree.calc_contribs(mid, k)
            if count >= total_A:
                chosen_lambda = mid
                high = mid - 1
            else:
                low = mid + 1

        prev_count, partial_sum = tree.calc_contribs(chosen_lambda - 1, k)
        remain = total_A - prev_count
        final_gain = partial_sum + remain * chosen_lambda
        answer = base + final_gain

        print(int(answer))

if __name__ == "__main__":
    solve()
