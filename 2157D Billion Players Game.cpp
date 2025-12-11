#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        long long l, r;
        cin >> n >> l >> r;
        vector<long long> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];}
        long long W = r - l;
        long long current_sum = 0;
        long long current_diff = 0;
        vector<long long> pos_undo;
        vector<long long> neg_undo;
        for (int i = 0; i < n; i++) {
            long long val = a[i];
            if (val < l) {
                current_sum += (l + r - 2 * val);
                current_diff += W;
            } else if (val > r) {
                current_sum += (2 * val - l - r);
                current_diff -= W;
            } else {
                long long v = 2 * val - (l + r);
                long long abs_v = llabs(v);
                current_sum += abs_v;
                if (v >= 0) {
                    current_diff -= W;
                    neg_undo.push_back(abs_v);
                    neg_undo.push_back(abs_v);
                } else {
                    current_diff += W;
                    pos_undo.push_back(abs_v);
                    pos_undo.push_back(abs_v);}}}
        if (W == 0) {
            cout << current_sum / 2 << endl;
            continue;}
        if (current_diff > 0) {
            sort(pos_undo.begin(), pos_undo.end());
            for (size_t i = 0; i < pos_undo.size(); i++) {
                long long cost = pos_undo[i];
                if (current_diff > 0 && cost < W) {
                    current_sum -= cost;
                    current_diff -= W;
                } else {
                    break;}}
        } else if (current_diff < 0) {
            sort(neg_undo.begin(), neg_undo.end());
            for (size_t i = 0; i < neg_undo.size(); i++) {
                long long cost = neg_undo[i];
                if (current_diff < 0 && cost < W) {
                    current_sum -= cost;
                    current_diff += W;
                } else {
                    break;}}}
        long long result = (current_sum - llabs(current_diff)) / 2;
        cout << result << endl;}
    return 0;}