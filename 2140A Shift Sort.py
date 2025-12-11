t=int(input())
rec=[]
for i in range(t):
    n=int(input())
    s=input()
    rec.append([n,s])
for i in range(t):
    n,s=rec[i]
    zeros = s.count('0')
    result = 0
    for i in range(zeros):
        if s[i] == '1':
            result += 1
    print(result)