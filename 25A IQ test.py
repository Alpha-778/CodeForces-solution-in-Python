n=int(input())
l=list(map(int,input().split()))
odd,even=0,0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
if odd==1:
    for i in range(0,n):
        if l[i]%2==1:
            print(i+1)
            break
else:
    for i in range(0,n):
        if l[i]%2==0:
            print(i+1)
            break