k,n,w=map(int,input().split())
a=w*(w+1)//2
a=a*k
if a>n:
    print(a-n)
else:
    print("0")