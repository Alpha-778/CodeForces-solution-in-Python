k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
if k == 1 or l == 1 or m == 1 or n == 1:
    print(d)
else:
    damaged = 0
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            damaged += 1
    print(damaged)