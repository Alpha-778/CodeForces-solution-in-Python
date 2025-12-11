class PartitionFinder:
    def __init__(self, n, numbers):
        self.n = n
        self.nums = [0] + numbers
        self.prefix = [0] * (n + 1)
        self.compute_prefix()
    def compute_prefix(self):
        for i in range(1, self.n + 1):
            self.prefix[i] = (self.prefix[i - 1] + self.nums[i]) % 3
    def find_partition(self):
        for l in range(1, self.n - 1):
            for r in range(l + 1, self.n):
                s1 = self.prefix[l]
                s2 = (self.prefix[r] - self.prefix[l] + 3) % 3
                s3 = (self.prefix[self.n] - self.prefix[r] + 3) % 3
                if (s1 == s2 == s3) or (s1 != s2 and s1 != s3 and s2 != s3):
                    return l, r
        return 0, 0
class Solution:
    def __init__(self):
        self.test_cases = int(input())
    def run(self):
        for _ in range(self.test_cases):
            n = int(input())
            arr = list(map(int, input().split()))
            finder = PartitionFinder(n, arr)
            l, r = finder.find_partition()
            print(l, r)
if __name__ == "__main__":
    Solution().run()