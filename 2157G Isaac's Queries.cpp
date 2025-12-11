#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
#include <utility>
#include <cstdlib>

using namespace std;

int n;
map< pair<int, int>, int > cache_val;
vector<int> value_mask;

int query(int a, int b) {
    if (a > b) {
        int t = a;
        a = b;
        b = t;
    }

    pair<int, int> key = make_pair(a, b);

    if (cache_val.count(key)) {
        return cache_val[key];
    }

    cout << "? " << a + 1 << " " << b << endl;
    int res;
    cin >> res;

    if (res == -2) {
        exit(0);
    }

    cache_val[key] = res;
    return res;
}

struct Dsu {
    vector<int> parent;
    vector<int> parity;

    Dsu(int size) {
        parent.resize(size);
        parity.assign(size, 0);
        iota(parent.begin(), parent.end(), 0);
    }

    pair<int, int> root(int x) {
        if (parent[x] == x) {
            return make_pair(x, 0);
        }

        pair<int, int> pr = root(parent[x]);
        parent[x] = pr.first;
        parity[x] ^= pr.second;

        return make_pair(parent[x], parity[x]);
    }

    bool join(int a, int b, int d) {
        pair<int, int> ra = root(a);
        pair<int, int> rb = root(b);

        if (ra.first != rb.first) {
            parent[ra.first] = rb.first;
            parity[ra.first] = d ^ ra.second ^ rb.second;
            return true;
        }

        return false;
    }
};

int highest_bit(int x) {
    int p = -1;
    while (x > 0) {
        p++;
        x >>= 1;
    }
    return p;
}

void solve_group(vector<int> &group, int bit) {
    if ((int)group.size() <= 1 || bit < 0) {
        return;
    }

    Dsu dsu(n + 1);

    vector<bool> in_group(n + 1, false);
    for (int i = 0; i < (int)group.size(); i++) {
        in_group[group[i]] = true;
    }

    for (map< pair<int, int>, int >::iterator it = cache_val.begin(); it != cache_val.end(); it++) {
        int u = it->first.first;
        int v = it->first.second;
        int w = it->second;

        if (!in_group[u] || !in_group[v]) {
            continue;
        }

        if (w > bit) {
            continue;
        }

        int diff = 0;
        if (w == bit) {
            diff = 1;
        }

        dsu.join(u, v, diff);
    }

    while (true) {
        map<int, vector<int> > comp;
        for (int i = 0; i < (int)group.size(); i++) {
            int x = group[i];
            int root_x = dsu.root(x).first;
            comp[root_x].push_back(x);
        }

        if ((int)comp.size() <= 1) {
            break;
        }

        int best_u = -1;
        int best_v = -1;
        double best_cost = 1e18;

        vector<int> roots;
        for (map<int, vector<int> >::iterator it = comp.begin(); it != comp.end(); it++) {
            roots.push_back(it->first);
        }

        for (int i = 0; i < (int)roots.size(); i++) {
            for (int j = i + 1; j < (int)roots.size(); j++) {
                int r1 = roots[i];
                int r2 = roots[j];

                vector<int> &a = comp[r1];
                vector<int> &b = comp[r2];

                for (int x = 0; x < (int)a.size(); x++) {
                    for (int y = 0; y < (int)b.size(); y++) {
                        int uu = a[x];
                        int vv = b[y];
                        int dist = uu - vv;
                        if (dist < 0) {
                            dist = -dist;
                        }
                        if (dist == 0) {
                            continue;
                        }
                        double cost = 1.0 / (double)dist;
                        if (cost < best_cost) {
                            best_cost = cost;
                            best_u = uu;
                            best_v = vv;
                        }
                    }
                }
            }
        }
        if (best_u == -1) {
            break;}
        int res = query(best_u, best_v);
        int diff = 0;
        if (res == bit) {
            diff = 1;}
        dsu.join(best_u, best_v, diff);}
    int bias = 0;
    bool has_zero = false;
    for (int i = 0; i < (int)group.size(); i++) {
        if (group[i] == 0) {
            has_zero = true;}}
    if (has_zero) {
        bias = dsu.root(0).second;}
    vector<int> group_zero;
    vector<int> group_one;
    for (int i = 0; i < (int)group.size(); i++) {
        int u = group[i];
        int par = dsu.root(u).second ^ bias;
        if (par == 0) {
            group_zero.push_back(u);
        } else {
            value_mask[u] |= (1 << bit);
            group_one.push_back(u);}}
    solve_group(group_zero, bit - 1);
    solve_group(group_one, bit - 1);}
void solve() {
    cin >> n;
    if (n == -2) {
        exit(0);}
    cache_val.clear();
    value_mask.assign(n + 1, 0);
    vector<int> group(n + 1);
    for (int i = 0; i <= n; i++) {
        group[i] = i;}
    solve_group(group, 29);
    cout << "!" << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j++) {
            int v = value_mask[i - 1] ^ value_mask[j];
            if (v == 0) {
                cout << "-1";
            } else {
                int hb = highest_bit(v);
                cout << hb;}
            if (j < n) {
                cout << " ";
            } else {
                cout << " ";}}
        cout << endl;}}
int main() {
    int t;
    if (!(cin >> t)) {
        return 0;}
    while (t--) {
        solve();}
    return 0;}