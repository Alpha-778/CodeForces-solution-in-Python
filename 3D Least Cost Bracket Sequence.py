import sys
import heapq
def main():
    pattern = input()
    m = pattern.count('?')
    jokers = []
    for _ in range(m):
        a, b = map(int, input().split())
        jokers.append((a, b))
    is_joker = [False] * len(pattern)
    pattern = list(pattern)
    total_cost = 0
    j = 0
    for i in range(len(pattern)):
        if pattern[i] == '?':
            is_joker[i] = True
            pattern[i] = ')'
            total_cost += jokers[j][1]
            j += 1
    st = 0
    heap = []
    k = 0
    for i in range(len(pattern)):
        if is_joker[i]:
            diff = jokers[k][0] - jokers[k][1]
            heapq.heappush(heap, (diff, i))
            k += 1
        if pattern[i] == '(':
            st += 1
        elif pattern[i] == ')':
            st -= 1
        if st < 0:
            if heap:
                diff, idx = heapq.heappop(heap)
                total_cost += diff
                pattern[idx] = '('
                st += 2
            else:
                break
    if st != 0:
        print("-1")
    else:
        print(total_cost)
        print("".join(pattern))
if __name__ == "__main__":
    main()