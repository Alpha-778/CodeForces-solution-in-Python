from collections import defaultdict

def cnt(a, s, mx):
        r = 0
        p = 0
        f = defaultdict(int)
        f[0] = 1
        for v in a:
            if v > mx:
                p = 0
                f = defaultdict(int)
                f[0] = 1
                continue
            p += v
            r += f[p - s]
            f[p] += 1
        return r

t=int(input())
rec=[]
for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))
    rec.append([n,s,x,a])
for _ in range(t):
    n,s,x,a=rec[_]    
    print(cnt(a, s, x) - cnt(a, s, x - 1))