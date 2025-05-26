n=int(input())
l=list(map(int,input().split()))
count25 = 0
flag=1
count50 = 0
for bill in l:
    if bill == 25:
        count25 += 1
    elif bill == 50:
        if count25 == 0:
            flag=0
        count25 -= 1
        count50 += 1
    elif bill == 100:
        if count50 >= 1 and count25 >= 1:
            count50 -= 1
            count25 -= 1
        elif count25 >= 3:
            count25 -= 3
        else:
            flag=0
if flag==1:
    print("YES")
else:
    print("NO")