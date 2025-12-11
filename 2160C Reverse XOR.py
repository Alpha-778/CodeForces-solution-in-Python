t = int(input())
rec=list(int(input()) for i in range(t))
for _ in range(t):
    n = rec[_]
    possible = False
    for L in range(1, 61):
        if n >= (1 << L):
            continue
        ok = True
        for i in range(L):
            bi = (n >> i) & 1
            bj = (n >> (L - 1 - i)) & 1
            if bi != bj:
                ok = False
                break
        if not ok:
            continue
        if L % 2 == 1:
            mid = L // 2
            if ((n >> mid) & 1) == 1:
                ok = False
        if ok:
            possible = True
            break
    print("YES" if possible else "NO")