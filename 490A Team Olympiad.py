n=int(input())
t=list(map(int,input().split()))
type1 = []
type2 = []
type3 = []
for i in range(n):
    if t[i] == 1:
        type1.append(i + 1)
    elif t[i] == 2:
        type2.append(i + 1)
    elif t[i] == 3:
        type3.append(i + 1)
w = min(len(type1), len(type2), len(type3))
print(w)
for i in range(w):
    print(type1[i], type2[i], type3[i])