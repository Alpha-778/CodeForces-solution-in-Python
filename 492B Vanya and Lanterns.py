n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
maxi = float('-inf')    
for i in range(1, n):
    maxi = max(maxi, a[i] - a[i - 1])
ld = a[0]
rd = l - a[n - 1]
if a[0] != 0 and a[n - 1] != l:
    print(f"{max(maxi / 2.0, max(ld, rd)):.10f}")
elif a[0] != 0:
    print(f"{max(maxi / 2.0, ld):.10f}")
elif a[n - 1] != l:
    print(f"{max(maxi / 2.0, rd):.10f}")
else:
    print(f"{maxi / 2.0:.10f}")
