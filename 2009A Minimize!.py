t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b=rec[i]
    print(b-a)