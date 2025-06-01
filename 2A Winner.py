from collections import defaultdict
while True:
    try:
        n = int(input())
        s = []
        a = []
        mp = defaultdict(int)
        for _ in range(n):
            name, val = input().split()
            val = int(val)
            s.append(name)
            a.append(val)
            mp[name] += val
        mx = max(mp.values())
        mp2 = defaultdict(int)
        for i in range(n):
            mp2[s[i]] += a[i]
            if mp2[s[i]] >= mx and mp[s[i]] == mx:
                print(s[i])
                break
    except EOFError:
        break