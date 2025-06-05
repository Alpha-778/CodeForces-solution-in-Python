n, v = map(int, input().split())
kayaks = []
catamarans = []
for i in range(1, n + 1):
    t, p = map(int, input().split())
    if t == 1:
        kayaks.append((p, i))
    else:
        catamarans.append((p, i))
kayaks.sort(reverse=True)
catamarans.sort(reverse=True)
kayak_prefix = [0]
for cap, _ in kayaks:
    kayak_prefix.append(kayak_prefix[-1] + cap)
catamaran_prefix = [0]
for cap, _ in catamarans:
    catamaran_prefix.append(catamaran_prefix[-1] + cap)
max_capacity = 0
best_kayaks = 0
best_catamarans = 0
for c in range(0, len(catamarans) + 1):
    space_used = 2 * c
    if space_used > v:
        break
    remaining_space = v - space_used
    k = min(remaining_space, len(kayaks))
    total_capacity = catamaran_prefix[c] + kayak_prefix[k]
    if total_capacity > max_capacity:
        max_capacity = total_capacity
        best_kayaks = k
        best_catamarans = c
print(max_capacity)
result_indices = [i for _, i in kayaks[:best_kayaks]] + [i for _, i in catamarans[:best_catamarans]]
print(" ".join(map(str, result_indices)))