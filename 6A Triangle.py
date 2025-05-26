from itertools import combinations
sticks = list(map(int, input().split()))
triangle_possible = False
segment_possible = False
for a, b, c in combinations(sticks, 3):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        triangle_possible = True
        break
    elif sides[0] + sides[1] == sides[2]:
        segment_possible = True
if triangle_possible:
    print("TRIANGLE")
elif segment_possible:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")