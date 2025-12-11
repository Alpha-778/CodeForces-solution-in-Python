t = int(input())
rec=[]
for _ in range(t):
    s = input()
    t2 = input()
    rec.append([s,t2])
for _ in range(t):
    s, t2 = rec[_]
    a = [0]*26
    b = [0]*26
    for c in s: a[ord(c)-97] += 1
    for c in t2: b[ord(c)-97] += 1
    ok = True
    e = ""
    for i in range(26):
        if b[i] < a[i]:
            ok = False
            break
        d = b[i] - a[i]
        if d > 0: e += chr(97+i)*d
    if not ok:
        print("Impossible")
        continue
    r = ""
    i = 0
    j = 0
    n = len(s)
    m = len(e)
    while i < n and j < m:
        if e[j] < s[i]:
            r += e[j]
            j += 1
        else:
            r += s[i]
            i += 1
    while j < m:
        r += e[j]
        j += 1
    while i < n:
        r += s[i]
        i += 1
    print(r)