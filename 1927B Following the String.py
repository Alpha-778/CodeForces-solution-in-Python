t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = []
    used = {}
    available_chars = [chr(ord('a') + i) for i in range(26)]
    idx = 0 
    for val in a:
        found = False
        for ch in used:
            if used[ch] == val:
                s.append(ch)
                used[ch] += 1
                found = True
                break
        if not found:
            ch = available_chars[idx]
            idx += 1
            s.append(ch)
            used[ch] = 1
    print("".join(s))