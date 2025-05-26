t=int(input())
rec=[input() for i in range(t)]
freq={}
for i in range(t):
    a=rec[i]
    if a not in freq:
        freq[a]=1
        print("OK")
    else:
        print(a,end="")
        print(freq[a])
        freq[a]+=1
