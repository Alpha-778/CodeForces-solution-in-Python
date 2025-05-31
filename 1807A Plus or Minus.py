t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b,c=rec[i]
    if a+b==c:
        print("+")
    elif a-b==c or b-a==c:
        print("-")