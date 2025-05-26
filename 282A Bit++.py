n=int(input())
x=0
rec=[]
for i in range(0,n):
    l=input()
    rec.append(l)
for i in range(0,n):
    l=rec[i]
    if l[0]=="+" or l[-1]=="+":
        x+=1
    else:
        x-=1
print(x)