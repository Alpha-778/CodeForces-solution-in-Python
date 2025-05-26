t=int(input())
rec=[int(input()) for i in range(0,t)]
for i in range(0,t):
    a=rec[i]
    n = 360 / (180 - a)
    if n == int(n) :
        print("YES")
    else :
        print("NO")