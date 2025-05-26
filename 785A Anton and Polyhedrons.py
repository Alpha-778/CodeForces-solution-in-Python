n=int(input())
rec=[input() for i in range(0,n)]
cnt=0
for i in range(0,n):
    l=rec[i]
    if l=="Tetrahedron":
        cnt+=4
    elif l=="Cube":
        cnt+=6
    elif l=="Octahedron":
        cnt+=8
    elif l=="Dodecahedron":
        cnt+=12
    elif l=="Icosahedron":
        cnt+=20
print(cnt)