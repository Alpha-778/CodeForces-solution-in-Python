from bisect import bisect_left
from collections import deque
t=int(input())
rec=[]
for _ in range(t):
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))
    directions = list(map(int, input().split()))
    total_states = n * k * 2
    forward_map = [-1] * total_states
    reverse_map = [[] for _ in range(total_states)]
    def get_state(index, direction, residue):
        return ((index << 1) | direction) * k + residue
    for pos in range(n):
        for d in range(2):
            direction_step = 1 if d == 0 else -1
            for mod_val in range(k):
                curr_state = get_state(pos, d, mod_val)
                new_dir = -direction_step if mod_val == directions[pos] else direction_step
                new_dir_idx = 0 if new_dir == 1 else 1
                next_pos = pos + new_dir
                if 0 <= next_pos < n:
                    gap = abs(positions[next_pos] - positions[pos]) % k
                    next_residue = (mod_val + gap) % k
                    next_state = get_state(next_pos, new_dir_idx, next_residue)
                    forward_map[curr_state] = next_state
                    reverse_map[next_state].append(curr_state)
                else:
                    forward_map[curr_state] = -1
    reachable = [False] * total_states
    q = deque()
    for state in range(total_states):
        if forward_map[state] == -1:
            reachable[state] = True
            q.append(state)
    while q:
        current = q.popleft()
        for prev in reverse_map[current]:
            if not reachable[prev]:
                reachable[prev] = True
                q.append(prev)
    queries = int(input())
    targets = list(map(int, input().split()))
    for val in targets:
        pos_index = bisect_left(positions, val)
        if pos_index == n:
            print("YES")
        else:
            offset = abs(positions[pos_index] - val) % k
            state = get_state(pos_index, 0, offset)
            print("YES" if reachable[state] else "NO")