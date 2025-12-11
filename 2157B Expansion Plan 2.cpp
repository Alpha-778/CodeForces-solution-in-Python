#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        long long x, y;
        cin >> n >> x >> y;
        string s;
        cin >> s;
        long long c8 = 0;
        long long c4 = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '8') {
                c8++;
            } else {
                c4++;}}
        long long dx = llabs(x);
        long long dy = llabs(y);
        long long d = c8;
        if (d > dx) d = dx;
        if (d > dy) d = dy;
        long long rx = dx - d;
        long long ry = dy - d;
        long long need = rx + ry;
        long long left = c4 + (c8 - d);
        if (left >= need) {
            cout << "YES\n";
        } else {
            cout << "NO\n";}}
    return 0;}