t = int(input())
rec=[input() for i in range(t)]
for i in range(t):
    s=rec[i]
    flag=0
    balance = 0
    for i in range(len(s) - 1):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            flag=1
    if flag==1:
        print("YES")
    else:
        print("NO")