n=int(input())
rec=[]
current_passengers = 0
max_passengers = 0
for i in range(n):
    rec.append(list(map(int,input().split())))
for i in range(n):
    a,b=rec[i]
    current_passengers -= a
    current_passengers += b
    max_passengers = max(max_passengers, current_passengers)
print(max_passengers)