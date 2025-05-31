t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    a,b=rec[i]
    diff = abs(a - b)
    moves = (diff + 9) // 10
    print(moves)