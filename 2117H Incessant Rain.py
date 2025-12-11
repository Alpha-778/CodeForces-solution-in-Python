import sys
import threading
import random

sys.setrecursionlimit(1 << 25)

class TreapNode:
    def __init__(self, idx, val):
        self.l = None
        self.r = None
        self.idx = idx
        self.pri = random.randint(1, 1 << 30)
        self.val = val
        self.maxv = val
        self.minv = val
        self.diff = 0
        self.tag = 0
        self.sz = 1

def apply(node, delta):
    if node:
        node.val += delta
        node.maxv += delta
        node.minv += delta
        node.tag += delta

def push(node):
    if node and node.tag != 0:
        apply(node.l, node.tag)
        apply(node.r, node.tag)
        node.tag = 0

def pull(node):
    if not node:
        return
    node.sz = 1
    node.maxv = node.minv = node.val
    node.diff = 0
    if node.l:
        node.sz += node.l.sz
        node.maxv = max(node.maxv, node.l.maxv)
        node.minv = min(node.minv, node.l.minv)
        node.diff = max(node.diff, node.l.diff)
        node.diff = max(node.diff, node.l.maxv - node.val)
    if node.r:
        node.sz += node.r.sz
        node.maxv = max(node.maxv, node.r.maxv)
        node.minv = min(node.minv, node.r.minv)
        node.diff = max(node.diff, node.r.diff)
        left_max = node.val
        if node.l:
            left_max = max(left_max, node.l.maxv)
        node.diff = max(node.diff, left_max - node.r.minv)

def merge(left, right):
    if not left or not right:
        return left or right
    if left.pri < right.pri:
        push(left)
        left.r = merge(left.r, right)
        pull(left)
        return left
    else:
        push(right)
        right.l = merge(left, right.l)
        pull(right)
        return right

def split(node, key):
    if not node:
        return (None, None)
    push(node)
    if node.idx < key:
        a, b = split(node.r, key)
        node.r = a
        pull(node)
        return node, b
    else:
        a, b = split(node.l, key)
        node.l = b
        pull(node)
        return a, node

t = int(input())
rec = []
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [list(map(int, input().split())) for __ in range(q)]
    rec.append([n, q, a, l])
for _ in range(t):
    n, q, a, l = rec[_]
    a = [0] + a
    roots = [None] * (n + 2)
    pos = [[] for _ in range(n + 2)]
    current = [0] * (n + 2)
    bests = []
    for i in range(1, n + 1):
        pos[a[i]].append(i)
    for val in range(1, n + 1):
        for j, i in enumerate(pos[val]):
            node = TreapNode(i, i - 2 * (j + 1))
            roots[val] = merge(roots[val], node)
        if roots[val]:
            current[val] = (roots[val].diff + 1) // 2
            bests.append(current[val])
    res = []
    for u, v in l:
        old = a[u]
        if old == v:
            res.append(max(bests))
            continue
        bests.remove(current[old])
        x, y = split(roots[old], u)
        y, z = split(y, u + 1)
        apply(z, 2)
        roots[old] = merge(x, z)
        current[old] = (roots[old].diff + 1) // 2 if roots[old] else 0
        bests.append(current[old])
        bests.remove(current[v])
        x, z = split(roots[v], u)
        apply(z, -2)
        left_sz = x.sz if x else 0
        new_node = TreapNode(u, u - 2 * (left_sz + 1))
        roots[v] = merge(merge(x, new_node), z)
        current[v] = (roots[v].diff + 1) // 2
        bests.append(current[v])
        a[u] = v
        res.append(max(bests))
    print(*res)