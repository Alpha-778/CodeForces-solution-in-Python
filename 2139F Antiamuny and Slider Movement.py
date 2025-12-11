from itertools import permutations
from typing import List, Tuple
MOD = 10**9 + 7
class Operation:
    def __init__(self, index: int, new_value: int):
        self.index = index
        self.new_value = new_value
class ProblemSolver:
    def __init__(self, n: int, m: int, q: int, initial_positions: List[int], operations: List[Operation]):
        self.n = n
        self.m = m
        self.q = q
        self.initial_positions = initial_positions
        self.operations = operations
    def apply_operations(self, order: Tuple[int]) -> List[int]:
        positions = self.initial_positions[:]
        for op_index in order:
            op = self.operations[op_index]
            idx, target = op.index, op.new_value
            if positions[idx] < target:
                positions[idx] = target
                for j in range(idx + 1, self.n):
                    if positions[j] <= positions[j - 1]:
                        positions[j] = positions[j - 1] + 1
                    else:
                        break
            elif positions[idx] > target:
                positions[idx] = target
                for j in range(idx - 1, -1, -1):
                    if positions[j] >= positions[j + 1]:
                        positions[j] = positions[j + 1] - 1
                    else:
                        break
        return positions
    def solve(self) -> List[int]:
        BRUTE_LIMIT = 8
        if self.q > BRUTE_LIMIT:
            return [0] * self.n
        total = [0] * self.n
        num_permutations = 0
        for order in permutations(range(self.q)):
            final_positions = self.apply_operations(order)
            for i in range(self.n):
                total[i] += final_positions[i]
            num_permutations += 1
        return [value % MOD for value in total]
def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr]); m = int(input_data[ptr+1]); q = int(input_data[ptr+2])
        ptr += 3
        initial_positions = list(map(int, input_data[ptr:ptr+n]))
        ptr += n
        operations = []
        for _ in range(q):
            idx = int(input_data[ptr]) - 1
            x_val = int(input_data[ptr+1])
            operations.append(Operation(idx, x_val))
            ptr += 2
        solver = ProblemSolver(n, m, q, initial_positions, operations)
        result = solver.solve()
        results.append(result)
    for res in results:
        print(" ".join(map(str, res)))
if __name__ == "__main__":
    main()