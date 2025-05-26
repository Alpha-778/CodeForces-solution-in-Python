n = int(input())

def is_lucky(num):
    for digit in str(num):
        if digit != '4' and digit != '7':
            return False
    return True

found = False
for i in range(1, n + 1):
    if is_lucky(i) and n % i == 0:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
