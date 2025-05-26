n=int(input())
l=input()
a=0
for i in range(0,n-1):
     if l[i]==l[i+1]:
          a+=1
print(a)