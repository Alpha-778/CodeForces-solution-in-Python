#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        long long k;
        cin >> n >> k;
        if (n == 0) {
            cout << 0 << "\n";
            continue;}
        vector<long long> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];}
        sort(a.begin(), a.end());
        long long M = 0;
        int p = 0;
        long long x = a[0];
        long long c = 0;
        bool open = false;
        long long start = -1;
        while (p < n || c > 0) {
            long long f = 0;
            while (p < n && a[p] == x) {
                f++;
                p++;}
            long long y = c + f;
            if (y <= k) {
                if (open) {
                    if (x - start > M) M = x - start;
                    open = false;}
                c = 0;
                if (p < n && a[p] > x) {
                    x = a[p];
                } else {
                    x++;}
            } else {
                if (!open) {
                    open = true;
                    start = x;}
                c = y - 1;
                x++;}}
        cout << M << "\n";}
    return 0;}