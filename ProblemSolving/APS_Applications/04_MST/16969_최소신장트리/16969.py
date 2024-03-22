import sys

sys.stdin = open('input.txt')

import heapq



T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append([w, n2])
        graph[n2].append([w, n1])
    cost = 0
    visited = [0] * (V+1)
    hq = [[0, 0]]
    while hq:
        w, curr = heapq.heappop(hq)
        if not visited[curr]:
            visited[curr] = 1
            cost = cost + w
            for n in graph[curr]:
                if not visited[n[1]]:
                    heapq.heappush(hq, n)
    print(f'#{t} {cost}')
