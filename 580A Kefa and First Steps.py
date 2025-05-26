n=int(input())
a=list(map(int,input().split()))
cnt=1
m=1
if n==1:
    print("1")
else:
    for i in range(0,n-1):
        if a[i]<=a[i+1]:
            cnt+=1
            m=max(m,cnt)
        else:
            cnt=1
    print(m)