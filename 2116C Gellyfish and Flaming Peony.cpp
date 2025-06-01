#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <numeric> 
#include <cstring> 
using namespace std;
const int MAX = 5001;
const int INF = 1e9;
int main() {
    int t;
    cin >> t;
    vector<pair<int, vector<int>>> rec(t);
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int j = 0; j < n; ++j) {
            cin >> a[j];
        }
        rec[i] = {n, a};
    }
    for (int i = 0; i < t; ++i) {
        int n = rec[i].first;
        vector<int> a = rec[i].second;
        int g = 0;
        for (int val : a) {
            g = gcd(g, val);
        }
        int countG = count(a.begin(), a.end(), g);
        if (countG > 0) {
            cout << (n - countG) << endl;
            continue;
        }
        bool seen[MAX] = {false};
        vector<int> uniq;
        for (int val : a) {
            if (!seen[val]) {
                seen[val] = true;
                uniq.push_back(val);
            }
        }
        vector<int> dist(MAX, INF);
        deque<int> q;
        for (int val : uniq) {
            dist[val] = 0;
            q.push_back(val);
        }
        while (!q.empty()) {
            int v = q.front(); q.pop_front();
            for (int x : uniq) {
                int newVal = gcd(v, x);
                if (dist[newVal] > dist[v] + 1) {
                    dist[newVal] = dist[v] + 1;
                    q.push_back(newVal);
                }
            }
        }
        int minStepsToG = dist[g];
        cout << (minStepsToG + (n - 1)) << endl;
    }
    return 0;
}