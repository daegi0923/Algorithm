#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int N;
vector<int> vec;
vector<int> dp;
void input(){
    cin >> N;
    vec.resize(N);
    dp.assign(N, 1);
    for(int i=0; i<N; i++) {
        int num;
        cin >> num;
        vec[i] = num;
    }
    
}

void solve() {
    int ans = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<i; j++){
            if(vec[i] > vec[j]){
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
        ans = max(dp[i], ans);
    }
    cout << ans;

}

int main() {
#ifdef LOCAL_DEBUG
    freopen("input.txt", "r", stdin);
#endif

    input();
    solve();

    return 0;
}