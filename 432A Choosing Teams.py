n,k=map(int,input().split())
y=list(map(int,input().split()))
valids = 0
for i in range(n):
    persons = y[i]
    if persons + k <= 5:
        valids += 1
print(valids // 3)
