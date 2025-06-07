n, b, d = map(int, input().split())
a = list(map(int, input().split()))
waste = 0
empties = 0
for orange in a:
    if orange <= b:
        waste += orange
        if waste > d:
            empties += 1
            waste = 0
print(empties)