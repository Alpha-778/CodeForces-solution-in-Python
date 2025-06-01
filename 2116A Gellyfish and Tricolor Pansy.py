t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a, b, c, d = rec[i]
    if b <= a and b <= c:
        print("Gellyfish")
    elif a < d:
        print("Flower")
    elif d<=c:
        print("Gellyfish")
    else:
        print("Flower")