#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    vector<int> pow2(1, 1);
    vector<tuple<int, vector<int>, vector<int>>> rec(t);
    for (int i = 0; i < t; ++i) {
        int n; cin >> n;
        vector<int> p(n), q(n);
        for (int j = 0; j < n; ++j) cin >> p[j];
        for (int j = 0; j < n; ++j) cin >> q[j];
        rec[i] = {n, p, q};
    }
    for (int tt = 0; tt < t; ++tt) {
        int n; vector<int> p, q;
        tie(n, p, q) = rec[tt];
        if ((int)pow2.size() <= n) {
            int old_len = (int)pow2.size();
            for (int i = old_len; i <= n; ++i) {
                pow2.push_back((1LL * pow2[i - 1] * 2) % MOD);
            }
        }
        vector<int> posP(n), posQ(n);
        for (int i = 0; i < n; ++i) {
            posP[p[i]] = i;
        }
        for (int i = 0; i < n; ++i) {
            posQ[q[i]] = i;
        }
        vector<int> Pmax(n), Qmax(n);
        Pmax[0] = p[0];
        Qmax[0] = q[0];
        for (int i = 1; i < n; ++i) {
            Pmax[i] = max(Pmax[i - 1], p[i]);
            Qmax[i] = max(Qmax[i - 1], q[i]);
        }
        vector<int> r(n);
        for (int i = 0; i < n; ++i) {
            int e = max(Pmax[i], Qmax[i]);
            int s;
            if (Pmax[i] > Qmax[i]) {
                int j = posP[e];
                int k = i - j;
                s = q[k];
            } else if (Qmax[i] > Pmax[i]) {
                int k = posQ[e];
                int j = i - k;
                s = p[j];
            } else {
                int j1 = posP[e];
                int k1 = i - j1;
                int s1 = (k1 >= 0 && k1 < n) ? q[k1] : -1;
                int k2 = posQ[e];
                int j2 = i - k2;
                int s2 = (j2 >= 0 && j2 < n) ? p[j2] : -1;
                s = max(s1, s2);
            }
            int val = (pow2[e] + pow2[s]) % MOD;
            r[i] = val;
        }
        for (int i = 0; i < n; ++i) {
            cout << r[i] << (i == n - 1 ? '\n' : ' ');
        }
    }
    return 0;
}
