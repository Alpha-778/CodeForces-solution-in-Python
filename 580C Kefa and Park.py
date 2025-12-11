from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def kefa_and_park(n, m, has_cat, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    valid_restaurants = 0
    def dfs(node, parent, consecutive_cats):
        nonlocal valid_restaurants
        if has_cat[node - 1]:
            consecutive_cats += 1
        else:
            consecutive_cats = 0

        if consecutive_cats > m:
            return
        is_leaf = True
        for neighbor in tree[node]:
            if neighbor != parent:
                is_leaf = False
                dfs(neighbor, node, consecutive_cats)
        if is_leaf:
            valid_restaurants += 1
    dfs(1, -1, 0)
    return valid_restaurants
# Example 1
n,m=map(int,input().split())
has_cat = list(map(int,input().split()))
edges = [list(map(int,input().split())) for i in range(n-1)]
print(kefa_and_park(n, m, has_cat, edges))