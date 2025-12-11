def popcount(x):
    return bin(x).count("1")

def process_case(n, k, arr):
    base_score = sum(popcount(num) for num in arr)
    deltas = []
    for val in arr:
        x = val
        while True:
            bit = (x ^ (x + 1)).bit_length() - 1
            if bit > 60:
                break
            step = 1 << bit
            if step > k:
                break
            deltas.append(step)
            x += step
    deltas.sort()
    total = 0
    gain = 0
    for d in deltas:
        if total + d > k:
            break
        total += d
        gain += 1
    return base_score + gain

def main():
    trials = int(input())
    data = [tuple(map(int, input().split())) + (list(map(int, input().split())),) for _ in range(trials)]
    for n, k, nums in data:
        print(process_case(n, k, nums))

main()