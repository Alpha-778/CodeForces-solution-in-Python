a,b=map(int,input().split())
i=0
c=0
while c==0:
    if a>b:
        print(i)
        c=1
    i=i+1
    a=a*3
    b=b*2