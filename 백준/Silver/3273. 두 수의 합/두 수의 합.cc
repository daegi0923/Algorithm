#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, k;
vector<int> v;
void input() {
    std::cin >> n;
    v.resize(n);
    for(int i=0;i < n;i++) {
        std::cin >> v[i];
    }
    std::cin >> k;
    sort(v.begin(), v.end());
}
void sol() {
    int cnt = 0, sum = 0, lo = 0, hi = n - 1;
    while(lo < hi) {
        sum = v[lo]+v[hi];
        if(sum > k)hi = hi - 1;
        else if(sum <k)lo = lo + 1;
        else {
            lo = lo + 1;
            hi = hi - 1;
            cnt = cnt + 1;
        }
    }
    cout << cnt;
}

int main() {
    input();
    sol();
    return 0;
}
