import sys
input = sys.stdin.read

def prefix_min_sum(arr):
    total = 0
    cur_min = float('inf')
    for x in arr:
        cur_min = min(cur_min, x)
        total += cur_min
    return total

def solve():
    data = input().split()
    idx = 0
    T = int(data[idx]); idx += 1
    results = []
    for _ in range(T):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx + n])); idx += n
        base_score = prefix_min_sum(a)
        best = [base_score] * n
        temp = [0] * n 
        for i in range(n):
            for d in range(1, min(n - i, 201)):
                j = i + d
                for k in range(n):
                    temp[k] = a[k]
                temp[i] += temp[j]
                temp[j] = 0
                score = prefix_min_sum(temp)
                if score > best[d]:
                    best[d] = score
        for i in range(n - 2, -1, -1):
            best[i] = max(best[i], best[i + 1])
        results.append(' '.join(map(str, best)))
    print('\n'.join(results))
solve()