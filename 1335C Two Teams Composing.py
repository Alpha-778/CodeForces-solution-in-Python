from collections import Counter
t=int(input())
rec=[]
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    rec.append([n,a])
for i in range(0,t):
    n,a=rec[i]
    results = []
    freq = Counter(a)
    unique_skills = len(freq)
    max_frequency = max(freq.values())
    if max_frequency == unique_skills:
        results.append(unique_skills - 1)
    else:
        results.append(min(unique_skills, max_frequency))
    print(*results)