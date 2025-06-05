t=int(input())
rec=[input() for i in range(t)]
for i in range(t):
    l=rec[i].lower()
    r="codeforces"
    cnt=0
    for j in range(len(r)):
        if l[j] != r[j]:
            cnt+=1
        else:
            continue
    print(cnt)