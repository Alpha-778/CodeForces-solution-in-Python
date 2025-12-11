import sys
data = sys.stdin.read().strip().split()
index = 0
try:
    test_cases = int(data[index])
except:
    sys.exit(0)
index += 1
for _ in range(test_cases):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    s = []
    for i in range(n):
        s.append(int(data[index]))
        index += 1
    t = []
    for i in range(n):
        t.append(int(data[index]))
        index += 1
    if k == 0:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
        continue
    count_map = {}
    for val in s:
        remainder = val % k
        if remainder < 0:
            remainder += k
        alt = min(remainder, k - remainder)
        if alt not in count_map:
            count_map[alt] = 0
        count_map[alt] += 1
    for val in t:
        remainder = val % k
        if remainder < 0:
            remainder += k
        alt = min(remainder, k - remainder)
        if alt not in count_map:
            count_map[alt] = 0
        count_map[alt] -= 1
    consistent = True
    for key in count_map:
        if count_map[key] != 0:
            consistent = False
            break
    if consistent:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")