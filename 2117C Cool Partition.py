t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    rec.append([n, arr])
for _ in range(t):
    n, arr = rec[_]
    next_pos = [n + 2] * (n + 2)
    last_pos = [n + 1] * (n + 2)
    for i in range(n, 0, -1):
        next_pos[i] = last_pos[arr[i]]
        last_pos[arr[i]] = i
    start_idx = 1
    segment_count = 0
    while start_idx <= n:
        end_idx = start_idx
        while True:
            max_next = 0
            for i in range(start_idx, end_idx + 1):
                if next_pos[i] > max_next:
                    max_next = next_pos[i]
            segment_count += 1
            if max_next > n:
                break
            start_idx = end_idx + 1
            end_idx = max_next
        break
    print(segment_count)