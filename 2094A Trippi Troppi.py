t=int(input())
rec=[list(map(str,input().split())) for i in range(t)]
for i in range(t):
    a,b,c=rec[i]
    print(a[0],b[0],c[0],sep="")