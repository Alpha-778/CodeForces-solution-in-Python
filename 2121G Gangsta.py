t = int(input())
rec=[]
for _ in range(t):
    n = int(input())
    s = input()
    rec.append([n,s])
for _ in range(t):
    n,s=rec[_]
    ans = 0
    for i in range(n):
        cnt0 = cnt1 = 0
        for j in range(i, n):
            if s[j] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            ans += max(cnt0, cnt1)
    print(ans)