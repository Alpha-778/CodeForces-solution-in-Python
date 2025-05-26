n=int(input())
a=0
rec=[]
for i in range(0,n):
    l=list(map(int,input().split()))
    rec.append(l)
for i in range(0,n):
    l=rec[i]
    t=sum(l)
    if t>=2:
        a+=1
    else:
        continue
print(a)