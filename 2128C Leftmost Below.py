import sys
def main():
    reader = sys.stdin.readline
    total_tests = int(reader())
    for _ in range(total_tests):
        n = int(reader())
        parts = reader().strip().split()
        sequence = []
        for token in parts:
            sequence.append(int(token))
        current_min = sequence[0]
        is_valid = True
        i = 1
        while i < n:
            value = sequence[i]
            limit1 = current_min * 2
            limit2 = current_min * (current_min + 1) // 2
            if value >= limit1 or value > limit2:
                is_valid = False
                break
            if value < current_min:
                current_min = value
            i += 1
        if is_valid:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
if __name__ == "__main__":
    main()