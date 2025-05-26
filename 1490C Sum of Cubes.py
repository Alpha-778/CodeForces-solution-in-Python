t=int(input())
rec=[int(input()) for i in range(t)]
for i in range(0,t):
    x=rec[i]
    a = 1
    flag=0
    while a ** 3 < x:
        b_cubed = x - a ** 3
        b = round(b_cubed ** (1/3))
        if b > 0 and b ** 3 == b_cubed:
            flag=1
        a += 1
    if flag==1:
        print("YES")
    else:
        print("NO")