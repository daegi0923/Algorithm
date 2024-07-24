#include <iostream>
#include <string>
#include <deque>
using namespace std;


int N, M;
string board[101];
int visited[101][101];
int di[4] = {0, 0, 1, -1};
int dj[4] = {1, -1, 0, 0};
void input() {
    cin >> N >> M;
    for(int i = 0; i < N;i++) {
        cin >> board[i];
        fill(visited[i], visited[i] + M, 0);
    }

}
void print() {
    for(int i=0; i < N ; i ++) {
        for(auto c : visited[i]) {
            cout << c << ' ';
        }
        cout << endl;
    }
}
void solve() {
    deque<pair<int,int>> dq;
    dq.push_back(make_pair(0, 0));
    visited[0][0] = 1;
    while(!dq.empty()) {
        int ci = dq.front().first;
        int cj = dq.front().second;
        dq.pop_front();
        for(int k = 0; k<4 ; k++) {
            int ni = ci + di[k];
            int nj = cj + dj[k];
            if(ni < 0|| N <= ni || nj < 0 || M <=nj) {
                continue;
            }
            if(board[ni][nj] == '0') {
                // cout << ni << ' ' << nj;
                continue;
            }
            if(visited[ni][nj]) {
                continue;
            }

            dq.push_back(make_pair(ni, nj));
            visited[ni][nj] = visited[ci][cj] + 1;
        }
    }
}

int main() {
#ifdef LOCAL_DEBUG
    freopen("input.txt", "r", stdin);
#endif

    input();
    solve();
    // print();
    cout << visited[N-1][M-1];

    return 0;
}