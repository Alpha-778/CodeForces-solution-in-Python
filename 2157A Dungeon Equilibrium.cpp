#include <iostream>
#include <vector>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> cnt(n + 1, 0);
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            if (a >= 0 && a <= n) {
                cnt[a] = cnt[a] + 1;}}
        int kept = 0;
        int x = 1;
        while (x <= n) {
            if (cnt[x] >= x) {
                kept = kept + x;}
            x = x + 1;}
        cout << (n - kept) << endl;}
    return 0;}