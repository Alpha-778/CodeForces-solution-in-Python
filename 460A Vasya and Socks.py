n,m=map(int,input().split())
days = 0
socks = n
while socks > 0:
    days += 1
    socks -= 1
    if days % m == 0:
        socks += 1
print(days)