import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd_heap = []
    diff = 0              
    max_pref = 0          
    prev_diff = 0
    ans = 0
    for i in range(1, n + 1):
        val = a[i - 1]
        if i % 2 == 1:
            heapq.heappush(odd_heap, -val)
            diff -= val
        else:
            diff += val
        if i >= 2:
            need = max_pref - diff
            while need > 0:
                if not odd_heap:
                    break
                top = -heapq.heappop(odd_heap)
                take = top if top <= need else need
                top -= take
                ans += take
                diff += take 
                need -= take
                if top > 0:
                    heapq.heappush(odd_heap, -top)
        max_pref = max(max_pref, prev_diff)
        prev_diff = diff
    print(ans)