def is_between(x, a, b):
    if a < b:
        return a < x < b
    else:
        return x > a or x < b

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if not is_between(b, a, b): 
        a, b = b, a
    if not is_between(d, c, d):
        c, d = d, c
    c_in_ab = is_between(c, a, b)
    d_in_ab = is_between(d, a, b)
    a_in_cd = is_between(a, c, d)
    b_in_cd = is_between(b, c, d)
    if (c_in_ab != d_in_ab):
        print("YES")
    elif (a_in_cd != b_in_cd):
        print("YES")
    else:
        print("NO")