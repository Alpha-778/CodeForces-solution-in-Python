#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; 
    if(!(cin >> T)) return 0;
    while(T--){
        int n, m;
        cin >> n >> m;
        vector<vector<int>> g(n+1);
        for(int i = 0, u, v; i < m; i++){
            cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);}
        vector<int> deg(n+1), off(n+2), ver, lbl;
        int tot = 0;
        for(int i = 1; i <= n; i++){
            deg[i] = g[i].size();
            off[i] = tot;
            tot += deg[i];}
        ver.resize(tot);
        lbl.resize(tot);
        for(int i = 1; i <= n; i++)
            for(int j = 0; j < deg[i]; j++){
                int id = off[i] + j;
                ver[id] = i;
                lbl[id] = j;}
        vector<int> dist(tot, INF), wait(tot, INF);
        deque<int> dq;
        int s = off[1];
        dist[s] = wait[s] = 0;
        dq.push_back(s);
        int bestD = INF, bestW = INF;
        while(!dq.empty()){
            int id = dq.front(); dq.pop_front();
            int d = dist[id], w = wait[id];
            int u = ver[id], r = lbl[id];
            if(d > bestD) break;
            if(u == n){
                if(d < bestD || (d == bestD && w < bestW))
                    bestD = d, bestW = w;
                continue;}
            int d1 = off[u] + (r + 1) % deg[u];
            if(dist[d1] > d + 1 || (dist[d1] == d + 1 && wait[d1] > w + 1)){
                dist[d1] = d + 1;
                wait[d1] = w + 1;
                dq.push_back(d1);}
            int v = g[u][r];
            int nr = (d + 1) % deg[v];
            int d2 = off[v] + nr;
            if(dist[d2] > d + 1 || (dist[d2] == d + 1 && wait[d2] > w)){
                dist[d2] = d + 1;
                wait[d2] = w;
                dq.push_back(d2);}}
        cout << bestD << " " << bestW << "\n";}
    return 0;}