t=int(input())
rec=[int(input()) for i in range(0,t)]
for i in range(t):
    n=rec[i]
    if n%2==1:
        print(n//2)
    else:
        print(n//2-1)