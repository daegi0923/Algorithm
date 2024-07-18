#include <iostream>
#include <functional>
#include <queue>
using namespace std;
int N, E;
int v1, v2;
const int INF = 0x3f3f3f3f;
int d[801];
vector<vector<pair<int, int>>> graph;
void input() {
    cin >> N >> E;
    graph.resize(N+1);
    for(int i = 0;i < E; i++) {
        int start, end, cost;
        cin >> start >> end >> cost;
        graph[start].emplace_back(make_pair(cost, end));
        graph[end].emplace_back(make_pair(cost, start));
    }
    cin >> v1 >> v2;
}
int dijkstra(int start, int end) {
    if(start == end) {
        return 0;
    }
    priority_queue<pair<int, int>> pq;
    fill(d, d+N+1, INF);
    d[start] = 0;
    pq.push(make_pair(0, start));
    while(!pq.empty()) {
        auto curr = pq.top();pq.pop();
        for(auto nxt:graph[curr.second]) {
            if(d[nxt.second] > nxt.first + curr.first) {
                d[nxt.second] = nxt.first + d[curr.second];
                pq.push(make_pair(nxt.first + d[curr.second], nxt.second));
            }
        }
    }
    if(d[end] < 9876000) {
        return d[end];
    } else {
        return INF;
    }
}
int main() {
    input();
    int res1, res2;
    if(dijkstra(1, v1) < INF && dijkstra(v1, v2) < INF && dijkstra(v2, N) < INF) {
        res1 = dijkstra(1, v1) + dijkstra(v1, v2)+ dijkstra(v2, N);
    }
    else {
        res1 = -1;
    }
    if(dijkstra(1, v2) <INF && dijkstra(v2, v1)<INF && dijkstra(v1, N) < INF) {
        res2 = dijkstra(1, v2) + dijkstra(v2, v1)+ dijkstra(v1, N);
    }
    else {
        res2 = -1;
    }
    if (res1 < 0 && res2 < 0) {
        cout << -1;
    } else if(res1 < 0 || res2 < 0){
        cout << max(res1, res2);

    }else {
        cout << min(res1, res2);
    }
    return 0;
}