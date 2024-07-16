#include <iostream>
#include <vector>
using namespace std;
int N, K;
int ans = 0;
int main() {
    cin >> N >> K;
    vector<vector<int>> mat(7, vector<int>(2, 0));
    for(int i = 0; i < N; i++) {
        int S, Y;
        cin >> S >> Y;
        mat[Y][S] = mat[Y][S] + 1;
    }
    for(auto v : mat) {
        for(auto i:v) {
            ans = ans + i/K;
            if(i%K) {
                ans = ans + 1;
            }
        }
    }
    cout << ans;
    return 0;
}
