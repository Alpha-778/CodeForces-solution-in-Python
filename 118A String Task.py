l=input()
for i in l:
    if i.lower() not in "aoyeui":
        print(".",i.lower(),sep="",end="")
print()