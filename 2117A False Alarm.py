t = int(input())
rec=[]
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    rec.append([n,x,a])
for _ in range(t):
    n,x,a=rec[_]
    used_button = False
    timer = 0
    success = True
    for i in range(n):
        if a[i] == 0:
            if timer > 0:
                timer -= 1
        else:
            if timer > 0:
                timer -= 1
            elif not used_button:
                used_button = True
                timer = x - 1  
            else:
                success = False
                break
    print("YES" if success else "NO")