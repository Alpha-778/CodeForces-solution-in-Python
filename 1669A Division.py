t=int(input())
rec=[int(input()) for i in range(t)]
for i in range(t):
    l=rec[i]
    if l<=1399:
        print("Division 4")
    elif l<=1599:
        print("Division 3")
    elif l<=1899:
        print("Division 2")
    else:
        print("Division 1")