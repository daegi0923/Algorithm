#include <iostream>
#include <vector>
#include <string>
using namespace std;
int N;
string alpha = "abcdefghijklmnopqrstuvwxyz";
int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        string str1, str2;
        int flag = 0;
        cin >> str1 >> str2;
        vector<int> v1(26, 0);
        vector<int> v2(26, 0);
        for(auto c:str1) {
            for(int j = 0; j < 26; j++) {
                if(alpha[j] == c) {
                    v1[j] = v1[j] + 1;
                }
            }
        }
        for(auto c:str2) {
            for(int j = 0; j < 26; j++) {
                if(alpha[j] == c) {
                    v2[j] = v2[j] + 1;
                }
            }
        }
        for(int i=0; i < 26; i++) {
            if(v1[i] != v2[i]) {
                flag = 1;
            }
        }
        if(flag) {
            cout << "Impossible"<<"\n";
        }
        else {
            cout << "Possible" <<"\n";
        }

    }
    return 0;
}
