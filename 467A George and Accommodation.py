n=int(input())
rec=[]
cnt=0
for i in range(0,n):
    rec.append(list(map(int,input().split())))
for i in range(0,n):
    p,q=rec[i]
    if q-p>=2:
        cnt+=1
print(cnt)