t = int(input())
rec=[]
for i in range(t):
    n=int(input())
    s=input()
    rec.append([n,s])
for j in range(t):
    n,s=rec[j]
    i = 0
    deletions = 0
    while i <= n - 3:
        if s[i:i+3] == 'map' or s[i:i+3] == 'pie':
            deletions += 1
            i += 3
        else:
            i += 1
    print(deletions)