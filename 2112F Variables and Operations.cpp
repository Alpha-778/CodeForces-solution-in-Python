#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int n, m, q;
vector<tuple<int, int, ll>> ops;
vector<ll> apply_operations(const vector<ll>& a) {
    vector<vector<pair<int, ll>>> g(n);
    vector<int> indeg(n);
    for (auto &[x, y, z] : ops) {
        g[y].emplace_back(x, z);
        indeg[x]++;
    }
    vector<ll> res = a;
    queue<int> q;
    for (int i = 0; i < n; ++i) if (indeg[i] == 0) q.push(i);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (auto &[v, z] : g[u]) {
            if (res[v] > res[u] + z) {
                res[v] = res[u] + z;
            }
            if (--indeg[v] == 0) q.push(v);
        }
    }
    return res;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    ops.resize(m);
    for (int i = 0; i < m; ++i) {
        int x, y; ll z;
        cin >> x >> y >> z;
        --x, --y;
        ops[i] = {x, y, z};
    }
    cin >> q;
    while (q--) {
        ll k;
        cin >> k;
        vector<ll> a(n);
        for (ll &x : a) cin >> x;
        vector<ll> base = apply_operations(a);
        string ans(n, '0');
        for (int i = 0; i < n; ++i) {
            for (int dec = 1; dec <= min(k, 50LL); ++dec) {
                vector<ll> test = a;
                test[i] -= dec;
                vector<ll> new_res = apply_operations(test);
                if (new_res[i] != base[i]) {
                    ans[i] = '1';
                    break;
                }
            }
        }
        cout << ans << '\n';
    }
    return 0;
}