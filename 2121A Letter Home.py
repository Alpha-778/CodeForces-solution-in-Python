t=int(input())
rec=[[list(map(int,input().split())),list(map(int,input().split()))] for i in range(t)]
for _ in range(t):
    n,s=rec[_][0]
    x=rec[_][1]
    min_x = x[0]
    max_x = x[-1]
    steps = min(abs(s - min_x), abs(s - max_x)) + (max_x - min_x)
    print(steps)