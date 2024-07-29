#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

int N, M;
vector<string> board;
vector<vector<int>> fire_visited;
vector<vector<int>> j_visited;

int di[] = {0, 0, 1, -1};
int dj[] = {1, -1, 0, 0};

void input() {
    cin >> N >> M;
    fire_visited.assign(N, vector<int>(M, -1));
    j_visited.assign(N, vector<int>(M, -1));
    board.resize(N);
    for(int i = 0; i < N; i++) {
        cin >> board[i];
    }
}

int solve() {
    int ans = -1;
    deque<pair<int, int>> fire_queue;
    deque<pair<int, int>> joe_queue;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(board[i][j] == 'J') {
                joe_queue.emplace_back(i, j);
                j_visited[i][j] = 0;
            }
            if(board[i][j] == 'F') {
                fire_queue.emplace_back(i, j);
                fire_visited[i][j] = 0;
            }
        }
    }

    while(!fire_queue.empty()) {
        auto [fi, fj] = fire_queue.front();
        fire_queue.pop_front();
        for(int d = 0; d < 4; d++) {
            int ni = fi + di[d];
            int nj = fj + dj[d];
            if(ni < 0 || N <= ni || nj < 0 || M <= nj) {
                continue;
            }
            if(board[ni][nj] == '#') {
                continue;
            }
            if(fire_visited[ni][nj] > -1) {
                continue;
            }
            fire_queue.emplace_back(ni, nj);
            fire_visited[ni][nj] = fire_visited[fi][fj] + 1;
        }
    }

    while(!joe_queue.empty()) {
        auto [ci, cj] = joe_queue.front();
        joe_queue.pop_front();
        for(int d = 0; d < 4; d++) {
            int ni = ci + di[d];
            int nj = cj + dj[d];
            if(ni < 0 || N <= ni || nj < 0 || M <= nj) {
                ans = j_visited[ci][cj] + 1;
                return ans;
            }
            if(board[ni][nj] == '#') {
                continue;
            }
            if(j_visited[ni][nj] > -1) {
                continue;
            }
            if(fire_visited[ni][nj] != -1 && fire_visited[ni][nj] <= j_visited[ci][cj] + 1) {
                continue;
            }
            joe_queue.emplace_back(ni, nj);
            j_visited[ni][nj] = j_visited[ci][cj] + 1;
        }
    }

    return -1;
}

int main() {
#ifdef LOCAL_DEBUG
    freopen("input.txt", "r", stdin);
#endif

    input();
    int ans = solve();
    if(ans == -1) {
        cout << "IMPOSSIBLE";
    } else {
        cout << ans;
    }

    return 0;
}
