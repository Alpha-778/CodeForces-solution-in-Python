m, s = map(int, input().split())
a = ""
b = ""
if s == 0:
    print("0 0" if m == 1 else "-1 -1")
    exit()
s_copy = s
for _ in range(m):
    t = min(s_copy, 9)
    b += str(t)
    s_copy -= t
if s_copy > 0:
    print("-1 -1")
    exit()
a = b[::-1]
a = list(a)
i = 0
while a[i] == '0':
    i += 1
a[i] = str(int(a[i]) - 1)
a[0] = str(int(a[0]) + 1)
a = ''.join(a)
print(a, b)