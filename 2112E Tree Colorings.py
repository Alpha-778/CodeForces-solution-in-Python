import sys
I = sys.stdin.read
F = int(1e9)
d = list(map(int, I().split()))
T, Q = d[0], d[1:]
M = max(Q)
K = M + 3
D, P, S = [[] for _ in range(M+1)], [F]*(M+1), [F]*K
P[1] = 0
for x in range(3, M+1):
    for y in range(x, M+1, x): D[y].append(x)
for i in range(3, K):
    S[i] = 1 + P[i-2]
    if i > M: break
    P[i] = S[i]
    for j in D[i]:
        q = i // j
        if P[q] < F:
            P[i] = min(P[i], P[q] + S[j])
for m in Q:
    print(1 if m==1 else -1 if P[m]>=F else 1+P[m])