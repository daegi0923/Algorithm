#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;


int N;
vector<int> vec;


void input() {
    cin >> N;
    vec.resize(N);
    for(int i=0;i<N;i++) {
        cin >> vec[i];
    }
    sort(vec.begin(), vec.end());

}

void solve() {
    vector ans = {0, 1, N-1};
    long long local_ans = (long long)vec[0]+ vec[1] + vec[N-1];
    for(int i = 0; i<N; i++) {
        int start = i+1;
        int end = N-1;
        while(start<end) {
            long long  sum = (long long)vec[i] + vec[start] + vec[end];
            if(abs(sum) <abs(local_ans)) {
                local_ans = abs(sum);
                ans[0] = i;
                ans[1] = start;
                ans[2] = end;
            }
            if(sum < 0) {
                start = start + 1;
            }
            else if(sum > 0) {
                end = end - 1;
            }
            else {
                break;
            }
        }
    }
    // for(auto i:vec) {
    //     cout << i << ' ';
    // }
    // cout << endl;
    // for(auto i:ans) {
    //     cout << i << " ";
    // }
    // cout << endl;
    cout << vec[ans[0]] << " " << vec[ans[1]] <<" "<< vec[ans[2]];
}


int main()
{
    input();
    solve();
    return 0;
}