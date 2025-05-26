n=int(input())
l=input()
rec=[]
if n<26:
    print("NO")
else:
    for i in l:
        if i.lower() not in rec:
            rec.append(i.lower())
        else:
            continue
    if len(rec)==26:
        print("YES")
    else:
        print("NO")