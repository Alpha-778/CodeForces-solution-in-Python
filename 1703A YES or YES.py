t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    l=rec[i]
    if l.lower()=="yes":
        print("YES")
    else:
        print("NO")