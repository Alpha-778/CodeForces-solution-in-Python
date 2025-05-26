n,m=map(int,input().split())
for i in range(0,n):
    if i%4==0:
        for j in range(m):
            print("#",end="")
        print()
    if i%4==1:
        for j in range(m-1):
            print(".",end="")
        print("#")
    if i%4==2:
        for j in range(m):
            print("#",end="")
        print()
    if i%4==3:
        print("#",end="")
        for j in range(m-1):
            print(".",end="")
        print()