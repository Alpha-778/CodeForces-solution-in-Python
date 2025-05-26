l=input()
rec=[]
for i in l:
    if i not in rec:
        rec.append(i)
if len(rec)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")    