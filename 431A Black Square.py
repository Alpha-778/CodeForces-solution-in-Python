a = list(map(int, input().split()))
s = input()
total = 0
for ch in s:
    index = int(ch) - 1 
    total += a[index]   
print(total)