import sys

input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append([r, q])
    graph[q].append([r, p])
for _ in range(Q):
    k, v = map(int, input().split())
    queue = deque([[float('inf'), v]])
    visited = [0] * (N+1)
    visited[v] = 1
    ans = 0
    while queue:
        cost, curr = queue.popleft()
        if graph[curr]:
            for next_node in graph[curr]:
                nc, nn = next_node
                if min(cost, nc) >= k and not visited[nn]:
                    visited[nn] = 1
                    ans = ans + 1
                    queue.append([min(cost, nc), nn])
    print(ans)