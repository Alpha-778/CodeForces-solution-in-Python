n=int(input())
rec=[list(map(int,input().split())) for i in range(0,n)]
count = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if rec[i][0] == rec[j][1]:
                count += 1
print(count)