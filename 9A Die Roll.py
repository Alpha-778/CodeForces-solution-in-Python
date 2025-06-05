from math import gcd
Y, W = map(int, input().split())
max_roll = max(Y, W)
favorable = 6 - max_roll + 1
total = 6
g = gcd(favorable, total)
print(f"{favorable // g}/{total // g}")