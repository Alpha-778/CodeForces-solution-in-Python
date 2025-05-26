t=int(input())
rec=[int(input()) for i in range(t)]
for i in range(t):
    n=rec[i]
    m=n//2020
    o=n%2020
    if o>m:
        print("NO")
    else:
        print("YES")
