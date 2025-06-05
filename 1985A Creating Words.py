t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    l=rec[i]
    j=l[4]+l[1:4]+l[0]+l[5:]
    print(j)