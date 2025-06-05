t=int(input())
rec=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    rec.append([n,a])
for i in range(t):
    n,a=rec[i]
    l=sum(a)
    print("NO" if l%2==1 else "YES")