class RBSBuilder:
    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.total_open = n // 2
        self.result = ""
    def is_rbs(self, t):
        bal = 0
        for c in t:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0
    def compute_f(self):
        f = 0
        for i in range(self.n):
            a = 1 if self.s[i] == '(' else -1
            f += (1 if i % 2 == 0 else -1) * a
        return f
    def build(self):
        if self.n % 2 == 1:
            return "-1"
        f = self.compute_f()
        diff = self.n - f
        if diff % 4 != 0:
            return "-1"
        k = diff // 4
        if k < 0 or k > (self.n // 2 - 1):
            return "-1"
        open_even = self.total_open - k
        open_odd = self.total_open - open_even
        t = []
        used_open = 0
        used_even_open = 0
        used_odd_open = 0
        total_even_pos = self.n // 2
        total_odd_pos = self.n // 2
        for i in range(self.n):
            parity = i % 2
            min_needed = (i + 2) // 2
            forced = used_open < min_needed
            even_used_up_to_i = (i // 2 + 1) if parity == 0 else ((i + 1) // 2)
            odd_used_up_to_i = (i + 1) - even_used_up_to_i
            rem_even = total_even_pos - even_used_up_to_i
            rem_odd = total_odd_pos - odd_used_up_to_i
            if forced:
                if parity == 0:
                    if open_even - used_even_open <= 0:
                        return "-1"
                    t.append('(')
                    used_open += 1
                    used_even_open += 1
                else:
                    if open_odd - used_odd_open <= 0:
                        return "-1"
                    t.append('(')
                    used_open += 1
                    used_odd_open += 1
            else:
                if parity == 0:
                    if open_even - used_even_open > 0 and open_even - (used_even_open + 1) <= rem_even and open_odd - used_odd_open <= rem_odd:
                        t.append('(')
                        used_open += 1
                        used_even_open += 1
                    else:
                        t.append(')')
                else:
                    if open_odd - used_odd_open > 0 and open_even - used_even_open <= rem_even and open_odd - (used_odd_open + 1) <= rem_odd:
                        t.append('(')
                        used_open += 1
                        used_odd_open += 1
                    else:
                        t.append(')')
        final_t = ''.join(t)
        if not self.is_rbs(final_t) or final_t.count('(') != self.total_open:
            evopen = sum(1 for i in range(self.n) if i % 2 == 0 and final_t[i] == '(')
            if not self.is_rbs(final_t) or evopen != open_even:
                return "-1"
        return final_t
class Solution:
    def __init__(self):
        self.results = []
    def solve(self):
        T = int(input())
        for _ in range(T):
            n = int(input())
            s = input().strip()
            builder = RBSBuilder(n, s)
            res = builder.build()
            print(res)
if __name__ == "__main__":
    Solution().solve()