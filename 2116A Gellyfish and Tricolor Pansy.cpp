#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    vector<vector<int>> rec(t, vector<int>(4));
    
    for (int i = 0; i < t; ++i) {
        cin >> rec[i][0] >> rec[i][1] >> rec[i][2] >> rec[i][3];
    }

    for (int i = 0; i < t; ++i) {
        int a = rec[i][0], b = rec[i][1], c = rec[i][2], d = rec[i][3];
        if (b <= a && b <= c) {
            cout << "Gellyfish" << endl;
        }
        else if (a < d) {
            cout << "Flower" << endl;
        }
        else if (d <= c) {
            cout << "Gellyfish" << endl;
        }
        else {
            cout << "Flower" << endl;
        }
    }

    return 0;
}
