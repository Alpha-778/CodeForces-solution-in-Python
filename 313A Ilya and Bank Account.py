n = int(input())
option1=0
option2=0
if n >= 0:
    print(n)
else:
    s = str(n)
    option1 = int(s[:-1])
    option2 = int(s[:-2] + s[-1])
    print(max(n, option1, option2))