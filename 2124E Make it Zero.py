def f(): return list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    a = f(); s = sum(a)
    if s % 2 or max(a) > s // 2:
        print(-1); continue
    m = s // 2; seg = [(i, x) for i, x in enumerate(a) if x]
    A, acc, i = [], 0, 0
    while i < len(seg) and acc < m:
        p, c = seg[i]
        if acc + c <= m: A.append((p, c)); acc += c; i += 1
        else: t = m - acc; A.append((p, t)); seg[i] = (p, c - t); acc = m
    B, accB = [], 0
    if acc == m and i < len(seg):
        p, c = seg[i]; t = min(c, m); B.append((p, t)); accB += t
        if c > t: seg[i] = (p, c - t); i += 1
        else: i += 1
    while i < len(seg) and accB < m:
        p, c = seg[i]; t = min(c, m - accB); B.append((p, t)); accB += t; i += 1
    sh = max(a) % m; rem, j, cum = sh, 0, 0
    if rem == 0: br = B[0][1]
    else:
        while j < len(B):
            if cum + B[j][1] > rem:
                br = B[j][1] - (rem - cum); break
            cum += B[j][1]; j += 1
    R, ai, ar = [], 0, A[0][1]
    while ai < len(A):
        bi = B[j][0]; ai_ = A[ai][0]
        t = min(ar, br); R.append((ai_, bi, t))
        ar -= t; br -= t
        if ar == 0:
            ai += 1
            if ai < len(A): ar = A[ai][1]
        if br == 0:
            j = (j + 1) % len(B)
            br = B[j][1]
    IV = [(min(i, j), max(i, j)-1, w) for i, j, w in R]
    ord = sorted(range(len(IV)), key=lambda x: IV[x][1])
    out, last, mapo = [], -1, [-1]*len(IV)
    for ix in ord:
        if last < IV[ix][0]:
            last = IV[ix][1]; out.append(last)
        mapo[ix] = len(out) - 1
    print(len(out))
    for op in range(len(out)):
        b = [0]*n
        for i, (x, y, w) in enumerate(R):
            if mapo[i] == op: b[x] += w; b[y] += w
        print(*b)