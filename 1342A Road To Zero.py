t=int(input())
rec=[]
for i in range(0,t):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    rec.append([x,y,a,b])
for i in range(0,t):
    x,y,a,b=rec[i]
    min_xy = min(x, y)
    diff = abs(x - y)
    if b < 2 * a:
        cost = b * min_xy + a * diff
    else:
        cost = (x + y) * a
    print(cost)