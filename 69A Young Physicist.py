n=int(input())
x1,y1,z1=0,0,0
rec=[list(map(int,input().split())) for i in range(n)]
for i in range(0,n):
    x,y,z=rec[i]
    x1+=x
    y1+=y
    z1+=z
if x1==0 and y1==0 and z1==0:
    print("YES")
else:
    print("NO")