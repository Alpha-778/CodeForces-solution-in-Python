t=int(input())
rec=[]
for i in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    rec.append([n,A])
for i in range(t):
    n,A=rec[i]
    present = set(A)
    mex = 0
    while mex in present:
        mex += 1
    print(mex)