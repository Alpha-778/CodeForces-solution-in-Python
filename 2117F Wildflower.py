MODULO = 10**9 + 7

def fast_exp(base_exp):
    result = 1
    base = 2
    power = base_exp
    while power > 0:
        if power & 1:
            result = (result * base) % MODULO
        base = (base * base) % MODULO
        power >>= 1
    return result

t = int(input())
rec = []
for _ in range(t):
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    rec.append([n, edges])
for _ in range(t):
    n, edges = rec[_]
    adjacency = [[] for _ in range(n + 1)]
    for x, y in edges:
        adjacency[x].append(y)
        adjacency[y].append(x)
    parents = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    stack = [1]
    parents[1] = -1
    while stack:
        current = stack.pop()
        for neighbor in adjacency[current]:
            if neighbor != parents[current]:
                parents[neighbor] = current
                children[current].append(neighbor)
                stack.append(neighbor)
    leaf_nodes = [i for i in range(1, n + 1) if not children[i]]
    if len(leaf_nodes) > 2:
        print(0)
        continue
    if len(leaf_nodes) == 1:
        print(fast_exp(n))
        continue
    candidate = -1
    for i in range(1, n + 1):
        if len(children[i]) == 2:
            candidate = i
            break
    first_child, second_child = children[candidate]
    def count_subtree_size(root):
        count = 0
        to_visit = [root]
        while to_visit:
            node = to_visit.pop()
            count += 1
            to_visit.extend(children[node])
        return count
    size1 = count_subtree_size(first_child)
    size2 = count_subtree_size(second_child)
    diff = abs(size1 - size2)
    remaining = n - size1 - size2
    if diff == 0:
        factor = 2
    else:
        factor = (3 * fast_exp(diff - 1)) % MODULO
    answer = (fast_exp(remaining) * factor) % MODULO
    print(answer)