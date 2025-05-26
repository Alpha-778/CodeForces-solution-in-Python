t=int(input())
rec=[]
for i in range(0,t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    rec.append([n,x,a])
for i in range(0,t):
    n,x,a=rec[i]
    even = 0
    odd = 0
    for j in a:
        if j%2==0:
            even+=1
        else:
            odd+=1
    m = min(even, x - 1)
    d = x - m
    if d % 2 == 0:
        d += 1     
    if odd >= d and d <= x:
        print("Yes")
    else:
        print("No")
