t=int(input())
rec=[[int(input()),input()] for i in range(t)]
for _ in range(t):
    n,s=rec[_]
    found = False
    for i in range(1, n - 1):
        a = s[:i]
        b = s[i]
        c = s[i+1:]
        if b in (a + c):
            found = True
            break
    print("Yes" if found else "No")