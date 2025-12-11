import sys
import bisect
def read():
    return sys.stdin.readline()
def run():
    q = int(read())
    for _ in range(q):
        arr = read().split()
        n = int(arr[0])
        c = int(arr[1])
        vals = list(map(int, read().split()))
        s = []
        for val in vals:
            bisect.insort(s, val)
        res = 0
        while s:
            idx = bisect.bisect_right(s, c)
            if idx > 0:
                del s[idx - 1]
            else:
                res += 1
                s.pop()
            u = []
            for item in s:
                k = item << 1
                if k > c:
                    k = c + 1
                bisect.insort(u, k)
            s = u
        sys.stdout.write(str(res) + '\n')
run()