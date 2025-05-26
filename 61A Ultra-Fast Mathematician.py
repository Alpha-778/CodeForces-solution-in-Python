l1=input()
l2=input()
for i in range(0,len(l1)):
    if l1[i]=="1" and l2[i]=="1":
        print(0,end="")
    elif l1[i]=="1" or l2[i]=="1":
        print(1,end="")
    else:
        print(0,end="")
print()