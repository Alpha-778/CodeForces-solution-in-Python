n=int(input())
# 8 4 2 6 8
if n==0:
    print("1")
else:
    if n%4==0:
        print("6")
    elif n%4==1:
        print("8")
    elif n%4==2:
        print("4")
    elif n%4==3:
        print("2")