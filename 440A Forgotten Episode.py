n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(n):
    try:
        if a[i]!=i+1:
            print(i+1)
            break
        else:
            continue
    except:
        print(n)