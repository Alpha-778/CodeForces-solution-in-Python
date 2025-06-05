t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    b=rec[i]
    a = b[0]
    for i in range(1, len(b), 2):
        a += b[i]
    print(a)