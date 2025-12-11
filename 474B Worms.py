import bisect
n = int(input())
a = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))
prefix_sums = []
current_sum = 0
for worms in a:
    current_sum += worms
    prefix_sums.append(current_sum)
for q in queries:
    pile_index = bisect.bisect_left(prefix_sums, q)
    print(pile_index + 1)