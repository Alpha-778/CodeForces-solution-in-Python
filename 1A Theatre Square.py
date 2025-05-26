n,m,a=map(int,input().split())
l=0
if n%a==0:
    l+=n//a
else:
    l+=n//a+1
if m%a==0:
    l*=m//a
else:
    l*=m//a+1
print(l)