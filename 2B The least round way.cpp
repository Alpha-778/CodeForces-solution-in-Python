#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits>
using namespace std;
const int MAX = 100000;
vector<vector<pair<int, int>>> matrix;
int power(int number, int base) {
    int p = 0;
    while (number % base == 0 && number != 0) {
        number /= base;
        p++;
    }
    return p;
}
int get_matrix(bool which, int r, int c) {
    return which ? matrix[r][c].second : matrix[r][c].first;
}
string find_path(int r, int c, bool which, const vector<vector<int>>& mx) {
    string path = "";
    while (r > 0 || c > 0) {
        if (r > 0 && mx[r][c] - get_matrix(which, r, c) == mx[r-1][c]) {
            r--;
            path = "D" + path;
        } else if (c > 0 && mx[r][c] - get_matrix(which, r, c) == mx[r][c-1]) {
            c--;
            path = "R" + path;
        }
    }
    return path;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    matrix.assign(n, vector<pair<int, int>>(n));
    vector<vector<int>> m2(n, vector<int>(n, MAX));
    vector<vector<int>> m5(n, vector<int>(n, MAX));
    bool zero = false;
    int zj = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int k;
            cin >> k;
            if (k == 0) {
                zero = true;
                zj = j;
                k = 10;
            }
            matrix[i][j] = { power(k, 2), power(k, 5) };
        }
    }
    m2[0][0] = matrix[0][0].first;
    m5[0][0] = matrix[0][0].second;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (j > 0) {
                m2[i][j] = min(m2[i][j], matrix[i][j].first + m2[i][j-1]);
                m5[i][j] = min(m5[i][j], matrix[i][j].second + m5[i][j-1]);
            }
            if (i > 0) {
                m2[i][j] = min(m2[i][j], matrix[i][j].first + m2[i-1][j]);
                m5[i][j] = min(m5[i][j], matrix[i][j].second + m5[i-1][j]);
            }
        }
    }
    int mini = min(m2[n-1][n-1], m5[n-1][n-1]);
    string path;
    if (zero && mini > 1) {
        mini = 1;
        path = string(zj, 'R') + string(n - 1, 'D') + string(n - 1 - zj, 'R');
    } else {
        if (m5[n-1][n-1] == mini) {
            path = find_path(n-1, n-1, true, m5);
        } else {
            path = find_path(n-1, n-1, false, m2);
        }
    }
    cout << (mini >= 0 ? mini : 1) << '\n';
    cout << path << '\n';
    return 0;
}