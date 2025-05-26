n=int(input())
rec=[]
for i in range(0,n):
    l=input()
    rec.append(l)
for i in range(0,n):
    l=rec[i]
    le=len(l)
    if le>10:
        print(l[0],end="")
        print(le-2,end="")
        print(l[-1])
    else:
        print(l)