t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    a=rec[i]
    if a in "codeforces":
        print("YES")
    else:
        print("NO")