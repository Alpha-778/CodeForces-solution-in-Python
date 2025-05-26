l1=input().lower()
l2=input().lower()
if l1==l2:
    print("0")
else:
    for i in range(len(l1)):
        if l1[i]>l2[i]:
            a="1"
            exit
        elif l1[i]<l2[i]:
            a="-1"            
        else:
            continue
        if a:
            print(a)
            break