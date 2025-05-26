l=input()
l1="hello"
j=0
flag=0
for i in range(len(l)):
    if l[i]==l1[j]:
        j+=1
        if j==5:
            flag=1
            break
    else:
        continue
if flag==1:
    print("YES")
else:
    print("NO")