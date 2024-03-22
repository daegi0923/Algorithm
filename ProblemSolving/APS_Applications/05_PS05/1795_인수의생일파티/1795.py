import sys

sys.stdin = open('input.txt')

import heapq

def dijkstra(s, tmp):
    cost_mat = [float('inf')] * (N+1)
    hq = [[0, s]]
    cost_mat[s] = 0
    while hq:
        c_weight, curr = heapq.heappop(hq)
        for nexts in tmp[curr]:
            n_weight, nxt = nexts
            if n_weight + c_weight < cost_mat[nxt]:
                heapq.heappush(hq, [n_weight+c_weight, nxt])
                cost_mat[nxt] = n_weight + c_weight
    return cost_mat

T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    r_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append([c, y])
        r_graph[y].append([c, x])

    # print(graph)
    ans = 0
    res = dijkstra(X, graph)
    res2 = dijkstra(X, r_graph)
    # print(res)
    # print(res2)
    for start in range(1, N+1):
        local_sum = res[start]+res2[start]
        ans = max(local_sum, ans)
    print(f'#{t} {ans}')