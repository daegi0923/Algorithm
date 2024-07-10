#include <bits/stdc++.h>

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    std::string alpha = "abcdefghijklmnopqrstuvwxyz";
    vector<int> cnt(26);

    string str;
    cin >> str;
    for(int i = 0; i <26; i++) {
        cnt[i] = count(str.begin(), str.end(), alpha[i]);
        cout << cnt[i] << ' ';
    }
    for(int i = 0; i < 26; i++) {
        
    }
    return 0;
}
