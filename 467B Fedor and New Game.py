n,m,k=map(int,input().split())
rec=[int(input()) for i in range(0,m+1)]
for i in range(0,m+1):
    x=rec[i]
    fa = rec[-1]
    fc = 0
    for i in range(m):
        diff = bin(rec[i] ^ fa).count('1')
        if diff <= k:
            fc += 1
print(fc)