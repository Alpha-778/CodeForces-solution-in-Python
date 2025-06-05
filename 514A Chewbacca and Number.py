x = input().strip()
result = ""
for i, ch in enumerate(x):
    digit = int(ch)
    inverted = 9 - digit
    if i == 0 and digit == 9:
        result += ch
    else:
        result += str(min(digit, inverted))
print(result)