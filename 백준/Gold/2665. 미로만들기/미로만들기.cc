#include <iostream>
#include <queue>
#include <algorithm>
#include <string>


using namespace std;

int N;
string matrix[50];
int ans;
int INF = 987654321;
int cost_mat[50][50];
int visited[50][50];
int di[4] = {0, 0, 1, -1};
int dj[4] = {1, -1, 0, 0};


void input() {
    cin >> N;
    for(int i = 0 ; i < N; i ++) {
        fill(cost_mat[i], cost_mat[i]+N, INF);
        cin >> matrix[i];
        for(int j = 0; j < N; j++) {
            visited[i][j] = false;
        }
    }

}
void solve() {
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    cost_mat[0][0] = 0;
    pq.push({0, 0, 0});
    visited[0][0] = true;
    while(!pq.empty()) {
        int curr_cost = pq.top()[0];
        int i = pq.top()[1];
        int j = pq.top()[2];
        pq.pop();
        // cout << curr_cost<< " " <<i <<" "<< j <<endl;
        for(int k =0; k < 4; k++) {
            int ni = i + di[k];
            int nj = j + dj[k];
            if(ni >= N || ni < 0 || nj < 0 || nj >= N) {
                continue;
            }
            if(visited[ni][nj]) {
                continue;
            }
            int next_cost;
            if(matrix[ni][nj] == '1') {
                next_cost = curr_cost;
            }else {
                next_cost = curr_cost + 1;
            }
            if(cost_mat[ni][nj] > next_cost) {
                // cout << "next : "<<matrix[i][j] << " " << ni << " " << nj<<endl;
                pq.push({next_cost, ni, nj});
                cost_mat[ni][nj] = next_cost;
                visited[ni][nj] = true;
            }

        }
    }




}


int main() {
#ifdef LOCAL_DEBUG
    freopen("input.txt", "r", stdin);
#endif

    input();
    solve();
    cout << cost_mat[N-1][N-1];
}