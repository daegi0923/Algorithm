#include <bits/stdc++.h>
#include <climits>

#define INF INT_MAX
using namespace std;
vector <pair<int, int>> graph[2][1001];

int N, M, X;
// vector<vector<int>> cost(2, vector<int> (1001, INF));
vector<vector<int>> cost_matrix(2, vector<int>(1001, INF));

// vector <int> cost[2][1001];

void input() {
    cin >> N >> M >> X;
    int s, e, t;
    for(int i = 0; i < M; i++) {
        cin >> s >> e >> t;
        graph[1][e].push_back(make_pair(t, s));//역방향
        graph[0][s].push_back(make_pair(t, e));// 정방향
    }
    // for(int i = 0 ; i < N+1 ; i ++) {
    //     for(pair e:graph[i]) {
    //         cout << e.first <<e.second << ' ';
    //     }
    //     cout << '\n';
    // }
}
void solve() {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push(make_pair(0, X));
    cost_matrix[0][X] = 0;
    cost_matrix[1][X] = 0;
    // cout << pq.empty() << endl;
    while(!pq.empty()) {
        int cx = pq.top().second; // 현재 정점
        // cout << cx << endl;

        int cdst = pq.top().first; // 현재 정점까지 거리
        pq.pop();
        for(pair next:graph[0][cx]) {
            int nx = next.second;
            int ndst = next.first;
            // cout << ndst << ' ' << cdst << endl;
            if(cdst+ndst<cost_matrix[0][nx]) {
                cost_matrix[0][nx] = cdst+ndst;
                // cout << cost_matrix[0][nx] << endl;
                pq.push(make_pair(cdst+ndst, nx));
            }
        }
    }
    pq.push(make_pair(0, X));
    while(!pq.empty()) {
        int cx = pq.top().second; // 현재 정점
        // cout << cx << endl;

        int cdst = pq.top().first; // 현재 정점까지 거리
        pq.pop();
        for(pair next:graph[1][cx]) {
            int nx = next.second;
            int ndst = next.first;
            // cout << ndst << ' ' << cdst << endl;
            if(cdst+ndst<cost_matrix[1][nx]) {
                cost_matrix[1][nx] = cdst+ndst;
                // cout << cost_matrix[1][nx] << endl;
                pq.push(make_pair(cdst+ndst, nx));
            }
        }
    }
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    input();
    solve();
    int ans = 0;
    for(int i = 1; i < N+1; i++) {
        // cout << i  <<" "<< cost_matrix[0][i] << endl;
        // cout << i  <<" "<< cost_matrix[1][i] << endl;
        ans = max(ans, cost_matrix[0][i] + cost_matrix[1][i]);
    }
    cout << ans;
    return 0;
}
