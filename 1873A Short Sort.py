t = int(input())
rec=[input() for i in range(t)]
for _ in range(t):
    s = rec[_]
    if s in ["abc", "acb", "bac", "cba"]:
        print("YES")
    else:
        print("NO")