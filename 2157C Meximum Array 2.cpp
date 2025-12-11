#include <iostream>
#include <vector>
int main() {
    int T;
    std::cin >> T;
    while (T--) {
        int n, k, q;
        std::cin >> n >> k >> q;
        std::vector<int> c(q);
        std::vector<int> l(q);
        std::vector<int> r(q);
        for (int i = 0; i < q; i++) {
            std::cin >> c[i] >> l[i] >> r[i];}
        std::vector<int> banned(n + 1, 0);
        std::vector<int> forbidden(n + 1, 0);
        for (int i = 0; i < q; i++) {
            if (c[i] == 1) {
                for (int j = l[i]; j <= r[i]; j++) {
                    banned[j] = 1;}
            } else {
                for (int j = l[i]; j <= r[i]; j++) {
                    forbidden[j] = 1;}}}
        int big = 1000000000;
        std::vector<int> a(n + 1, big);
        if (k > 0) {
            int count_free = 0;
            for (int i = 1; i <= n; i++) {
                if (banned[i] == 0) {
                    a[i] = count_free % k;
                    count_free++;}}}
        for (int i = 0; i < q; i++) {
            if (c[i] == 1) {
                int pos = -1;
                for (int j = l[i]; j <= r[i]; j++) {
                    if (forbidden[j] == 0) {
                        pos = j;
                        break;}}
                if (pos == -1) {
                    pos = l[i];}
                a[pos] = k;}}
        for (int i = 1; i <= n; i++) {
            if (i > 1) {
                std::cout << ' ';}
            std::cout << a[i];}
        std::cout << "\n";}
    return 0;}