t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    a,b,c,d,e,f=int(rec[i][0]),int(rec[i][1]),int(rec[i][2]),int(rec[i][3]),int(rec[i][4]),int(rec[i][5])
    if a+b+c==d+e+f:
        print("YES")
    else:
        print("NO")