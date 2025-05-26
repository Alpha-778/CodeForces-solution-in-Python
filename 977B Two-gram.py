n = int(input())
s = input()
freq = {}
for i in range(n - 1):
    tg = s[i:i+2]
    freq[tg] = freq.get(tg, 0) + 1
most_frequent = max(freq, key=freq.get)
print(most_frequent)