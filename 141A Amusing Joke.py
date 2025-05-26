guest = input().strip()
host = input().strip()
pile = input().strip()
combined = guest + host
if sorted(combined) == sorted(pile):
    print("YES")
else:
    print("NO")