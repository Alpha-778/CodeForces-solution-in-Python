def sereja_and_suffixes(n, m, a, queries):
    suffix_distinct = [0] * (n + 1)
    seen = set()
    for i in range(n, 0, -1):
        seen.add(a[i - 1])
        suffix_distinct[i] = len(seen)    
    return [suffix_distinct[li] for li in queries]

n,m=map(int,input().split())
a = list(map(int,input().split()))
queries = [int(input()) for i in range(m)]
result = sereja_and_suffixes(n, m, a, queries)
for r in result:
    print(r)