t=int(input())
rec=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    rec.append([n,a])
for _ in range(t):
    n,a=rec[_];a.sort();m,s=a[-1],a[-2];z=0
    for k in range(2,n):
        x=max(2*a[k],s if k==n-1 else m)-a[k];l,j=0,k-1
        while l<j:
            if a[l]+a[j]>x:z+=j-l;j-=1
            else:l+=1
    print(z)