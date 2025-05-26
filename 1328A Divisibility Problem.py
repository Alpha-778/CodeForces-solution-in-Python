t=int(input())
rec=[]
for i in range(0,t):
    a,b=map(int,input().split())
    rec.append([a,b])
for i in range(0,t):
    a,b=rec[i]
    if a%b==0:
        print("0")
    else:
        print(b-(a%b))