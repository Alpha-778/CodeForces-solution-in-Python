import sys
import threading
def task():
    t = int(sys.stdin.readline())
    q = 0
    while q < t:
        sz = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = [0 for _ in range(55)]
        z = 0
        j = 0
        while j < sz:
            val = a[j]
            b[val] += 1
            j += 1
        h = 0
        p = min(b[0], b[1])
        h = h + p * 2
        b[0] = b[0] - p
        b[1] = b[1] - p
        g = b[0]
        h = h + g
        b[0] = 0
        u = 0
        while u < 55:
            if b[u] > 0:
                h = h + (u * b[u])
            u = u + 1
        print(h)
        q += 1
threading.Thread(target=task).start()