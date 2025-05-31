t=int(input())
rec=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    rec.append([n,a])
for i in range(t):
    n,a=rec[i]
    a.sort()
    possible = True
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            possible = False
            break
    print("YES" if possible else "NO")