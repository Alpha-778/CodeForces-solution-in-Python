n,m,a,b=map(int,input().split())
cost_all_single = n * a
cost_mix = (n // m) * b + (n % m) * a
cost_all_multi = ((n + m - 1) // m) * b
print(min(cost_all_single, cost_mix, cost_all_multi))