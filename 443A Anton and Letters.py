l=input()
rec=[]
for i in l:
    if i in "qwertyuiopasdfghjklzxcvbnm" and not i in rec:
        rec.append(i)
print(len(rec))