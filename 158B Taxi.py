n=int(input())
s=list(map(int,input().split()))
b = s.count(4)
b += min(s.count(3), s.count(1))
remaining_3 = s.count(3) - min(s.count(3), s.count(1))
remaining_1 = s.count(1) - min(s.count(3), s.count(1))
b += remaining_3
pairs_of_2 = s.count(2) // 2
b += pairs_of_2
if s.count(2) % 2 == 1:
    b += 1
    remaining_1 -= min(2, remaining_1)
if remaining_1 > 0:
    b += (remaining_1 + 3) // 4
print(b)