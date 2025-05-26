n=int(input())
l=input()
a,d=0,0
for i in l:
    if i=="A":
        a+=1
    elif i=="D":
        d+=1
if a==d:
    print("Friendship")
elif a>d:
    print("Anton")
elif d>a:
    print("Danik")