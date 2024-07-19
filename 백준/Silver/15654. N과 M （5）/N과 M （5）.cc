#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int N,  M;
vector<int> v;
int visited[8];
int res[8];
void dfs(int k) {
    if(k == M) {
        for(int i = 0; i < M; i++) {
            cout << res[i] << " ";
        }
        cout << "\n";
    }
    for(int i = 0; i < N; i++) {
        if(!visited[i]) {
            res[k] = v[i];
            visited[i] = 1;
            dfs(k+1);
            visited[i] = 0;
        }
    }
}
int main() {
    cin >> N >> M;
    v.resize(N);
    fill(visited, visited+8, 0);
    for(int i = 0; i < N;  i ++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    dfs(0);
    return 0;
}
