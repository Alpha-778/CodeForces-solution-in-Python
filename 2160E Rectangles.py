t = int(input())
rec=[]
for i in range(t):
    n,m=map(int,input().split())
    G=list(input() for j in range(n))
    rec.append([n,m,G])
INF = 1 << 60
out_lines = []
for _ in range(t):
    n,m,G=rec[_]
    ans = [[INF] * m for _ in range(n)]
    if m <= n:
        for l in range(m):
            for r in range(l + 1, m):
                width = r - l + 1
                S = []
                for i in range(n):
                    if G[i][l] == '1' and G[i][r] == '1':
                        S.append(i)
                if len(S) < 2:
                    continue
                for k in range(len(S) - 1):
                    u = S[k]
                    v = S[k + 1]
                    height = v - u + 1
                    area = width * height
                    for i in range(u, v + 1):
                        for j in range(l, r + 1):
                            if area < ans[i][j]:
                                ans[i][j] = area
    else:
        for u in range(n):
            for d in range(u + 1, n):
                height = d - u + 1
                S = []
                for j in range(m):
                    if G[u][j] == '1' and G[d][j] == '1':
                        S.append(j)
                if len(S) < 2:
                    continue
                for k in range(len(S) - 1):
                    l = S[k]
                    r = S[k + 1]
                    width = r - l + 1
                    area = width * height
                    for j in range(l, r + 1):
                        for i in range(u, d + 1):
                            if area < ans[i][j]:
                                ans[i][j] = area

    for i in range(n):
        row = []
        for j in range(m):
            if ans[i][j] == INF:
                row.append("0")
            else:
                row.append(str(ans[i][j]))
        out_lines.append(" ".join(row))
print("\n".join(out_lines))