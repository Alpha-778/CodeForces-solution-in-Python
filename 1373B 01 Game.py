t = int(input())
for _ in range(t):
    s = input()
    count0 = s.count('0')
    count1 = s.count('1')
    moves = min(count0, count1)
    if moves % 2 == 1:
        print("DA")
    else:
        print("NET")