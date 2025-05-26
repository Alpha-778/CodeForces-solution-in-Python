l=input()
a,b=0,0
for i in l:
    if i==i.upper():
        a+=1
    else:
        b+=1
if a>b:
    print(l.upper())
else:
    print(l.lower())